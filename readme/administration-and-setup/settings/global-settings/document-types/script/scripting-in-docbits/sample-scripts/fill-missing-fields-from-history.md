# Ontbrekende Velden Invullen uit Historie

{% hint style="info" %}
**Beschikbaar vanaf versie 11.48.0** — Vereist `OPENSEARCH_ENABLED` licentie.
{% endhint %}

## Wat doet dit script?

Wanneer een document een PO-nummer heeft maar de leveranciersnaam ontbreekt, doorzoekt dit script het documentarchief op andere facturen met hetzelfde PO-nummer en kopieert de leveranciersnaam van de eerste overeenkomst.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    # Archief doorzoeken op documenten met dit PO-nummer
    history = fulltext_search(
        org_id, po,
        doc_type="INVOICE",
        size=3
    )

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            break
```

## Stapsgewijze Uitleg

1. **PO-nummer en leverancier lezen** uit het huidige document
2. **Voorwaarde controleren**: Alleen doorgaan als PO bestaat maar leverancier ontbreekt
3. **Archief doorzoeken** op documenten die het PO-nummer bevatten
4. **Leveranciersnaam kopieren** van de eerste overeenkomst die een leveranciersnaam heeft

## Variatie: Meerdere Velden Invullen

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(org_id, po, doc_type="INVOICE", size=3)

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            # Ook andere velden invullen indien beschikbaar
            if doc.get("total_amount") and not get_field_value(document_data, "total_amount", ""):
                set_field_value(document_data, "total_amount", doc["total_amount"])
            break
```

## Gebruikte Functies

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Veldwaarde lezen
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — OCR-tekst doorzoeken in alle documenten
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Veldwaarde schrijven
