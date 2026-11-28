# Quick Connect

Colleghi il suo assistente AI a DocBits in tre passaggi: scelga l'ambiente, copi un comando, effettui l'accesso una sola volta. Non serve alcuna API key.

## 1. Scelga l'ambiente

Usi l'endpoint per la **regione** (EU o US) e l'**ambiente** (Sandbox o Production) in cui si trova la sua organizzazione.

| Ambiente | Regione | Endpoint |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | EU | `https://eu.api.docbits.com/v3/mcp` |
| Production | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
L'assistente opera con i permessi dell'account con cui effettua l'accesso e può modificare i dati. Le modifiche in **Production** interessano i suoi documenti reali. Provi prima i nuovi prompt in Sandbox.
{% endhint %}

## 2. Si connetta con un clic o un comando

Usi i pulsanti per aggiungere il server a **Cursor** o **VS Code**, oppure copi il comando per il suo client da terminale. Ogni ambiente ha il proprio nome del server, così può collegare Sandbox e Production affiancati senza confonderli.

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

Per **Claude Desktop** e **claude.ai**, aggiunga invece un connettore personalizzato: apra le impostazioni dei connettori, scelga **Add custom connector** e incolli l'endpoint dalla tabella.

## 3. Effettui l'accesso una volta

La prima connessione apre l'accesso a DocBits nel suo browser. Se ha già effettuato l'accesso a DocBits, arriva direttamente alla schermata di consenso. La approvi e la connessione è attiva.

{% tabs %}
{% tab title="Claude Code" %}
Avvii Claude Code, esegua `/mcp`, selezioni il server DocBits e scelga **Authenticate**.
{% endtab %}

{% tab title="OpenAI Codex" %}
Sostituisca `docbits-sandbox-eu` con il nome del server che ha aggiunto:

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
Gemini CLI apre l'accesso la prima volta che usa il server. Può avviarlo di nuovo dal menu `/mcp`.
{% endtab %}
{% endtabs %}

Effettua l'accesso una sola volta. Il client rinnova l'accesso automaticamente per 30 giorni di utilizzo.

## 4. Verifichi la connessione

Avvii una nuova conversazione e invii questo prompt:

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

L'host API nella risposta deve corrispondere all'endpoint scelto, ad esempio `eu.sandbox.api.docbits.com` per Sandbox EU. In caso contrario, rimuova il server e lo aggiunga di nuovo con l'endpoint corretto.

## Prossimi passaggi

* [Esempi](examples.md): prompt pronti per documenti, ricerca e analisi
* [Configurare DocBits con Claude o Codex](configuration-with-claude-or-codex.md): modificare le impostazioni in sicurezza con anteprima, conferma e annullamento
* [Setup e configurazione](setup-and-configuration.md): accesso con API key per l'automazione e funzionamento dell'accesso OAuth

## Risoluzione dei problemi

| Sintomo | Soluzione |
| --- | --- |
| La pagina di accesso non si apre | Esegua di nuovo il passaggio di accesso. Su una macchina senza browser, usi una API key come descritto in [Setup e configurazione](setup-and-configuration.md). |
| `401` dopo la connessione | L'accesso è scaduto. Autentichi di nuovo il server. |
| L'assistente mostra dati dell'organizzazione sbagliata | Ha scelto la regione o l'ambiente sbagliato. Rimuova il server e aggiunga l'endpoint corretto. |
| Mancano dei tool | Il suo ruolo DocBits non consente queste funzioni. Si rivolga al suo amministratore. |
