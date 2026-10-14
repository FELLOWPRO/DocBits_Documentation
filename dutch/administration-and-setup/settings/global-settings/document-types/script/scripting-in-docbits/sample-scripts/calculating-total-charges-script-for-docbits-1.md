# Script voor het Berekenen van Totale Kosten voor Docbits

Het "Calculating Total Charges" script automatiseert het proces van het optellen van verschillende kosten en extra bedragen binnen factuurdocumenten. Deze handleiding leidt u door de scriptconfiguratie, logica en toepassing om nauwkeurige totale kostenberekeningen in uw documenten te garanderen.

### Doel

Dit script biedt een dynamische manier om de totale kosten op een factuur te berekenen door verschillende soorten kosten op te tellen, zoals basiskosten, vracht (Fracht) en verpakking (Verpackung). Het werkt vervolgens het veld voor totale kosten van de factuur bij met de berekende som, waardoor nauwkeurige factureringsinformatie wordt gegarandeerd.

### Scriptoverzicht

Het script haalt waarden op uit opgegeven velden, converteert ze naar drijvende-kommagetallen, telt ze op en werkt vervolgens het veld `total_charges` bij met het resultaat. Als het veld `total_charges` niet bestaat, maakt het script dit veld aan en stelt de waarde dienovereenkomstig in.

#### Codefragment

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Totaal initialiseren op 0
total = 0

# Vracht optellen bij totaal als het bestaat
if fracht:
    fracht = float(fracht)
    total += fracht

# Verpakking optellen bij totaal als het bestaat
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Totaal opmaken naar twee decimalen
formatted_total = "{0:.2f}".format(total)

# Controleren of het veld total_charges bestaat en dienovereenkomstig bijwerken of aanmaken
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
