# Configuración e instalación

## Endpoints de la API

| Entorno | Endpoint MCP |
|-------------|-------------|
| Desarrollo | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Producción | `https://docflow.docbits.com/v3/mcp/` |

La barra final es importante — `https://docflow.docbits.com/v3/mcp` (sin la barra) no coincidirá con la ruta.

## Autenticación

Todas las solicitudes MCP requieren una clave API de DocBits válida. Puedes encontrar tu clave API en **Configuración > Integración** en la interfaz de DocBits.

El servidor acepta la clave a través de cualquiera de estas cabeceras:

```
Authorization: Bearer <tu-clave-api>
```

o

```
x-api-key: <tu-clave-api>
```

### Contexto de la organización

Si tu clave API está asociada a más de una organización, envía también la cabecera `x-org-id` para que el servidor elija la correcta y resuelva tu rol de administrador:

```
x-org-id: <uuid-de-organizacion>
```

En la práctica, esta cabecera es necesaria para las herramientas de administrador listadas más abajo — sin ella, el servidor puede recurrir a una vista de token no admin y rechazar la solicitud.

{% hint style="warning" %}
**Herramientas solo para admin.** `sdk_approve_card`, `sdk_reject_card` y `sdk_delete_submission` requieren que el usuario que llama sea administrador de la organización. Envía `x-org-id` junto con tu clave API para estas llamadas.
{% endhint %}

## Configuración del cliente

### Claude Code

Añade el servidor DocFlow MCP usando la CLI:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

O añádelo a tu archivo de configuración `.claude.json`:

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

También puedes añadirlo a un archivo `.mcp.json` a nivel de proyecto:

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

Añade lo siguiente a tu `claude_desktop_config.json`:

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
En macOS, el archivo de configuración está en `~/Library/Application Support/Claude/claude_desktop_config.json`. En Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

La CLI de Codex admite servidores MCP. Añádelo a la configuración de tu proyecto:

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

Para integraciones personalizadas usando el SDK de Python de MCP:

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

## Verificar tu conexión

Después de configurar tu cliente, prueba la conexión llamando a la herramienta `list_workflows`. No requiere parámetros y debería devolver un array de flujos de trabajo (o un array vacío para organizaciones nuevas).

{% hint style="info" %}
Si obtienes errores de autenticación, verifica que tu clave API sea correcta y que la cabecera `Authorization` se esté enviando. Algunos clientes MCP requieren reiniciarse después de cambiar la configuración.
{% endhint %}
