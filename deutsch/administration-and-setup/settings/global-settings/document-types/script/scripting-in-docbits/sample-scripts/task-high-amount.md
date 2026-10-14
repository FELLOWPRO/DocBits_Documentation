# Aufgabe bei hohem Rechnungsbetrag

## Was macht dieses Skript?

Erstellt eine Genehmigungsaufgabe, wenn die Rechnungssumme einen Schwellwert überschreitet (z.B. 100.000). Die Aufgabe wird der Gruppe "Finance Approval" zugewiesen und löst eine E-Mail-Benachrichtigung aus, um eine rechtzeitige Prüfung sicherzustellen.

## Auslöser

`AFTER_FORMATTING` für Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
# Gesamtbetrag aus dem Dokument lesen
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Gruppe "Finance Approval" nach Name suchen
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Genehmigungsaufgabe erstellen
        create_document_task(
            user,
            document_data,
            title="Betrag > 100.000 - Genehmigung erforderlich",
            description=f"Gesamtbetrag: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## Schritt-für-Schritt-Erklärung

1. **Gesamtbetrag lesen** aus dem Dokument
2. **Schwellwert prüfen** — nur fortfahren, wenn der Betrag 100.000 überschreitet
3. **Gruppe finden** nach Name mit `get_group_by_name()`, um die Gruppen-ID dynamisch zu ermitteln
4. **Aufgabe erstellen** zugewiesen an die Finanzgruppe mit hoher Priorität und E-Mail-Benachrichtigung

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Feldwert lesen
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Gruppe nach Name finden
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Genehmigungsaufgabe erstellen
