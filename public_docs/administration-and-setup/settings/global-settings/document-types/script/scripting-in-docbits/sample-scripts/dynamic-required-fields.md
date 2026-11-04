# Campos Obrigatórios Dinâmicos

## O que faz este script?

Define dinamicamente os requisitos de campos com base no conteúdo do documento. Neste exemplo: quando a moeda da fatura não é EUR, o campo de taxa de câmbio torna-se obrigatório e visível. Para faturas em EUR, o campo de taxa de câmbio é oculto e opcional.

## Trigger

`ON_FIELD_CHANGE` no tipo de documento **INVOICE**

## Script Completo

```python
# Ler moeda atual
currency = get_field_value(document_data, "currency", "EUR")

# Moeda estrangeira: taxa de câmbio é obrigatória e visível
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: taxa de câmbio é opcional e oculta
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Variação: Fatura de compra vs. fatura de custo

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Fatura de compra: número da OC é obrigatório
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Fatura de custo: número da OC não necessário, ocultar tabela
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Explicação Passo a Passo

1. **Ler o campo de controlo** (moeda neste caso)
2. **Aplicar regras de negócio** — diferentes requisitos de campos com base no valor
3. **Definir visibilidade** — ocultar campos irrelevantes para manter a UI limpa
4. **Definir requisitos** — tornar campos relevantes obrigatórios

{% hint style="info" %}
**Escolha do trigger:** `ON_FIELD_CHANGE` executa cada vez que um utilizador modifica um campo, para que os requisitos sejam atualizados em tempo real. `AFTER_FORMATTING` executa apenas uma vez após a extração inicial.
{% endhint %}

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler campo de controlo
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Definir campo como obrigatório/opcional
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Mostrar/ocultar campos
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Definir campo de categoria
- [delete\_tables()](../table-functions.md#delete\_tables) — Remover tabelas para faturas de custo
