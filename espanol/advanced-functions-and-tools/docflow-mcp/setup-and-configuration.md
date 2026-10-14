# Configuración

## Endpoints de la API

| Entorno    | Endpoint MCP                             |
| ---------- | ---------------------------------------- |
| Desarrollo | `https://dev.api.docbits.com/api/mcp/`   |
| Stage      | `https://stage.api.docbits.com/api/mcp/` |
| Producción | `https://api.docbits.com/api/mcp/`       |

## Autenticación

Todas las solicitudes MCP requieren una clave API válida de DocBits pasada como token Bearer. Puedes encontrar tu clave API en **Configuración > Integración** en la interfaz de DocBits.

El token se envía a través del encabezado `Authorization`:

```
Authorization: Bearer <your-api-key>
```

{% hint style="warning" %}
Las herramientas exclusivas para administradores (`sdk_approve_card`, `sdk_reject_card`, `sdk_delete_submission`) requieren un token de administrador de la organización.
{% endhint %}

## Configuración del cliente

### Claude Code

Agrega el servidor MCP de DocFlow usando la CLI:

```bash
claude mcp add docflow-dev \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  -- https://dev.api.docbits.com/api/mcp/
```

O agrégalo a tu archivo de configuración `.claude.json`:

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

También puedes agregarlo a un archivo `.mcp.json` a nivel de proyecto:

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

Agrega lo siguiente a tu `claude_desktop_config.json`:

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
En macOS, el archivo de configuración se encuentra en `~/Library/Application Support/Claude/claude_desktop_config.json`. En Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI soporta servidores MCP. Agrégalo a la configuración de tu proyecto:

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

### Cliente MCP genérico (Python)

Para integraciones personalizadas usando el SDK de Python para MCP:

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

## Verificar tu conexión

Después de configurar tu cliente, prueba la conexión llamando a la herramienta `list_workflows`. No requiere parámetros y debería devolver un array de flujos de trabajo (o un array vacío para organizaciones nuevas).

{% hint style="info" %}
Si obtienes errores de autenticación, verifica que tu clave API sea correcta y que el encabezado `Authorization` se esté enviando. Algunos clientes MCP requieren que reinicies después de cambiar la configuración.
{% endhint %}
