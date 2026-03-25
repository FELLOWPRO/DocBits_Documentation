# Detección de Documentos Similares (Búsqueda Vectorial)

{% hint style="info" %}
**Disponible desde la versión 11.48.0** — Requiere licencia `OPENSEARCH_ENABLED`.
{% endhint %}

## ¿Qué hace este script?

Utiliza búsqueda de similitud basada en vectores para encontrar documentos semánticamente similares. Si se encuentra un documento con más del 95% de similitud, el número de factura se marca como potencialmente fraudulento o duplicado.

## Disparador

`AFTER_FORMATTING` en tipo de documento **INVOICE**

## Script Completo

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similar a: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## Funciones Utilizadas

- [vector\_search()](../fulltext-search-functions.md#vector\_search)
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid)
