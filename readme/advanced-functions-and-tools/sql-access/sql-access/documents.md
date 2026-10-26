# Dokumente

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `batch_id`: intern
* `doc_path`: intern
* `doc_type`: Dokumenttyp
* `status`: intern
* `message`: text
* `export_attempts`: integer
* `last_attempted_on`: timestamp with time zone
* `next_attempt_on`: timestamp with time zone
* `assigned_to`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `task_id`: intern
* `filename`: intern
* `assigned_on`: timestamp with time zone
* `pages`: integer
* `auto_processed`: boolean
* `exception_info`: text
* `doc_language`: Language
* `is_trimmed`: boolean
* `doc_origin`: Doc Origin
* `doc_locale`: Doc Locale
* `is_doc2landing_doc`: boolean
* `extraction_time`: double precision
* `export_time`: double precision
* `po_all_matched`: boolean
* `restart_allowed`: boolean
* `table_version`: intern
* `force_ocr`: boolean
* `locked_by`: integer
* `locked_on`: timestamp with time zone
* `lock_renewed_on`: timestamp with time zone
* `lock_key`: intern
* `last_saved_by`: integer
* `last_saved_on`: timestamp with time zone
* `document_version`: integer
* `lock_session_key`: intern
* `sub_org_id`: intern
* `doc_source`: intern
* `sub_doc_type`: intern
* `assigned_to_group`: intern
* `status_changed_on`: timestamp with time zone
* `improve_quality`: boolean
* `priority`: integer
* `metadata_field`: json
* `doc_classification_label`: intern
* `doc_start_page`: integer
* `doc_classification_class`: intern
* `celery_task_token`: intern
* `celery_task_attempt`: integer
* `celery_task_priority`: integer
* `has_zugferd`: boolean
* `has_peppol`: boolean
* `timestamp_for_validation`: timestamp with time zone
* `exception_details`: text
* `has_annotated_version`: boolean
* `po_match_status`: intern
* `tr_ocr_extracted_data`: text
* `pending_workflow_execution`: boolean
* `extracted_document_id`: intern
* `extracted_supplier_id`: intern
* `classification_manually_corrected`: boolean
* `supplier_as_org_id`: intern
* `extracted_data_basic`: jsonb
* `celery_task_queue`: intern
* `extracted_data`: jsonb
* `extracted_data_jsonb`: jsonb
* `warnings`: jsonb

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.documents`

## Einführung

Die Tabelle `public.documents` speichert und verwaltet Metadaten und Verarbeitungsinformationen zur Dokumentenverarbeitung innerhalb einer Organisation. Dazu gehören der Dokumentstatus, Verarbeitungsversuche, die Sprache und weitere administrative Details. Die Tabelle unterstützt die Dokumentklassifizierung, den Verarbeitungsworkflow und Benutzerzuweisungen und ist damit ein zentraler Bestandteil des Dokumentenmanagementsystems.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutige Kennung für jedes Dokument.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die das Dokument darstellt.

### org_id
- **Bedeutung**: Kennung der Organisation, die dem Dokument zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Organisation darstellt.

### batch_id
- **Bedeutung**: Kennung des Batches, in dem das Dokument verarbeitet wurde.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die den Batch darstellt.

### doc_path
- **Bedeutung**: Dateipfad, unter dem das Dokument gespeichert ist.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Pfad zur Dokumentdatei, z. B. `documents/{id}/{id}.pdf`.

### doc_type
- **Bedeutung**: Typ des gespeicherten Dokuments (z. B. Rechnung).
- **Rolle**: Dokumentklassifizierung.
- **Typischer Inhalt**: Eine Zeichenfolge wie `INVOICE`.

### status
- **Bedeutung**: Aktueller Verarbeitungsstatus des Dokuments.
- **Rolle**: Workflow-Indikator.
- **Typischer Inhalt**: Eine Zeichenfolge, die den Status angibt, z. B. `ready_for_validation`.

### message
- **Bedeutung**: Informationen zum Verarbeitungszustand des Dokuments oder zu Fehlern.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Text, der Fehler oder Meldungen zur Dokumentverarbeitung beschreibt.

### export_attempts
- **Bedeutung**: Anzahl der Exportversuche für das Dokument.
- **Rolle**: Verarbeitungsverfolgung.
- **Typischer Inhalt**: Ganzzahl mit der Anzahl der Exportversuche.

### last_attempted_on
- **Bedeutung**: Zeitstempel des letzten Versuchs, das Dokument zu verarbeiten oder zu exportieren.
- **Rolle**: Zeitstempelfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### next_attempt_on
- **Bedeutung**: Geplanter Zeitstempel für den nächsten Versuch, das Dokument zu verarbeiten oder zu exportieren.
- **Rolle**: Planungsfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### assigned_to
- **Bedeutung**: Kennung des Benutzers, dem dieses Dokument zugewiesen ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Ganzzahl, die die Benutzer-ID darstellt.

### created_by
- **Bedeutung**: Kennung des Benutzers, der das Dokument erstellt oder hochgeladen hat.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Ganzzahl, die die Benutzer-ID darstellt.

### created_on
- **Bedeutung**: Zeitstempel, wann das Dokument erstellt oder hochgeladen wurde.
- **Rolle**: Zeitstempelfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung am Dokumentdatensatz.
- **Rolle**: Zeitstempelfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### is_deleted
- **Bedeutung**: Gibt an, ob das Dokument als gelöscht markiert ist.
- **Rolle**: Kennzeichen für logisches Löschen.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### task_id
- **Bedeutung**: Kennung der Aufgabe, die der Dokumentverarbeitung zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Aufgabe darstellt.

### filename
- **Bedeutung**: Ursprünglicher Dateiname des Dokuments.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Name der Datei, z. B. `document.pdf`.

### assigned_on
- **Bedeutung**: Zeitstempel, wann das Dokument einem Benutzer zugewiesen wurde.
- **Rolle**: Zeitstempelfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### pages
- **Bedeutung**: Anzahl der Seiten des Dokuments.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ganzzahl, die die Seitenanzahl angibt.

### auto_processed
- **Bedeutung**: Gibt an, ob das Dokument automatisch verarbeitet wurde.
- **Rolle**: Kennzeichen für den Verarbeitungsstatus.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### exception_info
- **Bedeutung**: Informationen zu Ausnahmen, die bei der Verarbeitung aufgetreten sind.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Text, der Verarbeitungsausnahmen beschreibt.

### doc_language
- **Bedeutung**: Sprache des Dokumentinhalts.
- **Rolle**: Sprachklassifizierung.
- **Typischer Inhalt**: ISO-Sprachcode, z. B. `en`, `de`.

### is_trimmed
- **Bedeutung**: Gibt an, ob das Dokument zugeschnitten oder beschnitten wurde.
- **Rolle**: Kennzeichen für Dokumentänderungen.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### doc_origin
- **Bedeutung**: Herkunft des Dokuments, möglicherweise das Land oder das Quellsystem.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ländercode oder Herkunftskennung, z. B. `DE`.

### doc_locale
- **Bedeutung**: Gebietsschema-Einstellungen des Dokuments, die Sprache und Region angeben.
- **Rolle**: Gebietsschema-Klassifizierung.
- **Typischer Inhalt**: Zeichenfolge für das Gebietsschema, z. B. `de_DE.ISO8859-1`.

### is_doc2landing_doc
- **Bedeutung**: Gibt an, ob das Dokument zu einem bestimmten Verarbeitungsworkflow (Doc2Landing) gehört.
- **Rolle**: Workflow-Kennzeichen.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### extraction_time
- **Bedeutung**: Zeit, die für die Extraktion der Daten aus dem Dokument benötigt wurde.
- **Rolle**: Leistungskennzahl.
- **Typischer Inhalt**: Wert mit doppelter Genauigkeit, der die Extraktionszeit darstellt.

### export_time
- **Bedeutung**: Zeit, die für den Export des Dokuments benötigt wurde.
- **Rolle**: Leistungskennzahl.
- **Typischer Inhalt**: Wert mit doppelter Genauigkeit, der die Exportzeit darstellt.

### po_all_matched
- **Bedeutung**: Gibt an, ob alle zum Dokument gehörenden Bestellungen abgeglichen wurden.
- **Rolle**: Kennzeichen für den Abgleichstatus.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### restart_allowed
- **Bedeutung**: Gibt an, ob die Dokumentverarbeitung neu gestartet werden kann.
- **Rolle**: Kennzeichen zur Workflow-Steuerung.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### table_version
- **Bedeutung**: Version der Tabellenstruktur, die für das Dokument verwendet wird.
- **Rolle**: Versionsverwaltung.
- **Typischer Inhalt**: Zeichenfolge, die die Version angibt, z. B. `v3`.

### force_ocr
- **Bedeutung**: Gibt an, ob die OCR-Verarbeitung für das Dokument erzwungen wird.
- **Rolle**: Kennzeichen zur Verarbeitungssteuerung.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### locked_by
- **Bedeutung**: Kennung des Benutzers, der das Dokument zur Bearbeitung gesperrt hat.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Ganzzahl, die die Benutzer-ID darstellt.

### locked_on
- **Bedeutung**: Zeitstempel, wann das Dokument zur Bearbeitung gesperrt wurde.
- **Rolle**: Zeitstempelfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### lock_renewed_on
- **Bedeutung**: Zeitstempel, wann die Dokumentsperre zuletzt erneuert wurde.
- **Rolle**: Zeitstempelfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### lock_key
- **Bedeutung**: Schlüssel, der der Dokumentsperre zugeordnet ist.
- **Rolle**: Sperrsteuerung.
- **Typischer Inhalt**: Zeichenfolge, die den Sperrschlüssel darstellt.

### last_saved_by
- **Bedeutung**: Kennung des Benutzers, der das Dokument zuletzt gespeichert hat.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Ganzzahl, die die Benutzer-ID darstellt.

### last_saved_on
- **Bedeutung**: Zeitstempel, wann das Dokument zuletzt gespeichert wurde.
- **Rolle**: Zeitstempelfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### document_version
- **Bedeutung**: Versionsnummer des Dokuments.
- **Rolle**: Versionsverfolgung.
- **Typischer Inhalt**: Ganzzahl, die die Dokumentversion darstellt.

### lock_session_key
- **Bedeutung**: Sitzungsschlüssel, der der Dokumentsperre zugeordnet ist.
- **Rolle**: Sperrsteuerung.
- **Typischer Inhalt**: Zeichenfolge, die den Sitzungsschlüssel darstellt.

### sub_org_id
- **Bedeutung**: Kennung einer Unterorganisation, die dem Dokument zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Unterorganisation darstellt.

### doc_source
- **Bedeutung**: Quellsystem oder Herkunft des Dokuments.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolge, die die Quelle angibt, z. B. `doc2app`.

### sub_doc_type
- **Bedeutung**: Klassifizierung des Dokumentuntertyps.
- **Rolle**: Dokumentklassifizierung.
- **Typischer Inhalt**: Zeichenfolge, die den Untertyp angibt.

### assigned_to_group
- **Bedeutung**: Kennung der Gruppe, der das Dokument zugewiesen ist.
- **Rolle**: Zuweisungsverfolgung.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Gruppe darstellt.

### status_changed_on
- **Bedeutung**: Zeitstempel, wann sich der Status des Dokuments zuletzt geändert hat.
- **Rolle**: Zeitstempelfeld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### improve_quality
- **Bedeutung**: Gibt an, ob Prozesse zur Qualitätsverbesserung auf das Dokument angewendet werden.
- **Rolle**: Kennzeichen zur Qualitätskontrolle.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### priority
- **Bedeutung**: Verarbeitungspriorität des Dokuments.
- **Rolle**: Workflow-Steuerung.
- **Typischer Inhalt**: Ganzzahl, die die Prioritätsstufe angibt.

### metadata_field
- **Bedeutung**: JSON-Feld mit Metadaten zum Dokument.
- **Rolle**: Metadatenspeicher.
- **Typischer Inhalt**: JSON-Struktur mit verschiedenen Metadatenfeldern.

### doc_classification_label
- **Bedeutung**: Bezeichnung, die die Klassifizierung des Dokuments angibt.
- **Rolle**: Klassifizierungsbezeichnung.
- **Typischer Inhalt**: Zeichenfolge, die die Klassifizierung angibt, z. B. `INVOICE`.

### doc_start_page
- **Bedeutung**: Seitennummer, auf der der Dokumentinhalt beginnt.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ganzzahl, die die Startseite angibt.

### doc_classification_class
- **Bedeutung**: Klasse, die die detaillierte Klassifizierung des Dokuments angibt.
- **Rolle**: Klassifizierungsdetail.
- **Typischer Inhalt**: Zeichenfolge, die die Klassifizierungsklasse angibt.

### celery_task_token
- **Bedeutung**: Token zur Verfolgung der dem Dokument zugeordneten Celery-Aufgabe.
- **Rolle**: Aufgabenverfolgung.
- **Typischer Inhalt**: Zeichenfolge, die das Aufgaben-Token darstellt.

### celery_task_attempt
- **Bedeutung**: Anzahl der Versuche für die Celery-Aufgabe.
- **Rolle**: Aufgabenverfolgung.
- **Typischer Inhalt**: Ganzzahl mit der Anzahl der Aufgabenversuche.

### celery_task_priority
- **Bedeutung**: Prioritätsstufe der Celery-Aufgabe.
- **Rolle**: Aufgabensteuerung.
- **Typischer Inhalt**: Ganzzahl, die die Aufgabenpriorität angibt.

### has_zugferd
- **Bedeutung**: Gibt an, ob das Dokument im ZUGFeRD-Format vorliegt.
- **Rolle**: Formatindikator.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### has_peppol
- **Bedeutung**: Gibt an, ob das Dokument im PEPPOL-Format vorliegt.
- **Rolle**: Formatindikator.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### timestamp_for_validation
- **Bedeutung**: Zeitstempel, wann das Dokument validiert wurde.
- **Rolle**: Validierungsverfolgung.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone.

### exception_details
- **Bedeutung**: Detaillierte Informationen zu Ausnahmen während der Verarbeitung.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Text mit Details zu den Ausnahmen.

### has_annotated_version
- **Bedeutung**: Gibt an, ob eine annotierte Version des Dokuments vorhanden ist.
- **Rolle**: Versionsindikator.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### po_match_status
- **Bedeutung**: Status des Bestellabgleichs.
- **Rolle**: Indikator für den Abgleichstatus.
- **Typischer Inhalt**: Zeichenfolge, die den Abgleichstatus angibt.

### tr_ocr_extracted_data
- **Bedeutung**: Per OCR aus dem Dokument extrahierte Daten.
- **Rolle**: Datenspeicher.
- **Typischer Inhalt**: Text mit den extrahierten Daten.

### pending_workflow_execution
- **Bedeutung**: Gibt an, ob ausstehende Workflow-Ausführungen vorhanden sind.
- **Rolle**: Kennzeichen für den Workflow-Status.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### extracted_document_id
- **Bedeutung**: Kennung des extrahierten Dokuments.
- **Rolle**: Extraktionsverfolgung.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die das extrahierte Dokument darstellt.

### extracted_supplier_id
- **Bedeutung**: Kennung des extrahierten Lieferanten.
- **Rolle**: Extraktionsverfolgung.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die den extrahierten Lieferanten darstellt.

### classification_manually_corrected
- **Bedeutung**: Gibt an, ob die Klassifizierung des Dokuments manuell korrigiert wurde.
- **Rolle**: Kennzeichen für den Klassifizierungsstatus.
- **Typischer Inhalt**: Boolescher Wert (True oder False).

### supplier_as_org_id
- **Bedeutung**: Kennung des Lieferanten, der als Organisation behandelt wird.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Lieferantenorganisation darstellt.

### extracted_data_basic
- **Bedeutung**: Extrahierte Basisdaten im JSONB-Format.
- **Rolle**: Datenspeicher.
- **Typischer Inhalt**: JSONB-Struktur mit den extrahierten Datenfeldern.

### celery_task_queue
- **Bedeutung**: Name der Celery-Aufgabenwarteschlange.
- **Rolle**: Aufgabenverwaltung.
- **Typischer Inhalt**: Zeichenfolge, die den Warteschlangennamen angibt.

### extracted_data
- **Bedeutung**: Aus dem Dokument extrahierte Daten im JSONB-Format.
- **Rolle**: Datenspeicher.
- **Typischer Inhalt**: JSONB-Struktur mit den extrahierten Datenfeldern.

### extracted_data_jsonb
- **Bedeutung**: JSONB-Feld mit detaillierten extrahierten Daten.
- **Rolle**: Datenspeicher.
- **Typischer Inhalt**: JSONB-Struktur mit den extrahierten Datenfeldern.

### warnings
- **Bedeutung**: Warnungen zur Dokumentverarbeitung, gespeichert im JSONB-Format.
- **Rolle**: Warnungsspeicher.
- **Typischer Inhalt**: JSONB-Struktur mit Warnmeldungen.
```
