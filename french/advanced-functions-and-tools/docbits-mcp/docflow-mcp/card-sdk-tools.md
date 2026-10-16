# Outils du SDK de cartes

Les outils du SDK de cartes vous permettent de créer, valider, tester et gérer des cartes partenaires personnalisées via MCP. Les cartes partenaires étendent DocFlow avec une logique métier personnalisée écrite en Python.

## Cycle de vie des cartes

Une carte partenaire passe par les états de soumission suivants (`partner_status`) :

| État | Signification | Visibilité dans les workflows |
|-------|---------------------|---------------------|
| `validating` | Soumission acceptée ; le pipeline de validation est en cours d'exécution. | Organisation soumettante uniquement |
| `validated` | Toutes les étapes de validation ont réussi. En attente d'approbation par un administrateur. | Organisation soumettante uniquement |
| `rejected` | La validation a échoué, ou un administrateur a rejeté la carte. Le code source est conservé pour inspection. | Organisation soumettante uniquement |
| `approved` | Un administrateur a approuvé la carte ; `enabled = true`. | **Toutes les organisations** |
| `disabled` | Carte précédemment approuvée qu'un administrateur a désactivée. | Organisation soumettante uniquement |
| `deleted` | Supprimée de façon logique (soft delete) ; non renvoyée par les listes de soumissions. | Masquée |

{% hint style="warning" %}
**Visibilité par organisation :** une carte partenaire n'est disponible pour les nœuds de workflow dans `list_cards` qu'une fois qu'elle a été **approuvée**. Les cartes partenaires approuvées sont visibles par toutes les organisations de la plateforme — l'approbation est une activation globale, et non propre à une organisation. Les cartes non approuvées (validating, validated, rejected, disabled) ne sont visibles que par l'organisation qui les a soumises.
{% endhint %}

Déroulement typique :

