# Attivita per Importo Elevato della Fattura

## Cosa fa questo script?

Crea un'attivita di approvazione quando il totale della fattura supera una soglia (es. 100.000). L'attivita viene assegnata al gruppo "Finance Approval" e attiva una notifica email per garantire una revisione tempestiva.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
# Leggere l'importo totale dal documento
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Trovare il gruppo Finance Approval per nome
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Creare un'attivita di approvazione
        create_document_task(
            user,
            document_data,
            title="Importo > 100.000 - Approvazione necessaria",
            description=f"Importo totale: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## Spiegazione Passo dopo Passo

1. **Leggere l'importo totale** dal documento
2. **Verificare la soglia** — procedere solo se l'importo supera 100.000
3. **Trovare il gruppo** per nome usando `get_group_by_name()` per ottenere l'ID del gruppo dinamicamente
4. **Creare l'attivita** assegnata al gruppo finanziario con priorita alta e notifica email

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggere il valore del campo
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Trovare il gruppo per nome
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Creare l'attivita di approvazione
