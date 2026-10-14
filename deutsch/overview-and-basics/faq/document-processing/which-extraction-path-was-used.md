# Welcher Extraktionspfad wurde verwendet?

„Warum sieht diese Tabelle so aus?“ beantworten Sie, indem Sie herausfinden, *was* DocBits für dieses Dokument getan hat: gespeicherte Regeln, die KI-Tabelle, welche KI-Stufe, und wo es schiefgelaufen ist. Diese Seite ist die Checkliste, die Support und Partner durchgehen, bevor sie eine Konfiguration ändern.

## 1. Die Tabs im Validierungsbildschirm ansehen

Öffnen Sie das Dokument und sehen Sie sich die Tabs über der Positionstabelle an:

| Was Sie sehen | Pfad |
|---|---|
| Zeilen im Tab **Extrahierte Tabelle** | Regelbasierter Pfad. Der Lieferant hat eine trainierte Tabelle; die Zeilen stammen aus den gespeicherten Koordinatenregeln, und die KI war nicht beteiligt (außer bei Spalten mit *KI nutzen*). |
| Zeilen im Tab **KI Extrahierte Tabelle**, Feld *Tags* darunter | KI-Pfad. Keine gespeicherten Regeln haben gepasst; die KI-Tabellenextraktion hat die Zeilen erzeugt, mit der KI-Stufe der Organisation oder der Stufe, die für diesen Lieferanten unter *Weitere Einstellungen* → *Lieferantenbasiertes KI-Modell* festgelegt ist. |
| Tooltip *AI table not found* am KI-Tab | Der KI-Pfad ist gelaufen und hat für dieses Dokument nichts geliefert. |
| Gar keine Tabellen-Tabs | Beide Tabelleneinstellungen sind für die Organisation ausgeschaltet; nichts hat die Tabelle extrahiert. |
| *No line items yet* (Noch keine Einzelposten) | Der Pfad ist gelaufen, hat aber keine Zeilen gefunden (kein lesbarer Text, keine Tabelle auf der Seite, oder die Regeln haben auf dieses Layout nicht gepasst). |

Kopffelder tragen neben dem Wert ein eigenes Quellen-Kennzeichen: *Extracted using AI*, *Learned from validated AI extraction*, *Extracted using saved rules (FELLOW_KV2)* (Mit gespeicherten Regeln extrahiert), *Extracted from electronic document*, *Calculated from vendor master data* (Berechnet aus Kreditorenstammdaten). Diese Kennzeichen beschreiben das Kopffeld, nicht die Tabelle.

## 2. Die Konfiguration des Lieferanten prüfen

* **Einstellungen → Dokumentenverarbeitung → Klassifizierung und Extraktion → AI-Modell**: Die Tabelle unter der Auswahl listet jeden Lieferanten mit einem gespeicherten Modell oder Training. Ein Lieferant in dieser Liste mit *Trainingsdaten* hat gespeicherte Regeln; *Trainingsdaten zurücksetzen* entfernt sie.
* **Einstellungen → Dokumentenverarbeitung → OCR-Einstellungen**: *E-Text verwenden, falls verfügbar* und *Verwenden Sie AI-Daten für Tabellen, falls verfügbar* ändern, welchen Text die Extraktion sieht. Ein Lieferant kann E-Text unter *Weitere Einstellungen* im Validierungsbildschirm überschreiben.
* **Einstellungen → Globale Einstellungen → Dokumenttypen → Tabellenspalten**: die Kennzeichen Versteckt, Erforderlich und *KI nutzen*. Eine versteckte Spalte wird nie gefüllt; eine Spalte mit *KI nutzen* wird auch bei Lieferanten mit Regeln von der KI gefüllt.

## 3. Ohne die Oberfläche reproduzieren (API / MCP)

Mit API- oder MCP-Zugang können Sie dieselben Fragen programmatisch stellen:

| Frage | Tool |
|---|---|
| Wurde diese Tabelle von der KI erzeugt? | `get_extracted_tables(doc_id)`: Jede Tabelle trägt `is_ai_table: true/false`. |
| Was liefern die Regeln, was liefert die KI? | `get_table_extraction_report(doc_id, mode="nonai")` und noch einmal mit `mode="ai"`; der Bericht zeigt die konfigurierte Struktur, die extrahierten Zeilen und die Seitenvorschau für jeden Pfad. Vergleichen Sie beide. |
| Welche Spalten sind konfiguriert, mit welchen Kennzeichen? | `get_table_config(doc_type)` |
| Spielt die KI-Stufe eine Rolle? | `compare_table_extraction_models(doc_id)` führt zwei Stufen auf demselben Dokument aus (benötigt ein Dokument mit Lieferantennummer). |
| Die Extraktion auf diesem Dokument wiederholen | `extract_table_ai(doc_id)` (KI) oder `restart_document(doc_id)` (gesamte Pipeline). |
| Was hat die Pipeline für dieses Dokument protokolliert? | `get_document_logs(doc_id)` |

