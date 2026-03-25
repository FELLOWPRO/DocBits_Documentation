# Funções de Pesquisa Fulltext e Vetorial

{% hint style="info" %}
**Disponível a partir da versão 11.48.0**

Estas funções requerem que a licença/preferência **OPENSEARCH\_ENABLED** esteja ativada para a sua organização. Sem ela, todas as funções lançam um `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Funções para pesquisar arquivos de documentos, encontrar documentos semelhantes e consultar dados mestre do ERP. Estas pesquisam em **todos os documentos** da organização — ao contrário de `get_document_content()` que apenas lê o texto do documento atual.

{% hint style="success" %}
**Security:** The `org_id` is automatically injected by the script sandbox. You never need to pass it — your scripts always operate within your own organization's data.
{% endhint %}

**Fonte:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Pesquisa o texto OCR completo de **todos os documentos** da organização. Encontra texto nos campos `pages.pageText`, `tfidfCustomPageText` e `ai_text` através do microsserviço fulltextsearch.

```python
fulltext_search(query, **kwargs)
```

**Parâmetros:**

| Nome | Tipo | Padrão | Descrição |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obrigatório | Termo de pesquisa (pesquisado no texto OCR de todos os documentos) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (frase exata), `"fuzzy"` (tolerante a erros, até 2 caracteres de diferença), `"prefix"` (começa com) |
| `doc_type` | `str` | `None` | Filtrar por tipo de documento (separado por vírgula, ex: `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filtrar por estado do documento (separado por vírgula, ex: `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filtrar por nome do fornecedor |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Máximo de resultados (limitado a 50) |

**Retorna:** `list[dict]` — Cada dict contém:

| Campo | Descrição |
| ----- | ----------- |
| `doc_id` | UUID do documento |
| `name` | Nome do ficheiro (ex: `"INV-2026-001.pdf"`) |
| `doc_type` | Tipo de documento (`"INVOICE"`, `"ORDER_CONFIRMATION"`, etc.) |
| `vendor_name` | Nome do fornecedor |
| `status` | Estado do documento |
| `total_amount` | Valor total |
| `ocr_content` | Excerto de texto correspondente do documento |
| `highlights` | Dict com correspondências destacadas por campo |

**Exemplo — Pesquisar frase exata:**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Exemplo — Pesquisa fuzzy (tolerante a erros de OCR):**

```python
# Encontra "REVERSE CHARGE" mesmo com erros de OCR como "REVERS CHARG"
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Exemplo — Pesquisa por prefixo:**

```python
# Encontra todos os documentos contendo palavras que começam com "Rechn"
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Consulta vazia:** Passar uma string vazia retorna `[]` imediatamente sem fazer uma chamada HTTP.
{% endhint %}

{% hint style="info" %}
**Tratamento de erros:** Se o serviço fulltextsearch estiver inacessível, a função retorna `[]` e regista um aviso. **Não** lança uma exceção.
{% endhint %}

---

## vector\_search()

Encontra documentos semanticamente semelhantes usando embeddings vetoriais (pesquisa k-NN com vetores de 384 dimensões). Útil para encontrar documentos com conteúdo semelhante independentemente da formulação exata.

```python
vector_search(doc_id, **kwargs)
```

**Parâmetros:**

| Nome | Tipo | Padrão | Descrição |
| ---- | ---- | ------- | ----------- |
| `doc_id` | `str` | obrigatório | UUID do documento fonte (o documento para o qual encontrar correspondências semelhantes) |
| `k` | `int` | `5` | Número de documentos semelhantes a retornar (limitado a 50) |

**Retorna:** `list[dict]` — Cada dict contém:

| Campo | Descrição |
| ----- | ----------- |
| `doc_id` | UUID do documento semelhante |
| `name` | Nome do ficheiro |
| `doc_type` | Tipo de documento |
| `similarity_score` | Pontuação de semelhança bruta (0-1) |
| `similarity_percent` | Semelhança em percentagem (0-100) |

**Exemplo — Encontrar documentos semelhantes:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% semelhante")
```

{% hint style="info" %}
**Como funciona:** Cada documento é convertido num vetor de 384 dimensões quando indexado. A pesquisa vetorial encontra os vizinhos mais próximos neste espaço vetorial, que correspondem a documentos semanticamente semelhantes.
{% endhint %}

---

## fulltext\_search\_erp()

Pesquisa dados mestre do ERP (fornecedores, ordens de compra, clientes, materiais) indexados no OpenSearch.

```python
fulltext_search_erp(query, **kwargs)
```

**Parâmetros:**

| Nome | Tipo | Padrão | Descrição |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obrigatório | Termo de pesquisa |
| `entity_types` | `str` | `None` | Filtrar por tipo de entidade (separado por vírgula: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filtrar por número do fornecedor |
| `vendor_name` | `str` | `None` | Filtrar por nome do fornecedor |
| `company_code` | `str` | `None` | Filtrar por código da empresa |
| `size` | `int` | `10` | Máximo de resultados (limitado a 50) |

**Retorna:** `list[dict]` — Campos específicos do tipo de entidade (registos de fornecedores têm `vendor_number`, `vendor_name`, etc.)

**Exemplo — Validar fornecedor no ERP:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Exemplo — Pesquisar ordens de compra:**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(po_number,
                                   entity_types="purchase_order")
    if results:
        # OC encontrada no ERP
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

Retorna sugestões de autocompletar para termos de pesquisa. Agrupa resultados por categoria (fornecedores, nomes de ficheiros, números de fatura).

```python
fulltext_suggestions(query, **kwargs)
```

**Parâmetros:**

| Nome | Tipo | Padrão | Descrição |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | obrigatório | Prefixo / termo de pesquisa |
| `limit` | `int` | `10` | Máximo de sugestões por categoria (limitado a 20) |

**Retorna:** `dict` com sugestões agrupadas:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Exemplo — Obter sugestões de fornecedores:**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Consulta vazia:** Passar uma string vazia retorna `{}` imediatamente.
{% endhint %}

---

## Referência Rápida

| Função | Objetivo | Retorna |
| -------- | ------- | ------- |
| `fulltext_search(query, ...)` | Pesquisar texto OCR em todos os documentos | `list[dict]` |
| `vector_search(doc_id, ...)` | Encontrar documentos semanticamente semelhantes | `list[dict]` |
| `fulltext_search_erp(query, ...)` | Pesquisar dados mestre do ERP | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Sugestões de autocompletar | `dict` |

---

## Padrões Comuns

### Verificação de Licença

As quatro funções verificam automaticamente a preferência `OPENSEARCH_ENABLED`. Se não estiver ativada:

```python
# Isto irá lançar RuntimeError("Fulltext search license is missing")
results = fulltext_search("test")
```

Para lidar com isto de forma elegante nos scripts:

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    # OpenSearch não ativado para esta organização — ignorar pesquisa
    results = []
```

### Combinar com Funções de Campo

```python
# Pesquisar → validar → definir campo
results = fulltext_search(invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```
