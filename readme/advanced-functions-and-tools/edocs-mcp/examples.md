# Beispiele

Kopierbare Prompts und den vollständigen Ablauf für Diagnose, Entwurf, Aktivierung und Rückkehr finden Sie unter [DocBits mit Claude oder Codex konfigurieren](../docbits-mcp/configuration-with-claude-or-codex.md). Die Beispiele verwenden die aktuellen Werkzeugparameter. Ersetzen Sie alle Platzhalter durch Werte Ihrer Organisation und übergeben Sie vollständigen, korrekt als JSON-String escapten Quelltext.

## 1. Eine vorhandene Custom-Regel ändern

Lesen Sie die effektive `TRANSFORMATION` mit `get_edoc_attribute_source`. Verwenden Sie die genaue von der Klassifizierung zurückgegebene Formatbezeichnung:

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

Notieren Sie `attribute_id`, `active_value_id`, `active_version` und `value`. Lesen Sie `source: "default"` getrennt zum Vergleich und den Verlauf mit `list_edoc_attribute_versions`. Der folgende Änderungsablauf setzt ein vorhandenes Custom-Attribut der eigenen Organisation voraus.

Prüfen Sie den vollständigen Kandidaten ohne Speichern mit `preview_edoc_custom_xslt`. Verwenden Sie ein bereits vorhandenes Dokument derselben Organisation:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Bei `TRANSFORMATION` erhalten Sie transformiertes XML, bei `PREVIEW` ein PDF, bei `EXTRACTION_PATHS` Felder/Tabellen. Die Vorschau wählt keinen gespeicherten Entwurf aus und testet weder spätere Skripte noch Exporte.

Lesen Sie nach der Prüfung von Diff und Vorschau die aktive Quelle erneut. Speichern Sie mit `update_edoc_custom_attribute` einen Entwurf. Geben Sie ausdrücklich `activate: false` an; der Werkzeugstandard ist `true`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Rufen Sie nach Tests in der Testorganisation und Bestätigung der konkreten Änderung `activate_edoc_attribute_version` auf. `draft_id` ist die Versionswert-ID. Lesen Sie danach die effektive Quelle erneut. Für die Rückkehr verwenden Sie denselben Aufruf mit der zuvor notierten `active_value_id`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. Wenn noch kein Custom-Attribut existiert

`create_edoc_custom_attribute` erstellt eine sofort aktive erste Version, keinen Entwurf. Testen Sie eine neue Anpassung in einer Testorganisation oder nutzen Sie den unterstützten DocBits-Editorablauf. Legen Sie nicht nur für eine Vorschau eine Produktionsanpassung an und löschen Sie dafür auch keine. Erhalten Sie notwendige Custom-Zuordnungen; gemeinsame Standardregeln dürfen nicht global geändert werden.

## 3. Die aktive Konfiguration testen

Rufen Sie `test_electronic_document` mit dem Base64-kodierten Original-XML auf:

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

Dies prüft die aktuell aktiven Regeln ohne Dokumentenspeicherung, keinen inaktiven Entwurf. Remote-HTTP-MCP kann keinen lokalen `file_path` Ihres Rechners lesen. `compare_edoc_extraction` vergleicht nur Extraction Paths und benötigt ein angepasstes Extraction-Paths-Attribut; Transformationen vergleicht es nicht.

`validate_all_edocs` prüft verfügbare Server-Testdateien per Dry-run. `verify_electronic_documents` lädt sie hoch und verarbeitet sie; dabei entstehen Dokumente. Beides belegt keine erfolgreiche ERP-Übertragung. Nutzen Sie repräsentative Beispiele, prüfen Sie gespeicherte Felder/Beträge und Export separat und starten Sie Altdokumente nicht gesammelt neu.
