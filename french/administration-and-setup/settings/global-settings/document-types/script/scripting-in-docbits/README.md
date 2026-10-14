# Scripting dans DocBits

## Guide de Scripting DocBits

Bienvenue dans le guide de scripting DocBits ! Ici, vous apprendrez comment utiliser les scripts pour automatiser et améliorer votre traitement de documents dans DocBits. Les scripts permettent la manipulation personnalisée des champs, la transformation des données et l'implémentation de logique sur différents types de documents.

### Premiers pas

Les scripts dans DocBits sont écrits en Python. Ils interagissent avec les champs et les métadonnées des documents pour effectuer un large éventail d'opérations, de la simple mise en forme de données à la logique complexe.

#### Fonctions clés

* `get_field_value(fields_dict, field_name, default=None)` : Récupère la valeur d'un champ spécifié.
* `set_field_value(fields_dict, field_name, value)` : Définit la valeur d'un champ spécifié.
* `create_new_field(field_name, value)` : Crée un nouveau champ avec un nom et une valeur spécifiés.
* `format_decimal_to_locale(value, locale)` : Formate une valeur décimale selon une locale spécifiée.

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
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(fields_dict, "currency", currency_value)
```
