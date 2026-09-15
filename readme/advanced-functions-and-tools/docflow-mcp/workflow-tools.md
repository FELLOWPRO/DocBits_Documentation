# Outils de workflow

DocFlow MCP fournit des outils pour gérer et tester les workflows avancés, ainsi que des outils pour lire les journaux de workflow et gérer les variables de workflow.

{% hint style="info" %}
**Noms des outils via la passerelle DocBits MCP.** Lorsque vous vous connectez via le DocBits MCP unifié (`api.docbits.com/v3/mcp`), chaque outil DocFlow porte le préfixe `docflow_` : `list_workflows` s'appelle `docflow_list_workflows`, `run_workflow_with_assertions` devient `docflow_run_workflow_with_assertions`. Les paramètres sont identiques. Les noms ci-dessous sont les noms DocFlow sans préfixe.

Les workflows sont **créés et modifiés dans le concepteur DocFlow** de l'application web. Le MCP les lit, les teste, les exécute et les supprime ; il ne crée ni ne modifie les graphes de workflow.
{% endhint %} Les outils du SDK de cartes ont leur propre page, voir [Outils du SDK de Cartes](card-sdk-tools.md).

## list\_workflows

Lister tous les workflows de l'organisation actuelle.

**Paramètres :** Aucun

**Exemple de réponse :**

```json
[
  {
    "id": "a1b2c3d4-...",
    "name": "Invoice Approval",
    "version": 3,
    "enabled": true,
    "doc_types": ["INVOICE"],
    "workflow_type": "advanced",
    "created_on": "2025-01-15 10:30:00",
    "last_modified_on": "2025-03-20 14:22:00"
  }
]
```

## get\_workflow

Obtenir les détails d'un workflow spécifique, y compris sa structure de nœuds et d'arêtes.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Oui | UUID du workflow |

**Exemple de réponse :**

```json
{
  "id": "a1b2c3d4-...",
  "name": "Invoice Approval",
  "version": 3,
  "enabled": true,
  "doc_types": ["INVOICE"],
  "workflow_type": "advanced",
  "description": "Routes invoices based on amount",
  "advanced_config": {
    "nodes": [
      {"node_id": "when-1", "node_type": "when", "label": "Amount > 1000"},
      {"node_id": "then-1", "node_type": "then", "label": "Send for Approval"}
    ],
    "edges": [
      {"source_node_id": "when-1", "target_node_id": "then-1"}
    ]
  }
}
```

## delete\_workflow

Supprimer un workflow par ID (suppression logique).

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Oui | UUID du workflow à supprimer |

**Exemple de réponse :**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-..."
}
```

## test\_advanced\_workflow

Tester l'exécution d'un workflow avancé. Vous pouvez optionnellement fournir un ID de document pour tester avec un document réel.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Oui | UUID du workflow avancé |
| `doc_id` | string | Non | UUID d'un document pour le test |

**Exemple de réponse :**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-...",
  "execution_time": 0.234,
  "workflow_result": "completed",
  "node_results": {
    "when-1": {"status": "success", "output": true},
    "then-1": {"status": "success"}
  },
  "logs": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "status": "success",
      "error": null,
      "duration_ms": 12
    }
  ]
}
```

## list\_test\_scenarios

Lister tous les scénarios de test de workflow pour l'organisation.

**Paramètres :** Aucun

**Exemple de réponse :**

```json
[
  {
    "id": "scenario-uuid",
    "name": "Invoice over 1000 EUR",
    "workflow_id": "a1b2c3d4-...",
    "enabled": true,
    "status": "passed",
    "last_run": "2025-03-20 14:00:00"
  }
]
```

## list\_cards

Lister toutes les cartes de workflow disponibles avec leurs conditions et configuration.

**Paramètres :** Aucun

**Exemple de réponse :**

```json
[
  {
    "id": "card-uuid",
    "text": "Document Type Is",
    "card_type": "document_type_is",
    "card_version": 1,
    "category": "Document",
    "when_condition": true,
    "and_condition": false,
    "then_condition": false
  },
  {
    "id": "card-uuid-2",
    "text": "Send Email Notification",
    "card_type": "send_email",
    "card_version": 1,
    "category": "Communication",
    "when_condition": false,
    "and_condition": false,
    "then_condition": true
  }
]
```

{% hint style="info" %}
Les cartes ont des indicateurs de rôle : `when_condition` (déclencheur), `and_condition` (condition supplémentaire) et `then_condition` (action). Utilisez-les pour déterminer dans quels types de nœuds une carte peut être utilisée.
{% endhint %}

## list\_workflow\_variables

Lister toutes les variables de workflow de l'organisation avec leur nom, leur type et leur valeur actuelle.

**Paramètres :** Aucun

## set\_workflow\_variable

Créer une variable de workflow ou mettre à jour sa valeur. Les variables de type document n'ont pas de valeur propre ; elles sont définies par le workflow au moment de l'exécution.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `name` | string | Oui | Nom de la variable |
| `value` | string | Non | Nouvelle valeur |
| `var_type` | string | Non | Type de la variable lors de la création (par exemple `string`, `number`, `document`) |

## search\_workflow\_logs

Rechercher dans les journaux d'exécution des workflows pour comprendre pourquoi des exécutions ont échoué, réussi ou rencontré une condition non satisfaite.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Non | Limiter à un seul workflow |
| `doc_id` | string | Non | Limiter aux exécutions d'un seul document |
| `status` | string | Non | Statut d'exécution à filtrer |
| `keyword` | string | Non | Filtre en texte libre sur le journal |
| `include_workflow_data` | boolean | Non | Inclure l'instantané de la définition du workflow pour chaque exécution |
| `limit` / `offset` | integer | Non | Pagination |

## get\_workflow\_log\_detail

Détail complet d'une exécution : les journaux bruts d'exécution des cartes et la définition du workflow telle qu'elle était au moment de l'exécution.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `log_id` | string | Oui | ID de l'entrée de journal issue de `search_workflow_logs` |

## run\_workflow\_with\_assertions

Initialiser des variables de workflow, exécuter un workflow avancé avec l'exécuteur réel et vérifier le résultat dans la base de données. Les variables sont de véritables écritures, pas des simulations ; utilisez cet outil pour tester un workflow en intégration depuis un assistant.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Oui | UUID du workflow à exécuter |
| `doc_id` | string | Non | Document sur lequel exécuter le workflow |
| `seed_variables` | array | Non | Variables à créer ou mettre à jour avant l'exécution ; les variables de type document peuvent pointer vers un `doc_id` via `value` |
