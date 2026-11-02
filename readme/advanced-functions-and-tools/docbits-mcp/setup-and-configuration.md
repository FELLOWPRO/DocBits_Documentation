# Configurazione e setup

Collegare un assistente AI a DocBits MCP richiede un solo comando, seguito da un accesso una tantum. Il metodo di accesso consigliato è **OAuth**: lo stesso login DocBits che già utilizzi, nel tuo browser. Per l'automazione puoi invece collegarti con una chiave API.

## 1. Scegli il tuo endpoint

Il server MCP si trova sull'host dell'API DocBits. Utilizza l'host della **tua regione (UE o USA)**:

| Ambiente | Endpoint UE | Endpoint USA |
|-------------|-------------|-------------|
| Produzione | `https://eu.api.docbits.com/v3/mcp` | `https://us.api.docbits.com/v3/mcp` |
| Sandbox | `https://eu.sandbox.api.docbits.com/v3/mcp` | `https://us.sandbox.api.docbits.com/v3/mcp` |

{% hint style="info" %}
`api.docbits.com` è l'unico endpoint utilizzato dai clienti. Scegli sempre la **regione in cui risiede la tua organizzazione** (UE o USA): l'MCP indirizza automaticamente il login al server di autenticazione corrispondente, senza che tu debba configurarlo separatamente. Gli esempi seguenti usano l'host di produzione UE; sostituiscilo con il tuo.
{% endhint %}

## 2. Accedi con OAuth (consigliato)

OAuth è la via più semplice: nessun segreto da copiare. Dopo aver aggiunto il server, la **prima connessione apre il login DocBits nel browser**, approvi una schermata di consenso e il client è collegato.

**Cosa vedrai, per ogni client:**

1. Il client apre la pagina di login DocBits nel browser.
2. Accedi con il tuo account DocBits (se hai già effettuato l'accesso all'app web DocBits, la sessione viene riutilizzata: nessun nuovo login).
3. Approvi la schermata di consenso ("Authorize access").
4. Il browser consegna un token al client e la connessione è attiva.

OAuth emette un token di accesso a breve durata (8 h) più un token di refresh (30 giorni), quindi il client si aggiorna automaticamente e resta collegato: **devi accedere una sola volta.**

{% hint style="success" %}
**Devi aver effettuato l'accesso a DocBits: la tua sessione esistente viene riutilizzata.** Il login MCP non ti chiede di accedere di nuovo se il tuo browser ha già una sessione DocBits. Se hai già effettuato l'accesso all'app web DocBits, passi **direttamente alla schermata di consenso**. Se non hai effettuato l'accesso, compare prima la pagina di accesso di DocBits; dopo aver effettuato l'accesso una volta, la sessione viene trasferita automaticamente all'MCP.
{% endhint %}

<figure><img src="../../.gitbook/assets/docbits-mcp-login.png" alt="Pagina di accesso a DocBits"><figcaption><p>Accesso non ancora effettuato: la pagina di accesso DocBits con il marchio aziendale (la vedi solo se il tuo browser non ha una sessione DocBits)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits-mcp-consent.png" alt="Schermata di autorizzazione dell'accesso / consenso di DocBits"><figcaption><p>Accesso già effettuato: la sessione viene riutilizzata e passi direttamente alla schermata di consenso. Approva per collegarti; vengono mostrati i permessi richiesti dal client (scope e redirect).</p></figcaption></figure>

{% tabs %}
{% tab title="Claude Code" %}
```bash
# 1) add the server
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp

# 2) sign in (opens browser → DocBits login + consent → connected)
claude mcp login docbits
```

`claude mcp login docbits` è il passaggio OAuth. Dopo il successo, verifica chiedendo a Claude: *"controlla lo stato di salute dell'API DocBits"*.
{% endtab %}

{% tab title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp
```

Gemini CLI rileva automaticamente il server OAuth. **La prima volta** che usa il server, apre il login DocBits nel browser (la registrazione dinamica del client e la gestione dei token sono gestite per te). Approva il consenso e sei collegato. Se necessario, puoi riattivare l'accesso dal menu `/mcp` in Gemini.
{% endtab %}

{% tab title="OpenAI Codex" %}
```bash
codex mcp add docbits \
  --url https://eu.api.docbits.com/v3/mcp \
  --oauth-resource https://eu.api.docbits.com/v3/mcp
```

Il flag `--oauth-resource` indica a Codex di eseguire il login OAuth per questo server. Al primo utilizzo Codex apre il login DocBits nel browser; approva il consenso e sei collegato.
{% endtab %}
{% endtabs %}

## 3. Collegarsi con una chiave API (automazione)

Per agenti headless, CI o qualsiasi ambiente senza browser, salta OAuth e passa la chiave API della tua organizzazione come header `X-API-KEY`.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp \
  --header "X-API-KEY: <your-api-key>"
```
{% endtab %}

{% tab title="Gemini CLI" %}
Aggiungi a `~/.gemini/settings.json`:

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
Aggiungi a `~/.codex/config.toml`:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
http_headers = { "X-API-KEY" = "<your-api-key>" }
```

Oppure tieni la chiave fuori dal file e leggila dall'ambiente:

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
env_http_headers = { "X-API-KEY" = "DOCBITS_API_KEY" }
```
{% endtab %}
{% endtabs %}

## Come funziona il login OAuth (sotto il cofano)

DocBits implementa il flusso standard **MCP OAuth 2.1**, quindi qualsiasi client conforme si collega senza configurazione manuale:

1. Il client chiama l'endpoint MCP e riceve un `401` con un header `WWW-Authenticate` che punta ai metadati della risorsa protetta.
2. Legge `/.well-known/oauth-protected-resource`, che indica il server di autenticazione DocBits.
3. Legge i metadati del server di autenticazione e si **registra** dinamicamente (RFC 7591): non serve alcun client secret.
4. Il tuo browser apre il login DocBits + consenso. Se hai già effettuato l'accesso all'app web, la sessione viene riutilizzata.
5. Il client scambia il codice di autorizzazione (PKCE) con un token di accesso + un token di refresh e chiama l'MCP.

{% hint style="warning" %}
Disconnettersi dall'**app web DocBits non disconnette l'MCP**: l'MCP possiede i propri token e continua a funzionare finché il token di refresh non scade (30 giorni) o finché non rimuovi il server dal tuo client.
{% endhint %}

## Risoluzione dei problemi

| Sintomo | Causa / soluzione |
|---------|-------------|
| La pagina di login non si apre | Verifica che l'host/la regione dell'endpoint siano corretti e raggiungibili; alcuni ambienti headless non possono aprire un browser: utilizza invece una chiave API. |
| `401` dopo la connessione | Il token è scaduto e non c'è un token di refresh (la modalità con chiave API non effettua mai il refresh): ricollegati / ripeti il login. |
| Strumenti mancanti | Il tuo utente/la tua chiave API potrebbe non avere l'autorizzazione per quelle funzioni; controlla il tuo ruolo DocBits. |
| Dati / regione errati | Assicurati di aver usato l'endpoint della **tua** regione (UE o USA). |
