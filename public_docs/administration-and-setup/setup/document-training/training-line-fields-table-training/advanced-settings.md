# Configuración Avanzada

En algunos documentos, las estructuras de tabla pueden ser complejas: abarcan varias líneas, contienen información agrupada o incluyen filas adicionales innecesarias. Los _Ajustes avanzados_ en el modo de formación te permiten ajustar la extracción de tablas para estos casos y mejorar la precisión y la coherencia.

Para acceder a estos ajustes, activa el **Modo Formación** y haz clic en el icono de engranaje **Ajustes** de la barra de acciones superior:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-gear-es-20261112.png" alt="Pantalla de extracción de tablas en modo formación con el puntero sobre el icono de engranaje Ajustes en la barra de acciones superior."><figcaption><p>El engranaje Ajustes de la barra de acciones del modo formación abre la configuración avanzada.</p></figcaption></figure>

El diálogo **Ajustes** contiene todas las opciones descritas en esta página. Despliega la sección **Ajustes avanzados** para llegar a las opciones de agrupación, que permanecen contraídas hasta que las abras:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-max-rows-es-20261112.png" alt="Diálogo Ajustes con Recuento de hileras de encabezado 2 y la sección Ajustes avanzados desplegada, con Filas minimas agrupadas 2, Filas agrupadas máximas 3, Columnas de grupo distintas, Agrupación inversa y Texto dividido."><figcaption><p>La sección Ajustes avanzados con todas las opciones de agrupación.</p></figcaption></figure>

Cada opción se describe en su propia sección a continuación, junto con el efecto que tiene sobre la tabla extraída.

### Recuento de hileras de encabezado

**Utiliza este ajuste para definir cuántas líneas componen el encabezado de la tabla.**

Algunas tablas tienen encabezados de varias líneas. Por ejemplo, el encabezado de esta tabla abarca dos líneas:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-two-lines-es-20261112.png" alt="Tabla de factura cuyo encabezado abarca dos líneas (Preis / in EUR y Betrag / in EUR)."><figcaption><p>Un encabezado de tabla que abarca dos líneas.</p></figcaption></figure>

Ajusta el **Recuento de hileras de encabezado** para que coincida:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-row-count-es-20261112.png" alt="Diálogo Ajustes con Recuento de hileras de encabezado configurado en 2."><figcaption><p>Recuento de hileras de encabezado configurado en 2 en el diálogo Ajustes.</p></figcaption></figure>

#### ¿Por qué es importante?

Si no lo configuras, DocBits puede tratar la segunda línea como datos en lugar de como parte del encabezado, lo que provoca errores de extracción:

**Antes:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-before-es-20261112.png" alt="Tabla extraída con un recuento de hileras de encabezado incorrecto: la segunda línea del encabezado aparece como fila de datos y los encabezados de columna no están mapeados."><figcaption><p>Antes: la segunda línea del encabezado se trata como datos.</p></figcaption></figure>

Después:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-header-after-es-20261112.png" alt="Tabla extraída con Recuento de hileras de encabezado 2: las columnas están mapeadas como Posición, Descripción, Cantidad, Precio Unitario e Importe Neto y las filas son correctas."><figcaption><p>Después: las filas del encabezado y de los datos están separadas correctamente.</p></figcaption></figure>

### Mover filas adicionales a Basura

**Utiliza esto para descartar entradas de varias líneas no deseadas, como descripciones que desbordan.**

En este ejemplo, la descripción se extiende a varias filas, pero solo la primera línea es relevante:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-overflow-doc-es-20261112.png" alt="Tabla de factura en la que la descripción de cada artículo continúa en líneas de texto adicionales debajo del artículo."><figcaption><p>La descripción se extiende a varias líneas, de las que solo la primera es relevante.</p></figcaption></figure>

Configura **Mover filas adicionales a** en **Basura** para eliminar el desbordamiento:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-move-extra-rows-es-20261112.png" alt="Diálogo Ajustes con Mover filas adicionales a configurado en Basura."><figcaption><p>Mover filas adicionales a configurado en Basura.</p></figcaption></figure>

