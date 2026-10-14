# Configuración e instalación

## Endpoints de la API

| Entorno | Endpoint MCP |
|-------------|-------------|
| Desarrollo | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Producción | `https://docflow.docbits.com/v3/mcp/` |

La barra final es importante: `https://docflow.docbits.com/v3/mcp` (sin ella) no coincidirá con la ruta.

## Autenticación

Todas las solicitudes MCP requieren una clave API válida de DocBits. Puede encontrar su clave API en **Settings > Integration** en la interfaz de DocBits.

El servidor acepta la clave mediante cualquiera de estos encabezados:

```
Authorization: Bearer <your-api-key>
```

o

```
x-api-key: <your-api-key>
```

### Contexto de organización

Si su clave API está asociada a más de una organización, envíe también el encabezado `x-org-id` para que el servidor elija la correcta y resuelva su rol de administrador:

```
x-org-id: <organization-uuid>
```

En la práctica, este encabezado es obligatorio para las herramientas exclusivas para administradores que se describen más adelante; sin él, el servidor puede recurrir a una vista de token sin permisos de administrador y rechazar la solicitud.

{% hint style="warning" %}
**Herramientas exclusivas para administradores.** `sdk_approve_card`, `sdk_reject_card` y `sdk_delete_submission` requieren que el usuario que realiza la llamada sea administrador de la organización. Envíe `x-org-id` junto con su clave API en estas llamadas.
{% endhint %}

## Configuración del cliente

### Claude Code

Añada el servidor DocFlow MCP mediante la CLI:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

O añádalo a su archivo de configuración `.claude.json`:

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

También puede añadirlo a un archivo `.mcp.json` a nivel de proyecto:

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

Añada lo siguiente a su `claude_desktop_config.json`:

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
En macOS, el archivo de configuración se encuentra en `~/Library/Application Support/Claude/claude_desktop_config.json`. En Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI es compatible con los servidores MCP. Añádalo a la configuración de su proyecto:

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

### Cliente MCP genérico (Python)

Para integraciones personalizadas con el SDK de Python para MCP:

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

## Verificar su conexión

Después de configurar su cliente, pruebe la conexión llamando a la herramienta `list_workflows`. No requiere parámetros y debería devolver un array de flujos de trabajo (o un array vacío para organizaciones nuevas).

{% hint style="info" %}
Si obtiene errores de autenticación, verifique que su clave API sea correcta y que se esté enviando el encabezado `Authorization`. Algunos clientes MCP requieren que se reinicien después de cambiar la configuración.
{% endhint %}
