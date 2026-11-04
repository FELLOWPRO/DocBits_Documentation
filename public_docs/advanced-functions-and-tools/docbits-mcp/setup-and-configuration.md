# Einrichtung & Konfiguration

Einen KI-Assistenten mit DocBits MCP zu verbinden erfordert einen Befehl und anschließend eine einmalige Anmeldung. Der empfohlene Weg zur Anmeldung ist **OAuth** – dieselbe DocBits-Anmeldung, die Sie bereits verwenden, in Ihrem Browser. Für Automatisierungen können Sie sich stattdessen mit einem API-Schlüssel verbinden.

## 1. Endpunkt wählen

Der MCP-Server liegt auf dem DocBits-API-Host. Verwenden Sie den Host für **Ihre Region (EU oder US)**:

| Umgebung | EU-Endpunkt | US-Endpunkt |
|-------------|-------------|-------------|
| Produktion | `https://eu.api.docbits.com/v3/mcp` | `https://us.api.docbits.com/v3/mcp` |
| Sandbox | `https://eu.sandbox.api.docbits.com/v3/mcp` | `https://us.sandbox.api.docbits.com/v3/mcp` |

{% hint style="info" %}
`api.docbits.com` ist der einzige Endpunkt, den Kunden verwenden. Wählen Sie immer die **Region, in der Ihre Organisation liegt** (EU oder US) – der MCP verweist die Anmeldung automatisch auf den passenden Auth-Server, Sie konfigurieren ihn nicht separat. Die Beispiele unten verwenden den EU-Produktionshost; setzen Sie Ihren eigenen ein.
{% endhint %}

## 2. Mit OAuth anmelden (empfohlen)

OAuth ist der einfache Weg – keine Geheimnisse zum Kopieren. Nachdem Sie den Server hinzugefügt haben, **öffnet die erste Verbindung die DocBits-Anmeldung in Ihrem Browser**, Sie bestätigen einen Zustimmungsdialog, und der Client ist verbunden.

**Was Sie bei jedem Client sehen:**

1. Der Client öffnet die DocBits-Anmeldeseite in Ihrem Browser.
2. Sie melden sich mit Ihrem DocBits-Konto an (wenn Sie bereits in der DocBits-Web-App angemeldet sind, wird die Sitzung wiederverwendet – keine erneute Anmeldung).
3. Sie bestätigen den Zustimmungsdialog („Authorize access“).
4. Der Browser übergibt dem Client ein Token, und die Verbindung steht.

OAuth stellt ein kurzlebiges Zugriffstoken (8 Std.) sowie ein Refresh-Token (30 Tage) aus, sodass der Client sich automatisch erneuert und verbunden bleibt – **Sie melden sich nur einmal an.**

{% hint style="success" %}
**Sie müssen in DocBits angemeldet sein – Ihre bestehende Sitzung wird wiederverwendet.** Die MCP-Anmeldung fragt nicht erneut nach Ihren Zugangsdaten, wenn Ihr Browser bereits eine DocBits-Sitzung hat. Sind Sie bereits in der DocBits-Web-App angemeldet, gelangen Sie **direkt zum Zustimmungsdialog**. Sind Sie nicht angemeldet, erscheint zuerst die DocBits-Anmeldeseite; nach einmaliger Anmeldung wird die Sitzung automatisch an den MCP übergeben.
{% endhint %}

<figure><img src="../../.gitbook/assets/docbits-mcp-login.png" alt="DocBits-Anmeldeseite"><figcaption><p>Noch nicht angemeldet – die DocBits-Anmeldeseite im Branding (Sie sehen sie nur, wenn Ihr Browser keine DocBits-Sitzung hat)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits-mcp-consent.png" alt="DocBits-Dialog zur Zugriffsfreigabe / Zustimmung"><figcaption><p>Bereits angemeldet – die Sitzung wird wiederverwendet, und Sie gelangen direkt zum Zustimmungsdialog. Bestätigen Sie, um zu verbinden; was der Client anfordert (Scope und Redirect), wird angezeigt.</p></figcaption></figure>

{% tabs %}
{% tab title="Claude Code" %}
```bash
# 1) add the server
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp

# 2) sign in (opens browser → DocBits login + consent → connected)
claude mcp login docbits
```

