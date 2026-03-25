# Tarefa para Valor Elevado de Fatura

## O que faz este script?

Cria uma tarefa de aprovação quando o total da fatura excede um limiar (ex.: 100.000). A tarefa é atribuída ao grupo "Finance Approval" e aciona uma notificação por email para garantir uma revisão atempada.

## Trigger

`AFTER_FORMATTING` no tipo de documento **INVOICE**

## Script Completo

```python
# Ler valor total do documento
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Encontrar o grupo Finance Approval pelo nome
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Criar uma tarefa de aprovação
        create_document_task(
            user,
            document_data,
            title="Amount > 100,000 - Approval required",
            description=f"Total amount: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## Explicação Passo a Passo

1. **Ler valor total** do documento
2. **Verificar limiar** — prosseguir apenas se o valor exceder 100.000
3. **Encontrar grupo** pelo nome usando `get_group_by_name()` para obter o ID do grupo dinamicamente
4. **Criar tarefa** atribuída ao grupo financeiro com prioridade alta e notificação por email

## Funções Utilizadas

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Ler valor do campo
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Encontrar grupo pelo nome
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Criar tarefa de aprovação
