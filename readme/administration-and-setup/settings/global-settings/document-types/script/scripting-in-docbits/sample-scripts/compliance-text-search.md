# Ricerca Testo di Conformita (Reverse Charge)

{% hint style="info" %}
**Disponibile dalla versione 11.48.0** — Richiede la licenza `OPENSEARCH_ENABLED`.
{% endhint %}

## Cosa fa questo script?

Cerca testo rilevante per la conformita come "REVERSE CHARGE" nell'archivio documenti. Se vengono trovati documenti corrispondenti, il codice fiscale viene impostato automaticamente. Supporta sia la corrispondenza esatta della frase che la ricerca fuzzy (tollerante agli errori di OCR).

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
# Cerca "REVERSE CHARGE" nell'archivio documenti dell'organizzazione
rc_docs = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="match_phrase",
    doc_type="INVOICE",
    size=5
)

if rc_docs:
    set_field_value(document_data, "tax_code", "RC")
```

## Variante: Ricerca Fuzzy (Tollerante agli Errori OCR)

```python
# La ricerca fuzzy tollera errori OCR come "REVERS CHARG" o "REVERSE GHARGE"
rc_fuzzy = fulltext_search(
    org_id, "REVERSE CHARGE",
    search_type="fuzzy",
    vendor_name="ACME Corp"
)

if rc_fuzzy:
    set_field_value(document_data, "tax_code", "RC")
```

## Spiegazione Passo per Passo

1. **Cerca nell'archivio** la frase esatta "REVERSE CHARGE" usando `fulltext_search()`
2. **Filtra per tipo di documento** per cercare solo nelle fatture
3. **Se trovato**: Imposta automaticamente il campo del codice fiscale su "RC"
4. **Variante fuzzy**: Usa `search_type="fuzzy"` per intercettare errori di lettura OCR (fino a 2 caratteri di differenza)

## Funzioni Utilizzate

- [fulltext\_search()](../fulltext-search-functions.md#fulltext\_search) — Cerca nel testo OCR di tutti i documenti
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Scrivi valore campo
