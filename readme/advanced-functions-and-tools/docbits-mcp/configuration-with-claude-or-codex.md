# DocBits mit Claude oder Codex konfigurieren

Beschreiben Sie das gewünschte Ergebnis, lassen Sie den Assistenten die aktuelle Konfiguration lesen, prüfen Sie seinen Vorschlag und übernehmen Sie dann die vereinbarte Änderung. DocBits MCP stellt dafür Werkzeuge in Claude und Codex bereit. Es gelten die Berechtigungen des verbundenen DocBits-Kontos; Konfigurationsänderungen erfordern die passenden Administratorrechte.

Diese Anleitung beschreibt das Vorgehen. Sie meldet keinen bereits ausgeführten Kundenfix oder erfolgreichen Exporttest.

## 1. Mit der richtigen Organisation verbinden

Wählen Sie Region und Umgebung anhand der [Endpunktübersicht und Anmeldeanleitung](setup-and-configuration.md). Die Befehle verwenden die **EU-Sandbox**. Ersetzen Sie die URL, falls Ihre Testorganisation einen anderen Endpunkt nutzt. Führen Sie die Befehle auf dem Rechner aus, auf dem der Assistent läuft, und bestätigen Sie die DocBits-Anmeldung im Browser.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.sandbox.api.docbits.com/v3/mcp
claude mcp login docbits
```
{% endtab %}
{% tab title="Codex CLI" %}
```bash
codex mcp add docbits --url https://eu.sandbox.api.docbits.com/v3/mcp
codex mcp login docbits
```
{% endtab %}
{% endtabs %}

Nutzen Sie in der Codex-App die MCP-Einstellungen oder die auf demselben Rechner mit der CLI geteilte Konfiguration. Verwenden Sie in Claude Desktop einen benutzerdefinierten Remote-Connector, sofern Ihr Tarif ihn unterstützt, mit demselben HTTP-Endpunkt. Beginnen Sie bei fehlenden Werkzeugen einen neuen Chat. Aktuelle Client-Anleitungen: [Codex MCP](https://developers.openai.com/codex/mcp) und [Claude MCP](https://code.claude.com/docs/en/mcp).

Beginnen Sie mit diesem Prompt:

```text
Nur lesen. Prüfe die verbundene DocBits-Umgebung und Organisation mit
get_api_info und get_current_user. Liste die verfügbaren Konfigurationswerkzeuge.
Zeige Organisations-ID und API-Host, aber keine Tokens oder Schlüsselausschnitte.
Ändere keine Einstellungen und verarbeite keine Dokumente.
```

Ist die Organisation noch nicht aufgelöst, lesen Sie die relevante Konfiguration und prüfen Sie die `org_id` in der Antwort. Stoppen Sie bei einer falschen Organisation. Werkzeugnamen können einen Client-/Server-Präfix haben. Verwenden Sie die tatsächlich angebotenen Werkzeuge und Parameterschemas Ihrer Verbindung.

## 2. Eine einfache Einstellung ändern

Fragen Sie beispielsweise:

```text
Finde mit find_setting die Einstellung für die QR-Code-Extraktion dieser
Testorganisation. Zeige den genauen setting_key und aktuellen Wert. Frage
bei mehreren Treffern nach, welchen ich meine. Wenn apply_setting die
Einstellung unterstützt, erstelle eine Vorschau für das Einschalten.
Zeige current_value und proposed_value und warte auf meine Bestätigung,
bevor du confirm_setting_change aufrufst.
```

`apply_setting` erstellt nur eine Vorschau. Erst nach Ihrer Bestätigung dieses konkreten Vorschlags speichert `confirm_setting_change(preview_id)` die Änderung. Lesen Sie den Wert anschließend erneut. Bewahren Sie die zurückgegebene `undo_id` auf: `undo_setting_change` kann die Änderung innerhalb der angegebenen Frist zurücknehmen. Vorschauen laufen normalerweise nach 5 Minuten ab, die Rücknahme nach 15 Minuten. Hat sich der Wert inzwischen geändert oder ist die Vorschau abgelaufen, erstellen und prüfen Sie eine neue Vorschau.

Für unterstützte strukturierte Änderungen lautet die Folge `preview_settings_action` → `confirm_settings_action` → `undo_settings_action`. Lesen Sie zuerst die angebotenen Aktionstypen. Gibt es keine passende Schreibaktion, lassen Sie sich den `app_path` zeigen und ändern Sie die Einstellung in DocBits. Ersetzen Sie den Ablauf nicht durch einen erfundenen Preference-Key oder einen pauschalen `set_preference`-Aufruf.

## 3. Als Invoice gespeicherte Gutschrift untersuchen

Eine Custom-Transformation kann fest `<INVOICE_TYPE>Invoice</INVOICE_TYPE>` ausgeben, obwohl im ursprünglichen XML ein Gutschriftcode steht. Dies ist das Konfigurationsszenario der [Gutschrift-Anleitung mit Video aus der echten DocBits-Oberfläche](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md).

```text
Nur lesen. Ermittle für das bereitgestellte Original-XML und die Dokument-ID
eDoc-Familie, Syntax, Version/Profil und ursprünglichen Typcode. Liste Custom-
und Default-Attribute. Lies effektive und Standard-TRANSFORMATION sowie
EXTRACTION_PATHS mit get_edoc_attribute_source. Notiere attribute_id,
active_version und active_value_id und lies den Versionsverlauf.
Verfolge TypeCode -> transformiertes XML -> invoice_type -> gespeichertes Feld/
Exportvorschau und spätere Skripte. Zeige Belege und offene Fragen.
Nichts aktivieren, löschen, neu starten, freigeben oder exportieren.
```

Verwenden Sie die **genaue erkannte Formatbezeichnung**. Raten Sie keine ZUGFeRD- oder Factur-X-Version. Der technische `doc_type_key` kann weiterhin `INVOICE` lauten; untersucht wird der fachliche Wert `invoice_type`.

| Lesen | MCP-Werkzeug |
| --- | --- |
| Custom- und Default-Attribute | `list_edoc_custom_attributes` |
| Effektive Quelle oder Standard und aktive IDs | `get_edoc_attribute_source` mit `source: "effective"` oder `"default"` |
| Versionsverlauf einschließlich Entwürfen | `list_edoc_attribute_versions`, bei Bedarf mit `include_values: true` |
| Gespeicherte Felder, Protokolle, Exportvorschau | `get_extracted_fields`, `get_document_logs`, `get_export_preview` |

Bei historischen Dokumenten belegt die heute aktive Version nicht, welche Version damals lief. Halten Sie die Unsicherheit fest, falls die Protokolle keinen Nachweis liefern. Eine PDF-Vorschau belegt weder den gespeicherten Typ noch die exportierten Beträge.

<figure><img src="../../.gitbook/assets/edocs-transformation-de.png" alt="Schreibgeschütztes Entwicklungsbeispiel: der Quelltext- und Versionseditor von DocBits. Lesen Sie Ihre eigene effektive Quelle und den aktiven Wert per MCP; das Bild zeigt keine gespeicherte Änderung."><figcaption><p>Schreibgeschütztes Entwicklungsbeispiel: der Quelltext- und Versionseditor von DocBits. Lesen Sie Ihre eigene effektive Quelle und den aktiven Wert per MCP; das Bild zeigt keine gespeicherte Änderung.</p></figcaption></figure>

## 4. Die kleinste Korrektur vorab prüfen

```text
Schlage die kleinste Änderung unserer vorhandenen Custom-Transformation vor,
damit Code 381 zu Credit Note wird. Erhalte alle anderen Zuordnungen und
bisher unterstützten Gutschriftcodes. Ordne 383 und 384 nicht Credit Note zu.
Zeige den Diff. Prüfe den Vorschlag an unseren Testdokumenten ohne Speichern
und zeige INVOICE_TYPE im transformierten XML sowie die relevanten Beträge.
Nenne ausdrücklich, welche Prüfungen noch fehlen.
```

Für ein **bereits vorhandenes organisationsspezifisches Attribut** rufen Sie `preview_edoc_custom_xslt` mit dem vollständigen Änderungsvorschlag auf:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Ersetzen Sie alle Platzhalter durch Werte aus Ihren Antworten. XSLT-/JSON-Werte enthalten den vollständigen Quelltext mit korrekter JSON-Escapierung. Das Werkzeug verwendet ein vorhandenes Dokument derselben Organisation. Bei `TRANSFORMATION` liefert es transformiertes **XML**, bei `EXTRACTION_PATHS` Felder/Tabellen, bei `PREVIEW` ein **PDF**. Es speichert den Vorschlag nicht. Für den Vergleich mit der Standard-Transformation prüfen Sie deren Quelltext als weiteren Kandidaten mit derselben Custom-Attribut-ID und demselben Dokument.

`compare_edoc_extraction` vergleicht **EXTRACTION_PATHS** und benötigt ein angepasstes Extraction-Paths-Attribut. Es vergleicht keine zwei Transformationen. Legen Sie nicht nur für dieses Werkzeug eine unnötige Anpassung an.

Falls kein Custom-Attribut existiert, stoppen Sie vor der Anlage in Produktion: `create_edoc_custom_attribute` erstellt eine **sofort aktive** erste Version und hat keinen Schalter für eine reine Entwurfsanlage. Bereiten Sie eine neue Anpassung in einer Testorganisation vor oder verwenden Sie den unterstützten Vorschau-/Anlageablauf des DocBits-Editors. Versuchen Sie nicht, gemeinsame Standardregeln global zu ändern.

## 5. Entwurf speichern und bewusst aktivieren

Lesen Sie nach der Prüfung von Diff und Vorschau die aktive Quelle erneut. Hat sie sich inzwischen geändert, vergleichen Sie vor dem nächsten Schritt erneut. Speichern Sie ein vorhandenes Custom-Attribut mit `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Übergeben Sie für diesen Entwurf immer `activate: false`; der Standardwert des Werkzeugs ist `true`. Notieren Sie die zurückgegebene Versionswert-ID und prüfen Sie mit `list_edoc_attribute_versions`, dass die bisherige Version aktiv bleibt. Der gespeicherte Entwurf wirkt noch nicht auf die normale Verarbeitung.

