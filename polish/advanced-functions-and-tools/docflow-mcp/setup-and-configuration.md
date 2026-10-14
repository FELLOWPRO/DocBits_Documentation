# Konfiguracja

## Punkty koncowe API

| Srodowisko    | Punkt koncowy MCP                        |
| ------------- | ---------------------------------------- |
| Deweloperskie | `https://dev.api.docbits.com/api/mcp/`   |
| Stage         | `https://stage.api.docbits.com/api/mcp/` |
| Produkcyjne   | `https://api.docbits.com/api/mcp/`       |

## Uwierzytelnianie

Wszystkie zadania MCP wymagaja prawidlowego klucza API DocBits przekazanego jako token Bearer. Klucz API mozesz znalezc w **Settings > Integration** w interfejsie DocBits.

Token jest wysylany za pomoca naglowka `Authorization`:

```
Authorization: Bearer <your-api-key>
```

{% hint style="warning" %}
Narzedzia dostepne tylko dla administratorow (`sdk_approve_card`, `sdk_reject_card`, `sdk_delete_submission`) wymagaja tokenu administratora organizacji.
{% endhint %}

## Konfiguracja klienta

### Claude Code

Dodaj serwer DocFlow MCP za pomoca CLI:

```bash
claude mcp add docflow-dev \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  -- https://dev.api.docbits.com/api/mcp/
```

Lub dodaj go do pliku konfiguracyjnego `.claude.json`:

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

Mozesz rowniez dodac go do pliku `.mcp.json` na poziomie projektu:

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

Dodaj nastepujaca konfiguracje do pliku `claude_desktop_config.json`:

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
Na macOS plik konfiguracyjny znajduje sie w `~/Library/Application Support/Claude/claude_desktop_config.json`. Na Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI obsluguje serwery MCP. Dodaj do konfiguracji projektu:

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

### Ogolny klient MCP (Python)

Dla niestandardowych integracji z uzyciem MCP Python SDK:

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

## Weryfikacja polaczenia

Po skonfigurowaniu klienta przetestuj polaczenie, wywolujac narzedzie `list_workflows`. Nie wymaga ono zadnych parametrow i powinno zwrocic tablice przepływow pracy (lub pusta tablice dla nowych organizacji).

{% hint style="info" %}
Jesli otrzymujesz bledy uwierzytelniania, sprawdz, czy Twoj klucz API jest prawidlowy i czy naglowek `Authorization` jest wysylany. Niektorzy klienci MCP wymagaja ponownego uruchomienia po zmianie konfiguracji.
{% endhint %}
