# Setup & Configuration

## API Endpoints

| Environment | MCP Endpoint |
|-------------|-------------|
| Development | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Production | `https://docflow.docbits.com/v3/mcp/` |

The trailing slash matters — `https://docflow.docbits.com/v3/mcp` (without it) will not match the route.

## Authentication

All MCP requests require a valid DocBits API key. You can find your API key in **Settings > Integration** in the DocBits UI.

The server accepts the key via either of these headers:

```
Authorization: Bearer <your-api-key>
```

or

```
x-api-key: <your-api-key>
```

### Organization context

If your API key is associated with more than one organization, also send the `x-org-id` header so the server picks the right one and resolves your admin role:

```
x-org-id: <organization-uuid>
```

This header is required in practice for the admin-only tools below — without it, the server may fall back to a non-admin token view and reject the request.

{% hint style="warning" %}
**Admin-only tools.** `sdk_approve_card`, `sdk_reject_card`, and `sdk_delete_submission` require the calling user to be an organization admin. Send `x-org-id` alongside your API key for these calls.
{% endhint %}

## Client Configuration

### Claude Code

Add the DocFlow MCP server using the CLI:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Or add it to your `.claude.json` configuration file:

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

You can also add it to a project-level `.mcp.json` file:

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

Add the following to your `claude_desktop_config.json`:

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
On macOS, the config file is at `~/Library/Application Support/Claude/claude_desktop_config.json`. On Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI supports MCP servers. Add to your project configuration:

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

### Generic MCP Client (Python)

For custom integrations using the MCP Python SDK:

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

## Verifying Your Connection

After configuring your client, test the connection by calling the `list_workflows` tool. It requires no parameters and should return an array of workflows (or an empty array for new organizations).

{% hint style="info" %}
If you get authentication errors, verify that your API key is correct and that the `Authorization` header is being sent. Some MCP clients require you to restart after changing configuration.
{% endhint %}
