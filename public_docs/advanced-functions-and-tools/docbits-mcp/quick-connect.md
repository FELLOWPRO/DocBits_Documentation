# Quick Connect

Connectez votre assistant IA à DocBits en trois étapes : choisissez votre environnement, copiez une commande, connectez-vous une seule fois. Aucune API key n'est nécessaire.

## 1. Choisissez votre environnement

Utilisez l'endpoint correspondant à la **région** (EU ou US) et à l'**environnement** (Sandbox ou Production) de votre organisation.

| Environnement | Région | Endpoint |
| --- | --- | --- |
| Sandbox | EU | `https://eu.sandbox.api.docbits.com/v3/mcp` |
| Sandbox | US | `https://us.sandbox.api.docbits.com/v3/mcp` |
| Production | EU | `https://eu.api.docbits.com/v3/mcp` |
| Production | US | `https://us.api.docbits.com/v3/mcp` |

{% hint style="warning" %}
L'assistant utilise les autorisations du compte avec lequel vous vous connectez et peut modifier des données. Les modifications en **Production** affectent vos documents en production. Testez d'abord les nouveaux prompts dans Sandbox.
{% endhint %}

## 2. Connectez-vous en un clic ou avec une commande

Utilisez les boutons pour ajouter le serveur à **Cursor** ou **VS Code**, ou copiez la commande pour votre client de terminal. Chaque environnement utilise son propre nom de serveur, vous pouvez donc connecter Sandbox et Production côte à côte sans les confondre.

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

Pour **Claude Desktop** et **claude.ai**, ajoutez plutôt un connecteur personnalisé : ouvrez les paramètres des connecteurs, choisissez **Add custom connector** et collez l'endpoint indiqué dans le tableau.

## 3. Connectez-vous une seule fois

La première connexion ouvre la page de connexion DocBits dans votre navigateur. Si vous êtes déjà connecté à DocBits, vous accédez directement à l'écran de consentement. Approuvez-le et la connexion est établie.

{% tabs %}
{% tab title="Claude Code" %}
Lancez Claude Code, exécutez `/mcp`, sélectionnez le serveur DocBits et choisissez **Authenticate**.
{% endtab %}

{% tab title="OpenAI Codex" %}
Remplacez `docbits-sandbox-eu` par le nom du serveur que vous avez ajouté :

```bash
codex mcp login docbits-sandbox-eu
```
{% endtab %}

{% tab title="Gemini CLI" %}
Gemini CLI ouvre la page de connexion lors de la première utilisation du serveur. Vous pouvez la relancer depuis le menu `/mcp`.
{% endtab %}
{% endtabs %}

Vous ne vous connectez qu'une seule fois. Le client renouvelle son accès automatiquement pour 30 jours d'utilisation.

## 4. Vérifiez la connexion

Démarrez une nouvelle conversation et envoyez ce prompt :

```text
Read only. Call get_api_info and get_current_user. Show the API host and my
organization name. Do not change any setting and do not process documents.
```

L'hôte de l'API dans la réponse doit correspondre à l'endpoint que vous avez choisi, par exemple `eu.sandbox.api.docbits.com` pour Sandbox EU. Sinon, supprimez le serveur et ajoutez-le à nouveau avec le bon endpoint.

## Étapes suivantes

* [Exemples](examples.md) : prompts prêts à l'emploi pour les documents, la recherche et les analyses
* [Configurer DocBits avec Claude ou Codex](configuration-with-claude-or-codex.md) : modifier les paramètres en toute sécurité avec aperçu, confirmation et annulation
* [Configuration et installation](setup-and-configuration.md) : connexion par API key pour l'automatisation et fonctionnement de la connexion OAuth

## Dépannage

| Symptôme | Solution |
| --- | --- |
| La page de connexion ne s'ouvre pas | Relancez l'étape de connexion. Sur une machine sans navigateur, utilisez une API key comme décrit dans [Configuration et installation](setup-and-configuration.md). |
| `401` après la connexion | La connexion a expiré. Authentifiez à nouveau le serveur. |
| L'assistant affiche les données d'une mauvaise organisation | Vous avez choisi la mauvaise région ou le mauvais environnement. Supprimez le serveur et ajoutez le bon endpoint. |
| Des outils sont manquants | Votre rôle DocBits ne permet pas ces fonctionnalités. Contactez votre administrateur. |
