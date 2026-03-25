# Detecção de Faturas Duplicadas

{% hint style="info" %}
**Disponível a partir da versão 11.48.0** — Requer licença `OPENSEARCH_ENABLED`.
{% endhint %}

## O que faz este script?

Pesquisa no arquivo de documentos faturas existentes com o mesmo número de fatura do mesmo fornecedor. Se um potencial duplicado for encontrado, o campo do número da fatura é marcado como inválido com um aviso mostrando o nome do documento duplicado e o seu estado.

## Gatilho

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    # Pesquisar documentos com o mesmo número de fatura do mesmo fornecedor
    existing = fulltext_search(
        org_id, inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )

    # Excluir o documento atual dos resultados
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Possible duplicate: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Explicação Passo a Passo

1. **Ler número da fatura e fornecedor** do documento atual
2. **Pesquisar no arquivo** com `fulltext_search()` filtrando por nome do fornecedor e estados relevantes
3. **Excluir o documento atual** dos resultados para evitar auto-correspondência
4. **Marcar como inválido** se algum duplicado for encontrado, mostrando o nome do ficheiro e o estado do documento existente

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valor do campo
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Pesquisar texto OCR em todos os documentos
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostrar erro de validação
