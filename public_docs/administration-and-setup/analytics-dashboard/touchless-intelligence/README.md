# Touchless Intelligence

Touchless Intelligence answers two separate questions: **Did DocBits extract the invoice correctly?** And: **Did the whole process finish without a processing intervention?** Correct extraction can still need rework when Infor data differs. AP means the human Accounts Payable team.

## Video: Touchless report functions

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/en.mp4" %}

This 5:41 review version shows a populated report: filters, KPIs and calculation, trends, first blockers, recorded evidence, document history, run comparison, learned rules, improvements and history, consulting reports and actual MCP results.

[Open the video with English captions and 16 chapter links](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/en.html). Human listening review of this new version is still pending.

These training cases explain report functions. A recommendation or preview proves neither an applied setting nor a measured improvement. The displayed MCP change proposal still needs a specific target configuration; preview and apply are unavailable for that proposal. Some native product text may retain its original language.

<figure><img src="../../../.gitbook/assets/anatomy-touchless.svg" alt="Isometric sorting line: a conveyor with 14 gates, a pusher that diverts one document into a review tray, an export bin with a stack of documents and a dial reading 78.9 percent"><figcaption><p>Touchless as a sorting line, with the illustrative numbers from the example calculation: the 14 gates are the stages of the Pipeline Path, sheets still on the belt are in progress and not counted, a document that stops at a gate is pushed into the review tray with the AP assisted (30) and process exception (10) documents, and the pure (120) and approval-only (30) documents in the export bin give the dial's 150 of 190, or 78.9 %, past the 70 % target mark.</p></figcaption></figure>

## Find the right guide

| Guide | What it covers |
| --- | --- |
| [Metrics and calculation](touchless-metrics.md) | Outcome categories, numerator and denominator, AP actions and calculations |
| [Use the dashboard](touchless-dashboard.md) | Filters, KPI cards, trends, first blockers and controls |
| [Worked examples: price and quantity](touchless-examples.md) | Fictional invoices and real Dev PO views with price and quantity differences |
| [Supplier Diagnosis and Issue Clusters](touchless-supplier-diagnosis.md) | Prioritise suppliers and recurring causes |
| [PO Matching Diagnosis](touchless-po-matching-diagnosis.md) | Understand active rules, tolerances and the decision flow |
| [Document Trace](touchless-document-trace.md) | Inspect original values, processing runs, blockers and interventions |
| [Change Proposals and Reports](touchless-change-proposals.md) | Distinguish preview, apply, effect measurement and rollback |
| [Explain and improve Touchless with MCP](touchless-mcp.md) | Explain, diagnose and make controlled improvements through MCP |

<figure><img src="../../../.gitbook/assets/touchless-overview.png" alt="The Touchless Intelligence tab with five key figures, improvement suggestions and the touchless rate chart"><figcaption><p>The Touchless Intelligence tab: key figures, improvements, the rate over time and the lost-first chart. Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

## Report settings

The report reads four organisation settings that an administrator maintains under **Settings → Module → Dashboards & Analytics**. They set the target and the cost view; an empty field means DocBits uses the default.

| Setting | Default | What it controls |
| --- | --- | --- |
| Touchless target | 70 % | The share of documents that should pass without a processing intervention. The report uses it as the target mark in the rate chart. |
| Minutes per AP intervention | 6 min | The time an AP employee needs to correct and release one document. |
| Hourly cost | 40 | The cost of one hour of AP work in the currency below. |
| Currency | EUR | The currency of the cost view, as a three-letter ISO 4217 code such as `EUR`, `CHF` or `USD`. DocBits stores the code in upper case and rejects a value that is not a currency code, so a typo cannot reach the report. |

The API checks the stored values again and uses the default for a value it cannot work with.

## Access

This area belongs to the [Analytics Dashboard](../). Administrators have access; other users need the corresponding role grant. AI analysis, supported changes and consulting reports may require administrator rights.

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