**Resultado después del mapeo:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-trash-result-es-20261112.png" alt="Pantalla de extracción de tablas: el documento de origen muestra la descripción de cada artículo repartida en dos líneas, mientras que la tabla extraída de la derecha ya contiene una fila limpia por artículo."><figcaption><p>Resultado después del mapeo: las líneas sobrantes han desaparecido y solo quedan las filas relevantes.</p></figcaption></figure>

### Filas minimas agrupadas

**Utiliza esto cuando las filas deban agruparse bajo una fila principal (por ejemplo, elementos de línea con varias sublíneas).**

Aquí solo tres de seis filas son relevantes. Se mapean dos columnas clave (por ejemplo, Posición y Descripción), mientras que las demás se tratan como campos personalizados.

Empieza configurando el **Recuento de hileras de encabezado** y las **Filas minimas agrupadas**, es decir, el número mínimo de filas que debe tener un grupo para que DocBits las una:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-es-20261112.png" alt="Diálogo Ajustes con Recuento de hileras de encabezado 2 y la sección Ajustes avanzados desplegada, con Filas minimas agrupadas configurado en 2."><figcaption><p>Recuento de hileras de encabezado y Filas minimas agrupadas configurados en el diálogo Ajustes.</p></figcaption></figure>

Configura también **Mover filas adicionales a** en **Basura** para limpiar los datos que no son relevantes:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-min-grouped-trash-es-20261112.png" alt="Diálogo Ajustes con Recuento de hileras de encabezado 2, Mover filas adicionales a Basura y Filas minimas agrupadas 2."><figcaption><p>Mover filas adicionales a configurado además en Basura.</p></figcaption></figure>

A continuación define la columna clave de agrupación, por ejemplo _Posición_, abriendo el menú de columna de esa columna y eligiendo **Hileras grupales**:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-group-key-es-20261112.png" alt="Tabla extraída con el menú de la columna Posición abierto, que muestra Eliminar columna, Hileras grupales y Regular."><figcaption><p>Elige Hileras grupales en el menú de la columna clave de agrupación (Posición).</p></figcaption></figure>

Las otras dos entradas de ese menú actúan sobre la misma columna: con **Eliminar columna** ocultas la columna de la tabla extraída (la asignación de nombre de esa columna se libera y, si era la columna de agrupación, la agrupación se cancela); con **Regular** abres el diálogo **Gestionar reglas** en la pestaña REGULAR, donde defines la expresión regular de la columna, explicada en [Estructuración y Mejora de la Extracción de Tablas en DocBits](improving-table-extraction-with-regex.md).

La agrupación en sí y las demás herramientas de columna que funcionan junto con ella (selección manual de filas y mapeo de columnas) se explican paso a paso en [Estructuración y Mejora de la Extracción de Tablas en DocBits](improving-table-extraction-with-regex.md).

**Resultado:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-grouped-result-es-20261112.png" alt="Pantalla de extracción de tablas: el documento de origen contiene seis líneas físicas, dos por artículo, y la tabla extraída de la derecha muestra una fila agrupada por artículo."><figcaption><p>Resultado: las seis filas físicas se agrupan en tres elementos de línea.</p></figcaption></figure>

#### Filas agrupadas máximas

**Utiliza esto para limitar cuántas filas puede contener un grupo.** La información sobre herramientas de la opción pregunta: _¿Cuántas filas tiene el máximo de su columna agrupada?_ Es la contrapartida de Filas minimas agrupadas: un grupo que necesitaría más filas que este número no se une.

Déjalo vacío cuando los grupos puedan tener cualquier tamaño. Configúralo cuando un documento contenga artículos con muchas sublíneas y quieras que DocBits deje sin agrupar los bloques inusualmente grandes para que puedas revisarlos tú mismo.

Se configura en la misma área del diálogo que Filas minimas agrupadas, directamente debajo:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-max-rows-es-20261112.png" alt="Diálogo Ajustes con Filas minimas agrupadas 2 y Filas agrupadas máximas 3, mientras Columnas de grupo distintas, Agrupación inversa y Texto dividido están desmarcadas."><figcaption><p>Filas agrupadas máximas (aquí 3) está directamente debajo de Filas minimas agrupadas.</p></figcaption></figure>

#### Columnas de grupo distintas

**Utiliza esto para conservar solo valores únicos en la columna clave de agrupación.**

