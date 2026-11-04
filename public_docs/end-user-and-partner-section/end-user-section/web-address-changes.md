# Modifiche agli indirizzi web

Gli indirizzi web (URL) che utilizzi per raggiungere le pagine di DocBits sono stati riordinati e resi coerenti. Questa pagina spiega che cosa è cambiato, perché i tuoi vecchi link continuano a funzionare e come trovare qualsiasi pagina al suo nuovo indirizzo.

## Che cosa è cambiato

Gli indirizzi web in DocBits seguono ora un unico schema chiaro: prima l'elemento su cui stai lavorando, poi la sua vista. Ad esempio, la schermata di convalida di un documento è ora:

```
/documents/<document-id>/validation
```

invece del vecchio:

```
/field_validation_v1/<document-id>
```

Col tempo, alcune schermate sono arrivate ad avere più versioni e più indirizzi: ad esempio, l'approvazione aveva indirizzi separati per la prima approvazione, per la seconda approvazione e per le versioni precedenti di ciascuna. Ora condividono un unico indirizzo e DocBits mostra automaticamente la versione corretta per la tua organizzazione. Non è più necessario sapere, o indovinare, quale versione si applichi a te.

Gli indirizzi usano inoltre solo parole in minuscolo separate da trattini, invece di un misto di trattini bassi, lettere maiuscole e abbreviazioni.

## I tuoi vecchi link continuano a funzionare

Non devi modificare nulla subito. I segnalibri, i link salvati nelle e-mail e quelli salvati altrove continuano a funzionare esattamente come prima. Quando apri un vecchio indirizzo, DocBits ti reindirizza automaticamente al nuovo, compresi eventuali filtri od opzioni che facevano parte del link originale.

Dopo il reindirizzamento, la barra degli indirizzi del browser mostra il nuovo indirizzo. È normale: significa che il reindirizzamento ha funzionato. Nel tempo ti consigliamo di aggiornare i segnalibri salvati in modo che puntino direttamente ai nuovi indirizzi, così da arrivare a destinazione senza il passaggio aggiuntivo del reindirizzamento. Non c'è però alcuna scadenza: i vecchi indirizzi continueranno a funzionare.

## Trovare una pagina

Se non sei sicuro di quale sia il nuovo indirizzo di una pagina, o vuoi semplicemente passare direttamente a qualcosa, hai tre modi per orientarti:

* **Mappa del Sito.** La pagina [Mappa del Sito](sitemap.md) elenca tutte le pagine di DocBits, raggruppate per area, con una casella di ricerca e dei filtri. Aprila dalla barra laterale oppure dalla Ricerca Rapida Globale scegliendo **Vedi tutti i risultati**.
* **Ricerca Rapida Globale.** Premi <kbd>Cmd</kbd> + <kbd>K</kbd> su Mac oppure <kbd>Ctrl</kbd> + <kbd>K</kbd> su Windows da qualsiasi punto di DocBits, quindi digita il nome di ciò che cerchi. Per i dettagli, consulta [Ricerca Rapida Globale](global-quick-search.md).
* **La schermata di pagina non trovata.** Se digiti o incolli solo la prima parte di un indirizzo, ad esempio `/documents` o `/analytics`, senza il resto, DocBits mostra una schermata di pagina non trovata con l'elenco di tutte le pagine che si trovano sotto quell'indirizzo. Funziona come un indice per quel gruppo di pagine e dispone della stessa casella di ricerca della Ricerca Rapida Globale, quindi puoi cercare anche da lì.

## Vecchi e nuovi indirizzi

La tabella seguente elenca tutti gli indirizzi che sono cambiati, raggruppati per area. Quando più vecchi indirizzi portano ora allo stesso nuovo indirizzo, ogni vecchio indirizzo è riportato su una riga a sé. Gli indirizzi usati solo dagli sviluppatori (ad esempio le pagine di debug o di demo) non sono elencati, poiché non influiscono sull'uso quotidiano.

I segnaposto nella tabella rappresentano valori reali:

* `<document-id>` — l'ID di un documento
* `<task-id>` — l'ID di un'attività
* `<workflow-id>` — l'ID di un workflow
* `<document-type>` — un tipo di documento, ad esempio fattura o ordine di acquisto
* `<file-name>` — un nome di file
* `<order-number>` / `<sales-order-id>` — un riferimento a un ordine di acquisto o di vendita
* `<organisation-id>` — l'ID di un'organizzazione
* `<layout-type>` — un tipo di layout
* `<supplier-id>` — l'ID di un fornitore
* `<page>` — un numero di pagina

### Documenti

| Vecchio indirizzo | Nuovo indirizzo |
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

### Attività

| Vecchio indirizzo | Nuovo indirizzo |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### Flusso di lavoro

| Vecchio indirizzo | Nuovo indirizzo |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### Ordini e fatture

| Vecchio indirizzo | Nuovo indirizzo |
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

### Analisi e ricerca

| Vecchio indirizzo | Nuovo indirizzo |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### Link condivisi

| Vecchio indirizzo | Nuovo indirizzo |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### Account e accesso

| Vecchio indirizzo | Nuovo indirizzo |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### Layout

| Vecchio indirizzo | Nuovo indirizzo |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
