# Quick Search

**Quick Search** is the fastest way to find documents on the Dashboard. You
type what you're looking for — a name, a status, an amount, a date — and the
document list filters instantly.

This guide is organised the way the search is built up:

1. **Standard fields** — the columns every document has (document name, status,
   dates). Always available.
2. **Fulltext fields** — extracted content (supplier, purchase order, invoice
   number, amounts, line items). Available when fulltext search is enabled.
3. **Operators, shortcuts & recipes** — the full reference once you're
   comfortable.

> You don't have to memorise anything: click the search bar and pick a field and
> value from the list — Quick Search builds the query for you. The examples below
> also show the typed form so you can copy them directly.

<figure><img src="../../../.gitbook/assets/quick_search_01_entry.png" alt="The Quick Search bar at the top of the Dashboard"><figcaption><p>The Quick Search bar at the top of the Dashboard.</p></figcaption></figure>

---

## Part 1 — Standard fields

Standard fields are the document's own columns. They are **always available**,
whether or not fulltext search is switched on.

### Find documents by name

The document name is the most common search. There are three ways to match it —
all **case-insensitive**:

#### `=` → starts with

```
filename=invoice
```

Finds documents whose name **starts with** "invoice": `Invoice.pdf`,
`invoice_2026.xml`, `INVOICE-001.pdf`.

<figure><img src="../../../.gitbook/assets/quick_search_02_filename_starts.png" alt="filename=invoice matches only names that start with invoice"><figcaption><p><code>filename=invoice</code> — only names that <strong>start with</strong> "Invoice" (3 results). Compare with <code>:</code> below, which returns far more.</p></figcaption></figure>

#### `:` → contains (anywhere)

```
filename:invoice
```

Use `:` to match the word **anywhere** in the name — `2026_Invoice.pdf`,
`vietnam_einvoice_sample.xml`, `scan_invoice_copy.pdf`.

<figure><img src="../../../.gitbook/assets/quick_search_03_filename_contains.png" alt="filename:invoice matches the word anywhere in the name"><figcaption><p><code>filename:invoice</code> — matches the word anywhere in the document name.</p></figcaption></figure>

#### `="…"` → starts *or* ends with

```
filename="invoice"
```

Quotes make `=` match names that **start or end** with the value — handy for a
leading code or a file ending.

> **The three in one line:** `=` → starts with · `:` → contains · `="…"` →
> starts or ends with. All ignore upper/lower case. You can see this summarised
> any time via the **help icon** in the search bar (next section).

### Find documents by status

```
status=ready_for_validation
```

Status is a fixed list, so `=` is an **exact** match and the bar offers a value
picker when you type `status=`.

<figure><img src="../../../.gitbook/assets/quick_search_05_status.png" alt="Filtering by document status"><figcaption><p><code>status=ready_for_validation</code> — exact match on a fixed-list field.</p></figcaption></figure>

### Find documents by date

```
created_on>2026-05-25
```

Use `>`, `<`, `>=`, `<=` for date ranges. You can also use **relative** dates:
`today()`, `today()-7` (last 7 days), `today()+30` (next 30 days).

<figure><img src="../../../.gitbook/assets/quick_search_06_date.png" alt="Filtering by creation date"><figcaption><p><code>created_on&#62;2026-05-25</code> — documents created after a date.</p></figcaption></figure>

---

## Part 2 — Fulltext fields

Fulltext fields search the **extracted content** of your documents — supplier,
purchase order, invoice number, amounts, line items. They appear in **orange**
and are available when **fulltext search is enabled** for your organisation. The
matching rules are exactly the same as for standard text fields
(`=` starts-with, `:` contains, `="…"` starts-or-ends).

### Find documents from a supplier

```
supplier_name=Test
```

Starts-with on the extracted supplier name. Use `supplier_name:fuji` to match
anywhere, or `supplier_name:"Ruiz Foods"` to quote a value with spaces.

<figure><img src="../../../.gitbook/assets/quick_search_09_supplier.png" alt="Searching by supplier name"><figcaption><p><code>supplier_name=Test</code> — every result's supplier starts with "Test".</p></figcaption></figure>

### Find documents by purchase order

```
purchase_order=PO
```

Starts-with on the extracted PO number — great for a PO prefix.

<figure><img src="../../../.gitbook/assets/quick_search_10_purchase_order.png" alt="Searching by purchase order"><figcaption><p><code>purchase_order=PO</code> — documents whose PO number starts with "PO".</p></figcaption></figure>

### Find documents by amount

```
total_amount>5000
```

Use `>`, `<`, `>=`, `<=`, or `between 100 and 500` for a span.

<figure><img src="../../../.gitbook/assets/quick_search_07_amount.png" alt="Filtering by total amount"><figcaption><p><code>total_amount&#62;5000</code> — invoices above 5,000.</p></figcaption></figure>

For a window, use `between`:

```
total_amount between 1000 and 5000
```

This is shorthand for `total_amount>=1000 AND total_amount<=5000`.

<figure><img src="../../../.gitbook/assets/quick_search_14_between.png" alt="Amount window with between"><figcaption><p><code>total_amount between 1000 and 5000</code> — every result falls inside the window.</p></figcaption></figure>

### Find what's missing

```
supplier_name=""
```

