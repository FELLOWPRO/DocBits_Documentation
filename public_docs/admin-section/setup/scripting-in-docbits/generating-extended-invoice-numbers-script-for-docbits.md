# Génération de script de numéros de facture étendus pour Docbits

### Aperçu

Ce guide se concentre sur l'automatisation de la création de numéros de facture étendus dans Docbits, une fonctionnalité cruciale pour améliorer la gestion et le suivi des factures. Le script "Génération de numéros de facture étendus" concatène divers identifiants de documents, tels que l'ID de facture et le numéro de bon de commande, pour créer un identifiant complet et unique pour chaque facture.

### Objectif

L'objectif principal de ce script est d'automatiser la génération de numéros de facture étendus, facilitant le suivi et la gestion des factures en combinant plusieurs identifiants en un seul numéro unique.

### Implémentation du script

#### Extrait de code
```python
# Retrieve the values of invoice ID and purchase order number from the document
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Concatenate the invoice ID and purchase order number with a hyphen if both exist
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check and update the 'invoice_extended_number' field with the concatenated value
if extended_number:
if 'invoice_extended_number' not in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

