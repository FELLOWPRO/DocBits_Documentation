# Document extracted data

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `field_name`: internal
* `field_value`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `field_type`: internal

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.document_extracted_data`

## Einführung

Die Tabelle `public.document_extracted_data` dient der Speicherung extrahierter Daten aus verschiedenen Dokumenten, vermutlich für die Dokumentverarbeitung und -analyse. Jeder Eintrag in der Tabelle entspricht einem bestimmten, aus einem Dokument (etwa einer Rechnung) extrahierten Feld und enthält Metadaten zum Extraktionsprozess. Die Tabelle erleichtert die Nachverfolgung und Verwaltung von Dokumentdaten, indem sie diese Organisationen und bestimmten Dokumenten zuordnet.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Ein eindeutiger Bezeichner für jeden Eintrag mit extrahierten Daten.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine im UUID-Format vorliegende Zeichenfolge, die den Datensatz mit extrahierten Daten eindeutig identifiziert.

### org_id
- **Bedeutung**: Bezeichner der Organisation, die den Dokumentdaten zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine im UUID-Format vorliegende Zeichenfolge, die die Organisation darstellt.

### doc_id
- **Bedeutung**: Bezeichner des Dokuments, aus dem Daten extrahiert wurden.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine im UUID-Format vorliegende Zeichenfolge, die das Dokument darstellt.

### field_name
- **Bedeutung**: Der Name des aus dem Dokument extrahierten Felds.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolgen wie 'invoice_id', 'invoice_date' usw., die die Art der extrahierten Daten angeben.

### field_value
- **Bedeutung**: Der Wert, der dem extrahierten Feld zugeordnet ist.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolgen, die verschiedene Datentypen wie Rechnungsnummern, Datumsangaben oder Beträge darstellen.

### created_by
- **Bedeutung**: Der Bezeichner des Benutzers oder Prozesses, der den Dateneintrag erstellt hat.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ganzzahl, die eine Benutzer-ID oder Prozess-ID darstellt.

### created_on
- **Bedeutung**: Der Zeitstempel, zu dem der Dateneintrag erstellt wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Zeitstempel mit Zeitzonendaten, der Erstellungsdatum und -uhrzeit angibt.

### last_modified_on
- **Bedeutung**: Der Zeitstempel der letzten Änderung am Dateneintrag.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Zeitstempel mit Zeitzonendaten, der Datum und Uhrzeit der letzten Änderung angibt (kann null sein, wenn nie geändert).

### is_deleted
- **Bedeutung**: Ein Kennzeichen, das angibt, ob der Dateneintrag als gelöscht markiert wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Boolescher Wert, wobei `False` aktive Einträge und `True` gelöschte Einträge kennzeichnet.

### field_type
- **Bedeutung**: Der Typ der Daten, die in der Spalte `field_value` gespeichert sind.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolgen wie 'date', 'AMOUNT' oder null, wenn der Typ nicht angegeben ist.

Dieses strukturierte Datenmodell ermöglicht die effiziente Speicherung und Abfrage dokumentbezogener Daten und unterstützt Anwendungen von der Rechnungsverarbeitung bis zum Compliance-Management.
```
