# Transformation Rules: Complete Practical Overview

> Known preview limitation (checked on 29 October 2026, version 11.15.2): when adding the prefix `INV-`, the preview incorrectly changes `INV-4711` to `INV-INV-4711`. The independently checked server test retains `INV-4711`. Check repeated execution with a server test as well; a correct preview result alone does not prove the complete save-time execution.

Review date: October 28, 2026. Examples were verified with synthetic training values on Dev NOVA. A preview is not proof of a saved document change, a purchase order match, or an ERP export.

## Four Scopes

| Scope | Input and Target | Typical Task |
| --- | --- | --- |
| Header field | One field per document; source can be another header field | Clean invoice number, carry over purchase order number |
| Table column | The selected column for each row of the selected table | Standardize item numbers or unit codes |
| Table rows | Entire table | Remove rows or add defined positions |
| Routing | Document attribute `sub_org_id` | Assign existing sub-organization |

The scopes run **Header field → Routing → Table rows → Table column**. Within a scope, priority and rule key determine the order. The steps of a rule run from top to bottom. A subsequent rule can therefore read already modified values. The order of scopes is not reversed by the priority of an individual rule.

## All Steps of the Editor

The reviewed editor offers 14 value steps for header/column, two steps for entire tables, and one fixed assignment in routing. `fix_value` and the fixed routing assignment both use `set_value` server-side. Additionally, the interface knows `default`; this step is not offered in the reviewed normal step menu.

| Step | Variants and Parameters | Example | Limit and Verification |
| --- | --- | --- | --- |
| Change case (`case`) | upper, lower, title, capitalize | `inv-4711` → `INV-4711` | Title: `acme gmbh` → `Acme Gmbh`; capitalize: `aCME GMBH` → `Acme gmbh`. Proper names/abbreviations may change in an operationally undesirable way. For `capitalize`, the reviewed browser preview leaves the remainder unchanged, while the server lowercases it; verify server value separately. |
| Trim (`trim`) | both / left / right; character empty = whitespace | `  4711  ` → `4711` | `47 11` is preserved. Left character `0`: `004711` → `4711`, but `000` → empty. Characters are a set, not a complete prefix text. |
| Pad (`pad`) | minimum length, one fill character, left/right | Length 10, left `0`: `4711` → `0000004711` | Already 11 characters remain 11 characters. Right `_`, length 6: `ABC` → `ABC___`. |
| Truncate (`truncate`) | maximum length | Length 10: `ABCDEFGHIJKL` → `ABCDEFGHIJ` | `ABC` remains `ABC`. Truncation loses information and can cause numbers to collapse. |
| Affix (`affix`) | add/remove prefix/suffix | `INV-` + `4711` → `INV-4711` | Existing exact affix is not added twice. Removal only takes effect at the matching edge and respects case. |
| Clean characters (`sanitize`) | keep alphanumeric / letters / digits / alphanumeric + space; alternatively remove character class | `DE 123.456.789` → `DE123456789` | Symbols can be semantically significant. When removing, the input is a regular expression character class; protect hyphen correctly, e.g. `.\-/`. |
| Substring (`substring`) | start + length **or** start + end; negative indices possible | Start 3, end 7: `DE-4711-X` → `4711` | Start counts from zero, end is exclusive. Start −4: last four characters. Separate original source required. |
| Extract (`regex_extract`) | regular expression, capture group | `PO[- ]?(\d+)`, group 1: `Order PO-45001234` → `45001234` | First match; group 0 = full match. No match: empty. Separate source required. |
| Find and replace (`regex_replace`) | pattern, replacement, count | `\s+` → space: `ACME    GmbH` → `ACME GmbH` | Count 0 = all, 1 = first match. Separate source required. Verify browser/server regular expression separately for complex patterns. |
| Map values (`value_map`) | complete from→to pairs; ignore case; replacement without match | `stk` → `PCE` with `STK→PCE` and ignored case | Empty replacement means **keep input**. `BOX` remains `BOX`; a fixed replacement `C62` would overwrite `BOX`. Trimming does not occur automatically. |
| Format date (`date_format`) | output pattern, e.g. `%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y` | `2026-10-28` → `28.10.2026` in text target | For DATE header fields, the saved value may remain ISO and only the display changes. Unreadable text remains unchanged; the server test states the reason. |
| Format number (`number_format`) | de_DE / en_US / en_GB / fr_FR; min./max. decimal places | `1234.5` → `1234,50` or `1234.50` in the reviewed server result | No thousands separator in the reviewed server result. No currency or quantity conversion. Verify rounding and reprocessing separately. |
| Fixed value (`fix_value` in editor, `set_value` in API) | one fixed value | `USD` → `EUR` | Overwrites existing values as well. Do not confuse with a default value. |
| Clear (`clear`) | no parameters | `Altwert` → `""` | Empties the value; does not delete field definition or document. |
| Delete all rows (`clear_rows`) | table rows only | 2 positions → 0 | Can invalidate row references and existing PO match. |
| Add row (`add_row`) | beginning/end; per column fixed value or header source | Quantity `1`, net amount from `header.total_net_amount` | Without prior deletion only with appropriate one-time execution. No automatic aggregation of existing positions. |
| Fixed sub-organization (`set_value`, routing) | existing target from the sub-organization selection | Supplier A → sub-organization North | No arbitrary status/user/permission attribute. Alternatively assign via `value_map` and source. |

### Default Value via API

`default` supplements its value only for missing/empty input. With default `1`, `null` and `""` yield the value `1`; `0` remains `0`, `100` remains `100`. This is verified server-side. The normal editor has no dedicated step for this in the reviewed state. The operationally corresponding simple case can often be mapped with **target is empty → fixed value**. This is a rule condition with assignment, not a hidden menu item.

