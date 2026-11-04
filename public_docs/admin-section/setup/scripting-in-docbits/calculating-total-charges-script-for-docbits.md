# Calcul de script des frais totaux pour Docbits

### Introduction

Ce document fournit un guide détaillé sur le script "Calcul des frais totaux" au sein de la plateforme Docbits. Le script est conçu pour calculer automatiquement le montant total facturé sur une facture en additionnant divers frais individuels. Cette automatisation améliore la précision et l'efficacité du traitement des documents.

### Objectif

L'objectif de ce script est de rationaliser le processus de calcul des frais totaux sur les factures. En ajoutant automatiquement des frais spécifiés, tels que les frais de base, les taxes et les frais supplémentaires, le script garantit que les frais totaux reflétés sur chaque facture sont précis et complets.

### Détails du script

#### Implémentation du code
```python
# Initialize variables to store the values of individual charges
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Calculate the total by converting each charge to a float and summing them up
total = 0
if fracht:
total += float(fracht)
if verpackung:
total += float(verpackung)

# Format the total to two decimal places and update the 'total_charges' field
formatted_total = "{0:.2f}".format(total)
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

