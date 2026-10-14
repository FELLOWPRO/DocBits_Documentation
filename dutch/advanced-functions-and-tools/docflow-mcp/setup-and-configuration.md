# Installatie en Configuratie

## API-eindpunten

| Omgeving     | MCP-eindpunt                             |
| ------------ | ---------------------------------------- |
| Ontwikkeling | `https://dev.api.docbits.com/api/mcp/`   |
| Stage        | `https://stage.api.docbits.com/api/mcp/` |
| Productie    | `https://api.docbits.com/api/mcp/`       |

## Authenticatie

Alle MCP-verzoeken vereisen een geldige DocBits API-sleutel die als Bearer-token wordt meegegeven. U vindt uw API-sleutel in **Instellingen > Integratie** in de DocBits-gebruikersinterface.

Het token wordt verzonden via de `Authorization`-header:

```
Authorization: Bearer <your-api-key>
```

{% hint style="warning" %}
Tools die alleen voor admins beschikbaar zijn (`sdk_approve_card`, `sdk_reject_card`, `sdk_delete_submission`) vereisen een organisatiebeheerder-token.
{% endhint %}

## Clientconfiguratie

### Claude Code

Voeg de DocFlow MCP-server toe via de CLI:

```bash
claude mcp add docflow-dev \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  -- https://dev.api.docbits.com/api/mcp/
```

Of voeg het toe aan uw `.claude.json`-configuratiebestand:

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

U kunt het ook toevoegen aan een `.mcp.json`-bestand op projectniveau:

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

Voeg het volgende toe aan uw `claude_desktop_config.json`:

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
Op macOS bevindt het configuratiebestand zich op `~/Library/Application Support/Claude/claude_desktop_config.json`. Op Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI ondersteunt MCP-servers. Voeg toe aan uw projectconfiguratie:

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

### Generieke MCP-client (Python)

Voor aangepaste integraties met de MCP Python SDK:

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

## Verbinding verifiëren

Na het configureren van uw client kunt u de verbinding testen door de `list_workflows`-tool aan te roepen. Deze vereist geen parameters en zou een array van workflows moeten retourneren (of een lege array voor nieuwe organisaties).

{% hint style="info" %}
Als u authenticatiefouten krijgt, controleer dan of uw API-sleutel correct is en of de `Authorization`-header wordt meegestuurd. Sommige MCP-clients vereisen een herstart na het wijzigen van de configuratie.
{% endhint %}
