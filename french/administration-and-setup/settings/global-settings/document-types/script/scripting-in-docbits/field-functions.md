# Fonctions de Champ

Fonctions pour lire, écrire et contrôler les champs de document.

**Source :** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Lit la valeur d'un champ du document.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `document_data` | `dict` | L'objet de contexte `document_data` |
| `field_name` | `str` | Nom du champ (ex. `"invoice_id"`) |
| `default_value` | `any` | Valeur de retour si le champ est vide/manquant (par défaut : `None`) |
| `is_clean` | `bool` | Si `True` : la valeur est convertie en MAJUSCULES avec les espaces supprimés |

**Retourne :** La valeur du champ sous forme de chaîne, ou `default_value`

**Exemple — Lire le numéro de facture avec valeur par défaut :**

```python
# Lire le champ avec une valeur par défaut
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# Avec is_clean=True : "INV 001" devient "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**Ce qui se passe :** Retourne la valeur du champ. Lorsque `is_clean=True`, la valeur est transformée via `value.upper().replace(" ", "").strip()` — utile pour les comparaisons.

---

## set\_field\_value()

Définit la valeur d'un champ. Crée automatiquement le champ s'il n'existe pas.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `document_data` | `dict` | L'objet de contexte `document_data` |
| `field_name` | `str` | Nom du champ |
| `value` | `any` | Nouvelle valeur |
| `remove_link` | `bool` | Si `True` : supprime les coordonnées, la confiance, la règle, etc. |

**Retourne :** `True` si la valeur a changé, `False` si identique

**Effets de bord :**
- Définit `highlight_field = True` (indicateur visuel dans l'UI)
- Définit `extraction_method = "SCRIPT"`
- Définit `formatted_value = value`

**Exemple — Affectation conditionnelle de valeur :**

```python
# Définir l'ID de facture
set_field_value(document_data, "invoice_id", "INV-2026-001")

# Avec remove_link : supprime le lien OCR (coordonnées, confiance etc.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**Ce qui se passe :** La valeur du champ est mise à jour et marquée comme modifiée par script. Si le champ n'existe pas, il est automatiquement créé avec `extraction_method: "SCRIPT"` et ajouté à la fois à `fields` et `fields_dict`.

---

## set\_date\_value()

Définit une valeur de date avec formatage automatique et arithmétique de dates optionnelle.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `value` | `str` | Date ISO : `"2026-03-25"`. Si vide : date du jour |
| `add_days` | `int` | Jours à ajouter (ex. `30` pour les délais de paiement) |
| `skip_weekend` | `bool` | Ignorer les week-ends lors de l'ajout de jours |
| `exclude_final_days` | `str/list` | Jours supplémentaires à exclure (ex. `"MONDAY,FRIDAY"`) |

**Exemple — Calculer la date d'échéance de paiement (30 jours, sans week-ends) :**

```python
# Date d'échéance : 30 jours après la date de facture, sans les week-ends
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Définir la date de livraison à aujourd'hui
set_date_value(document_data, "delivery_date", None)  # None = aujourd'hui

# 14 jours, en excluant samedi et lundi
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**Ce qui se passe :** La date est calculée en ajoutant des jours (en sautant optionnellement les week-ends/jours spécifiques) et automatiquement formatée selon le `date_format_pattern` du document (ex. `%d.%m.%Y` pour l'Allemagne).

**Codes de jours pour `exclude_final_days` :**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Définit une valeur de montant avec formatage automatique selon la locale.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `value` | `str/number` | Montant en format anglais (ex. `"1234.56"`) |

**Exemple — Définir le montant net :**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value devient ex. "1.234,56" pour la locale de_DE
```

**Ce qui se passe :** Le montant est formaté selon `amount_format_locale` de `document_json` (ex. `de_DE`, `en_US`).

---

## create\_new\_field()

