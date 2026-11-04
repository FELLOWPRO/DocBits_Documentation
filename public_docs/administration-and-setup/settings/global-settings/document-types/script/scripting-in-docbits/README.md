# Scripting dans DocBits

## Tutoriel vidéo : les fonctions de script les plus importantes

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-script-functions/v3/fr.mp4" %}
Les fonctions de script les plus importantes dans DocBits
{% endembed %}

La vidéo montre dans l'éditeur de scripts comment lire un champ (`get_field_value`), définir une valeur (`set_field_value`), calculer une date d'échéance (`set_date_value`), marquer un champ comme invalide (`set_field_as_invalid`) et rendre un champ obligatoire (`set_is_required`).

## Guide de Scripting DocBits

Bienvenue dans le guide de scripting DocBits ! Ici, vous apprendrez comment utiliser les scripts pour automatiser et améliorer votre traitement de documents dans DocBits. Les scripts permettent la manipulation personnalisée des champs, la transformation des données et l'implémentation de logique sur différents types de documents.

### Premiers pas

Les scripts dans DocBits sont écrits en Python. Ils interagissent avec les champs et les métadonnées des documents pour effectuer un large éventail d'opérations, de la simple mise en forme de données à la logique complexe.

#### Fonctions clés

Chaque script reçoit le document sous le nom `document_data`. Passez-le comme premier argument aux fonctions de champ. Vous trouverez la référence complète sur la page [Fonctions de Champ](field-functions.md).

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)` : Lit la valeur d'un champ.
* `set_field_value(document_data, field_name, value)` : Écrit une valeur dans un champ et crée le champ s'il n'existe pas.
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)` : Écrit une date, éventuellement avec des jours ajoutés et sans week-ends.
* `set_amount_value(document_data, field_name, value)` : Écrit un montant au format de la locale du document.
* `set_field_as_invalid(document_data, field_name, message, code=None)` : Marque un champ comme invalide et affiche le message à l'utilisateur.
* `set_is_required(document_data, field_name, value)` : Rend un champ obligatoire ou lève cette obligation.

### Exemples de Scripts

Voici plusieurs exemples illustrant les tâches de scripting courantes.

#### Exemple 1 : Mapping de devises pour les factures

Standardiser les symboles ou textes de devises en codes ISO de devises.

```python
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```
