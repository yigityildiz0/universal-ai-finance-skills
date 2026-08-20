#!/usr/bin/env python3
"""Aggregate transparent portfolio exposures, liquidity, limits and scenarios."""

import argparse
import json
from collections import defaultdict
from pathlib import Path


GROUPS = ("issuer", "sector", "country", "currency", "asset_class", "strategy")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("packet", type=Path)
    args = parser.parse_args()
    packet = json.loads(args.packet.read_text(encoding="utf-8"))
    nav = float(packet.get("portfolio_value", 0))
    cash = float(packet.get("cash", 0))
    positions = packet.get("positions")
    if nav <= 0 or not isinstance(positions, list):
        raise SystemExit("portfolio_value must be positive and positions must be a list")

    group_signed = {group: defaultdict(float) for group in GROUPS}
    group_absolute = {group: defaultdict(float) for group in GROUPS}
    lookthrough = defaultdict(float)
    scenario_pnl = defaultdict(float)
    position_rows = []
    warnings = []
    seen = set()
    for index, position in enumerate(positions):
        identifier = str(position.get("id", "")).strip()
        if not identifier or identifier in seen:
            raise SystemExit(f"position {index} needs a unique id")
        seen.add(identifier)
        value = float(position.get("market_value", 0))
        if value == 0:
            raise SystemExit(f"position {identifier} market_value cannot be zero")
        weight = value / nav
        row = {"id": identifier, "market_value": value, "weight": weight, "absolute_weight": abs(weight)}
        for group in GROUPS:
            label = str(position.get(group, "UNKNOWN")).strip() or "UNKNOWN"
            group_signed[group][label] += value
            group_absolute[group][label] += abs(value)

        holdings = position.get("lookthrough", [])
        if holdings:
            if not isinstance(holdings, list):
                raise SystemExit(f"position {identifier} lookthrough must be a list")
            total_weight = 0.0
            for holding in holdings:
                label = str(holding.get("name", "")).strip()
                holding_weight = float(holding.get("weight", -1))
                if not label or not 0 <= holding_weight <= 1:
                    raise SystemExit(f"position {identifier} has invalid lookthrough item")
                total_weight += holding_weight
                lookthrough[label] += value * holding_weight
            if total_weight > 1.000001:
                raise SystemExit(f"position {identifier} lookthrough weights exceed 1")
            if total_weight < 0.95:
                warnings.append(f"{identifier} lookthrough covers only {total_weight:.1%}")

        adv = position.get("average_daily_traded_value")
        participation = float(packet.get("max_daily_participation", 0.10))
        if adv is not None:
            adv = float(adv)
            if adv <= 0 or not 0 < participation <= 1:
                raise SystemExit("average_daily_traded_value must be positive and participation 0..1")
            row["estimated_exit_days"] = abs(value) / (adv * participation)

        scenarios = position.get("scenarios", {})
        if not isinstance(scenarios, dict):
            raise SystemExit(f"position {identifier} scenarios must be an object")
        for name, scenario_return in scenarios.items():
            scenario_pnl[name] += value * float(scenario_return)
        position_rows.append(row)

    position_rows.sort(key=lambda row: row["absolute_weight"], reverse=True)
    gross = sum(abs(row["market_value"]) for row in position_rows) / nav
    net = sum(row["market_value"] for row in position_rows) / nav
    concentration_index = sum(row["absolute_weight"] ** 2 for row in position_rows)

    limits = packet.get("limits", {})
    if not isinstance(limits, dict):
        raise SystemExit("limits must be an object")
    breaches = []
    max_position = limits.get("max_position_weight")
    if max_position is not None:
        if float(max_position) <= 0:
            raise SystemExit("max_position_weight must be positive")
        breaches.extend(f"position:{row['id']}" for row in position_rows if row["absolute_weight"] > float(max_position))
    for group, limit_name in (("issuer", "max_issuer_weight"), ("sector", "max_sector_weight")):
        limit = limits.get(limit_name)
        if limit is not None:
            if float(limit) <= 0:
                raise SystemExit(f"{limit_name} must be positive")
            breaches.extend(f"{group}:{label}" for label, value in group_absolute[group].items() if value / nav > float(limit))

    groups = {}
    for group in GROUPS:
        labels = set(group_signed[group]) | set(group_absolute[group])
        groups[group] = sorted(({
            "name": label,
            "signed_weight": group_signed[group][label] / nav,
            "gross_weight": group_absolute[group][label] / nav,
        } for label in labels), key=lambda row: row["gross_weight"], reverse=True)

    result = {
        "portfolio_value": nav,
        "cash": cash,
        "cash_weight": cash / nav,
        "net_exposure": net,
        "gross_exposure": gross,
        "position_concentration_index": concentration_index,
        "positions": position_rows,
        "group_exposures": groups,
        "lookthrough_exposures": sorted(({"name": label, "weight": value / nav} for label, value in lookthrough.items()), key=lambda row: abs(row["weight"]), reverse=True),
        "scenario_pnl": [{"scenario": name, "pnl": value, "return_on_portfolio": value / nav} for name, value in sorted(scenario_pnl.items())],
        "limit_breaches": sorted(set(breaches)),
        "warnings": warnings + ["Scenario returns, holdings and liquidity are user-supplied inputs; this script does not verify live data or correlation stability."],
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
