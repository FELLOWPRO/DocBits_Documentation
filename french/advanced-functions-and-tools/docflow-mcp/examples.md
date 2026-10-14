# Exemples

Exemples complets de bout en bout montrant comment utiliser les outils DocFlow MCP ensemble.

## Exemple 1 : Créer une carte personnalisée et l'utiliser dans un workflow

Cet exemple parcourt le cycle de vie complet : créer une carte partenaire, la valider, la tester, l'approuver et construire un workflow qui l'utilise.

### Étape 1 : Créer la carte

Appelez `sdk_create_card` :

```json
{
  "app_manifest": {
    "id": "com.example.invoice-tools",
    "name": "Invoice Tools",
    "version": "1.0.0",
    "partner": {
      "id": "example-partner",
      "name": "Example Corp"
    }
  },
  "card_manifest": {
    "id": "high-value-check",
    "title": {"en": "High Value Invoice Check"},
    "entry_point": "src/high_value.py",
    "class_name": "HighValueCheck",
    "args": [
      {
        "id": "threshold",
        "title": {"en": "Amount Threshold"},
        "type": "number",
        "required": true
      }
    ]
  },
  "card_type": "condition",
  "source_code": "from api.sdk.base import PartnerCard\nfrom api.sdk.result import CardResult, CardStatus\n\nclass HighValueCheck(PartnerCard):\n    def execute(self, context):\n        threshold = float(self.variables.get('threshold', 1000))\n        total = float(context.document_fields.get('total_amount', 0))\n        if total > threshold:\n            return CardResult(status=CardStatus.SUCCESS, message=f'High value: {total}')\n        return CardResult(status=CardStatus.FAILURE, message=f'Below threshold: {total}')",
  "test_code": "def test_high_value():\n    assert True  # Basic test"
}
```

Notez le `card_id` de la réponse -- vous en aurez besoin dans les étapes suivantes.

### Étape 2 : Valider la carte

Appelez `sdk_validate_card` avec l'ID de la carte :

```json
{
  "card_id": "returned-card-uuid"
}
```

Examinez le rapport de validation. Les 5 étapes doivent réussir.

### Étape 3 : Tester la carte

Appelez `sdk_test_card` avec un contexte de document simulé :

```json
{
  "card_id": "returned-card-uuid",
  "variables": {"threshold": "1000"},
  "mock_context": {
    "document_type": "INVOICE",
    "document_fields": {
      "total_amount": "2500.00",
      "currency": "EUR"
    }
  }
}
```

Vérifiez que la réponse affiche `CardStatus.SUCCESS`.

### Étape 4 : Approuver la carte

Appelez `sdk_approve_card` (nécessite un administrateur) :

```json
{
  "card_id": "returned-card-uuid"
}
```

La carte est maintenant active et disponible pour une utilisation dans les workflows.

### Étape 5 : Construire un workflow avec la carte

Ouvrez le **concepteur DocFlow** dans l'application web, créez un workflow avancé et ajoutez la carte approuvée comme nœud, par exemple un déclencheur *Document reçu*, la carte *High Value Check* et un nœud *Approbation* pour la branche `true`. Les graphes de workflow sont créés et modifiés dans le concepteur ; le MCP ne les crée pas.

De retour dans l'assistant, confirmez que le workflow existe et lisez sa structure :

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id issu de list_workflows>"
}
```

### Étape 6 : Tester le workflow

Appelez `test_advanced_workflow` :

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

Examinez les journaux d'exécution pour vérifier que chaque nœud s'est exécuté correctement.

---

## Exemple 2 : Construire un workflow avec des cartes intégrées

Cet exemple crée un workflow en utilisant uniquement des cartes intégrées (aucune carte personnalisée nécessaire).

### Étape 1 : Découvrir les cartes disponibles

Appelez `sdk_list_cards_picker` pour voir toutes les cartes disponibles avec leurs indicateurs de rôle :

```json
// Response includes cards like:
{
  "card_id": "doc-type-uuid",
  "card_name": "Document Type Is",
  "is_when": true,
  "is_and": false,
  "is_then": false
}
```

Filtrez par rôle :
- `is_when: true` — Utiliser dans les nœuds WHEN (déclencheurs)
- `is_and: true` — Utiliser dans les nœuds AND (conditions supplémentaires)
- `is_then: true` — Utiliser dans les nœuds THEN (actions)

### Étape 2 : Créer le workflow

```json
{
  "name": "Invoice Document Type Router",
  "description": "When document is an invoice, apply validation",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 250, "y": 50},
      "label": "Document is Invoice",
      "card": {
        "id": "doc-type-card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "and-1",
      "node_type": "and",
      "position": {"x": 250, "y": 200},
      "label": "Amount > 1000",
      "card": {
        "id": "amount-card-uuid",
        "card_type": "field_value_check",
        "version": 1,
        "variables": [
          {"id": "field-var", "data": "total_amount", "data_type": "string"},
          {"id": "op-var", "data": ">", "data_type": "string"},
          {"id": "val-var", "data": "1000", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 250, "y": 350},
      "label": "Set Status to Review",
      "card": {
        "id": "status-card-uuid",
        "card_type": "set_document_status",
        "version": 1,
        "variables": [
          {"id": "status-var", "data": "review", "data_type": "string"}
        ]
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "and-1",
      "source_handle": "success",
      "target_handle": "input"
    },
    {
      "edge_id": "e2",
      "source_node_id": "and-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

Cela crée un workflow : **WHEN** le document est une facture **AND** le montant > 1000 **THEN** définir le statut sur révision.

---

## Exemple 3 : Importer des cartes depuis GitHub

Si vos cartes partenaires se trouvent dans un dépôt GitHub, vous pouvez les importer directement :

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

Pour les dépôts privés, incluez un jeton GitHub :

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

Après l'importation, les cartes passent automatiquement par la validation. Vérifiez leur statut avec `sdk_list_submissions` et approuvez-les avec `sdk_approve_card`.
