---
description: "P1: Calculate table columns and check regex dependencies"
---

# P1: Calculate table columns and check regex dependencies

**Calculate Columns** calculates two columns within a row and writes the result column. **Calculate in / CALC_COLUMNS_REGEX** adds a regex condition on a third column. Here the regex decides whether to calculate; it neither extracts nor replaces text. The earlier replacement explanation does not describe this card.

Example: `QTY=2`, `PRICE=10`, operation `*`, result `TOTAL=20.0`. For the regex variant use `TYPE` and pattern `^A$`. An A row is calculated. For a nonmatching B row, the inspected code writes an empty result; an existing TOTAL is not automatically preserved.

The arithmetic helper rounds numeric results to four decimal places. An individual empty operand can become 0; two empty strings return empty. With `+`, nonnumeric text can be concatenated. In the inspected helper, `10/0` raises an error. Validate numbers and required cells before calculation and provide an error route.

Keep a complete before/after table: two matching rows, one nonmatching regex row, empty input, invalid text and division by zero. For dependent A→B calculations, connect the cards explicitly and inspect the updated value read by the second card. Compare every row and unrelated existing columns, not only document status.

## Cards and example parameters

These values describe individual card parameters, not an importable complete workflow. Replace YOUR_* with your own test selections. The designer manages the hidden caller ID. Catalog: Dev, DocFlow 2.10.38, 21 October 2026; check available versions and entitlements in your own organization.

### `calc_columns` · v2

Identity: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

Identity: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| Parameter | Type / choices | Example |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## Business test cases

| Case | Input / setup | Expected outcome |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## Evidence and limits

Parameters and behavior were checked against the Dev catalog and inspected source revision. Business test cases are an acceptance procedure. Personal approvals, real data changes and delivery were not performed for this chapter.

[Continue learning](../workflow-learning-path.md) · [Training kit](../workflow-training-kit.md)
