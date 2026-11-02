# Konfiguracja i ustawienia

## Punkty koncowe API

| Srodowisko | Punkt koncowy MCP |
|-------------|-------------|
| Deweloperskie | `https://dev.docflow.docbits.com/v3/mcp/` |
| Sandbox | `https://sandbox.docflow.docbits.com/v3/mcp/` |
| Produkcyjne | `https://docflow.docbits.com/v3/mcp/` |

Konczacy slash jest istotny — `https://docflow.docbits.com/v3/mcp` (bez niego) nie dopasuje sie do trasy.

## Uwierzytelnianie

Wszystkie zadania MCP wymagaja wazonego klucza API DocBits. Klucz API znajdziesz w **Ustawienia > Integracja** w interfejsie DocBits.

Serwer akceptuje klucz za pomoca jednego z tych naglowkow:

```
Authorization: Bearer <twoj-klucz-api>
```

lub

```
x-api-key: <twoj-klucz-api>
```

### Kontekst organizacji

Jesli twoj klucz API jest powiazany z wiecej niz jedna organizacja, wyslij rowniez naglowek `x-org-id`, aby serwer wybral wlasciwa organizacje i rozpoznal twoja role administratora:

```
x-org-id: <uuid-organizacji>
```

W praktyce ten naglowek jest wymagany dla narzedzi tylko dla adminow wymienionych ponizej — bez niego serwer moze wrocic do widoku tokena bez uprawnien admina i odrzucic zadanie.

{% hint style="warning" %}
**Narzedzia tylko dla adminow.** `sdk_approve_card`, `sdk_reject_card` i `sdk_delete_submission` wymagaja, aby uzytkownik wywolujacy byl administratorem organizacji. Wyslij `x-org-id` razem z kluczem API dla tych wywolan.
{% endhint %}

## Konfiguracja klienta

### Claude Code

Dodaj serwer DocFlow MCP za pomoca CLI:

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

Mozesz go rowniez dodac do pliku `.mcp.json` na poziomie projektu:

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

Dodaj nastepujace do pliku `claude_desktop_config.json`:

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
Na macOS plik konfiguracyjny znajduje sie w `~/Library/Application Support/Claude/claude_desktop_config.json`. Na Windows: `%APPDATA%\Claude\claude_desktop_config.json`.
{% endhint %}

### OpenAI Codex

CLI Codex obsluguje serwery MCP. Dodaj do konfiguracji projektu:

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

### Ogolny klient MCP (Python)

Dla niestandardowych integracji uzywajacych Python SDK MCP:

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

## Sprawdzanie polaczenia

Po skonfigurowaniu klienta przetestuj polaczenie wywolujac narzedzie `list_workflows`. Nie wymaga zadnych parametrow i powinno zwrocic tablice przepływow pracy (lub pusta tablice dla nowych organizacji).

{% hint style="info" %}
Jesli otrzymujesz bledy uwierzytelniania, sprawdz, czy klucz API jest poprawny i czy wysylany jest naglowek `Authorization`. Niektorzy klienci MCP wymagaja ponownego uruchomienia po zmianie konfiguracji.
{% endhint %}
