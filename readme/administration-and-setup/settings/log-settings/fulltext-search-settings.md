# Fulltext Search Settings

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Fulltext Search Settings"><figcaption><p>Fulltext Search Settings — Module Required Dialog</p></figcaption></figure>

Fulltext Search Settings configures what DocBits indexes and how it makes that content searchable across documents, ERP master data, and templates. The settings page only opens when the **Fulltext Search module** is enabled — see [Fulltext Search](../document-processing/module/fulltext-search.md) for the user-facing query language.

## Prerequisites

The Fulltext Search module must be activated in **Settings → Document Processing → Module → Dashboards → Full text search**. If the module is not enabled, a dialog prompts you to either:

* **Go to Modules** — Navigate to the Module settings page to review the configuration.
* **Enable Now** — Activate the Fulltext Search module directly (starts a DocSearch subscription).

The settings page itself becomes available once the module is active.

## Page layout

The settings page is organised into three tabs, each scoping a different content type that Fulltext Search can index.

### Documents tab

The Documents tab covers everything related to indexing processed documents:

* **Indexing statistics** — totals for documents indexed and pending, refreshed on demand.
* **Vector preferences** — three organisation-level toggles that control whether vector indexing runs alongside the text index for documents. Vector indexing powers the `vector:` query mode and the "Find Similar" feature.
* **Reindex actions** — start a full or incremental reindex. While a reindex runs, you see live progress (documents per minute, ETA), the current stream status, and the last failure (if any).
* **Sync diagnostics** — on-demand diagnostics for cases when the index appears out of sync with the underlying document store.

<mark>Reindexing is non-destructive — existing search continues to work while the new index is being rebuilt.</mark>

### ERP tab

The ERP tab controls indexing for ERP master data — suppliers, customers, items, and similar entities. Each entity has its own toggle:

* **Indexing** — text-index the entity so it is searchable from the dashboard.
* **Vector** — vector-index the entity so it can be matched by semantic queries.

Use the **Toggle all** action at the top of the list to apply the same on/off state to every entity at once. Indexing kicks off in the background; an indicator on each row shows when it is in progress.

### Templates tab

The Templates tab lists the template versions known to the Fulltext index. Use this view to confirm that the template versions you depend on are present in the index after a redeploy.

## What gets indexed

Once enabled and configured, Fulltext Search lets users:

* Search across all document content (not just metadata fields).
* Find documents by text contained within uploaded files.
* Use advanced search operators for precise queries.
* Access search results directly from the dashboard.
* Use semantic search (`vector:` prefix) when vector indexing is on for that content type.

See the [Fulltext Search](../document-processing/module/fulltext-search.md) module page for the complete query language reference, including range queries, smart filters, and the AI search mode.
