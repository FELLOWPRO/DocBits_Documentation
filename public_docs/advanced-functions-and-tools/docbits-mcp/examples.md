# Beispiele

Sobald DocBits MCP verbunden ist (siehe [Einrichtung & Konfiguration](setup-and-configuration.md)), sprechen Sie in einfacher Sprache mit Ihrem Assistenten – er wählt die passenden DocBits-Tools für Sie aus. Nachfolgend finden Sie realistische Aufgaben von Kunden, mit der Art von Prompt, die Sie eingeben würden, und den Tools, die der Assistent im Hintergrund verwendet.

{% hint style="info" %}
Diese funktionieren in Claude Code, Gemini CLI und Codex gleichermaßen – die Prompts sind natürliche Sprache, keine Befehle.
{% endhint %}

## Die Arbeitswarteschlange sichten

> *„Wie viele Dokumente warten auf Validierung, und welche Typen sind das?“*

Verwendet `get_pending_documents_count`, `get_pending_tasks_detail`, `get_top_document_types`. Der Assistent fasst den Rückstand zusammen und kann in jedes Dokument hineinschauen.

> *„Zeige mir die Rechnungen, die heute einen Fehler hatten, und sage mir, warum.“*

Verwendet `search_documents` / `query_document_dashboard` + `get_document_logs`, um fehlerhafte Dokumente zu finden und den Fehler anhand der Protokolle zu erklären.

## Ein Dokument finden und prüfen

> *„Öffne die Rechnung INV-2026-00231 und zeige die extrahierten Felder und die Positionen.“*

Verwendet `get_document_by_name`, `get_extracted_fields`, `get_extracted_tables`. Der Assistent liefert die Kopfdaten und die Tabelle und kann mit `get_page_image` das Seitenbild abrufen, wenn Sie die Quelle sehen möchten.

> *„Suche alle Dokumente des Lieferanten ‚ACME GmbH‘ vom letzten Monat über 10.000 €.“*

Verwendet `search_documents` / `query_document_dashboard` mit feldbezogenen Filtern.

## Korrigieren und genehmigen

> *„Setze bei Dokument 84213 die Bestellnummer auf 4500098123 und das Fälligkeitsdatum auf 2026-07-15 und validiere es dann.“*

Verwendet `update_document_fields` und anschließend `validate_document`. Der Assistent meldet etwaige Validierungsfehler, damit Sie sie beheben können.

> *„Validiere und exportiere Dokument 84213 ins ERP, aber zeige mir zuerst die Exportvorschau.“*

Verwendet `get_export_preview` und nach Ihrer Bestätigung `validate_and_export`.

## Eine Tabellenextraktion korrigieren

> *„In der Positionstabelle dieses Lieferscheins fehlen zwei Zeilen. Extrahiere sie erneut mit KI, blende die Spalte *Charges* aus und behalte das für diesen Lieferanten bei.“*

Verwendet `extract_table_ai`, um die KI-Tabelle auf dem Dokument erneut auszuführen, `apply_ai_table_formatting`, um die Spalte auszublenden, und `save_table_training_rules`, um das Ergebnis für den Lieferanten zu speichern; der nächste Lieferschein dieses Lieferanten wird genauso extrahiert. `get_extracted_tables` zeigt die endgültige Tabelle. Nützlich bei Dokumenten, bei denen die regelbasierte Extraktion Zeilen übersehen hat.

## Analysen & Berichte

> *„Gib mir eine Management-Zusammenfassung für diesen Monat: Volumentrend, Touchless-Rate und die Top-5-Dokumenttypen.“*

Verwendet `get_executive_summary`, `get_volume_trends`, `get_success_rates`, `get_top_document_types`. Ideal für ein schnelles Management-Update, ohne das Dashboard zu öffnen.

## E-Rechnung (eDocs)

> *„Welche elektronischen Rechnungsformate sind für uns aktiviert, und wird diese ZUGFeRD-Datei korrekt extrahiert?“*

Verwendet `list_electronic_document_types` + `test_electronic_document`, anschließend `verify_electronic_documents`, um die extrahierten Felder zu bestätigen.

## Stammdaten & Lieferantenanreicherung

> *„Lege einen neuen Lieferanten (Name, USt-ID, IBAN) in den Stammdaten an und führe dann die Lieferantensuche für Dokument 84500 erneut aus.“*

Verwendet `upsert_vendor_master_data` + `trigger_supplier_lookup`.

## Konfigurationsänderungen

> *„Aktiviere die QR-Code-Extraktion für unsere Organisation und bestätige, dass die Einstellung gesetzt ist.“*

Verwendet `set_preference` (das den Cache automatisch leert) + `get_preference` zur Bestätigung.

> *„Liste unsere Dokumenttypen auf und zeige die Feldeinstellungen für ‚Invoice‘.“*

Verwendet `list_document_types` + `get_field_settings`.

## Health & Diagnose

> *„Sind die DocBits-API und der Verarbeitungs-Worker gerade gesund? Als wer bin ich verbunden?“*

Verwendet `check_api_health`, `check_celery_health`, `get_current_user`.

---

## Tipps

- **Seien Sie bei dem Dokument konkret** – eine ID oder ein exakter Dateiname ist am schnellsten; andernfalls sucht der Assistent zuerst.
- **Fordern Sie vor dem Export eine Vorschau an** – mit `get_export_preview` bestätigen Sie die ERP-Payload, bevor `validate_and_export` sie sendet.
- **Berechtigungen gelten** – der Assistent kann nur das tun, was Ihr DocBits-Benutzer oder Ihr API-Schlüssel darf. Genehmigungen und Exporte berücksichtigen Ihre Rolle und ACLs.
- **Vorsicht in Produktion** – der MCP arbeitet auf echten Daten. Bevorzugen Sie in Kunden-/Produktionsumgebungen Lese- und Vorschau-Aktionen und bestätigen Sie, bevor Sie genehmigen, exportieren oder löschen.
