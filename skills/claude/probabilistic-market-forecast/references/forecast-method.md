# Forecast method

## Evidence stack

1. Verified current price and product identity
2. Point-in-time adjusted historical distribution and matched regimes
3. Options/implied information when liquid and available
4. Fundamentals, valuation and consensus dispersion
5. Dated catalyst/event probabilities
6. Macro, sector and technical regime
7. Execution, liquidity, spread, time decay and leverage

## Horizon weighting

- Days to a few weeks: volatility, market regime, liquidity, technical structure and dated events dominate; directional drift is heavily shrunk.
- Months: add earnings path, estimate revisions, valuation and sector/macro transmission.
- Years: business economics, reinvestment, balance sheet, dilution, valuation and regime change dominate; short-term technical indicators carry little weight.

## Distribution construction

Use at least two views when data permits:

- Parametric range from annualized volatility and a conservative drift.
- Empirical rolling-horizon distribution from adjusted point-in-time history.

Add separate event branches when a binary or discontinuous catalyst exists. Do not average mutually exclusive product outcomes into one smooth target without showing the branches.

## Benchmark and humility

Freeze a naive comparator before the outcome: zero/benchmark drift, unconditional historical base rate, equal-probability categories, or a relevant liquid market-implied probability. Choose it by decision and horizon rather than after seeing results. Financial-forecast competition evidence shows that directional edge is often small and unstable; a wider well-calibrated distribution or better risk estimate may add more decision value than a confident point target.

Do not select a model because it won on the same evaluation sample. Use walk-forward or held-out scoring, include costs when forecasts drive actions, and preserve negative results.

## Candidate ranking

Use a transparent table containing median return, probability of profit, probability of exceeding the target, expected downside, severe-loss probability, liquidity/spread, catalyst quality, invalidation and confidence. Avoid composite scores unless weights are visible.
