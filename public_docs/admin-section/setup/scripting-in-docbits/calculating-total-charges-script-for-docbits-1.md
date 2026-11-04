# Skrypt Obliczający Całkowite Opłaty dla DocBits

##

Skrypt "Obliczanie Całkowitych Opłat" automatyzuje proces sumowania różnych opłat i dodatkowych kwot w dokumentach faktur. Ten przewodnik prowadzi Cię przez konfigurację skryptu, logikę i zastosowanie, aby zapewnić dokładne obliczenia całkowitych opłat w Twoich dokumentach.

### Cel

Ten skrypt ma na celu zapewnienie dynamicznego sposobu obliczania całkowitych opłat na fakturze poprzez dodawanie różnych typów opłat, takich jak opłaty podstawowe, fracht i opakowanie. Następnie aktualizuje pole całkowite opłaty faktury o obliczoną sumę, zapewniając dokładne informacje rozliczeniowe.

### Przegląd Skryptu

Skrypt pobiera wartości z określonych pól, konwertuje je na liczby zmiennoprzecinkowe, sumuje je, a następnie aktualizuje pole `total_charges` wynikiem. Jeśli pole `total_charges` nie istnieje, skrypt tworzy to pole i ustawia jego wartość odpowiednio.

#### Fragment Kodu
```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
fracht = float(fracht)
total += fracht

# Add verpackung to total if it exists
if verpackung:
verpackung = float(verpackung)
total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
new_field = create_new_field('total_charges', formatted_total)
fields_dict['total_charges'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'total_charges', formatted_total)
```

