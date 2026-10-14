# Vergelijkbare Documenten Detectie (Vectorzoekopdracht)

{% hint style="info" %}
**Beschikbaar vanaf versie 11.48.0** — Vereist `OPENSEARCH_ENABLED` licentie.
{% endhint %}

## Wat doet dit script?

Gebruikt vectorgebaseerde gelijkeniszoekopdracht om documenten te vinden die semantisch vergelijkbaar zijn met het huidige document. Als een document met meer dan 95% gelijkenis wordt gevonden, wordt het factuurnummer gemarkeerd als mogelijk frauduleus of duplicaat.

## Trigger

`AFTER_FORMATTING` op documenttype **INVOICE**

## Volledig Script

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similar to: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## Stapsgewijze Uitleg

1. **Huidig document-ID ophalen** uit `document_json`
2. **Vergelijkbare documenten vinden** met `vector_search()` die de 5 dichtstbijzijnde buren retourneert
3. **Gelijkenisdrempel controleren**: Als een document meer dan 95% gelijkenis vertoont, wordt het gemarkeerd
4. **Als ongeldig markeren** met de naam van het vergelijkbare document en de gelijkenisscore

## Hoe Vectorzoekopdracht Werkt

De OCR-tekst van elk document wordt bij indexering omgezet naar een 384-dimensionale vectorembedding. `vector_search()` vindt de dichtstbijzijnde buren in deze vectorruimte met behulp van k-NN (k-Nearest Neighbors), en retourneert documenten waarvan de inhoud semantisch vergelijkbaar is — zelfs als de exacte woorden verschillen.

**Toepassingen:**
- Fraudedetectie (bijna identieke facturen van verschillende "leveranciers")
- Duplicaatdetectie die verder gaat dan exacte tekstovereenkomst
- Gerelateerde documenten vinden in verschillende formaten of talen

## Gebruikte Functies

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Semantisch vergelijkbare documenten vinden
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Validatiefout weergeven
