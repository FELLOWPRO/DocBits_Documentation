# Cálculo da Data de Vencimento

## O que faz este script?

Calcula a data de vencimento do pagamento com base na data da fatura adicionando um número configurável de dias (ex.: 30). Os fins de semana são automaticamente saltados para que a data de vencimento caia sempre num dia útil.

## Trigger

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
# Ler data da fatura
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Calcular data de vencimento: 30 dias após a data da fatura, saltar fins de semana
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Também definir data contabilística = data da fatura
    set_date_value(document_data, "accounting_date", inv_date)
```

## Variações

### 14 dias, excluindo segundas-feiras

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 dias, sem salto de fins de semana

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### Definir data de entrega para hoje

```python
set_date_value(document_data, "delivery_date", None)  # None = hoje
```

## Explicação Passo a Passo

1. **Ler data da fatura** do documento
2. **Calcular data de vencimento** usando `set_date_value()` com `add_days=30` e `skip_weekend=True`
3. **Formatação da data** é automática — usa o `date_format_pattern` do documento (ex.: `%d.%m.%Y`)
4. **Salto de fins de semana** garante que a data de vencimento cai de segunda a sexta

## Códigos de Dias para `exclude_final_days`

`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler data da fatura
- [set\_date\_value()](../field-functions.md#set\_date\_value) — Calcular e definir data de vencimento
