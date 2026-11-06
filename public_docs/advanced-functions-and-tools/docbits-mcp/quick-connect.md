# Quick Connect

Connect your AI assistant to DocBits in three steps: pick your environment, copy one command, sign in once. No API key is needed.

## 1. Pick your environment

Use the endpoint for the **region** (EU or US) and **environment** (Sandbox or Production) your organization lives in.

| Environment | Region | Endpoint |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | EU | `https://eu.api.docbits.com/v3/mcp` |
| Production | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
The assistant works with the permissions of the account you sign in with, and it can change data. Changes in **Production** affect your live documents. Try new prompts in Sandbox first.
{% endhint %}

## 2. Connect with one click or one command

Use the buttons to add the server to **Cursor** or **VS Code**, or copy the command for your terminal client. Each environment uses its own server name, so you can connect Sandbox and Production side by side without mixing them up.

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

For **Claude Desktop** and **claude.ai**, add a custom connector instead: open the connector settings, choose **Add custom connector**, and paste the endpoint from the table.

## 3. Sign in once

The first connection opens the DocBits login in your browser. If you are already signed in to DocBits, you go straight to the consent screen. Approve it and you are connected.

{% tabs %}
{% tab title="Claude Code" %}
Start Claude Code, run `/mcp`, select the DocBits server and choose **Authenticate**.
{% endtab %}

{% tab title="OpenAI Codex" %}
Replace `docbits-sandbox-eu` with the server name you added:

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
Gemini CLI opens the login the first time it uses the server. You can start it again from the `/mcp` menu.
{% endtab %}
{% endtabs %}

You only sign in once. The client renews its access automatically for 30 days of use.

## 4. Check the connection

Start a new conversation and send this prompt:

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

The API host in the answer must match the endpoint you chose, for example `eu.sandbox.api.docbits.com` for Sandbox EU. If it does not, remove the server and add it again with the right endpoint.

## Next steps

* [Examples](examples.md): ready-made prompts for documents, search and analytics
* [Configure DocBits with Claude or Codex](configuration-with-claude-or-codex.md): change settings safely with preview, confirm and undo
* [Setup & Configuration](setup-and-configuration.md): API key login for automation and how the OAuth sign-in works

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| The login page does not open | Run the sign-in step again. On a machine without a browser, use an API key as described in [Setup & Configuration](setup-and-configuration.md). |
| `401` after connecting | The sign-in expired. Authenticate the server again. |
| The assistant shows data from the wrong organization | You chose the wrong region or environment. Remove the server and add the right endpoint. |
| Tools are missing | Your DocBits role does not allow those features. Ask your administrator. |
