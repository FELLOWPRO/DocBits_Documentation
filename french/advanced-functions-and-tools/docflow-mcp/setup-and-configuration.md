# Installation et Configuration

## Points de terminaison API

| Environnement | Point de terminaison MCP                 |
| ------------- | ---------------------------------------- |
| Développement | `https://dev.api.docbits.com/api/mcp/`   |
| Stage         | `https://stage.api.docbits.com/api/mcp/` |
| Production    | `https://api.docbits.com/api/mcp/`       |

## Authentification

Toutes les requêtes MCP nécessitent une clé API DocBits valide transmise en tant que jeton Bearer. Vous pouvez trouver votre clé API dans **Paramètres > Intégration** dans l'interface DocBits.

Le jeton est envoyé via l'en-tête `Authorization` :

```
Authorization: Bearer <your-api-key>
```

{% hint style="warning" %}
Les outils réservés aux administrateurs (`sdk_approve_card`, `sdk_reject_card`, `sdk_delete_submission`) nécessitent un jeton d'administrateur d'organisation.
{% endhint %}

## Configuration du client

### Claude Code

Ajoutez le serveur MCP DocFlow en utilisant la CLI :

```bash
claude mcp add docflow-dev \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  -- https://dev.api.docbits.com/api/mcp/
```

Ou ajoutez-le à votre fichier de configuration `.claude.json` :

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

Vous pouvez également l'ajouter à un fichier `.mcp.json` au niveau du projet :

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

Ajoutez ce qui suit à votre fichier `claude_desktop_config.json` :

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
Sur macOS, le fichier de configuration se trouve à `~/Library/Application Support/Claude/claude_desktop_config.json`. Sur Windows : `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI prend en charge les serveurs MCP. Ajoutez à la configuration de votre projet :

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

### Client MCP générique (Python)

Pour les intégrations personnalisées utilisant le SDK Python MCP :

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

## Vérification de votre connexion

Après avoir configuré votre client, testez la connexion en appelant l'outil `list_workflows`. Il ne nécessite aucun paramètre et devrait retourner un tableau de workflows (ou un tableau vide pour les nouvelles organisations).

{% hint style="info" %}
Si vous obtenez des erreurs d'authentification, vérifiez que votre clé API est correcte et que l'en-tête `Authorization` est bien envoyé. Certains clients MCP nécessitent un redémarrage après modification de la configuration.
{% endhint %}
