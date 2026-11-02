---
description: "P1: Choose Field is, Docfield is or Compare two Fields"
---

# P1: Choose Field is, Docfield is or Compare two Fields

Use **Field is** for empty-state checks, **Docfield is** to compare against a configured value, and **Compare two Fields** for two values on the current document. An empty-state check does not prove that a field exists in the layout or is business-valid.

For Field is version 2, an absent field, `null`, empty text, whitespace-only text and boolean `false` are empty. Number `0`, text `"0"` and text `"false"` are not empty. These eight cases were tested in Dev using complete document data. Use an explicit checkbox condition when true/false is the business decision.

A value `"1000.01"` in an AMOUNT field differs from the same characters in a text field. The v2 training kit uses AMOUNT and decimal points in JSON. Check the technical field key, layout and type together. A translated label is not a technical key, and a currency symbol is not a numeric value.

For Compare two Fields, set the left field, operator and right field. Confirm compatible types and both inputs; absent or incomparable data is a data error, not proven inequality. Repeat positive, negative, missing-input and exact-boundary cases. Record each value, type and selected output.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `condition_docfield_status` · v2

Identity: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identity: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identity: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Evidence and limits

Selected card and node outcomes were checked with synthetic data in Advanced Test. Responses are in the training kit. Document actions are simulated; these tests do not establish a persisted document run or external delivery.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
