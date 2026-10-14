# Sales order

## Tabella `public.sales_order`

### Colonne

* `id`: interno
* `org_id`: ID dell'organizzazione
* `sub_org_id`: interno
* `location_id`: interno
* `order_number`: interno
* `customer_purchase_order`: interno
* `customer_id`: interno
* `customer_name`: interno
* `warehouse_id`: interno
* `warehouse_name`: interno
* `transportation_method`: interno
* `requested_delivery_date`: timestamp with time zone
* `order_date`: timestamp with time zone
* `sales_person_id`: interno
* `sales_person_name`: interno
* `ship_to_party_id`: interno
* `ship_to_party_name`: interno
* `ship_to_party_city`: interno
* `ship_to_party_state`: interno
* `ship_to_party_country`: interno
* `ship_to_party_zip`: interno
* `status`: interno
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `preview_path`: interno
* `last_modified_by`: interno
* `deleted_by`: interno

### Analisi e descrizione

## Documentazione tecnica della tabella `public.sales_order`

### Introduzione

La tabella `public.sales_order` è progettata per acquisire e memorizzare le informazioni relative agli ordini di vendita in un contesto aziendale. Comprende dettagli sull'ordine, sul cliente, sulla logistica e vari metadati associati al ciclo di vita dell'ordine. La tabella funge da archivio centrale per tracciare lo stato e la cronologia delle transazioni di vendita.

### Descrizione delle colonne

#### id

* **Significato**: identificatore univoco di ogni ordine di vendita.
* **Ruolo**: chiave primaria.
* **Contenuto tipico**: una stringa UUID (ad es. `'6ffe4673-7563-44dc-8e71-855e8f25534a'`).

#### org\_id

* **Significato**: identificatore dell'organizzazione che ha creato l'ordine di vendita.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa UUID che rappresenta l'organizzazione (ad es. `'23f3d697-7411-4c95-981d-faf089d266be'`).

#### sub\_org\_id

* **Significato**: identificatore di una sottorganizzazione, se applicabile.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: può essere `NULL` se non applicabile.

#### location\_id

* **Significato**: identificatore della sede associata all'ordine di vendita.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un codice stringa che rappresenta una sede (ad es. `'028'`).

#### order\_number

* **Significato**: numero univoco assegnato all'ordine di vendita.
* **Ruolo**: campo tecnico per il tracciamento dell'ordine.
* **Contenuto tipico**: una stringa (ad es. `'0010174175'`).

#### customer\_purchase\_order

* **Significato**: numero di riferimento dell'ordine di acquisto del cliente.
* **Ruolo**: campo tecnico per i riferimenti incrociati.
* **Contenuto tipico**: una stringa (ad es. `'1YFNC3'`).

#### customer\_id

* **Significato**: identificatore del cliente che effettua l'ordine.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un codice stringa (ad es. `'35623000'`).

#### customer\_name

* **Significato**: nome del cliente.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa (ad es. `'DOLLAR GENERAL'`).

#### warehouse\_id

* **Significato**: identificatore del magazzino responsabile dell'evasione dell'ordine.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: un codice stringa (ad es. `'028'`).

#### warehouse\_name

* **Significato**: nome del magazzino.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa (ad es. `'USCS - DENTON, TX'`).

#### transportation\_method

* **Significato**: metodo di trasporto per la consegna dell'ordine.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un codice stringa (ad es. `'001'`).

#### requested\_delivery\_date

* **Significato**: data di consegna richiesta dal cliente.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un timestamp (ad es. `None`).

#### order\_date

* **Significato**: data in cui è stato effettuato l'ordine.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: un timestamp (ad es. `datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`).

#### sales\_person\_id

* **Significato**: identificatore del venditore che gestisce l'ordine.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa (ad es. `'ROBERTDOCK'`).

#### sales\_person\_name

* **Significato**: nome del venditore.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa (ad es. `'ROBERT DOCKINS'`).

#### ship\_to\_party\_id

* **Significato**: identificatore del destinatario a cui viene spedito l'ordine.
* **Ruolo**: chiave esterna.
* **Contenuto tipico**: una stringa (ad es. `'35623000 009'`).

#### ship\_to\_party\_name

* **Significato**: nome del destinatario a cui viene spedito l'ordine.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa (ad es. `'DOLLAR GENERAL DC 98061/96460'`).

#### ship\_to\_party\_city

* **Significato**: città dell'indirizzo di spedizione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa (ad es. `'SAN ANTONIO'`).

#### ship\_to\_party\_state

* **Significato**: stato (provincia) dell'indirizzo di spedizione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: può essere `NULL`.

#### ship\_to\_party\_country

* **Significato**: paese dell'indirizzo di spedizione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa (ad es. `'US'`).

#### ship\_to\_party\_zip

* **Significato**: CAP dell'indirizzo di spedizione.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa (ad es. `'78218'`).

#### status

* **Significato**: stato attuale dell'ordine di vendita.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa (ad es. `'Allocated'`).

#### created\_by

* **Significato**: identificatore dell'utente che ha creato la voce.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un intero (ad es. `1`).

#### created\_on

* **Significato**: timestamp di creazione della voce.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un timestamp (ad es. `datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`).

#### last\_modified\_on

* **Significato**: timestamp dell'ultima modifica.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un timestamp (ad es. `datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`).

#### is\_deleted

* **Significato**: flag che indica se l'ordine è contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: un valore booleano (ad es. `False`).

#### deleted\_on

* **Significato**: timestamp del momento in cui l'ordine è stato contrassegnato come eliminato.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: data predefinita se non eliminato (ad es. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`).

#### preview\_path

* **Significato**: percorso di un documento di anteprima dell'ordine di vendita.
* **Ruolo**: campo descrittivo.
* **Contenuto tipico**: una stringa che rappresenta un percorso di file (ad es. `'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`).

#### last\_modified\_by

* **Significato**: identificatore dell'utente che ha modificato per ultimo la voce.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: può essere `NULL`.

#### deleted\_by

* **Significato**: identificatore dell'utente che ha contrassegnato la voce come eliminata.
* **Ruolo**: campo tecnico.
* **Contenuto tipico**: può essere `NULL`.
