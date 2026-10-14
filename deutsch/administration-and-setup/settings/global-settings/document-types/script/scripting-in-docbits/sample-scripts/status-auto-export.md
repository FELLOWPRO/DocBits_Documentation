# Auto-Export nach Bedingungen

## Was macht dieses Skript?

Setzt den Dokumentstatus automatisch auf "bereit zum Export", wenn bestimmte Bedingungen erfüllt sind: Der Lieferant ist ein bekannter/vertrauenswürdiger Anbieter UND der Rechnungsbetrag liegt unter einem Schwellwert. Dadurch wird die manuelle Validierung für risikoarme Rechnungen übersprungen.

## Auslöser

`AFTER_FORMATTING` für Dokumenttyp **INVOICE**

## Vollständiges Skript

```python
# Relevante Felder lesen
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Vertrauenswürdige Lieferanten für Auto-Export definieren
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-Export für bekannte Lieferanten mit kleinen Beträgen
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Automatisch exportiert (kleiner Betrag, bekannter Lieferant)"
    )
```

## Schritt-für-Schritt-Erklärung

1. **Nettobetrag und Lieferantenname lesen** aus dem Dokument (Lieferant mit `is_clean=True` für den Vergleich)
2. **Vertrauenswürdige Lieferanten definieren** — Liste bekannter Anbieternamen (bereinigt/Großbuchstaben)
3. **Bedingungen prüfen** — Lieferant muss in der vertrauenswürdigen Liste sein UND der Betrag muss unter 500 liegen
4. **Status ändern** auf `"ready_for_export"` mit einer aussagekräftigen Meldung

{% hint style="warning" %}
**Vorsicht:** Statusänderungen lösen nachgelagerte Workflows aus (DocFlow, Export-Hooks). Stellen Sie sicher, dass die Bedingungen streng genug sind, um unbeabsichtigte Exporte zu vermeiden.
{% endhint %}

## Verwendete Funktionen

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Feldwerte lesen
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Dokumentstatus ändern
