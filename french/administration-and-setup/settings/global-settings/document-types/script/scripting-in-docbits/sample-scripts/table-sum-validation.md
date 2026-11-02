# Validation de la Somme du Tableau

## Que fait ce script ?

Valide que la somme de tous les totaux de lignes dans le tableau de facture correspond au montant net du document. S'il y a un écart supérieur à 0,01, la somme calculée remplace le montant net extrait — garantissant la cohérence entre les postes et les champs d'en-tête.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script complet

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Calculer la somme de tous les totaux de lignes
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Comparer avec le montant net extrait
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # La somme des lignes diffère de l'en-tête — mettre à jour le montant net
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Variante : Marquer comme invalide au lieu d'écraser

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        diff = abs(float(net_amount) - total)
        if diff > 0.01:
            set_field_as_invalid(document_data, "net_amount",
                f"Line total sum ({round(total, 2)}) differs from net amount ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Amounts match")
    except ValueError:
        pass
```

## Explication étape par étape

1. **Obtenir le tableau de facture** depuis `tables_dict`
2. **Additionner toutes les valeurs LINE_TOTAL** sur les lignes du tableau
3. **Comparer** la somme calculée avec le montant net extrait
4. **Mettre à jour ou signaler** — soit remplacer le montant net, soit le marquer comme invalide

## Fonctions utilisées

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Lire les valeurs des colonnes depuis les lignes
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Lire le montant net
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Définir le montant corrigé
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Marquer le champ comme invalide
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Marquer le champ comme valide
