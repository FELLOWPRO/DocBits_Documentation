# Funções de Campo

Funções para ler, escrever e controlar campos de documentos.

**Fonte:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Lê o valor de um campo do documento.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `document_data` | `dict` | O objeto de contexto `document_data` |
| `field_name` | `str` | Nome do campo (ex.: `"invoice_id"`) |
| `default_value` | `any` | Valor de retorno se o campo estiver vazio/ausente (padrão: `None`) |
| `is_clean` | `bool` | Se `True`: o valor é convertido para MAIÚSCULAS com espaços removidos |

**Retorna:** O valor do campo como string, ou `default_value`

**Exemplo — Ler número da fatura com fallback:**

```python
# Ler campo com valor padrão
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# Com is_clean=True: "INV 001" torna-se "INV001"
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**O que acontece:** Retorna o valor do campo. Quando `is_clean=True`, o valor é transformado via `value.upper().replace(" ", "").strip()` — útil para comparações.

---

## set\_field\_value()

Define o valor de um campo. Cria automaticamente o campo se não existir.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `document_data` | `dict` | O objeto de contexto `document_data` |
| `field_name` | `str` | Nome do campo |
| `value` | `any` | Novo valor |
| `remove_link` | `bool` | Se `True`: remove coordenadas, confiança, regra, etc. |

**Retorna:** `True` se o valor mudou, `False` se idêntico

**Efeitos colaterais:**
- Define `highlight_field = True` (indicador visual na UI)
- Define `extraction_method = "SCRIPT"`
- Define `formatted_value = value`

**Exemplo — Atribuição condicional de valor:**

```python
# Definir ID da fatura
set_field_value(document_data, "invoice_id", "INV-2026-001")

# Com remove_link: remove ligação OCR (coordenadas, confiança, etc.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**O que acontece:** O valor do campo é atualizado e marcado como modificado por script. Se o campo não existir, é automaticamente criado com `extraction_method: "SCRIPT"` e adicionado tanto a `fields` como a `fields_dict`.

---

## set\_date\_value()

Define um valor de data com formatação automática e aritmética de datas opcional.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `value` | `str` | Data ISO: `"2026-03-25"`. Se vazio: data de hoje |
| `add_days` | `int` | Dias a adicionar (ex.: `30` para condições de pagamento) |
| `skip_weekend` | `bool` | Saltar fins de semana ao adicionar dias |
| `exclude_final_days` | `str/list` | Dias adicionais a excluir (ex.: `"MONDAY,FRIDAY"`) |

**Exemplo — Calcular data de vencimento do pagamento (30 dias, sem fins de semana):**

```python
# Data de vencimento: 30 dias após a data da fatura, saltar fins de semana
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Definir data de entrega para hoje
set_date_value(document_data, "delivery_date", None)  # None = hoje

# 14 dias, excluindo sábado e segunda-feira
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**O que acontece:** A data é calculada adicionando dias (opcionalmente saltando fins de semana/dias específicos) e automaticamente formatada de acordo com o `date_format_pattern` do documento (ex.: `%d.%m.%Y` para Alemanha).

**Códigos de dias para `exclude_final_days`:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Define um valor monetário com formatação automática de localidade.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `value` | `str/number` | Valor em formato inglês (ex.: `"1234.56"`) |

**Exemplo — Definir valor líquido:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value torna-se, por ex., "1.234,56" para localidade de_DE
```

**O que acontece:** O valor é formatado de acordo com `amount_format_locale` de `document_json` (ex.: `de_DE`, `en_US`).

---

## create\_new\_field()

Cria um novo dicionário de campo (sem adicioná-lo ao documento).

```python
create_new_field(field_name, value="")
```

**Retorna:** Dict com `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"`

**Exemplo:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Alternativa mais simples:** Use `set_field_value()` em vez disso — cria automaticamente o campo se não existir. `create_new_field()` só é necessário quando pretende manipular manualmente o dict do campo.
{% endhint %}

---

## delete\_field()

Remove um campo do documento.

```python
delete_field(document_data, field_name)
```

**Retorna:** Tuplo `(doc_json, fields_dict)` após a eliminação

**Exemplo:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Marca um campo como inválido com uma mensagem de erro.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `message` | `str` | Mensagem de erro (exibida na UI) |
| `code` | `str` | Código de erro (padrão: `INVALID_VALUE`) |

**Efeitos colaterais:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Exemplo — Validação de IBAN:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN must be at least 15 characters",
                         "IBAN_TOO_SHORT")
```

**O que acontece:** O campo é destacado a vermelho no ecrã de validação com a mensagem de erro exibida ao utilizador.

---

## set\_field\_as\_valid()

Remove o estado inválido de um campo.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Exemplo:**

```python
set_field_as_valid(document_data, "iban", "IBAN valid")
```

**O que acontece:** Remove `invalidated_by_script`, `validation_message`, `validation_code` e define `is_valid = True`.

---

## set\_field\_attribute()

Define um atributo arbitrário num campo.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Exemplo:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Consulte a lista completa de [Atributos Suportados](#supported-attributes) abaixo.

---

## set\_is\_required()

Torna um campo obrigatório ou remove a exigência.

```python
set_is_required(document_data, field_name, value)
```

**Exemplo — Número de OC obrigatório para faturas de compra:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Torna um campo somente leitura ou editável.

```python
set_is_readonly(document_data, field_name, value)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = somente leitura, `False` = editável, `None` = remover atributo |

**Exemplo:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

Oculta ou mostra um campo na UI.

```python
set_is_hidden(document_data, field_name, value)
```

**Exemplo — Mostrar campos de sub-organização apenas quando relevante:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Força a validação manual de um campo.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = forçar validação, `False` = remover |
| `reset_validation` | `bool` | Se `True`: redefine `is_validated` para `False` |

**Efeitos colaterais quando `value=True`:**
- `force_validation = True`
- `is_valid = False` (se ainda não validado)
- `validation_code = "FORCED_VALIDATION"`

**Exemplo — Forçar validação para valores elevados:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Atributos Suportados

### Atributos Principais do Campo

| Atributo | Tipo | Descrição |
| --------- | ---- | ----------- |
| `value` | any | O valor bruto do campo |
| `formatted_value` | string | Valor formatado para exibição |
| `content` | string | Conteúdo original extraído |
| `is_required` | bool | Se o campo é obrigatório |
| `is_valid` | bool | Estado de validação |
| `is_validated` | bool | Se o campo foi validado pelo utilizador |
| `is_readonly` | bool | Se o campo é somente leitura |
| `is_hidden` | bool | Se o campo está oculto na UI |
| `force_validation` | bool | Forçar o utilizador a validar este campo |
| `highlight_field` | bool | Destacar campo na UI |
| `extraction_method` | string | Como o valor foi extraído (ex.: `"SCRIPT"`) |

### Atributos de Validação

| Atributo | Tipo | Descrição |
| --------- | ---- | ----------- |
| `validation_message` | string | Mensagem de erro mostrada ao utilizador |
| `validation_code` | string | Código de erro (ex.: `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Marca o campo como invalidado por script |

### Atributos de Extração/OCR

| Atributo | Tipo | Descrição |
| --------- | ---- | ----------- |
| `coords` | object | Coordenadas da caixa delimitadora no documento |
| `confidence` | float | Pontuação de confiança do OCR/extração |
| `score` | float | Pontuação de correspondência/validação |
| `score_description` | string | Descrição da pontuação |
| `page` | int | Número da página onde o campo foi encontrado |
| `rule` | string | Regra de extração que foi aplicada |
