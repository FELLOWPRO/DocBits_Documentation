# Auto-Exportação por Condições

## O que faz este script?

Define automaticamente o estado do documento para "pronto para exportação" quando condições específicas são cumpridas: o fornecedor é um vendedor conhecido/de confiança E o valor da fatura está abaixo de um limiar. Isto salta a validação manual para faturas de baixo risco.

## Trigger

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
# Ler campos relevantes
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Definir fornecedores de confiança para auto-exportação
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-exportar para fornecedores conhecidos com valores baixos
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-exported (small amount, known supplier)"
    )
```

## Explicação Passo a Passo

1. **Ler valor líquido e nome do fornecedor** do documento (fornecedor com `is_clean=True` para comparação)
2. **Definir fornecedores de confiança** — lista de nomes de vendedores conhecidos (limpos/maiúsculas)
3. **Verificar condições** — o fornecedor deve estar na lista de confiança E o valor deve ser inferior a 500
4. **Alterar estado** para `"ready_for_export"` com uma mensagem descritiva

{% hint style="warning" %}
**Atenção:** Alterações de estado acionam workflows a jusante (DocFlow, hooks de exportação). Certifique-se de que as condições são suficientemente rigorosas para evitar exportações não intencionais.
{% endhint %}

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valores dos campos
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Alterar estado do documento
