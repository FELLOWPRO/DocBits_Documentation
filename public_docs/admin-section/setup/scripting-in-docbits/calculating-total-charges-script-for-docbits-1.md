# Script de Cálculo de Cargas Totais para Docbits

##

O script "Calculando Cargas Totais" automatiza o processo de somar várias cobranças e valores adicionais em documentos de fatura. Este guia orienta você na configuração do script, lógica e aplicação para garantir cálculos precisos de carga total em seus documentos.

### Propósito

Este script tem como objetivo fornecer uma maneira dinâmica de calcular as cargas totais em uma fatura, somando diferentes tipos de cobranças, como cobranças base, frete (Fracht) e embalagem (Verpackung). Em seguida, atualiza o campo de cargas totais da fatura com a soma calculada, garantindo informações precisas de faturamento.

### Visão Geral do Script

O script recupera valores de campos especificados, converte-os em floats, os soma e, em seguida, atualiza o campo `total_charges` com o resultado. Se o campo `total_charges` não existir, o script cria este campo e define seu valor adequadamente.

#### Trecho de Código
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

