# Validazione Fornitore ERP

{% hint style="info" %}
**Disponibile dalla versione 11.48.0** — Richiede la licenza `OPENSEARCH_ENABLED`.
{% endhint %}

## Cosa fa questo script?

Verifica se il fornitore sulla fattura esiste nei dati master ERP indicizzati in OpenSearch. Se il fornitore non viene trovato nell'ERP, il campo viene contrassegnato come non valido. Questo integra la funzione esistente `is_supplier_valid()` cercando nell'indice ERP anziche nella tabella di lookup.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
vendor = get_field_value(document_data, "supplier_name", "")

if vendor:
    erp_matches = fulltext_search_erp(
        vendor,
        entity_types="vendor",
        size=5
    )

    if not erp_matches:
        set_field_as_invalid(
            document_data, "supplier_name",
            "Vendor not found in ERP master data"
        )
```

## Variante: Validazione con Numero Fornitore

```python
vendor_nr = get_field_value(document_data, "supplier_id", "")

if vendor_nr:
    erp_matches = fulltext_search_erp(
        vendor_nr,
        entity_types="vendor",
        vendor_number=vendor_nr,
        size=1
    )

    if erp_matches:
        # Compila automaticamente il nome del fornitore dall'ERP
        erp_vendor = erp_matches[0]
        set_field_value(document_data, "supplier_name",
                        erp_vendor.get("vendor_name", ""))
    else:
        set_field_as_invalid(
            document_data, "supplier_id",
            f"Vendor '{vendor_nr}' not found in ERP"
        )
```

## Spiegazione Passo per Passo

1. **Leggi il nome del fornitore** dal documento corrente
2. **Cerca nei dati master ERP** con `fulltext_search_erp()` filtrando per tipo di entita `"vendor"`
3. **Se non trovato**: Contrassegna il campo nome fornitore come non valido
4. **Variante**: Cerca per numero fornitore e compila automaticamente il nome del fornitore dai dati ERP

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggi valore campo
- [fulltext\_search\_erp()](../fulltext-search-functions.md#fulltext\_search\_erp) — Cerca nei dati master ERP
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostra errore di validazione
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Scrivi valore campo
