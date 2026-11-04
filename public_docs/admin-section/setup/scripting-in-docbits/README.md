# Scripting in DocBits

## Guide de script DocBits

Bienvenue dans le guide de script DocBits ! Ici, vous apprendrez comment utiliser des scripts pour automatiser et améliorer le traitement de vos documents dans DocBits. Les scripts permettent la manipulation de champs personnalisés, la transformation des données et la mise en œuvre de la logique sur différents types de documents.

### Pour commencer

Les scripts dans DocBits sont écrits en Python. Ils interagissent avec les champs de document et les métadonnées pour effectuer une large gamme d'opérations, du simple formatage des données à la logique complexe.

#### Fonctions clés

* `get_field_value(fields_dict, field_name, default=None)`: Récupère la valeur d'un champ spécifié.
* `set_field_value(fields_dict, field_name, value)`: Définit la valeur d'un champ spécifié.
* `create_new_field(field_name, value)`: Crée un nouveau champ avec un nom et une valeur spécifiés.
* `format_decimal_to_locale(value, locale)`: Formate une valeur décimale selon une locale spécifiée.

### Exemples de scripts

Ci-dessous se trouvent plusieurs exemples illustrant des tâches de script courantes.

#### Exemple 1 : Mappage de devises pour les factures

Standardiser les symboles ou le texte de devise en codes de devise ISO.
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

