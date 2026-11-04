# Gerando Script de Números de Fatura Estendidos para Docbits

### Visão Geral

Este guia foca na automatização da criação de números de fatura estendidos no Docbits, uma funcionalidade crucial para melhorar a gestão e rastreamento de faturas. O script "Gerando Números de Fatura Estendidos" concatena vários identificadores de documentos, como ID da fatura e número do pedido de compra, para criar um identificador abrangente e único para cada fatura.

### Objetivo

O principal objetivo deste script é automatizar a geração de números de fatura estendidos, facilitando o rastreamento e gestão de faturas ao combinar múltiplos identificadores em um único número único.

### Implementação do Script

#### Trecho de Código
```python
# Retrieve the values of invoice ID and purchase order number from the document
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Concatenate the invoice ID and purchase order number with a hyphen if both exist
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check and update the 'invoice_extended_number' field with the concatenated value
if extended_number:
if 'invoice_extended_number' not in fields_dict:
new_field = create_new_field('invoice_extended_number', extended_number)
fields_dict['invoice_extended_number'] = new_field
document_json['fields'].append(new_field)
else:
set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

