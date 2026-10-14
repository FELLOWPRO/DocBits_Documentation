# PO match tolerance

## Tabelle `public.po_match_tolerance`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `item_number`: internal
* `supplier_item_number`: internal
* `description`: internal
* `unit_price_tolerance`: double precision
* `quantity_tolerance`: double precision
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `unit_price_tolerance_type`: internal
* `quantity_tolerance_type`: internal

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.po_match_tolerance`

### Einführung

Die Tabelle `public.po_match_tolerance` verwaltet und speichert Toleranzgrenzen für den Bestellabgleich (PO Matching). Dabei geht es in der Regel um zulässige Abweichungen bei Stückpreisen und Mengen zwischen bestellten und gelieferten Waren. Jeder Eintrag in der Tabelle stellt Toleranzeinstellungen für bestimmte Artikel dar und kann Organisationen helfen, Konsistenz und Genauigkeit in ihren Beschaffungsprozessen sicherzustellen.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Eintrag in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jeden Datensatz einer Toleranzeinstellung eindeutig identifiziert.

#### org\_id

* **Bedeutung**: Kennung der Organisation, der die Toleranzeinstellungen zugeordnet sind.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf die Organisation im System verweist.

#### item\_number

* **Bedeutung**: Die Artikelnummer, für die Toleranzeinstellungen definiert sind.
* **Rolle**: Geschäftliche Kennung.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Code oder die Nummer des Artikels im Bestand der Organisation darstellt.

#### supplier\_item\_number

* **Bedeutung**: Die vom Lieferanten angegebene Artikelnummer.
* **Rolle**: Geschäftliche Kennung.
* **Typischer Inhalt**: Eine Zeichenfolge, die `None` sein kann, wenn sie nicht angegeben ist, und den Code oder die Nummer des Lieferanten für den Artikel darstellt.

#### description

* **Bedeutung**: Eine Textbeschreibung des Artikels.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge mit Details zum Artikel, die `None` sein kann.

#### unit\_price\_tolerance

* **Bedeutung**: Die zulässige Abweichung beim Stückpreis des Artikels.
* **Rolle**: Geschäftsregel.
* **Typischer Inhalt**: Ein numerischer Wert, der die prozentuale oder absolute Toleranz beim Stückpreis angibt.

#### quantity\_tolerance

* **Bedeutung**: Die zulässige Abweichung bei der Menge des Artikels.
* **Rolle**: Geschäftsregel.
* **Typischer Inhalt**: Ein numerischer Wert, der die prozentuale oder absolute Toleranz bei der Menge angibt.

#### created\_by

* **Bedeutung**: Kennung des Benutzers, der den Eintrag erstellt hat.
* **Rolle**: Audit- bzw. Protokollfeld.
* **Typischer Inhalt**: Eine Ganzzahl, die üblicherweise auf eine Benutzer-ID im System verweist.

#### created\_on

* **Bedeutung**: Der Zeitstempel der Erstellung des Eintrags.
* **Rolle**: Audit- bzw. Protokollfeld.
* **Typischer Inhalt**: Ein Datum-Uhrzeit-Wert mit Zeitzone, der Datum und Uhrzeit der Erstellung angibt.

#### last\_modified\_on

* **Bedeutung**: Der Zeitstempel der letzten Änderung des Eintrags.
* **Rolle**: Audit- bzw. Protokollfeld.
* **Typischer Inhalt**: Ein Datum-Uhrzeit-Wert mit Zeitzone, der angibt, wann der Datensatz zuletzt aktualisiert wurde; kann `None` sein, wenn nicht geändert.

#### is\_deleted

* **Bedeutung**: Gibt an, ob der Eintrag logisch gelöscht ist.
* **Rolle**: Technischer Indikator für logisches Löschen (Soft Delete).
* **Typischer Inhalt**: Ein boolescher Wert, wobei `False` aktiv und `True` logisch gelöscht bedeutet.

#### unit\_price\_tolerance\_type

* **Bedeutung**: Definiert die Art der Stückpreistoleranz (z. B. Prozentwert oder absoluter Wert).
* **Rolle**: Geschäftsregel.
* **Typischer Inhalt**: Eine Zeichenfolge, häufig 'value', die die Art des Toleranzmaßes angibt.

#### quantity\_tolerance\_type

* **Bedeutung**: Definiert die Art der Mengentoleranz (z. B. Prozentwert oder absoluter Wert).
* **Rolle**: Geschäftsregel.
* **Typischer Inhalt**: Eine Zeichenfolge, häufig 'value', die die Art des Toleranzmaßes angibt.

Diese Dokumentation bietet einen detaillierten Überblick über jedes Feld der Tabelle `public.po_match_tolerance` und gibt Einblicke in deren mögliche Inhalte und Rollen im Kontext der Bestellverwaltung.
