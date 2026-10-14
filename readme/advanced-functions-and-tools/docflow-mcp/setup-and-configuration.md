# Konfiguracja i ustawienia

## Punkty końcowe API

| Środowisko | Punkt końcowy MCP |
|-------------|-------------|
| Deweloperskie | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Produkcyjne | `https://docflow.docbits.com/v3/mcp/` |

Ukośnik na końcu ma znaczenie — adres `https://docflow.docbits.com/v3/mcp` (bez niego) nie pasuje do trasy.

## Uwierzytelnianie

Wszystkie żądania MCP wymagają prawidłowego klucza API DocBits. Swój klucz API znajdziesz w **Settings > Integration** w interfejsie DocBits.

Serwer akceptuje klucz w jednym z poniższych nagłówków:

```
Authorization: Bearer <your-api-key>
```

lub

```
x-api-key: <your-api-key>
```

### Kontekst organizacji

Jeśli Twój klucz API jest powiązany z więcej niż jedną organizacją, wyślij również nagłówek `x-org-id`, aby serwer wybrał właściwą organizację i ustalił Twoją rolę administratora:

```
x-org-id: <organization-uuid>
```

W praktyce ten nagłówek jest wymagany dla poniższych narzędzi dostępnych tylko dla administratorów — bez niego serwer może wrócić do widoku tokenu bez uprawnień administratora i odrzucić żądanie.

{% hint style="warning" %}
**Narzędzia tylko dla administratorów.** `sdk_approve_card`, `sdk_reject_card` i `sdk_delete_submission` wymagają, aby wywołujący użytkownik był administratorem organizacji. Przy tych wywołaniach wyślij `x-org-id` razem z kluczem API.
{% endhint %}

## Konfiguracja klienta

### Claude Code

Dodaj serwer DocFlow MCP za pomocą CLI:

```bash
claude mcp add docflow \
  --transport http \
  --header "Authorization: Bearer YOUR_API_KEY" \
  --header "x-org-id: YOUR_ORG_UUID" \
  -- https://docflow.docbits.com/v3/mcp/
```

Lub dodaj go do pliku konfiguracyjnego `.claude.json`:

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

Możesz też dodać go do pliku `.mcp.json` na poziomie projektu:

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

Dodaj poniższą konfigurację do pliku `claude_desktop_config.json`:

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
W macOS plik konfiguracyjny znajduje się w `~/Library/Application Support/Claude/claude_desktop_config.json`. W Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

Codex CLI obsługuje serwery MCP. Dodaj do konfiguracji projektu:

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

### Ogólny klient MCP (Python)

Dla niestandardowych integracji z użyciem MCP Python SDK:

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

## Weryfikacja połączenia

Po skonfigurowaniu klienta przetestuj połączenie, wywołując narzędzie `list_workflows`. Nie wymaga ono żadnych parametrów i powinno zwrócić tablicę przepływów pracy (lub pustą tablicę dla nowych organizacji).

{% hint style="info" %}
Jeśli otrzymujesz błędy uwierzytelniania, sprawdź, czy Twój klucz API jest prawidłowy i czy nagłówek `Authorization` jest wysyłany. Niektórzy klienci MCP wymagają ponownego uruchomienia po zmianie konfiguracji.
{% endhint %}
