# Quick Connect

Połącz swojego asystenta AI z DocBits w trzech krokach: wybierz środowisko, skopiuj jedno polecenie, zaloguj się raz. Nie potrzebujesz API key.

## 1. Wybierz środowisko

Użyj endpointu odpowiedniego dla **regionu** (EU lub US) i **środowiska** (Sandbox lub Production), w którym działa Twoja organizacja.

| Środowisko | Region | Endpoint |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | EU | `https://eu.api.docbits.com/v3/mcp` |
| Production | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
Asystent działa z uprawnieniami konta, na którym się logujesz, i może zmieniać dane. Zmiany w **Production** wpływają na Twoje produkcyjne dokumenty. Nowe prompty wypróbuj najpierw w Sandbox.
{% endhint %}

## 2. Połącz jednym kliknięciem lub jednym poleceniem

Użyj przycisków, aby dodać serwer do **Cursor** lub **VS Code**, albo skopiuj polecenie dla swojego klienta terminala. Każde środowisko ma własną nazwę serwera, więc możesz połączyć Sandbox i Production obok siebie bez ryzyka pomylenia.

{% tabs %}
{% tab title="Sandbox EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-sandbox-eu https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-sandbox-eu --url https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-sandbox-eu https://eu.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Sandbox US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-sandbox-us https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-sandbox-us --url https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-sandbox-us https://us.sandbox.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Production EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-prod-eu https://eu.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-prod-eu --url https://eu.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-prod-eu https://eu.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}

{% tab title="Production US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Add to Cursor</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Add to VS Code</a>

{% code title="Claude Code" %}
```bash
claude mcp add --transport http docbits-prod-us https://us.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="OpenAI Codex" %}
```bash
codex mcp add docbits-prod-us --url https://us.api.docbits.com/v3/mcp
```
{% endcode %}

{% code title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits-prod-us https://us.api.docbits.com/v3/mcp
```
{% endcode %}
{% endtab %}
{% endtabs %}

Dla **Claude Desktop** i **claude.ai** dodaj zamiast tego własny connector: otwórz ustawienia connectorów, wybierz **Add custom connector** i wklej endpoint z tabeli.

## 3. Zaloguj się raz

Pierwsze połączenie otwiera logowanie DocBits w Twojej przeglądarce. Jeśli jesteś już zalogowany do DocBits, przejdziesz od razu do ekranu zgody. Zatwierdź go i połączenie jest gotowe.

{% tabs %}
{% tab title="Claude Code" %}
Uruchom Claude Code, wpisz `/mcp`, wybierz serwer DocBits i wybierz **Authenticate**.
{% endtab %}

{% tab title="OpenAI Codex" %}
Zastąp `docbits-sandbox-eu` nazwą serwera, który dodałeś:

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
Gemini CLI otwiera logowanie przy pierwszym użyciu serwera. Możesz uruchomić je ponownie z menu `/mcp`.
{% endtab %}
{% endtabs %}

Logujesz się tylko raz. Klient automatycznie odnawia dostęp na 30 dni użytkowania.

## 4. Sprawdź połączenie

Rozpocznij nową rozmowę i wyślij ten prompt:

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

Host API w odpowiedzi musi odpowiadać wybranemu endpointowi, na przykład `eu.sandbox.api.docbits.com` dla Sandbox EU. Jeśli tak nie jest, usuń serwer i dodaj go ponownie z właściwym endpointem.

## Następne kroki

* [Przykłady](examples.md): gotowe prompty do dokumentów, wyszukiwania i analityki
* [Konfiguracja DocBits z Claude lub Codex](configuration-with-claude-or-codex.md): bezpieczna zmiana ustawień z podglądem, potwierdzeniem i cofnięciem
* [Konfiguracja i ustawienia](setup-and-configuration.md): logowanie przez API key do automatyzacji i sposób działania logowania OAuth

## Rozwiązywanie problemów

| Objaw | Rozwiązanie |
| --- | --- |
| Strona logowania się nie otwiera | Powtórz krok logowania. Na komputerze bez przeglądarki użyj API key, jak opisano w [Konfiguracja i ustawienia](setup-and-configuration.md). |
| `401` po połączeniu | Logowanie wygasło. Uwierzytelnij serwer ponownie. |
| Asystent pokazuje dane z niewłaściwej organizacji | Wybrano niewłaściwy region lub środowisko. Usuń serwer i dodaj właściwy endpoint. |
| Brakuje narzędzi | Twoja rola w DocBits nie pozwala na te funkcje. Zapytaj administratora. |
