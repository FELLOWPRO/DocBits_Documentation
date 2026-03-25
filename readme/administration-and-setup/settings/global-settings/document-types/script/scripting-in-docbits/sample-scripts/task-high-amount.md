# Tâche pour Montant Élevé de Facture

## Que fait ce script ?

Crée une tâche d'approbation lorsque le total de la facture dépasse un seuil (ex. 100 000). La tâche est assignée au groupe "Finance Approval" et déclenche une notification par e-mail pour assurer une révision rapide.

## Déclencheur

`AFTER_FORMATTING` sur le type de document **INVOICE**

## Script complet

```python
# Lire le montant total depuis le document
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Trouver le groupe Finance Approval par nom
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Créer une tâche d'approbation
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

## Explication étape par étape

1. **Lire le montant total** depuis le document
2. **Vérifier le seuil** — ne procéder que si le montant dépasse 100 000
3. **Trouver le groupe** par nom avec `get_group_by_name()` pour obtenir l'ID du groupe dynamiquement
4. **Créer la tâche** assignée au groupe financier avec priorité haute et notification par e-mail

## Fonctions utilisées

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Lire la valeur du champ
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Trouver le groupe par nom
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Créer une tâche d'approbation
