# Setup & Configuration

Connecting an AI assistant to DocBits MCP takes one command. The assistant then signs in through your browser (OAuth) — the same DocBits login you already use — or you can connect with an API key for automation.

## 1. Pick your endpoint

The MCP server lives on the DocBits API host for your environment and region:

```
https://<region>.<env>.api.docbits.com/v3/mcp
```

| Environment | EU endpoint | US endpoint |
|-------------|-------------|-------------|
| Dev | `https://eu.dev.api.docbits.com/v3/mcp` | `https://us.dev.api.docbits.com/v3/mcp` |
| Stage | `https://eu.stage.api.docbits.com/v3/mcp` | `https://us.stage.api.docbits.com/v3/mcp` |
| Sandbox | `https://eu.sandbox.api.docbits.com/v3/mcp` | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | `https://eu.api.docbits.com/v3/mcp` | `https://us.api.docbits.com/v3/mcp` |

{% hint style="info" %}
Use the **region your organization lives in** (EU or US). The MCP server automatically points the login at the matching auth server (`<region>.<env>.auth.docbits.com`) — you do not configure it separately.
{% endhint %}

## 2. Choose how to authenticate

| Method | Best for | How |
|--------|----------|-----|
| **OAuth login** (recommended) | Interactive use in your editor / chat | Browser opens → DocBits login + consent → connected. If you are already signed in to the DocBits web app, the session is reused (no re-login). |
| **API key** (`X-API-KEY`) | Automation, CI, headless agents | Pass your organization API key as a header. No browser. |

OAuth issues a short-lived access token (8 h) plus a refresh token (30 days), so the assistant stays connected and refreshes automatically — you only log in once.

## 3. Connect your client

{% tabs %}
{% tab title="Claude Code" %}
**OAuth login (recommended):**

```bash
claude mcp add --transport http docbits https://eu.dev.api.docbits.com/v3/mcp
claude mcp login docbits
```

`claude mcp login` opens your browser, shows the branded DocBits login and a consent screen, then connects. Run a tool to confirm, e.g. ask Claude to *"check the DocBits API health"*.

**API key instead of login:**

```bash
claude mcp add --transport http docbits https://eu.dev.api.docbits.com/v3/mcp \
  --header "X-API-KEY: <your-api-key>"
```
{% endtab %}

{% tab title="Gemini CLI" %}
**OAuth login (recommended):**

```bash
gemini mcp add --transport http docbits https://eu.dev.api.docbits.com/v3/mcp
```

Gemini CLI discovers the OAuth server automatically and prompts you to sign in on first use (dynamic client registration + token management are handled for you).

**API key instead of login** — add to `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "docbits": {
      "httpUrl": "https://eu.dev.api.docbits.com/v3/mcp",
      "headers": { "X-API-KEY": "<your-api-key>" }
    }
  }
}
```
{% endtab %}

{% tab title="OpenAI Codex" %}
**OAuth login (recommended):**

```bash
codex mcp add docbits \
  --url https://eu.dev.api.docbits.com/v3/mcp \
  --oauth-resource https://eu.dev.api.docbits.com/v3/mcp
```

Codex performs the OAuth login for the streamable-HTTP server on first use.

**API key instead of login** — add to `~/.codex/config.toml`:

```toml
[mcp_servers.docbits]
url = "https://eu.dev.api.docbits.com/v3/mcp"
http_headers = { "X-API-KEY" = "<your-api-key>" }
```

Or keep the key out of the file and read it from the environment:

```toml
[mcp_servers.docbits]
url = "https://eu.dev.api.docbits.com/v3/mcp"
env_http_headers = { "X-API-KEY" = "DOCBITS_API_KEY" }
```
{% endtab %}
{% endtabs %}

## How the OAuth login works (under the hood)

DocBits implements the standard **MCP OAuth 2.1** flow, so any compliant client connects without manual configuration:

1. The client calls `/v3/mcp` and gets a `401` with a `WWW-Authenticate` header pointing to the protected-resource metadata.
2. It reads `/.well-known/oauth-protected-resource` (on the API host), which names the auth server.
3. It reads `/.well-known/oauth-authorization-server` (on the auth host) and **registers itself** dynamically (RFC 7591) — no client secret needed.
4. Your browser opens the DocBits login + consent. If you are already logged in to the web app, the session is reused.
5. The client exchanges the authorization code (PKCE) for an access token + refresh token and calls the MCP.

{% hint style="warning" %}
Logging out of the DocBits **web app does not disconnect the MCP** — the MCP holds its own tokens and keeps working until the refresh token expires (30 days) or you remove the server from your client.
{% endhint %}

## Troubleshooting

| Symptom | Cause / fix |
|---------|-------------|
| Login page never opens | Confirm the endpoint host/region is correct and reachable; some headless environments cannot open a browser — use an API key instead. |
| `401` after connecting | Token expired and no refresh token (API-key mode never refreshes) — reconnect / re-login. |
| Tools missing | Your user/API key may lack permission for those features; check your DocBits role. |
| Wrong data / region | Make sure you used **your** region's endpoint (EU vs US). |
