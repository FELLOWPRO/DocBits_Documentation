# Funções de Lógica de Negócio

Funções para lookups, correspondência de OC, tarefas, gestão de utilizadores/grupos e alterações de estado.

**Fonte:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Consulta dados mestre de tabelas de lookup (fornecedores, itens, contas contabilísticas, etc.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID da organização |
| `sub_org_id` | `str/None` | UUID da sub-organização (ou `None`) |
| `lookup_name` | `str` | Nome do lookup (ex.: `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Condições de filtro (ver formatos abaixo) |
| `skip` | `int` | Offset para paginação (padrão: 0) |
| `limit` | `int` | Máximo de resultados (padrão: 100) |
| `match_all` | `bool` | `True` = AND, `False` = OR (padrão: `True`) |
| `sort_order` | `list` | Ordenação (opcional) |

### Formatos de Filtro

Três formatos são suportados:

```python
# Formato 1: Dict com campo/operador/valor
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Formato 2: Tuplo/Lista com 2 elementos (campo, valor) → operador = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Formato 3: Tuplo/Lista com 3 elementos (campo, operador, valor)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Ordenação

```python
# Formato 1: Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Formato 2: Tuplo/Lista
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Exemplo — Lookup de fornecedor por ID de vendedor:**

```python
# Encontrar fornecedor por ID de vendedor
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Exemplo — Pesquisar contas contabilísticas com múltiplos filtros:**

```python
records = get_lookup_records(
    org_id, document_json.get("sub_org_id"), "gl_account",
    [
        {"field": "ACCOUNT_TYPE", "operator": "exact", "value": "EXPENSE"},
        {"field": "IS_ACTIVE", "operator": "exact", "value": "true"},
    ],
    limit=50,
    sort_order=[["ACCOUNT_NUMBER", "asc"]],
)
```

{% hint style="info" %}
Internamente utiliza `search_operator="SMART"` que suporta correspondência difusa.
{% endhint %}

---

## is\_supplier\_valid()

Verifica se um fornecedor existe nos dados de lookup.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | O objeto de contexto `user` |
| `filter_data_json` | `dict` | Filtro no formato `{"match_all": True, "filters": [...]}` |
| `sub_org_id` | `str/None` | Sub-organização |

**Retorna:** `True` se houver pelo menos 1 correspondência, caso contrário `False`

**Exemplo — Validar fornecedor:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Supplier not found in master data")
```

---

## auto\_po\_match\_for\_purchase\_orders()

Aciona a correspondência automática de OC via o microserviço po-match-service.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Deve ser um objeto de utilizador real |
| `document_data` | `dict` | Contexto do documento |
| `po_numbers` | `str/list` | Números de OC (separados por vírgula ou lista) |

**Retorna:** `document_data` atualizado com `po_items`, `po_match_status`, `po_multi_matched`

**Exemplo — Correspondência automática de OC:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Proteção contra duplicados:** Números de OC já verificados são armazenados em `already_verified_po_numbers` e não serão correspondidos novamente.
{% endhint %}

---

## get\_next\_sequence\_number()

Obtém e incrementa atomicamente um número de sequência na base de dados.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID da organização |
| `sequence_name` | `str` | Deve conter `"sequence"` (ex.: `"invoice_sequence"`) |
| `default_value` | `int` | Valor inicial quando a sequência é criada pela primeira vez |

**Retorna:** `int` — o próximo número, ou `None` se o nome for inválido

**Exemplo — Gerar número interno do documento:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Regra de nomenclatura:** O `sequence_name` deve começar ou terminar com "sequence", ou conter "SEQUENCE\_". Caso contrário, a função retorna `None`.
{% endhint %}

---

## create\_document\_task()

Cria uma tarefa para o documento atual.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Contexto do utilizador |
| `title` | `str` | Título da tarefa |
| `description` | `str` | Descrição |
| `priority` | `str/int` | Prioridade |
| `assigned_to_user_id` | `str/None` | Utilizador atribuído |
| `assigned_to_group_id` | `str/None` | Grupo atribuído |
| `send_email` | `bool` | Enviar notificação por email |

**Exemplo — Criar tarefa para faturas de valor elevado:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="High invoice amount - review required",
        description=f"Invoice amount: {amount} exceeds 50,000 threshold",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Atribui uma sub-organização a um documento.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Efeitos colaterais:**
- Define `sub_org_id` em `document_json`
- Guarda diretamente na base de dados (se `doc_id` estiver presente)

**Exemplo — Encaminhar com base no fornecedor:**

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
sub_org_map = {
    "ACMECORP": "uuid-acme-sub-org",
    "WIDGETSINC": "uuid-widgets-sub-org",
}
for key, sub_org in sub_org_map.items():
    if key in supplier:
        set_document_sub_org_id(document_data, sub_org)
        break
```

---

## update\_document\_status\_with\_doc\_id()

Altera o estado de um documento.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `doc_id` | `str` | UUID do documento |
| `status` | `str` | Novo estado (ex.: `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Mensagem de estado |
| `doc_classification_class` | `str/None` | Para estado `CLASSIFIED`: novo tipo de documento |

**Exemplo — Definir documento para estado de erro:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Required field missing: supplier number"
)
```

{% hint style="warning" %}
**Atenção:** Alterações de estado acionam ações a jusante (workflows do DocFlow, hooks de alteração de estado). Use apenas quando necessário.
{% endhint %}

---

## get\_document\_content()

Retorna o texto OCR completo do documento.

```python
get_document_content(document_data)
```

**Retorna:** `str` — Texto concatenado de todas as páginas

**Exemplo — Pesquisar texto completo por palavras-chave:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Pesquisa regex no texto completo
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
O resultado é cacheado durante 60 segundos (cache TTL com máximo de 128 entradas).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Pesquisa um utilizador por ID ou email.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Retorna:** Objeto `UsersCache` com atributos como `.email`, `.first_name`, `.last_name`, `.user_id`

**Exemplo — Atribuir tarefa a um utilizador específico:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="Review required",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Pesquisa um grupo de utilizadores por ID ou nome.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Retorna:** Objeto `GroupCache`

**Exemplo — Encontrar grupo para atribuição de tarefa:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Approval needed",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Comparação inteligente de valores com conversão de tipo.

```python
compare_values(value1, value2)
```

**Lógica de comparação:**
1. `None == None` → `True`
2. `None != non-None` → `False`
3. Strings que são números → comparação numérica (`"1.0" == "1.00"` → `True`)
4. Strings → insensível a maiúsculas/minúsculas e espaços (`"ABC " == " abc"` → `True`)
5. Bool vs String → comparação de strings (`True == "true"` → `True`)
6. Comparação Decimal como fallback

**Exemplo — Verificar se os valores coincidem:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Amounts match")
```

---

## get\_lov\_values()

Obtém entradas de Lista de Valores (LOV).

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parâmetros:**

| Nome | Tipo | Descrição |
| ---- | ---- | ----------- |
| `org_id` | `str` | UUID da organização |
| `key` | `str` | Chave LOV |
| `return_type` | `str` | `"list_of_objects"` ou `"list_of_values"` |
| `sub_org_id` | `str/None` | Filtro opcional de sub-organização |
| `language_code` | `str` | Código de idioma (ex.: `"en"`, `"de"`) |

**Retorna:** Valores LOV como lista de objetos ou como lista simples.

**Exemplo — Obter códigos fiscais configurados:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```