## Nine Detailed Practical Sequences

- [01 · Basics, Scopes, and Safe Testing](01-foundations.md)
- [02 · Clean Text: Case, Trim, and Characters](02-text-cleaning.md)
- [03 · Shape Numbers: Pad, Truncate, Prefix and Suffix](03-numbers-and-affixes.md)
- [04 · Substrings and Patterns: Cut, Extract, Replace](04-substrings-and-patterns.md)
- [05 · Value Mappings and Rules per Table Row](05-value-mapping.md)
- [06 · Format Dates and Numbers Correctly](06-dates-and-numbers.md)
- [07 · Carry Over Fields, Fixed Values, Clear, and Default Values](07-field-copy-and-defaults.md)
- [08 · Rebuild Table Rows](08-table-rows.md)
- [09 · Routing, Order, Master Data, and Repetitions](09-routing-and-execution.md)

| Sequence | Content | Concrete Verification Point |
| --- | --- | --- |
| 01 Basics | Target, source, four scopes, pipeline, conditions, preview, saving | Matching case, counter-case, saved rule reopened |
| 02 Text cleaning | All four cases, trimming, all cleaning modes | Internal spaces, pure zero sequence, semantically significant characters |
| 03 Numbers | Padding, truncation, all four affix variants | Number too long, prefix already present, duplicate prefixes |
| 04 Patterns | Substring, negative indices, extraction/groups, replacement/count | Separate source, no match, multiple matches |
| 05 Mapping | Pairs, case, replacement, application per row | `STK→PCE`, unknown `BOX`, reapplication to `PCE` |
| 06 Formats | Date, DATE vs. text, unreadable date, number formats | Actual server value instead of assumed browser display |
| 07 Field carry-over | Other source, empty target, fixed value, clear, API default value | Protect existing correct purchase order number; zero remains zero |
| 08 Tables | Delete, add, static and dynamic column values | Order, repetition, row count and PO references |
| 09 Interaction | Routing, phases, lookup, one-time execution, logs | Cleaned header source, skipped condition, second save |

## Conditions and Sources

With "Always" the rule applies without operational restriction for the document type. "Only if…" limits it through conditions. Header values are available in the context `header.*`, document characteristics in `doc.*`; `row.*` is only available in the row context of a column rule. Nested AND/OR groups allow combined criteria. For the individual operators, the separate documentation of rule conditions applies.

**Example field carry-over:** Target `purchase_order`, source `header.invoice_id`, condition `header.purchase_order` is empty, steps Trim → Uppercase. `  po-4711  ` yields `PO-4711`. An already correctly filled purchase order number should remain unchanged. Do not empty the wrong source: copying with processing does not move the source.

**Example item number:** Table `INVOICE_TABLE`, column `ITEM_NUMBER`, remove prefix `Art.-Nr. ` → keep alphanumeric → uppercase. `Art.-Nr. ab-12/3` yields `AB123`. Only suitable if the target system expects exactly this form.

**Example total row:** For a clearly delimited supplier first `clear_rows`, then `add_row`; `POSITION=001`, `QUANTITY=1`, `NET_AMOUNT` from the header net amount. Whether a purchase order match against the total sum is operationally correct is determined by the additional PO configuration and a separate match test.

## Repetition and One-Time Execution

Rules can run in multiple processing passes and upon saving again. Always verify **the entire pipeline**, not just the stability of an individual step.

* `substring`, `regex_extract`, and `regex_replace` must not read their own target value in the reviewed server contract. A separate source is required; `run_once` does not override this requirement.
* Adding an already existing exact affix is stable. Removing a multiply present prefix, however, can remove further with each pass.
* `A→B` and `B→C` in the same value mapping can eventually make `A` into `C` after two passes. Test outputs again as inputs.
* `clear_rows → add_row` rebuilds a table in a limited way. `add_row` without prior deletion requires appropriate one-time execution, otherwise the table grows with each save.
* "Run only once per document" marks an actually applied rule. Unfulfilled conditions do not consume the application. Without reliably readable document/application proof, execution of a one-time rule is deferred.

## After Lookup and Before Purchase Order Match

"Also run after master data lookup" adds a phase after lookup population and before PO match. Only rules marked accordingly run in this additional phase. The remaining passes remain. Combined with one-time execution, the rule waits for the later phase during the first extraction pass; if the lookup phase fails, a later regular pass comes into consideration. The phase display of the current editor shows these differences.

## A Robust Acceptance Test

1. Define operational target, target system format, and scope.
2. Prepare a matching raw value, a counter-case, an empty value, and an already processed result.
3. Verify conditions and all intermediate values in the preview.
4. Execute server-side test against the same example; compare complex patterns and number/date formats particularly.
5. Save and reopen rule. Only deploy an active rule within the intended test scope.
6. Save on an isolated document, reload and verify value and display; for tables also row count and column values.
7. Save once more. The result must not be unintentionally further modified or multiplied.
8. If operationally required, additionally verify PO match and actual receipt in the target system. A transformation log alone does not prove these results.

## What a Transformation Does Not Automatically Handle

No new OCR recognition, no mathematical unit or currency conversion, no arbitrary table aggregation, and no complete ERP posting. Routing is limited to the offered document attribute. Availability and exact display depend on the deployed version, document type, and organization configuration.

## Consistent Practice Document

{% file src="../../../../../.gitbook/assets/transformation-training-invoice-en-20261028.pdf" %}
Download training invoice
{% endfile %}

The fictitious document contains two positions, different cases of the unit, and a purchase order reference in free text. For reproducible rule tests, the initial values are prepared deliberately; this is not proof of an automatically error-free OCR extraction.
