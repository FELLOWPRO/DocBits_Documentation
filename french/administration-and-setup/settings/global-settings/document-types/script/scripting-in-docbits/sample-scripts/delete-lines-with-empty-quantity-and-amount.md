# Supprimer les lignes avec quantité et montant vides

#### Partie 1 : Supprimer les Lignes avec Quantité et Montant Vides

Cette section du script traite un tableau de facture pour supprimer toutes les lignes où la quantité et le montant total sont nuls ou non fournis.

* **Vérifier INVOICE\_TABLE :** Il commence par vérifier si la clé `INVOICE_TABLE` existe dans le dictionnaire `tables_dict`.
* **Itérer sur les Lignes :** Pour chaque ligne du tableau, le script initialise des indicateurs et des variables pour déterminer si les colonnes `TOTAL_AMOUNT` et `QUANTITY` existent et pour capturer leurs valeurs.
* **Vérifier les Noms de Colonnes :** En parcourant chaque colonne d'une ligne, il recherche les colonnes nommées `TOTAL_AMOUNT` et `QUANTITY`.
  * Si `TOTAL_AMOUNT` est trouvé, il capture la valeur. Si cette valeur n'est pas nulle, il la convertit en nombre à virgule flottante.
  * De même pour `QUANTITY`, en capturant et convertissant la valeur si elle n'est pas nulle.
* **Marquer la Ligne pour Suppression :** Après avoir vérifié les deux colonnes d'une ligne, si le montant total et la quantité sont effectivement nuls (soit en étant zéro, soit en n'existant pas), la ligne est marquée pour suppression en définissant `row['is_deleted']` à `True`.

#### Partie 2 : Valider le Total des Lignes par rapport au Total de la Facture

Cette section calcule le montant total de toutes les lignes d'une facture et le compare au total déclaré de la facture pour valider leur cohérence.

* **Initialiser le Total des Lignes :** Commence par définir une variable `lines_total` à 0.0 pour accumuler le montant total de toutes les lignes.
* **Additionner les Montants des Lignes :** Parcourt chaque ligne de `INVOICE_TABLE`, extrait le `TOTAL_AMOUNT` de chacune et l'ajoute à `lines_total`.
* **Récupérer et Convertir le Total de la Facture :** Obtient le montant total de la facture en utilisant une fonction auxiliaire `get_field_value` et le convertit en nombre à virgule flottante.
* **Comparer les Totaux :** Enfin, il vérifie si la différence absolue entre le total calculé des lignes (`lines_total`) et le total déclaré de la facture (`total_amount`) dépasse un seuil de 0,05. Si c'est le cas, il marque le champ du total de la facture comme invalide en utilisant une autre fonction auxiliaire `set_field_as_invalid`, citant un écart.

```python
##################################################
# Supprimer les lignes avec quantité et montant vides
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
# Fin : Supprimer les lignes avec quantité et montant vides
##################################################

##################################################
# Validation du total des lignes par rapport au total de la facture
##################################################
lines_total = 0.0
# Obtenir le total des lignes
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

# Obtenir le total de la facture
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Comparer le total des lignes avec le total de la facture
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# Fin : Validation du total des lignes par rapport au total de la facture
##################################################
```

#### Résumé

Le script assure efficacement l'intégrité des données en :

1. Supprimant les lignes de données qui ne contribuent pas au total financier de la facture en raison de quantités ou montants manquants.
2. Validant la cohérence entre la somme des montants individuels des lignes et le total global de la facture, en mettant en évidence les écarts pour des actions ultérieures.

Cette automatisation aide à maintenir des registres financiers précis et peut être cruciale pour les systèmes tels que les ERP qui nécessitent des données précises pour la comptabilité et les rapports financiers.
