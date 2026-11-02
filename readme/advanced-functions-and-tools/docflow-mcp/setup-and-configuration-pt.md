# Configuração e Instalação

## Endpoints da API

| Ambiente | Endpoint MCP |
|-------------|-------------|
| Desenvolvimento | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Produção | `https://docflow.docbits.com/v3/mcp/` |

A barra final é importante — `https://docflow.docbits.com/v3/mcp` (sem ela) não corresponderá à rota.

## Autenticação

Todas as requisições MCP exigem uma chave de API DocBits válida. Você pode encontrar sua chave de API em **Configurações > Integração** na interface DocBits.

O servidor aceita a chave por meio de qualquer um destes cabeçalhos:

```
Authorization: Bearer <sua-chave-api>
```

ou

```
x-api-key: <sua-chave-api>
```

### Contexto da organização

Se sua chave de API estiver associada a mais de uma organização, envie também o cabeçalho `x-org-id` para que o servidor escolha a correta e resolva sua função de administrador:

```
x-org-id: <uuid-da-organizacao>
```

Na prática, este cabeçalho é necessário para as ferramentas exclusivas de admin listadas abaixo — sem ele, o servidor pode recorrer a uma visualização de token sem privilégios de admin e rejeitar a requisição.

{% hint style="warning" %}
**Ferramentas exclusivas de admin.** `sdk_approve_card`, `sdk_reject_card` e `sdk_delete_submission` exigem que o usuário chamador seja administrador da organização. Envie `x-org-id` junto com sua chave de API para essas chamadas.
{% endhint %}

## Configuração do Cliente

### Claude Code

Adicione o servidor DocFlow MCP usando a CLI:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Ou adicione ao seu arquivo de configuração `.claude.json`:

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

Você também pode adicioná-lo a um arquivo `.mcp.json` no nível do projeto:

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

Adicione o seguinte ao seu `claude_desktop_config.json`:

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
No macOS, o arquivo de configuração fica em `~/Library/Application Support/Claude/claude_desktop_config.json`. No Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

A CLI Codex suporta servidores MCP. Adicione à configuração do seu projeto:

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

### Cliente MCP Genérico (Python)

Para integrações personalizadas usando o MCP Python SDK:

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

## Verificando sua Conexão

Após configurar seu cliente, teste a conexão chamando a ferramenta `list_workflows`. Ela não exige parâmetros e deve retornar um array de workflows (ou um array vazio para organizações novas).

{% hint style="info" %}
Se você receber erros de autenticação, verifique se sua chave de API está correta e se o cabeçalho `Authorization` está sendo enviado. Alguns clientes MCP exigem reinicialização após alterar a configuração.
{% endhint %}
