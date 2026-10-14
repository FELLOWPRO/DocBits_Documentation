# Skrypt Generowania Rozszerzonych Numerów Faktur dla DocBits

Ten dokument opisuje szczegółowo skrypt „Generating Extended Invoice Numbers", który automatyzuje tworzenie rozszerzonych numerów faktur w DocBits. Rozszerzone numery faktur łączą wiele identyfikatorów dokumentu, takich jak ID faktury i numer zamówienia zakupu, w jeden kompleksowy identyfikator. Ten skrypt zwiększa identyfikowalność dokumentów i upraszcza prowadzenie ewidencji.

### Cel

Celem tego skryptu jest optymalizacja procesu generowania rozszerzonych numerów faktur poprzez automatyczne łączenie ID faktury i numeru zamówienia zakupu, zapewniając tym samym ujednolicony i unikalny identyfikator dla każdego dokumentu faktury.

### Przegląd Skryptu

Skrypt sprawdza obecność pól ID faktury i numeru zamówienia zakupu w dokumencie, łączy ich wartości, jeśli oba są obecne (rozdzielone myślnikiem), oraz aktualizuje lub tworzy nowe pole do przechowywania połączonej wartości.

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
