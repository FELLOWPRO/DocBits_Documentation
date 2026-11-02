# Bestellposition

## Tabelle `public.purchase_order_line`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `purchase_order_id`: intern
* `purchase_order_number`: intern
* `line_number`: intern
* `item_id`: intern
* `supplier_item_id`: intern
* `description`: intern
* `quantity`: double precision
* `unit_code`: intern
* `unit_price`: double precision
* `total_amount`: double precision
* `currency`: intern
* `status`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `open_quantity`: double precision
* `received_quantity`: double precision
* `confirmed_quantity`: double precision
* `note`: text
* `sub_org_id`: intern
* `sub_line_number`: intern
* `unit_price_per`: double precision
* `buyer_id`: intern
* `buyer_name`: intern
* `unit_code_price`: intern
* `geo_code`: intern
* `promised_delivery_date`: timestamp with time zone
* `delivery_method`: intern
* `requested_ship_date`: date
* `received_base_mou_quantity`: double precision
* `extended_amount`: double precision

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.purchase_order_line`

### Einführung

Die Tabelle `public.purchase_order_line` speichert detaillierte Informationen zu jeder Position einer Bestellung. Sie erfasst verschiedene Attribute einer Bestellposition, etwa Artikeldetails, Mengen, Preise und Status. Diese Tabelle ist unerlässlich, um Bestellungen und deren Erfüllungsstatus in einem Organisationskontext zu verwalten und nachzuverfolgen.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jede Bestellposition.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Bestellposition eindeutig identifiziert.

#### org\_id

* **Bedeutung**: Kennung der Organisation, die der Bestellung zugeordnet ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf eine Organisation verweist.

#### purchase\_order\_id

* **Bedeutung**: Kennung der Bestellung, zu der die Position gehört.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf eine Bestellung verweist.

#### purchase\_order\_number

* **Bedeutung**: Die der Bestellung zugewiesene Nummer.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Bestellnummer darstellt.

#### line\_number

* **Bedeutung**: Die Positionsnummer des Artikels innerhalb der Bestellung.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Reihenfolge der Position in der Bestellung angibt.

#### item\_id

* **Bedeutung**: Kennung des bestellten Artikels.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Artikelcode darstellt.

#### supplier\_item\_id

* **Bedeutung**: Lieferantenspezifische Kennung des Artikels.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, kann null sein, wenn sie vom Lieferanten nicht angegeben wurde.

#### description

* **Bedeutung**: Beschreibung des Artikels.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Textbeschreibung des Artikels.

#### quantity

* **Bedeutung**: Die Anzahl der bestellten Einheiten.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, der die bestellte Menge angibt.

#### unit\_code

* **Bedeutung**: Code, der die Maßeinheit des Artikels darstellt.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die Einheiten darstellt, z. B. 'EA' für Stück.

#### unit\_price

* **Bedeutung**: Preis pro Einheit des Artikels.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, der den Preis pro Einheit darstellt.

#### total\_amount

* **Bedeutung**: Gesamtbetrag der Position (Menge \* Stückpreis).
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, der den Gesamtbetrag darstellt.

#### currency

* **Bedeutung**: Währung, in der der Kauf erfolgt.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Währungscode darstellt, z. B. 'USD'.

#### status

* **Bedeutung**: Aktueller Status der Bestellposition.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Status angibt, z. B. 'Received', 'Invoiced'.

#### created\_by

* **Bedeutung**: Kennung des Benutzers, der den Eintrag erstellt hat.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID darstellt.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Eintrags.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation, kann null sein, wenn nie geändert.

#### deleted\_on

* **Bedeutung**: Zeitstempel, wann der Eintrag als gelöscht markiert wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation, kann null sein, wenn nicht gelöscht.

#### is\_deleted

* **Bedeutung**: Gibt an, ob der Eintrag als gelöscht markiert wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolescher Wert (true/false).

#### open\_quantity

* **Bedeutung**: Menge, die noch nicht eingegangen oder abgerechnet wurde.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, üblicherweise null, wenn vollständig eingegangen.

#### received\_quantity

* **Bedeutung**: Menge, die bereits eingegangen ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, der die eingegangene Menge angibt.

#### confirmed\_quantity

* **Bedeutung**: Vom Lieferanten bestätigte Menge.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, kann null sein, wenn nicht bestätigt.

#### note

* **Bedeutung**: Zusätzliche Anmerkungen zur Bestellposition.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Text, kann besondere Anweisungen oder Kommentare enthalten.

#### sub\_org\_id

* **Bedeutung**: Kennung der Unterorganisation, die der Bestellposition zugeordnet ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Zeichenfolge, möglicherweise null, falls nicht zutreffend.

#### sub\_line\_number

* **Bedeutung**: Unterpositionsnummer innerhalb der Bestellung.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Reihenfolge der Unterposition darstellt.

#### unit\_price\_per

* **Bedeutung**: Basis-Stückpreis des Artikels.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, der den Basis-Stückpreis darstellt.

#### buyer\_id

* **Bedeutung**: Kennung des für den Einkauf verantwortlichen Einkäufers.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Einkäufer-ID darstellt.

#### buyer\_name

* **Bedeutung**: Name des verantwortlichen Einkäufers.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Namen des Einkäufers darstellt.

#### unit\_code\_price

* **Bedeutung**: Einheitencode im Zusammenhang mit der Preisgestaltung.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, ähnlich wie unit\_code.

#### geo\_code

* **Bedeutung**: Geografischer Code für die Lieferung.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die einen geografischen Ort darstellt.

#### promised\_delivery\_date

* **Bedeutung**: Für die Lieferung zugesagtes Datum.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation.

#### delivery\_method

* **Bedeutung**: Liefermethode für die Bestellposition.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Liefermethode darstellt.

#### requested\_ship\_date

* **Bedeutung**: Für den Versand gewünschtes Datum.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein Datumswert.

#### received\_base\_mou\_quantity

* **Bedeutung**: In Basismaßeinheiten eingegangene Menge.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, der die eingegangene Menge in Basismaßeinheiten (Base MOU) angibt.

#### extended\_amount

* **Bedeutung**: Erweiterter Betrag der Position.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein numerischer Wert, der den erweiterten Betrag darstellt; er kann dem total\_amount entsprechen, wenn keine Rabatte oder Zusatzkosten anfallen.
