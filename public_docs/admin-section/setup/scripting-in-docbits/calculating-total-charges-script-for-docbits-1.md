# Calcul du script des frais totaux pour Docbits

##

Le script "Calcul des frais totaux" automatise le processus de sommation des différents frais et montants supplémentaires dans les documents de facturation. Ce guide vous guide à travers la configuration du script, la logique et l'application pour garantir des calculs précis des frais totaux sur vos documents.

### Objectif

Ce script vise à fournir une manière dynamique de calculer les frais totaux sur une facture en additionnant différents types de frais, tels que les frais de base, le fret et l'emballage. Il met ensuite à jour le champ des frais totaux de la facture avec la somme calculée, garantissant des informations de facturation précises.

### Aperçu du script

Le script récupère les valeurs des champs spécifiés, les convertit en nombres décimaux, les additionne, puis met à jour le champ `total_charges` avec le résultat. Si le champ `total_charges` n'existe pas, le script crée ce champ et définit sa valeur en conséquence.

#### Extrait de code
```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
fracht = float(fracht)
total += fracht

# Add verpackung to total if it exists
if verpackung:
verpackung = float(verpackung)
total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

