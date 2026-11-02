# Voor ontwikkelaars

Deze pagina is bedoeld voor ontwikkelaars en CI-eigenaren die sjablonen als JSON schrijven of tests vanuit code starten.

## Sjabloon-JSON in het kort

Een sjabloon is een JSON-document (schemaversie 1; schema 1.1 tot 1.3 voegen extra stappen en instellingen toe). Exporteer een willekeurig sjabloon met het downloadpictogram om een volledig voorbeeld te zien.

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

* `id` en `version` identificeren een sjabloon; een opgeslagen versie verandert nooit, sla wijzigingen op onder een nieuwe `version`.
* `params` declareert de waarden die een invoer levert; stappen verwijzen ernaar als `{{params.<name>}}`. Vanaf schema 1.3 kan een stap een waarde onthouden (`captureValue`, `as`) en latere stappen gebruiken die als `{{vars.<name>}}`.
* `section` (`prepare`, `check`, `cleanup`) deelt een stap in een fase in. Vanaf schema 1.3 moeten `cleanup`-stappen de laatste stappen zijn en worden ze ook na een mislukking uitgevoerd. `reload` (schema 1.3) laadt de pagina opnieuw en de run gaat daarna verder.
* `allowWrites: true` is vereist voor sjablonen die uploaden, exporteren, verwijderen of goedkeuren.
* Stappen adresseren elementen via stabiele test-ID's (`target`), nooit via zichtbare tekst, zodat een sjabloon in elke UI-taal werkt.
* Valideer voordat u opslaat: **JSON importeren → Valideren**, of `POST /live-tests/validate`.

## Een invoer starten via REST of Playwright

Vereisten: een token van een organisatiebeheerder, de organisatie-ID, de invoer-ID en de `session_id` van een browsertabblad
waarop **Starten op afstand toestaan** is ingeschakeld.

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

Het antwoord is `202` met `log_id`, `run_id` en `status`. Vraag `GET /testing/logs/<log_id>` herhaaldelijk op totdat het resultaat definitief is.
Voeg `"confirm_writes": true` alleen toe voor een sjabloon dat gegevens schrijft, en alleen als dat de bedoeling is.

```ts
// Playwright test (API request context)
const res = await request.post(`${API}/testing/start`, {
  headers: { Authorization: `Bearer ${token}`, 'X-ORG-ID': orgId },
  data: { input_id: inputId, session_id: sessionId, source: 'playwright' },
});
expect(res.status()).toBe(202);
const { log_id } = await res.json();
// poll `${API}/testing/logs/${log_id}` until the result is PASS, FAIL or BLOCKED
```

Gebruik de API-host van uw regio (zie [DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp) voor de lijst met hosts).
CSV van de logboeken: `GET /testing/logs/export.csv` (dezelfde filters als de lijst) en `GET /testing/logs/<log_id>/export.csv`.

## Starten via MCP

De DocBits MCP-server biedt de Testing-tools `testing_list_templates`, `testing_list_inputs`, `testing_start`,
`testing_get_log` en `testing_list_logs`, en `list_test_sessions` voor de geregistreerde tabbladen. `testing_start` vereist een
expliciete `session_id`; `confirm_writes` wordt pas ingesteld nadat de gebruiker akkoord is gegaan. Gevoelige waarden worden alleen
voor de run doorgegeven en nooit opgeslagen.

## Beperkingen van de runner in de browser

* Tests worden uitgevoerd als de persoon die het tabblad heeft geregistreerd: geen aanmelding, geen rolwissel.
* Een volledige paginaherlading beëindigt de run, behalve de eigen `reload`-stap van het sjabloon (schema 1.3).
* Native browserdialogen (bestandskiezer, afdrukken, meldingen) kunnen niet worden bediend; bestandsuploads gebruiken organisatiebestanden of servertestbestanden.
* Screenshotstappen worden overgeslagen (de run wordt **Geblokkeerd**).
Gebruik voor alles wat daarbuiten valt Playwright rechtstreeks.
