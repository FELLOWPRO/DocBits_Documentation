# Auto-Export op Basis van Voorwaarden

## Wat doet dit script?

Stelt automatisch de documentstatus in op "ready for export" wanneer aan specifieke voorwaarden is voldaan: de leverancier is een bekende/vertrouwde leverancier EN het factuurbedrag ligt onder een drempelwaarde. Dit slaat handmatige validatie over voor laagrisicofacturen.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
# Relevante velden lezen
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Vertrouwde leveranciers definiëren voor auto-export
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-export voor bekende leveranciers met kleine bedragen
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-geëxporteerd (klein bedrag, bekende leverancier)"
    )
```

## Stapsgewijze Uitleg

1. **Nettobedrag en leveranciersnaam lezen** uit het document (leverancier met `is_clean=True` voor vergelijking)
2. **Vertrouwde leveranciers definiëren** — lijst van bekende leveranciersnamen (opgeschoond/hoofdletters)
3. **Voorwaarden controleren** — leverancier moet in de vertrouwde lijst staan EN het bedrag moet onder 500 liggen
4. **Status wijzigen** naar `"ready_for_export"` met een beschrijvend bericht

{% hint style="warning" %}
**Let op:** Statuswijzigingen activeren downstream-workflows (DocFlow, exporthooks). Zorg ervoor dat de voorwaarden streng genoeg zijn om onbedoelde exports te voorkomen.
{% endhint %}

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Veldwaarden lezen
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Documentstatus wijzigen
