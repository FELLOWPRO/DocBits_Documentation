# How documentation search works

The Settings Assistant looks for relevant information in the public pages on [docs.docbits.com](https://docs.docbits.com). Results can include a page title, a short passage, and a link to the source page. Open the link when you need the complete instructions or a screenshot.

## Finding the right page

The search combines word matching with meaning-based matching. This helps when your question uses different words from a page title. The assistant may also use the settings page you are viewing to make the answer more relevant.

If meaning-based search is temporarily unavailable, the documentation search can still use word matching. A specific question with the name of the setting is the best way to retry.

## Languages

Documentation search currently uses the **English** and **German** help-page indexes. When your DocBits interface uses another language, the assistant falls back to English documentation results. The linked page shows its own language; check that language before following steps or comparing screenshots.

## When changes become searchable

The search index is refreshed when English or German documentation changes are published from the documentation repository. A regular reconciliation also removes links to pages that are no longer in the documentation navigation. A newly published page may take a short time to appear in the assistant.

### Technical overview for administrators

Published help pages are split into sections and stored in a dedicated **OpenSearch documentation index** for each supported language. This index is separate from the indexes used for an organization's uploaded documents. When a page changes, unchanged sections can be skipped and changed sections are indexed again. Removed pages are deleted from the documentation index.

For a question, the service combines keyword matches with vector similarity, then orders the most relevant passages. If the embedding service is unavailable, keyword search remains available. The Settings Assistant receives source links and short passages from this documentation search; it does not read an organization's document index for this purpose.

If you cannot find a page, search [docs.docbits.com](https://docs.docbits.com) directly, try a more precise question, or contact DocBits support.

{% hint style="info" %}
This search covers DocBits help pages. The [Fulltext Search](../document-processing/module/fulltext-search.md) feature searches your organization's documents and has separate settings.
{% endhint %}

Return to [using the Settings Assistant](README.md).
