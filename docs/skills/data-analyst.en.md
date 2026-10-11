# data-analyst

[English](data-analyst.en.md) · [Türkçe](data-analyst.tr.md) · [Library](../../README.md)

**Analyze data with explicit units, missingness, assumptions and uncertainty.**

## Try it

> Explore this dataset and explain which conclusions its sample can support.

## Trigger and routing

The host matches the request against the skill description. Explicit selection by canonical name is available where supported. Typing /name in chat does not register a command.

<details>
<summary>Exact source description</summary>

Structured data work: exploratory and statistical analysis, data quality, SQL queries, metric definitions and data dictionaries, dashboards and KPI views, chart selection and chart review. Turkish triggers: veriyi analiz et, tabloyu incele, istatistik, SQL yaz/düzelt, dashboard yap, grafik seç, KPI, veri temizle. More triggers: KPI panosu, karar odaklı raporlama, veri sözlüğü, metrik tanımı.

</details>

## How it works

Inspect schema and quality; choose an appropriate method; compute or visualize; distinguish observation from interpretation.

The root entry point owns routing; only relevant modules and references are loaded. A bundled script is not an executed result. Work uses actual host tools, available input and the task scope.

## Inputs, outputs and verification

- Input: the example goal, relevant files/URLs/data, and constraints that change the result.
- Output: a task-appropriate answer, plan, draft or authorized file change with evidence and uncertainty.
- Verification: performed and suggested checks are separate; inaccessible sources and unexecuted tools are not counted as used.

## Runtime and boundaries

The package supplies no model weights, permissions, account or API credit. This edition uses existing host tools, open access and local computation; a separately billed service is not an automatic fallback. Clinical/investment outputs do not replace professional judgment or execute orders.

## Modules and source

[SKILL.md](../../skills/common/data-analyst/SKILL.md) · [Installation](../INSTALL.md) · [License scope](../LICENSE-SCOPE.md)

| Module | Source scope |
|---|---|
| [data-analysis](../../skills/common/data-analyst/modules/data-analysis/MODULE.md) | Perform defensible exploratory, descriptive, statistical, or diagnostic analysis on structured data. Use for analyze data, investigate a metric, statistics, data quality, trends, c |
| [data-context](../../skills/common/data-analyst/modules/data-context/MODULE.md) | Create or repair a durable data context containing schema, grain, metric definitions, lineage, ownership, freshness, and quality caveats. Use for data dictionary, metric definition |
| [data-dashboard](../../skills/common/data-analyst/modules/data-dashboard/MODULE.md) | Plan, build, review, or improve a decision-focused dashboard with metric definitions, owners, filters, freshness, alerts, and validation. Use for dashboard, KPI dashboard, analytic |
| [data-visualization-playbook](../../skills/common/data-analyst/modules/data-visualization-playbook/MODULE.md) | Apply a concise decision-focused playbook to design, implement, critique, or validate charts with correct encodings, annotations, accessibility, and source context. Use when the us |
| [sql-analytics-workflow](../../skills/common/data-analyst/modules/sql-analytics-workflow/MODULE.md) | Design, review, debug, or explain analytical SQL with correct grain, joins, filters, time logic, performance awareness, and validation. Use for SQL analysis, writing or debugging a |
