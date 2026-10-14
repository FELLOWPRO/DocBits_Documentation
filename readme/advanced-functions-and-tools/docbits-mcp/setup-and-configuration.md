# Configuração e Instalação

Conectar um assistente de IA ao DocBits MCP exige um único comando e, em seguida, um login feito uma só vez. A forma recomendada de entrar é o **OAuth** — o mesmo login do DocBits que você já usa, no seu navegador. Para automação, você pode se conectar com uma chave de API.

## 1. Escolha o seu endpoint

O servidor MCP fica no host da API do DocBits. Use o host da **sua região (UE ou EUA)**:

| Ambiente | Endpoint UE | Endpoint EUA |
|-------------|-------------|-------------|
| Produção | `https://eu.api.docbits.com/v3/mcp` | `https://us.api.docbits.com/v3/mcp` |
| Sandbox | `https://eu.sandbox.api.docbits.com/v3/mcp` | `https://us.sandbox.api.docbits.com/v3/mcp` |

{% hint style="info" %}
`api.docbits.com` é o endpoint único que os clientes usam. Escolha sempre a **região em que a sua organização está** (UE ou EUA) — o MCP direciona o login automaticamente para o servidor de autenticação correspondente, você não precisa configurá-lo separadamente. Os exemplos abaixo usam o host de produção da UE; substitua pelo seu.
{% endhint %}

## 2. Entre com OAuth (recomendado)

O OAuth é o caminho mais fácil — não há segredos para copiar. Depois que você adiciona o servidor, a **primeira conexão abre o login do DocBits no seu navegador**, você aprova uma tela de consentimento e o cliente fica conectado.

**O que você verá, em qualquer cliente:**

1. O cliente abre a página de login do DocBits no seu navegador.
2. Você entra com a sua conta do DocBits (se você já estiver conectado ao aplicativo web do DocBits, a sessão é reutilizada — sem novo login).
3. Você aprova a tela de consentimento ("Authorize access").
4. O navegador entrega um token ao cliente e a conexão fica ativa.

O OAuth emite um token de acesso de curta duração (8 h) e um token de atualização (30 dias), de modo que o cliente se atualiza automaticamente e permanece conectado — **você só faz login uma vez.**

{% hint style="success" %}
**Você precisa estar conectado ao DocBits — sua sessão existente é reutilizada.** O login do MCP não pede que você entre novamente se o seu navegador já tiver uma sessão do DocBits. Se você já estiver conectado ao aplicativo web do DocBits, vai **direto para a tela de consentimento**. Se não estiver conectado, a página de login do DocBits aparece primeiro; depois de entrar uma vez, a sessão passa automaticamente para o MCP.
{% endhint %}

<figure><img src="../../.gitbook/assets/docbits-mcp-login.png" alt="Página de login do DocBits"><figcaption><p>Ainda não conectado — a página de login do DocBits com a identidade visual da marca (você só a vê se o seu navegador não tiver uma sessão do DocBits)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits-mcp-consent.png" alt="Tela de autorização de acesso / consentimento do DocBits"><figcaption><p>Já conectado — a sessão é reutilizada e você vai direto para a tela de consentimento. Aprove para conectar; o que o cliente solicita (escopo e redirecionamento) é exibido.</p></figcaption></figure>

{% tabs %}
{% tab title="Claude Code" %}
```bash
# 1) add the server
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp

# 2) sign in (opens browser → DocBits login + consent → connected)
claude mcp login docbits
```

`claude mcp login docbits` é a etapa do OAuth. Depois que ela for bem-sucedida, confirme perguntando ao Claude: *"verifique a saúde da API do DocBits"*.
{% endtab %}

{% tab title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp
```

O Gemini CLI descobre o servidor OAuth automaticamente. Na **primeira vez** que usa o servidor, ele abre o login do DocBits no seu navegador (o registro dinâmico do cliente e o gerenciamento de tokens são tratados para você). Aprove o consentimento e você estará conectado. Se necessário, você pode acionar o login novamente pelo menu `/mcp` do Gemini.
{% endtab %}

{% tab title="OpenAI Codex" %}
```bash
codex mcp add docbits \
  --url https://eu.api.docbits.com/v3/mcp \
  --oauth-resource https://eu.api.docbits.com/v3/mcp
```

O parâmetro `--oauth-resource` informa ao Codex que deve executar o login OAuth para este servidor. No primeiro uso, o Codex abre o login do DocBits no seu navegador; aprove o consentimento e você estará conectado.
{% endtab %}
{% endtabs %}

## 3. Conecte com uma chave de API (automação)

Para agentes sem interface, CI ou qualquer ambiente sem navegador, ignore o OAuth e passe a chave de API da sua organização no cabeçalho `X-API-KEY`.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp \
  --header "X-API-KEY: <your-api-key>"
```
{% endtab %}

{% tab title="Gemini CLI" %}
Adicione a `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "docbits": {
      "httpUrl": "https://eu.api.docbits.com/v3/mcp",
      "headers": { "X-API-KEY": "<your-api-key>" }
    }
  }
}
```
{% endtab %}

{% tab title="OpenAI Codex" %}
Adicione a `~/.codex/config.toml`:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
http_headers = { "X-API-KEY" = "<your-api-key>" }
```

Ou mantenha a chave fora do arquivo e leia-a do ambiente:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
env_http_headers = { "X-API-KEY" = "DOCBITS_API_KEY" }
```
{% endtab %}
{% endtabs %}

## Como o login OAuth funciona (nos bastidores)

O DocBits implementa o fluxo padrão **MCP OAuth 2.1**, de modo que qualquer cliente compatível se conecta sem configuração manual:

1. O cliente chama o endpoint MCP e recebe um `401` com um cabeçalho `WWW-Authenticate` que aponta para os metadados do recurso protegido.
2. Ele lê `/.well-known/oauth-protected-resource`, que indica o servidor de autenticação do DocBits.
3. Ele lê os metadados do servidor de autenticação e **se registra** dinamicamente (RFC 7591) — não é necessário um segredo de cliente.
4. Seu navegador abre o login + consentimento do DocBits. Se você já estiver conectado ao aplicativo web, a sessão é reutilizada.
5. O cliente troca o código de autorização (PKCE) por um token de acesso + token de atualização e chama o MCP.

{% hint style="warning" %}
Sair do **aplicativo web** do DocBits **não desconecta o MCP** — o MCP mantém seus próprios tokens e continua funcionando até que o token de atualização expire (30 dias) ou você remova o servidor do seu cliente.
{% endhint %}

## Solução de problemas

| Sintoma | Causa / solução |
|---------|-------------|
| A página de login nunca abre | Confirme que o host/região do endpoint está correto e acessível; alguns ambientes sem interface não conseguem abrir um navegador — use uma chave de API. |
| `401` após conectar | O token expirou e não há token de atualização (o modo com chave de API nunca atualiza) — reconecte / faça login novamente. |
| Ferramentas ausentes | Seu usuário/chave de API pode não ter permissão para esses recursos; verifique o seu papel no DocBits. |
| Dados / região errados | Certifique-se de ter usado o endpoint da **sua** região (UE vs. EUA). |
