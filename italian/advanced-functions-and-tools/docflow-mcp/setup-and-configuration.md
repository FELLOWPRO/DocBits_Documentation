# Installazione e Configurazione

## Endpoint API

| Ambiente   | Endpoint MCP                             |
| ---------- | ---------------------------------------- |
| Sviluppo   | `https://dev.api.docbits.com/api/mcp/`   |
| Stage      | `https://stage.api.docbits.com/api/mcp/` |
| Produzione | `https://api.docbits.com/api/mcp/`       |

## Autenticazione

Tutte le richieste MCP richiedono una chiave API DocBits valida passata come token Bearer. Puoi trovare la tua chiave API in **Impostazioni > Integrazione** nell'interfaccia DocBits.

Il token viene inviato tramite l'header `Authorization`:

```
Authorization: Bearer <your-api-key>
```

{% hint style="warning" %}
Gli strumenti riservati agli admin (`sdk_approve_card`, `sdk_reject_card`, `sdk_delete_submission`) richiedono un token di amministratore dell'organizzazione.
{% endhint %}

## Configurazione del Client

### Claude Code

Aggiungi il server MCP DocFlow utilizzando la CLI:

```bash
claude mcp add docflow-dev \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  -- https://dev.api.docbits.com/api/mcp/
```

Oppure aggiungilo al file di configurazione `.claude.json`:

```json
{
  "mcpServers": {
    "docflow-dev": {
      "type": "http",
      "url": "https://dev.api.docbits.com/api/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

Puoi anche aggiungerlo a un file `.mcp.json` a livello di progetto:

```json
{
  "mcpServers": {
    "docflow-dev": {
      "type": "http",
      "url": "https://dev.api.docbits.com/api/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
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
      "url": "https://dev.api.docbits.com/api/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
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
      "url": "https://dev.api.docbits.com/api/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_API_KEY"
      }
    }
  }
}
```

### Client MCP Generico (Python)

Per integrazioni personalizzate utilizzando l'SDK Python MCP:

```python
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession

async def connect():
    async with streamablehttp_client(
        url="https://dev.api.docbits.com/api/mcp/",
        headers={"Authorization": "Bearer YOUR_API_KEY"},
    ) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            tools = await session.list_tools()
            print(f"Available tools: {[t.name for t in tools.tools]}")
```

## Verifica della Connessione

Dopo aver configurato il client, testa la connessione chiamando lo strumento `list_workflows`. Non richiede parametri e dovrebbe restituire un array di workflow (o un array vuoto per le nuove organizzazioni).

{% hint style="info" %}
Se ricevi errori di autenticazione, verifica che la tua chiave API sia corretta e che l'header `Authorization` venga inviato. Alcuni client MCP richiedono un riavvio dopo la modifica della configurazione.
{% endhint %}
