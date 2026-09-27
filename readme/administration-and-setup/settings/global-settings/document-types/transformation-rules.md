# Transformation Rules

## Overview

Transformation rules clean up or rewrite extracted data **automatically** — a field in the header, a column in a table, whole table rows, or an attribute of the document — every time a document is processed and every time it is saved. They replace the small scripts many organisations used to write for "always trim this field", "default this column to 1", "map this supplier's unit codes" or "collapse the line items of this supplier into one total line".

A rule is defined per **document type** and runs on every document of that type. Rules run **before** validation, scripts and purchase order matching, so everything downstream already sees the transformed values.

## How to access

1. Navigate to **Settings → Global Settings → Document Types**.
2. Open the document type and choose **Transformation Rules**. The list shows every rule of the type with its scope, target, priority and whether it is active.
3. Click **New rule** to open the rule builder, or open an existing rule to change it.

## Anatomy of a rule

| Part              | What it is                                                                                                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name / key**    | The display name shown in lists, messages and the matching history, and a technical key that stays stable when you rename the rule.                                                                                              |
| **Scope**         | Where the rule writes: a **header field**, a **table column**, a **table** (whole rows) or a **document attribute**. See below.                                                                                                  |
| **Target**        | The field, column (with its table) or table the rule writes to.                                                                                                                                                                   |
| **Source**        | Optional. Where the rule reads its input from instead of the target itself: `header.<field>` for a header field, `doc.<attribute>` for a document attribute, `row.<column>` for another column of the same row (column scope only). |
| **When**          | **Always**, or **only when** a condition is true (see Conditions).                                                                                                                                                                 |
| **Actions**       | The list of transformations, applied in order; the output of one action is the input of the next.                                                                                                                                 |
| **Priority**      | Rules of the same scope run in ascending priority (then by key). Use it when one rule must see the result of another.                                                                                                              |
| **Run once**      | The rule applies to a document **at most once**. Needed for actions that would change the value again on every save (substring, regex replace, regex extract) and for table rules that should not rebuild the lines again.        |
| **Log execution** | Writes one log line per application — useful while you tune a new rule.                                                                                                                                                           |

### Scopes

| Scope                  | Writes to                                                  | Typical rule                                                                            |
| ---------------------- | ---------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| **Header field**       | one extracted header field (invoice number, currency, …)   | trim and upper-case the invoice number; map "EUR€" to "EUR"                             |
| **Table column**       | one column in every row of a table                         | default `UNIT_PRICE_PER` to 1; strip the "Art.-Nr." prefix from the item number         |
| **Table**              | the rows of a table                                        | clear the lines and add one total line for a supplier that is matched on the total       |
| **Document attribute** | an attribute of the document itself (currently the sub-organisation) | route documents of a supplier to a sub-organisation                                      |

Rules run scope by scope in this order: header → document → table → column. A column rule therefore already sees rows that a table rule added.

### Conditions ("only when")

A condition compares a value of the document with a constant. The value comes from a header field (`header.<field>`), a document attribute (`doc.<attribute>`) or, for column rules, a column of the current row (`row.<column>`).

| Operator                          | Meaning                                    |
| --------------------------------- | ------------------------------------------ |
| is / is not                       | exact comparison                           |
| is one of / is not one of         | value in a list                            |
| contains, starts with, ends with  | text comparison                            |
| is empty / is not empty           | no value needed                            |
| greater than, less than, at least, at most | numeric comparison                 |
| matches                           | regular expression                         |

Conditions can be grouped with **all of** (and) and **any of** (or) and negated with **not**. Example: _only when `header.supplier_id` is `20723`_ — the rule runs for one supplier only.

### Actions

Actions for header fields and table columns (they form a pipeline; the value goes in at the top and comes out at the bottom):

