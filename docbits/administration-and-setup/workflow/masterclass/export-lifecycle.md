---
description: "P1: Choose export variants, pending-task checks and final status"
---

# P1: Choose export variants, pending-task checks and final status

**Start Export** uses the configured export route. **Export with Export Configuration** runs a selected configuration. Its deferred variant queues that configuration for final export at the end of the current run. Queuing does not mean automatic delivery after all later human approvals.

The inspected newer versions offer `status=finished` or `status=exported`: finished closes the document; exported allows further editing. Start Export provides this choice from v4; configured and deferred export from v3. Earlier versions use finished. A missing choice in newer versions also defaults to finished in the code; an invalid choice is a configuration error.

With `ignore_pending_tasks=false`, open tasks are checked. The document service can therefore refuse immediate configured export. That card does not establish automatic resumption after later task completion. Define a new execution event and check for an existing destination record before sending again. Ignoring tasks is not a substitute for approval.

Connect export only after an explicitly verified approval condition. Acceptance covers an open task, completed task, missing approval, successful test-destination receipt and a repeated run. Distinguish requested export, recipient receipt and ERP processing. The training kit has no real export destinations; its test results do not prove delivery.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `export` · v4

Identity: `757f30ca-ed60-4e04-8131-2779df17f019`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `boolean` | `boolean:bool` | `true` |
| `status` | `finished / exported` | `"finished"` |

### `action_export_with` · v3

Identity: `ebcd854d-68b3-4b5f-8d45-1bcf8c675b21`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"exported"` |

### `action_export_with_config_deferred` · v3

Identity: `060ef4c8-625f-447c-83c9-2ca3f680d88d`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `export_configuration` | `export_configuration:int` | `"YOUR_TEST_EXPORT_CONFIGURATION_ID"` |
| `ignore_pending_tasks` | `ignore_pending_tasks:bool` | `false` |
| `status` | `finished / exported` | `"finished"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| EXPORT-01 | status=finished | closed |
| EXPORT-02 | status=exported | editable |
| EXPORT-03 | ignore_pending_tasks=false; pending_tasks>0 | may refuse; no automatic resume proven |
| EXPORT-04 | action_export_with_config_deferred | queue ≠ receipt |
| EXPORT-05 | RUN-1 → RUN-2 | destination_records=1 |

## Evidence and limits

Parameters and behavior were checked against the Dev catalog and inspected source revision. Business test cases are an acceptance procedure. Personal approvals, real data changes and delivery were not performed for this chapter.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
