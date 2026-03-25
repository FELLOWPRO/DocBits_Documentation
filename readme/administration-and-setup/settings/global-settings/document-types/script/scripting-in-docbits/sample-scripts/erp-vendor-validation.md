# Validação de Fornecedor ERP

{% hint style="info" %}
**Disponível a partir da versão 11.48.0** — Requer licença `OPENSEARCH_ENABLED`.
{% endhint %}

## O que faz este script?

Valida se o fornecedor na fatura existe nos dados mestre do ERP indexados no OpenSearch. Se o fornecedor não for encontrado no ERP, o campo é marcado como inválido. Isto complementa a função existente `is_supplier_valid()` pesquisando no índice do ERP em vez da tabela de lookup.

## Gatilho

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
vendor = get_field_value(document_data, "supplier_name", "")

if vendor:
    erp_matches = fulltext_search_erp(
        org_id, vendor,
        entity_types="vendor",
        size=5
    )

    if not erp_matches:
        set_field_as_invalid(
            document_data, "supplier_name",
            "Vendor not found in ERP master data"
        )
```

## Variante: Validar com Número do Fornecedor

```python
vendor_nr = get_field_value(document_data, "supplier_id", "")

if vendor_nr:
    erp_matches = fulltext_search_erp(
        org_id, vendor_nr,
        entity_types="vendor",
        vendor_number=vendor_nr,
        size=1
    )

    if erp_matches:
        # Preencher automaticamente o nome do fornecedor a partir do ERP
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Explicação Passo a Passo

1. **Ler nome do fornecedor** do documento atual
2. **Pesquisar dados mestre do ERP** com `fulltext_search_erp()` filtrando por tipo de entidade `"vendor"`
3. **Se não encontrado**: Marcar o campo do nome do fornecedor como inválido
4. **Variante**: Pesquisar por número do fornecedor e preencher automaticamente o nome do fornecedor a partir dos dados do ERP

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valor do campo
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — Pesquisar dados mestre do ERP
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostrar erro de validação
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escrever valor do campo
