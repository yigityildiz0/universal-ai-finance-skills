#!/usr/bin/env python3
"""Compute common indicators from a validated OHLCV CSV using stdlib only."""

import argparse
import csv
import json
from pathlib import Path


def sma(values, window):
    return sum(values[-window:]) / window if len(values) >= window else None


def ema_series(values, window):
    if len(values) < window:
        return []
    alpha = 2 / (window + 1)
    result = [sum(values[:window]) / window]
    for value in values[window:]:
        result.append(alpha * value + (1 - alpha) * result[-1])
    return result


def rsi(values, window=14):
    if len(values) <= window:
        return None
    changes = [values[i] - values[i - 1] for i in range(1, len(values))]
    gains = [max(0.0, value) for value in changes]
    losses = [max(0.0, -value) for value in changes]
    avg_gain = sum(gains[:window]) / window
    avg_loss = sum(losses[:window]) / window
    for gain, loss in zip(gains[window:], losses[window:]):
        avg_gain = (avg_gain * (window - 1) + gain) / window
        avg_loss = (avg_loss * (window - 1) + loss) / window
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return 100 - 100 / (1 + rs)


def atr(highs, lows, closes, window=14):
    if len(closes) <= window:
        return None
    true_ranges = []
    for i in range(1, len(closes)):
        true_ranges.append(max(highs[i] - lows[i], abs(highs[i] - closes[i - 1]), abs(lows[i] - closes[i - 1])))
    value = sum(true_ranges[:window]) / window
    for current in true_ranges[window:]:
        value = (value * (window - 1) + current) / window
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_file", type=Path)
    parser.add_argument("--complete-column", default="complete")
    args = parser.parse_args()

    rows = []
    with args.csv_file.open(encoding="utf-8-sig", newline="") as handle:
        for row in csv.DictReader(handle):
            if args.complete_column in row and row[args.complete_column].strip().lower() in {"0", "false", "no"}:
                continue
            parsed = {key: float(row[key]) for key in ("open", "high", "low", "close", "volume")}
            parsed["date"] = row["date"]
            if parsed["high"] < max(parsed["open"], parsed["close"], parsed["low"]) or parsed["low"] > min(parsed["open"], parsed["close"], parsed["high"]):
                raise SystemExit(f"invalid OHLC row: {row['date']}")
            if min(parsed["open"], parsed["high"], parsed["low"], parsed["close"]) <= 0 or parsed["volume"] < 0:
                raise SystemExit(f"non-positive price or negative volume: {row['date']}")
            rows.append(parsed)
    if len(rows) < 27:
        raise SystemExit("need at least 27 complete candles")
    if [row["date"] for row in rows] != sorted(row["date"] for row in rows) or len({row["date"] for row in rows}) != len(rows):
        raise SystemExit("dates must be unique and ascending ISO strings")

    closes = [row["close"] for row in rows]
    highs = [row["high"] for row in rows]
    lows = [row["low"] for row in rows]
    volumes = [row["volume"] for row in rows]
    ema12 = ema_series(closes, 12)
    ema26 = ema_series(closes, 26)
    offset = len(ema12) - len(ema26)
    macd_series = [ema12[i + offset] - ema26[i] for i in range(len(ema26))]
    signal = ema_series(macd_series, 9)
    last = closes[-1]
    atr14 = atr(highs, lows, closes)
    output = {
        "as_of": rows[-1]["date"],
        "candles": len(rows),
        "close": last,
        "sma20": sma(closes, 20),
        "sma50": sma(closes, 50),
        "sma200": sma(closes, 200),
        "ema12": ema12[-1],
        "ema26": ema26[-1],
        "macd": macd_series[-1],
        "macd_signal": signal[-1] if signal else None,
        "rsi14": rsi(closes),
        "atr14": atr14,
        "atr_pct": atr14 / last * 100 if atr14 else None,
        "volume_sma20": sma(volumes, 20),
        "distance_sma20_pct": (last / sma(closes, 20) - 1) * 100 if sma(closes, 20) else None,
        "distance_sma50_pct": (last / sma(closes, 50) - 1) * 100 if sma(closes, 50) else None,
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
