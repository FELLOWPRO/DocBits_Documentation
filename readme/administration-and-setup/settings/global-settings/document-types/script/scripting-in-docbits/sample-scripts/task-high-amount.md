# Zadatak za visok iznos fakture

## Sta ova skripta radi?

Kreira zadatak za odobrenje kada ukupni iznos fakture prelazi prag (npr. 100.000). Zadatak se dodeljuje grupi "Finance Approval" i pokrece obavestenje putem e-poste kako bi se obezbedio blagovremen pregled.

## Okidac

`AFTER_FORMATTING` na tipu dokumenta **INVOICE**

## Kompletna skripta

```python
# Citanje ukupnog iznosa iz dokumenta
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Pronalazenje grupe za odobrenje finansija po nazivu
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Kreiranje zadatka za odobrenje
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

## Objasnjenje korak po korak

1. **Citanje ukupnog iznosa** iz dokumenta
2. **Provera praga** -- nastavlja se samo ako iznos prelazi 100.000
3. **Pronalazenje grupe** po nazivu koriscenjem `get_group_by_name()` za dinamicko preuzimanje ID-a grupe
4. **Kreiranje zadatka** dodeljenog finansijskoj grupi sa visokim prioritetom i obavestenjem putem e-poste

## Koriscene funkcije

- [get\_field\_value()](../field-functions.md#get\_field\_value) -- Citanje vrednosti polja
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) -- Pronalazenje grupe po nazivu
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) -- Kreiranje zadatka za odobrenje
