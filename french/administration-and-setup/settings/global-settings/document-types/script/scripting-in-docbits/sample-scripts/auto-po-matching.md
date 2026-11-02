# Correspondance Automatique des BC

## Que fait ce script ?

Déclenche automatiquement la correspondance BC (Bon de Commande) lorsqu'un numéro de BC est présent sur la facture. Le microservice po-match-service compare les postes de la facture avec le BC et remplit les résultats de correspondance.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script complet

```python
# Lire le numéro de BC depuis le document
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # Nettoyer le numéro de BC : supprimer le préfixe et les espaces
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Mettre à jour le numéro de BC nettoyé
    set_field_value(document_data, "purchase_order", po_nr)

    # Déclencher la correspondance automatique des BC
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Explication étape par étape

1. **Lire le numéro de BC** depuis la facture
2. **Nettoyer** le numéro de BC en supprimant les préfixes courants comme "PO-" ou "PO "
3. **Mettre à jour** le numéro de BC nettoyé dans le document
4. **Déclencher la correspondance BC** qui appelle le po-match-service pour comparer les lignes de facture avec les lignes du BC

## Que se passe-t-il après la correspondance ?

Le `document_data` est mis à jour avec :
- `po_items` — Postes BC mis en correspondance
- `po_match_status` — Résultat de la correspondance (`"matched"`, `"partially_matched"`, etc.)
- `po_multi_matched` — Si plusieurs BC ont été mis en correspondance

## Fonctions utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Lire la valeur du champ
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Écrire le numéro de BC nettoyé
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — Déclencher la correspondance BC
