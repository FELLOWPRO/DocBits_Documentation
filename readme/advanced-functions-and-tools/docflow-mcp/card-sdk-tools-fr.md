# Outils du SDK de cartes

Les outils du SDK de cartes vous permettent de créer, valider, tester et gérer des cartes partenaires personnalisées via MCP. Les cartes partenaires étendent DocFlow avec une logique métier personnalisée écrite en Python.

## Cycle de vie des cartes

Une carte partenaire passe par les états de soumission suivants (`partner_status`) :

| État | Signification | Visibilité dans les workflows |
|-------|---------|---------------------|
| `validating` | Soumission acceptée ; le pipeline de validation est en cours. | Organisation soumettrice uniquement |
| `validated` | Toutes les étapes de validation ont réussi. En attente d'approbation d'un admin. | Organisation soumettrice uniquement |
| `rejected` | Validation échouée, ou un admin a rejeté la carte. Le code source est conservé pour inspection. | Organisation soumettrice uniquement |
| `approved` | Un admin a approuvé la carte ; `enabled = true`. | **Toutes les organisations** |
| `disabled` | Carte précédemment approuvée qu'un admin a désactivée. | Organisation soumettrice uniquement |
| `deleted` | Supprimée en douceur ; non retournée par les listes de soumissions. | Masquée |

{% hint style="warning" %}
**Visibilité entre organisations :** Une carte partenaire n'est disponible pour les nœuds de workflow dans `list_cards` qu'une fois qu'elle a été **approuvée**. Les cartes partenaires approuvées sont visibles par chaque organisation de la plateforme — l'approbation est une activation globale, pas une activation par organisation. Les cartes non approuvées (validating, validated, rejected, disabled) ne sont visibles que par l'organisation qui les a soumises.
{% endhint %}

Flux typique :

