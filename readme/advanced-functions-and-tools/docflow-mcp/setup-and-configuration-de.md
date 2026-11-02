# Einrichtung & Konfiguration

## API-Endpunkte

| Umgebung | MCP-Endpunkt |
|-------------|-------------|
| Entwicklung | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Produktion | `https://docflow.docbits.com/v3/mcp/` |

Der abschliessende Slash ist wichtig -- `https://docflow.docbits.com/v3/mcp` (ohne Slash) trifft die Route nicht.

## Authentifizierung

Alle MCP-Anfragen erfordern einen gueltigen DocBits-API-Schluessel. Sie finden Ihren API-Schluessel unter **Einstellungen > Integration** in der DocBits-Oberflaeche.

Der Server akzeptiert den Schluessel ueber einen der folgenden Header:

```
Authorization: Bearer <ihr-api-schluessel>
```

oder

```
x-api-key: <ihr-api-schluessel>
```

### Organisationskontext

Wenn Ihr API-Schluessel mit mehr als einer Organisation verknuepft ist, senden Sie zusaetzlich den Header `x-org-id`, damit der Server die richtige Organisation auswaehlt und Ihre Admin-Rolle aufloest:

```
x-org-id: <organisations-uuid>
```

Dieser Header ist in der Praxis fuer die unten aufgefuehrten Admin-Tools erforderlich -- ohne ihn kann der Server auf eine eingeschraenkte Token-Ansicht zurueckfallen und die Anfrage ablehnen.

{% hint style="warning" %}
**Admin-only-Tools.** `sdk_approve_card`, `sdk_reject_card` und `sdk_delete_submission` erfordern, dass der aufrufende Benutzer Organisations-Administrator ist. Senden Sie `x-org-id` zusammen mit Ihrem API-Schluessel fuer diese Aufrufe.
{% endhint %}

## Client-Konfiguration

### Claude Code

Fuegen Sie den DocFlow MCP-Server ueber die CLI hinzu:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Oder fuegen Sie ihn in Ihre `.claude.json`-Konfigurationsdatei ein:

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

Sie koennen ihn auch in eine projektbezogene `.mcp.json`-Datei eintragen:

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

Fuegen Sie Folgendes in Ihre `claude_desktop_config.json` ein:

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
Unter macOS liegt die Konfigurationsdatei unter `~/Library/Application Support/Claude/claude_desktop_config.json`. Unter Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Die Codex-CLI unterstuetzt MCP-Server. Fuegen Sie sie zu Ihrer Projektkonfiguration hinzu:

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

### Generischer MCP-Client (Python)

Fuer benutzerdefinierte Integrationen mit dem MCP-Python-SDK:

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

## Verbindung pruefen

Testen Sie die Verbindung nach der Konfiguration Ihres Clients, indem Sie das Tool `list_workflows` aufrufen. Es benoetigt keine Parameter und sollte ein Array von Workflows zurueckgeben (oder ein leeres Array bei neuen Organisationen).

{% hint style="info" %}
Wenn Sie Authentifizierungsfehler erhalten, pruefen Sie, ob Ihr API-Schluessel korrekt ist und ob der `Authorization`-Header gesendet wird. Einige MCP-Clients erfordern einen Neustart nach Konfigurationsaenderungen.
{% endhint %}