| Action             | Effect                                                                                                              |
| ------------------ | ------------------------------------------------------------------------------------------------------------------- |
| `trim`             | remove whitespace (or given characters) on the left, right or both sides                                            |
| `case`             | upper, lower, title or capitalize                                                                                   |
| `pad`              | pad to a length with a character, left or right                                                                     |
| `truncate`         | cut to a maximum length                                                                                             |
| `affix`            | add a prefix or suffix, or strip one                                                                                |
| `sanitize`         | keep only a character class (alphanumeric, alpha, numeric, alphanumeric + space) or strip a set of characters        |
| `substring`        | take a part of the value by start and length or end                                                                 |
| `regex_replace`    | replace what a regular expression matches                                                                           |
| `regex_extract`    | keep what a regular expression captures                                                                             |
| `value_map`        | map values to other values (optionally case-insensitive, with a default)                                            |
| `date_format`      | re-format a date (the input must be the ISO date DocBits stores in `value`)                                         |
| `number_format`    | re-format a number                                                                                                  |
| `default`          | set a value only when the field is empty                                                                            |
| `set_value`        | set a fixed value, whatever the field contained                                                                     |
| `clear`            | empty the field                                                                                                     |

Actions for **table** scope (they work on rows, not on values, and cannot be mixed with the actions above):

| Action       | Effect                                                                                                                             |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| `clear_rows` | delete every row of the table                                                                                                      |
| `add_row`    | add one row at the end or the start; every column gets either a fixed value or a value read from the header (`header.<field>`) or the document (`doc.<attribute>`) |

{% hint style="info" %}
`substring`, `regex_replace` and `regex_extract` change a value again when they run on an already transformed value. Combine them with **Run once**, or write the regular expression so that a second run has nothing left to change.
{% endhint %}

## When rules run

* During processing, after extraction and before validation, scripts and purchase order matching.
* On **every save** of the document in which the extracted data changed. Rules without **Run once** are applied again on each save; because every action except the three above is idempotent, a value that is already in the target form stays as it is.

## Transformation rules and purchase order matching

Table rules and column rules change what the PO matcher sees:

* A table rule that **rebuilds** lines (for example clear all rows and add one total line) keeps an existing purchase order match as long as it produces the **same lines again** — values are compared by meaning, so `1.0` and `1.00` are the same line. The lines keep their identity and the match survives every save.
* If a rule **replaces or removes lines that were matched**, the match cannot be kept. The document then records which rule dropped it, the Purchase Order Matching screen shows this as the reason ("_The PO match could not be saved: the transformation rule "…" rebuilt the table_") and administrators get a link to the rule. The **matching history** of the document shows a _Transformation rules_ step before the first matching stage with the rules that ran.
* The number of lines after the rules is what the [activation conditions](more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) of the matching rules count. A rule that collapses an invoice into **one** line only makes sense together with a match-on-total rule that is active for one-line documents (`[[count(table_lines)]] >= 1`).

## Examples

**Clean the invoice number** — header field `invoice_id`, always: `trim` → `case` upper.

**Default the price basis** — table column `UNIT_PRICE_PER` of the line-item table, always: `default` `1`.

**Map a supplier's unit codes** — table column `UNIT` of the line-item table, only when `header.supplier_id` is `10040`: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**One total line for a supplier that is matched on the total** — table scope on the line-item table, only when `header.supplier_id` is `20723`: `clear_rows`, then `add_row` with `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Pair it with a match-on-total rule whose activation condition accepts one document line.

**Route a supplier to a sub-organisation** — document attribute `sub_org_id`, only when `header.supplier_id` is one of `[…]`: `set_value` `<sub-organisation id>`.

## Troubleshooting

| Symptom                                                    | What to check                                                                                                                                                                              |
| ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| The rule did not change anything                           | Is it active? Does the document type match? Is the condition true for this document (compare the exact value, including spaces)? Has a **Run once** rule already been applied to the document? |
| The value changes again on every save                      | The pipeline contains `substring`, `regex_replace` or `regex_extract`. Switch on **Run once** or make the expression idempotent.                                                              |
| The purchase order match is lost after saving              | A table rule replaced the matched lines. The reason on the document names the rule; make the rule reproduce the same lines, or set it to **Run once**.                                        |
| A matching rule never runs after the transformation        | The rule changed the number of lines; adjust the activation condition of the matching rule.                                                                                                |
