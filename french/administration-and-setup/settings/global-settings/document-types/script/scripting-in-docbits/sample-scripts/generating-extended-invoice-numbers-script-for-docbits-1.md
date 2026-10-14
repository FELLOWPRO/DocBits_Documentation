# Script de Génération de Numéros de Facture Étendus pour DocBits

Ce document détaille le script "Génération de Numéros de Facture Étendus", qui automatise la création de numéros de facture étendus dans DocBits. Les numéros de facture étendus combinent plusieurs identifiants de documents, tels que l'ID de facture et le numéro de bon de commande, en un seul identifiant complet. Ce script améliore la traçabilité des documents et simplifie la tenue des registres.

### Objectif

L'objectif de ce script est de rationaliser le processus de génération de numéros de facture étendus en concaténant automatiquement l'ID de facture et le numéro de bon de commande, fournissant ainsi un identifiant unifié et unique pour chaque document de facture.

### Aperçu du Script

Le script vérifie la présence des champs ID de facture et numéro de bon de commande dans le document, concatène leurs valeurs si les deux sont présents (séparés par un tiret), et met à jour ou crée un nouveau champ pour stocker la valeur combinée.

#### Extrait de Code

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combiner l'ID de facture et le numéro de bon de commande avec un tiret comme séparateur
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Vérifier s'il y a un numéro étendu à définir
if extended_number:
    # Mettre à jour le champ 'invoice_extended_number' avec la valeur combinée
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```
