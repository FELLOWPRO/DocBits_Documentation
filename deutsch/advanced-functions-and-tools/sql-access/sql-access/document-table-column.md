# Document table column

## Spalten

* `id`: internal
* `document_table_id`: internal
* `table_name`: internal
* `org_id`: ID to organisation
* `column_name`: internal
* `column_type`: internal
* `title`: internal
* `translation_key`: internal
* `sort_order`: integer
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.document_table_column`

## Einführung

Die Tabelle `public.document_table_column` dient offenbar der Speicherung von Metadaten zu Spalten in verschiedenen dokumentbezogenen Tabellen, etwa Rechnungs- oder Lieferscheintabellen. Diese Metadaten umfassen Informationen zu Name, Typ und Eigenschaften jeder Spalte sowie organisatorische und technische Bezeichner. Die Tabelle unterstützt die dynamische Erzeugung und Verwaltung von Dokumentschemata im System.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Ein eindeutiger Bezeichner für jeden Spalteneintrag in der Tabelle.
- **Rolle**: Primärschlüssel.
- **Hinweis**: In der Regel eine UUID-Zeichenfolge, die eine Zeile dieser Tabelle eindeutig identifiziert.

### document_table_id
- **Bedeutung**: Verweist auf die Tabelle, die das Dokument enthält, zu dem diese Spalte gehört.
- **Rolle**: Fremdschlüssel.
- **Hinweis**: Vermutlich eine UUID, die auf eine andere Tabelle verweist, in der Dokumenttabellen definiert sind.

### table_name
- **Bedeutung**: Der Name der Dokumenttabelle, zu der diese Spalte gehört.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Namen wie `INVOICE_TABLE`, `DELIVERY_NOTE_TABLE`.
- **Hinweis**: Erleichtert das Verständnis, zu welcher Dokumentstruktur die Spalte gehört.

### org_id
- **Bedeutung**: Bezeichner der Organisation, der die Dokumenttabelle gehört oder die sie verwaltet.
- **Rolle**: Fremdschlüssel.
- **Hinweis**: In der Regel eine UUID, die auf eine Organisationsentität verweist.

### column_name
- **Bedeutung**: Der technische Name der Spalte innerhalb ihrer Dokumenttabelle.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Namen wie `COUNTRY_ORIGIN`, `ORDERED_QUANTITY`.
- **Hinweis**: Stellt den tatsächlichen Feldnamen in der Dokumenttabelle dar.

### column_type
- **Bedeutung**: Beschreibt den Datentyp der Spalte.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: `STRING`, `DATE`.
- **Hinweis**: Gibt an, welche Art von Daten in der Spalte gespeichert wird.

### title
- **Bedeutung**: Ein lesbarer Titel oder eine Bezeichnung für die Spalte.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: `COUNTRY_ORIGIN`, `Ordered Quantity`.
- **Hinweis**: Wird verwendet, um Spaltennamen benutzerfreundlich anzuzeigen.

### translation_key
- **Bedeutung**: Schlüssel für die Internationalisierung und Lokalisierung des Spaltentitels.
- **Rolle**: Technisches Feld.
- **Hinweis**: In den Beispieldaten derzeit leer, was auf eine optionale Verwendung hindeutet.

### sort_order
- **Bedeutung**: Legt die Reihenfolge der Spalten bei der Anzeige fest.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ganzzahlen wie `16`, `5`.
- **Hinweis**: Bestimmt die Reihenfolge der Spalten in der Ansicht der Dokumenttabelle.

### clean_field
- **Bedeutung**: Gibt an, ob die Spalte bereinigte Daten enthält.
- **Rolle**: Boolesches Kennzeichen.
- **Typischer Inhalt**: `True` oder `False`.
- **Hinweis**: Wird für die Datenvalidierung oder den Bereinigungsstatus verwendet.

### alphanumeric_field
- **Bedeutung**: Gibt an, ob die Spalte als alphanumerisches Feld behandelt werden soll.
- **Rolle**: Boolesches Kennzeichen.
- **Typischer Inhalt**: `True` oder `False`.
- **Hinweis**: Nützlich für Eingabevalidierung oder Formatierung.

### created_by
- **Bedeutung**: Bezeichner des Benutzers, der diesen Spalteneintrag erstellt hat.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Ganzzahlen wie `1`, `8`.
- **Hinweis**: Verweist auf einen Benutzer oder eine Systementität, die für die Erstellung verantwortlich ist.

### created_on
- **Bedeutung**: Zeitstempel der Erstellung des Spalteneintrags.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Datums- und Zeitwerte in UTC.
- **Hinweis**: Nützlich für Audits und die Nachverfolgung von Änderungen.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung am Spalteneintrag.
- **Rolle**: Technisches Feld.
- **Hinweis**: In den Beispieldaten derzeit `None`, d. h. nach der Erstellung hat keine Änderung stattgefunden.

### is_deleted
- **Bedeutung**: Gibt an, ob der Spalteneintrag logisch gelöscht wurde.
- **Rolle**: Boolesches Kennzeichen.
- **Typischer Inhalt**: `True` oder `False`.
- **Hinweis**: Hilft bei der Verwaltung weicher Löschungen, ohne Daten physisch zu entfernen.

```
