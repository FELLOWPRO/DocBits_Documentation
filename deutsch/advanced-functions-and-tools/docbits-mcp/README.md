# DocBits MCP

DocBits stellt einen **Model Context Protocol (MCP)**-Server bereit, mit dem KI-Assistenten direkt aus einem Chat oder einer Coding-Sitzung heraus mit Ihren Dokumenten, der Extraktion, der Suche, den Analysen und der Konfiguration arbeiten können. Jeder MCP-kompatible Client kann sich verbinden: **Claude Code**, **Claude Desktop**, **Google Gemini CLI**, **OpenAI Codex** oder jede benutzerdefinierte Integration.

Der Server ist in die DocBits-API unter `/v3/mcp` eingebunden und auf Ihre Organisation beschränkt – jeder Aufruf läuft mit den Berechtigungen des Benutzers (oder API-Schlüssels), der die Verbindung hergestellt hat.

{% hint style="info" %}
**Endpunkt – verwenden Sie Ihre Region (EU oder US):**

* Produktion (EU) — `https://eu.api.docbits.com/v3/mcp`
* Produktion (US) — `https://us.api.docbits.com/v3/mcp`

Die vollständige Host-Matrix und die Anmeldung per OAuth finden Sie unter [Einrichtung & Konfiguration](setup-and-configuration.md).
{% endhint %}

## Was können Sie tun?

Mit DocBits MCP kann ein Assistent in Ihrem Auftrag:

* **Dokumente finden und lesen** — auflisten, suchen (Volltext und feldbezogen), ein Dokument öffnen, seinen Status, seine Protokolle, Seitenbilder und die Exportvorschau lesen
* **Mit extrahierten Daten arbeiten** — extrahierte Felder und Tabellen lesen, Feldwerte korrigieren, Tabellen mit KI extrahieren, validieren, genehmigen und in Ihr ERP exportieren
* **Das Dashboard abfragen** — Dashboard-Abfragen in natürlicher Sprache ausführen, Suchmodi vergleichen und Suchfunktionen einsehen
* **Analysen abrufen** — Management-Zusammenfassungen, Erfolgsraten, Volumentrends, häufigste Dokumenttypen und Details zu offenen Aufgaben
* **E-Rechnungen (eDocs) verarbeiten** — Typen elektronischer Dokumente auflisten, E-Dokumente testen und verifizieren, benutzerdefinierte Extraktionsattribute verwalten
* **Stammdaten verwalten** — Lieferantenstammdaten anlegen oder aktualisieren, Lieferantensuchen auslösen, Lieferantenrechnungs-BODs importieren, Zuordnungen für Zahlungsbedingungen und Skonti pflegen
* **Konfiguration lesen und ändern** — Organisationseinstellungen, Dokumenttypen, Feldeinstellungen, Benutzer und Cache
* **Den Zustand prüfen** — API- und Celery-Health, aktueller Benutzer und API-Informationen

## Tools-Übersicht

DocBits MCP gruppiert weit über hundert Tools in die unten stehenden Kategorien (die genaue Anzahl wächst mit jedem Release; Ihr Assistent listet den aktuellen Umfang auf). Die meisten entsprechen bestehenden DocBits-REST-Endpunkten, Details zu Anfrage und Antwort finden Sie in der [API-Referenz](../../). Ein Assistent wählt anhand Ihrer Anfrage automatisch das passende Tool; die Tabellen sind eine Übersicht darüber, was verfügbar ist.

### Dokumente & Verarbeitung

| Tool                                    | Beschreibung                                                      |
| --------------------------------------- | ----------------------------------------------------------------- |
| `list_documents`                        | Dokumente der Organisation auflisten (filterbar)                  |
| `get_document` / `get_document_by_name` | Ein Dokument anhand von ID oder Dateiname öffnen                  |
| `upload_document`                       | Ein neues Dokument zur Verarbeitung hochladen                     |
| `get_document_status`                   | Aktueller Pipeline-Status eines Dokuments                         |
| `get_document_logs`                     | Verarbeitungsprotokolleinträge eines Dokuments                    |
| `query_org_logs`                        | Die Service-Protokolle der Organisation seitenweise durchblättern |
| `restart_document`                      | Die Verarbeitungspipeline erneut ausführen                        |
| `delete_document`                       | Ein Dokument löschen                                              |
| `get_pending_documents_count`           | Wie viele Dokumente auf Validierung warten                        |

### Extraktion & Validierung

| Tool                                                | Beschreibung                                                                                            |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `get_extracted_fields` / `get_document_fields`      | Extrahierte Kopffelder lesen                                                                            |
| `get_extracted_tables`                              | Extrahierte Positionstabellen lesen                                                                     |
| `get_document_for_validation` / `get_next_document` | Ein Dokument so öffnen, wie es der Validierungsbildschirm tut; das nächste in der Warteschlange abrufen |
| `get_page_image`                                    | Seitenbild für visuelle Prüfungen                                                                       |
| `update_document_fields`                            | Feldwerte korrigieren oder setzen                                                                       |
| `validate_document`                                 | Feldvalidierungsregeln ausführen                                                                        |
| `approve_document`                                  | Ein validiertes Dokument genehmigen                                                                     |
| `validate_and_export`                               | Validieren und anschließend ins ERP exportieren                                                         |
| `get_export_preview`                                | Vorschau der Export-Payload vor dem Senden                                                              |

