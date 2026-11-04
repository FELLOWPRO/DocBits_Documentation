# Script de Cálculo de Cargas Totais para Docbits

### Introdução

Este documento fornece um guia detalhado sobre o script "Calculando Cargas Totais" dentro da plataforma Docbits. O script é projetado para calcular automaticamente o valor total cobrado em uma fatura somando várias cobranças individuais. Essa automação aprimora a precisão e eficiência no processamento de documentos.

### Objetivo

O objetivo deste script é simplificar o processo de cálculo das cargas totais em faturas. Ao adicionar automaticamente as cobranças especificadas, como cobranças base, impostos e taxas adicionais, o script garante que as cargas totais refletidas em cada fatura sejam precisas e abrangentes.

### Detalhes do Script

#### Implementação de Código
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

