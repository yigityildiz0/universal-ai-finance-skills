# purchase-advisor

[English](purchase-advisor.en.md) · [Türkçe](purchase-advisor.tr.md) · [Library](../../README.md)

**Compare product suitability, evidence and real total cost rather than promotional rankings.**

## Try it

> Compare these two products for my actual use case and budget.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Purchase and price-value advisor for products, services and subscriptions: current dated price checks, total cost, alternatives and cheaper equivalents, value-for-money verdicts, and evidence checks for health products such as supplements, creams, braces, tapes, massagers, TENS/EMS devices and rehab aids (ingredients, regulatory status, SGK). Turkish triggers: alayım mı, fiyatı iyi mi, almaya değer mi, muadili var mı, en ucuz/kaliteli hangisi, işe yarar mı, 10 üzerinden kaç, zararlı mı. More triggers: SGK karşılıyor mu, reçeteli mi, fiyat-performans.

</details>

## How it works

Pin the exact model/market; define priorities; verify specs and independent evidence; compare total cost and tradeoffs.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/purchase-advisor/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [health-product-evidence-check](../../skills/common/purchase-advisor/modules/health-product-evidence-check/MODULE.md) | Automatically evaluate a health-related product, medicine-like item, supplement, cream/gel, brace, tape, massager, electrotherapy device, wearable, exercise/rehabilitation aid, or  |
| [market-pricing-analysis](../../skills/common/purchase-advisor/modules/market-pricing-analysis/MODULE.md) | Automatically analyze product, service, subscription, marketplace, or competitor pricing when the user asks "fiyatı iyi mi", "almaya değer mi", "en ucuz/kaliteli hangisi", "muadili |
