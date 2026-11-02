# Script voor het Formatteren van Exportcertificaat Referentienummers voor Docbits

Dit document beschrijft het "Formatting Export Certificate Reference Numbers" script, gericht op het standaardiseren van referentienummers op exportcertificaten in Docbits. Correcte opmaak zorgt ervoor dat referentienummers voldoen aan de vereisten van externe systemen of regelgeving.

### Doel

Het primaire doel van het script is om referentienummers op exportcertificaten te formatteren, zodat ze voldoen aan een vooraf gedefinieerde lengtevereiste door ze aan te vullen met voorloopnullen. Deze consistentie helpt bij het handhaven van een gestandaardiseerd formaat voor alle exportdocumenten die via Docbits worden verwerkt.

### Scriptoverzicht

Het script identificeert het veld `reference_number` in een exportcertificaat, controleert de lengte ervan en vult het nummer indien nodig aan met voorloopnullen om ervoor te zorgen dat het aan de minimale lengtevereiste voldoet.

#### Codefragment

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Controleren of het referentienummer minimaal 10 tekens lang is
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```


