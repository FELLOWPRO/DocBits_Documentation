# Schnellverbindung

Verbinden Sie Ihren KI-Assistenten in drei Schritten mit DocBits: Umgebung wählen, einen Befehl kopieren, einmal anmelden. Ein API-Schlüssel ist nicht nötig.

## 1. Umgebung wählen

Verwenden Sie den Endpunkt für die **Region** (EU oder US) und die **Umgebung** (Sandbox oder Produktion), in der Ihre Organisation liegt.

| Umgebung | Region | Endpunkt |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Produktion | EU | `https://eu.api.docbits.com/v3/mcp` |
| Produktion | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
Der Assistent arbeitet mit den Berechtigungen des Kontos, mit dem Sie sich anmelden, und kann Daten ändern. Änderungen in **Produktion** wirken sich auf Ihre produktiven Dokumente aus. Probieren Sie neue Prompts zuerst in der Sandbox aus.
{% endhint %}

## 2. Mit einem Klick oder einem Befehl verbinden

Nutzen Sie die Schaltflächen, um den Server in **Cursor** oder **VS Code** hinzuzufügen, oder kopieren Sie den Befehl für Ihren Terminal-Client. Jede Umgebung hat einen eigenen Servernamen, sodass Sie Sandbox und Produktion nebeneinander verbinden können, ohne sie zu verwechseln.

{% tabs %}
{% tab title="Sandbox EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Zu Cursor hinzufügen</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Zu VS Code hinzufügen</a>

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
<a href="https://cursor.com/en/install-mcp?name=docbits-sandbox-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5zYW5kYm94LmFwaS5kb2NiaXRzLmNvbS92My9tY3AifQ%3D%3D" class="button primary">Zu Cursor hinzufügen</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-sandbox-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.sandbox.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Zu VS Code hinzufügen</a>

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

{% tab title="Produktion EU" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-eu&config=eyJ1cmwiOiAiaHR0cHM6Ly9ldS5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Zu Cursor hinzufügen</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-eu&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Feu.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Zu VS Code hinzufügen</a>

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

{% tab title="Produktion US" %}
<a href="https://cursor.com/en/install-mcp?name=docbits-prod-us&config=eyJ1cmwiOiAiaHR0cHM6Ly91cy5hcGkuZG9jYml0cy5jb20vdjMvbWNwIn0%3D" class="button primary">Zu Cursor hinzufügen</a> <a href="https://vscode.dev/redirect/mcp/install?name=docbits-prod-us&config=%7B%22type%22%3A%22http%22%2C%22url%22%3A%22https%3A%2F%2Fus.api.docbits.com%2Fv3%2Fmcp%22%7D" class="button secondary">Zu VS Code hinzufügen</a>

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

Für **Claude Desktop** und **claude.ai** fügen Sie stattdessen einen benutzerdefinierten Connector hinzu: Öffnen Sie die Connector-Einstellungen, wählen Sie **Benutzerdefinierten Connector hinzufügen** und fügen Sie den Endpunkt aus der Tabelle ein.

## 3. Einmal anmelden

Die erste Verbindung öffnet die DocBits-Anmeldung in Ihrem Browser. Sind Sie bereits bei DocBits angemeldet, gelangen Sie direkt zum Zustimmungsdialog. Bestätigen Sie ihn, und Sie sind verbunden.

{% tabs %}
{% tab title="Claude Code" %}
Starten Sie Claude Code, führen Sie `/mcp` aus, wählen Sie den DocBits-Server und dann **Authenticate**.
{% endtab %}

{% tab title="OpenAI Codex" %}
Ersetzen Sie `docbits-sandbox-eu` durch den Servernamen, den Sie hinzugefügt haben:

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
Gemini CLI öffnet die Anmeldung bei der ersten Nutzung des Servers. Über das Menü `/mcp` können Sie sie erneut starten.
{% endtab %}
{% endtabs %}

Sie melden sich nur einmal an. Der Client erneuert den Zugriff bei Nutzung automatisch für 30 Tage.

## 4. Verbindung prüfen

Starten Sie eine neue Unterhaltung und senden Sie diesen Prompt:

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

Der API-Host in der Antwort muss zum gewählten Endpunkt passen, zum Beispiel `eu.sandbox.api.docbits.com` für Sandbox EU. Wenn nicht, entfernen Sie den Server und fügen Sie ihn mit dem richtigen Endpunkt erneut hinzu.

## Nächste Schritte

* [Beispiele](examples.md): fertige Prompts für Dokumente, Suche und Analysen
* [DocBits mit Claude oder Codex konfigurieren](configuration-with-claude-or-codex.md): Einstellungen sicher ändern mit Vorschau, Bestätigung und Rückgängig
* [Einrichtung & Konfiguration](setup-and-configuration.md): Anmeldung per API-Schlüssel für Automatisierung und Funktionsweise der OAuth-Anmeldung

## Fehlerbehebung

| Symptom | Lösung |
| --- | --- |
| Die Anmeldeseite öffnet sich nicht | Führen Sie den Anmeldeschritt erneut aus. Auf einem Rechner ohne Browser verwenden Sie einen API-Schlüssel wie unter [Einrichtung & Konfiguration](setup-and-configuration.md) beschrieben. |
| `401` nach dem Verbinden | Die Anmeldung ist abgelaufen. Authentifizieren Sie den Server erneut. |
| Der Assistent zeigt Daten einer falschen Organisation | Sie haben die falsche Region oder Umgebung gewählt. Entfernen Sie den Server und fügen Sie den richtigen Endpunkt hinzu. |
| Tools fehlen | Ihre DocBits-Rolle erlaubt diese Funktionen nicht. Fragen Sie Ihren Administrator. |
