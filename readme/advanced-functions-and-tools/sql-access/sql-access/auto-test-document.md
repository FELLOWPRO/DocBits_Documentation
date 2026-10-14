# Auto test document

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `extracted_data`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `filename`: internal

## Analyse & Beschreibung

```markdown
# Tabellendokumentation: `public.auto_test_document`

## Einführung

Die Tabelle `public.auto_test_document` dient der Speicherung von Metadaten und Extraktionsergebnissen aus der Dokumentenverarbeitung innerhalb einer Organisation. Die Tabelle erfasst Informationen zu Dokumenten, ihren Typen und den daraus extrahierten Daten. Sie enthält Felder zur Dokumentidentifikation, Verarbeitungsmetadaten und Statuskennzeichen, die für die Verwaltung von Dokumenten-Workflows und die Sicherstellung der Datenintegrität wesentlich sind.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutiger Bezeichner für jeden Dokumenteintrag in der Tabelle.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: UUID-Zeichenfolge.
- **Hinweis**: Dient als eindeutiger Bezeichner für Datensätze und stellt sicher, dass sich jeder Eintrag unterscheiden lässt.

### org_id
- **Bedeutung**: Bezeichner der Organisation, die dem Dokument zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: UUID-Zeichenfolge.
- **Hinweis**: Verknüpft das Dokument mit einer bestimmten Organisation im System.

### doc_id
- **Bedeutung**: Bezeichner des Dokuments, das verarbeitet wird.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: UUID-Zeichenfolge.
- **Hinweis**: Wird verwendet, um extrahierte Daten dem ursprünglichen Dokument zuzuordnen.

### doc_type
- **Bedeutung**: Typ oder Kategorie des Dokuments.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolge wie "MEDI_ORDER".
- **Hinweis**: Hilft bei der Kategorisierung von Dokumenten für Verarbeitung und Analyse.

### extracted_data
- **Bedeutung**: JSON-Struktur mit detaillierten, aus dem Dokument extrahierten Daten.
- **Rolle**: Datenfeld.
- **Typischer Inhalt**: JSON-Text mit Feldern, Werten und Extraktionsmetadaten.
- **Hinweis**: Speichert die Ergebnisse der Datenextraktion des Dokuments.

### created_by
- **Bedeutung**: Bezeichner des Benutzers, der den Dokumentdatensatz erstellt hat.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ganzzahl, die eine Benutzer-ID darstellt.
- **Hinweis**: Verfolgt, welcher Benutzer das Dokument im System angelegt hat.

### created_on
- **Bedeutung**: Zeitstempel, der angibt, wann der Dokumentdatensatz erstellt wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation.
- **Hinweis**: Nützlich für Audits und die Nachverfolgung des Lebenszyklus des Dokuments.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung am Dokumentdatensatz.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation.
- **Hinweis**: Hilft, Änderungen und Aktualisierungen des Dokumentdatensatzes nachzuverfolgen.

### is_deleted
- **Bedeutung**: Kennzeichen, das angibt, ob der Dokumentdatensatz als gelöscht markiert wurde.
- **Rolle**: Statusfeld.
- **Typischer Inhalt**: Boolescher Wert.
- **Hinweis**: Ermöglicht das weiche Löschen (Soft Delete) von Datensätzen und damit eine Wiederherstellung bei Bedarf.

### filename
- **Bedeutung**: Name der Datei, die dem Dokument zugeordnet ist.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolge, z. B. "7.pdf".
- **Hinweis**: Stellt einen Verweis auf die physische Datei bereit, die zum Dokumenteintrag gehört.

```
