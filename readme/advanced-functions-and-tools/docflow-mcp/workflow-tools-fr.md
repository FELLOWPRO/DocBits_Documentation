# Outils de workflow

DocFlow MCP expose des outils pour gérer et tester les workflows avancés, ainsi que des outils pour lire les logs de workflow et gérer les variables de workflow. Les outils Card SDK ont leur propre page — voir [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Lister tous les workflows de l'organisation courante.

**Paramètres :** Aucun

## get\_workflow

Obtenir les détails d'un workflow spécifique, y compris sa structure de nœuds et d'arêtes.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Oui | UUID du workflow |

## create\_advanced\_workflow

Créer un nouveau workflow avancé avec des nœuds et des arêtes.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `name` | string | Oui | Nom du workflow (3-126 caractères) |
| `description` | string | Non | Description optionnelle |
| `nodes` | array | Oui | Tableau de nœuds de workflow |
| `edges` | array | Oui | Tableau d'arêtes reliant les nœuds |

### Structure des nœuds

Chaque nœud nécessite :

| Champ | Type | Description |
|-------|------|-------------|
| `node_id` | string | Identifiant unique du nœud |
| `node_type` | string | Voir les types de nœuds ci-dessous |
| `position` | object | `{x: number, y: number}` position sur le canevas |
| `label` | string | Libellé d'affichage |
| `card` | object | Configuration de la carte (obligatoire pour `when`, `and`, `then` — voir ci-dessous) |

**Types de nœuds :**

| Type | Carte requise | Rôle |
|------|------------------|---------|
| `start` | Aucune carte | Nœud déclencheur — point d'entrée du workflow |
| `when` | Carte de condition | Condition de déclenchement (également point d'entrée valide) |
| `and` | Carte de condition | Filtre de condition supplémentaire après un `when` |
| `or` | Aucune carte | Nœud de branchement — poursuit si l'une des branches entrantes réussit |
| `then` | Carte d'action | Action à exécuter |
| `delay` | Aucune carte | Nœud d'attente — met l'exécution en pause pendant une durée configurée |
| `all` | Aucune carte | Nœud de fusion — attend toutes les branches entrantes |
| `any` | Aucune carte | Nœud de fusion — poursuit dès la première branche entrante |
| `note` | Aucune carte | Note autocollante / annotation ; non exécutée |

### Structure des arêtes

Chaque arête nécessite :

| Champ | Type | Description |
|-------|------|-------------|
| `edge_id` | string | Identifiant unique de l'arête |
| `source_node_id` | string | ID du nœud source |
| `target_node_id` | string | ID du nœud cible |
| `source_handle` | string | `success`, `error` ou `failed_condition` (optionnel) |
| `target_handle` | string | `input` (optionnel) |

**Handles source :**

- `success` — pris quand le nœud source réussit (disponible sur tout nœud exécutable).
- `failed_condition` — pris quand une carte de condition `when` ou `and` est évaluée à false.
- `error` — pris quand un nœud `and` ou `then` lève une erreur.

### Configuration de la carte

Les cartes définissent ce que fait un nœud. Utilisez `list_cards` ou `sdk_list_cards_picker` pour obtenir les cartes disponibles.

```json
{
  "id": "card-uuid-here",
  "card_type": "document_type_is",
  "version": 1,
  "variables": [
    {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
  ]
}
```

{% hint style="info" %}
Vous n'avez qu'à fournir `id`, `card_type`, `version` et `variables` pour chaque carte. Le serveur enrichit automatiquement les cartes avec les métadonnées d'affichage (svg, text, category) depuis la base de données.
{% endhint %}

**Exemple de requête :**

```json
{
  "name": "Simple Invoice Router",
  "description": "Routes invoices to approval",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 100, "y": 100},
      "label": "Document is Invoice",
      "card": {
        "id": "card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 100, "y": 300},
      "label": "Send Notification",
      "card": {
        "id": "card-uuid-2",
        "card_type": "send_email",
        "version": 1,
        "variables": []
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

## update\_advanced\_workflow

Mettre à jour un workflow avancé existant. Vous pouvez mettre à jour toute combinaison de nom, description, nœuds et arêtes.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Oui | UUID du workflow à mettre à jour |
| `name` | string | Non | Nouveau nom |
| `description` | string | Non | Nouvelle description |
| `nodes` | array | Non | Nouveaux nœuds (remplace tous les nœuds existants) |
| `edges` | array | Non | Nouvelles arêtes (remplace toutes les arêtes existantes) |

## delete\_workflow

Supprimer un workflow par ID (suppression douce).

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Oui | UUID du workflow à supprimer |

## test\_advanced\_workflow

Tester l'exécution d'un workflow avancé. Vous pouvez optionnellement fournir un ID de document pour tester avec un document réel.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `workflow_id` | string | Oui | UUID du workflow avancé |
| `doc_id` | string | Non | UUID d'un document avec lequel tester |

## list\_test\_scenarios

Lister tous les scénarios de test de workflows pour l'organisation.

**Paramètres :** Aucun

## list\_cards

Lister toutes les cartes de workflow disponibles avec leurs conditions et configuration.

**Paramètres :** Aucun

{% hint style="info" %}
Les cartes ont des drapeaux de rôle : `when_condition` (déclencheur), `and_condition` (condition supplémentaire) et `then_condition` (action). Utilisez-les pour déterminer dans quels types de nœuds une carte peut être utilisée.
{% endhint %}
