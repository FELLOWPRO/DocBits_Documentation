# Dynamische Pflichtfelder

## Was macht dieses Skript?

Setzt Feldanforderungen dynamisch basierend auf dem Dokumentinhalt. In diesem Beispiel: Wenn die Rechnungswährung nicht EUR ist, wird das Wechselkursfeld obligatorisch und sichtbar. Bei EUR-Rechnungen wird das Wechselkursfeld ausgeblendet und optional.

## Auslöser

`ON_FIELD_CHANGE` für Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
# Aktuelle Währung lesen
currency = get_field_value(document_data, "currency", "EUR")

# Fremdwährung: Wechselkurs ist erforderlich und sichtbar
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: Wechselkurs ist optional und ausgeblendet
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Variation: Einkaufsrechnung vs. Kostenrechnung

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Einkaufsrechnung: PO-Nummer ist erforderlich
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Kostenrechnung: PO-Nummer nicht benötigt, Tabelle ausblenden
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Schritt-für-Schritt-Erklärung

1. **Steuerungsfeld lesen** (in diesem Fall Währung)
2. **Geschäftsregeln anwenden** — unterschiedliche Feldanforderungen je nach Wert
3. **Sichtbarkeit setzen** — irrelevante Felder ausblenden, um die UI übersichtlich zu halten
4. **Anforderungen setzen** — relevante Felder als Pflichtfelder markieren

{% hint style="info" %}
**Auslöser-Wahl:** `ON_FIELD_CHANGE` wird bei jeder Feldänderung durch den Benutzer ausgeführt, sodass sich die Anforderungen in Echtzeit aktualisieren. `AFTER_FORMATTING` wird nur einmal nach der initialen Extraktion ausgeführt.
{% endhint %}

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Steuerungsfeld lesen
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Feld als Pflicht/optional setzen
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Felder ein-/ausblenden
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Kategoriefeld setzen
- [delete\_tables()](../table-functions.md#delete\_tables) — Tabellen für Kostenrechnungen entfernen
