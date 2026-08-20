# Forecast calibration and ledger

## Freeze before outcome

Store an immutable forecast record with:

- Unique ID, instrument identity, venue and currency
- Issue time, source/data cutoff, horizon and exact maturity/outcome rule
- Current adjusted price/value and target definition
- P10/P25/P50/P75/P90 or categorical probabilities
- Binary target/loss probabilities when used
- Declared naive or market-implied benchmark probabilities/ranges
- Model/version, training or lookback cutoff, regime, assumptions and exclusions
- Source ledger and record hash when the host supports it

Append the realized adjusted value/outcome and scoring time after maturity. Never edit the original probability, quantile, target, benchmark or cutoff. Early exits and unresolved outcomes remain separate from matured records.

## Proper evaluation

- Binary events: Brier score and calibration bins; compare Brier with the frozen benchmark.
- Ordered categories: ranked probability score (RPS) and benchmark RPS.
- Quantiles: observed coverage and pinball loss at every reported quantile.
- Intervals: width versus realized coverage, including tail misses.
- Direction/return: compare with zero-change, historical base-rate and relevant market-implied benchmarks when available.
- Decision usefulness: include costs, spread, slippage, turnover and whether the forecast changed the action.

Lower scores are better for Brier, RPS and pinball loss. Report skill relative to a benchmark only when both were frozen under the same outcome rule.

## Segmentation and correction

Review by asset class, horizon, volatility, liquidity and catalyst regime only after enough comparable matured cases. Report count and missingness for every segment. Do not tune thresholds repeatedly on the evaluation sample.

Do not claim calibration from a handful of forecasts. Widen intervals, shrink directional confidence and investigate regime or data failures when tails exceed the model or benchmark-relative skill is negative. Preserve bad forecasts; they are evidence, not clutter.
