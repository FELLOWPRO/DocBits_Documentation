# Web Address Changes

The web addresses (URLs) you use to reach pages in DocBits have been cleaned up and made consistent. This page explains what changed, why your old links still work, and how to find any page under its new address.

## What changed

Web addresses in DocBits now follow one clear pattern: the thing you are working on comes first, then the view of it. For example, a document's validation screen is now:

```
/documents/<document-id>/validation
```

instead of the old:

```
/field_validation_v1/<document-id>
```

Over time, some screens ended up with several different versions and addresses — for instance, approval had separate addresses for the first approval, the second approval, and older versions of each. These now share a single address, and DocBits automatically shows the right version for your organisation. You no longer need to know or guess which version applies to you.

Addresses now also use lowercase words separated by hyphens only, instead of a mix of underscores, capital letters, and abbreviations.

## Your old links still work

You do not need to change anything right away. Bookmarks, links saved in emails, and links saved anywhere else keep working exactly as before. When you open an old address, DocBits automatically forwards you to its new address — including any filters or options that were part of the original link.

After you are forwarded, the browser's address bar shows the new address. That is expected: it means the forwarding worked. Over time, we recommend updating your saved bookmarks to point directly at the new addresses, so you get there without the extra forwarding step. But there is no deadline — the old addresses will keep working.

## Finding a page

If you are not sure what the new address for a page is, or you just want to jump straight to something, there are three ways to find your way around:

* **Sitemap.** The [Sitemap](sitemap.md) page lists every page in DocBits, grouped by area, with a search box and filters. Open it from the sidebar, or from Global Quick Search by choosing **View all results**.
* **Global Quick Search.** Press <kbd>Cmd</kbd> + <kbd>K</kbd> on a Mac or <kbd>Ctrl</kbd> + <kbd>K</kbd> on Windows from anywhere in DocBits, then type the name of what you are looking for. See [Global Quick Search](global-quick-search.md) for details.
* **The page-not-found screen.** If you type or paste only the first part of an address — for example `/documents` or `/analytics` — without the rest, DocBits shows a page-not-found screen listing every page that lives under that address. It works like an index for that group of pages, and it has the same search box as Global Quick Search, so you can search from there too.

## Old and new addresses

The table below lists every address that changed, grouped by area. Where several old addresses now lead to the same new one, each old address is listed on its own row. Addresses used only by developers (for example debugging or demo pages) are not listed, since they do not affect day-to-day use.

Placeholders in the table stand for real values:

* `<document-id>` — a document's ID
* `<task-id>` — a task's ID
* `<workflow-id>` — a workflow's ID
* `<document-type>` — a document type, such as invoice or purchase order
* `<file-name>` — a file name
* `<order-number>` / `<sales-order-id>` — a purchase or sales order reference
* `<organisation-id>` — an organisation ID
* `<layout-type>` — a layout type
* `<supplier-id>` — a supplier's ID
* `<page>` — a page number

### Documents

| Old address | New address |
|---|---|
| `/document/<document-id>` | `/documents/<document-id>` |
| `/field_validation_v1/<document-id>` | `/documents/<document-id>/validation` |
| `/field_validation/<document-id>` | `/documents/<document-id>/validation` |
| `/medi_order_v3/<document-id>` | `/documents/<document-id>/validation` |
| `/ready_for_approval_v3/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-approval-v2/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-approval/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval-v3/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval-v2/<document-id>` | `/documents/<document-id>/approval` |
| `/ready-for-second-approval/<document-id>` | `/documents/<document-id>/approval` |
| `/in_review/<document-id>` | `/documents/<document-id>/review` |
| `/in-review-v2/<document-id>` | `/documents/<document-id>/review` |
| `/rejected/<document-id>` | `/documents/<document-id>/rejected` |
| `/summary/<document-id>` | `/documents/<document-id>/summary` |
| `/tbl_ext_v3/<document-id>` | `/documents/<document-id>/table-extraction` |
| `/tbl_training/<document-id>` | `/documents/<document-id>/table-training` |
| `/table_train_v3` | `/table-training` |
| `/doc_flow/<document-id>` | `/documents/<document-id>/flow` |
| `/document_pdf/<file-name>/<document-id>` | `/documents/<document-id>/pdf/<file-name>` |
| `/document_error/<document-id>` | `/documents/<document-id>/error` |
| `/document_classifiy/<document-id>` | `/documents/<document-id>/classify` |
| `/accounting/<document-id>` | `/documents/<document-id>/accounting` |
| `/quote-details/<document-id>` | `/documents/<document-id>/quote` |
| `/vertex-details/<document-id>` | `/documents/<document-id>/vertex` |
| `/po-matching/<document-id>` | `/documents/<document-id>/po-matching` |
| `/po-matching-v3/<document-id>` | `/documents/<document-id>/po-matching-v3` |
| `/ocr-document/<document-id>/<page>` | `/documents/<document-id>/ocr/<page>` |
| `/fields_sep_comp_v3/<document-id>` | `/documents/<document-id>/window/medi-fields` |
| `/simple_fields_comp/<document-id>` | `/documents/<document-id>/window/fields` |
| `/show_pdf/<document-id>` | `/documents/<document-id>/window/pdf` |

### Tasks

| Old address | New address |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### Workflows

| Old address | New address |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### Orders and invoices

| Old address | New address |
|---|---|
| `/purchase-order` | `/supplier/purchase-orders` |
| `/purchase-order-detail/<order-number>` | `/supplier/purchase-orders/<order-number>` |
| `/sales_order_detail/<sales-order-id>` | `/sales-orders/<sales-order-id>` |
| `/asn_shipment` | `/shipments/asn` |
| `/asn_shipment/dashboard` | `/shipments/asn` |
| `/shipment-order` | `/shipments/orders` |
| `/invoice/dashboard` | `/invoices` |
| `/invoice/details/<document-id>` | `/invoices/<document-id>` |
| `/accounting_range` | `/accounting/range` |

### Analytics and search

| Old address | New address |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### Shared links

| Old address | New address |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### Account and sign-in

| Old address | New address |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### Layouts

| Old address | New address |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
