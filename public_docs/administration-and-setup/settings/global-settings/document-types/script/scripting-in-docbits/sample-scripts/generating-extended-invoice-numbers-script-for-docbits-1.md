# Script voor het Genereren van Uitgebreide Factuurnummers voor Docbits

Dit document beschrijft in detail het "Generating Extended Invoice Numbers" script, dat de creatie van uitgebreide factuurnummers in Docbits automatiseert. Uitgebreide factuurnummers combineren meerdere documentidentificatoren, zoals het factuur-ID en het inkoopordernummer, tot één uitgebreide identificator. Dit script verbetert de traceerbaarheid van documenten en vereenvoudigt het bijhouden van gegevens.

### Doel

Het doel van dit script is om het proces van het genereren van uitgebreide factuurnummers te stroomlijnen door automatisch het factuur-ID en inkoopordernummer samen te voegen, waardoor een uniforme en unieke identificator voor elk factuurdocument wordt geboden.

### Scriptoverzicht

Het script controleert de aanwezigheid van de velden factuur-ID en inkoopordernummer binnen het document, voegt hun waarden samen als beide aanwezig zijn (gescheiden door een koppelteken), en werkt een bestaand veld bij of maakt een nieuw veld aan om de gecombineerde waarde op te slaan.

#### Codefragment

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Factuurnummer en inkoopordernummer combineren met een koppelteken als scheidingsteken
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Controleren of er een uitgebreid nummer is om in te stellen
if extended_number:
    # Het veld 'invoice_extended_number' bijwerken met de gecombineerde waarde
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```


