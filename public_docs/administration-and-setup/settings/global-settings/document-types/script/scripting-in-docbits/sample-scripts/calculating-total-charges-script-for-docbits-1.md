# Skrypt Obliczania Całkowitych Opłat dla DocBits

### Przegląd

Ten dokument opisuje szczegółowo skrypt „Calculating Total Charges", automatyzację zaprojektowaną do obliczania łącznych opłat na fakturach w DocBits. Skrypt identyfikuje pola zawierające termin „charge" i agreguje ich wartości, upraszczając procesy finansowe.

### Cel

Głównym celem tego skryptu jest zwiększenie dokładności i efektywności przetwarzania faktur poprzez automatyczne sumowanie wszystkich pól związanych z opłatami w jeden całkowity wynik. Jest to niezbędne dla firm wymagających precyzyjnych obliczeń finansowych.

### Przegląd Skryptu

Skrypt iteruje przez wszystkie pola dokumentu faktury, filtruje pola zawierające „charge" w nazwie i sumuje ich wartości.

#### Fragment Kodu

```python
# Initialize total charges to zero
total_charges = 0

# Iterate through all fields in the document
for field_name, field_data in fields_dict.items():
    # Check if 'charge' is in the field name (case insensitive)
    if 'charge' in field_name.lower():
        # Get the field value and add to total
        charge_value = get_field_value(fields_dict, field_name, 0)
        if charge_value:
            total_charges += float(charge_value)

# Update or create the total_charges field
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', total_charges)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', total_charges)
```
