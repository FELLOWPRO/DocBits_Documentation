# Änderungen der Webadressen

Die Webadressen (URLs), über die Sie Seiten in DocBits erreichen, wurden bereinigt und vereinheitlicht. Diese Seite erklärt, was sich geändert hat, warum Ihre alten Links weiterhin funktionieren und wie Sie jede Seite unter ihrer neuen Adresse finden.

## Was sich geändert hat

Webadressen in DocBits folgen jetzt einem klaren Muster: Zuerst kommt das Objekt, mit dem Sie arbeiten, danach die Ansicht darauf. Beispielsweise lautet die Validierungsansicht eines Dokuments jetzt:

```
/documents/<document-id>/validation
```

anstelle der früheren:

```
/field_validation_v1/<document-id>
```

Im Laufe der Zeit gab es für manche Ansichten mehrere Versionen und Adressen – bei der Genehmigung beispielsweise getrennte Adressen für die erste Genehmigung, die zweite Genehmigung und ältere Versionen davon. Diese teilen sich nun eine einzige Adresse, und DocBits zeigt automatisch die passende Version für Ihre Organisation an. Sie müssen nicht mehr wissen oder erraten, welche Version für Sie gilt.

Adressen bestehen außerdem jetzt nur noch aus kleingeschriebenen Wörtern, die durch Bindestriche getrennt sind, statt aus einer Mischung aus Unterstrichen, Großbuchstaben und Abkürzungen.

## Ihre alten Links funktionieren weiterhin

Sie müssen nicht sofort etwas ändern. Lesezeichen, in E-Mails gespeicherte Links und anderswo abgelegte Links funktionieren genau wie bisher. Wenn Sie eine alte Adresse öffnen, leitet DocBits Sie automatisch auf die neue Adresse weiter – einschließlich aller Filter oder Optionen, die Teil des ursprünglichen Links waren.

Nach der Weiterleitung zeigt die Adressleiste des Browsers die neue Adresse an. Das ist erwartungsgemäß: Es bedeutet, dass die Weiterleitung funktioniert hat. Wir empfehlen, Ihre gespeicherten Lesezeichen mit der Zeit auf die neuen Adressen umzustellen, damit Sie ohne den zusätzlichen Weiterleitungsschritt direkt dorthin gelangen. Es gibt jedoch keine Frist – die alten Adressen funktionieren weiterhin.

## Eine Seite finden

Wenn Sie nicht sicher sind, wie die neue Adresse einer Seite lautet, oder einfach direkt zu etwas springen möchten, gibt es drei Möglichkeiten, sich zurechtzufinden:

* **Sitemap.** Die Seite [Sitemap](sitemap.md) listet alle Seiten in DocBits nach Bereichen gruppiert auf, mit Suchfeld und Filtern. Öffnen Sie sie über die Seitenleiste oder über die Globale Schnellsuche, indem Sie **View all results** wählen.
* **Globale Schnellsuche.** Drücken Sie von überall in DocBits <kbd>Cmd</kbd> + <kbd>K</kbd> auf dem Mac bzw. <kbd>Ctrl</kbd> + <kbd>K</kbd> unter Windows und geben Sie dann den Namen dessen ein, was Sie suchen. Details finden Sie unter [Globale Schnellsuche](global-quick-search.md).
* **Die Seite „Seite nicht gefunden“.** Wenn Sie nur den ersten Teil einer Adresse eingeben oder einfügen – zum Beispiel `/documents` oder `/analytics` – ohne den Rest, zeigt DocBits eine Seite „Seite nicht gefunden“ an, die alle unter dieser Adresse liegenden Seiten auflistet. Sie funktioniert wie ein Index für diese Seitengruppe und bietet dasselbe Suchfeld wie die Globale Schnellsuche, sodass Sie auch von dort aus suchen können.

## Alte und neue Adressen

Die folgende Tabelle listet jede geänderte Adresse nach Bereichen gruppiert auf. Wenn mehrere alte Adressen jetzt zur selben neuen Adresse führen, steht jede alte Adresse in einer eigenen Zeile. Adressen, die nur von Entwicklern verwendet werden (zum Beispiel Debugging- oder Demo-Seiten), sind nicht aufgeführt, da sie die tägliche Nutzung nicht betreffen.

Die Platzhalter in der Tabelle stehen für echte Werte:

* `<document-id>` — die ID eines Dokuments
* `<task-id>` — die ID einer Aufgabe
* `<workflow-id>` — die ID eines Workflows
* `<document-type>` — ein Dokumenttyp, etwa Rechnung oder Bestellung
* `<file-name>` — ein Dateiname
* `<order-number>` / `<sales-order-id>` — ein Verweis auf eine Einkaufs- oder Verkaufsbestellung
* `<organisation-id>` — die ID einer Organisation
* `<layout-type>` — ein Layouttyp
* `<supplier-id>` — die ID eines Lieferanten
* `<page>` — eine Seitenzahl

### Dokumente

| Alte Adresse | Neue Adresse |
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

### Aufgaben

| Alte Adresse | Neue Adresse |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### Workflows

| Alte Adresse | Neue Adresse |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### Bestellungen und Rechnungen

| Alte Adresse | Neue Adresse |
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

### Analysen und Suche

| Alte Adresse | Neue Adresse |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### Geteilte Links

| Alte Adresse | Neue Adresse |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### Konto und Anmeldung

| Alte Adresse | Neue Adresse |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### Layouts

| Alte Adresse | Neue Adresse |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
