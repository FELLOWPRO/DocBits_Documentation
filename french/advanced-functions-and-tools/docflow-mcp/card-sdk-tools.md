# Outils du SDK de Cartes

Les outils du SDK de cartes vous permettent de créer, valider, tester et gérer des cartes partenaires personnalisées via MCP. Les cartes partenaires étendent DocFlow avec une logique métier personnalisée écrite en Python.

## Cycle de vie des cartes

```
Create → Validate → Test → Approve → Use in Workflows
```

1. **Créer** une carte avec `sdk_create_card` ou `sdk_import_github`
2. **Valider** avec `sdk_validate_card` (validation en 5 étapes)
3. **Tester** avec `sdk_test_card` (exécution sandboxée)
4. **Approuver** avec `sdk_approve_card` (administrateur requis)
5. La carte est maintenant disponible dans `list_cards` et peut être utilisée dans les workflows

## Outils de développement

### sdk\_create\_card

Créer une nouvelle carte partenaire à partir du code source et des manifestes. Exécute la validation complète en 5 étapes et enregistre la carte dans la base de données. La carte démarre dans un état en attente et nécessite l'approbation d'un administrateur pour être activée.

**Paramètres :**

| Paramètre       | Type   | Obligatoire | Description                                                           |
| --------------- | ------ | ----------- | --------------------------------------------------------------------- |
| `app_manifest`  | object | Oui         | Manifeste de l'application avec id, nom, version, infos partenaire    |
| `card_manifest` | object | Oui         | Manifeste de la carte avec id, titre, entry\_point, class\_name, args |
| `card_type`     | string | Oui         | `action` ou `condition`                                               |
| `source_code`   | string | Oui         | Code source Python (doit étendre `PartnerCard`)                       |
| `test_code`     | string | Oui         | Code de test Pytest pour la carte                                     |
| `locales`       | object | Non         | Traductions locales, ex. `{"en": {...}, "de": {...}}`                 |

**Exemple de manifeste d'application :**

```json
{
  "id": "com.acme.invoice-tools",
  "name": "Invoice Tools",
  "version": "1.0.0",
  "partner": {
    "id": "acme",
    "name": "Acme Corp"
  }
}
```

**Exemple de manifeste de carte :**

```json
{
  "id": "amount-threshold",
  "title": {"en": "Amount Threshold Check"},
  "entry_point": "src/amount_threshold.py",
  "class_name": "AmountThreshold",
  "args": [
    {
      "id": "threshold",
      "title": {"en": "Threshold Amount"},
      "type": "number",
      "required": true
    }
  ]
}
```

**Exemple de code source :**

```python
from api.sdk.base import PartnerCard
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context):
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}"
            )
        return CardResult(
            status=CardStatus.FAILURE,
            message=f"Amount {total} below threshold {threshold}"
        )
```

**Exemple de réponse :**

```json
{
  "success": true,
  "cards": ["amount-threshold"],
  "validation_report": {
    "status": "validated",
    "stages": {
      "structure": {"passed": true},
      "ast_analysis": {"passed": true},
      "dependencies": {"passed": true},
      "tests": {"passed": true},
      "behavioral": {"passed": true}
    }
  }
}
```

### sdk\_validate\_card

Exécuter la validation en 5 étapes sur une carte partenaire sans l'enregistrer. Deux modes :

* **Mode A** — Valider une carte existante par ID
* **Mode B** — Valider un nouveau code source en ligne

**Paramètres :**

| Paramètre       | Type   | Obligatoire | Description                         |
| --------------- | ------ | ----------- | ----------------------------------- |
| `card_id`       | string | Non         | UUID de la carte existante (Mode A) |
| `app_manifest`  | object | Non         | Manifeste de l'application (Mode B) |
| `card_manifest` | object | Non         | Manifeste de la carte (Mode B)      |
| `card_type`     | string | Non         | `action` ou `condition` (Mode B)    |
| `source_code`   | string | Non         | Code source Python (Mode B)         |
| `test_code`     | string | Non         | Code de test (Mode B)               |

{% hint style="info" %}
Fournissez soit `card_id` seul (Mode A), soit `app_manifest` + `card_manifest` + `source_code` ensemble (Mode B).
{% endhint %}

**Étapes de validation :**

1. **Structure** — Vérifie la disposition des fichiers, le schéma du manifeste, les fichiers requis
2. **Analyse AST** — Vérifie la syntaxe Python, la hiérarchie des classes, les signatures de méthodes
3. **Dépendances** — Valide les imports par rapport aux modules autorisés
4. **Tests** — Exécute la suite de tests de la carte
5. **Comportemental** — Exécute la carte en sandbox pour vérifier le comportement à l'exécution

### sdk\_test\_card

Exécuter une carte partenaire dans un environnement sandboxé avec un contexte simulé. Utilise le même modèle de sécurité qu'en production (builtins restreints, liste blanche d'imports, timeout de 10 secondes).

**Paramètres :**

| Paramètre      | Type   | Obligatoire | Description                                     |
| -------------- | ------ | ----------- | ----------------------------------------------- |
| `card_id`      | string | Non         | UUID de la carte existante (Mode A)             |
| `source_code`  | string | Non         | Code source pour le test en ligne (Mode B)      |
| `class_name`   | string | Non         | Nom de la classe pour le test en ligne (Mode B) |
| `variables`    | object | Non         | Variables à passer au constructeur de la carte  |
| `mock_context` | object | Non         | Contexte d'exécution simulé                     |

