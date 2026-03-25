# Skripta za obracun ukupnih troskova u DocBits-u

Skripta "Obracun ukupnih troskova" automatizuje proces sabiranja razlicitih troskova i dodatnih iznosa u dokumentima faktura. Ovaj vodic vas vodi kroz podesavanje skripte, logiku i primenu kako bi se obezbedili tacni obracuni ukupnih troskova u vasim dokumentima.

### Svrha

Ova skripta ima za cilj da pruzi dinamican nacin za izracunavanje ukupnih troskova na fakturi sabiranjem razlicitih tipova troskova, kao sto su osnovni troskovi, prevoz (Fracht) i pakovanje (Verpackung). Zatim azurira polje ukupnih troskova fakture sa izracunatim zbirom, cime se osiguravaju tacne informacije o naplati.

### Pregled skripte

Skripta preuzima vrednosti iz navedenih polja, konvertuje ih u decimalne brojeve, sabira ih, a zatim azurira polje `total_charges` sa rezultatom. Ako polje `total_charges` ne postoji, skripta kreira ovo polje i postavlja njegovu vrednost u skladu s tim.

#### Isecak koda

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Inicijalizacija ukupnog iznosa na 0
total = 0

# Dodavanje prevoza ukupnom iznosu ako postoji
if fracht:
    fracht = float(fracht)
    total += fracht

# Dodavanje pakovanja ukupnom iznosu ako postoji
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Formatiranje ukupnog iznosa na dva decimalna mesta
formatted_total = "{0:.2f}".format(total)

# Provera da li polje total_charges postoji i azuriranje ili kreiranje u skladu s tim
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
