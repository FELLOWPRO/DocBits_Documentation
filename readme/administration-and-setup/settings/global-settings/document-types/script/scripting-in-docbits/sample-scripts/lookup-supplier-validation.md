# Validacija dobavljaca putem Lookup-a

## Sta ova skripta radi?

Validira broj dobavljaca sa fakture prema maticnim podacima u lookup tabeli. Ako je dobavljac pronadjen, njihovo ime i uslovi placanja se automatski popunjavaju. Ako nije pronadjen, polje se oznacava kao nevazece kako bi korisnik mogao da ga ispravi.

## Okidac

`AFTER_FORMATTING` na tipu dokumenta **INVOICE**

## Kompletna skripta

```python
# Citanje ID-a dobavljaca iz dokumenta
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Upit prema lookup tabeli dobavljaca
    records = get_lookup_records(
        org_id,                                    # Trenutna organizacija
        document_json.get("sub_org_id"),           # Podorganizacija (ako je primenljivo)
        "supplier",                                # Naziv lookup tabele
        [["VENDOR_ID", supplier_id]],              # Filter: tacno podudaranje po VENDOR_ID
        limit=1                                    # Potreban je samo prvi rezultat
    )

    if records:
        # Dobavljac pronadjen -- automatsko popunjavanje povezanih polja
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Dobavljac nije pronadjen -- oznaci kao nevazece
        set_field_as_invalid(document_data, "supplier_id",
                             f"Supplier '{supplier_id}' not found in master data")
```

## Objasnjenje korak po korak

1. **Citanje ID-a dobavljaca** iz dokumenta koriscenjem `get_field_value()`
2. **Upit prema lookup tabeli** sa `get_lookup_records()` koriscenjem ID-a dobavljaca kao filtera
3. **Kada se pronadje podudaranje**: Automatsko popunjavanje imena dobavljaca i uslova placanja iz maticnih podataka
4. **Kada nema podudaranja**: Oznacavanje polja ID-a dobavljaca kao nevazeceg sa opisnom porukom o gresci

## Koriscene funkcije

- [get\_field\_value()](../field-functions.md#get\_field\_value) -- Citanje vrednosti polja
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) -- Upit prema maticnim podacima
- [set\_field\_value()](../field-functions.md#set\_field\_value) -- Pisanje vrednosti polja
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) -- Prikazivanje greske validacije
