# Quick Connect

Conecte o seu assistente de IA ao DocBits em três etapas: escolha o ambiente, copie um comando e faça login uma vez. Nenhuma API key é necessária.

## 1. Escolha o seu ambiente

Use o endpoint da **região** (EU ou US) e do **ambiente** (Sandbox ou Production) em que a sua organização está.

| Ambiente | Região | Endpoint |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | EU | `https://eu.api.docbits.com/v3/mcp` |
| Production | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
O assistente trabalha com as permissões da conta com a qual você faz login e pode alterar dados. Alterações em **Production** afetam os seus documentos em produção. Teste novos prompts primeiro em Sandbox.
{% endhint %}

## 2. Conecte com um clique ou um comando

Use os botões para adicionar o servidor ao **Cursor** ou ao **VS Code**, ou copie o comando para o seu cliente de terminal. Cada ambiente tem o seu próprio nome de servidor, para que você possa conectar Sandbox e Production lado a lado sem confundi-los.

{% tabs %}
{% tab title="Sandbox EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-sandbox-eu https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-sandbox-eu --url https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-sandbox-eu https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Sandbox US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-sandbox-us https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-sandbox-us --url https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-sandbox-us https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Production EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-prod-eu https://eu.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-prod-eu --url https://eu.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-prod-eu https://eu.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Production US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-prod-us https://us.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-prod-us --url https://us.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-prod-us https://us.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}
{% endtabs %}

Para **Claude Desktop** e **claude.ai**, adicione um conector personalizado: abra as configurações de conectores, escolha **Add custom connector** e cole o endpoint da tabela.

## 3. Faça login uma vez

A primeira conexão abre o login do DocBits no seu navegador. Se você já estiver conectado ao DocBits, vai direto para a tela de consentimento. Aprove-a e você estará conectado.

{% tabs %}
{% tab title="Claude Code" %}
Inicie o Claude Code, execute `/mcp`, selecione o servidor DocBits e escolha **Authenticate**.
{% endtab %}

{% tab title="OpenAI Codex" %}
Substitua `docbits-sandbox-eu` pelo nome de servidor que você adicionou:

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
O Gemini CLI abre o login na primeira vez que usa o servidor. Você pode iniciá-lo novamente pelo menu `/mcp`.
{% endtab %}
{% endtabs %}

Você só faz login uma vez. O cliente renova o acesso automaticamente por 30 dias de uso.

## 4. Verifique a conexão

Inicie uma nova conversa e envie este prompt:

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

O host da API na resposta deve corresponder ao endpoint escolhido, por exemplo `eu.sandbox.api.docbits.com` para Sandbox EU. Se não corresponder, remova o servidor e adicione-o novamente com o endpoint correto.

## Próximas etapas

* [Exemplos](examples.md): prompts prontos para documentos, busca e análises
* [Configurar o DocBits com Claude ou Codex](configuration-with-claude-or-codex.md): altere configurações com segurança com prévia, confirmação e desfazer
* [Instalação e configuração](setup-and-configuration.md): login com API key para automação e como funciona o login via OAuth

## Solução de problemas

| Sintoma | Solução |
| --- | --- |
| A página de login não abre | Execute a etapa de login novamente. Em uma máquina sem navegador, use uma API key conforme descrito em [Instalação e configuração](setup-and-configuration.md). |
| `401` após conectar | O login expirou. Autentique o servidor novamente. |
| O assistente mostra dados da organização errada | Você escolheu a região ou o ambiente errado. Remova o servidor e adicione o endpoint correto. |
| As ferramentas não aparecem | A sua função no DocBits não permite esses recursos. Pergunte ao seu administrador. |
