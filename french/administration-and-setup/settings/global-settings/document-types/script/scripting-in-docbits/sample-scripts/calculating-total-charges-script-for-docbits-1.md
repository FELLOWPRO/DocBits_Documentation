# Script de Calcul des Frais Totaux pour DocBits

Le script "Calcul des Frais Totaux" automatise le processus de sommation de divers frais et montants supplémentaires dans les documents de facture. Ce guide vous explique la configuration, la logique et l'application du script pour garantir des calculs précis des frais totaux dans vos documents.

### Objectif

Ce script vise à fournir une méthode dynamique pour calculer les frais totaux d'une facture en additionnant différents types de frais, tels que les frais de base, le fret (Fracht) et l'emballage (Verpackung). Il met ensuite à jour le champ des frais totaux de la facture avec la somme calculée, garantissant ainsi des informations de facturation précises.

### Aperçu du Script

Le script récupère les valeurs des champs spécifiés, les convertit en nombres à virgule flottante, les additionne, puis met à jour le champ `total_charges` avec le résultat. Si le champ `total_charges` n'existe pas, le script crée ce champ et définit sa valeur en conséquence.

#### Extrait de Code

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialiser le total à 0
total = 0

# Ajouter le fret au total s'il existe
if fracht:
    fracht = float(fracht)
    total += fracht

# Ajouter l'emballage au total s'il existe
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Formatage du total à deux décimales
formatted_total = "{0:.2f}".format(total)

# Vérifier si le champ total_charges existe et mettre à jour ou créer en conséquence
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
