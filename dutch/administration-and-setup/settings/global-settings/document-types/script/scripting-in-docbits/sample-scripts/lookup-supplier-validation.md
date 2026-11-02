# Leverancier Lookup Validatie

## Wat doet dit script?

Valideert het leveranciersnummer van de factuur tegen stamgegevens in de lookup-tabel. Als de leverancier wordt gevonden, worden de naam en betalingstermijnen automatisch ingevuld. Als de leverancier niet wordt gevonden, wordt het veld als ongeldig gemarkeerd zodat de gebruiker het kan corrigeren.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
# Leveranciers-ID uit het document lezen
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # De leverancier-lookuptabel bevragen
    records = get_lookup_records(
        org_id,                                    # Huidige organisatie
        document_json.get("sub_org_id"),           # Sub-org (indien van toepassing)
        "supplier",                                # Naam van de lookuptabel
        [["VENDOR_ID", supplier_id]],              # Filter: exacte match op VENDOR_ID
        limit=1                                    # Alleen de eerste match nodig
    )

    if records:
        # Leverancier gevonden — gerelateerde velden automatisch invullen
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Leverancier niet gevonden — als ongeldig markeren
        set_field_as_invalid(document_data, "supplier_id",
                             f"Leverancier '{supplier_id}' niet gevonden in stamgegevens")
```

## Stapsgewijze Uitleg

1. **Leveranciers-ID lezen** uit het document met `get_field_value()`
2. **Lookuptabel bevragen** met `get_lookup_records()` waarbij het leveranciersnummer als filter wordt gebruikt
3. **Bij overeenkomst**: Leveranciersnaam en betalingstermijnen automatisch invullen vanuit stamgegevens
4. **Bij geen overeenkomst**: Het leveranciers-ID-veld als ongeldig markeren met een beschrijvende foutmelding

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Veldwaarde lezen
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Stamgegevens bevragen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Veldwaarde schrijven
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Validatiefout tonen