1. **Créer** une carte avec `sdk_create_card` ou `sdk_import_github` — exécute le pipeline de validation et enregistre la carte avec `partner_status = validated` (ou `rejected` en cas d'échec).
2. **Valider** avec `sdk_validate_card` pour revérifier une carte existante ou tester à blanc un nouveau code source sans l'enregistrer.
3. **Tester** avec `sdk_test_card` pour exécuter la carte dans la sandbox avec un contexte simulé.
4. **Approuver** avec `sdk_approve_card` (administrateur d'organisation uniquement) — relance la validation AST et comportementale, puis définit `partner_status = approved` et `enabled = true`.
5. Une fois approuvée, la carte apparaît dans `list_cards` pour toutes les organisations et peut être référencée depuis les nœuds de workflow.

## Outils de développement

### sdk\_create\_card

Créer une nouvelle carte partenaire à partir du code source et des manifestes. Exécute le pipeline de validation complet (voir [Étapes de validation](#sdk_validate_card) ci-dessous) et enregistre la carte dans la base de données. La carte passe à l'état `validated` et nécessite l'approbation d'un administrateur avant de pouvoir être utilisée dans les workflows.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|----------|-------------|
| `app_manifest` | object | Oui | Manifeste de l'application avec id, nom, version et informations sur le partenaire |
| `card_manifest` | object | Oui | Manifeste de la carte avec id, titre, entry\_point, class\_name, args |
| `card_type` | string | Oui | `action` ou `condition` |
| `source_code` | string | Oui | Code source Python (doit étendre `PartnerCard`) |
| `test_code` | string | Oui | Code de test Pytest pour la carte |
| `locales` | object | Non | Traductions des locales, par ex. `{"en": {...}, "de": {...}}` |

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
from api.sdk.context import ExecutionContext
from api.sdk.result import CardResult, CardStatus

class AmountThreshold(PartnerCard):
    def execute(self, context: ExecutionContext) -> CardResult:
        threshold = float(self.variables.get("threshold", 0))
        total = context.document_fields.get("total_amount", 0)
        if float(total) > threshold:
            return CardResult(
                status=CardStatus.SUCCESS,
                message=f"Amount {total} exceeds threshold {threshold}",
            )
        return CardResult(
            status=CardStatus.FAILED,
            message=f"Amount {total} below threshold {threshold}",
        )
```

{% hint style="info" %}
`CardStatus` comporte trois valeurs, qui correspondent directement aux arêtes du workflow :

| Statut | Arête empruntée | À utiliser pour |
|--------|------------|------------|
| `SUCCESS` | `success` | La carte a réussi — s'applique aux conditions comme aux actions. |
| `FAILED` | `failed_condition` | **Cartes de condition uniquement.** La condition a été évaluée à faux — le workflow emprunte la branche « sinon ». Les cartes d'action n'ont pas de point de sortie `failed_condition` ; renvoyer `FAILED` depuis une action laisse donc l'exécution sans issue. |
| `ERROR` | `error` | Une défaillance inattendue à l'exécution (exception). S'applique aux conditions comme aux actions. |

En résumé : les actions renvoient `SUCCESS` ou `ERROR` ; les conditions peuvent en plus renvoyer `FAILED`.
{% endhint %}

### sdk\_validate\_card

Exécuter le pipeline de validation sur une carte partenaire sans l'enregistrer. Deux modes :

- **Mode A** — Valider une carte existante par ID
- **Mode B** — Valider un nouveau code source en ligne

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Non | UUID de la carte existante (Mode A) |
| `app_manifest` | object | Non | Manifeste de l'application (Mode B) |
| `card_manifest` | object | Non | Manifeste de la carte (Mode B) |
| `card_type` | string | Non | `action` ou `condition` (Mode B) |
| `source_code` | string | Non | Code source Python (Mode B) |
| `test_code` | string | Non | Code de test (Mode B) |

{% hint style="info" %}
Fournissez soit `card_id` seul (Mode A), soit `app_manifest` + `card_manifest` + `source_code` ensemble (Mode B).
{% endhint %}

**Étapes de validation :**

1. **Structure** — Vérifie la disposition des fichiers, le schéma du manifeste (`app.json`, `.docflowcompose/flow/...`) et l'existence des points d'entrée déclarés.
2. **Locales** — Rapproche les clés de traduction utilisées dans la carte des fichiers `locales/<lang>.json` ; échoue si une clé manque dans une langue déclarée.
3. **Analyse AST** — Parcourt chaque fichier `.py` sous `src/` et recherche les imports interdits, les appels dangereux, ainsi que les exigences de hiérarchie de classes et de signatures de méthodes.
4. **Dépendances** — Vérifie que tous les imports correspondent à des modules autorisés de la liste blanche du SDK.
5. **Tests** — Exécute la suite pytest de la carte avec des rlimits réduites.
6. **Comportemental** — Exécute la carte dans la sandbox de production avec un contexte simulé minimal pour confirmer le comportement à l'exécution.

Les étapes s'exécutent dans l'ordre ; la première étape en échec interrompt les suivantes. L'étape 6 (Comportemental) est également relancée au moment de l'approbation, comme contrôle de défense en profondeur, avant l'activation de la carte.

### sdk\_test\_card

Exécuter une carte partenaire dans un environnement sandboxé avec un contexte simulé. La sandbox impose des builtins restreints, une liste blanche d'imports sélectionnés, un délai d'exécution maximal et des limites de ressources de processus réduites — les mêmes restrictions que celles sous lesquelles une carte s'exécute une fois approuvée.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Non | UUID de la carte existante (Mode A) |
| `source_code` | string | Non | Code source pour le test en ligne (Mode B) |
| `class_name` | string | Non | Nom de la classe pour le test en ligne (Mode B) |
| `variables` | object | Non | Variables à transmettre au constructeur de la carte |
| `mock_context` | object | Non | Contexte d'exécution simulé |

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

L'outil renvoie `execution_success` (indique si la sandbox a mené la carte jusqu'au bout — un délai dépassé, une violation d'import ou une exception levée le met à `false`), `card_status` (le `CardStatus` renvoyé par `execute()` lui-même), le `message` et les `data` de la carte, les `logs` capturés, ainsi que `execution_time_ms`.

### sdk\_import\_github

Importer une application partenaire depuis un dépôt GitHub. Clone le dépôt, lit `app.json` et importe toutes les cartes trouvées dans le répertoire `.docflowcompose`.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|----------|-------------|
| `github_url` | string | Oui | URL HTTPS GitHub (par ex. `https://github.com/org/repo`) |
| `branch` | string | Non | Branche à cloner (par défaut : `main`) |
| `token` | string | Non | Jeton GitHub pour les dépôts privés |

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

## Outils de gestion

### sdk\_list\_submissions

Lister toutes les soumissions de cartes partenaires pour l'organisation actuelle.

**Paramètres :** aucun

### sdk\_get\_submission\_status

Obtenir le statut de validation et le rapport d'une soumission de carte partenaire donnée.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Oui | UUID de la carte partenaire |

### sdk\_approve\_card

Approuver une carte partenaire validée et l'activer. L'approbation relance la validation AST et comportementale comme contrôle de défense en profondeur, définit `partner_status = approved` et `enabled = true`, puis enregistre la carte dans le registre d'exécution. Une fois approuvée, la carte apparaît dans `list_cards` pour **toutes les organisations**, et pas seulement pour celle qui l'a soumise.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Oui | UUID de la carte partenaire |

{% hint style="warning" %}
Nécessite les permissions d'administrateur d'organisation. La carte doit être à l'état `validated`. Les cartes rejetées doivent être renvoyées et revalidées avant de pouvoir être approuvées.
{% endhint %}

### sdk\_reject\_card

Rejeter une soumission de carte partenaire et la désactiver.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Oui | UUID de la carte partenaire |
| `reason` | string | Non | Motif du rejet |

{% hint style="warning" %}
Nécessite les permissions d'administrateur d'organisation.
{% endhint %}

### sdk\_delete\_submission

Supprimer de façon logique (soft delete) une soumission de carte partenaire, quel que soit son état actuel. Définit `partner_status = deleted`, `enabled = false` et `deprecated = true`. La ligne est conservée à des fins d'audit, mais elle est masquée dans les listes de soumissions et dans `list_cards`.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|----------|-------------|
| `card_id` | string | Oui | UUID de la carte partenaire |

{% hint style="warning" %}
Nécessite les permissions d'administrateur d'organisation.
{% endhint %}

### sdk\_list\_cards\_picker

Lister toutes les cartes activées et non obsolètes avec leurs indicateurs de rôle. Utile pour déterminer quelles cartes peuvent être utilisées dans quels types de nœuds lors de la construction de workflows.

**Paramètres :** aucun

## Fonctionnalités actuelles et feuille de route

Le SDK de cartes partenaires est déployé progressivement. Voici ce sur quoi votre carte peut s'appuyer dès aujourd'hui et ce qui est encore en cours d'intégration :

| Fonctionnalité | Statut |
|------------|--------|
| **Conditions sur les champs** — lire les champs du document depuis `context.document_fields` et créer des branches selon leurs valeurs dans les cartes de condition | ✅ Implémenté |
| **Requêtes HTTP sortantes** — appeler des services externes depuis une carte | 🚧 En cours d'ajout |
| **Informations étendues sur le document** — métadonnées supplémentaires du document (au-delà de `document_id`, `document_type` et `document_fields`) exposées dans `ExecutionContext` | 🚧 En cours d'ajout |
| **Aides à la consultation des tables de base de données** — aides intégrées pour lire les tables de données de référence / de consultation de DocBits depuis une carte | 📅 Prévu pour la version 1.1 |
| **Visionneuse du code source des cartes partenaires** — vue en lecture seule du code de la carte partenaire soumise dans l'interface DocBits, afin que les administrateurs puissent inspecter ce qu'ils approuvent | 📅 Prévu pour la version 1.1 |

{% hint style="info" %}
Si votre carte a besoin d'une fonctionnalité encore en cours de développement, elle échouera à la validation (import interdit, attribut de contexte manquant ou restriction de la sandbox) tant que l'élément correspondant n'aura pas été livré. Cette page sera mise à jour à mesure que chaque fonctionnalité sera disponible.
{% endhint %}

{% hint style="danger" %}
**Les cartes partenaires exécutent du code tiers — à utiliser à vos propres risques.**

Les cartes téléversées via le SDK de cartes partenaires ne sont que **partiellement validées par DocBits**. Le pipeline de validation contrôle la structure, les locales, les imports, les motifs AST, les dépendances, les propres tests de la carte et une exécution comportementale de vérification dans la sandbox — il ne constitue **pas** un audit de sécurité complet ni une garantie fonctionnelle de la logique métier de la carte.

Dès qu'un administrateur d'organisation approuve une carte partenaire, celle-ci devient disponible pour toutes les organisations de la plateforme et s'exécute dans la sandbox de production sur des documents réels. Approuver et activer une carte partenaire constitue donc une décision de confiance explicite de la part de l'administrateur qui l'approuve. DocBits décline toute responsabilité en cas de perte de données, d'acheminement incorrect, de fuite d'informations ou de tout autre résultat causé par une carte partenaire que vous choisissez d'installer ou d'approuver.

Si vous n'êtes pas l'auteur d'origine de la carte, examinez le code source (et, une fois la version 1.1 disponible, utilisez la visionneuse du code source des cartes partenaires) avant de l'approuver.
{% endhint %}
