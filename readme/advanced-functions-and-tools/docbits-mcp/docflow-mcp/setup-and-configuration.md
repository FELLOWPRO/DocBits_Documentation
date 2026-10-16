# 设置与配置

## API 端点

| 环境 | MCP 端点 |
|-------------|-------------|
| 开发环境 | `https://dev.docflow.docbits.com/v3/mcp/` |
| 沙盒环境 | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| 生产环境 | `https://docflow.docbits.com/v3/mcp/` |

末尾的斜杠很重要——`https://docflow.docbits.com/v3/mcp`（不带斜杠）将无法匹配该路由。

## 身份验证

所有 MCP 请求都需要有效的 DocBits API 密钥。你可以在 DocBits UI 的 **设置 > 集成** 中找到 API 密钥。

服务器接受通过以下任一请求头传入密钥：

```
Authorization: Bearer <your-api-key>
```

或

```
x-api-key: <your-api-key>
```

### 组织上下文

如果你的 API 密钥关联了多个组织，还需要发送 `x-org-id` 请求头，以便服务器选择正确的组织并解析你的管理员角色：

```
x-org-id: <organization-uuid>
```

实际上，以下仅限管理员使用的工具都需要此请求头——如果不提供，服务器可能会回退到非管理员令牌视图并拒绝请求。

{% hint style="warning" %}
**仅限管理员使用的工具。** `sdk_approve_card`、`sdk_reject_card` 和 `sdk_delete_submission` 要求调用用户是组织管理员。调用这些工具时，请在 API 密钥之外一并发送 `x-org-id`。
{% endhint %}

## 客户端配置

### Claude Code

使用 CLI 添加 DocFlow MCP 服务器：

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

或者将其添加到 `.claude.json` 配置文件中：

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

你也可以将其添加到项目级 `.mcp.json` 文件中：

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

将以下内容添加到 `claude_desktop_config.json`：

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
在 macOS 上，配置文件位于 `~/Library/Application Support/Claude/claude_desktop_config.json`。在 Windows 上，位于 `%APPDATA%\Claude\claude_desktop_config.json`。
{% endhint %}

### OpenAI Codex

Codex CLI 支持 MCP 服务器。将以下配置添加到项目配置中：

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

### 通用 MCP 客户端（Python）

对于使用 MCP Python SDK 的自定义集成：

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

## 验证连接

配置客户端后，通过调用 `list_workflows` 工具测试连接。该工具不需要参数，应返回工作流数组（新组织可能返回空数组）。

{% hint style="info" %}
如果遇到身份验证错误，请确认 API 密钥正确，并且已发送 `Authorization` 请求头。某些 MCP 客户端在更改配置后需要重启。
{% endhint %}
