#!/usr/bin/env python3
"""Score frozen matured forecasts with proper scores and benchmark comparison."""

import argparse
import json
import re
from pathlib import Path


QUANTILE_PATTERN = re.compile(r"^p(\d{1,2}|100)$")


def brier(rows, probability_key):
    values = [(float(row[probability_key]) - int(row["outcome"])) ** 2 for row in rows if probability_key in row]
    return sum(values) / len(values) if values else None


def ranked_probability_score(probabilities, outcome_index):
    if len(probabilities) < 2 or not 0 <= outcome_index < len(probabilities):
        raise ValueError("categorical probabilities need at least two classes and a valid outcome_index")
    if any(value < 0 for value in probabilities) or abs(sum(probabilities) - 1) > 1e-6:
        raise ValueError("categorical probabilities must be non-negative and sum to 1")
    cumulative_forecast = 0.0
    score = 0.0
    for index in range(len(probabilities) - 1):
        cumulative_forecast += probabilities[index]
        cumulative_outcome = 1.0 if outcome_index <= index else 0.0
        score += (cumulative_forecast - cumulative_outcome) ** 2
    return score / (len(probabilities) - 1)


def skill_score(model, benchmark):
    return 1 - model / benchmark if model is not None and benchmark not in (None, 0) else None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("records", type=Path)
    parser.add_argument("--strict", action="store_true", help="require immutable-record provenance fields")
    args = parser.parse_args()
    records = json.loads(args.records.read_text(encoding="utf-8"))
    if not isinstance(records, list) or not records:
        raise SystemExit("records must be a non-empty JSON array")
    required_strict = ("id", "issued_at", "source_cutoff", "maturity_time", "model_version", "benchmark_probability")
    squared = []
    benchmark_squared = []
    bins = {"0-20": [], "20-40": [], "40-60": [], "60-80": [], "80-100": []}
    categorical_scores = []
    categorical_benchmarks = []
    quantile_rows = []
    for row in records:
        if args.strict:
            missing = [field for field in required_strict if row.get(field) in (None, "")]
            if missing:
                raise SystemExit(f"strict record missing: {', '.join(missing)}")
        probability = float(row["probability"])
        outcome = int(row["outcome"])
        if not 0 <= probability <= 1 or outcome not in (0, 1):
            raise SystemExit("probability must be 0..1 and outcome 0 or 1")
        squared.append((probability - outcome) ** 2)
        if "benchmark_probability" in row:
            benchmark_probability = float(row["benchmark_probability"])
            if not 0 <= benchmark_probability <= 1:
                raise SystemExit("benchmark_probability must be 0..1")
            benchmark_squared.append((benchmark_probability - outcome) ** 2)
        index = min(4, int(probability * 5))
        bins[list(bins)[index]].append((probability, outcome))
        if "probabilities" in row or "outcome_index" in row:
            if "probabilities" not in row or "outcome_index" not in row:
                raise SystemExit("probabilities and outcome_index must be supplied together")
            try:
                categorical_scores.append(ranked_probability_score([float(value) for value in row["probabilities"]], int(row["outcome_index"])))
                if "benchmark_probabilities" in row:
                    categorical_benchmarks.append(ranked_probability_score([float(value) for value in row["benchmark_probabilities"]], int(row["outcome_index"])))
                elif args.strict:
                    raise SystemExit("strict categorical records require benchmark_probabilities")
            except ValueError as exc:
                raise SystemExit(str(exc)) from exc
        if "quantiles" in row or "realized" in row:
            if not isinstance(row.get("quantiles"), dict) or "realized" not in row:
                raise SystemExit("quantiles and realized must be supplied together")
            realized = float(row["realized"])
            benchmark_quantiles = row.get("benchmark_quantiles")
            if args.strict and not isinstance(benchmark_quantiles, dict):
                raise SystemExit("strict quantile records require benchmark_quantiles")
            for name, raw_value in row["quantiles"].items():
                match = QUANTILE_PATTERN.fullmatch(name)
                if not match:
                    raise SystemExit(f"invalid quantile name: {name}")
                level = int(match.group(1)) / 100
                if not 0 < level < 1:
                    raise SystemExit("quantile levels must be between p1 and p99")
                forecast = float(raw_value)
                error = realized - forecast
                pinball = max(level * error, (level - 1) * error)
                benchmark_pinball = None
                if benchmark_quantiles is not None:
                    if name not in benchmark_quantiles:
                        raise SystemExit(f"benchmark_quantiles missing {name}")
                    benchmark_error = realized - float(benchmark_quantiles[name])
                    benchmark_pinball = max(level * benchmark_error, (level - 1) * benchmark_error)
                quantile_rows.append((name, level, realized <= forecast, pinball, benchmark_pinball))
    calibration = {}
    for name, values in bins.items():
        if values:
            calibration[name] = {
                "count": len(values),
                "mean_forecast": sum(p for p, _ in values) / len(values),
                "observed_rate": sum(o for _, o in values) / len(values),
            }
    brier_score = sum(squared) / len(squared)
    benchmark_brier = sum(benchmark_squared) / len(benchmark_squared) if benchmark_squared else None
    quantiles = {}
    for name in sorted({row[0] for row in quantile_rows}, key=lambda value: int(value[1:])):
        values = [row for row in quantile_rows if row[0] == name]
        quantiles[name] = {
            "count": len(values),
            "nominal_coverage": values[0][1],
            "observed_below_or_equal_rate": sum(row[2] for row in values) / len(values),
            "mean_pinball_loss": sum(row[3] for row in values) / len(values),
            "benchmark_mean_pinball_loss": sum(row[4] for row in values) / len(values) if all(row[4] is not None for row in values) else None,
        }
        quantiles[name]["pinball_skill_score"] = skill_score(quantiles[name]["mean_pinball_loss"], quantiles[name]["benchmark_mean_pinball_loss"])
    rps = sum(categorical_scores) / len(categorical_scores) if categorical_scores else None
    benchmark_rps = sum(categorical_benchmarks) / len(categorical_benchmarks) if categorical_benchmarks else None
    print(json.dumps({
        "count": len(records),
        "brier_score": brier_score,
        "benchmark_brier_score": benchmark_brier,
        "brier_skill_score": skill_score(brier_score, benchmark_brier),
        "calibration_bins": calibration,
        "ranked_probability_score": rps,
        "benchmark_ranked_probability_score": benchmark_rps,
        "rps_skill_score": skill_score(rps, benchmark_rps),
        "quantile_evaluation": quantiles,
        "warnings": [
            "Calibration conclusions require enough comparable matured forecasts.",
            "Benchmark comparisons are valid only when forecasts and benchmarks were frozen under the same outcome rule before maturity.",
        ],
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
