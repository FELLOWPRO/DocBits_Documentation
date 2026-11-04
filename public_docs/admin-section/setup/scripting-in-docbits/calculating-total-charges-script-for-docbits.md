# Skrypt Obliczający Całkowite Opłaty dla DocBits

### Wprowadzenie

Ten dokument zawiera szczegółowy przewodnik dotyczący skryptu "Obliczanie Całkowitych Opłat" w platformie DocBits. Skrypt ten został zaprojektowany do automatycznego obliczania całkowitej kwoty na fakturze poprzez zsumowanie różnych opłat indywidualnych. Ta automatyzacja zwiększa dokładność i efektywność przetwarzania dokumentów.

### Cel

Celem tego skryptu jest usprawnienie procesu obliczania całkowitych opłat na fakturach. Poprzez automatyczne dodawanie określonych opłat, takich jak opłaty podstawowe, podatki i dodatkowe opłaty, skrypt zapewnia, że całkowite opłaty odzwierciedlone na każdej fakturze są dokładne i kompleksowe.

### Szczegóły Skryptu

#### Implementacja Kodu
```python
# Initialize variables to store the values of individual charges
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Calculate the total by converting each charge to a float and summing them up
total = 0
if fracht:
total += float(fracht)
if verpackung:
total += float(verpackung)

# Format the total to two decimal places and update the 'total_charges' field
formatted_total = "{0:.2f}".format(total)
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

