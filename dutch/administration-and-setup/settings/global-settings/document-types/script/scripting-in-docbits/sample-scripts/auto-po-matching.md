# Automatische PO-Matching

## Wat doet dit script?

Start automatisch PO (Purchase Order)-matching wanneer een PO-nummer aanwezig is op de factuur. De po-match-service microservice vergelijkt factuurregelitems met de PO en vult de matchresultaten in.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
# PO-nummer uit het document lezen
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # PO-nummer opschonen: voorvoegsel en witruimte verwijderen
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Opgeschoond PO-nummer bijwerken
    set_field_value(document_data, "purchase_order", po_nr)

    # Automatische PO-matching activeren
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Stapsgewijze Uitleg

1. **PO-nummer lezen** van de factuur
2. **Opschonen** van het PO-nummer door veelvoorkomende voorvoegsels zoals "PO-" of "PO " te verwijderen
3. **Bijwerken** van het opgeschoonde PO-nummer terug naar het document
4. **PO-matching activeren** die de po-match-service aanroept om factuurregels te vergelijken met PO-regels

## Wat gebeurt er na matching?

De `document_data` wordt bijgewerkt met:
- `po_items` — Gematchte PO-regelitems
- `po_match_status` — Matchresultaat (`"matched"`, `"partially_matched"`, enz.)
- `po_multi_matched` — Of meerdere PO's zijn gematcht

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Veldwaarde lezen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Opgeschoond PO-nummer schrijven
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — PO-matching activeren
