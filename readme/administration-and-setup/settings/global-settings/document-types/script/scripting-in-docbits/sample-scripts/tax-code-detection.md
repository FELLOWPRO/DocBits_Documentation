# Detekcija poreskog koda

## Sta ova skripta radi?

Automatski odredjuje ispravan poreski kod na osnovu celokupnog teksta dokumenta i iznosa poreza/neto. Detektuje scenarije obrnutog zaracunavanja poreza, fakture oslobodjene poreza i izracunava poresku stopu za dodeljivanje odgovarajuceg koda (npr. S1 za 19%, S2 za 7%).

## Okidac

`AFTER_FORMATTING` na tipu dokumenta **INVOICE**

## Kompletna skripta

```python
# Preuzimanje celokupnog teksta dokumenta i iznosa
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Pravilo 1: Detekcija obrnutog zaracunavanja putem celokupnog teksta
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Pravilo 2: Nulti porez = oslobodjeno od poreza
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Pravilo 3: Izracunavanje poreske stope iz iznosa
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Standardna stopa
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Smanjena stopa
    else:
        set_field_value(document_data, "tax_code", "S3")    # Ostale stope
```

## Objasnjenje korak po korak

1. **Citanje celokupnog teksta** sa `get_document_content()` za detekciju kljucnih reci
2. **Citanje iznosa poreza i neto iznosa** za izracunavanje poreske stope
3. **Provera kljucnih reci za obrnuto zaracunavanje** u tekstu dokumenta (nemacki i engleski)
4. **Provera nultog poreza** -- ako je iznos poreza 0, dodeljuje kod za oslobodjenje od poreza
5. **Izracunavanje poreske stope** iz odnosa porez/neto i dodeljivanje odgovarajuceg koda

## Koriscene funkcije

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) -- Citanje OCR celokupnog teksta
- [get\_field\_value()](../field-functions.md#get\_field\_value) -- Citanje vrednosti polja
- [set\_field\_value()](../field-functions.md#set\_field\_value) -- Postavljanje poreskog koda
