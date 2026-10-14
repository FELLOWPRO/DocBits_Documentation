# Validation de Fournisseur par Lookup

## Que fait ce script ?

Valide le numéro de fournisseur de la facture par rapport aux données de référence dans la table de recherche. Si le fournisseur est trouvé, son nom et ses conditions de paiement sont automatiquement remplis. S'il n'est pas trouvé, le champ est marqué comme invalide afin que l'utilisateur puisse le corriger.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script complet

```python
# Lire l'ID du fournisseur depuis le document
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Interroger la table de recherche des fournisseurs
    records = get_lookup_records(
        org_id,                                    # Organisation actuelle
        document_json.get("sub_org_id"),           # Sous-org (le cas échéant)
        "supplier",                                # Nom de la table de recherche
        [["VENDOR_ID", supplier_id]],              # Filtre : correspondance exacte sur VENDOR_ID
        limit=1                                    # Seule la première correspondance est nécessaire
    )

    if records:
        # Fournisseur trouvé — remplir automatiquement les champs associés
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Fournisseur non trouvé — marquer comme invalide
        set_field_as_invalid(document_data, "supplier_id",
                             f"Supplier '{supplier_id}' not found in master data")
```

## Explication étape par étape

1. **Lire l'ID du fournisseur** depuis le document avec `get_field_value()`
2. **Interroger la table de recherche** avec `get_lookup_records()` en utilisant l'ID fournisseur comme filtre
3. **En cas de correspondance** : Remplir automatiquement le nom du fournisseur et les conditions de paiement depuis les données de référence
4. **En cas de non-correspondance** : Marquer le champ ID fournisseur comme invalide avec un message d'erreur descriptif

## Fonctions utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Lire la valeur du champ
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Interroger les données de référence
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Écrire la valeur du champ
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Afficher une erreur de validation
