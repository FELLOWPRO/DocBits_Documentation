# public.fellow\_kv\_table\_column\_rule

## Tabla `public.fellow_kv_table_column_rule`

### Columnas

* `id`: interno
* `docType`: interno
* `tableName`: interno
* `dlfName`: interno
* `multi_line`: boolean
* `filterID1`: interno
* `filterID2`: interno
* `filterID3`: interno
* `tfidf_doc_id`: interno
* `tfidf_id`: interno
* `valuePattern`: interno
* `coordsY0`: integer
* `coordsY1`: integer
* `coordsX0`: integer
* `coordsX1`: integer
* `normalizedY0`: numeric
* `normalizedY1`: numeric
* `normalizedX0`: numeric
* `normalizedX1`: numeric
* `width`: integer
* `height`: integer
* `patternLeft`: interno
* `patternRight`: interno
* `patternAbove`: interno
* `patternBelow`: interno
* `wordLeft`: interno
* `wordAbove`: interno
* `ruleWeight`: integer
* `user_id`: integer
* `org_id`: ID de la organización
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_new`: boolean

### Análisis y descripción

## Documentación técnica de `public.fellow_kv_table_column_rule`

### Introducción

La tabla `public.fellow_kv_table_column_rule` parece estar diseñada para almacenar reglas y patrones para procesar o extraer datos de documentos. Esto se deduce de la presencia de campos como `docType`, `tableName`, `dlfName` y diversos campos relacionados con patrones y coordenadas. La tabla parece facilitar la aplicación de reglas a distintos tipos de documento, lo que permite el reconocimiento de patrones y la extracción de datos de documentos estructurados, como facturas o contratos.

### Descripción de las columnas

#### id

* **Significado**: Identificador único de cada regla.
* **Función**: Clave primaria.
* **Contenido típico**: Cadenas UUID.
* **Nota**: Esencial para identificar cada fila de forma única.

#### docType

* **Significado**: Tipo de documento al que se aplica la regla.
* **Función**: Campo descriptivo.
* **Contenido típico**: Tipos de documento como 'INVOICE', 'CONTRACT'.
* **Nota**: Ayuda a categorizar las reglas por tipo de documento.

#### tableName

* **Significado**: Nombre de la tabla en la que se aplica la regla.
* **Función**: Campo descriptivo.
* **Contenido típico**: Nombres de tabla como 'INVOICE\_TABLE'.
* **Nota**: Indica el contexto en el que se aplica la regla.

#### dlfName

* **Significado**: Nombre del campo o la columna específicos del documento.
* **Función**: Campo descriptivo.
* **Contenido típico**: Nombres de campo como 'COUNTRY\_ORIGIN'.
* **Nota**: Especifica el campo de destino para la extracción de datos.

#### multi\_line

* **Significado**: Indica si la regla se aplica a texto de varias líneas.
* **Función**: Indicador booleano.
* **Contenido típico**: `True` o `False`.
* **Nota**: Útil para manejar campos de texto de varias líneas.

#### filterID1, filterID2, filterID3

* **Significado**: Filtros o condiciones para aplicar la regla.
* **Función**: Campos descriptivos o condicionales.
* **Contenido típico**: Posiblemente cadenas que representan condiciones de filtro.
* **Nota**: Se utilizan para afinar la aplicación de la regla en función de determinadas condiciones.

#### tfidf\_doc\_id, tfidf\_id

* **Significado**: Identificadores relacionados con el procesamiento TF-IDF.
* **Función**: Funciones similares a una clave externa o identificadores.
* **Contenido típico**: Cadenas UUID.
* **Nota**: Probablemente relacionados con el análisis de texto y la extracción de características.

#### valuePattern

* **Significado**: Patrón de expresión regular para la extracción de valores.
* **Función**: Campo de patrón.
* **Contenido típico**: Expresiones regulares.
* **Nota**: Define el patrón utilizado para identificar y extraer valores.

#### coordsY0, coordsY1, coordsX0, coordsX1

* **Significado**: Coordenadas que definen el cuadro delimitador para la extracción.
* **Función**: Campos de coordenadas.
* **Contenido típico**: Enteros que representan posiciones en píxeles.
* **Nota**: Definen el área de interés de un documento para la extracción de datos.

#### normalizedY0, normalizedY1, normalizedX0, normalizedX1

* **Significado**: Coordenadas normalizadas para la extracción.
* **Función**: Campos de coordenadas.
* **Contenido típico**: Valores numéricos que representan posiciones proporcionales.
* **Nota**: Se utilizan para definir áreas independientes de la resolución.

#### width, height

* **Significado**: Dimensiones del área definida por las coordenadas.
* **Función**: Campos de dimensiones.
* **Contenido típico**: Valores enteros.
* **Nota**: Ayudan a definir el tamaño del área de extracción.

#### patternLeft, patternRight, patternAbove, patternBelow

* **Significado**: Patrones contextuales que rodean los datos de destino.
* **Función**: Campos de patrón.
* **Contenido típico**: Expresiones regulares.
* **Nota**: Proporcionan contexto sobre dónde se encuentran los datos en relación con otro texto.

#### wordLeft, wordAbove

* **Significado**: Palabras específicas situadas cerca de los datos de destino.
* **Función**: Campos contextuales.
* **Contenido típico**: Palabras o frases específicas.
* **Nota**: Ayudan a afinar la búsqueda de los datos de destino en función de las palabras cercanas.

#### ruleWeight

* **Significado**: Importancia o prioridad de la regla.
* **Función**: Campo de peso o prioridad.
* **Contenido típico**: Valores enteros.
* **Nota**: Los valores más altos podrían indicar una mayor prioridad o importancia.

#### user\_id

* **Significado**: Identificador del usuario que creó o modificó la regla.
* **Función**: Clave externa.
* **Contenido típico**: Valores enteros.
* **Nota**: Vincula la regla con un usuario específico.

#### org\_id

* **Significado**: Identificador de la organización asociada con la regla.
* **Función**: Clave externa.
* **Contenido típico**: Cadenas UUID.
* **Nota**: Asocia la regla con una organización.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó la regla.
* **Función**: Campo técnico.
* **Contenido típico**: Marca de tiempo con zona horaria.
* **Nota**: Útil para realizar el seguimiento del historial de creación de la regla.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación de la regla.
* **Función**: Campo técnico.
* **Contenido típico**: Marca de tiempo con zona horaria o `None`.
* **Nota**: Registra los cambios de la regla a lo largo del tiempo.

#### is\_deleted

* **Significado**: Indica si la regla está marcada como eliminada.
* **Función**: Indicador booleano.
* **Contenido típico**: `True` o `False`.
* **Nota**: Se utiliza para el borrado lógico de reglas.

#### is\_new

* **Significado**: Indica si la regla se ha creado recientemente.
* **Función**: Indicador booleano.
* **Contenido típico**: `True` o `False`.
* **Nota**: Ayuda a identificar las reglas añadidas recientemente.