`claude mcp login docbits` ist der OAuth-Schritt. Nach erfolgreichem Abschluss prüfen Sie die Verbindung, indem Sie Claude fragen: *„Prüfe den Zustand der DocBits-API“*.
{% endtab %}

{% tab title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp
```

Gemini CLI erkennt den OAuth-Server automatisch. Bei der **ersten Verwendung** des Servers öffnet es die DocBits-Anmeldung in Ihrem Browser (dynamische Client-Registrierung und Token-Verwaltung werden für Sie erledigt). Bestätigen Sie die Zustimmung, und Sie sind verbunden. Falls nötig, können Sie die Anmeldung im Menü `/mcp` von Gemini erneut auslösen.
{% endtab %}

{% tab title="OpenAI Codex" %}
```bash
codex mcp add docbits \
  --url https://eu.api.docbits.com/v3/mcp \
  --oauth-resource https://eu.api.docbits.com/v3/mcp
```

Der Parameter `--oauth-resource` weist Codex an, die OAuth-Anmeldung für diesen Server auszuführen. Bei der ersten Verwendung öffnet Codex die DocBits-Anmeldung in Ihrem Browser; bestätigen Sie die Zustimmung, und Sie sind verbunden.
{% endtab %}
{% endtabs %}

## 3. Mit einem API-Schlüssel verbinden (Automatisierung)

Für Headless-Agenten, CI oder jede Umgebung ohne Browser überspringen Sie OAuth und übergeben den API-Schlüssel Ihrer Organisation als Header `X-API-KEY`.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp \
  --header "X-API-KEY: <your-api-key>"
```
{% endtab %}

{% tab title="Gemini CLI" %}
Fügen Sie in `~/.gemini/settings.json` Folgendes hinzu:

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
Fügen Sie in `~/.codex/config.toml` Folgendes hinzu:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
http_headers = { "X-API-KEY" = "<your-api-key>" }
```

Oder halten Sie den Schlüssel aus der Datei heraus und lesen Sie ihn aus der Umgebung:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
env_http_headers = { "X-API-KEY" = "DOCBITS_API_KEY" }
```
{% endtab %}
{% endtabs %}

## Wie die OAuth-Anmeldung funktioniert (unter der Haube)

DocBits implementiert den Standard-Ablauf **MCP OAuth 2.1**, sodass sich jeder konforme Client ohne manuelle Konfiguration verbinden kann:

1. Der Client ruft den MCP-Endpunkt auf und erhält ein `401` mit einem `WWW-Authenticate`-Header, der auf die Metadaten der geschützten Ressource verweist.
2. Er liest `/.well-known/oauth-protected-resource`, das den DocBits-Auth-Server benennt.
3. Er liest die Metadaten des Auth-Servers und **registriert sich dynamisch selbst** (RFC 7591) – ein Client-Secret ist nicht nötig.
4. Ihr Browser öffnet die DocBits-Anmeldung samt Zustimmung. Sind Sie bereits in der Web-App angemeldet, wird die Sitzung wiederverwendet.
5. Der Client tauscht den Autorisierungscode (PKCE) gegen ein Zugriffstoken und ein Refresh-Token und ruft den MCP auf.

{% hint style="warning" %}
Das Abmelden aus der DocBits-**Web-App trennt den MCP nicht** – der MCP hält eigene Tokens und funktioniert weiter, bis das Refresh-Token abläuft (30 Tage) oder Sie den Server aus Ihrem Client entfernen.
{% endhint %}

## Fehlerbehebung

| Symptom | Ursache / Lösung |
|---------|-------------|
| Die Anmeldeseite öffnet sich nie | Prüfen Sie, ob Host/Region des Endpunkts korrekt und erreichbar sind; manche Headless-Umgebungen können keinen Browser öffnen – verwenden Sie stattdessen einen API-Schlüssel. |
| `401` nach dem Verbinden | Das Token ist abgelaufen und es gibt kein Refresh-Token (der API-Schlüssel-Modus erneuert nie) – erneut verbinden / anmelden. |
| Tools fehlen | Ihrem Benutzer bzw. API-Schlüssel fehlt möglicherweise die Berechtigung für diese Funktionen; prüfen Sie Ihre DocBits-Rolle. |
| Falsche Daten / Region | Stellen Sie sicher, dass Sie den Endpunkt **Ihrer** Region (EU oder US) verwendet haben. |
