# Wareneingangsposition

## Tabelle `public.receive_delivery_line`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `receive_delivery_id`: intern
* `delivery_number`: intern
* `line_number`: intern
* `item_id`: intern
* `description`: intern
* `shipped_quantity`: double precision
* `status`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `purchase_order`: intern
* `sequence_number`: intern
* `sub_org_id`: intern
* `shipped_quantity_unit_code`: intern
* `packing_slip_quantity`: double precision
* `packing_slip_quantity_unit_code`: intern
* `received_quantity`: double precision
* `received_quantity_unit_code`: intern
* `purchase_order_line_number`: intern
* `status_effective_from`: timestamp with time zone
* `purchase_order_sub_line_number`: intern
* `invoiced_quantity`: double precision
* `invoice_matching_status`: intern
* `open_quantity`: double precision
* `last_modified_by`: intern
* `deleted_by`: intern

### Analyse & Beschreibung

## Tabellendokumentation: `public.receive_delivery_line`

### Einführung

Die Tabelle `public.receive_delivery_line` ist offenbar ein detailliertes Verzeichnis von Liefer- und Wareneingangspositionen im Rahmen der Logistik- und Lieferkettenprozesse einer Organisation. Jede Zeile der Tabelle stellt eine bestimmte Position einer Lieferung dar und erfasst Details wie Artikelbeschreibung, versandte und eingegangene Mengen sowie verschiedene Statusfelder. Die Tabelle ist ein wesentlicher Bestandteil, um den Warenfluss vom Versand bis zum Wareneingang nachzuverfolgen, einschließlich Rechnungsstellung und Bestellverwaltung.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jede Lieferposition.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine universell eindeutige Kennung (UUID).

#### org\_id

* **Bedeutung**: Kennung der Organisation, die der Lieferung zugeordnet ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID, die die Organisation darstellt.

#### receive\_delivery\_id

* **Bedeutung**: Kennung, die auf die gesamte Liefertransaktion verweist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID, die einer bestimmten Liefertransaktion zugeordnet ist.

#### delivery\_number

* **Bedeutung**: Der Lieferung zugewiesene eindeutige Nummer.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Liefernummer darstellt.

#### line\_number

* **Bedeutung**: Bestimmte Positionsnummer innerhalb einer Lieferung.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Numerische Zeichenfolge, die die Reihenfolge der Position angibt.

#### item\_id

* **Bedeutung**: Kennung des versandten Artikels.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Eine numerische Zeichenfolge, die einem Artikel entspricht.

#### description

* **Bedeutung**: Beschreibung des Artikels.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Textbeschreibung des Artikels, z. B. "FLOUR, WHEAT, UN-BLEACHED ENRICHED, BULK".

#### shipped\_quantity

* **Bedeutung**: Menge des Artikels, die versandt wurde.
* **Rolle**: Mengenfeld.
* **Typischer Inhalt**: Eine Dezimalzahl, die die versandte Menge angibt.

#### status

* **Bedeutung**: Aktueller Status der Lieferposition.
* **Rolle**: Statusfeld.
* **Typischer Inhalt**: Text wie "Received".

#### created\_by

* **Bedeutung**: Kennung des Benutzers oder Systems, das den Datensatz erstellt hat.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Ganzzahl, die eine Benutzer-ID darstellt.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Datensatzes.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

#### deleted\_on

* **Bedeutung**: Zeitstempel, wann der Datensatz als gelöscht markiert wurde.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone, häufig null, sofern nicht gelöscht.

#### is\_deleted

* **Bedeutung**: Gibt an, ob der Datensatz als gelöscht markiert ist.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolescher Wert, true oder false.

#### purchase\_order

* **Bedeutung**: Verweis auf die zugehörige Bestellung.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Alphanumerische Zeichenfolge, die eine Bestellnummer darstellt.

#### sequence\_number

* **Bedeutung**: Laufende Nummer der Lieferposition.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Numerische Zeichenfolge, häufig null.

#### sub\_org\_id

* **Bedeutung**: Kennung einer beteiligten Unterorganisation.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: UUID, häufig null.

#### shipped\_quantity\_unit\_code

* **Bedeutung**: Maßeinheit der versandten Menge.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Code, der Einheiten darstellt, z. B. "LBP".

#### packing\_slip\_quantity

* **Bedeutung**: Menge laut Lieferschein.
* **Rolle**: Mengenfeld.
* **Typischer Inhalt**: Dezimalzahl, häufig null.

#### packing\_slip\_quantity\_unit\_code

* **Bedeutung**: Einheitencode für die Menge laut Lieferschein.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Code, der Einheiten darstellt, häufig null.

#### received\_quantity

* **Bedeutung**: Menge der tatsächlich eingegangenen Artikel.
* **Rolle**: Mengenfeld.
* **Typischer Inhalt**: Dezimalzahl, die die eingegangene Menge angibt.

#### received\_quantity\_unit\_code

* **Bedeutung**: Einheitencode für die eingegangene Menge.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Code, der Einheiten darstellt, z. B. "LBP".

#### purchase\_order\_line\_number

* **Bedeutung**: Positionsnummer innerhalb der Bestellung.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Numerische Zeichenfolge.

#### status\_effective\_from

* **Bedeutung**: Datum und Uhrzeit, ab denen der Status gültig ist.
* **Rolle**: Statusfeld.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone, häufig null.

#### purchase\_order\_sub\_line\_number

* **Bedeutung**: Unterpositionsnummer innerhalb der Bestellung.
* **Rolle**: Referenzfeld.
* **Typischer Inhalt**: Numerische Zeichenfolge, häufig "000".

#### invoiced\_quantity

* **Bedeutung**: Menge, die bereits abgerechnet wurde.
* **Rolle**: Mengenfeld.
* **Typischer Inhalt**: Dezimalzahl.

#### invoice\_matching\_status

* **Bedeutung**: Status des Rechnungsabgleichs.
* **Rolle**: Statusfeld.
* **Typischer Inhalt**: Textueller Statuscode, z. B. "9.0".

#### open\_quantity

* **Bedeutung**: Menge, die noch offen oder noch nicht verarbeitet ist.
* **Rolle**: Mengenfeld.
* **Typischer Inhalt**: Dezimalzahl.

#### last\_modified\_by

* **Bedeutung**: Kennung des Benutzers, der den Datensatz zuletzt geändert hat.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: UUID des Benutzers, häufig null.

#### deleted\_by

* **Bedeutung**: Kennung des Benutzers, der den Datensatz als gelöscht markiert hat.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: UUID des Benutzers, häufig null.