Lassen Sie nach den Tests die konkrete Organisation, das Attribut, den Diff und die Version vom Administrator bestätigen. Aktivieren Sie dann mit `activate_edoc_attribute_version`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

`draft_id` ist die **Wert-ID der Version**, nicht die Versionsnummer oder Attribut-ID. Lesen Sie effektive Quelle und Versionsverlauf erneut und prüfen Sie, dass genau dieser Wert aktiv ist. eDocs nutzt diese Werkzeuge direkt, nicht den allgemeinen Einstellungsablauf mit `preview_id`. Lesen Sie IDs aus der Zielumgebung; Sandbox-IDs lassen sich nicht für Produktion übernehmen.

## 6. Klassifizierung, Beträge und Export prüfen

`test_electronic_document` prüft die **aktuell aktive** Konfiguration ohne Speicherung eines Dokuments. Es hat keinen Parameter zur Auswahl eines Kandidaten oder Entwurfs. Über Remote-HTTP-MCP senden Sie das Original-XML als `file_content_base64` mit `file_name`; der entfernte Server kann keinen lokalen `file_path` Ihres Rechners lesen. Für den vollständigen Test des Kandidaten aktivieren Sie ihn zuerst ausdrücklich in der Testorganisation. Die XSLT-Vorschau allein prüft keine späteren Skripte und keinen Export.

