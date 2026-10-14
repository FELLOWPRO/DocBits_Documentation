# Script de Geração de Números de Fatura Estendidos para DocBits

Este documento detalha o script "Geração de Números de Fatura Estendidos", que automatiza a criação de números de fatura estendidos no DocBits. Números de fatura estendidos combinam múltiplos identificadores de documentos, como o ID da fatura e o número da ordem de compra, num único identificador abrangente. Este script melhora a rastreabilidade de documentos e simplifica a manutenção de registos.

### Propósito

O propósito deste script é otimizar o processo de geração de números de fatura estendidos concatenando automaticamente o ID da fatura e o número da ordem de compra, proporcionando assim um identificador unificado e único para cada documento de fatura.

### Visão Geral do Script

O script verifica a presença dos campos ID da fatura e número da ordem de compra dentro do documento, concatena os seus valores se ambos estiverem presentes (separados por um hífen), e atualiza ou cria um novo campo para armazenar o valor combinado.

#### Trecho de Código

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combinar ID da fatura e número da ordem de compra com separador hífen
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Verificar se existe um número estendido para definir
if extended_number:
    # Atualizar o campo 'invoice_extended_number' com o valor combinado
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```


