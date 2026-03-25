# Skripta za generisanje prosirenih brojeva faktura u DocBits-u

Ovaj dokument detaljno opisuje skriptu "Generisanje prosirenih brojeva faktura", koja automatizuje kreiranje prosirenih brojeva faktura u DocBits-u. Prosireni brojevi faktura kombinuju vise identifikatora dokumenta, kao sto su ID fakture i broj narudzbenice, u jedan sveobuhvatan identifikator. Ova skripta poboljsava sledljivost dokumenata i pojednostavljuje vodjenje evidencije.

### Svrha

Svrha ove skripte je da pojednostavi proces generisanja prosirenih brojeva faktura automatskim spajanjem ID-a fakture i broja narudzbenice, cime se obezbeduje jedinstven i sveobuhvatan identifikator za svaki dokument fakture.

### Pregled skripte

Skripta proverava prisustvo polja ID fakture i broja narudzbenice u dokumentu, spaja njihove vrednosti ako su oba prisutna (razdvojeni crticom) i azurira ili kreira novo polje za cuvanje kombinovane vrednosti.

#### Isecak koda

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Kombinovanje ID-a fakture i broja narudzbenice sa crticom kao separatorom
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Provera da li postoji prosireni broj za postavljanje
if extended_number:
    # Azuriranje polja 'invoice_extended_number' sa kombinovanom vrednoscu
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