### Tabellenextraktion

Alles, was der Validierungsbildschirm und die Einstellungen der Tabellenspalten mit Positionstabellen tun können. Konfigurations-Tools ändern die Dokumenttypen der Organisation; Extraktions- und Korrektur-Tools arbeiten an einem Dokument; Regel-Tools speichern, was DocBits für einen Lieferanten gelernt hat.

| Tool                                                          | Beschreibung                                                                                                                            |
| ------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| `list_tables` / `get_table_config`                            | Tabellen und Spalten eines Dokumenttyps mit den Kennzeichen Required / Read Only / Hidden / Use AI                                      |
| `create_table`                                                | Einem Dokumenttyp eine zweite Positionstabelle hinzufügen                                                                               |
| `add_table_column` / `delete_table_column`                    | Eine Tabellenspalte hinzufügen oder per Soft-Delete entfernen                                                                           |
| `set_ai_table_config`                                         | KI-Tabellenextraktion, Vision und strukturierten Modus für die Organisation umschalten                                                  |
| `extract_table_ai`                                            | Die KI-Tabellenextraktion auf einem Dokument ausführen (Text oder Vision)                                                               |
| `extract_table_only`                                          | Die Tabelle extrahieren, ohne die Kopffelder anzutasten (Regeln oder KI)                                                                |
| `extract_table_nonai`                                         | Regelbasierte Extraktion anhand übergebener Koordinaten, der erste Schritt eines Tabellentrainings über die API                         |
| `apply_ai_table_formatting` / `apply_table_feedback`          | Eine KI-Tabelle neu formatieren: Spalten ausblenden, neu zuordnen, Benutzerfeedback anwenden                                            |
| `remap_table_columns`                                         | Ändern, welche extrahierte Spalte welche konfigurierte Spalte befüllt                                                                   |
| `save_table_rules` / `save_table_training_rules`              | Die Koordinatenregeln oder die KI-Formatierungsregeln für den Lieferanten speichern, damit das nächste Dokument genauso extrahiert wird |
| `delete_table_training_rules`                                 | Die gespeicherten Regeln eines Lieferanten entfernen; das nächste Dokument fällt auf die KI zurück                                      |
| `get_table_extraction_report` / `list_table_report_suppliers` | Bericht pro Lieferant, wie Tabellen extrahiert werden (Regeln, KI, Modell), mit Vorschau                                                |
| `compare_table_extraction_models`                             | Dasselbe Dokument mit zwei KI-Stufen extrahieren und die Tabellen vergleichen                                                           |

### Suche & Dashboard

| Tool                                              | Beschreibung                                                                                               |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `search_documents` / `search_documents_by_name`   | Volltext- und Dateinamensuche                                                                              |
| `query_document_dashboard`                        | Dashboard-Abfrage in natürlicher Sprache                                                                   |
| `explain_document_dashboard_query`                | Anzeigen, wie eine Abfrage interpretiert wurde                                                             |
| `get_search_capabilities`                         | Welche Suchfunktionen die Organisation aktiviert hat                                                       |
| `compare_search_modes`                            | Schlüsselwort- und Vektorergebnisse vergleichen                                                            |
| `diagnose_document_search`                        | Warum ein Dokument bei einer bestimmten Suche erscheint oder nicht, klassisch und Volltext nebeneinander   |
| `inspect_document_search_index`                   | Ob ein Dokument in den Dokument-, Text- und Vektorindizes vorhanden ist und wann jeweils geschrieben wurde |
| `get_dashboard_columns` / `set_dashboard_columns` | Die im Dokumenten-Dashboard angezeigten Spalten lesen oder ändern                                          |

### Touchless Intelligence

Warum Dokumente menschliches Eingreifen benötigen und was zu ändern ist, damit es weniger werden. Jedes Tool hier ist schreibgeschützt, außer `touchless_apply_change`, das genau eine zuvor in der Vorschau geprüfte Einstellungsänderung schreibt.

