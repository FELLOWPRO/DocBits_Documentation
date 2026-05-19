# DocFlow MCP

DocFlow expose un serveur **Model Context Protocol (MCP)** qui permet aux assistants IA de gérer les workflows et les cartes partenaires de manière programmatique. Tout client compatible MCP — Claude Code, Claude Desktop, OpenAI Codex ou des intégrations personnalisées — peut se connecter et utiliser ces outils.

## Que pouvez-vous faire ?

Avec DocFlow MCP, vous pouvez :

- **Lister, créer, mettre à jour et supprimer** des workflows avancés
- **Tester les workflows** avec des documents réels ou fictifs
- **Construire des cartes personnalisées** avec le Partner Card SDK
- **Valider, tester, approuver et gérer** les soumissions de cartes partenaires
- **Importer des cartes** directement depuis des dépôts GitHub

## Vue d'ensemble des outils

DocFlow MCP regroupe ses outils dans les catégories suivantes. La plupart des outils Workflow et Card SDK reflètent des endpoints REST existants — consultez la référence d'API pour ceux-ci. Les catégories ci-dessous couvrent la surface spécifique à MCP et les concepts de workflow nécessaires à son utilisation.

### Gestion des workflows

| Outil | Description |
|------|-------------|
| `list_workflows` | Lister tous les workflows de l'organisation courante |
| `get_workflow` | Obtenir les détails d'un workflow spécifique par ID |
| `create_advanced_workflow` | Créer un nouveau workflow avancé avec nœuds et arêtes |
| `update_advanced_workflow` | Mettre à jour un workflow avancé existant |
| `delete_workflow` | Supprimer un workflow par ID |

### Tests de workflows

| Outil | Description |
|------|-------------|
| `test_advanced_workflow` | Tester l'exécution d'un workflow avancé, document optionnel |
| `list_test_scenarios` | Lister tous les scénarios de test de workflows |
| `list_cards` | Lister les cartes / actions de workflow disponibles |

### Gestion du Card SDK

| Outil | Description |
|------|-------------|
| `sdk_list_submissions` | Lister toutes les soumissions de cartes partenaires |
| `sdk_get_submission_status` | Obtenir le statut de validation d'une soumission |
| `sdk_approve_card` | Approuver une carte partenaire validée (admin) |
| `sdk_reject_card` | Rejeter une soumission de carte partenaire (admin) |
| `sdk_delete_submission` | Désactiver ou supprimer une soumission (admin) |
| `sdk_list_cards_picker` | Lister toutes les cartes activées avec leurs drapeaux de rôle |

### Développement du Card SDK

| Outil | Description |
|------|-------------|
| `sdk_create_card` | Créer une nouvelle carte partenaire à partir du code source |
| `sdk_validate_card` | Exécuter le pipeline de validation sans enregistrer |
| `sdk_test_card` | Exécuter une carte dans un environnement sandboxé |
| `sdk_import_github` | Importer une application partenaire depuis GitHub |

## Pour commencer

1. [Configurez votre client MCP](setup-and-configuration.md)
2. Découvrez les [Outils de workflow](workflow-tools.md)
3. Explorez les [Outils du Card SDK](card-sdk-tools.md)
4. Suivez les [exemples](examples.md) de bout en bout

{% hint style="info" %}
DocFlow MCP utilise le transport **Streamable HTTP**. L'endpoint du serveur est `/v3/mcp/` sur l'hôte DocFlow (par ex. `https://docflow.docbits.com/v3/mcp/`). Consultez [Installation & Configuration](setup-and-configuration.md) pour la liste complète des URL.
{% endhint %}