**Champs du contexte simulé :**

```json
{
  "document_id": "doc-uuid",
  "document_type": "INVOICE",
  "document_fields": {
    "total_amount": "1500.00",
    "currency": "EUR",
    "vendor_name": "Acme Corp"
  },
  "metadata": {
    "custom_key": "custom_value"
  }
}
```

**Exemple de réponse :**

```json
{
  "success": true,
  "status": "CardStatus.SUCCESS",
  "message": "Amount 1500.00 exceeds threshold 1000",
  "data": {},
  "logs": ["Checking threshold...", "Amount exceeds threshold"]
}
```

### sdk\_import\_github

Importer une application partenaire depuis un dépôt GitHub. Clone le dépôt, lit `app.json` et importe toutes les cartes trouvées dans le répertoire `.docflowcompose`.

**Paramètres :**

| Paramètre    | Type   | Obligatoire | Description                                          |
| ------------ | ------ | ----------- | ---------------------------------------------------- |
| `github_url` | string | Oui         | URL HTTPS GitHub (ex. `https://github.com/org/repo`) |
| `branch`     | string | Non         | Branche à cloner (par défaut : `main`)               |
| `token`      | string | Non         | Jeton GitHub pour les dépôts privés                  |

**Structure de dépôt attendue :**

```
repo/
  app.json
  .docflowcompose/
    flow/
      actions/
        my-action.json
      conditions/
        my-condition.json
  src/
    my_action.py
    my_condition.py
  tests/
    test_card.py
```

**Exemple de réponse :**

```json
{
  "success": true,
  "message": "Imported 2 cards from GitHub. Status: validated",
  "app_id": "com.acme.invoice-tools",
  "cards_created": ["my-action", "my-condition"],
  "validation_report": {"status": "validated"}
}
```

## Outils de gestion

### sdk\_list\_submissions

Lister toutes les soumissions de cartes partenaires pour l'organisation actuelle.

**Paramètres :** Aucun

**Exemple de réponse :**

```json
[
  {
    "card_id": "card-uuid",
    "card_name": "Amount Threshold Check",
    "partner_app_id": "com.acme.invoice-tools",
    "partner_status": "validated",
    "version": "1.0.0",
    "card_type": "condition",
    "enabled": false,
    "submitted_at": "2025-03-20T10:00:00"
  }
]
```

### sdk\_get\_submission\_status

Obtenir le statut de validation et le rapport pour une soumission de carte partenaire spécifique.

**Paramètres :**

| Paramètre | Type   | Obligatoire | Description                 |
| --------- | ------ | ----------- | --------------------------- |
| `card_id` | string | Oui         | UUID de la carte partenaire |

**Exemple de réponse :**

```json
{
  "card_id": "card-uuid",
  "status": "validated",
  "validation_report": {
    "status": "validated",
    "stages": {
      "structure": {"passed": true},
      "ast_analysis": {"passed": true},
      "dependencies": {"passed": true},
      "tests": {"passed": true},
      "behavioral": {"passed": true}
    }
  }
}
```

### sdk\_approve\_card

Approuver une carte partenaire validée et l'activer pour une utilisation dans les workflows. La carte est enregistrée dans le registre d'exécution et devient disponible dans `list_cards`.

**Paramètres :**

| Paramètre | Type   | Obligatoire | Description                 |
| --------- | ------ | ----------- | --------------------------- |
| `card_id` | string | Oui         | UUID de la carte partenaire |

{% hint style="warning" %}
Nécessite les permissions d'administrateur d'organisation. La carte doit être dans l'état `validated` ou `rejected`.
{% endhint %}

### sdk\_reject\_card

Rejeter une soumission de carte partenaire et la désactiver.

**Paramètres :**

| Paramètre | Type   | Obligatoire | Description                 |
| --------- | ------ | ----------- | --------------------------- |
| `card_id` | string | Oui         | UUID de la carte partenaire |
| `reason`  | string | Non         | Motif du rejet              |

{% hint style="warning" %}
Nécessite les permissions d'administrateur d'organisation.
{% endhint %}

### sdk\_delete\_submission

Désactiver ou supprimer une soumission de carte partenaire. Les cartes rejetées ou désactivées sont physiquement supprimées de la base de données. Les cartes actives sont d'abord désactivées.

**Paramètres :**

| Paramètre | Type   | Obligatoire | Description                 |
| --------- | ------ | ----------- | --------------------------- |
| `card_id` | string | Oui         | UUID de la carte partenaire |

{% hint style="warning" %}
Nécessite les permissions d'administrateur d'organisation.
{% endhint %}

### sdk\_list\_cards\_picker

Lister toutes les cartes activées et non obsolètes avec les indicateurs de rôle. Utile pour déterminer quelles cartes peuvent être utilisées dans quels types de nœuds lors de la construction de workflows.

**Paramètres :** Aucun

**Exemple de réponse :**

```json
[
  {
    "card_id": "card-uuid",
    "card_name": "Document Type Is",
    "category": "Document",
    "card_type": "document_type_is",
    "is_when": true,
    "is_and": false,
    "is_then": false,
    "is_partner_card": false
  }
]
```
