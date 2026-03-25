# Compilazione Campi Mancanti dalla Cronologia

{% hint style="info" %}
**Disponibile dalla versione 11.48.0** — Richiede la licenza `OPENSEARCH_ENABLED`.
{% endhint %}

## Cosa fa questo script?

Quando un documento ha un numero OdA ma manca il nome del fornitore, questo script cerca nell'archivio documenti altre fatture contenenti lo stesso numero OdA e copia il nome del fornitore dalla prima corrispondenza.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    # Cerca nell'archivio documenti con questo numero OdA
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

## Spiegazione Passo per Passo

1. **Leggi numero OdA e fornitore** dal documento corrente
2. **Controlla la condizione**: Procedi solo se l'OdA esiste ma il fornitore manca
3. **Cerca nell'archivio** i documenti contenenti il numero OdA
4. **Copia il nome del fornitore** dalla prima corrispondenza che ha un nome fornitore impostato

## Variante: Compila Piu Campi

```python
po = get_field_value(document_data, "purchase_order", "")
supplier = get_field_value(document_data, "supplier_name", "")

if po and not supplier:
    history = fulltext_search(org_id, po, doc_type="INVOICE", size=3)

    for doc in history:
        if doc.get("vendor_name"):
            set_field_value(document_data, "supplier_name", doc["vendor_name"])
            # Compila anche altri campi se disponibili
            if doc.get("total_amount") and not get_field_value(document_data, "total_amount", ""):
                set_field_value(document_data, "total_amount", doc["total_amount"])
            break
```

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggi valore campo
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Cerca nel testo OCR di tutti i documenti
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Scrivi valore campo
