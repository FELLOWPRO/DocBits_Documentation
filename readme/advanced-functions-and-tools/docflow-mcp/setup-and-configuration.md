# Configuração

## Endpoints da API

| Ambiente | Endpoint MCP |
|-------------|-------------|
| Desenvolvimento | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Produção | `https://docflow.docbits.com/v3/mcp/` |

A barra final é importante — `https://docflow.docbits.com/v3/mcp` (sem ela) não corresponde à rota.

## Autenticação

Todas as requisições MCP exigem uma chave de API válida do DocBits. Você encontra sua chave de API em **Configurações > Integração** na interface do DocBits.

O servidor aceita a chave em qualquer um destes cabeçalhos:

```
Authorization: Bearer <your-api-key>
```

ou

```
x-api-key: <your-api-key>
```

### Contexto da organização

Se sua chave de API estiver associada a mais de uma organização, envie também o cabeçalho `x-org-id` para que o servidor escolha a correta e resolva sua função de administrador:

```
x-org-id: <organization-uuid>
```

Na prática, esse cabeçalho é obrigatório para as ferramentas exclusivas de administrador abaixo — sem ele, o servidor pode recorrer a uma visão de token sem privilégios de administrador e rejeitar a requisição.

{% hint style="warning" %}
**Ferramentas exclusivas de administrador.** `sdk_approve_card`, `sdk_reject_card` e `sdk_delete_submission` exigem que o usuário que faz a chamada seja administrador da organização. Envie `x-org-id` junto com sua chave de API nessas chamadas.
{% endhint %}

## Configuração do cliente

### Claude Code

Adicione o servidor MCP do DocFlow usando a CLI:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Ou adicione-o ao seu arquivo de configuração `.claude.json`:

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

O Codex CLI oferece suporte a servidores MCP. Adicione à configuração do seu projeto:

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

Para integrações personalizadas com o MCP Python SDK:

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

## Verificando a conexão

Depois de configurar seu cliente, teste a conexão chamando a ferramenta `list_workflows`. Ela não exige parâmetros e deve retornar uma lista de workflows (ou uma lista vazia para organizações novas).

{% hint style="info" %}
Se você receber erros de autenticação, verifique se a chave de API está correta e se o cabeçalho `Authorization` está sendo enviado. Alguns clientes MCP exigem reinicialização após a alteração da configuração.
{% endhint %}
