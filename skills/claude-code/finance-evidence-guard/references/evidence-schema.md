# Evidence schema

Store each material record with:

- `claim_id`: stable local identifier
- `claim`: concise statement
- `claim_type`: fact, estimate, calculation, inference, or opinion
- `instrument_id`: ticker plus exchange, ISIN/CIK/accession, fund code, or network plus contract
- `source_url` and `publisher`
- `published_at` or `effective_at`
- `fetched_at`
- `period`: instant, date range, fiscal quarter/year, candle interval, or NAV date
- `value`, `unit`, and `currency` when numeric
- `latency`: realtime, delayed, end_of_day, indicative, or unknown
- `adjustment`: adjusted, unadjusted, split-adjusted, inflation-adjusted, or not_applicable
- `primary`: true or false
- `notes`: conflicts, transformations, and caveats

Required fields depend on the claim, but every current numeric market fact needs instrument identity, source, value, unit/currency, effective time, fetched time, and latency.

Do not store credentials, account numbers, or private portfolio identifiers in an evidence packet.
