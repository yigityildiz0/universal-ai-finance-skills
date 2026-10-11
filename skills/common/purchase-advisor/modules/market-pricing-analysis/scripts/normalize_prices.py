#!/usr/bin/env python3
"""Normalize landed prices and transparent value scores from JSON offers."""

import argparse
import json
import math
from pathlib import Path


def nonnegative_number(offer, key, default=None):
    raw = offer.get(key, default)
    try:
        value = float(raw)
    except (TypeError, ValueError):
        raise SystemExit(f"{key} must be a finite non-negative number")
    if isinstance(raw, bool) or not math.isfinite(value) or value < 0:
        raise SystemExit(f"{key} must be a finite non-negative number")
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("offers", type=Path)
    parser.add_argument("--base-currency", required=True)
    args = parser.parse_args()
    offers = json.loads(args.offers.read_text(encoding="utf-8"))
    if not isinstance(offers, list) or not offers:
        raise SystemExit("offers must be a non-empty JSON array")

    rows = []
    for offer in offers:
        if not isinstance(offer, dict):
            raise SystemExit("each offer must be a JSON object")
        required = {"name", "price", "currency", "fx_to_base", "quantity", "quantity_unit"}
        missing = required - offer.keys()
        if missing:
            raise SystemExit(f"{offer.get('name', 'offer')} missing {sorted(missing)}")
        price = nonnegative_number(offer, "price")
        tax = nonnegative_number(offer, "tax", 0)
        shipping = nonnegative_number(offer, "shipping", 0)
        mandatory_fees = nonnegative_number(offer, "mandatory_fees", 0)
        discount = nonnegative_number(offer, "discount", 0)
        quantity = nonnegative_number(offer, "quantity")
        fx = nonnegative_number(offer, "fx_to_base")
        if price < 0 or quantity <= 0 or fx <= 0:
            raise SystemExit("price must be non-negative; quantity and fx_to_base positive")
        landed = (price + tax + shipping + mandatory_fees - discount) * fx
        unit_price = landed / quantity
        if landed < 0 or not math.isfinite(landed) or not math.isfinite(unit_price):
            raise SystemExit("landed/unit price must be finite and non-negative; check fees and discount")
        quality = offer.get("quality_score")
        quality = nonnegative_number(offer, "quality_score") if quality is not None else None
        value = quality / unit_price if quality is not None and unit_price > 0 else None
        if value is not None and not math.isfinite(value):
            raise SystemExit("value score overflow; check quality score and unit price")
        rows.append({
            "name": offer["name"],
            "base_currency": args.base_currency,
            "landed_price": landed,
            "normalized_unit_price": unit_price,
            "quantity_unit": offer["quantity_unit"],
            "quality_score": quality,
            "value_score": value,
            "fx_timestamp": offer.get("fx_timestamp"),
            "observed_at": offer.get("observed_at"),
        })
    price_rank = sorted(rows, key=lambda row: row["normalized_unit_price"])
    value_rank = sorted([row for row in rows if row["value_score"] is not None], key=lambda row: row["value_score"], reverse=True)
    print(json.dumps({
        "offers": rows,
        "cheapest_normalized": [row["name"] for row in price_rank],
        "best_value_when_scored": [row["name"] for row in value_rank],
        "warning": "Value ranking is only as valid as the explicit quality scores and weights.",
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
