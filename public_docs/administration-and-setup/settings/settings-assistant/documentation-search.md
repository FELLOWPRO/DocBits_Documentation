# Cómo funciona la búsqueda en la documentación

El Settings Assistant busca información relevante en las páginas públicas de [docs.docbits.com](https://docs.docbits.com). Los resultados pueden incluir el título de una página, un pasaje corto y un enlace a la página de origen. Abra el enlace cuando necesite las instrucciones completas o una captura de pantalla.

## Encontrar la página correcta

La búsqueda combina coincidencia de palabras con coincidencia por significado. Eso ayuda cuando su pregunta usa palabras distintas de las de un título de página. El asistente también puede usar la página de ajustes que está viendo para hacer la respuesta más relevante.

Si la búsqueda por significado no está disponible temporalmente, la búsqueda en la documentación puede seguir usando la coincidencia de palabras. Una pregunta concreta con el nombre de la opción es la mejor forma de volver a intentarlo.

## Idiomas

La búsqueda en la documentación usa actualmente los índices de páginas de ayuda en **inglés** y **alemán**. Si la interfaz de DocBits usa otro idioma, el asistente recurre a resultados de documentación en inglés. La página enlazada muestra su propio idioma; compruébelo antes de seguir pasos o comparar capturas.

## Cuándo son consultables los cambios

El índice de búsqueda se actualiza cuando se publican cambios en la documentación inglesa o alemana desde el repositorio de documentación. Una conciliación periódica también elimina los enlaces a páginas que ya no están en la navegación de la documentación. Una página recién publicada puede tardar un poco en aparecer en el asistente.

### Resumen técnico para administradores

Las páginas de ayuda publicadas se dividen en secciones y se guardan en un **OpenSearch documentation index** propio por cada idioma admitido. Este índice está separado de los índices que se usan para los documentos subidos de una organización. Cuando una página cambia, las secciones sin cambios pueden omitirse y las modificadas se indexan de nuevo. Las páginas eliminadas se borran del índice de documentación.

Para una pregunta, el servicio combina coincidencias de palabras clave con similitud vectorial y después ordena los pasajes más relevantes. Si el servicio de embeddings no está disponible, la búsqueda por palabras clave sigue disponible. El Settings Assistant recibe enlaces de origen y pasajes cortos de esta búsqueda en la documentación; no lee el índice de documentos de una organización para este fin.

Si no encuentra una página, busque directamente en [docs.docbits.com](https://docs.docbits.com), pruebe una pregunta más precisa o contacte con el soporte de DocBits.

{% hint style="info" %}
Esta búsqueda abarca las páginas de ayuda de DocBits. La función [Fulltext Search](../document-processing/module/fulltext-search.md) busca en los documentos de su organización y tiene ajustes propios.
{% endhint %}

Volver a [usar el Settings Assistant](README.md).
