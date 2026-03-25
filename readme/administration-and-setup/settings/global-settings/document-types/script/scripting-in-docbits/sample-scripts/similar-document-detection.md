# Rilevamento Documenti Simili (Ricerca Vettoriale)

{% hint style="info" %}
**Disponibile dalla versione 11.48.0** — Richiede la licenza `OPENSEARCH_ENABLED`.
{% endhint %}

## Cosa fa questo script?

Utilizza la ricerca di similarita basata su vettori per trovare documenti semanticamente simili a quello corrente. Se viene trovato un documento con piu del 95% di similarita, il numero fattura viene contrassegnato come potenzialmente fraudolento o duplicato.

## Trigger

`AFTER_FORMATTING` sul tipo di documento **INVOICE**

## Script Completo

```python
doc_id = document_json["doc_id"]
similar = vector_search(org_id, doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similar to: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## Spiegazione Passo per Passo

1. **Ottieni l'ID del documento corrente** da `document_json`
2. **Trova documenti simili** con `vector_search()` restituendo i 5 vicini piu prossimi
3. **Controlla la soglia di similarita**: Se un documento supera il 95% di similarita, viene contrassegnato
4. **Contrassegna come non valido** con il nome del documento simile e il punteggio di similarita

## Come Funziona la Ricerca Vettoriale

Il testo OCR di ogni documento viene convertito in un embedding vettoriale a 384 dimensioni quando viene indicizzato. `vector_search()` trova i vicini piu prossimi in questo spazio vettoriale utilizzando k-NN (k-Nearest Neighbors), restituendo documenti il cui contenuto e semanticamente simile — anche se le parole esatte sono diverse.

**Casi d'uso:**
- Rilevamento frodi (fatture quasi identiche da "fornitori" diversi)
- Rilevamento duplicati che va oltre la corrispondenza esatta del testo
- Ricerca di documenti correlati in formati o lingue diverse

## Funzioni Utilizzate

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Trova documenti semanticamente simili
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostra errore di validazione
