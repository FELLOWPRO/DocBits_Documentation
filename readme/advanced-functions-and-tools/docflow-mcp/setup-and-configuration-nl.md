# Installatie & Configuratie

## API-eindpunten

| Omgeving | MCP-eindpunt |
|-------------|-------------|
| Ontwikkeling | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Productie | `https://docflow.docbits.com/v3/mcp/` |

De afsluitende slash is belangrijk — `https://docflow.docbits.com/v3/mcp` (zonder slash) komt niet overeen met de route.

## Authenticatie

Alle MCP-verzoeken vereisen een geldige DocBits API-sleutel. U vindt uw API-sleutel onder **Instellingen > Integratie** in de DocBits-interface.

De server accepteert de sleutel via een van deze headers:

```
Authorization: Bearer <uw-api-sleutel>
```

of

```
x-api-key: <uw-api-sleutel>
```

### Organisatiecontext

Als uw API-sleutel aan meer dan één organisatie is gekoppeld, stuur dan ook de header `x-org-id` zodat de server de juiste organisatie kiest en uw admin-rol oplost:

```
x-org-id: <organisatie-uuid>
```

In de praktijk is deze header nodig voor de admin-only tools hieronder — zonder deze kan de server terugvallen op een niet-admin tokenweergave en het verzoek afwijzen.

{% hint style="warning" %}
**Admin-only tools.** `sdk_approve_card`, `sdk_reject_card` en `sdk_delete_submission` vereisen dat de aanroepende gebruiker organisatie-administrator is. Stuur `x-org-id` samen met uw API-sleutel voor deze aanroepen.
{% endhint %}

## Clientconfiguratie

### Claude Code

Voeg de DocFlow MCP-server toe via de CLI:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Of voeg hem toe aan uw `.claude.json`-configuratiebestand:

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

U kunt hem ook toevoegen aan een `.mcp.json`-bestand op projectniveau:

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

Voeg het volgende toe aan uw `claude_desktop_config.json`:

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
Op macOS staat het configuratiebestand op `~/Library/Application Support/Claude/claude_desktop_config.json`. Op Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

De Codex-CLI ondersteunt MCP-servers. Voeg toe aan uw projectconfiguratie:

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

### Generieke MCP-client (Python)

Voor aangepaste integraties met de MCP Python-SDK:

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

## Uw verbinding verifiëren

Test na het configureren van uw client de verbinding door de tool `list_workflows` aan te roepen. Deze vereist geen parameters en zou een array van workflows moeten teruggeven (of een lege array voor nieuwe organisaties).

{% hint style="info" %}
Als u authenticatiefouten krijgt, controleer dan of uw API-sleutel correct is en of de header `Authorization` wordt verzonden. Sommige MCP-clients vereisen een herstart na een wijziging in de configuratie.
{% endhint %}
