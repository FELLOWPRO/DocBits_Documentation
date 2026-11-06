# Para desenvolvedores

Esta página é para desenvolvedores e responsáveis por CI que escrevem modelos como JSON ou iniciam testes a partir de código.

## O modelo JSON em resumo

Um modelo é um documento JSON (schema versão 1; os schemas 1.1 a 1.3 acrescentam outras etapas e configurações). Exporte qualquer modelo com o ícone de download para ver um exemplo completo.

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

* `id` e `version` identificam um modelo; uma versão salva nunca muda, salve as alterações com uma nova `version`.
* `params` declara os valores que uma entrada fornece; as etapas se referem a eles como `{{params.<name>}}`. A partir do schema 1.3, uma etapa pode memorizar um valor (`captureValue`, `as`) e as etapas seguintes o usam como `{{vars.<name>}}`.
* `section` (`prepare`, `check`, `cleanup`) classifica uma etapa em uma fase. A partir do schema 1.3, as etapas `cleanup` devem ser as últimas etapas e são executadas mesmo depois de uma falha. `reload` (schema 1.3) recarrega a página e a execução continua depois.
* `allowWrites: true` é obrigatório para modelos que carregam, exportam, excluem ou aprovam.
* As etapas endereçam elementos por IDs de teste estáveis (`target`), nunca pelo texto visível, de modo que um modelo funciona em todos os idiomas da interface.
* Valide antes de salvar: **Importar JSON → Validar**, ou `POST /live-tests/validate`.

## Iniciar uma entrada via REST ou Playwright

Pré-requisitos: um token de administrador da organização, o ID da organização, o ID da entrada e o `session_id` de uma aba do navegador
com **Permitir inícios a partir de fora** ativado.

```http
POST https://eu.api.docbits.com/testing/start
Authorization: Bearer <token>
X-ORG-ID: <organisation id>
Content-Type: application/json

{ "input_id": "<input id>", "session_id": "<session id>", "source": "playwright" }
```

A resposta é `202` com `log_id`, `run_id` e `status`. Consulte `GET /testing/logs/<log_id>` repetidamente até o resultado ser final.
Adicione `"confirm_writes": true` somente para um modelo que grava dados, e somente quando isso for intencional.

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

Use o host de API da sua região (veja [DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp) para a lista de hosts).
CSV dos registros: `GET /testing/logs/export.csv` (mesmos filtros da lista) e `GET /testing/logs/<log_id>/export.csv`.

## Iniciar abrindo um link de início

Se a sua automação controla um navegador no qual você já fez login, abra o link de início do modelo em vez de chamar a API:

`https://<your-environment>/settings/testing?run=<template>&version=<version>&input=<input>&autostart=1`

`run` é a chave do modelo (obrigatória), `version` fixa uma versão salva (padrão: a mais recente), `input` identifica uma entrada salva
pelo nome ou ID, e `autostart=1` inicia um modelo que apenas lê dados sem necessidade de clique. Um modelo que
grava dados continua exigindo confirmação, portanto a execução aguarda `testing-start-confirm`. O link só funciona em um
navegador em que um administrador da organização tenha feito login; os cliques acontecem nessa aba.

```ts
// signed in as an organisation admin (your login helper)
await page.goto('https://<your-environment>/settings/testing?run=default-smoke-analytics&version=1.0.0');
const start = page.getByTestId('testing-start-confirm');
const status = page.getByTestId('testing-run-status');
await start.or(status).first().waitFor();
if (await start.isVisible()) await start.click();
await expect(status).toHaveAttribute('data-status', /(passed|failed|blocked|cancelled)$/);
```

`data-status` é `running`, `passed`, `failed`, `blocked` ou `cancelled`. `blocked` significa que uma regra interrompeu a execução
antes da execução das etapas. Os parâmetros são removidos da URL depois de lidos, portanto recarregar a página não
inicia o teste novamente. Copie o link na caixa de diálogo de início, em **Comece de fora → Link de início**.

## Iniciar via MCP

O servidor MCP do DocBits oferece as ferramentas de Testing `testing_list_templates`, `testing_list_inputs`, `testing_start`,
`testing_get_log` e `testing_list_logs`, e `list_test_sessions` para as abas registradas. `testing_start` precisa de um
`session_id` explícito; `confirm_writes` só é definido depois de o usuário concordar. Os valores sensíveis são passados
somente para a execução e nunca são armazenados.

## Limites do executor no navegador

* Os testes são executados como a pessoa que registrou a aba: sem login, sem troca de perfil.
* Um recarregamento completo da página encerra a execução, exceto a própria etapa `reload` do modelo (schema 1.3).
* As caixas de diálogo nativas do navegador (seletor de arquivos, impressão, alertas) não podem ser conduzidas; os uploads de arquivos usam arquivos de teste da organização ou do servidor.
* As etapas de captura de tela são ignoradas (a execução passa a ser **Bloqueado**).
Para qualquer coisa além disso, use o Playwright diretamente.
