# Formatação do Script de Números de Referência de Certificado de Exportação para Docbits

Este documento descreve o script "Formatação de Números de Referência de Certificado de Exportação", com o objetivo de padronizar os números de referência em certificados de exportação no Docbits. A formatação adequada garante que os números de referência estejam em conformidade com os sistemas externos ou requisitos regulatórios.

### Propósito

O objetivo principal do script é formatar os números de referência nos certificados de exportação, garantindo que atendam a um requisito de comprimento predefinido preenchendo-os com zeros à esquerda. Essa consistência ajuda a manter um formato padronizado para todos os documentos de exportação processados pelo Docbits.

### Visão Geral do Script

O script identifica o campo `reference_number` em um certificado de exportação, verifica seu comprimento e, se necessário, preenche o número com zeros à esquerda para garantir que atenda ao requisito mínimo de comprimento.

#### Trecho de Código
```python
ref_number = get_field_value(fields_dict, 'reference_number')
# Ensure the reference number meets a minimum length of 10 characters
if len(ref_number) < 10:
ref_number = ref_number.zfill(10)
set_field_value(fields_dict, 'reference_number', ref_number)
```

