# Para desarrolladores

Esta página está dirigida a desarrolladores y responsables de CI que escriben plantillas como JSON o inician pruebas desde código.

## La plantilla JSON de un vistazo

Una plantilla es un documento JSON (schema versión 1; schema 1.1 a 1.3 añaden más pasos y ajustes). Exporte cualquier plantilla con el icono de descarga para ver un ejemplo completo.

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

* `id` y `version` identifican una plantilla; una versión guardada nunca cambia, guarde los cambios con una nueva `version`.
* `params` declara los valores que aporta una entrada; los pasos se refieren a ellos como `{{params.<name>}}`. A partir del schema 1.3, un paso puede memorizar un valor (`captureValue`, `as`) y los pasos posteriores lo utilizan como `{{vars.<name>}}`.
* `section` (`prepare`, `check`, `cleanup`) asigna un paso a una fase. A partir del schema 1.3, los pasos `cleanup` deben ser los últimos y se ejecutan incluso tras un fallo. `reload` (schema 1.3) recarga la página y la ejecución continúa después.
* `allowWrites: true` es obligatorio para las plantillas que suben, exportan, eliminan o aprueban.
* Los pasos direccionan los elementos mediante ID de prueba estables (`target`), nunca mediante el texto visible, de modo que una plantilla funciona en todos los idiomas de la interfaz.
* Valide antes de guardar: **Importar JSON → Validar**, o `POST /live-tests/validate`.

## Iniciar una entrada mediante REST o Playwright

Requisitos previos: un token de administrador de la organización, el ID de la organización, el ID de la entrada y el `session_id` de una pestaña del navegador
con **Permitir inicios desde fuera** activado.

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

La respuesta es `202` con `log_id`, `run_id` y `status`. Consulte `GET /testing/logs/<log_id>` periódicamente hasta que el resultado sea definitivo.
Añada `"confirm_writes": true` solo para una plantilla que escribe datos, y solo cuando sea intencionado.

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

Utilice el host de API de su región (consulte [DocBits MCP](../../../../advanced-functions-and-tools/docbits-mcp/README.md) para ver la lista de hosts).
CSV de los registros: `GET /testing/logs/export.csv` (mismos filtros que la lista) y `GET /testing/logs/<log_id>/export.csv`.

## Iniciar una prueba mediante un enlace de inicio

Si su automatización controla un navegador con la sesión iniciada, abra el enlace de inicio de la plantilla en lugar de llamar a la API:

`https://<your-environment>/settings/testing?run=<template>&version=<version>&input=<input>&autostart=1`

`run` es la clave de la plantilla (obligatoria), `version` fija una versión guardada (de forma predeterminada, la última), `input` indica una
entrada guardada por su nombre o su ID, y `autostart=1` inicia sin ningún clic una plantilla que solo lee datos. Una plantilla que
escribe datos sigue requiriendo confirmación, por lo que la ejecución espera a `testing-start-confirm`. El enlace solo funciona en el navegador
de un administrador de la organización con la sesión iniciada; los clics se producen en esa pestaña.

```ts
// signed in as an organisation admin (your login helper)
await page.goto('https://<your-environment>/settings/testing?run=default-smoke-analytics&version=1.0.0');
const start = page.getByTestId('testing-start-confirm');
const status = page.getByTestId('testing-run-status');
await start.or(status).first().waitFor();
if (await start.isVisible()) await start.click();
await expect(status).toHaveAttribute('data-status', /(passed|failed|blocked|cancelled)$/);
```

`data-status` es `running`, `passed`, `failed`, `blocked` o `cancelled`. `blocked` significa que una regla detuvo la ejecución
antes de que se ejecutaran sus pasos. Los parámetros se eliminan de la URL después de leerse, por lo que recargar la página no
vuelve a iniciar la prueba. Copie el enlace en el cuadro de diálogo de inicio, en **Comience desde afuera → Enlace de inicio**.

## Iniciar mediante MCP

El servidor MCP de DocBits ofrece las herramientas de Testing `testing_list_templates`, `testing_list_inputs`, `testing_start`,
`testing_get_log` y `testing_list_logs`, y `list_test_sessions` para las pestañas registradas. `testing_start` necesita un
`session_id` explícito; `confirm_writes` solo se establece después de que el usuario haya dado su consentimiento. Los valores confidenciales se transmiten únicamente
para la ejecución y nunca se almacenan.

## Límites del ejecutor del navegador

* Las pruebas se ejecutan como la persona que registró la pestaña: sin inicio de sesión ni cambio de rol.
* Una recarga completa de la página finaliza la ejecución, salvo el propio paso `reload` de la plantilla (schema 1.3).
* Los cuadros de diálogo nativos del navegador (selector de archivos, impresión, alertas) no se pueden manejar; las cargas de archivos utilizan archivos de prueba de la organización o del servidor.
* Los pasos de captura de pantalla se omiten (la ejecución pasa a **Bloqueado**).

Para cualquier cosa más allá de esto, utilice Playwright directamente.