1. **Créer** une carte avec `sdk_create_card` ou `sdk_import_github` — exécute le pipeline de validation et stocke la carte avec `partner_status = validated` (ou `rejected` en cas d'échec).
2. **Valider** avec `sdk_validate_card` pour vérifier à nouveau une carte existante ou pour tester du nouveau code source sans le persister.
3. **Tester** avec `sdk_test_card` pour exécuter la carte dans la sandbox contre un contexte fictif.
4. **Approuver** avec `sdk_approve_card` (admin de l'organisation uniquement) — réexécute la validation AST et comportementale, puis définit `partner_status = approved` et `enabled = true`.
5. Une fois approuvée, la carte apparaît dans `list_cards` pour chaque organisation et peut être référencée depuis les nœuds de workflow.

## Outils de développement

### sdk\_create\_card

Créer une nouvelle carte partenaire à partir du code source et des manifestes. Exécute le pipeline de validation complet (voir [Étapes de validation](#sdk_validate_card) ci-dessous) et stocke la carte dans la base de données. La carte se retrouve à l'état `validated` et nécessite l'approbation d'un admin avant de pouvoir être utilisée dans les workflows.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `app_manifest` | object | Oui | Manifeste de l'application avec id, nom, version, infos partenaire |
| `card_manifest` | object | Oui | Manifeste de la carte avec id, titre, entry\_point, class\_name, args |
| `card_type` | string | Oui | `action` ou `condition` |
| `source_code` | string | Oui | Code source Python (doit étendre `PartnerCard`) |
| `test_code` | string | Oui | Code de test Pytest pour la carte |
| `locales` | object | Non | Traductions locales, ex. `{"en": {...}, "de": {...}}` |

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
`CardStatus` possède trois valeurs qui se mappent directement sur les arêtes de workflow :

| Statut | Arête prise | À utiliser pour |
|--------|------------|------------|
| `SUCCESS` | `success` | La carte a réussi — s'applique aux conditions et aux actions. |
| `FAILED` | `failed_condition` | **Cartes de condition uniquement.** La condition a été évaluée à false — le workflow prend la branche « else ». Les cartes d'action n'ont pas de handle `failed_condition`, donc renvoyer `FAILED` depuis une action laisse l'exécution sans sortie. |
| `ERROR` | `error` | Une erreur d'exécution inattendue (exception). S'applique aux conditions et aux actions. |

En bref : les actions renvoient `SUCCESS` ou `ERROR` ; les conditions peuvent en plus renvoyer `FAILED`.
{% endhint %}

### sdk\_validate\_card

Exécuter le pipeline de validation sur une carte partenaire sans l'enregistrer. Deux modes :

- **Mode A** — Valider une carte existante par son ID
- **Mode B** — Valider du nouveau code source en mode inline

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `card_id` | string | Non | UUID d'une carte existante (Mode A) |
| `app_manifest` | object | Non | Manifeste de l'application (Mode B) |
| `card_manifest` | object | Non | Manifeste de la carte (Mode B) |
| `card_type` | string | Non | `action` ou `condition` (Mode B) |
| `source_code` | string | Non | Code source Python (Mode B) |
| `test_code` | string | Non | Code de test (Mode B) |

{% hint style="info" %}
Fournissez soit `card_id` seul (Mode A), soit `app_manifest` + `card_manifest` + `source_code` ensemble (Mode B).
{% endhint %}

**Étapes de validation :**

1. **Structure** — Vérifie la disposition des fichiers, le schéma du manifeste (`app.json`, `.docflowcompose/flow/...`) et que les entry points déclarés existent.
2. **Locales** — Réconcilie les clés de traduction utilisées dans la carte avec les fichiers `locales/<lang>.json` ; échoue si une clé manque dans une langue déclarée.
3. **AST Analysis** — Parcourt chaque fichier `.py` sous `src/` et vérifie les imports interdits, les appels dangereux et les exigences de hiérarchie de classes / signatures de méthodes.
4. **Dependencies** — Valide que tous les imports se résolvent en modules autorisés depuis la liste blanche du SDK.
5. **Tests** — Exécute la suite pytest de la carte sous des rlimits réduits.
6. **Behavioral** — Exécute la carte dans la sandbox de production contre un contexte fictif minimal pour confirmer le comportement à l'exécution.

Les étapes s'exécutent dans l'ordre ; la première étape en échec court-circuite les suivantes. L'étape 6 (Behavioral) est également réexécutée au moment de l'approbation comme contrôle de défense en profondeur avant que la carte ne soit activée.

### sdk\_test\_card

Exécuter une carte partenaire dans un environnement sandboxé avec un contexte fictif. La sandbox applique des builtins restreints, une liste blanche d'imports curée, un timeout d'exécution et des limites réduites de ressources processus — les mêmes restrictions sous lesquelles une carte tourne une fois approuvée.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `card_id` | string | Non | UUID d'une carte existante (Mode A) |
| `source_code` | string | Non | Code source pour le test inline (Mode B) |
| `class_name` | string | Non | Nom de classe pour le test inline (Mode B) |
| `variables` | object | Non | Variables à passer au constructeur de la carte |
| `mock_context` | object | Non | Contexte d'exécution fictif |

**Champs du mock context :**

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

L'outil retourne `execution_success` (indique si la sandbox a exécuté la carte jusqu'au bout — un timeout, une violation d'import ou une exception levée le met à `false`), `card_status` (le `CardStatus` retourné par `execute()` lui-même), le `message` et `data` de la carte, les `logs` capturés et `execution_time_ms`.

### sdk\_import\_github

Importer une application partenaire depuis un dépôt GitHub. Clone le dépôt, lit `app.json` et importe toutes les cartes trouvées dans le répertoire `.docflowcompose`.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `github_url` | string | Oui | URL HTTPS GitHub (ex. `https://github.com/org/repo`) |
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

Lister toutes les soumissions de cartes partenaires pour l'organisation courante.

**Paramètres :** Aucun

### sdk\_get\_submission\_status

Obtenir le statut de validation et le rapport pour une soumission de carte partenaire spécifique.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `card_id` | string | Oui | UUID de la carte partenaire |

### sdk\_approve\_card

Approuver une carte partenaire validée et l'activer. L'approbation réexécute la validation AST et comportementale comme contrôle de défense en profondeur, définit `partner_status = approved` et `enabled = true`, et enregistre la carte dans le registre d'exécution. Une fois approuvée, la carte apparaît dans `list_cards` pour **chaque organisation**, pas seulement pour celle qui l'a soumise.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `card_id` | string | Oui | UUID de la carte partenaire |

{% hint style="warning" %}
Nécessite des privilèges d'admin de l'organisation. La carte doit être à l'état `validated`. Les cartes rejetées doivent être re-téléchargées et re-validées avant de pouvoir être approuvées.
{% endhint %}

### sdk\_reject\_card

Rejeter une soumission de carte partenaire et la désactiver.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `card_id` | string | Oui | UUID de la carte partenaire |
| `reason` | string | Non | Raison du rejet |

{% hint style="warning" %}
Nécessite des privilèges d'admin de l'organisation.
{% endhint %}

### sdk\_delete\_submission

Supprimer en douceur une soumission de carte partenaire, quel que soit son état actuel. Définit `partner_status = deleted`, `enabled = false` et `deprecated = true`. La ligne est conservée à des fins d'audit, mais masquée des listes de soumissions et de `list_cards`.

**Paramètres :**

| Paramètre | Type | Obligatoire | Description |
|-----------|------|-------------|-------------|
| `card_id` | string | Oui | UUID de la carte partenaire |

{% hint style="warning" %}
Nécessite des privilèges d'admin de l'organisation.
{% endhint %}

### sdk\_list\_cards\_picker

Lister toutes les cartes activées, non obsolètes, avec leurs drapeaux de rôle. Utile pour déterminer quelles cartes peuvent être utilisées dans quels types de nœuds lors de la construction des workflows.

**Paramètres :** Aucun

## Fonctionnalités actuelles & feuille de route

Le Partner Card SDK est déployé de manière incrémentale. Voici ce sur quoi votre carte peut compter aujourd'hui et ce qui est encore en cours d'intégration :

| Fonctionnalité | Statut |
|------------|--------|
| **Conditions sur les champs** — lire les champs de document depuis `context.document_fields` et brancher selon leurs valeurs dans les cartes de condition | ✅ Implémenté |
| **Requêtes HTTP sortantes** — appeler des services externes depuis une carte | 🚧 En cours d'ajout |
| **Informations document étendues** — métadonnées document supplémentaires (au-delà de `document_id`, `document_type` et `document_fields`) exposées sur `ExecutionContext` | 🚧 En cours d'ajout |
| **Helpers de lookup sur tables de base de données** — helpers intégrés pour lire depuis les tables master-data / lookup DocBits depuis une carte | 📅 Prévu pour 1.1 |
| **Visualiseur du code source de carte partenaire** — vue en lecture seule du code de carte partenaire soumis dans l'interface DocBits, pour que les admins puissent inspecter ce qu'ils approuvent | 📅 Prévu pour 1.1 |

{% hint style="info" %}
Si votre carte a besoin d'une fonctionnalité encore en cours, elle échouera à la validation (import interdit, attribut de contexte manquant ou restriction de sandbox) jusqu'à ce que la partie correspondante soit livrée. Cette page sera mise à jour au fur et à mesure de la livraison de chaque fonctionnalité.
{% endhint %}

{% hint style="danger" %}
**Les cartes partenaires exécutent du code tiers — utilisation à vos propres risques.**

Les cartes téléchargées via le Partner Card SDK ne sont que **partiellement validées par DocBits**. Le pipeline de validation contrôle la structure, les locales, les imports, les motifs AST, les dépendances, les tests propres à la carte et une exécution comportementale de smoke dans la sandbox — il ne constitue **pas** un audit de sécurité complet ni une garantie fonctionnelle de la logique métier de la carte.

Une fois qu'un admin d'organisation approuve une carte partenaire, celle-ci devient disponible pour chaque organisation de la plateforme et tourne dans la sandbox de production contre des documents réels. Approuver et activer une carte partenaire est donc une décision de confiance explicite de la part de l'admin qui approuve. DocBits n'accepte aucune responsabilité pour la perte de données, le routage incorrect, les informations divulguées ou tout autre résultat causé par une carte partenaire que vous choisissez d'installer ou d'approuver.

Si vous n'êtes pas l'auteur d'origine de la carte, examinez la source (et, une fois la version 1.1 livrée, utilisez le visualiseur du code source de carte partenaire) avant de l'approuver.
{% endhint %}
