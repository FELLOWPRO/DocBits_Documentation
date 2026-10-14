# Wijzigingen in webadressen

De webadressen (URL's) waarmee u pagina's in DocBits bereikt, zijn opgeschoond en consistent gemaakt. Deze pagina legt uit wat er is veranderd, waarom uw oude links nog werken en hoe u elke pagina onder het nieuwe adres vindt.

## Wat is er veranderd

Webadressen in DocBits volgen nu één duidelijk patroon: eerst het onderdeel waarmee u werkt, dan de weergave ervan. Het validatiescherm van een document is bijvoorbeeld nu:

```
/documents/<document-id>/validation
```

in plaats van het oude:

```
/field_validation_v1/<document-id>
```

In de loop der tijd kregen sommige schermen meerdere versies en adressen — goedkeuring had bijvoorbeeld aparte adressen voor de eerste goedkeuring, de tweede goedkeuring en oudere versies van beide. Die delen nu één enkel adres en DocBits toont automatisch de juiste versie voor uw organisatie. U hoeft niet meer te weten of te raden welke versie voor u geldt.

Adressen gebruiken nu ook uitsluitend kleine letters en woorden gescheiden door streepjes, in plaats van een mix van underscores, hoofdletters en afkortingen.

## Uw oude links werken nog

U hoeft niet direct iets te wijzigen. Bladwijzers, links in e-mails en links die ergens anders zijn opgeslagen blijven precies zo werken als voorheen. Wanneer u een oud adres opent, stuurt DocBits u automatisch door naar het nieuwe adres — inclusief alle filters of opties die deel uitmaakten van de oorspronkelijke link.

Nadat u bent doorgestuurd, toont de adresbalk van de browser het nieuwe adres. Dat is normaal: het betekent dat het doorsturen is gelukt. We raden aan om uw opgeslagen bladwijzers na verloop van tijd bij te werken zodat ze rechtstreeks naar de nieuwe adressen verwijzen en u de extra doorstuurstap overslaat. Maar er is geen deadline — de oude adressen blijven werken.

## Een pagina vinden

Als u niet zeker weet wat het nieuwe adres van een pagina is, of gewoon direct ergens naartoe wilt, zijn er drie manieren om uw weg te vinden:

* **Sitemap.** De pagina [Sitemap](sitemap.md) toont elke pagina in DocBits, gegroepeerd per gebied, met een zoekvak en filters. Open hem via de zijbalk, of via Global Quick Search door **View all results** te kiezen.
* **Global Quick Search.** Druk overal in DocBits op <kbd>Cmd</kbd> + <kbd>K</kbd> op een Mac of <kbd>Ctrl</kbd> + <kbd>K</kbd> op Windows en typ de naam van wat u zoekt. Zie [Global Quick Search](global-quick-search.md) voor details.
* **Het scherm Pagina niet gevonden.** Als u alleen het eerste deel van een adres typt of plakt — bijvoorbeeld `/documents` of `/analytics` — zonder de rest, toont DocBits een scherm "pagina niet gevonden" met alle pagina's die onder dat adres vallen. Het werkt als een index voor die groep pagina's en heeft hetzelfde zoekvak als Global Quick Search, zodat u ook vanaf daar kunt zoeken.

## Oude en nieuwe adressen

De onderstaande tabellen tonen elk adres dat is gewijzigd, gegroepeerd per gebied. Waar meerdere oude adressen nu naar hetzelfde nieuwe adres leiden, staat elk oud adres op een eigen rij. Adressen die alleen door ontwikkelaars worden gebruikt (bijvoorbeeld debug- of demopagina's) staan er niet bij, omdat ze het dagelijkse gebruik niet beïnvloeden.

Plaatshouders in de tabel staan voor echte waarden:

* `<document-id>` — de ID van een document
* `<task-id>` — de ID van een taak
* `<workflow-id>` — de ID van een workflow
* `<document-type>` — een documenttype, zoals factuur of inkooporder
* `<file-name>` — een bestandsnaam
* `<order-number>` / `<sales-order-id>` — een referentie van een inkoop- of verkooporder
* `<organisation-id>` — een organisatie-ID
* `<layout-type>` — een lay-outtype
* `<supplier-id>` — de ID van een leverancier
* `<page>` — een paginanummer

### Documenten

| Oud adres | Nieuw adres |
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

### Taken

| Oud adres | Nieuw adres |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### Workflows

| Oud adres | Nieuw adres |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### Orders en facturen

| Oud adres | Nieuw adres |
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

### Analyses en zoeken

| Oud adres | Nieuw adres |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### Gedeelde links

| Oud adres | Nieuw adres |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### Account en aanmelden

| Oud adres | Nieuw adres |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### Lay-outs

| Oud adres | Nieuw adres |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
