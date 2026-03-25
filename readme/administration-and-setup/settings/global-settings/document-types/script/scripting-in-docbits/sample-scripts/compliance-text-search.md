# Pesquisa de Texto de Conformidade (Reverse Charge)

{% hint style="info" %}
**Disponível a partir da versão 11.48.0** — Requer licença `OPENSEARCH_ENABLED`.
{% endhint %}

## O que faz este script?

Pesquisa texto relevante para conformidade como "REVERSE CHARGE" no arquivo de documentos. Se documentos correspondentes existirem, o código fiscal é automaticamente definido. Suporta tanto correspondência de frase exata como pesquisa fuzzy (tolerante a erros de OCR).

## Gatilho

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
# Pesquisar "REVERSE CHARGE" no arquivo de documentos da organização
rc_docs = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Variante: Pesquisa Fuzzy (Tolerante a Erros de OCR)

```python
# A pesquisa fuzzy tolera erros de OCR como "REVERS CHARG" ou "REVERSE GHARGE"
rc_fuzzy = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Explicação Passo a Passo

1. **Pesquisar no arquivo** a frase exata "REVERSE CHARGE" usando `fulltext_search()`
2. **Filtrar por tipo de documento** para pesquisar apenas faturas
3. **Se encontrado**: Definir automaticamente o campo do código fiscal para "RC"
4. **Variante fuzzy**: Usar `search_type="fuzzy"` para capturar erros de leitura OCR (até 2 caracteres de diferença)

## Funções Utilizadas

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Pesquisar texto OCR em todos os documentos
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escrever valor do campo
