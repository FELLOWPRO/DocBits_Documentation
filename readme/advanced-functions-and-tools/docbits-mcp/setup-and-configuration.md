# Installation et configuration

Connecter un assistant IA à DocBits MCP demande une seule commande, puis une connexion unique. La méthode recommandée pour se connecter est **OAuth** — le même identifiant DocBits que vous utilisez déjà, dans votre navigateur. Pour l'automatisation, vous pouvez vous connecter avec une clé d'API à la place.

## 1. Choisir votre point de terminaison

Le serveur MCP se trouve sur l'hôte de l'API DocBits. Utilisez l'hôte de **votre région (UE ou États-Unis)** :

| Environnement | Point de terminaison UE | Point de terminaison États-Unis |
|-------------|-------------|-------------|
| Production | `https://eu.api.docbits.com/v3/mcp` | `https://us.api.docbits.com/v3/mcp` |
| Sandbox | `https://eu.sandbox.api.docbits.com/v3/mcp` | `https://us.sandbox.api.docbits.com/v3/mcp` |

{% hint style="info" %}
`api.docbits.com` est le point de terminaison unique utilisé par les clients. Choisissez toujours la **région où se trouve votre organisation** (UE ou États-Unis) — le MCP dirige automatiquement la connexion vers le serveur d'authentification correspondant, vous n'avez pas à le configurer séparément. Les exemples ci-dessous utilisent l'hôte de production UE ; remplacez-le par le vôtre.
{% endhint %}

## 2. Se connecter avec OAuth (recommandé)

OAuth est la voie simple — aucun secret à copier. Après l'ajout du serveur, la **première connexion ouvre la page de connexion DocBits dans votre navigateur**, vous validez un écran de consentement, et le client est connecté.

**Ce que vous verrez, pour chaque client :**

