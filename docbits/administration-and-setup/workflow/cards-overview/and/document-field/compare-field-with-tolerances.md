# Compare Field with tolerances

<figure><img src="../../../../../.gitbook/assets/image (57).png" alt="" width="563"><figcaption></figcaption></figure>

## When to use this card

Use this condition to compare a numeric document field with a fixed reference while allowing a defined deviation. For example, a total amount may count as matching a reference of 100 when it differs by no more than 5.

## Where to find it

In the standard workflow designer, add a card under **And**, open **Document Field**, and select the comparison of one field with a reference and tolerances. The example below uses version 2.

## Settings

Use a numeric field configured in your organization. The field value, reference and tolerance are evaluated numerically. Keep their units consistent.

| Setting | Meaning |
| --- | --- |
| Field name | The configured document field, such as `total_amount`. |
| Operator | The comparison to apply: `eq`, `neq`, `gt`, `ge`, `lt` or `le`. |
| Reference value | The fixed number against which the field is compared. |
| Tolerance amount | The allowed numeric deviation. |
| Tolerance type | **Value** (`value`) for an absolute amount, or **Percent** (`percent`) for a relative amount. |

For example, with a positive reference of 200, a percentage tolerance of 5 gives a deviation of 10. An absolute tolerance of 5 gives a deviation of 5. Check the relevant boundary cases for your selected operator and values.

## How tolerance changes the comparison

For a reference of **100** and an absolute tolerance of **5**, the lower bound is **95** and the upper bound is **105**.

| Operator | Condition is met when the field value is… |
| --- | --- |
| `eq` (=) | Between 95 and 105, including both bounds. |
| `neq` (≠) | Below 95 or above 105. |
| `gt` (>) | Above 105. |
| `ge` (≥) | At least 95. |
| `lt` (<) | Below 95. |
| `le` (≤) | At most 105. |

This card returns a condition result. Follow-up steps depend on the workflow's trigger, other conditions and configured actions.

<!-- workflow-card-complete-example-20261021 condition_docfield_operator_value_tolerances -->

## Practical example

1. Select the configured numeric field `total_amount`.
2. Choose **Equals** (`eq`).
3. Enter reference **100** and tolerance **5**.
4. Choose tolerance type **Value** (`value`).

| Field value | Absolute difference from 100 | Expected result |
| --- | --- | --- |
| 103 | 3 | Condition met. |
| 110 | 10 | Condition not met. |
| 95 or 105 | 5 | Condition met: the equality comparison includes the tolerance bounds. |

These are expected calculation results for an illustrative configuration. No workflow was executed for this example.

## Before enabling the rule

Check a matching case, a non-matching case and the boundaries with suitable test data. Investigate missing fields, nonnumeric values and configuration errors separately. Use the execution log to inspect the values, operator, tolerance and result actually used.

For a comparison in which both amounts come from document fields, use the separate [two-field tolerance card](compare-two-fields-with-tolerance.md).