| Tool                                                             | Beschreibung                                                                                                      |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| `touchless_get_summary`                                          | Touchless-Scorecard der Organisation: wie viele Dokumente unberührt durchgelaufen sind, nach Zeitraum und Segment |
| `touchless_list_segments`                                        | Werte, nach denen Sie die Zahlen segmentieren können (Lieferant, Dokumenttyp, …)                                  |
| `touchless_rank_supplier_opportunities`                          | Lieferanten, geordnet danach, wie viel manuelle Arbeit sie verursachen                                            |
| `touchless_diagnose_supplier`                                    | Warum die Dokumente eines Lieferanten für einen Menschen anhalten                                                 |
| `touchless_get_issue_cluster`                                    | Ein wiederkehrendes Problem und die davon betroffenen Dokumente                                                   |
| `touchless_get_document_trace`                                   | Vollständiger Touchless-Verlauf eines Dokuments                                                                   |
| `touchless_explain_pipeline`                                     | Wo in der Pipeline ein Dokument oder ein Cluster angehalten hat                                                   |
| `touchless_explain_po_match` / `touchless_get_po_match_evidence` | Warum das PO-Matching erfolgreich war oder fehlschlug, mit Regelsatz und Toleranzrechnung                         |
| `touchless_get_recommendations`                                  | Was zu ändern ist, nicht nur, was schiefgelaufen ist                                                              |
| `touchless_list_change_proposals`                                | Einstellungsänderungen, die die Touchless-Rate erhöhen würden, mit dem erwarteten Zuwachs                         |
| `touchless_preview_change`                                       | Einen Vorschlag im Trockenlauf prüfen: Es wird nichts geschrieben                                                 |
| `touchless_apply_change`                                         | Einen zuvor in der Vorschau geprüften Vorschlag auf die Organisation anwenden                                     |
| `touchless_verify_change`                                        | Was eine angewendete Änderung tatsächlich gebracht hat                                                            |

### Analysen & BI

| Tool                       | Beschreibung                        |
| -------------------------- | ----------------------------------- |
| `get_executive_summary`    | Übergeordnete KPIs der Organisation |
| `get_success_rates`        | Touchless- / Straight-Through-Raten |
| `get_volume_trends`        | Dokumentvolumen im Zeitverlauf      |
| `get_top_document_types`   | Häufigste Dokumenttypen             |
| `get_pending_tasks_detail` | Details zu offenen Aufgaben         |

### Elektronische Dokumente (E-Rechnungen)

| Tool                                                           | Beschreibung                                                           |
| -------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `list_electronic_document_types`                               | Unterstützte E-Rechnungsformate (ZUGFeRD, XRechnung, Factur-X, UBL, …) |
| `test_electronic_document`                                     | Ein Beispiel-E-Dokument klassifizieren und extrahieren                 |
| `verify_electronic_documents` / `validate_all_edocs`           | Die Extraktion von E-Dokumenten verifizieren                           |
| `list_edoc_custom_attributes` / `create_edoc_custom_attribute` | Benutzerdefinierte Extraktionsattribute verwalten                      |

### Stammdaten

| Tool                                                      | Beschreibung                                                                                   |
| --------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `upsert_vendor_master_data`                               | Lieferantenstammdaten anlegen oder aktualisieren                                               |
| `trigger_supplier_lookup`                                 | Ein Dokument mit Lieferantenstammdaten anreichern                                              |
| `import_supplier_invoice_bod`                             | Ein Lieferantenrechnungs-BOD importieren                                                       |
| `get_supplier_invoice`                                    | Die gespeicherten Lieferantenrechnungsdaten (BOD) nach Rechnung, Lieferant oder Dokument lesen |
| `upsert_payment_term_mapping` / `upsert_discount_mapping` | Berechnungszuordnungen pflegen                                                                 |

### Konfiguration, Administration & Health

| Tool                                                    | Beschreibung                                           |
| ------------------------------------------------------- | ------------------------------------------------------ |
| `get_preferences` / `get_preference` / `set_preference` | Organisationseinstellungen lesen und ändern            |
| `list_document_types` / `get_field_settings`            | Die Einrichtung von Dokumenttypen und Feldern einsehen |
| `list_users`                                            | Benutzer der Organisation auflisten                    |
| `clear_org_cache`                                       | Zwischengespeicherte Konfiguration leeren              |
| `check_api_health` / `check_celery_health`              | Service-Health                                         |
| `get_current_user` / `get_api_info`                     | Identität und API-Metadaten                            |

## Nächste Schritte

* [**Einrichtung & Konfiguration**](setup-and-configuration.md) — Claude Code, Gemini CLI oder Codex verbinden (mit Anmeldung oder API-Schlüssel)
* [**Beispiele**](examples.md) — reale Aufgaben, die Kunden ihrem Assistenten stellen
* [**Elektronische Dokumente (eDocs)**](edocs-mcp/) — Vertiefung zu den eDoc-Tools: Verarbeitung von E-Rechnungen einsehen/testen und benutzerdefinierte Extraktions-/Vorschauregeln verwalten (gleicher Endpunkt, gleiche Anmeldung)
* [**Workflows & Karten (DocFlow)**](docflow-mcp/) — erweiterte Workflows und Partner-Karten verwalten

{% hint style="info" %}
**Ein MCP für alles.** Die eDoc-Tools und die Tools für **Workflows & Karten (DocFlow)** laufen auf **demselben** Endpunkt `api.docbits.com/v3/mcp` mit derselben DocBits-Anmeldung. DocFlow-Tools erscheinen dort mit dem Präfix `docflow_` (zum Beispiel `docflow_list_workflows`); die DocFlow-Seite dokumentiert sie unter ihren einfachen Namen. Die direkte Verbindung zum DocFlow-Host ist weiterhin möglich, aber nicht mehr nötig.
{% endhint %}
