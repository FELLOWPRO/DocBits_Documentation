# Preencher Campos Ausentes do Histórico de Documentos

{% hint style="info" %}
**Disponível a partir da versão 11.48.0** — Requer licença `OPENSEARCH_ENABLED`.
{% endhint %}

## O que faz este script?

Quando um documento tem um número de OC mas falta o nome do fornecedor, este script pesquisa no arquivo de documentos outras faturas contendo o mesmo número de OC e copia o nome do fornecedor da primeira correspondência.

## Gatilho

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    # Pesquisar no arquivo documentos com este número de OC
    history = fulltext_search(
        org_id, po,
        doc_type="INVOICE",
        size=3
    )

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            break
```

## Explicação Passo a Passo

1. **Ler número da OC e fornecedor** do documento atual
2. **Verificar condição**: Só prosseguir se a OC existir mas o fornecedor estiver ausente
3. **Pesquisar no arquivo** documentos contendo o número da OC
4. **Copiar nome do fornecedor** da primeira correspondência que tenha um nome de fornecedor definido

## Variante: Preencher Múltiplos Campos

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(org_id, po, doc_type="INVOICE", size=3)

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            # Preencher também outros campos se disponíveis
            if doc.get("total_amount") and not get_field_value(document_data, "total_amount", ""):
                set_field_value(document_data, "total_amount", doc["total_amount"])
            break
```

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valor do campo
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Pesquisar texto OCR em todos os documentos
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escrever valor do campo
