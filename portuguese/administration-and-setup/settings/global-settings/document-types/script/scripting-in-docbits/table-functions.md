# Funções de Tabela

Funções para ler, escrever e manipular tabelas e linhas de tabelas.

**Fonte:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Lê o valor de uma coluna de uma linha da tabela.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `row` | `dict` | Um objeto de linha de `table["rows"]` |
| `column_name` | `str` | Nome da coluna (insensível a maiúsculas/minúsculas) |
| `default_value` | `any` | Valor de retorno se a coluna estiver vazia/ausente |
| `is_clean` | `bool` | Se `True`: MAIÚSCULAS com espaços removidos |

**Exemplo — Iterar linhas da tabela:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
A comparação do nome da coluna é **insensível a maiúsculas/minúsculas**: `"DESCRIPTION"` também corresponde a `"description"` ou `"Description"`.
{% endhint %}

---

## set\_column\_value()

Define o valor de uma coluna numa linha da tabela.

```python
set_column_value(row, column_name, value)
```

**Retorna:** `True` se o valor mudou, `False` se idêntico

**Efeitos colaterais:**
- Define `extraction_method = "SCRIPT"`
- Cria automaticamente a coluna se não existir

**Exemplo — Calcular totais de linha:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
        try:
            total = float(qty) * float(price)
            set_column_value(row, "LINE_TOTAL", str(total))
        except ValueError:
            pass
```

---

## set\_column\_date\_value()

Define um valor de data numa célula da tabela com formatação e aritmética de datas.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `document_data` | `dict` | Necessário para `date_format_pattern` |
| `row` | `dict` | Linha da tabela |
| `column_name` | `str` | Nome da coluna |
| `value` | `str` | Data ISO `"2026-03-25"` |
| `add_days` | `int` | Dias a adicionar |
| `skip_weekend` | `bool` | Saltar fins de semana |
| `exclude_final_days` | `str/list` | Dias a excluir |

**Exemplo — Calcular datas de entrega por linha:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Define um valor monetário numa célula da tabela com formatação de localidade.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Exemplo — Calcular e formatar totais de linha:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` é automaticamente convertido para `str()` antes de ser definido.
{% endhint %}

---

## add\_table\_column()

Adiciona uma nova coluna a todas as linhas de uma tabela.

```python
add_table_column(table, col_name, default_value=None)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `table` | `dict` | O objeto da tabela (não `tables_dict`!) |
| `col_name` | `str` | Nome da nova coluna |
| `default_value` | `any` | Valor inicial para todas as linhas |

**Efeitos colaterais:**
- `is_extra_column = True` (marcada como não original)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Exemplo — Adicionar coluna de código fiscal:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Agora definir valores por linha
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Proteção contra duplicados:** Se a coluna já existir (verificação insensível a maiúsculas/minúsculas), **não** será adicionada novamente.
{% endhint %}

---

## remove\_rows\_from\_table()

Remove um número específico de linhas de uma tabela.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `table_name` | `str` | Nome da tabela |
| `count` | `int` | Número de linhas a remover |
| `start` | `int` | Índice inicial (baseado em 0) |

**Lança:** `ValueError` se `start` ou `count` estiver fora do intervalo

**Exemplo — Remover linhas de cabeçalho ou última linha:**

```python
# Remover as primeiras 2 linhas (ex.: linhas de cabeçalho)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Remover a última linha
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Mantém apenas uma linha específica e remove todas as outras.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `line_number` | `int` | Número da linha (baseado em 1!) |

{% hint style="warning" %}
`line_number=1` mantém a primeira linha. Não confundir com índices baseados em 0.
{% endhint %}

**Exemplo:**

```python
# Manter apenas a 3.ª linha
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Elimina todas as tabelas do documento (com backup).

```python
delete_tables(document_data)
```

**Efeitos colaterais:**
- Guarda as tabelas em `last_deleted_table`
- Remove `po_items`, `po_multi_matched`, `po_match_status`

**Exemplo:**

```python
# Eliminar tabelas (ex.: para faturas de custo sem itens de linha)
delete_tables(document_data)
```

---

## restore\_tables()

Restaura tabelas previamente eliminadas com `delete_tables()`.

```python
restore_tables(document_data)
```

**Exemplo:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Padrão Eliminar + Restaurar:** Útil quando pretende remover tabelas temporariamente e restaurá-las sob certas condições.
{% endhint %}

---

## Padrões Comuns

### Calcular soma de coluna

```python
table = tables_dict.get("INVOICE_TABLE")
total = 0
if table:
    for row in table["rows"]:
        val = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(val)
        except ValueError:
            pass
    set_field_value(document_data, "calculated_total", str(round(total, 2)))
```

### Filtrar linhas vazias

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Remover de trás para a frente
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Calcular coluna a partir de outras colunas

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_AMOUNT", "0")
    for row in table["rows"]:
        net = float(get_column_value(row, "NET_AMOUNT", "0"))
        tax_rate = float(get_column_value(row, "TAX_RATE", "0"))
        tax = net * tax_rate / 100
        set_column_amount_value(document_data, row, "TAX_AMOUNT", tax)
```
