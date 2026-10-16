# DocFlow MCP

DocFlow expose un serveur **Model Context Protocol (MCP)** qui permet aux assistants IA de gérer les workflows et les cartes partenaires de manière programmatique. Tout client compatible MCP — Claude Code, Claude Desktop, OpenAI Codex ou des intégrations personnalisées — peut se connecter et utiliser ces outils.

## Que pouvez-vous faire ?

Avec DocFlow MCP, vous pouvez :

- **Lister, créer, mettre à jour et supprimer** des workflows avancés
- **Tester des workflows** avec des documents réels ou simulés
- **Créer des cartes personnalisées** à l'aide du SDK de cartes partenaires
- **Valider, tester, approuver et gérer** les soumissions de cartes partenaires
- **Importer des cartes** directement depuis des dépôts GitHub

## Aperçu des outils

DocFlow MCP fournit **18 outils** répartis en quatre catégories :

### Gestion des workflows

| Outil | Description |
|-------|-------------|
| `list_workflows` | Lister tous les workflows de l'organisation actuelle |
| `get_workflow` | Obtenir les détails d'un workflow spécifique par ID |
| `delete_workflow` | Supprimer un workflow par ID |

### Test des workflows

| Outil | Description |
|-------|-------------|
| `test_advanced_workflow` | Tester l'exécution d'un workflow avancé avec un document optionnel |
| `list_test_scenarios` | Lister tous les scénarios de test de workflow |
| `list_cards` | Lister les cartes/actions de workflow disponibles |

### Gestion du SDK de cartes

| Outil | Description |
|-------|-------------|
| `sdk_list_submissions` | Lister toutes les soumissions de cartes partenaires |
| `sdk_get_submission_status` | Obtenir le statut de validation d'une soumission |
| `sdk_approve_card` | Approuver une carte partenaire validée (admin) |
| `sdk_reject_card` | Rejeter une soumission de carte partenaire (admin) |
| `sdk_delete_submission` | Désactiver ou supprimer une soumission (admin) |
| `sdk_list_cards_picker` | Lister toutes les cartes activées avec les indicateurs de rôle |

### Développement avec le SDK de cartes

| Outil | Description |
|-------|-------------|
| `sdk_create_card` | Créer une nouvelle carte partenaire à partir du code source |
| `sdk_validate_card` | Exécuter une validation en 5 étapes sans enregistrer |
| `sdk_test_card` | Exécuter une carte dans un environnement sandboxé |
| `sdk_import_github` | Importer une application partenaire depuis GitHub |

## Pour commencer

1. [Configurez votre client MCP](setup-and-configuration.md)
2. Découvrez les [Outils de workflow](workflow-tools.md)
3. Explorez les [Outils du SDK de cartes](card-sdk-tools.md)
4. Suivez les [Exemples](examples.md) de bout en bout

{% hint style="info" %}
DocFlow MCP utilise le transport **Streamable HTTP**. Le point de terminaison du serveur est `/api/mcp/` sur votre hôte API DocBits.
{% endhint %}
