# Validação de Fornecedor por Lookup

## O que faz este script?

Valida o número do fornecedor da fatura contra os dados mestre na tabela de lookup. Se o fornecedor for encontrado, o seu nome e condições de pagamento são preenchidos automaticamente. Se não for encontrado, o campo é marcado como inválido para que o utilizador possa corrigi-lo.

## Trigger

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
# Ler ID do fornecedor do documento
supplier_id = get_field_value(document_data, "supplier_id", "")

if supplier_id:
    # Consultar a tabela de lookup de fornecedores
    records = get_lookup_records(
        org_id,                                    # Organização atual
        document_json.get("sub_org_id"),           # Sub-org (se aplicável)
        "supplier",                                # Nome da tabela de lookup
        [["VENDOR_ID", supplier_id]],              # Filtro: correspondência exata por VENDOR_ID
        limit=1                                    # Apenas precisa da primeira correspondência
    )

    if records:
        # Fornecedor encontrado — preencher campos relacionados automaticamente
        supplier = records[0]
        set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
        set_field_value(document_data, "payment_terms", supplier.get("PAYMENT_TERMS", ""))
    else:
        # Fornecedor não encontrado — marcar como inválido
        set_field_as_invalid(document_data, "supplier_id",
                             f"Supplier '{supplier_id}' not found in master data")
```

## Explicação Passo a Passo

1. **Ler ID do fornecedor** do documento usando `get_field_value()`
2. **Consultar tabela de lookup** com `get_lookup_records()` usando o ID do vendedor como filtro
3. **Em caso de correspondência**: Preencher automaticamente o nome do fornecedor e as condições de pagamento a partir dos dados mestre
4. **Sem correspondência**: Marcar o campo de ID do fornecedor como inválido com uma mensagem de erro descritiva

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valor do campo
- [get\_lookup\_records()](../business-logic-functions.md#get\_lookup\_records) — Consultar dados mestre
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escrever valor do campo
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostrar erro de validação
