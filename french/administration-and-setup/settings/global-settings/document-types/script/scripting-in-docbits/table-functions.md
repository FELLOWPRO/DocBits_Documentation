# Fonctions de Tableau

Fonctions pour lire, écrire et manipuler les tables et les lignes de table.

**Source :** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Lit la valeur d'une colonne d'une ligne de table.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `row` | `dict` | Un objet ligne de `table["rows"]` |
| `column_name` | `str` | Nom de la colonne (insensible à la casse) |
| `default_value` | `any` | Valeur de retour si la colonne est vide/manquante |
| `is_clean` | `bool` | Si `True` : MAJUSCULES avec espaces supprimés |

**Exemple — Itérer sur les lignes de table :**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
La comparaison des noms de colonnes est **insensible à la casse** : `"DESCRIPTION"` correspond aussi à `"description"` ou `"Description"`.
{% endhint %}

---

## set\_column\_value()

Définit la valeur d'une colonne dans une ligne de table.

```python
set_column_value(row, column_name, value)
```

**Retourne :** `True` si la valeur a changé, `False` si identique

**Effets de bord :**
- Définit `extraction_method = "SCRIPT"`
- Crée automatiquement la colonne si elle n'existe pas

**Exemple — Calculer les totaux de ligne :**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
        try:
            total = float(qty) * float(price)
            set_column_value(row, "LINE_TOTAL", str(total))
        except ValueError:
            pass
```

---

## set\_column\_date\_value()

Définit une valeur de date dans une cellule de table avec formatage et arithmétique de dates.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Requis pour `date_format_pattern` |
| `row` | `dict` | Ligne de table |
| `column_name` | `str` | Nom de la colonne |
| `value` | `str` | Date ISO `"2026-03-25"` |
| `add_days` | `int` | Jours à ajouter |
| `skip_weekend` | `bool` | Ignorer les week-ends |
| `exclude_final_days` | `str/list` | Jours à exclure |

**Exemple — Calculer les dates de livraison par ligne :**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Définit une valeur de montant dans une cellule de table avec formatage selon la locale.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Exemple — Calculer et formater les totaux de ligne :**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` est automatiquement converti en `str()` avant d'être défini.
{% endhint %}

---

## add\_table\_column()

Ajoute une nouvelle colonne à toutes les lignes d'une table.

```python
add_table_column(table, col_name, default_value=None)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `table` | `dict` | L'objet table (pas `tables_dict` !) |
| `col_name` | `str` | Nom de la nouvelle colonne |
| `default_value` | `any` | Valeur initiale pour toutes les lignes |

**Effets de bord :**
- `is_extra_column = True` (marqué comme non original)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Exemple — Ajouter une colonne de code fiscal :**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Maintenant définir les valeurs par ligne
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Protection contre les doublons :** Si la colonne existe déjà (vérification insensible à la casse), elle ne sera **pas** ajoutée à nouveau.
{% endhint %}

---

## remove\_rows\_from\_table()

Supprime un nombre spécifique de lignes d'une table.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `table_name` | `str` | Nom de la table |
| `count` | `int` | Nombre de lignes à supprimer |
| `start` | `int` | Index de départ (basé sur 0) |

**Lève :** `ValueError` si `start` ou `count` est hors limites

**Exemple — Supprimer les lignes d'en-tête ou la dernière ligne :**

```python
# Supprimer les 2 premières lignes (ex. lignes d'en-tête)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Supprimer la dernière ligne
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Conserve uniquement une ligne spécifique et supprime toutes les autres.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Paramètres :**

| Nom | Type | Description |
| ---- | ---- | ----------- |
| `line_number` | `int` | Numéro de ligne (basé sur 1 !) |

{% hint style="warning" %}
`line_number=1` conserve la première ligne. Ne pas confondre avec les indices basés sur 0.
{% endhint %}

**Exemple :**

```python
# Conserver uniquement la 3ème ligne
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Supprime toutes les tables du document (avec sauvegarde).

```python
delete_tables(document_data)
```

**Effets de bord :**
- Sauvegarde les tables sous `last_deleted_table`
- Supprime `po_items`, `po_multi_matched`, `po_match_status`

**Exemple :**

```python
# Supprimer les tables (ex. pour les factures de coûts sans postes)
delete_tables(document_data)
```

---

## restore\_tables()

Restaure les tables précédemment supprimées avec `delete_tables()`.

```python
restore_tables(document_data)
```

**Exemple :**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Modèle Supprimer + Restaurer :** Utile lorsque vous souhaitez supprimer temporairement des tables et les restaurer sous certaines conditions.
{% endhint %}

---

## Modèles courants

### Calculer la somme d'une colonne

```python
table = tables_dict.get("INVOICE_TABLE")
total = 0
if table:
    for row in table["rows"]:
        val = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(val)
        except ValueError:
            pass
    set_field_value(document_data, "calculated_total", str(round(total, 2)))
```

### Filtrer les lignes vides

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Supprimer de l'arrière vers l'avant
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Calculer une colonne à partir d'autres colonnes

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_AMOUNT", "0")
    for row in table["rows"]:
        net = float(get_column_value(row, "NET_AMOUNT", "0"))
        tax_rate = float(get_column_value(row, "TAX_RATE", "0"))
        tax = net * tax_rate / 100
        set_column_amount_value(document_data, row, "TAX_AMOUNT", tax)
```
