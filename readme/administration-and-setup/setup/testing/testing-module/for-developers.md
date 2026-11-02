# Dla programistów

Ta strona jest przeznaczona dla programistów i właścicieli CI, którzy piszą szablony w JSON lub uruchamiają testy z kodu.

## Szablon JSON w skrócie

Szablon to dokument JSON (wersja schematu 1; schematy od 1.1 do 1.3 dodają kolejne kroki i ustawienia). Wyeksportuj dowolny szablon ikoną pobierania, aby zobaczyć kompletny przykład.

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

* `id` i `version` identyfikują szablon; zapisana wersja nigdy się nie zmienia, zmiany zapisuj pod nową `version`.
* `params` deklaruje wartości, które dostarczają dane wejściowe; kroki odwołują się do nich jako `{{params.<name>}}`. Od schematu 1.3 krok może zapamiętać wartość (`captureValue`, `as`), a kolejne kroki używają jej jako `{{vars.<name>}}`.
* `section` (`prepare`, `check`, `cleanup`) przypisuje krok do fazy. Od schematu 1.3 kroki `cleanup` muszą być ostatnimi krokami i są wykonywane nawet po niepowodzeniu. `reload` (schemat 1.3) ładuje stronę ponownie, a przebieg jest potem kontynuowany.
* `allowWrites: true` jest wymagane dla szablonów, które przesyłają, eksportują, usuwają lub zatwierdzają.
* Kroki adresują elementy za pomocą stabilnych identyfikatorów testowych (`target`), nigdy według widocznego tekstu, dzięki czemu szablon działa w każdym języku interfejsu.
* Sprawdź przed zapisaniem: **Importuj JSON → Sprawdź** lub `POST /live-tests/validate`.

## Uruchamianie danych wejściowych przez REST lub Playwright

Wymagania wstępne: token administratora organizacji, identyfikator organizacji, identyfikator danych wejściowych oraz `session_id` karty przeglądarki
z włączoną opcją **Zezwól na uruchamianie z zewnątrz**.

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

Odpowiedź to `202` z `log_id`, `run_id` i `status`. Odpytuj `GET /testing/logs/<log_id>`, aż wynik będzie ostateczny.
Dodaj `"confirm_writes": true` tylko dla szablonu, który zapisuje dane, i tylko wtedy, gdy jest to zamierzone.

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

Użyj hosta API swojego regionu (listę hostów znajdziesz w [DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)).
CSV dzienników: `GET /testing/logs/export.csv` (te same filtry co na liście) oraz `GET /testing/logs/<log_id>/export.csv`.

## Uruchamianie przez MCP

Serwer MCP DocBits udostępnia narzędzia Testing `testing_list_templates`, `testing_list_inputs`, `testing_start`,
`testing_get_log` i `testing_list_logs` oraz `list_test_sessions` dla zarejestrowanych kart. `testing_start` wymaga
jawnego `session_id`; `confirm_writes` jest ustawiane dopiero po wyrażeniu zgody przez użytkownika. Wartości wrażliwe są przekazywane
tylko na czas przebiegu i nigdy nie są zapisywane.

## Ograniczenia programu uruchamiającego w przeglądarce

* Testy działają jako osoba, która zarejestrowała kartę: bez logowania, bez zmiany roli.
* Pełne przeładowanie strony kończy przebieg, z wyjątkiem własnego kroku `reload` szablonu (schemat 1.3).
* Natywnych okien dialogowych przeglądarki (wybór pliku, drukowanie, alerty) nie można obsłużyć; przesyłanie plików korzysta z plików testowych organizacji lub serwera.
* Kroki ze zrzutem ekranu są pomijane (przebieg staje się **Zablokowany**).
Do wszystkiego, co wykracza poza te ograniczenia, użyj bezpośrednio Playwright.
