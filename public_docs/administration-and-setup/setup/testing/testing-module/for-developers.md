# Per sviluppatori

Questa pagina è rivolta a sviluppatori e responsabili CI che scrivono modelli in JSON o avviano test da codice.

## Il JSON del modello in sintesi

Un modello è un documento JSON (schema versione 1; gli schemi da 1.1 a 1.3 aggiungono altri passaggi e impostazioni). Esportare un modello qualsiasi con l'icona di download per vedere un esempio completo.

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

* `id` e `version` identificano un modello; una versione salvata non cambia mai, salvare le modifiche con una nuova `version`.
* `params` dichiara i valori forniti da un input; i passaggi vi fanno riferimento come `{{params.<name>}}`. A partire dallo schema 1.3, un passaggio può memorizzare un valore (`captureValue`, `as`) e i passaggi successivi lo utilizzano come `{{vars.<name>}}`.
* `section` (`prepare`, `check`, `cleanup`) assegna un passaggio a una fase. A partire dallo schema 1.3, i passaggi `cleanup` devono essere gli ultimi e vengono eseguiti anche dopo un errore. `reload` (schema 1.3) ricarica la pagina e l'esecuzione prosegue subito dopo.
* `allowWrites: true` è obbligatorio per i modelli che caricano, esportano, eliminano o approvano.
* I passaggi indirizzano gli elementi tramite ID di test stabili (`target`), mai tramite il testo visibile, così un modello funziona in ogni lingua dell'interfaccia.
* Convalidare prima di salvare: **Importa JSON → Convalida**, oppure `POST /live-tests/validate`.

## Avviare un input tramite REST o Playwright

Prerequisiti: un token di amministratore dell'organizzazione, l'ID dell'organizzazione, l'ID dell'input e il `session_id` di una scheda del browser
con **Consenti avvii dall'esterno** attivato.

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

La risposta è `202` con `log_id`, `run_id` e `status`. Eseguire un polling di `GET /testing/logs/<log_id>` finché il risultato non è definitivo.
Aggiungere `"confirm_writes": true` solo per un modello che scrive dati e solo quando è voluto.

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

Utilizzare l'host API della propria regione (per l'elenco degli host vedere [DocBits MCP](../../../../advanced-functions-and-tools/docbits-mcp/README.md)).
CSV dei log: `GET /testing/logs/export.csv` (stessi filtri dell'elenco) e `GET /testing/logs/<log_id>/export.csv`.

## Avviare aprendo un link di avvio

Se l'automazione controlla un browser autenticato, aprire il link di avvio del modello invece di chiamare l'API:

`https://<your-environment>/settings/testing?run=<template>&version=<version>&input=<input>&autostart=1`

`run` è la chiave del modello (obbligatoria), `version` specifica la versione salvata da utilizzare (predefinita: la
più recente), `input` indica un input salvato tramite nome o ID e `autostart=1` avvia senza clic un modello di sola
lettura. Un modello che scrive dati mantiene la richiesta di conferma, quindi l'esecuzione attende
`testing-start-confirm`. Il link funziona solo nel browser autenticato di un amministratore dell'organizzazione; i
clic avvengono in quella scheda.

```ts
// signed in as an organisation admin (your login helper)
await page.goto('https://<your-environment>/settings/testing?run=default-smoke-analytics&version=1.0.0');
const start = page.getByTestId('testing-start-confirm');
const status = page.getByTestId('testing-run-status');
await start.or(status).first().waitFor();
if (await start.isVisible()) await start.click();
await expect(status).toHaveAttribute('data-status', /(passed|failed|blocked|cancelled)$/);
```

`data-status` può essere `running`, `passed`, `failed`, `blocked` o `cancelled`. `blocked` indica che una regola ha
interrotto l'esecuzione prima che venissero eseguiti i passaggi. Dopo la lettura, i parametri vengono rimossi
dall'URL, quindi ricaricando la pagina il test non viene avviato di nuovo. Copiare il link nella finestra di avvio
sotto **Avvia dall'esterno → Link di avvio**.

## Avviare tramite MCP

Il server DocBits MCP offre gli strumenti Testing `testing_list_templates`, `testing_list_inputs`, `testing_start`,
`testing_get_log` e `testing_list_logs`, e `list_test_sessions` per le schede registrate. `testing_start` richiede un
`session_id` esplicito; `confirm_writes` viene impostato solo dopo il consenso dell'utente. I valori riservati vengono passati solo per
l'esecuzione e non vengono mai memorizzati.

## Limiti dell'esecutore nel browser

* I test vengono eseguiti come la persona che ha registrato la scheda: nessun login, nessun cambio di ruolo.
* Un ricaricamento completo della pagina termina l'esecuzione, tranne il passaggio `reload` del modello stesso (schema 1.3).
* Le finestre di dialogo native del browser (selezione file, stampa, avvisi) non possono essere gestite; i caricamenti di file utilizzano file dell'organizzazione o file di test del server.
* I passaggi di screenshot vengono saltati (l'esecuzione diventa **Bloccato**).

Per tutto ciò che va oltre, utilizzare direttamente Playwright.
