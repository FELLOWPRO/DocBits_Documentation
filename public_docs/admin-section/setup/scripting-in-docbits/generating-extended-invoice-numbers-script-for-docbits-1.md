# Generowanie Rozszerzonych Numerów Faktur Skrypt dla Docbits

Ten dokument szczegółowo opisuje skrypt "Generowanie Rozszerzonych Numerów Faktur", który automatyzuje tworzenie rozszerzonych numerów faktur w Docbits. Rozszerzone numery faktur łączą wiele identyfikatorów dokumentów, takich jak ID faktury i numer zamówienia, w jeden kompleksowy identyfikator. Ten skrypt zwiększa śledzenie dokumentów i upraszcza prowadzenie rejestrów.

### Cel

Celem tego skryptu jest usprawnienie procesu generowania rozszerzonych numerów faktur poprzez automatyczne łączenie ID faktury i numeru zamówienia, co zapewnia zjednoczony i unikalny identyfikator dla każdego dokumentu faktury.

### Przegląd Skryptu

Skrypt sprawdza obecność pól ID faktury i numeru zamówienia w dokumencie, łączy ich wartości, jeśli oba są obecne (oddzielone myślnikiem) oraz aktualizuje lub tworzy nowe pole, aby przechowywać połączoną wartość.

#### Fragment Kodu
```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
# Updating the 'invoice_extended_number' field with the combined value
if not 'invoice_extended_number' in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

