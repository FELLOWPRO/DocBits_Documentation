# Touchless Intelligence

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/en.mp4" %}

Touchless Intelligence answers two separate questions: **Did DocBits extract the invoice correctly?** And: **Did the whole process finish without a processing intervention?** Correct extraction can still need rework when Infor data differs. AP means the human Accounts Payable team.

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

## Access

This area belongs to the [Analytics Dashboard](../). Administrators have access; other users need the corresponding role grant. AI analysis, supported changes and consulting reports may require administrator rights.

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
