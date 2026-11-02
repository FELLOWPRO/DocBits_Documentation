# Erkennung ähnlicher Dokumente (Vektorsuche)

{% hint style="info" %}
**Verfügbar ab Version 11.48.0** — Erfordert die Lizenz `OPENSEARCH_ENABLED`.
{% endhint %}

## Was macht dieses Skript?

Verwendet eine vektorbasierte Ähnlichkeitssuche, um Dokumente zu finden, die dem aktuellen semantisch ähnlich sind. Wird ein Dokument mit mehr als 95 % Ähnlichkeit gefunden, wird die Rechnungsnummer als potenziell betrügerisch oder doppelt markiert.

## Auslöser

`AFTER_FORMATTING` auf Dokumenttyp **INVOICE**

## Vollständiges Skript

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

## Schritt-für-Schritt-Erklärung

1. **ID des aktuellen Dokuments abrufen** aus `document_json`
2. **Ähnliche Dokumente finden** mit `vector_search()`, das die 5 nächsten Nachbarn zurückgibt
3. **Ähnlichkeitsschwelle prüfen**: Überschreitet ein Dokument 95 % Ähnlichkeit, wird es markiert
4. **Als ungültig markieren** mit dem Namen des ähnlichen Dokuments und dem Ähnlichkeitswert

## So funktioniert die Vektorsuche

Der OCR-Text jedes Dokuments wird bei der Indizierung in ein 384-dimensionales Vektor-Embedding umgewandelt. `vector_search()` findet per k-NN (k-Nearest Neighbors) die nächsten Nachbarn in diesem Vektorraum und liefert Dokumente, deren Inhalt semantisch ähnlich ist — auch wenn die genauen Wörter abweichen.

**Anwendungsfälle:**
- Betrugserkennung (nahezu identische Rechnungen von unterschiedlichen „Lieferanten")
- Duplikaterkennung, die über den exakten Textvergleich hinausgeht
- Verwandte Dokumente über verschiedene Formate oder Sprachen hinweg finden

## Verwendete Funktionen

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Semantisch ähnliche Dokumente finden
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Validierungsfehler anzeigen