1. Le client ouvre la page de connexion DocBits dans votre navigateur.
2. Vous vous connectez avec votre compte DocBits (si vous êtes déjà connecté à l'application web DocBits, la session est réutilisée — pas de nouvelle connexion).
3. Vous validez l'écran de consentement (« Authorize access »).
4. Le navigateur transmet un jeton au client et la connexion est active.

OAuth émet un jeton d'accès de courte durée (8 h) ainsi qu'un jeton d'actualisation (30 jours), de sorte que le client se renouvelle automatiquement et reste connecté — **vous ne vous connectez qu'une seule fois.**

{% hint style="success" %}
**Vous devez être connecté à DocBits — votre session existante est réutilisée.** La connexion MCP ne vous redemande pas de vous connecter si votre navigateur possède déjà une session DocBits. Si vous êtes déjà connecté à l'application web DocBits, vous arrivez **directement à l'écran de consentement**. Si vous n'êtes pas connecté, la page de connexion DocBits s'affiche d'abord ; après une première connexion, la session est reprise automatiquement par le MCP.
{% endhint %}

<figure><img src="../../.gitbook/assets/docbits-mcp-login.png" alt="Page de connexion DocBits"><figcaption><p>Pas encore connecté — la page de connexion DocBits à votre image (vous ne la voyez que si votre navigateur n'a aucune session DocBits)</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/docbits-mcp-consent.png" alt="Écran d'autorisation d'accès / de consentement DocBits"><figcaption><p>Déjà connecté — la session est réutilisée et vous arrivez directement à l'écran de consentement. Validez pour vous connecter ; ce que demande le client (périmètre et redirection) est affiché.</p></figcaption></figure>

{% tabs %}
{% tab title="Claude Code" %}
```bash
# 1) add the server
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp

# 2) sign in (opens browser → DocBits login + consent → connected)
claude mcp login docbits
```

`claude mcp login docbits` est l'étape OAuth. Une fois qu'elle a réussi, confirmez en demandant à Claude : *« vérifie la santé de l'API DocBits »*.
{% endtab %}

{% tab title="Gemini CLI" %}
```bash
gemini mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp
```

Gemini CLI découvre automatiquement le serveur OAuth. **La première fois** qu'il utilise le serveur, il ouvre la connexion DocBits dans votre navigateur (l'enregistrement dynamique du client et la gestion des jetons sont pris en charge pour vous). Validez le consentement et vous êtes connecté. Vous pouvez relancer la connexion depuis le menu `/mcp` de Gemini si nécessaire.
{% endtab %}

{% tab title="OpenAI Codex" %}
```bash
codex mcp add docbits \
  --url https://eu.api.docbits.com/v3/mcp \
  --oauth-resource https://eu.api.docbits.com/v3/mcp
```

L'option `--oauth-resource` indique à Codex d'exécuter la connexion OAuth pour ce serveur. À la première utilisation, Codex ouvre la connexion DocBits dans votre navigateur ; validez le consentement et vous êtes connecté.
{% endtab %}
{% endtabs %}

## 3. Se connecter avec une clé d'API (automatisation)

Pour les agents sans interface, la CI ou tout environnement sans navigateur, ignorez OAuth et transmettez la clé d'API de votre organisation dans l'en-tête `X-API-KEY`.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.api.docbits.com/v3/mcp \
  --header "X-API-KEY: <your-api-key>"
```
{% endtab %}

{% tab title="Gemini CLI" %}
Ajoutez à `~/.gemini/settings.json` :

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
Ajoutez à `~/.codex/config.toml` :

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
http_headers = { "X-API-KEY" = "<your-api-key>" }
```

Ou gardez la clé hors du fichier et lisez-la depuis l'environnement :

```toml
[mcp_servers.docbits]
url = "https://eu.api.docbits.com/v3/mcp"
env_http_headers = { "X-API-KEY" = "DOCBITS_API_KEY" }
```
{% endtab %}
{% endtabs %}

## Comment fonctionne la connexion OAuth (en coulisses)

DocBits implémente le flux standard **MCP OAuth 2.1**, de sorte que tout client conforme se connecte sans configuration manuelle :

1. Le client appelle le point de terminaison MCP et reçoit un `401` avec un en-tête `WWW-Authenticate` pointant vers les métadonnées de la ressource protégée.
2. Il lit `/.well-known/oauth-protected-resource`, qui désigne le serveur d'authentification DocBits.
3. Il lit les métadonnées du serveur d'authentification et **s'enregistre lui-même** dynamiquement (RFC 7591) — aucun secret client n'est nécessaire.
4. Votre navigateur ouvre la connexion DocBits + le consentement. Si vous êtes déjà connecté à l'application web, la session est réutilisée.
5. Le client échange le code d'autorisation (PKCE) contre un jeton d'accès + un jeton d'actualisation et appelle le MCP.

{% hint style="warning" %}
Se déconnecter de l'**application web DocBits ne déconnecte pas le MCP** — le MCP détient ses propres jetons et continue de fonctionner jusqu'à l'expiration du jeton d'actualisation (30 jours) ou jusqu'à ce que vous supprimiez le serveur de votre client.
{% endhint %}

## Dépannage

| Symptôme | Cause / solution |
|---------|-------------|
| La page de connexion ne s'ouvre jamais | Vérifiez que l'hôte/la région du point de terminaison est correct et joignable ; certains environnements sans interface ne peuvent pas ouvrir de navigateur — utilisez plutôt une clé d'API. |
| `401` après la connexion | Le jeton a expiré et il n'y a pas de jeton d'actualisation (le mode clé d'API ne se renouvelle jamais) — reconnectez-vous. |
| Outils manquants | Votre utilisateur/clé d'API n'a peut-être pas l'autorisation pour ces fonctionnalités ; vérifiez votre rôle DocBits. |
| Mauvaises données / mauvaise région | Assurez-vous d'avoir utilisé le point de terminaison de **votre** région (UE ou États-Unis). |