Crée un nouveau dictionnaire de champ (sans l'ajouter au document).

```python
create_new_field(field_name, value="")
```

**Retourne :** Dict avec `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Exemple :**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Alternative plus simple :** Utilisez `set_field_value()` à la place — elle crée automatiquement le champ s'il n'existe pas. `create_new_field()` n'est nécessaire que lorsque vous souhaitez manipuler manuellement le dictionnaire du champ.
{% endhint %}

---

## delete\_field()

Supprime un champ du document.

```python
delete_field(document_data, field_name)
```

**Retourne :** Tuple `(doc_json, fields_dict)` après la suppression

**Exemple :**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Marque un champ comme invalide avec un message d'erreur.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `message` | `str` | Message d'erreur (affiché dans l'UI) |
| `code` | `str` | Code d'erreur (par défaut : `INVALID_VALUE`) |

**Effets de bord :**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Exemple — Validation IBAN :**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN must be at least 15 characters",
                         "IBAN_TOO_SHORT")
```

**Ce qui se passe :** Le champ est surligné en rouge dans l'écran de validation avec le message d'erreur affiché à l'utilisateur.

---

## set\_field\_as\_valid()

Supprime le statut invalide d'un champ.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Exemple :**

```python
set_field_as_valid(document_data, "iban", "IBAN valid")
```

**Ce qui se passe :** Supprime `invalidated_by_script`, `validation_message`, `validation_code` et définit `is_valid = True`.

---

## set\_field\_attribute()

Définit un attribut arbitraire sur un champ.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Exemple :**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Voir la liste complète des [Attributs supportés](#supported-attributes) ci-dessous.

---

## set\_is\_required()

Rend un champ obligatoire ou supprime l'obligation.

```python
set_is_required(document_data, field_name, value)
```

**Exemple — Numéro de BC obligatoire pour les factures d'achat :**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Rend un champ en lecture seule ou modifiable.

```python
set_is_readonly(document_data, field_name, value)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = lecture seule, `False` = modifiable, `None` = supprimer l'attribut |

**Exemple :**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Masque ou affiche un champ dans l'UI.

```python
set_is_hidden(document_data, field_name, value)
```

**Exemple — Afficher les champs de sous-organisation uniquement quand c'est pertinent :**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Force la validation manuelle d'un champ.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = forcer la validation, `False` = supprimer |
| `reset_validation` | `bool` | Si `True` : réinitialise `is_validated` à `False` |

**Effets de bord quand `value=True` :**
- `force_validation = True`
- `is_valid = False` (si pas encore validé)
- `validation_code = "FORCED_VALIDATION"`

**Exemple — Forcer la validation pour les montants élevés :**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Attributs supportés

### Attributs de champ principaux

| Attribut | Type | Description |
| --------- | ---- | ----------- |
| `value` | any | La valeur brute du champ |
| `formatted_value` | string | Valeur formatée pour l'affichage |
| `content` | string | Contenu extrait original |
| `is_required` | bool | Si le champ est obligatoire |
| `is_valid` | bool | Statut de validation |
| `is_validated` | bool | Si le champ a été validé par l'utilisateur |
| `is_readonly` | bool | Si le champ est en lecture seule |
| `is_hidden` | bool | Si le champ est masqué dans l'UI |
| `force_validation` | bool | Forcer l'utilisateur à valider ce champ |
| `highlight_field` | bool | Mettre en surbrillance le champ dans l'UI |
| `extraction_method` | string | Comment la valeur a été extraite (ex. `"SCRIPT"`) |

### Attributs de validation

| Attribut | Type | Description |
| --------- | ---- | ----------- |
| `validation_message` | string | Message d'erreur affiché à l'utilisateur |
| `validation_code` | string | Code d'erreur (ex. `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Marque le champ comme invalidé par un script |

### Attributs d'extraction/OCR

| Attribut | Type | Description |
| --------- | ---- | ----------- |
| `coords` | object | Coordonnées de la boîte englobante sur le document |
| `confidence` | float | Score de confiance OCR/extraction |
| `score` | float | Score de correspondance/validation |
| `score_description` | string | Description du score |
| `page` | int | Numéro de page où le champ a été trouvé |
| `rule` | string | Règle d'extraction qui a été appliquée |
