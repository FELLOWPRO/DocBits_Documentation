# Smart Search Ranking

Smart Search Ranking coloca los documentos que buscas al principio de una búsqueda en el panel. Una búsqueda por palabra clave encuentra todos los documentos que contienen tu palabra; Smart Search Ranking añade un paso: una IA lee los mejores resultados y pone primero los documentos que realmente tratan de tu búsqueda. Las coincidencias exactas —números de factura, números de pedido, nombres de proveedor— siempre se quedan arriba.

## Qué cambia

| | Orden por palabra clave | Con Smart Search Ranking |
| --- | --- | --- |
| Qué documentos se encuentran | Los mismos | Los mismos |
| Orden de los resultados | Por coincidencia de palabra clave | Primero los documentos que tratan de tu búsqueda |
| Coincidencias exactas (número de factura, número de pedido, proveedor) | Primero | Primero |
| Ordenación por columna, búsquedas `ocr:` y por campo | Sin cambios | Sin cambios: mantienen su propio orden |

## Ejemplo

Ocho facturas de prueba contienen la palabra *tornillo*: tornillos de acero inoxidable, un juego de destornilladores, el mantenimiento de un compresor de tornillo, pasta en forma de tornillo, una planta, archivadores de tornillos, un fijador de roscas y un maletín surtido de tornillos.

* Busca **tornillo**. En el orden por palabra clave, el juego de destornilladores es el primer resultado y la factura de tornillos es la quinta. Con Smart Search Ranking, los tornillos pasan a ser los primeros y el surtido de tornillos sube; el juego de destornilladores baja al octavo puesto.
* Busca **destornillador**. En el orden por palabra clave, el juego de destornilladores es el primero. Con Smart Search Ranking, los destornilladores profesionales pasan al primer puesto y el juego se queda justo detrás, porque esta vez son destornilladores de verdad; el cóctel y el juguete bajan.

## Dónde se aplica

* En la [Búsqueda rápida](quick-search.md) del panel con texto normal (no en los chips de campo `campo:`).
* Se reordena la parte superior de la lista de resultados; más abajo, las listas largas mantienen su orden por palabra clave.
* Si el servicio de clasificación no responde dentro de su tiempo, la búsqueda muestra el orden normal por palabra clave. No se oculta nada ni se elimina ningún resultado.

## Cómo se activa

Smart Search Ranking lo activa DocBits por organización. Pide a tu contacto de DocBits que lo active. Se aplica a todos los usuarios de la organización en un minuto, sin cambiar tu forma de buscar.
