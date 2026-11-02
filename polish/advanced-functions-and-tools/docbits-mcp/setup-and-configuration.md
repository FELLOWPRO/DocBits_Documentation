# Konfiguracja

Podłączenie asystenta AI do DocBits MCP wymaga jednego polecenia, a następnie jednorazowego logowania. Zalecanym sposobem logowania jest **OAuth** — to samo logowanie DocBits, którego już używasz, w przeglądarce. Do automatyzacji możesz zamiast tego połączyć się za pomocą klucza API.

## 1. Wybierz endpoint

Serwer MCP działa na hoście API DocBits. Użyj hosta dla **swojego regionu (EU lub US)**:

| Środowisko | Endpoint EU | Endpoint US |
|-------------|-------------|-------------|
| Produkcja | `https://eu.api.docbits.com/v3/mcp` | `https://us.api.docbits.com/v3/mcp` |
| Sandbox | `https://eu.sandbox.api.docbits.com/v3/mcp` | `https://us.sandbox.api.docbits.com/v3/mcp` |

{% hint style="info" %}
`api.docbits.com` to jedyny endpoint używany przez klientów. Zawsze wybieraj **region, w którym działa Twoja organizacja** (EU lub US) — MCP automatycznie kieruje logowanie do odpowiedniego serwera uwierzytelniania, nie musisz konfigurować tego osobno. Poniższe przykłady używają hosta produkcyjnego EU; podstaw własny.
{% endhint %}

## 2. Zaloguj się przez OAuth (zalecane)

OAuth to najprostsza droga — bez kopiowania sekretów. Po dodaniu serwera **pierwsze połączenie otwiera logowanie DocBits w przeglądarce**, zatwierdzasz ekran zgody i klient jest połączony.

**Co zobaczysz w każdym kliencie:**

1. Klient otwiera w przeglądarce stronę logowania DocBits.
2. Logujesz się swoim kontem DocBits (jeśli jesteś już zalogowany w aplikacji internetowej DocBits, sesja jest wykorzystywana ponownie — bez ponownego logowania).
3. Zatwierdzasz ekran zgody („Authorize access”).
4. Przeglądarka przekazuje klientowi token i połączenie jest aktywne.

OAuth wystawia krótkotrwały token dostępu (8 godz.) oraz token odświeżania (30 dni), więc klient odświeża się automatycznie i pozostaje połączony — **logujesz się tylko raz.**

{% hint style="success" %}
**Musisz być zalogowany w DocBits — Twoja istniejąca sesja jest wykorzystywana ponownie.** Logowanie MCP nie prosi o ponowne zalogowanie, jeśli Twoja przeglądarka ma już sesję DocBits. Jeśli jesteś już zalogowany w aplikacji internetowej DocBits, przechodzisz **od razu do ekranu zgody**. Jeśli nie jesteś zalogowany, najpierw pojawia się strona logowania DocBits; po jednorazowym zalogowaniu sesja jest automatycznie przenoszona do MCP.
{% endhint %}

<figure><img src="../../.gitbook/assets/docbits-mcp-login.png" alt="Strona logowania DocBits"><figcaption><p>Jeszcze nie zalogowany — markowa strona logowania DocBits (widzisz ją tylko wtedy, gdy przeglądarka nie ma sesji DocBits)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits-mcp-consent.png" alt="Ekran autoryzacji dostępu / zgody DocBits"><figcaption><p>Już zalogowany — sesja jest wykorzystywana ponownie i przechodzisz od razu do ekranu zgody. Zatwierdź, aby się połączyć; wyświetlane jest to, o co prosi klient (zakres i adres przekierowania).</p></figcaption></figure>

{% tabs %}
{% tab title="Claude Code" %}
```bash
# 1) add the server
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp

# 2) sign in (opens browser → DocBits login + consent → connected)
claude mcp login docbits
```

`claude mcp login docbits` to krok OAuth. Po jego pomyślnym zakończeniu potwierdź połączenie, pytając Claude: *„sprawdź stan API DocBits”*.
{% endtab %}

