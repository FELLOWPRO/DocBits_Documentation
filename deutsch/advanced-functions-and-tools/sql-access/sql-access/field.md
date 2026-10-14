# Field

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: internal
* `field_name`: internal
* `field_type`: internal
* `title`: internal
* `translation_key`: internal
* `hide_label`: boolean
* `input_type`: internal
* `input_size`: internal
* `icon_left`: internal
* `icon_right`: internal
* `icon_above`: internal
* `group_id`: internal
* `row_order`: integer
* `sort_order`: integer
* `fuzzy_name`: internal
* `fuzzy_field`: internal
* `fuzzy_primary_field`: boolean
* `label_align`: internal
* `calculation_formula`: text
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `placeholder`: internal
* `coordinates`: internal
* `normalized_coordinates`: internal
* `threshold`: internal
* `reference_point`: internal
* `checkbox_group`: internal
* `list_of_values`: internal
* `enforce_list_of_values`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `costing_element`: internal
* `erp_field_name`: internal

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.field`

## Einführung

Die Tabelle `public.field` dient offenbar der Verwaltung von Metadaten und Konfigurationen für verschiedene Felder, die Dokumenten zugeordnet sind, vermutlich im Versicherungsbereich. Jede Zeile der Tabelle scheint eine bestimmte Feldkonfiguration darzustellen, einschließlich Typ, Beschriftung, Sichtbarkeitseinstellungen und weiterer Eigenschaften, die festlegen, wie das Feld dargestellt und verarbeitet werden soll.

## Spalten

### id
- **Bedeutung**: Eindeutige Kennung für jede Feldkonfiguration.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jeden Eintrag in der Tabelle eindeutig identifiziert.

### org_id
- **Bedeutung**: Kennung der Organisation, der die Feldkonfiguration zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID, die auf eine Organisation verweist.

### doc_type
- **Bedeutung**: Gibt den Dokumenttyp an, dem das Feld zugeordnet ist.
- **Rolle**: Möglicherweise ein Fremdschlüssel oder eine kategoriale Kennung.
- **Typischer Inhalt**: Eine Zeichenfolge im Format `INSURANCE_DOCUMENTS_<UUID>`, die den Dokumenttyp angibt.

### is_sub_doc_type_field
- **Bedeutung**: Gibt an, ob das Feld ein Untertyp des Dokumenttyps ist.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### profile
- **Bedeutung**: Definiert möglicherweise das Profil oder den Geltungsbereich des Feldes.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Häufig leer oder eine kurze Textbeschreibung.

### field_name
- **Bedeutung**: Der interne Name des Feldes.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge, die den Namen des Feldes in einem technischen Kontext darstellt (z. B. `Schadennummer`).

### field_type
- **Bedeutung**: Definiert den Datentyp, den das Feld enthält.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Beschreibende Zeichenfolgen wie `STRING`, `AMOUNT`.

### title
- **Bedeutung**: Der Anzeigetitel des Feldes.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolge in Großbuchstaben, die für die Anzeige der Feldbeschriftung verwendet wird.

### translation_key
- **Bedeutung**: Schlüssel für die Übersetzung in verschiedene Sprachen.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Zeichenfolge in Kleinbuchstaben, die den Übersetzungsschlüssel darstellt.

### hide_label
- **Bedeutung**: Gibt an, ob die Beschriftung des Feldes in der Benutzeroberfläche ausgeblendet werden soll.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### input_type
- **Bedeutung**: Legt die Eingabemethode für das Feld fest.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Kann leer sein oder Zeichenfolgen enthalten, die den Eingabetyp definieren.

### input_size
- **Bedeutung**: Bestimmt die Größe des Eingabefeldes.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Kann leer sein oder Zeichenfolgen enthalten, die die Eingabegröße definieren.

### icon_left
- **Bedeutung**: Symbol, das auf der linken Seite des Feldes angezeigt wird.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit Symbolkennungen.

### icon_right
- **Bedeutung**: Symbol, das auf der rechten Seite des Feldes angezeigt wird.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit Symbolkennungen.

### icon_above
- **Bedeutung**: Symbol, das oberhalb des Feldes angezeigt wird.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit Symbolkennungen.

### group_id
- **Bedeutung**: Kennung der Feldgruppe, zu der dieses Feld gehört.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID, die auf eine Feldgruppe verweist.

### row_order
- **Bedeutung**: Bestimmt die Reihenfolge des Feldes in einer Liste oder einem Formular.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ganzzahl, die die Position angibt.

### sort_order
- **Bedeutung**: Legt die Sortierreihenfolge für das Feld fest.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ganzzahl, die den Sortierrang definiert.

### fuzzy_name
- **Bedeutung**: Ein alternativer Name für den unscharfen Abgleich (Fuzzy Matching).
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Häufig leer oder eine Zeichenfolge für Abgleichszwecke.

### fuzzy_field
- **Bedeutung**: Gibt an, ob das Feld im unscharfen Abgleich verwendet wird.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder eine Zeichenfolge.

### fuzzy_primary_field
- **Bedeutung**: Gibt an, ob dies das primäre Feld für den unscharfen Abgleich ist.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### label_align
- **Bedeutung**: Ausrichtungseinstellung für die Feldbeschriftung.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Häufig leer oder mit Ausrichtungsangaben (z. B. left, right, center).

### calculation_formula
- **Bedeutung**: Formel, die für Berechnungen mit dem Feld verwendet wird.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Text mit einer Formel oder Berechnungslogik.

### clean_field
- **Bedeutung**: Gibt an, ob das Feld einer Datenbereinigung unterzogen werden soll.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### alphanumeric_field
- **Bedeutung**: Gibt an, ob das Feld nur alphanumerische Zeichen akzeptieren soll.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### placeholder
- **Bedeutung**: Platzhaltertext für das Eingabefeld.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Häufig leer oder mit einem Hinweistext.

### coordinates
- **Bedeutung**: Dem Feld zugeordnete Koordinatendaten.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit Koordinateninformationen.

### normalized_coordinates
- **Bedeutung**: Normalisierte Version der Koordinaten für mehr Konsistenz.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit normalisierten Koordinatendaten.

### threshold
- **Bedeutung**: Schwellenwert im Zusammenhang mit der Validierung oder Verarbeitung des Feldes.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit Schwellenwerten.

### reference_point
- **Bedeutung**: Bezugspunkt, der bei Berechnungen oder der Positionierung verwendet wird.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Häufig leer oder mit Bezugspunktdaten.

### checkbox_group
- **Bedeutung**: Gruppierungskennung für Kontrollkästchenfelder.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit Gruppenkennungen.

### list_of_values
- **Bedeutung**: Legt eine Liste zulässiger Werte für das Feld fest.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit einer Werteliste.

### enforce_list_of_values
- **Bedeutung**: Gibt an, ob die Werteliste strikt durchgesetzt werden soll.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### created_by
- **Bedeutung**: Kennung des Benutzers, der den Feldeintrag erstellt hat.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ganzzahl, die auf eine Benutzer-ID verweist.

### created_on
- **Bedeutung**: Zeitstempel der Erstellung des Feldes.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Datum und Uhrzeit in UTC.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung des Feldes.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Datum und Uhrzeit in UTC.

### is_deleted
- **Bedeutung**: Gibt an, ob das Feld als gelöscht markiert wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### costing_element
- **Bedeutung**: Kostenelement, das dem Feld zugeordnet ist.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit Kennungen von Kostenelementen.

### erp_field_name
- **Bedeutung**: Name des Feldes, wie er in ERP-Systemen verwendet wird.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel leer oder mit ERP-spezifischen Feldnamen.

Diese Dokumentation bietet einen detaillierten Überblick über Struktur und Zweck jeder Spalte der Tabelle `public.field`. Sie dient Entwicklern als Leitfaden, um das Datenmodell und seine Anwendung im System zu verstehen.
```