Die DocBits-MCP-Tools sind auf der Seite *DocBits MCP* der englischen Dokumentation beschrieben.

## 4. Die Protokolle lesen

**Einstellungen → Log-Einstellungen** (Aktivitätsprotokollierung) zeigt die Ereignisse aller Dienste. Für eine Tabellenfrage:

* Filtern Sie unter *Protokolle durchsuchen* nach dem Dateinamen oder der ID des Dokuments.
* Verwenden Sie den Filter *Dienst*: Die Extraktion selbst läuft im Extraktionsdienst und in den Celery-Workern, nicht im Dienst `api`. Sehen Sie nur `api`-Zeilen, erweitern Sie den Filter.
* Ein normaler Lauf protokolliert der Reihe nach: Dokument empfangen → OCR / E-Text → Klassifizierung → Feldextraktion → Tabellenextraktion (Regelsuche, dann KI, wenn keine Regeln passen) → Validierung → Statuswechsel. Der Schritt, der fehlt oder einen Fehler meldet, ist der, den Sie sich ansehen müssen.

## 5. Entscheiden: Konfiguration, Daten oder Fehler

| Symptom | Wahrscheinlichste Ursache | Nächster Schritt |
|---|---|---|
| Tabelle bei Lieferant A richtig, bei Lieferant B falsch, gleicher Dokumenttyp | Lieferantenspezifisch: B hat keine Regeln, oder alte Regeln, die nicht mehr auf das Layout von B passen | Tabelle von B einmal trainieren (oder die Regeln von B löschen, damit die KI übernimmt). |
| Tabelle seit einem bestimmten Datum bei jedem Lieferanten falsch | Organisationseinstellung geändert (KI-Stufe, strukturierte Extraktion, Vision, Tabellenspalten) | Einstellungen mit dem Änderungsdatum vergleichen; ein Dokument neu starten, um es zu bestätigen. |
| Gleiches Dokument: Regelpfad leer, KI-Pfad richtig | Die Regeln passen nicht auf diese Layoutvariante | Mit diesem Dokument neu trainieren, oder die Regeln löschen. |
| Gleiches Dokument: beide Pfade leer | Kein lesbarer Text (Scan ohne OCR-Text, reines Bild-PDF) | OCR-Ansicht im Validierungsbildschirm; E-Text aktivieren, wenn das PDF eine Textebene hat; eine andere OCR-Version ausprobieren. |
| Eine Spalte in jeder Zeile falsch, der Rest in Ordnung | Spaltenzuordnung oder Kennzeichen *KI nutzen* | Tabellenspalten-Einstellungen; im Tabellentraining neu zuordnen. |
| Zeilen fehlen bei Seitenumbrüchen oder nach einer Zwischensumme | Layout, dem die KI oder die Regeln nicht gefolgt sind | Tabelle mit einem mehrseitigen Dokument trainieren; ein Tag wie *„Tabelle wird auf Seite 2 fortgesetzt“* hinzufügen. |
| Extraktionsschritt fehlt in den Protokollen, Dokument hängt in *running* | Infrastruktur (Worker-Rückstau), keine Konfiguration | Ausstehende Aufgaben prüfen (`get_pending_tasks_detail` über MCP) und den Support mit der Dokument-ID kontaktieren. |

## Was Sie an den Support senden

* Dokument-ID und Organisation
* Welcher Tab die Zeilen enthält (Extrahierte Tabelle / KI Extrahierte Tabelle / keiner) und die verwendete KI-Stufe
* Ob der Lieferant gespeicherte Regeln hat und wann sie zuletzt gespeichert wurden
* Ein Beispieldokument, bei dem es funktioniert, und eines, bei dem nicht, falls Sie beide haben

## Weitere Seiten

* [Tabellenauszug Fehlerbehebung](table-extraction-troubleshoot.md): Extraktionsqualität, OCR, E-Text, Meldungen an der Tabelle
* [Schulung Linienfelder/Tabelle Schulung](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [KI-Tabelle](../../../end-user-and-partner-section/end-user-section/ai-table/README.md)
* [Log-Einstellungen](../../../administration-and-setup/settings/log-settings/README.md)
