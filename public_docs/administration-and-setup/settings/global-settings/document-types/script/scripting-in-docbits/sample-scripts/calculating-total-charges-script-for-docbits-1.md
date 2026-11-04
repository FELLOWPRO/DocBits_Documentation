# Script de Cálculo de Encargos Totais para DocBits

O script "Cálculo de Encargos Totais" automatiza o processo de soma de vários encargos e valores adicionais dentro de documentos de fatura. Este guia orienta-o através da configuração, lógica e aplicação do script para garantir cálculos precisos de encargos totais nos seus documentos.

### Propósito

Este script visa fornecer uma forma dinâmica de calcular os encargos totais numa fatura somando diferentes tipos de encargos, como encargos base, frete (Fracht) e embalagem (Verpackung). Em seguida, atualiza o campo de encargos totais da fatura com a soma calculada, garantindo informações de faturação precisas.

### Visão Geral do Script

O script obtém valores de campos especificados, converte-os em números de ponto flutuante, soma-os e depois atualiza o campo `total_charges` com o resultado. Se o campo `total_charges` não existir, o script cria este campo e define o seu valor de acordo.

#### Trecho de Código

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Inicializar total a 0
total = 0

# Adicionar frete ao total se existir
if fracht:
    fracht = float(fracht)
    total += fracht

# Adicionar embalagem ao total se existir
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Formatar o total com duas casas decimais
formatted_total = "{0:.2f}".format(total)

# Verificar se o campo total_charges existe e atualizar ou criar de acordo
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```
