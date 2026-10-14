# Zmiany adresów internetowych

Adresy internetowe (URL), których używasz do otwierania stron w DocBits, zostały uporządkowane i ujednolicone. Ta strona wyjaśnia, co się zmieniło, dlaczego Twoje stare linki nadal działają i jak znaleźć dowolną stronę pod jej nowym adresem.

## Co się zmieniło

Adresy internetowe w DocBits mają teraz jeden czytelny wzorzec: najpierw to, nad czym pracujesz, a potem widok tego elementu. Na przykład ekran walidacji dokumentu ma teraz adres:

```
/documents/<document-id>/validation
```

zamiast dawnego:

```
/field_validation_v1/<document-id>
```

Z czasem niektóre ekrany doczekały się kilku różnych wersji i adresów — na przykład zatwierdzanie miało osobne adresy dla pierwszego zatwierdzenia, drugiego zatwierdzenia oraz starszych wersji każdego z nich. Teraz współdzielą one jeden adres, a DocBits automatycznie wyświetla właściwą wersję dla Twojej organizacji. Nie musisz już wiedzieć ani zgadywać, która wersja Cię dotyczy.

Adresy używają też teraz wyłącznie małych liter oraz słów oddzielonych myślnikami, zamiast mieszaniny podkreślników, wielkich liter i skrótów.

## Twoje stare linki nadal działają

Nie musisz niczego zmieniać od razu. Zakładki, linki zapisane w wiadomościach e-mail i linki zapisane gdziekolwiek indziej działają dokładnie tak jak wcześniej. Gdy otworzysz stary adres, DocBits automatycznie przekieruje Cię na nowy adres — wraz ze wszystkimi filtrami i opcjami, które były częścią oryginalnego linku.

Po przekierowaniu pasek adresu przeglądarki pokazuje nowy adres. To oczekiwane zachowanie: oznacza, że przekierowanie zadziałało. Z czasem zalecamy zaktualizowanie zapisanych zakładek tak, aby wskazywały bezpośrednio nowe adresy, dzięki czemu będziesz trafiać tam bez dodatkowego przekierowania. Nie ma jednak żadnego terminu — stare adresy będą nadal działać.

## Znajdowanie strony

Jeśli nie masz pewności, jaki jest nowy adres danej strony, lub po prostu chcesz od razu przejść do wybranego miejsca, masz trzy sposoby poruszania się po aplikacji:

* **Mapa Witryny.** Strona [Mapa Witryny](sitemap.md) wymienia wszystkie strony w DocBits, pogrupowane według obszarów, z polem wyszukiwania i filtrami. Otwórz ją z paska bocznego lub z Globalnego Szybkiego Wyszukiwania, wybierając **Zobacz wszystkie wyniki**.
* **Globalne Szybkie Wyszukiwanie.** Naciśnij <kbd>Cmd</kbd> + <kbd>K</kbd> na komputerze Mac lub <kbd>Ctrl</kbd> + <kbd>K</kbd> w systemie Windows z dowolnego miejsca w DocBits, a następnie wpisz nazwę tego, czego szukasz. Szczegóły znajdziesz w [Globalne Szybkie Wyszukiwanie](global-quick-search.md).
* **Ekran „nie znaleziono strony”.** Jeśli wpiszesz lub wkleisz tylko pierwszą część adresu — na przykład `/documents` lub `/analytics` — bez reszty, DocBits wyświetli ekran „nie znaleziono strony” z listą wszystkich stron znajdujących się pod tym adresem. Działa on jak indeks tej grupy stron i ma to samo pole wyszukiwania co Globalne Szybkie Wyszukiwanie, więc możesz wyszukiwać również stamtąd.

## Stare i nowe adresy

Poniższa tabela wymienia każdy adres, który uległ zmianie, pogrupowany według obszarów. Jeśli kilka starych adresów prowadzi teraz do tego samego nowego, każdy stary adres jest wymieniony w osobnym wierszu. Adresy używane wyłącznie przez programistów (na przykład strony debugowania lub demonstracyjne) nie zostały uwzględnione, ponieważ nie mają wpływu na codzienną pracę.

Symbole zastępcze w tabeli oznaczają rzeczywiste wartości:

* `<document-id>` — identyfikator dokumentu
* `<task-id>` — identyfikator zadania
* `<workflow-id>` — identyfikator workflow
* `<document-type>` — typ dokumentu, taki jak faktura lub zamówienie zakupu
* `<file-name>` — nazwa pliku
* `<order-number>` / `<sales-order-id>` — odwołanie do zamówienia zakupu lub sprzedaży
* `<organisation-id>` — identyfikator organizacji
* `<layout-type>` — typ układu
* `<supplier-id>` — identyfikator dostawcy
* `<page>` — numer strony

### Dokumenty

| Stary adres | Nowy adres |
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

### Zadania

| Stary adres | Nowy adres |
|---|---|
| `/task/<task-id>` | `/tasks/<task-id>` |

### Workflow

| Stary adres | Nowy adres |
|---|---|
| `/workflowsdashboard` | `/workflows` |
| `/my_workflow/<document-type>/<workflow-id>` | `/workflows/my/<document-type>/<workflow-id>` |
| `/workflow_designer/<workflow-id>` | `/workflows/designer/<workflow-id>` |
| `/advanced_workflow_designer/<workflow-id>` | `/workflows/advanced-designer/<workflow-id>` |
| `/workflow_logs/<workflow-id>` | `/workflows/logs/<workflow-id>` |
| `/template_designer/<workflow-id>` | `/workflows/templates/<workflow-id>` |
| `/flow` | `/workflows/flow` |

### Zamówienia i faktury

| Stary adres | Nowy adres |
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

### Analityka i wyszukiwanie

| Stary adres | Nowy adres |
|---|---|
| `/analytics-dashboard` | `/analytics` |
| `/report` | `/analytics/reports` |
| `/performance_report` | `/analytics/performance` |
| `/touchless-intelligence/supplier/<supplier-id>` | `/analytics/touchless/suppliers/<supplier-id>` |
| `/touchless-intelligence/document/<document-id>/trace` | `/analytics/touchless/documents/<document-id>/trace` |
| `/supplier-statistic` | `/analytics/suppliers` |
| `/graph-explorer` | `/analytics/graph-explorer` |
| `/full-search` | `/search` |

### Udostępnione linki

| Stary adres | Nowy adres |
|---|---|
| `/status/<document-id>` | `/share/documents/<document-id>/status` |
| `/sales_order_detail/<sales-order-id>/share` | `/share/sales-orders/<sales-order-id>` |
| `/supplier_invoice/share/get_details` | `/share/supplier-invoice` |

### Konto i logowanie

| Stary adres | Nowy adres |
|---|---|
| `/register` | `/auth/register` |
| `/register-success` | `/auth/register-success` |
| `/verify-email` | `/auth/verify-email` |
| `/forget-password` | `/auth/forgot-password` |
| `/reset-password` | `/auth/reset-password` |
| `/set-password` | `/auth/set-password` |
| `/supplier/register/terms_and_conditions/<organisation-id>` | `/supplier/register/terms-and-conditions/<organisation-id>` |

### Układy

| Stary adres | Nowy adres |
|---|---|
| `/layout-builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_layout_builder/<document-type>` | `/layouts/builder/<document-type>` |
| `/manage_approval_layout_builder_v2/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/vertex_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
| `/manage_approval_layout_builder/<document-type>/<layout-type>` | `/layouts/builder/<document-type>/<layout-type>` |
