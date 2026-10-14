# Configurazione

## Endpoint API

| Ambiente | Endpoint MCP |
|-------------|-------------|
| Sviluppo | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Produzione | `https://docflow.docbits.com/v3/mcp/` |

La barra finale è importante — `https://docflow.docbits.com/v3/mcp` (senza barra) non corrisponderà alla route.

## Autenticazione

Tutte le richieste MCP richiedono una API key DocBits valida. Puoi trovare la tua API key in **Settings > Integration** nell'interfaccia di DocBits.

Il server accetta la chiave tramite uno di questi header:

```
Authorization: Bearer <your-api-key>
```

oppure

```
x-api-key: <your-api-key>
```

### Contesto dell'organizzazione

Se la tua API key è associata a più di un'organizzazione, invia anche l'header `x-org-id` in modo che il server scelga quella giusta e risolva il tuo ruolo di amministratore:

```
x-org-id: <organization-uuid>
```

Questo header è di fatto obbligatorio per gli strumenti riservati agli amministratori indicati di seguito — senza di esso, il server potrebbe ripiegare su una vista del token senza privilegi di amministratore e rifiutare la richiesta.

{% hint style="warning" %}
**Strumenti riservati agli amministratori.** `sdk_approve_card`, `sdk_reject_card` e `sdk_delete_submission` richiedono che l'utente chiamante sia un amministratore dell'organizzazione. Invia `x-org-id` insieme alla tua API key per queste chiamate.
{% endhint %}

## Configurazione del Client

### Claude Code

Aggiungi il server MCP DocFlow tramite la CLI:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Oppure aggiungilo al tuo file di configurazione `.claude.json`:

```json
{
  "mcpServers": {
    "docflow": {
      "type": "http",
      "url": "https://docflow.docbits.com/v3/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY",
        "x-org-id": "YOUR_ORG_UUID"
      }
    }
  }
}
```

Puoi anche aggiungerlo a un file `.mcp.json` a livello di progetto:

```json
{
  "mcpServers": {
    "docflow": {
      "type": "http",
      "url": "https://docflow.docbits.com/v3/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY",
        "x-org-id": "YOUR_ORG_UUID"
      }
    }
  }
}
```

### Claude Desktop

Aggiungi quanto segue al tuo `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "docflow": {
      "type": "streamable-http",
      "url": "https://docflow.docbits.com/v3/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY",
        "x-org-id": "YOUR_ORG_UUID"
      }
    }
  }
}
```

{% hint style="info" %}
Su macOS, il file di configurazione si trova in `~/Library/Application Support/Claude/claude_desktop_config.json`. Su Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI supporta i server MCP. Aggiungi alla configurazione del tuo progetto:

```json
{
  "mcpServers": {
    "docflow": {
      "type": "http",
      "url": "https://docflow.docbits.com/v3/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY",
        "x-org-id": "YOUR_ORG_UUID"
      }
    }
  }
}
```

### Client MCP Generico (Python)

Per integrazioni personalizzate con l'SDK Python di MCP:

```python
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def connect():
    async with streamablehttp_client(
        url="https://docflow.docbits.com/v3/mcp/",
        headers={
            "Authorization": "Bearer YOUR_API_KEY",
            "x-org-id": "YOUR_ORG_UUID",
        },
    ) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")
```

## Verificare la Connessione

Dopo aver configurato il client, testa la connessione chiamando lo strumento `list_workflows`. Non richiede parametri e dovrebbe restituire un array di workflow (o un array vuoto per le nuove organizzazioni).

{% hint style="info" %}
Se ricevi errori di autenticazione, verifica che la tua API key sia corretta e che l'header `Authorization` venga inviato. Alcuni client MCP richiedono un riavvio dopo la modifica della configurazione.
{% endhint %}
