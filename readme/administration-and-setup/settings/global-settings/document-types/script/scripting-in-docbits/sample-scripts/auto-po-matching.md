# Correspondência Automática de OC

## O que faz este script?

Aciona automaticamente a correspondência de OC (Ordem de Compra) quando um número de OC está presente na fatura. O microserviço po-match-service compara os itens de linha da fatura com a OC e preenche os resultados da correspondência.

## Trigger

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
# Ler número da OC do documento
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # Limpar número da OC: remover prefixo e espaços
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Atualizar número da OC limpo
    set_field_value(document_data, "purchase_order", po_nr)

    # Acionar correspondência automática de OC
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## Explicação Passo a Passo

1. **Ler número da OC** da fatura
2. **Limpar** o número da OC removendo prefixos comuns como "PO-" ou "PO "
3. **Atualizar** o número da OC limpo de volta no documento
4. **Acionar correspondência de OC** que chama o po-match-service para comparar as linhas da fatura com as linhas da OC

## O que acontece após a correspondência?

O `document_data` é atualizado com:
- `po_items` — Itens de linha da OC correspondidos
- `po_match_status` — Resultado da correspondência (`"matched"`, `"partially_matched"`, etc.)
- `po_multi_matched` — Se múltiplas OCs foram correspondidas

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valor do campo
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Escrever número da OC limpo
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — Acionar correspondência de OC
