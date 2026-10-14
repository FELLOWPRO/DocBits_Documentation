# Document Report

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_id`: internal
* `doc_type`: DOC Type
* `sub_doc_type`: internal
* `time_spent`: internal
* `fields_total`: integer
* `fields_correct`: integer
* `checkbox_fields_total`: integer
* `checkbox_fields_correct`: integer
* `table_values_total`: integer
* `table_values_correct`: integer
* `detail_report`: text
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `validated_by`: integer
* `sub_org_id`: internal

## Analyse & Beschreibung

```markdown
# Tabellendokumentation Document Report

## Einführung
Die Tabelle `public.document_report` dient der Speicherung detaillierter Informationen zu Berichten über die Dokumentverarbeitung, insbesondere zur Validierung und Extraktion von Feldern aus Dokumenten wie Rechnungen. Die Tabelle erfasst Metadaten zum Dokument, Verarbeitungskennzahlen und Validierungsergebnisse, die für Audits, Nachverfolgung und die Verbesserung von Dokumentverarbeitungs-Workflows genutzt werden können.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutiger Bezeichner für jeden Eintrag im Dokumentbericht.
- **Rolle**: Primärschlüssel
- **Typischer Inhalt**: Eine UUID, die den eindeutigen Dokumentbericht darstellt.

### org_id
- **Bedeutung**: Bezeichner der Organisation, die dem Dokument zugeordnet ist.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: Eine UUID, die auf eine Organisation verweist.

### doc_id
- **Bedeutung**: Bezeichner des konkreten Dokuments, über das berichtet wird.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: Eine UUID, die das eindeutige Dokument darstellt.

### doc_type
- **Bedeutung**: Typ des verarbeiteten Dokuments, etwa eine Rechnung.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Werte wie `INVOICE`.

### sub_doc_type
- **Bedeutung**: Untertyp des Dokuments, der eine weitere Kategorisierung bietet.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Kann `null` sein oder bestimmte Untertypen wie "Cost Invoice" enthalten.

### time_spent
- **Bedeutung**: Für die Validierung des Dokuments aufgewendete Zeit.
- **Rolle**: Kennzahlfeld
- **Typischer Inhalt**: In der Regel '0'; die Zeit wird in vordefinierten Einheiten gemessen.

### fields_total
- **Bedeutung**: Gesamtzahl der aus dem Dokument extrahierten Felder.
- **Rolle**: Kennzahlfeld
- **Typischer Inhalt**: Eine Ganzzahl, die die Gesamtzahl der Felder darstellt, z. B. 13.

### fields_correct
- **Bedeutung**: Anzahl der korrekt extrahierten und validierten Felder.
- **Rolle**: Kennzahlfeld
- **Typischer Inhalt**: Eine Ganzzahl, die die korrekt verarbeiteten Felder darstellt, z. B. 12.

### checkbox_fields_total
- **Bedeutung**: Gesamtzahl der verarbeiteten Kontrollkästchenfelder.
- **Rolle**: Kennzahlfeld
- **Typischer Inhalt**: Meist `0`, d. h. keine Kontrollkästchenfelder verarbeitet.

### checkbox_fields_correct
- **Bedeutung**: Anzahl der korrekt validierten Kontrollkästchenfelder.
- **Rolle**: Kennzahlfeld
- **Typischer Inhalt**: Meist `0`, d. h. keine korrekt validierten Kontrollkästchenfelder.

### table_values_total
- **Bedeutung**: Gesamtzahl der aus dem Dokument extrahierten Tabellenwerte.
- **Rolle**: Kennzahlfeld
- **Typischer Inhalt**: Meist `0`, d. h. keine Tabellenwerte verarbeitet.

### table_values_correct
- **Bedeutung**: Anzahl der korrekt validierten Tabellenwerte.
- **Rolle**: Kennzahlfeld
- **Typischer Inhalt**: Meist `0`, d. h. keine korrekt validierten Tabellenwerte.

### detail_report
- **Bedeutung**: JSON-Inhalt mit einem detaillierten Bericht über die Dokumentfelder und deren Validierungsstatus.
- **Rolle**: Beschreibendes/technisches Feld
- **Typischer Inhalt**: JSON-Zeichenfolge mit detaillierten Feldinformationen.

### created_on
- **Bedeutung**: Zeitstempel, zu dem der Dokumentberichtseintrag erstellt wurde.
- **Rolle**: Technisches Feld
- **Typischer Inhalt**: Zeitstempel in UTC, z. B. `2025-03-10 08:07:24+00`.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung am Dokumentbericht.
- **Rolle**: Technisches Feld
- **Typischer Inhalt**: Zeitstempel in UTC, der den Zeitpunkt der letzten Aktualisierung angibt.

### is_deleted
- **Bedeutung**: Gibt an, ob der Dokumentbericht als gelöscht markiert wurde.
- **Rolle**: Technisches Feld
- **Typischer Inhalt**: Boolescher Wert; `False`, wenn nicht gelöscht.

### validated_by
- **Bedeutung**: Bezeichner des Benutzers, der das Dokument validiert hat.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: Ganzzahl, die die ID des Validierenden darstellt, z. B. `1`.

### sub_org_id
- **Bedeutung**: Bezeichner einer Unterorganisation, die zum Dokument gehört.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: Eine UUID, die auf eine Unterorganisation verweist.
```
