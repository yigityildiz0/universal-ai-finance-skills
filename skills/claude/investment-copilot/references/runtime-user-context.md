# Runtime user context

This file defines **what context may be used**, not a stored profile of any individual.

## Allowed decision context

Use only facts supplied in the active request/conversation or returned by an explicitly authorized context source when relevant:

- jurisdiction, base currency, and market access;
- decision horizon and liquidity needs;
- current position, cost basis, and portfolio concentration;
- investable amount and maximum acceptable loss;
- tax/account/product constraints that are actually verified;
- requested answer language, depth, and decision format.

Treat every dated holding, balance, preference, platform, prior recommendation, and screenshot as historical until reconfirmed. Never infer broad risk tolerance from one small speculative budget.

## Privacy rules

Do not persist a real name, email, phone number, account number, student/work identifier, exact address, bank balance, full portfolio, credentials, tax documents, or other unnecessary identifier in this skill. Keep sensitive fields in the active context only for as long as the task requires them.

When an exact quantity is requested, verify instrument identity, executable price or bid/ask, fees, lot/contract size, available budget, and maximum loss. When a screenshot or OCR result supplies a code, verify the code and product type before analysis.

## Language support

Default instructions are English. Answer in the user's language. Turkish investment shorthand and natural prompts are supported, including `alınır mı`, `tut`, `artır`, `azalt`, `sat`, `kaç lot/adet`, `ne kadar yükselir/düşer`, and `emin misin`; these are intent signals, not stored user preferences.
