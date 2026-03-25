# Taak bij Hoog Factuurbedrag

## Wat doet dit script?

Maakt een goedkeuringstaak aan wanneer het factuurtotaal een drempelwaarde overschrijdt (bijv. 100.000). De taak wordt toegewezen aan de groep "Finance Approval" en activeert een e-mailnotificatie om tijdige beoordeling te garanderen.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
# Totaalbedrag uit het document lezen
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # De Finance Approval-groep zoeken op naam
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Een goedkeuringstaak aanmaken
        create_document_task(
            user,
            document_data,
            title="Bedrag > 100.000 - Goedkeuring vereist",
            description=f"Totaalbedrag: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## Stapsgewijze Uitleg

1. **Totaalbedrag lezen** uit het document
2. **Drempelwaarde controleren** — alleen doorgaan als het bedrag hoger is dan 100.000
3. **Groep zoeken** op naam met `get_group_by_name()` om de groeps-ID dynamisch op te halen
4. **Taak aanmaken** toegewezen aan de financiele groep met hoge prioriteit en e-mailnotificatie

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Veldwaarde lezen
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Groep zoeken op naam
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Goedkeuringstaak aanmaken
