# Document Import log

## Spalten

* `id`: integer
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `original_filename`: internal
* `filename`: internal
* `imported_on`: internal
* `source_type`: internal
* `source`: internal
* `success`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `import_id`: text
* `extra_data`: text
* `doc_id`: internal
* `email_connection_id`: integer
* `subject`: internal
* `body`: text
* `sender`: internal
* `error_resp`: internal
* `source_received_on`: timestamp with time zone

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.document_import_log`

## Einführung

Die Tabelle `public.document_import_log` dient dazu, die Details von Dokumentimporten in das System zu protokollieren. Sie erfasst Informationen zu jedem Dokument, darunter Herkunft, Importstatus und zugehörige Metadaten. Die Tabelle ist wesentlich, um Importaktivitäten nachzuverfolgen und Probleme zu diagnostizieren, die beim Import auftreten können.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Ein eindeutiger Bezeichner für jeden Eintrag im Importprotokoll.
- **Rolle**: Primärschlüssel
- **Typischer Inhalt**: Fortlaufende Ganzzahlwerte, die jeden Datensatz eindeutig identifizieren.

### org_id
- **Bedeutung**: Der Bezeichner der Organisation, die dem Import zugeordnet ist.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: UUID oder ähnlicher eindeutiger String-Bezeichner, der die Organisation darstellt.

### sub_org_id
- **Bedeutung**: Der Bezeichner einer Unterorganisation oder Abteilung innerhalb der Hauptorganisation.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: UUID oder ähnlicher eindeutiger String-Bezeichner; kann `None` sein, wenn nicht zutreffend.

### original_filename
- **Bedeutung**: Der ursprüngliche Name der Dokumentdatei beim Hochladen.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Zeichenfolge, die den Dateinamen darstellt, z. B. `anton_invoice-1.pdf`.

### filename
- **Bedeutung**: Der Name der Dokumentdatei, nachdem sie verarbeitet oder im System gespeichert wurde.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Zeichenfolge, die den Dateinamen darstellt, oft identisch mit `original_filename`.

### imported_on
- **Bedeutung**: Datum und Uhrzeit, zu denen das Dokument importiert wurde.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Zeitstempel im ISO-8601-Format.

### source_type
- **Bedeutung**: Der Typ der Quelle, aus der das Dokument importiert wurde.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Zeichenfolge, z. B. `EMAIL`, die den Quelltyp angibt.

### source
- **Bedeutung**: Detaillierte Informationen zur Quelle des Imports.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Zeichenfolge mit Details zur Quelle, z. B. `Email:O365:demo@fellow-digital.de:Tini Test`.

### success
- **Bedeutung**: Gibt an, ob der Import erfolgreich war.
- **Rolle**: Statusfeld
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

### created_by
- **Bedeutung**: Der Bezeichner des Benutzers, der den Import gestartet hat.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: Ganzzahl, die die Benutzer-ID darstellt.

### created_on
- **Bedeutung**: Datum und Uhrzeit, zu denen der Importprotokolleintrag erstellt wurde.
- **Rolle**: Technisches Feld
- **Typischer Inhalt**: Zeitstempel mit Zeitzone.

### last_modified_on
- **Bedeutung**: Datum und Uhrzeit der letzten Änderung des Importprotokolleintrags.
- **Rolle**: Technisches Feld
- **Typischer Inhalt**: Zeitstempel mit Zeitzone; kann `None` sein, wenn nicht geändert.

### is_deleted
- **Bedeutung**: Gibt an, ob der Importprotokolleintrag als gelöscht markiert wurde.
- **Rolle**: Statusfeld
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

### import_id
- **Bedeutung**: Ein eindeutiger Bezeichner für den Importvorgang.
- **Rolle**: Technisches Feld
- **Typischer Inhalt**: Zeichenfolge oder Text, die eine eindeutige Prozess-ID darstellt.

### extra_data
- **Bedeutung**: Zusätzliche Metadaten zum Import.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: JSON-Zeichenfolge mit zusätzlichen Daten wie Datum, Absender, Betreff und Anzahl.

### doc_id
- **Bedeutung**: Der Bezeichner des Dokuments.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: UUID oder ähnlicher eindeutiger String-Bezeichner; kann `None` sein.

### email_connection_id
- **Bedeutung**: Der Bezeichner der E-Mail-Verbindung, die für den Import verwendet wurde.
- **Rolle**: Fremdschlüssel
- **Typischer Inhalt**: Ganzzahl, die die ID der E-Mail-Verbindung darstellt; kann `None` sein.

### subject
- **Bedeutung**: Die Betreffzeile der E-Mail, aus der das Dokument importiert wurde.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Zeichenfolge, die den E-Mail-Betreff darstellt.

### body
- **Bedeutung**: Der Textinhalt der E-Mail, aus der das Dokument importiert wurde.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Text mit dem Inhalt der E-Mail; kann `None` sein.

### sender
- **Bedeutung**: Die E-Mail-Adresse des Absenders des Dokuments.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Zeichenfolge mit der E-Mail-Adresse des Absenders.

### error_resp
- **Bedeutung**: Fehlerantwort oder Fehlermeldung, wenn der Import fehlgeschlagen ist.
- **Rolle**: Statusfeld
- **Typischer Inhalt**: Zeichenfolge mit Fehlerdetails; kann `None` sein.

### source_received_on
- **Bedeutung**: Datum und Uhrzeit, zu denen das Dokument von der Quelle empfangen wurde.
- **Rolle**: Beschreibendes Feld
- **Typischer Inhalt**: Zeitstempel mit Zeitzone.

Diese Dokumentation bietet einen detaillierten Überblick über die Tabelle `public.document_import_log` und ihre Spalten, die für das Verständnis und die Verwaltung von Dokumentimporten im System wesentlich sind.
```
