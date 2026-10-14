# Configuração

## Endpoints da API

| Ambiente        | Endpoint MCP                             |
| --------------- | ---------------------------------------- |
| Desenvolvimento | `https://dev.api.docbits.com/api/mcp/`   |
| Stage           | `https://stage.api.docbits.com/api/mcp/` |
| Produção        | `https://api.docbits.com/api/mcp/`       |

## Autenticação

Todas as requisições MCP requerem uma chave de API válida do DocBits passada como token Bearer. Você pode encontrar sua chave de API em **Configurações > Integração** na interface do DocBits.

O token é enviado através do cabeçalho `Authorization`:

```
Authorization: Bearer <sua-chave-de-api>
```

{% hint style="warning" %}
Ferramentas exclusivas para administradores (`sdk_approve_card`, `sdk_reject_card`, `sdk_delete_submission`) requerem um token de administrador da organização.
{% endhint %}

## Configuração do Cliente

### Claude Code

Adicione o servidor MCP do DocFlow usando a CLI:

```bash
claude mcp add docflow-dev \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  -- https://dev.api.docbits.com/api/mcp/
```

Ou adicione ao seu arquivo de configuração `.claude.json`:

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

Você também pode adicioná-lo a um arquivo `.mcp.json` no nível do projeto:

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

Adicione o seguinte ao seu `claude_desktop_config.json`:

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
No macOS, o arquivo de configuração está em `~/Library/Application Support/Claude/claude_desktop_config.json`. No Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

O Codex CLI suporta servidores MCP. Adicione à configuração do seu projeto:

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

### Cliente MCP Genérico (Python)

Para integrações personalizadas usando o MCP Python SDK:

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

## Verificando Sua Conexão

Após configurar seu cliente, teste a conexão chamando a ferramenta `list_workflows`. Ela não requer parâmetros e deve retornar um array de workflows (ou um array vazio para organizações novas).

{% hint style="info" %}
Se você receber erros de autenticação, verifique se sua chave de API está correta e se o cabeçalho `Authorization` está sendo enviado. Alguns clientes MCP requerem reinicialização após alterações na configuração.
{% endhint %}
