# Validação da Soma da Tabela

## O que faz este script?

Valida que a soma de todos os totais de linha na tabela de fatura corresponde ao valor líquido do documento. Se houver uma discrepância superior a 0.01, a soma calculada substitui o valor líquido extraído — garantindo consistência entre os itens de linha e os campos de cabeçalho.

## Trigger

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Calcular soma de todos os totais de linha
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Comparar com o valor líquido extraído
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # Soma das linhas difere do cabeçalho — atualizar valor líquido
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## Variação: Marcar como inválido em vez de substituir

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        diff = abs(float(net_amount) - total)
        if diff > 0.01:
            set_field_as_invalid(document_data, "net_amount",
                f"Line total sum ({round(total, 2)}) differs from net amount ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Amounts match")
    except ValueError:
        pass
```

## Explicação Passo a Passo

1. **Obter tabela de fatura** de `tables_dict`
2. **Somar todos os valores LINE_TOTAL** nas linhas da tabela
3. **Comparar** a soma calculada com o valor líquido extraído
4. **Atualizar ou sinalizar** — substituir o valor líquido ou marcá-lo como inválido

## Funções Utilizadas

- [get\_column\_value()](../table-functions.md#get\_column\_value) — Ler valores de colunas das linhas
- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valor líquido
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — Definir valor corrigido
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Marcar campo como inválido
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — Marcar campo como válido
