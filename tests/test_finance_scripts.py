#!/usr/bin/env python3
"""Deterministic regression tests for the finance skill calculators."""

from __future__ import annotations

import csv
import json
import math
import subprocess
import sys
import tempfile
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1] / "skills" / "common"


def run(skill: str, script: str, *arguments: str, expected_code: int = 0):
    command = [sys.executable, str(ROOT / skill / "scripts" / script), *map(str, arguments)]
    result = subprocess.run(command, text=True, encoding="utf-8", capture_output=True, check=False)
    if result.returncode != expected_code:
        raise AssertionError(f"{command} returned {result.returncode}: {result.stderr}\n{result.stdout}")
    return json.loads(result.stdout) if result.stdout else None


def approx(actual, expected, tolerance=1e-8):
    if not math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance):
        raise AssertionError(f"expected {expected}, got {actual}")


def main():
    with tempfile.TemporaryDirectory() as temporary:
        temp = Path(temporary)

        fund_csv = temp / "fund.csv"
        with fund_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["date", "value", "benchmark"])
            writer.writeheader()
            writer.writerows([
                {"date": "2026-01-01", "value": 100, "benchmark": 100},
                {"date": "2026-01-02", "value": 110, "benchmark": 105},
                {"date": "2026-01-03", "value": 121, "benchmark": 110.25},
            ])
        fund = run("fund-etf-analyst", "fund_metrics.py", fund_csv, "--benchmark-column", "benchmark")
        approx(fund["total_return"], 0.21)
        approx(fund["benchmark"]["total_return"], 0.1025)

        warrant = run(
            "warrant-structured-product-analyst", "warrant_model.py",
            "--option-type", "call", "--spot", "100", "--strike", "100", "--days-to-expiry", "365",
            "--volatility", "0.2", "--underlying-units-per-warrant", "1", "--quoted-warrant-price", "8",
            "--scenario-spots", "80,100,120",
        )
        approx(warrant["modeled_warrant_value"], 7.965567455405804, tolerance=1e-7)
        assert len(warrant["scenario_grid"]) == 3

        portfolio_packet = temp / "portfolio.json"
        portfolio_packet.write_text(json.dumps({
            "portfolio_value": 100000,
            "cash": 50000,
            "max_daily_participation": 0.1,
            "limits": {"max_position_weight": 0.4, "max_issuer_weight": 0.5, "max_sector_weight": 0.5},
            "positions": [
                {"id": "AAA", "market_value": 30000, "issuer": "A", "sector": "Tech", "country": "TR", "currency": "TRY", "asset_class": "Equity", "strategy": "Core", "average_daily_traded_value": 300000, "scenarios": {"bear": -0.2, "bull": 0.1}},
                {"id": "FUND", "market_value": 20000, "issuer": "F", "sector": "Mixed", "country": "TR", "currency": "TRY", "asset_class": "Fund", "strategy": "Core", "lookthrough": [{"name": "AAA", "weight": 0.25}, {"name": "BBB", "weight": 0.75}], "scenarios": {"bear": -0.1, "bull": 0.05}},
            ],
        }), encoding="utf-8")
        portfolio = run("portfolio-risk-and-sizing", "portfolio_exposure.py", portfolio_packet)
        approx(portfolio["net_exposure"], 0.5)
        approx(portfolio["scenario_pnl"][0]["pnl"], -8000)
        assert portfolio["limit_breaches"] == []

        valid_gate = {
            "identity": {"name": "Example", "identifier": "EX", "venue": "X", "currency": "TRY", "product_type": "equity"},
            "decision": "BUY", "direction": "long", "horizon": "3 months", "evidence_cutoff": "2026-08-20T12:00:00+03:00",
            "entry": {"order_type": "limit", "price": 100, "source": "exchange", "timestamp": "2026-08-20T12:00:00+03:00", "market_status": "open"},
            "thesis": "Dated test thesis", "invalidation": "KPI fails", "exit_plan": "Review at result",
            "scenario": {"bear": -0.2, "base": 0.1, "bull": 0.3, "stress_loss": 2000},
            "size": {"quantity": 100, "cash_or_notional": 10000, "max_modeled_loss": 2000, "loss_limit": 2500, "post_trade_weight": 0.1},
            "costs": {"fees": 10, "spread": 0.002, "slippage_status": "modeled", "tax_status": "verified_or_not_applicable"},
            "liquidity": "adequate", "settlement": "verified", "portfolio_fit": {"checked": True},
            "evidence_guard": {"status": "PASS"}, "red_team": {"status": "PASS"}, "product_checks": {"ordinary_equity_terms": True}, "conditions": [],
        }
        gate_packet = temp / "gate.json"
        gate_packet.write_text(json.dumps(valid_gate), encoding="utf-8")
        assert run("pre-trade-investment-gate", "validate_pretrade.py", gate_packet)["status"] == "READY"
        conditional = dict(valid_gate)
        conditional["conditions"] = ["limit price at or below 100"]
        gate_packet.write_text(json.dumps(conditional), encoding="utf-8")
        assert run("pre-trade-investment-gate", "validate_pretrade.py", gate_packet, expected_code=2)["status"] == "READY WITH CONDITIONS"
        incomplete = dict(valid_gate)
        incomplete.pop("entry")
        gate_packet.write_text(json.dumps(incomplete), encoding="utf-8")
        assert run("pre-trade-investment-gate", "validate_pretrade.py", gate_packet, expected_code=1)["status"] == "NOT READY"

        journal_csv = temp / "journal.csv"
        with journal_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["trade_id", "pnl_after_costs", "planned_risk", "process_followed", "strategy", "forecast_probability", "forecast_outcome"])
            writer.writeheader()
            writer.writerows([
                {"trade_id": "1", "pnl_after_costs": 100, "planned_risk": 100, "process_followed": "true", "strategy": "A", "forecast_probability": 0.7, "forecast_outcome": 1},
                {"trade_id": "2", "pnl_after_costs": -100, "planned_risk": 100, "process_followed": "true", "strategy": "A", "forecast_probability": 0.6, "forecast_outcome": 0},
                {"trade_id": "3", "pnl_after_costs": 200, "planned_risk": 100, "process_followed": "false", "strategy": "B", "forecast_probability": 0.8, "forecast_outcome": 1},
                {"trade_id": "4", "pnl_after_costs": -50, "planned_risk": 100, "process_followed": "true", "strategy": "B", "forecast_probability": 0.4, "forecast_outcome": 0},
            ])
        journal = run("investment-journal-review", "journal_metrics.py", journal_csv)
        approx(journal["overall"]["average_r"], 0.375)
        approx(journal["overall"]["process_adherence"], 0.75)

        real = run("financial-literacy-coach", "finance_calculator.py", "real-return", "--nominal-return", "0.10", "--inflation", "0.05")
        approx(real["result"]["real_return"], 1.10 / 1.05 - 1)
        negative = run("financial-literacy-coach", "finance_calculator.py", "real-return", "--nominal-return", "-0.10", "--inflation", "0.05")
        approx(negative["result"]["real_return"], 0.90 / 1.05 - 1)
        compounded = run("financial-literacy-coach", "finance_calculator.py", "compound", "--principal", "100", "--annual-return", "0.10", "--years", "1", "--periods-per-year", "1")
        approx(compounded["result"]["future_value"], 110)

        regime_csv = temp / "regime.csv"
        with regime_csv.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=["date", "close", "volume", "advances", "declines"])
            writer.writeheader()
            for index in range(65):
                writer.writerow({"date": (date(2026, 1, 1) + timedelta(days=index)).isoformat(), "close": 100 + index, "volume": 1000 + index, "advances": 60, "declines": 40})
        regime = run("market-regime-analysis", "regime_features.py", regime_csv)
        approx(regime["advance_share"], 0.6)
        assert regime["sma60"] is not None

        forecasts = temp / "forecasts.json"
        base_record = {"issued_at": "2026-01-01T00:00:00Z", "source_cutoff": "2025-12-31T23:59:59Z", "maturity_time": "2026-02-01T00:00:00Z", "model_version": "1"}
        forecasts.write_text(json.dumps([
            {**base_record, "id": "f1", "probability": 0.8, "outcome": 1, "benchmark_probability": 0.5, "probabilities": [0.1, 0.2, 0.7], "benchmark_probabilities": [1/3, 1/3, 1/3], "outcome_index": 2, "quantiles": {"p10": -0.2, "p50": 0.05, "p90": 0.3}, "benchmark_quantiles": {"p10": -0.25, "p50": 0.0, "p90": 0.25}, "realized": 0.1},
            {**base_record, "id": "f2", "probability": 0.2, "outcome": 0, "benchmark_probability": 0.5, "probabilities": [0.7, 0.2, 0.1], "benchmark_probabilities": [1/3, 1/3, 1/3], "outcome_index": 0, "quantiles": {"p10": -0.1, "p50": 0.03, "p90": 0.2}, "benchmark_quantiles": {"p10": -0.2, "p50": 0.0, "p90": 0.2}, "realized": -0.05},
        ]), encoding="utf-8")
        scored = run("probabilistic-market-forecast", "score_forecasts.py", forecasts, "--strict")
        approx(scored["brier_score"], 0.04)
        approx(scored["benchmark_brier_score"], 0.25)
        approx(scored["brier_skill_score"], 0.84)
        assert scored["ranked_probability_score"] is not None and scored["quantile_evaluation"]["p50"]["count"] == 2

    print(json.dumps({"status": "PASS", "scripts_tested": 8}, indent=2))


if __name__ == "__main__":
    main()
