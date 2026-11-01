# Für Entwickler

Diese Seite richtet sich an Entwickler und CI-Verantwortliche, die Templates als JSON schreiben oder Tests aus Code starten.

## Template-JSON im Überblick

Ein Template ist ein JSON-Dokument (Schemaversion 1). Exportieren Sie ein beliebiges Template über das Download-Symbol, um ein
vollständiges Beispiel zu sehen.

```json
{
  "schemaVersion": 1,
  "id": "my-testing-page-check",
  "name": "Testing page check",
  "category": "smoke",
  "version": "1.0.0",
  "timeoutMs": 60000,
  "allowWrites": false,
  "params": {
    "document_id": { "type": "string", "required": true, "description": "Document to open" }
  },
  "steps": [
    { "id": "open", "action": "navigate", "route": "/settings/testing" },
    { "id": "badge", "action": "waitFor", "target": "testing.environment-badge", "state": "visible" }
  ]
}
```

* `id` und `version` bestimmen ein Template; eine gespeicherte Version ändert sich nie, Änderungen erhalten eine neue `version`.
* `params` erklärt die Werte, die eine Eingabe liefert; Schritte verweisen darauf mit `{{params.<name>}}`.
* `allowWrites: true` ist Pflicht für Templates, die hochladen, exportieren, löschen oder freigeben.
* Schritte sprechen Elemente über stabile Test-IDs an (`target`), nie über sichtbaren Text; so läuft ein Template in jeder Oberflächensprache.
* Vor dem Speichern prüfen: **JSON importieren → Prüfen** oder `POST /live-tests/validate`.

## Eine Eingabe per REST oder Playwright starten

Voraussetzungen: ein Token eines Organisations-Admins, die Organisations-ID, die ID der Eingabe und die `session_id` eines
Browser-Tabs mit eingeschaltetem **Start von außen erlauben**.

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

Die Antwort ist `202` mit `log_id`, `run_id` und `status`. Fragen Sie `GET /testing/logs/<log_id>` ab, bis das Ergebnis
feststeht. `"confirm_writes": true` nur bei einem Template setzen, das Daten schreibt, und nur, wenn das gewollt ist.

```ts
// Playwright-Test (API-Request-Kontext)
const res = await request.post(`${API}/testing/start`, {
  headers: { Authorization: `Bearer ${token}`, 'X-ORG-ID': orgId },
  data: { input_id: inputId, session_id: sessionId, source: 'playwright' },
});
expect(res.status()).toBe(202);
const { log_id } = await res.json();
// `${API}/testing/logs/${log_id}` abfragen, bis das Ergebnis PASS, FAIL oder BLOCKED ist
```

Verwenden Sie den API-Host Ihrer Region (Liste auf der Seite *DocBits MCP*). CSV der Protokolle:
`GET /testing/logs/export.csv` (dieselben Filter wie die Liste) und `GET /testing/logs/<log_id>/export.csv`.

## Start per MCP

Der DocBits-MCP-Server bietet für das Testing-Modul die Werkzeuge `testing_list_templates`, `testing_list_inputs`,
`testing_start`, `testing_get_log` und `testing_list_logs` sowie `list_test_sessions` für die registrierten Tabs.
`testing_start` braucht eine ausdrückliche `session_id`; `confirm_writes` wird erst nach Zustimmung der Person gesetzt.
Vertrauliche Werte gelten nur für den Lauf und werden nie gespeichert.

## Grenzen des Browser-Runners

* Tests laufen als die Person, die den Tab registriert hat: keine Anmeldung, kein Rollenwechsel.
* Ein vollständiges Neuladen der Seite beendet den Lauf.
* Native Browserdialoge (Dateiauswahl, Drucken, Hinweisfenster) lassen sich nicht bedienen; Uploads nutzen Dateien der
  Organisation oder Testdateien des Servers.
* Screenshot-Schritte werden übersprungen (der Lauf wird **Blockiert**).

Für alles darüber hinaus verwenden Sie Playwright direkt.
