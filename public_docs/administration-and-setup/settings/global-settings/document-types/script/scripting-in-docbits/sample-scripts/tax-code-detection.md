# Detecção de Código Fiscal

## O que faz este script?

Determina automaticamente o código fiscal correto com base no conteúdo de texto completo do documento e nos valores de imposto/líquido. Deteta cenários de reverse charge, faturas isentas de imposto e calcula a taxa de imposto para atribuir o código apropriado (ex.: S1 para 19%, S2 para 7%).

## Trigger

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
# Obter texto completo do documento e valores
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Regra 1: Deteção de reverse charge via texto completo
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Regra 2: Imposto zero = isento de imposto
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Regra 3: Calcular taxa de imposto a partir dos valores
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Taxa normal
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Taxa reduzida
    else:
        set_field_value(document_data, "tax_code", "S3")    # Outra taxa
```

## Explicação Passo a Passo

1. **Ler texto completo** com `get_document_content()` para deteção de palavras-chave
2. **Ler valores de imposto e líquido** para cálculo da taxa de imposto
3. **Verificar palavras-chave de reverse charge** no texto do documento (alemão e inglês)
4. **Verificar imposto zero** — se o valor do imposto for 0, atribuir código isento de imposto
5. **Calcular taxa de imposto** a partir da razão imposto/líquido e atribuir o código correspondente

## Funções Utilizadas

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — Ler texto completo OCR
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valores dos campos
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Definir código fiscal