| Ursprünglicher Code | Erwartete Prüfung |
| --- | --- |
| 380 | Invoice bleibt Invoice |
| 381 | Gutschrift wird Credit Note |
| 261 | Gutschriftverhalten erhalten, soweit Format/Mapping es unterstützen |
| 383 | Lastschrift wird nicht allein wegen einer Rechnungsanpassung zu Credit Note |
| 384 | Korrigierte Rechnung wird nicht allein wegen einer Korrektur zu Credit Note |

Prüfen Sie auch angepasste Felder, Positionen, Summen und die Einstellung für negative Gutschriftbeträge. Verarbeiten Sie ein **neues Testdokument** in einer isolierten Testorganisation mit kontrollierten automatischen Exporten. Vergleichen Sie gespeichertes `invoice_type`, Dashboard und `get_export_preview`. Ein tatsächlicher Export ins Zielsystem erfordert einen separat vereinbarten Test. Weder Dry-run noch Exportvorschau belegen eine erfolgreiche ERP-Übertragung.

`validate_all_edocs` prüft die verfügbaren Server-Testdateien per Dry-run; `verify_electronic_documents` **lädt Testdateien hoch und verarbeitet sie**. Beides ersetzt weder Ihre repräsentativen Dokumente noch nachgelagerte Prüfungen. Fehlen Testdateien oder Werkzeuge, prüfen Sie bereitgestellte Beispiele.

## 7. Zurückrollen und Altdokumente getrennt behandeln

Rufen Sie für die Rückkehr `activate_edoc_attribute_version` mit der zuvor notierten `active_value_id` als `draft_id` auf und prüfen Sie die effektive Quelle erneut. Löschen Sie nicht die gesamte Custom-Anpassung, um ein Feld zu korrigieren: Dabei gehen andere Zuordnungen verloren und der Standard greift.

Starten Sie historische Dokumente nicht gesammelt neu. Ein Neustart kann extrahierte Daten und Exportprotokolle löschen sowie Freigaben oder Exporte wiederholen. Prüfen Sie je Dokument Exportstatus, Freigaben und manuelle Änderungen, bevor Sie über seine Korrektur entscheiden.

Beginnen Sie andere Konfigurationsfragen mit `find_setting` oder `run_config_checks` und lassen Sie sich die unterstützte Aktion oder den UI-Pfad zeigen. Bewahren Sie Vorher-/Nachher-Vorschlag, Testergebnisse, aktive Wert-IDs und die Rückrollreferenz bei Ihrer Änderungsdokumentation auf.
