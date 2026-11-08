# Explain and improve Touchless with MCP

<!-- touchless-admin-video-v2-20261104:start -->
**Video chapter (review version):** [Query figures with MCP](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/en.html#chapter=12).
<!-- touchless-admin-video-v2-20261104:end -->

The following workflows use tools actually advertised by DocBits MCP. Distinguish reading and explanation from writing. Check organisation, role, document type, period and data timestamp; do not invent missing evidence.

<figure><img src="../../../.gitbook/assets/touchless-owned-po-price-en.png" alt="Actual English Dev view of an owned fictional PO: 10 × 9 = 90. This is source comparison for MCP diagnosis, not a screenshot of an MCP client or proof of successful extraction or processing."><figcaption><p>Actual English Dev view of an owned fictional PO: 10 × 9 = 90. This is source comparison for MCP diagnosis, not a screenshot of an MCP client or proof of successful extraction or processing.</p></figcaption></figure>

## Explain Touchless through MCP

> Explain Pure Touchless, approval-only outcomes and the combined AP rate for invoices over the last 30 days. State the numerator, denominator, in-progress and excluded documents, scope and data timestamp. Keep extraction correctness separate.

Use `touchless_get_summary` with `period: "30d"` and `doc_type: "INVOICE"`. For a subprocess, use only segment fields and values actually returned by `touchless_list_segments`. Compare the dashboard and MCP with the same organisation, document type, segment and period; read `data_as_of`.

**Verified Dev counterexample:** Three newly uploaded test invoices were still `IN_PROGRESS`. The summary returned `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0` and `official_touchless_rate.ap_pct: null`. No rate was measurable yet. This is neither 0% extraction accuracy nor 100% Touchless. Summary eligibility here refers to the completed KPI population; an individual trace can simultaneously show `eligible: true` and `bucket_final: false`.

The MCP examples on these five pages use direct DocBits MCP tools checked on Dev. Your connected account's organisation and role apply; availability in another interface or an additional tool allowlist is not established by that test.

## FAQ

**DocBits extracted everything correctly. Why is the invoice AP assisted?**
Touchless measures the whole process. Incorrect or outdated Infor data can require a recorded correction or manual restart even with correct extraction. Check the original invoice, the values DocBits extracted and the imported source data separately.

**Does AP assisted tell me whether DocBits or Infor caused the work?**
No. It records the intervention, not responsibility. Use the document trace and the underlying document and source data to confirm the cause.

**The rates show a dash (—).** No document has reached a final outcome in the period, or fewer documents than the minimum were measured. Documents that are still in progress are not counted.

**The tab is missing.** Ask your administrator to enable the module and to grant your role the **Analytics dashboard** tab.

**A document is counted as touched, but it ran through without anyone this time.** It was touched in an earlier run (a correction or a restart). The rate counts the work that happened.

**Why does the number change after a few hours?** The ERP may confirm an export hours after it was sent. The outcome is recalculated every 15 minutes.

**Does the AI change anything on its own?** No. AI writes explanations only. A setting changes only after an administrator previews and applies it.

## Investigate discrepancies through MCP

> Check this invoice's PO number, import status and actual active matching rules. Separate extraction, stale import, wrong source data and missing configuration. Do not change anything yet.

1. Compare the original, `get_extracted_fields` and `get_extracted_tables` before claiming correct extraction.
2. Use `get_po_sync_status` with `po_number: "TL20261104X1-PO02"` and `language: "en"`. The Dev test confirmed a processed import and an existing PO. This proves arrival, not business correctness or the current Infor record.
3. Use `touchless_get_document_trace` and `touchless_explain_po_match` with the same `doc_id`. Read actual engine, active rule version, columns and effective tolerances. For an actual returned cluster, use its `issue_signature` in `touchless_get_po_match_evidence`.
4. Preserve missing evidence: our new test type returned `state: "none_published"` and `parse_error: "no published rule set"`, as well as empty extraction fields. No price/quantity blocker or successful match was proven. A generic decision flow cannot replace those missing checks.
5. Fix the confirmed cause and check new invoices. Human correction or restart remains relevant after success; a final ERP failure takes precedence as an exception, and an unfinished document is outside the rate denominator.

For a complete case retain the original, extraction before correction, imported/current source values and import time, actual rules, AP action and final result. Missing evidence stays open.

## Read the evidence through MCP

> Inspect this invoice without changing it. Compare the original, current fields and tables. Explain the recorded stages and runs, and identify missing historical extraction evidence.

| Tool, using the same `doc_id` | Evidence and limit |
| --- | --- |
| `get_extracted_fields` | Current header values and confidence; not a historical snapshot |
| `get_extracted_tables` | Actual tables and rows; not proof they agree with the original |
| `touchless_get_document_trace` | Recorded outcomes, interventions, stages and runs |
| `touchless_explain_pipeline` | Explanation of the evidenced processing path; does not fill missing evidence |

**Observed negative check:** Our fresh test invoice had a `passed` header-extraction stage but `extracted_field_count: 0`, eight empty required fields and no table. Field validation blocked with `REQUIRED_FIELD_MISSING`. The assistant must investigate missing extraction/configuration, rather than claim correct extraction from a green stage or a proven PO-price blocker from differing source values.

### Does an MCP action count as a human touch?

Read-only inspection does not change an invoice. Other MCP tools may write fields, validate or restart. Classification depends on the recorded event and whether its actor is a human or system account. An API key can act as a system account; “performed through MCP” alone proves neither a human touch nor Pure Touchless. Never use system credentials to hide human rework.

After a document action inspect `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, final status and runs. Business approval only is different from a saved correction, manual validation or human restart.

## Prioritise suppliers and verify a lasting improvement through MCP

> Rank the suppliers losing the most Touchless invoices. Separate extraction errors, imported-source discrepancies and process settings. Propose one action and a verifiable success check for each confirmed cause; do not change anything yet.

1. Use `touchless_rank_supplier_opportunities` with `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. Use `search` for a supplier number or name; `limit` and `offset` page results.
2. Pass the returned `supplier_key` unchanged to `touchless_diagnose_supplier`. Use `window: 30` for current issues or 90 to investigate recurring issues.
3. Pass an actual returned `issue_signature` to `touchless_get_issue_cluster`. Review example documents and missing evidence before confirming the cause. Do not invent identifiers.
4. Use `touchless_get_recommendations` to explain a supported action. Expected lift is an estimate; overlapping clusters must not simply be added.
5. Check new comparable invoices after the fix and the [change measurement](touchless-change-proposals.md). Previously touched invoices do not become Pure Touchless retrospectively.

For correct extraction and stale POs, fix source/import data. For a mismatch between original and extraction, investigate extraction configuration. Approval required by policy is a separate successful AP Touchless outcome. An empty ranking is not proof of no problems: our three in-progress test invoices produced no ranked supplier outcome yet. Check scope, data timestamp, supplier identification and completed volume.

## Preview, apply and measure with MCP

> Explain the confirmed cause and list supported proposals. Preview the selected change, its scope and risks. Apply only that chosen change, then verify the saved setting, change history and measurable effect.

| Step | Tool and actual returned identifiers | What it proves |
| --- | --- | --- |
| List | `touchless_list_change_proposals`, optional `issue_signature`, `window: "30d"`, `lang: "en"` | Available proposals; no setting saved |
| Preview | `touchless_preview_change` with the returned `proposal_id` and matching `issue_signature` | Concrete scope and a bound `preview_token` when permitted |
| Apply selected change | `touchless_apply_change` with the same IDs, `preview_token`, `overrides` and `window` | **Writes** the supported setting; successful response returns a `change_id` |
| Read effect | `touchless_verify_change` with that `change_id` and the same `window` | Before/after measurement; at least 20 eligible completed documents per period still required |

Copy IDs and tokens from genuine responses. A token previewing one value cannot apply a different value. An expired, forbidden or incomplete preview is not evidence of an applied change. Read-only tools and apply must not be described as equivalent. This table explains the tool sequence; it does not claim that the demo executed a proposal or measured a gain.

**Configuration example:** After a confirmed configuration fix, inspect the actual saved value and new invoices. 52% before and 61% after is an observed 9 percentage-point difference, not proof that this change alone caused it. **Source-data example:** A wrong Infor PO needs a business correction and a verified import. `touchless_apply_change` is not a general Infor-write tool. Do not widen tolerances to conceal wrong source data.

The report screenshot shows recommendations and estimated impact, not application or rollback. A successful apply needs a success response and history entry. Undo is available only where the selected proposal supports it; verify the actual restored setting. Reloading history does not apply a setting, and rollback does not delete past document interventions.

## Related pages

* [Touchless Intelligence](./)
* [Metrics and calculation](touchless-metrics.md)
* [Use the dashboard](touchless-dashboard.md)
* [Worked examples: price and quantity](touchless-examples.md)
* [Supplier Diagnosis and Issue Clusters](touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals and Reports](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->
<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
