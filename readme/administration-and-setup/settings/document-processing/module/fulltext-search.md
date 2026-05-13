# Fulltext Search

Fulltext Search lets users search the actual content of documents and every extracted field, not just filenames and IDs.

<figure><img src="../../../../.gitbook/assets/fulltext-search-required-dialog.png" alt="Fulltext Module Required dialog shown when the module is disabled"><figcaption><p>The Fulltext Module Required dialog appears on pages that depend on the module.</p></figcaption></figure>

## Without the module

When Fulltext Search is not enabled, the dashboard search bar can only query a small set of structured fields. Free-text input falls back to matching against:

* `filename`
* Document `ID`
* `invoice_id`
* `purchase_order`

Anything outside these fields is ignored. There is no content-level search and no support for ranges, operators, or smart filters.

## With the module enabled

Activating Fulltext Search unlocks search across every extracted field on a document and replaces the dashboard search bar with a richer query language. Queries can combine field filters, range comparisons, logical operators, relative dates, and smart-filter shortcuts.

<figure><img src="../../../../.gitbook/assets/fulltext-search-dashboard-query.png" alt="Dashboard search bar showing a range query and the resulting filtered document list"><figcaption><p>The dashboard search bar accepts the extended query language. Type a query and press <kbd>Enter</kbd> to filter the document list.</p></figcaption></figure>

### Field-scoped queries

Match a specific extracted field by prefixing the field name with a colon. Field names follow the API identifier convention (lowercase, snake\_case) and apply to every field captured by your document types — supplier, invoice metadata, line items, custom fields.

```
supplier_name: Acme
invoice_id: INV-1234
status: ready_for_validation
```

### Range queries

Use comparison operators on numeric and date fields. Both open-ended comparisons and bounded ranges are supported.

```
total_amount > 5000
total_amount <= 10000
invoice_due_date between 2026-01-01 and 2026-04-30
```

### Logical operators

Combine clauses with `AND`, `OR`, and `NOT`, grouping with parentheses for precedence. `IN`-lists match any value from a set on a single field.

```
supplier_name: Acme AND total_amount > 1000
(status: ready_for_validation OR status: validated) AND invoice_date: this_month
NOT status: archived
status IN (ready_for_validation, exported)
```

### Relative dates

Time expressions evaluated against the query timestamp. Use them anywhere a date is expected.

```
imported_on: today()
invoice_date: last_week
imported_on: this_quarter
```

### Smart filters

Single-token shortcuts for common queries. They work on their own or as part of a larger expression.

```
overdue
@User
#INV-1234
$5k+
```

* `overdue` — documents past their due date.
* `@User` — filter by assignee; replace `User` with the assignee's name.
* `#INV-1234` — quick lookup by document identifier.
* `$5k+` — monetary amounts greater than 5,000 in the document's currency.

## Sub-features

Two specialised search modes are layered on top of the Fulltext module. Both depend on the module being enabled and cannot be used standalone.

### Vector search

Vector search finds documents that are semantically similar to your query rather than only lexically matching. The dashboard treats any query starting with `vector:` as a vector search, runs it through document embeddings, and ranks results by similarity.

```
vector: frozen food invoices
```

Vector indexing is toggled separately from the Fulltext text index on the Fulltext Search Settings page. Disabling it stops embedding new documents while leaving the text index in place.

### AI search

AI search accepts natural-language queries and uses an LLM to extract structured filters, which are then run through the Fulltext index. Prefix the query with `ai:`.

```
ai: invoices from Ruiz over 1000 last quarter
```

AI search and Vector search are not interchangeable: Vector matches similar content, AI translates language into filters. AI search has no separate switch — it routes through the existing Fulltext and Vector indexes.

<figure><img src="../../../../.gitbook/assets/fulltext-search-settings-page.png" alt="Fulltext Search Settings page showing the Documents, Vector Index and Fulltext (text) sub-indexes"><figcaption><p>Fulltext Search Settings. The Vector Index has its own toggle; the Fulltext text index runs whenever the module is on.</p></figcaption></figure>

## Prerequisites

* OpenSearch infrastructure runs in the background to power the index.
* The first time the module is enabled, all existing documents are reindexed. Indexing time scales with the number of documents in the organisation.
* Only organisation admins can toggle modules.

## How to enable

1. Go to **Settings → Document Processing → Module**.
2. Under the **Dashboards** group, enable **Full text search**.
3. Confirm the subscription dialog when it appears.
4. Wait for the initial reindex to finish before relying on Fulltext queries.

<figure><img src="../../../../.gitbook/assets/fulltext-search-module-toggle.png" alt="Modules page with the Full text search toggle under the Dashboards group"><figcaption><p>The Full text search toggle lives under <strong>Module → Dashboards &#x26; Analytics</strong>.</p></figcaption></figure>

{% hint style="info" %}
Pricing for the Fulltext Search module is handled through your DocBits sales contact. The subscription confirmation appears the first time the module is activated.
{% endhint %}

## See also

* [Fulltext Search Settings](../../log-settings/fulltext-search-settings.md) — index management and the Vector Index toggle.
* [Fulltext Search Functions](../../global-settings/document-types/script/scripting-in-docbits/fulltext-search-functions.md) — scripting API for `fulltext_search()` and `vector_search()`.
* [Modules overview](README.md) — full list of optional DocBits modules.
