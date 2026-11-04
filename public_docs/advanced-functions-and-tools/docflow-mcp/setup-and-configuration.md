# Installatie & Configuratie

## API-eindpunten

| Omgeving | MCP-eindpunt |
|-------------|-------------|
| Ontwikkeling | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Productie | `https://docflow.docbits.com/v3/mcp/` |

De afsluitende schuine streep is belangrijk — `https://docflow.docbits.com/v3/mcp` (zonder) komt niet overeen met de route.

## Authenticatie

Alle MCP-verzoeken vereisen een geldige DocBits API-sleutel. U vindt uw API-sleutel onder **Instellingen > Integratie** in de DocBits-gebruikersinterface.

De server accepteert de sleutel via een van deze headers:

```
Authorization: Bearer <your-api-key>
```

of

```
x-api-key: <your-api-key>
```

### Organisatiecontext

Als uw API-sleutel aan meer dan één organisatie is gekoppeld, stuur dan ook de header `x-org-id` mee, zodat de server de juiste organisatie kiest en uw beheerdersrol bepaalt:

```
x-org-id: <organization-uuid>
```

Voor de onderstaande tools die alleen voor beheerders beschikbaar zijn, is deze header in de praktijk vereist — zonder deze header kan de server terugvallen op een weergave zonder beheerdersrechten en het verzoek afwijzen.

{% hint style="warning" %}
**Tools alleen voor beheerders.** `sdk_approve_card`, `sdk_reject_card` en `sdk_delete_submission` vereisen dat de aanroepende gebruiker organisatiebeheerder is. Stuur bij deze aanroepen `x-org-id` mee naast uw API-sleutel.
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

Of voeg het toe aan uw `.claude.json`-configuratiebestand:

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

U kunt het ook toevoegen aan een `.mcp.json`-bestand op projectniveau:

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
Op macOS bevindt het configuratiebestand zich op `~/Library/Application Support/Claude/claude_desktop_config.json`. Op Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI ondersteunt MCP-servers. Voeg toe aan uw projectconfiguratie:

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

Voor aangepaste integraties met de MCP Python SDK:

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

## Verbinding verifiëren

Na het configureren van uw client kunt u de verbinding testen door de `list_workflows`-tool aan te roepen. Deze vereist geen parameters en zou een array van workflows moeten retourneren (of een lege array voor nieuwe organisaties).

{% hint style="info" %}
Als u authenticatiefouten krijgt, controleer dan of uw API-sleutel correct is en of de `Authorization`-header wordt meegestuurd. Sommige MCP-clients vereisen een herstart na het wijzigen van de configuratie.
{% endhint %}
