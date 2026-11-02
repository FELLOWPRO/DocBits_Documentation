# Installation et configuration

## Points de terminaison API

| Environnement | Point de terminaison MCP |
|-------------|-------------|
| Développement | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Production | `https://docflow.docbits.com/v3/mcp/` |

Le slash final est important — `https://docflow.docbits.com/v3/mcp` (sans slash) ne correspondra pas à la route.

## Authentification

Toutes les requêtes MCP nécessitent une clé API DocBits valide. Vous trouverez votre clé API dans **Paramètres > Intégration** dans l'interface DocBits.

Le serveur accepte la clé via l'un de ces en-têtes :

```
Authorization: Bearer <votre-cle-api>
```

ou

```
x-api-key: <votre-cle-api>
```

### Contexte de l'organisation

Si votre clé API est associée à plus d'une organisation, envoyez également l'en-tête `x-org-id` pour que le serveur sélectionne la bonne organisation et résolve votre rôle d'administrateur :

```
x-org-id: <uuid-organisation>
```

Cet en-tête est requis en pratique pour les outils réservés aux administrateurs ci-dessous — sans lui, le serveur peut retomber sur une vue de jeton non-admin et rejeter la requête.

{% hint style="warning" %}
**Outils réservés aux admins.** `sdk_approve_card`, `sdk_reject_card` et `sdk_delete_submission` exigent que l'utilisateur appelant soit administrateur de l'organisation. Envoyez `x-org-id` avec votre clé API pour ces appels.
{% endhint %}

## Configuration du client

### Claude Code

Ajoutez le serveur DocFlow MCP via la CLI :

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Ou ajoutez-le à votre fichier de configuration `.claude.json` :

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

Vous pouvez aussi l'ajouter à un fichier `.mcp.json` au niveau du projet :

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

Ajoutez ce qui suit à votre `claude_desktop_config.json` :

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
Sur macOS, le fichier de configuration se trouve dans `~/Library/Application Support/Claude/claude_desktop_config.json`. Sur Windows : `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

La CLI Codex prend en charge les serveurs MCP. Ajoutez-le à la configuration de votre projet :

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

### Client MCP générique (Python)

Pour les intégrations personnalisées avec le SDK Python MCP :

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

## Vérifier votre connexion

Après avoir configuré votre client, testez la connexion en appelant l'outil `list_workflows`. Il ne nécessite aucun paramètre et doit retourner un tableau de workflows (ou un tableau vide pour les nouvelles organisations).

{% hint style="info" %}
Si vous obtenez des erreurs d'authentification, vérifiez que votre clé API est correcte et que l'en-tête `Authorization` est bien envoyé. Certains clients MCP nécessitent un redémarrage après modification de la configuration.
{% endhint %}
