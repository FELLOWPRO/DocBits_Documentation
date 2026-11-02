# Einrichtung & Konfiguration

## API-Endpunkte

| Umgebung | MCP-Endpunkt |
|-------------|-------------|
| Entwicklung | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Produktion | `https://docflow.docbits.com/v3/mcp/` |

Der abschließende Schrägstrich ist wichtig – `https://docflow.docbits.com/v3/mcp` (ohne ihn) passt nicht zur Route.

## Authentifizierung

Alle MCP-Anfragen erfordern einen gültigen DocBits-API-Schlüssel. Sie finden Ihren API-Schlüssel unter **Settings > Integration** in der DocBits-Oberfläche.

Der Server akzeptiert den Schlüssel über einen dieser Header:

```
Authorization: Bearer <your-api-key>
```

oder

```
x-api-key: <your-api-key>
```

### Organisationskontext

Wenn Ihr API-Schlüssel mehr als einer Organisation zugeordnet ist, senden Sie zusätzlich den Header `x-org-id`, damit der Server die richtige Organisation auswählt und Ihre Admin-Rolle ermittelt:

```
x-org-id: <organization-uuid>
```

Dieser Header ist für die unten genannten reinen Admin-Tools in der Praxis erforderlich – ohne ihn kann der Server auf eine Token-Ansicht ohne Admin-Rechte zurückfallen und die Anfrage ablehnen.

{% hint style="warning" %}
**Reine Admin-Tools.** `sdk_approve_card`, `sdk_reject_card` und `sdk_delete_submission` setzen voraus, dass der aufrufende Benutzer Organisations-Admin ist. Senden Sie bei diesen Aufrufen `x-org-id` zusammen mit Ihrem API-Schlüssel.
{% endhint %}

## Client-Konfiguration

### Claude Code

Fügen Sie den DocFlow-MCP-Server über die CLI hinzu:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Oder fügen Sie ihn Ihrer Konfigurationsdatei `.claude.json` hinzu:

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

Sie können ihn auch einer projektbezogenen Datei `.mcp.json` hinzufügen:

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

Fügen Sie Folgendes in Ihre `claude_desktop_config.json` ein:

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
Unter macOS befindet sich die Konfigurationsdatei unter `~/Library/Application Support/Claude/claude_desktop_config.json`. Unter Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Die Codex CLI unterstützt MCP-Server. Fügen Sie Ihrer Projektkonfiguration Folgendes hinzu:

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

Für eigene Integrationen mit dem MCP Python SDK:

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

## Verbindung überprüfen

Testen Sie nach der Konfiguration Ihres Clients die Verbindung, indem Sie das Tool `list_workflows` aufrufen. Es benötigt keine Parameter und sollte ein Array von Workflows zurückgeben (bzw. ein leeres Array bei neuen Organisationen).

{% hint style="info" %}
Wenn Authentifizierungsfehler auftreten, überprüfen Sie, ob Ihr API-Schlüssel korrekt ist und der Header `Authorization` gesendet wird. Einige MCP-Clients müssen nach einer Änderung der Konfiguration neu gestartet werden.
{% endhint %}
