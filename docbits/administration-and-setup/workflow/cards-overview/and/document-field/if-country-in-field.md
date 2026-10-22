# If Country in Field

<figure><img src="../../../../../.gitbook/assets/image (55).png" alt="" width="563"><figcaption></figcaption></figure>

Use this condition when an additional processing step should depend on a country group. The example checks whether the country in a document field belongs to the European Union.

**Where:** Standard workflow → additional conditions (AND) → Document Field. Configure the subsequent action separately under THEN.

## Configuration — version 2

| Setting | Value |
| --- | --- |
| Field | An existing text field containing the country name |
| Operator | `is` |
| Region | European Union (EU) |
| Continue value | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Practical example

| Country field value | Expected condition |
| --- | --- |
| `Germany` | Met |
| `United States` | Not met |

The country names shown as code are fixed input values for this example.

## Limits and checks

`false` does not invert the comparison. Even a matching country does not produce a positive condition with that setting. To check the opposite condition, select `isnot` with `true`.

Handle missing fields and empty country values separately; they can return a missing-data result rather than an ordinary non-match.

Source inspection of the development version dated 22 October 2026 shows a conversion error for ISO inputs such as `DE` and `DEU`. These examples therefore use full country names. Check ISO-code handling separately in your installed version.

The offered groups, including EU, Schengen and NAFTA, come from the card implementation. Check the country membership implemented in your version before using a group for a business rule.