La información sobre herramientas de la propia opción pregunta: _¿Quieres solo valores únicos para tu columna agrupada?_ Actívala cuando varios grupos lleven el mismo valor en la columna clave de agrupación y quieras que DocBits conserve ese valor una sola vez, de modo que los grupos repetidos muestren la clave vacía en lugar del valor duplicado.

Es una casilla de verificación de la misma sección que Filas minimas agrupadas:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-distinct-split-es-20261112.png" alt="Diálogo Ajustes con la sección Ajustes avanzados: las casillas Columnas de grupo distintas y Texto dividido están marcadas y Agrupación inversa no."><figcaption><p>Columnas de grupo distintas es la casilla situada debajo de Filas agrupadas máximas.</p></figcaption></figure>

#### Agrupación inversa

**Utiliza esto cuando la fila de agrupación aparezca** _**después**_ **de las filas que debería agrupar.**

La información sobre herramientas de la opción pregunta: _¿Quieres combinar todas las filas sobre el atributo agrupado?_ Actívala cuando la fila que lleva la clave de agrupación (por ejemplo, la posición o el importe) esté _debajo_ de sus líneas de continuación, para que DocBits una en el grupo las filas situadas por encima de la clave en lugar de las que están por debajo:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-doc-es-20261112.png" alt="Tabla de factura en la que la línea de descripción está encima de la línea que lleva posición, cantidad e importes."><figcaption><p>La fila de agrupación aparece después de las filas que debería agrupar.</p></figcaption></figure>

Activa **Agrupación inversa**, agrupa por una columna principal (por ejemplo, Importe Neto) y configura **Mover filas adicionales a** en **Basura** si es necesario:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-dialog-es-20261112.png" alt="Diálogo Ajustes con Agrupación inversa marcada, Mover filas adicionales a Basura y Recuento de hileras de encabezado 2."><figcaption><p>Agrupación inversa activada junto con Mover filas adicionales a Basura.</p></figcaption></figure>

**Resultado final:**

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-reverse-result-es-20261112.png" alt="Tabla extraída con tres filas después de la agrupación inversa por la columna de importe."><figcaption><p>Resultado final con agrupación inversa.</p></figcaption></figure>

#### Texto dividido

**Utiliza esto para dividir el texto de una celda exactamente en el separador de columna.**

La información sobre herramientas de la opción pregunta: _¿Quieres dividir el texto exactamente en el separador de columna?_ Actívala cuando una celda extraída contenga el texto de dos columnas que el separador de la tabla no separó. DocBits vuelve a extraer la tabla y corta cada valor en la posición del separador que hayas definido, en lugar de guardar ambos valores en una sola celda.

Como la división vuelve a ejecutar la extracción, DocBits te pide confirmación antes de ejecutarla: la confirmación aparece en cuanto marcas la casilla y la división solo se aplica después de hacer clic en **Proceder**.

La casilla es la última opción de la sección Ajustes avanzados:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-distinct-split-es-20261112.png" alt="Diálogo Ajustes con la sección Ajustes avanzados: Texto dividido está marcado como última casilla y Columnas de grupo distintas también está marcado."><figcaption><p>Texto dividido es la última casilla de la sección.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-advanced-settings-split-confirm-es-20261112.png" alt="Diálogo de confirmación con la pregunta ¿Está seguro? La tabla será extraída nuevamente y los botones Cancelar y Proceder."><figcaption><p>Al marcar Texto dividido aparece esta confirmación; solo Proceder aplica la división.</p></figcaption></figure>

### Resumen

Utiliza los _Ajustes avanzados_ para enseñar a DocBits a manejar con precisión estructuras de tabla más complejas o inconsistentes. Estos ajustes mejoran la precisión de la extracción al tener en cuenta:

* Encabezados de varias líneas
* Descripciones de varias filas
* Elementos de línea agrupados
* Orden inverso de datos agrupados
* Texto que debe dividirse en un separador de columna

Activar estas opciones durante la formación garantiza que DocBits recuerde el diseño correcto para futuros documentos del mismo proveedor. Cuando la extracción sea correcta, guarda la configuración con la acción **Guardar reglas** descrita en [Guardar y Eliminar Reglas](save-and-delete-rules.md).
