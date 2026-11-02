# Detección de Documentos Similares (Búsqueda Vectorial)

{% hint style="info" %}
**Disponible desde la versión 11.48.0** — Requiere licencia `OPENSEARCH_ENABLED`.
{% endhint %}

## ¿Qué hace este script?

Utiliza una búsqueda de similitud basada en vectores para encontrar documentos semánticamente similares al actual. Si se encuentra un documento con más del 95 % de similitud, el número de factura se marca como potencialmente fraudulento o duplicado.

## Disparador

`AFTER_FORMATTING` en el tipo de documento **INVOICE**

## Script Completo

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

## Explicación Paso a Paso

1. **Obtener el ID del documento actual** desde `document_json`
2. **Buscar documentos similares** con `vector_search()`, que devuelve los 5 vecinos más cercanos
3. **Comprobar el umbral de similitud**: si algún documento supera el 95 % de similitud, se marca
4. **Marcar como no válido** con el nombre del documento similar y su puntuación de similitud

## Cómo Funciona la Búsqueda Vectorial

El texto OCR de cada documento se convierte en un vector de incrustación (embedding) de 384 dimensiones al indexarse. `vector_search()` encuentra los vecinos más cercanos en este espacio vectorial mediante k-NN (k vecinos más cercanos) y devuelve documentos cuyo contenido es semánticamente similar, incluso si las palabras exactas difieren.

**Casos de uso:**
- Detección de fraude (facturas casi idénticas de distintos "proveedores")
- Detección de duplicados que va más allá de la coincidencia exacta de texto
- Búsqueda de documentos relacionados en distintos formatos o idiomas

## Funciones Utilizadas

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Encontrar documentos semánticamente similares
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Mostrar un error de validación
