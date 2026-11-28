# Quick Connect

Verbind je AI-assistent in drie stappen met DocBits: kies je omgeving, kopieer één commando, meld je één keer aan. Een API key is niet nodig.

## 1. Kies je omgeving

Gebruik het endpoint voor de **regio** (EU of US) en de **omgeving** (Sandbox of Production) waarin je organisatie zit.

| Omgeving | Regio | Endpoint |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | EU | `https://eu.api.docbits.com/v3/mcp` |
| Production | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
De assistent werkt met de rechten van het account waarmee je aanmeldt, en kan gegevens wijzigen. Wijzigingen in **Production** hebben invloed op je live documenten. Probeer nieuwe prompts eerst in Sandbox.
{% endhint %}

## 2. Verbinden met één klik of één commando

Gebruik de knoppen om de server toe te voegen aan **Cursor** of **VS Code**, of kopieer het commando voor je terminalclient. Elke omgeving heeft een eigen servernaam, zodat je Sandbox en Production naast elkaar kunt verbinden zonder ze door elkaar te halen.

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

Voor **Claude Desktop** en **claude.ai** voeg je in plaats daarvan een custom connector toe: open de connectorinstellingen, kies **Add custom connector** en plak het endpoint uit de tabel.

## 3. Één keer aanmelden

De eerste verbinding opent de DocBits-login in je browser. Ben je al aangemeld bij DocBits, dan ga je direct naar het toestemmingsscherm. Bevestig het en je bent verbonden.

{% tabs %}
{% tab title="Claude Code" %}
Start Claude Code, voer `/mcp` uit, selecteer de DocBits-server en kies **Authenticate**.
{% endtab %}

{% tab title="OpenAI Codex" %}
Vervang `docbits-sandbox-eu` door de servernaam die je hebt toegevoegd:

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
Gemini CLI opent de login de eerste keer dat het de server gebruikt. Je kunt die opnieuw starten via het menu `/mcp`.
{% endtab %}
{% endtabs %}

Je meldt je maar één keer aan. De client verlengt de toegang automatisch voor 30 dagen gebruik.

## 4. Verbinding controleren

Start een nieuw gesprek en stuur deze prompt:

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

De API-host in het antwoord moet overeenkomen met het endpoint dat je hebt gekozen, bijvoorbeeld `eu.sandbox.api.docbits.com` voor Sandbox EU. Is dat niet zo, verwijder dan de server en voeg hem opnieuw toe met het juiste endpoint.

## Volgende stappen

* [Voorbeelden](examples.md): kant-en-klare prompts voor documenten, zoeken en analyses
* [DocBits configureren met Claude of Codex](configuration-with-claude-or-codex.md): instellingen veilig wijzigen met preview, bevestigen en ongedaan maken
* [Installatie & configuratie](setup-and-configuration.md): aanmelden met een API key voor automatisering en hoe de OAuth-aanmelding werkt

## Problemen oplossen

| Symptoom | Oplossing |
| --- | --- |
| De inlogpagina opent niet | Voer de aanmeldstap opnieuw uit. Op een machine zonder browser gebruik je een API key zoals beschreven in [Installatie & configuratie](setup-and-configuration.md). |
| `401` na het verbinden | De aanmelding is verlopen. Authenticeer de server opnieuw. |
| De assistent toont gegevens van de verkeerde organisatie | Je hebt de verkeerde regio of omgeving gekozen. Verwijder de server en voeg het juiste endpoint toe. |
| Tools ontbreken | Je DocBits-rol staat die functies niet toe. Vraag je beheerder. |
