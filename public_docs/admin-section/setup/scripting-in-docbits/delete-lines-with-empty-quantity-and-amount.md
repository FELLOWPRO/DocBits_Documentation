# Supprimer les lignes avec une quantité et un montant vides

#### Partie 1 : Supprimer les lignes avec une quantité et un montant vides

Cette section du script traite une table de facturation pour supprimer toutes les lignes où à la fois la quantité et le montant total sont nuls ou non fournis.

* **Vérifier la table de FACTURATION :** Il commence par vérifier si la clé `INVOICE_TABLE` existe dans le dictionnaire `tables_dict`.
* **Itérer sur les lignes :** Pour chaque ligne dans la table, le script initialise des indicateurs et des variables pour déterminer si les colonnes `TOTAL_AMOUNT` et `QUANTITY` existent et pour capturer leurs valeurs.
* **Vérifier les noms de colonnes :** En parcourant chaque colonne dans une ligne, il recherche les colonnes nommées `TOTAL_AMOUNT` et `QUANTITY`.
* Si `TOTAL_AMOUNT` est trouvé, il capture la valeur. Si cette valeur est non nulle, elle est convertie en flottant.
* De même pour `QUANTITY`, en capturant et convertissant la valeur si elle est non nulle.
* **Marquer la ligne pour suppression :** Après avoir vérifié les deux colonnes dans une ligne, si à la fois le montant total et la quantité sont effectivement nuls (soit en étant nuls, soit en n'existant pas), la ligne est marquée pour suppression en définissant `row['is_deleted']` sur `True`.

#### Partie 2 : Valider le total de la ligne par rapport au total de la facture

Cette section calcule le montant total de toutes les lignes d'une facture et le compare au total déclaré de la facture pour valider leur cohérence.

* **Initialiser le total de la ligne :** Commence par définir une variable `lines_total` à 0.0 pour accumuler le montant total de toutes les lignes.
* **Additionner les montants des lignes :** Itère sur chaque ligne dans la `INVOICE_TABLE`, extrait le `TOTAL_AMOUNT` de chacune et l'ajoute à `lines_total`.
* **Récupérer et convertir le total de la facture :** Récupère le montant total de la facture en utilisant une fonction auxiliaire `get_field_value` et le convertit en flottant.
* **Comparer les totaux :** Enfin, il vérifie si la différence absolue entre le total de la ligne calculé (`lines_total`) et le total de la facture déclaré (`total_amount`) dépasse un seuil de 0,05. Si c'est le cas, il marque le champ du total de la facture comme invalide en utilisant une autre fonction auxiliaire `set_field_as_invalid`, citant une incohérence.
```python
##################################################
# Delete lines with empty quantity and amount
##################################################


if tables_dict.get('INVOICE_TABLE'):
for row in tables_dict['INVOICE_TABLE']['rows']:
amount_col_found = False
quantity_col_found = False
line_amount = 0.0
line_quantity = 0.0
for col in row['columns']:
if col['name'] == 'TOTAL_AMOUNT':
amount_col_found = True
line_amount = col.get('value', 0)
if line_amount:
line_amount = float(line_amount)
if col['name'] == 'QUANTITY':
quantity_col_found = True
line_quantity = col.get('value', 0)
if line_quantity:
line_quantity = float(line_quantity)
if amount_col_found and quantity_col_found:
break
if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
row['is_deleted'] = True

##################################################
# End: Delete lines with empty quantity and amount
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
if tables_dict.get('INVOICE_TABLE'):
for row in tables_dict['INVOICE_TABLE']['rows']:
line_amount = 0.0
for col in row['columns']:
if col['name'] == 'TOTAL_AMOUNT':
line_amount = col.get('value', 0)
if line_amount:
line_amount = float(line_amount)
break
lines_total += line_amount

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
total_amount = float(total_amount)

# Comparing lines total with invoice total
if abs(total_amount - lines_total) > 0.05:
set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################







```
#### Résumé

Le script garantit efficacement l'intégrité des données en :

1. Supprimant les lignes de données qui ne contribuent pas au total financier de la facture en raison de quantités ou montants manquants.
2. Validant la cohérence entre la somme des montants de ligne individuels et le total global de la facture, en mettant en évidence les écarts pour une action ultérieure.

Cette automatisation aide à maintenir des dossiers financiers précis et peut être cruciale pour des systèmes comme les ERP qui nécessitent des données précises pour la comptabilité et les rapports financiers.
