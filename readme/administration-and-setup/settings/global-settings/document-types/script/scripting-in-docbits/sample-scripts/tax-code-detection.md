# Belastingcode Detectie

## Wat doet dit script?

Bepaalt automatisch de juiste belastingcode op basis van de volledige tekst van het document en de belasting-/nettobedragen. Detecteert verleggingsregelingscenario's, belastingvrije facturen en berekent het belastingtarief om de juiste code toe te wijzen (bijv. S1 voor 19%, S2 voor 7%).

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
# Volledige documenttekst en bedragen ophalen
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Regel 1: Verleggingsregeling detecteren via volledige tekst
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regel 2: Nul belasting = belastingvrij
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Regel 3: Belastingtarief berekenen uit bedragen
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Standaardtarief
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Verlaagd tarief
    else:
        set_field_value(document_data, "tax_code", "S3")    # Overig tarief
```

## Stapsgewijze Uitleg

1. **Volledige tekst lezen** met `get_document_content()` voor trefwoorddetectie
2. **Belasting- en nettobedragen lezen** voor belastingtariefberekening
3. **Controleren op verleggingsregeling** trefwoorden in de documenttekst (Duits en Engels)
4. **Controleren op nul belasting** — als het belastingbedrag 0 is, belastingvrije code toewijzen
5. **Belastingtarief berekenen** uit belasting/netto-verhouding en de bijbehorende code toewijzen

## Gebruikte Functies

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — OCR volledige tekst lezen
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Veldwaarden lezen
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Belastingcode instellen
