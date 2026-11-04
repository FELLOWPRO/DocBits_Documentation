# Auto-Export selon Conditions

## Que fait ce script ?

Définit automatiquement le statut du document à "prêt pour l'export" lorsque des conditions spécifiques sont remplies : le fournisseur est un vendeur connu/de confiance ET le montant de la facture est inférieur à un seuil. Cela permet de contourner la validation manuelle pour les factures à faible risque.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script complet

```python
# Lire les champs pertinents
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Définir les fournisseurs de confiance pour l'auto-export
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-export pour les fournisseurs connus avec de petits montants
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-exported (small amount, known supplier)"
    )
```

## Explication étape par étape

1. **Lire le montant net et le nom du fournisseur** depuis le document (fournisseur avec `is_clean=True` pour la comparaison)
2. **Définir les fournisseurs de confiance** — liste de noms de vendeurs connus (nettoyés/en majuscules)
3. **Vérifier les conditions** — le fournisseur doit être dans la liste de confiance ET le montant doit être inférieur à 500
4. **Changer le statut** à `"ready_for_export"` avec un message descriptif

{% hint style="warning" %}
**Attention :** Les changements de statut déclenchent des flux de travail en aval (DocFlow, hooks d'export). Assurez-vous que les conditions sont suffisamment strictes pour éviter les exports non intentionnels.
{% endhint %}

## Fonctions utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Lire les valeurs des champs
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Changer le statut du document
