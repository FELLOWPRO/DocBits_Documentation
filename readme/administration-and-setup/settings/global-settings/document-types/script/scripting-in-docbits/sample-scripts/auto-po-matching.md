# Automatsko uparivanje narudzbenica

## Sta ova skripta radi?

Automatski pokrece uparivanje narudzbenica (PO) kada je broj narudzbenice prisutan na fakturi. Mikroservis po-match-service uporedjuje stavke fakture sa stavkama narudzbenice i popunjava rezultate uparivanja.

## Okidac

`AFTER_FORMATTING` na tipu dokumenta **INVOICE**

## Kompletna skripta

```python
# Citanje broja narudzbenice iz dokumenta
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # Ciscenje broja narudzbenice: uklanjanje prefiksa i razmaka
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Azuriranje ociscenog broja narudzbenice
    set_field_value(document_data, "purchase_order", po_nr)

    # Pokretanje automatskog uparivanja narudzbenica
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Objasnjenje korak po korak

1. **Citanje broja narudzbenice** sa fakture
2. **Ciscenje** broja narudzbenice uklanjanjem uobicajenih prefiksa kao sto su "PO-" ili "PO "
3. **Azuriranje** ociscenog broja narudzbenice nazad u dokument
4. **Pokretanje uparivanja narudzbenica** koje poziva po-match-service za uporedjivanje stavki fakture sa stavkama narudzbenice

## Sta se desava posle uparivanja?

`document_data` se azurira sa:
- `po_items` -- Uparene stavke narudzbenice
- `po_match_status` -- Rezultat uparivanja (`"matched"`, `"partially_matched"` itd.)
- `po_multi_matched` -- Da li je upareno vise narudzbenica

## Koriscene funkcije

- [get\_field\_value()](../field-functions.md#get\_field\_value) -- Citanje vrednosti polja
- [set\_field\_value()](../field-functions.md#set\_field\_value) -- Pisanje ociscenog broja narudzbenice
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) -- Pokretanje uparivanja narudzbenica
