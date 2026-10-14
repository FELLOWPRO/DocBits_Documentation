# Setup & Konfiguration

## API-Endpunkte

| Umgebung    | MCP-Endpunkt                             |
| ----------- | ---------------------------------------- |
| Entwicklung | `https://dev.api.docbits.com/api/mcp/`   |
| Stage       | `https://stage.api.docbits.com/api/mcp/` |
| Produktion  | `https://api.docbits.com/api/mcp/`       |

## Authentifizierung

Alle MCP-Anfragen erfordern einen gueltigen DocBits-API-Schluessel, der als Bearer-Token uebergeben wird. Sie finden Ihren API-Schluessel unter **Einstellungen > Integration** in der DocBits-Oberflaeche.

Der Token wird ueber den `Authorization`-Header gesendet:

```
Authorization: Bearer <ihr-api-schluessel>
```

{% hint style="warning" %}
Admin-only-Tools (`sdk_approve_card`, `sdk_reject_card`, `sdk_delete_submission`) erfordern einen Organisations-Admin-Token.
{% endhint %}

## Client-Konfiguration

### Claude Code

Fuegen Sie den DocFlow MCP-Server ueber die CLI hinzu:

```bash
claude mcp add docflow-dev \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  -- https://dev.api.docbits.com/api/mcp/
```

Oder fuegen Sie ihn in Ihre `.claude.json`-Konfigurationsdatei ein:

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

Sie koennen ihn auch in eine projektbezogene `.mcp.json`-Datei einfuegen:

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

Fuegen Sie Folgendes in Ihre `claude_desktop_config.json` ein:

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
Unter macOS befindet sich die Konfigurationsdatei unter `~/Library/Application Support/Claude/claude_desktop_config.json`. Unter Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI unterstuetzt MCP-Server. Fuegen Sie Folgendes zu Ihrer Projektkonfiguration hinzu:

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

### Generischer MCP-Client (Python)

Fuer benutzerdefinierte Integrationen mit dem MCP Python SDK:

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

## Verbindung ueberpruefen

Nachdem Sie Ihren Client konfiguriert haben, testen Sie die Verbindung, indem Sie das Tool `list_workflows` aufrufen. Es erfordert keine Parameter und sollte ein Array von Workflows zurueckgeben (oder ein leeres Array fuer neue Organisationen).

{% hint style="info" %}
Wenn Sie Authentifizierungsfehler erhalten, ueberpruefen Sie, ob Ihr API-Schluessel korrekt ist und der `Authorization`-Header gesendet wird. Einige MCP-Clients erfordern einen Neustart nach Aenderung der Konfiguration.
{% endhint %}
