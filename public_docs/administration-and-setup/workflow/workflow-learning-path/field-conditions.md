---
description: 'Choose Field is, Docfield is or Compare two Fields'
---

# Choose Field is, Docfield is or Compare two Fields

Three condition cards look alike in the designer, and the difference between them decides what a rule can actually catch. This page helps you pick the right one, then gives you three short exercises that show what each card returns. Afterwards you can tell "empty" apart from "zero", "false" apart from "missing", and a failed condition apart from an error.

Do the exercises in Advanced Test, in your own test organization, against a synthetic document. Nothing here touches a customer document.

## Which card do you need?

| If you want to check ... | Use | Card and version |
| --- | --- | --- |
| whether a field carries any value at all | **Field is** | `condition_docfield_status` v2 |
| one field against a value you enter | **Docfield is** | `condition_docfield_operator_value` v2 |
| two fields on the same document against each other | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

All three are conditions: they return a result and change nothing on the document. An empty-state check does not prove that a field exists in the layout or that its content is business-valid. The individual card pages list every setting: [Field is](../cards-overview/and/document-field/field-is.md), [Docfield is](../cards-overview/and/document-field/docfield-is.md) and [Compare two Fields](../cards-overview/and/document-field/compare-two-fields.md).

## Exercise 1: find out what "empty" means

**Goal:** know which values Field is version 2 treats as empty.

1. Add **Field is** version 2 to a rule in your test organization and select a text field from your layout.
2. Set Field status to `field_empty` (Empty or missing).
3. Run eight Advanced Test cases with complete document data: a missing field, `null`, empty text `""`, whitespace-only `" "`, boolean `false`, number `0`, text `"0"` and text `"false"`.

**Done when:** the first five cases return `field_empty=success` and the last three return `field_empty=failed_condition`. These eight cases were tested in Dev with complete document data.

Number `0`, text `"0"` and text `"false"` are values, not absences. If true or false is your business decision, use an explicit checkbox condition instead of testing the field for emptiness.

## Exercise 2: compare one field with a value

**Goal:** see how the operator and the field type change the answer.

1. Choose a numeric field such as `total_amount`, the operator `gt` and the value `1000`.
2. Test `1000`, `1000.01`, a missing field and an invalid value.

**Done when:** `1000` returns `failed_condition`, because `gt` means strictly greater, `1000.01` returns `success`, and a missing or invalid input returns `error`.

## Exercise 3: compare two fields

**Goal:** know when two values are compared and when the card cannot compare them at all.

1. Set the left field, the operator and the right field. Use two fields with compatible types.
2. Test equal values, different values, and one input missing.

**Done when:** equal values satisfy `eq`, different values return `failed_condition`, and a missing input returns `error` instead of a proven inequality.

## What the three results mean

| Result | What it tells you |
| --- | --- |
| `success` | The card compared the values and the condition was met. |
| `failed_condition` | The card compared the values and the condition was not met. `0` and `"0"` end here in an empty-state check. |
| `error` | The card could not compare, for example because a value is missing or invalid. An error is not the same answer as "not equal". |

## Types are part of the comparison

A value `"1000.01"` in an AMOUNT field is not the same as the same characters in a text field. The v2 training kit uses AMOUNT and decimal points in JSON. Check the technical field key, the layout and the type together. A translated label is not a technical key, and a currency symbol is not a numeric value.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR\_\* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

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
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Evidence and limits

Selected card and node outcomes were checked with synthetic data in Advanced Test. Responses are in the training kit. Document actions are simulated; these tests do not establish a persisted document run or external delivery.

[Continue learning](./) · [Training kit](workflow-training-kit.md)