`=""` means "this field is **not set**"; `supplier_name!=""` means "has any
supplier".

<figure><img src="../../../.gitbook/assets/quick_search_12_empty.png" alt="Finding documents with no supplier"><figcaption><p><code>supplier_name=""</code> — documents that have no supplier yet.</p></figcaption></figure>

The same presence check works on any field — for example documents still
missing an AP assignment code:

```
ap_assignment_code=""
```

<figure><img src="../../../.gitbook/assets/quick_search_15_ap_empty.png" alt="Documents missing an AP assignment code"><figcaption><p><code>ap_assignment_code=""</code> — documents that have no AP assignment code. Use <code>ap_assignment_code!=""</code> for those that do.</p></figcaption></figure>

---

## Part 3 — Operators, connectors, shortcuts

### The built-in help

The **help icon** in the search bar opens a complete reference of every field,
operator and shortcut available in your workspace — including which fields are
standard vs. fulltext.

<figure><img src="../../../.gitbook/assets/quick_search_08_help_modal.png" alt="The in-app Dashboard Search help with all operators"><figcaption><p>The built-in <strong>Dashboard Search — Fields &#38; Syntax</strong> help, listing every operator and how values are matched.</p></figcaption></figure>

### How `=` matches, by field type

All text matching ignores case.

| Field type | Example | `=` means |
|------------|---------|-----------|
| Text (name, supplier, purchase order) | `filename=invoice` | **starts with** |
| Text, anywhere | `filename:invoice` | **contains** |
| Text, start *or* end | `filename="invoice"` | **starts or ends with** |
| Status / type / PO match (fixed lists) | `status=finished` | **exact** |
| Identifiers (invoice number, supplier id) | `invoice_number=INV-100` | **exact** |
| Number | `total_amount>5000` | range (`> < >= <= between`) |
| Date | `created_on>2026-01-01` | range + `today()±N` |

### Operators

| Operator | Meaning |
|----------|---------|
| `=` | starts-with (text) / exact (list, number, date) |
| `:` | contains (text, anywhere) |
| `="…"` | starts-with or ends-with (text) |
| `!=` | the opposite of `=` |
| `>` `<` `>=` `<=` | greater / less than |
| `between … and …` | inclusive range |
| `field=""` / `field!=""` | is empty / is set |
| `today()`, `today()-7`, `today()+30` | relative dates |

### Connectors

Combine conditions with **AND** (both true), **OR** (either), **NOT**, and
parentheses `( … )` for grouping:

```
status=ready_for_validation AND supplier_name=Test
(status=error OR status=failed) AND created_on>today()-1
```

<figure><img src="../../../.gitbook/assets/quick_search_13_combined.png" alt="Combining conditions with AND"><figcaption><p><code>status=ready_for_validation AND supplier_name=Test</code> — two conditions combined.</p></figcaption></figure>

### Shortcuts

Shorter phrasings for the same queries — use whichever reads better:

| Shortcut | Same as | Description |
|----------|---------|-------------|
| `total_amount gt 5000` | `total_amount>5000` | Word aliases for comparison operators (`gt`/`gte`/`lt`/`lte`/`eq`/`ne`) |
| `due_date > today` | `due_date>today()` | Bare `today` / `yesterday` / `tomorrow` |
| `imported_on this_week` | `imported_on>=today()-7 AND imported_on<=today()` | Relative periods (`this_week`, `last_week`, `this_month`, …) |
| `ap_assignment_code is empty` | `ap_assignment_code=""` | Whether a field has any value |
| `status:open` | `status=ready_for_validation` | Friendly status label (`open`/`closed`/`failed`/`done`) |
| `total_amount not between 100, 200` | `total_amount<100 OR total_amount>200` | Value outside a window |
| `status in (finished, error)` | `status=finished OR status=error` | Match any value from a list |
| `not status=finished` | `status!=finished` | Negate any predicate |
| `filename contains rechnung` | `filename:rechnung` | String match (`contains`/`starts_with`/`ends_with`) |
| `total_amount > 5k` | `total_amount>5000` | Currency suffix `k` (×1 000), `M` (×1 000 000) |
| `overdue` | `invoice_due_date<today() AND status!=finished` | Unpaid invoices past due |
| `#INV-1234` | `invoice_id:INV-1234` | Twitter-style prefix for invoice id |
| `@User` | `assigned_to:User` | Twitter-style prefix for assignee |
| `$5000+` | `total_amount>=5000` | `$` prefix for amount thresholds |

### Recipes

| You want… | Type this |
|-----------|-----------|
| Ready to validate, fully matched | `status=ready_for_validation AND po_match_status=full_matched` |
| This supplier, this week | `supplier_name=Test AND created_on>today()-7` |
| High-value overdue invoices | `total_amount>5000 AND invoice_due_date<today()` |
| Two suppliers at once | `supplier_name=fuji OR supplier_name=acme` |
| Errored docs from today | `(status=error OR status=failed) AND created_on>today()-1` |
| Electronic credit notes | `is_edoc=true AND sub_doc_type=CREDIT_NOTE` |
| By purchase-order prefix | `purchase_order=PO-2026` |

> Orange (fulltext) fields require **fulltext search** to be enabled for your
> organisation. A literal `%` or `_` in a value is treated as a normal character.
