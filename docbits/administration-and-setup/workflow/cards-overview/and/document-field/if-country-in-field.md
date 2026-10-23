# If Country in Field

<figure><img src="../../../../../.gitbook/assets/image (55).png" alt="Workflow And card that checks whether the country in a field matches a value" width="563"><figcaption></figcaption></figure>

Intended use: an additional processing step depends on a country group. The example below describes a rule for membership of the European Union.

## Current limitation — development source checked on 22 October 2026

Local source tests using the native region-selection type fail before comparing the country, returning `missing_variable` or `error`. Full country names do not bypass this problem. A successful run on the deployed backend has not been verified for this version.

**Where:** Standard workflow → additional conditions (AND) → Document Field. Configure the subsequent action separately under THEN.

## Configuration — version 2

| Setting | Value |
| --- | --- |
| Field | An existing text field containing the country name |
| Operator | `is` |
| Region | European Union (EU) |
| Continue value | `true` |

<!-- workflow-card-practical-example-20261021 -->

## Intended example — verify the fix before use

Verify the correction and both example cases in your installed version before enabling this rule. The table describes the intended business rule, not a confirmed successful execution.

| Country field value | Intended country grouping |
| --- | --- |
| `Germany` | Inside the EU |
| `United States` | Outside the EU |

The country names shown as code are fixed input values for this example.

## Limits and checks

`false` does not invert the comparison. Even a matching country does not produce a positive condition with that setting. To check the opposite condition, select `isnot` with `true`.

Handle missing fields and empty country values separately; they can return a missing-data result rather than an ordinary non-match.

The ISO conversion issue for inputs such as `DE` and `DEU` is separate. Replacing ISO codes with full country names does not resolve the region-selection error.

The offered groups, including EU, Schengen and NAFTA, come from the card implementation. Check the country membership implemented in your version before using a group for a business rule.