{% tab title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp
```

Gemini CLI automatycznie wykrywa serwer OAuth. **Przy pierwszym** użyciu serwera otwiera logowanie DocBits w przeglądarce (dynamiczna rejestracja klienta i zarządzanie tokenami odbywają się automatycznie). Zatwierdź zgodę i jesteś połączony. W razie potrzeby możesz ponownie uruchomić logowanie z menu `/mcp` w Gemini.
{% endtab %}

{% tab title="OpenAI Codex" %}
```bash
codex mcp add docbits \
  --url https://eu.api.docbits.com/v3/mcp \
  --oauth-resource https://eu.api.docbits.com/v3/mcp
```

Flaga `--oauth-resource` mówi Codex, aby dla tego serwera przeprowadził logowanie OAuth. Przy pierwszym użyciu Codex otwiera logowanie DocBits w przeglądarce; zatwierdź zgodę i jesteś połączony.
{% endtab %}
{% endtabs %}

## 3. Połącz się za pomocą klucza API (automatyzacja)

W przypadku agentów bez interfejsu, CI lub dowolnego środowiska bez przeglądarki pomiń OAuth i przekaż klucz API swojej organizacji w nagłówku `X-API-KEY`.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp \
  --header "X-API-KEY: <your-api-key>"
```
{% endtab %}

{% tab title="Gemini CLI" %}
Dodaj do `~/.gemini/settings.json`:

```json
{
  "mcpServers": {
    "docbits": {
      "httpUrl": "https://eu.api.docbits.com/v3/mcp",
      "headers": { "X-API-KEY": "<your-api-key>" }
    }
  }
}
```
{% endtab %}

{% tab title="OpenAI Codex" %}
Dodaj do `~/.codex/config.toml`:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
http_headers = { "X-API-KEY" = "<your-api-key>" }
```

Możesz też nie umieszczać klucza w pliku i odczytywać go ze zmiennej środowiskowej:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
env_http_headers = { "X-API-KEY" = "DOCBITS_API_KEY" }
```
{% endtab %}
{% endtabs %}

## Jak działa logowanie OAuth (pod maską)

DocBits implementuje standardowy przepływ **MCP OAuth 2.1**, więc każdy zgodny klient łączy się bez ręcznej konfiguracji:

1. Klient wywołuje endpoint MCP i otrzymuje odpowiedź `401` z nagłówkiem `WWW-Authenticate` wskazującym metadane chronionego zasobu.
2. Odczytuje `/.well-known/oauth-protected-resource`, który wskazuje serwer uwierzytelniania DocBits.
3. Odczytuje metadane serwera uwierzytelniania i **rejestruje się** dynamicznie (RFC 7591) — sekret klienta nie jest potrzebny.
4. Przeglądarka otwiera logowanie DocBits i ekran zgody. Jeśli jesteś już zalogowany w aplikacji internetowej, sesja jest wykorzystywana ponownie.
5. Klient wymienia kod autoryzacji (PKCE) na token dostępu i token odświeżania, a następnie wywołuje MCP.

{% hint style="warning" %}
Wylogowanie z **aplikacji internetowej DocBits nie rozłącza MCP** — MCP przechowuje własne tokeny i działa dalej, dopóki token odświeżania nie wygaśnie (30 dni) lub nie usuniesz serwera z klienta.
{% endhint %}

## Rozwiązywanie problemów

| Objaw | Przyczyna / rozwiązanie |
|---------|-------------|
| Strona logowania nigdy się nie otwiera | Sprawdź, czy host/region endpointu jest poprawny i osiągalny; niektóre środowiska bez interfejsu nie mogą otworzyć przeglądarki — użyj klucza API. |
| `401` po połączeniu | Token wygasł, a token odświeżania nie istnieje (tryb klucza API nigdy się nie odświeża) — połącz się ponownie / zaloguj ponownie. |
| Brak narzędzi | Twój użytkownik/klucz API może nie mieć uprawnień do tych funkcji; sprawdź swoją rolę w DocBits. |
| Błędne dane / region | Upewnij się, że użyto endpointu **Twojego** regionu (EU vs US). |
