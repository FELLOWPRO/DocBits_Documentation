---
description: "Validate structure, choose document or custom test input, inspect node results and preserve regression scenarios."
---

# Validation & Testing

**Validate** checks graph structure. **Test** evaluates the current graph with specific input. A valid drawing or one green test does not prove that every production case is covered.

## Validate

Use the **check-circle** button or **Cmd/Ctrl + Shift + V**. Errors and warnings appear above the canvas. Click a message with a node reference to focus that node.

| Check | Correction |
| --- | --- |
| Entry | Include and connect Start or When. Entry nodes cannot be targets. |
| Action | Include at least one Then. |
| Connections | Use a supported output handle and a valid destination input. |
| Cycles | Remove self-connections and loops. |
| Merges | At least two inputs for Wait ALL/ANY; two distinct sources for OR. |
| Unused nodes | Reconnect or remove orphaned processing nodes. Notes need no connections. |
| Existing Delay | Positive duration, no more than 86,400 seconds. |
| Cards | Resolve missing-card and version-compatibility warnings. |

A warning can flag a questionable design, such as several outcome handles from one source feeding the same target. Review its meaning; it is not successful testing.

Validation cannot reliably establish that every version-specific card field contains correct runtime data. Configure the visible fields and test realistic input. Runtime tests can reveal missing data that structural checks do not detect.

## Choose test input

Use the toolbar **play-circle** or **Cmd/Ctrl + Shift + T** to open **Select Test Document**.

<figure><img src="../../../.gitbook/assets/advanced_workflows_test_picker_en.png" alt="Select Test Document with document search, custom data and Test Without Document"><figcaption><p>Choose the input required by your cards. Document-independent testing cannot verify document-dependent conditions.</p></figcaption></figure>

| Choice | How | Appropriate use |
| --- | --- | --- |
| **Search Document** | Enter at least two characters, select a document and choose Test. | Document-dependent checks using available document data. |
| **Custom Data** | Enter valid document-data JSON and test. This requires the document-data structure, not arbitrary key/value JSON. | Controlled input and edge cases when you know the structure. |
| **Test Without Document** | Run without selecting a document. | Document-independent cards and control-flow checks. |

<figure><img src="../../../.gitbook/assets/advanced_workflows_custom_data_en.png" alt="Custom Data tab with the document-data JSON input"><figcaption><p>Use complete document-data JSON for controlled scenarios. The placeholder comment alone does not provide the fields a document-dependent card needs.</p></figcaption></figure>

The **Start play control** tests directly without opening the picker. **Test from here** on a node starts at that point. Required downstream context must still exist. A partial test does not verify the omitted trigger and upstream checks.

After a partial test, repeat the scenario from the full entry point, especially when it includes merge nodes. A test starting halfway through the graph can have a different set of completed predecessors from a real document event.

Tests use the **current canvas**, including unsaved edits. Test mode simulates destructive actions and skips actual delays. A simulated export, email or task does not establish that the production integration completed.

## Read results

Inspect the summary and per-node result indicators on the canvas. Open result details for messages and duration per node. The result dialog offers **View in Designer**, **Re-test** and **Close** where available.

| Result | Meaning | Inspect |
| --- | --- | --- |
| **Green — Success** | Node completed successfully. | Expected action and route. |
| **Orange — Failed Condition** | Evaluated condition was false. | Orange alternative and input values. |
| **Red — Error** | Evaluation or action failed. | Exact node message and required data. |
| **Gray — Skipped** | Node did not run. | Preceding outcome, entry and branch. |

A false condition can lead to an expected alternative and a successful workflow. A successful error handler can coexist with an overall error. Read individual nodes as well as the overall badge.

Overall test duration can include setup and document loading. Per-node durations describe the individual operations; the measurements need not add up exactly.

## Repeatable tests

Use [Test Manager](../test-manager.md) for saved regression scenarios. Cover:

- True, false and error outcomes.
- Exact amount/date/tolerance boundaries.
- Missing data and unexpected document types.
- All merge inputs matching, only one matching and none matching.
- Every relevant event entry and expected downstream action.

Re-test corrections and alternatives. Then **Save**, check the enabled state in Workflow List and inspect a new real run in [Workflow Logs](../workflow-logs.md).
