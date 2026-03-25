# Rilevamento Fatture Duplicate

{% hint style="info" %}
**Disponibile dalla versione 11.48.0** — Richiede la licenza `OPENSEARCH_ENABLED`.
{% endhint %}

## Cosa fa questo script?

Cerca nell'archivio documenti le fatture esistenti con lo stesso numero di fattura dallo stesso fornitore. Se viene trovato un potenziale duplicato, il campo del numero fattura viene contrassegnato come non valido con un avviso che mostra il nome del documento duplicato e il suo stato.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
inv_id = get_field_value(document_data, "invoice_id", "")
vendor = get_field_value(document_data, "supplier_name", "")

if inv_id and vendor:
    # Cerca documenti con lo stesso numero fattura dallo stesso fornitore
    existing = fulltext_search(
        inv_id,
        vendor_name=vendor,
        status="ready_for_validation,exported",
        size=5
    )

    # Escludi il documento corrente dai risultati
    current_doc_id = document_json["doc_id"]
    duplicates = [d for d in existing if d["doc_id"] != current_doc_id]

    if duplicates:
        dup = duplicates[0]
        set_field_as_invalid(
            document_data, "invoice_id",
            f"Possible duplicate: {dup['name']} ({dup.get('status', 'unknown')})"
        )
```

## Spiegazione Passo per Passo

1. **Leggi numero fattura e fornitore** dal documento corrente
2. **Cerca nell'archivio** con `fulltext_search()` filtrando per nome fornitore e stati rilevanti
3. **Escludi il documento corrente** dai risultati per evitare auto-corrispondenze
4. **Contrassegna come non valido** se viene trovato un duplicato, mostrando il nome del file e lo stato del documento esistente

## Funzioni Utilizzate

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Leggi valore campo
- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Cerca nel testo OCR di tutti i documenti
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostra errore di validazione
