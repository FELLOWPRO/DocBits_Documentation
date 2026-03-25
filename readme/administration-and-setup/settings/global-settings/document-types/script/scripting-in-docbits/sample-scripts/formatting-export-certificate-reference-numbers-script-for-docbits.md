# Script de Formatação de Números de Referência de Certificado de Exportação para DocBits

Este documento descreve o script "Formatação de Números de Referência de Certificado de Exportação", destinado a padronizar números de referência em certificados de exportação no DocBits. A formatação adequada garante que os números de referência estejam em conformidade com os requisitos de sistemas externos ou regulamentações.

### Propósito

O objetivo principal do script é formatar números de referência em certificados de exportação, garantindo que cumpram um requisito de comprimento predefinido preenchendo-os com zeros à esquerda. Esta consistência ajuda a manter um formato padronizado para todos os documentos de exportação processados através do DocBits.

### Visão Geral do Script

O script identifica o campo `reference_number` num certificado de exportação, verifica o seu comprimento e, se necessário, preenche o número com zeros à esquerda para garantir que cumpre o requisito de comprimento mínimo.

#### Trecho de Código

```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Garantir que o número de referência cumpre um comprimento mínimo de 10 caracteres
if len(ref_number) < 10:
    ref_number = ref_number.zfill(10)
    set_field_value(fields_dict, 'reference_number', ref_number)
```


