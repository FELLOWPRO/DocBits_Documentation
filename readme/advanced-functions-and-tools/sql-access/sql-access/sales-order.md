# Kundenauftrag

## Tabelle `public.sales_order`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `sub_org_id`: intern
* `location_id`: intern
* `order_number`: intern
* `customer_purchase_order`: intern
* `customer_id`: intern
* `customer_name`: intern
* `warehouse_id`: intern
* `warehouse_name`: intern
* `transportation_method`: intern
* `requested_delivery_date`: timestamp with time zone
* `order_date`: timestamp with time zone
* `sales_person_id`: intern
* `sales_person_name`: intern
* `ship_to_party_id`: intern
* `ship_to_party_name`: intern
* `ship_to_party_city`: intern
* `ship_to_party_state`: intern
* `ship_to_party_country`: intern
* `ship_to_party_zip`: intern
* `status`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `preview_path`: intern
* `last_modified_by`: intern
* `deleted_by`: intern

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.sales_order`

### Einführung

Die Tabelle `public.sales_order` erfasst und speichert Informationen zu Kundenaufträgen im Geschäftskontext. Dazu gehören Details zum Auftrag, zum Kunden, zur Logistik und verschiedene Metadaten zum Lebenszyklus des Auftrags. Die Tabelle dient als zentrales Verzeichnis zur Nachverfolgung von Status und Historie von Verkaufstransaktionen.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Kundenauftrag.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge (z. B. `'6ffe4673-7563-44dc-8e71-855e8f25534a'`).

#### org\_id

* **Bedeutung**: Kennung der Organisation, die den Kundenauftrag erstellt hat.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Organisation darstellt (z. B. `'23f3d697-7411-4c95-981d-faf089d266be'`).

#### sub\_org\_id

* **Bedeutung**: Kennung einer Unterorganisation, falls zutreffend.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Kann `NULL` sein, falls nicht zutreffend.

#### location\_id

* **Bedeutung**: Kennung des Standorts, der dem Kundenauftrag zugeordnet ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Code-Zeichenfolge, die einen Standort darstellt (z. B. `'028'`).

#### order\_number

* **Bedeutung**: Dem Kundenauftrag zugewiesene eindeutige Nummer.
* **Rolle**: Technisches Feld zur Auftragsverfolgung.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'0010174175'`).

#### customer\_purchase\_order

* **Bedeutung**: Referenznummer der Bestellung des Kunden.
* **Rolle**: Technisches Feld für Querverweise.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'1YFNC3'`).

#### customer\_id

* **Bedeutung**: Kennung des Kunden, der den Auftrag erteilt.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Code-Zeichenfolge (z. B. `'35623000'`).

#### customer\_name

* **Bedeutung**: Name des Kunden.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'DOLLAR GENERAL'`).

#### warehouse\_id

* **Bedeutung**: Kennung des Lagers, das für die Auftragserfüllung zuständig ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Code-Zeichenfolge (z. B. `'028'`).

#### warehouse\_name

* **Bedeutung**: Name des Lagers.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'USCS - DENTON, TX'`).

#### transportation\_method

* **Bedeutung**: Transportmethode für die Lieferung des Auftrags.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Code-Zeichenfolge (z. B. `'001'`).

#### requested\_delivery\_date

* **Bedeutung**: Vom Kunden gewünschtes Lieferdatum.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein Zeitstempel (z. B. `None`).

#### order\_date

* **Bedeutung**: Datum, an dem der Auftrag erteilt wurde.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein Zeitstempel (z. B. `datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`).

#### sales\_person\_id

* **Bedeutung**: Kennung des Vertriebsmitarbeiters, der den Auftrag bearbeitet.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'ROBERTDOCK'`).

#### sales\_person\_name

* **Bedeutung**: Name des Vertriebsmitarbeiters.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'ROBERT DOCKINS'`).

#### ship\_to\_party\_id

* **Bedeutung**: Kennung der Partei, an die der Auftrag geliefert wird.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'35623000 009'`).

#### ship\_to\_party\_name

* **Bedeutung**: Name der Partei, an die der Auftrag geliefert wird.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'DOLLAR GENERAL DC 98061/96460'`).

#### ship\_to\_party\_city

* **Bedeutung**: Stadt der Lieferadresse.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'SAN ANTONIO'`).

#### ship\_to\_party\_state

* **Bedeutung**: Bundesstaat der Lieferadresse.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Kann `NULL` sein.

#### ship\_to\_party\_country

* **Bedeutung**: Land der Lieferadresse.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'US'`).

#### ship\_to\_party\_zip

* **Bedeutung**: Postleitzahl der Lieferadresse.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'78218'`).

#### status

* **Bedeutung**: Aktueller Status des Kundenauftrags.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge (z. B. `'Allocated'`).

#### created\_by

* **Bedeutung**: Kennung des Benutzers, der den Eintrag erstellt hat.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Eine Ganzzahl (z. B. `1`).

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Eintrags.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein Zeitstempel (z. B. `datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`).

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein Zeitstempel (z. B. `datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`).

#### is\_deleted

* **Bedeutung**: Kennzeichen, das angibt, ob der Auftrag als gelöscht markiert ist.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein boolescher Wert (z. B. `False`).

#### deleted\_on

* **Bedeutung**: Zeitstempel, wann der Auftrag als gelöscht markiert wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Standarddatum, falls nicht gelöscht (z. B. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`).

#### preview\_path

* **Bedeutung**: Pfad zu einem Vorschaudokument für den Kundenauftrag.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die einen Dateipfad darstellt (z. B. `'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`).

#### last\_modified\_by

* **Bedeutung**: Kennung des Benutzers, der den Eintrag zuletzt geändert hat.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Kann `NULL` sein.

#### deleted\_by

* **Bedeutung**: Kennung des Benutzers, der den Eintrag als gelöscht markiert hat.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Kann `NULL` sein.
