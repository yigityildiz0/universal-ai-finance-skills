# Portfolio risk protocol

## Snapshot contract

Require a dated base-currency NAV and position ledger. Each position should contain exact identifier, product type, signed market value or notional convention, currency, issuer, sector/strategy, liquidity measure and any look-through data. Record cash, liabilities, margin, derivatives and off-platform exposures when material.

Do not infer a live holding from a prior conversation. Mark incomplete coverage explicitly.

## Exposure views

Report at least:

- Net and gross exposure relative to NAV
- Position and issuer concentration
- Sector/industry and country exposure
- Currency and rate/duration exposure
- Fund and ETF look-through overlap
- Leveraged, short, derivative and full-loss exposure
- Liquidity and time-to-exit assumptions

Use a concentration index only as a diagnostic; it does not replace scenario analysis or economic look-through.

## Size constraints

For a proposed trade calculate independently:

1. Cash/budget limit
2. Loss-at-invalidation or full-loss limit
3. Post-trade position/issuer/cluster concentration limit
4. Liquidity/exit limit
5. Product-specific margin, expiry or settlement limit

The allowed quantity is the smallest constraint after fees and lot rounding. State which constraint binds. If gap or path-dependent loss can exceed the stated limit, show the larger stress amount.

## Scenario discipline

Use named coherent scenarios with visible holding-level returns and aggregate P&L. Do not call a hand-built scenario VaR. When using historical covariance or simulations, report lookback, frequency, missing data, estimator, benchmark and instability; keep a simple stress test alongside it.
