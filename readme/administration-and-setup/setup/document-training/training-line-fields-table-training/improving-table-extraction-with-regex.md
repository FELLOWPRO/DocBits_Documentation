# Estructuración y Mejora de la Extracción de Tablas en DocBits

Una vez que se extrae una tabla y se completa el mapeo inicial de columnas, puedes mejorar la calidad y estructura de los datos utilizando varias herramientas integradas. Esta guía te lleva a través de:

* Agrupación de filas
* Selección manual de filas
* Mapeo de columnas
* Refinamiento de encabezados usando regex

Estas herramientas son especialmente útiles al tratar con diseños de documentos complejos o inconsistentes.

## 1. Agrupación de Filas

Documentos como facturas o confirmaciones de pedidos a menudo contienen entradas de tabla donde una columna (por ejemplo, una descripción) abarca varias líneas, mientras que otras columnas (por ejemplo, cantidad o precio) solo utilizan una línea.

Toma este ejemplo de factura en alemán: la columna "Bezeichnung" (descripción) abarca varias filas:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-multiline-doc-es-20261009.png" alt="Tabla de una factura alemana en la que la descripción (Bezeichnung) de cada artículo ocupa varias líneas."><figcaption><p>Una columna de descripción que abarca varias filas.</p></figcaption></figure>

Inicialmente, DocBits extrae cada fila por separado:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-initial-extraction-es-20261009.png" alt="Tabla extraída en la vista Extracción De Tabla, donde cada línea de texto de la descripción se ha convertido en una fila propia."><figcaption><p>DocBits extrae primero cada fila por separado.</p></figcaption></figure>

Luego puedes **agrupar filas basadas en una columna**, como "Posición". Esto fusiona líneas relacionadas en una entrada única y estructurada:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-grouped-result-es-20261009.png" alt="Tabla extraída en la que las líneas de descripción agrupadas por Posición forman una sola entrada por posición."><figcaption><p>Tras agrupar por Posición, las líneas relacionadas forman una sola entrada.</p></figcaption></figure>

Cuántas sublíneas se combinan en una entrada y cómo se comporta la agrupación se configura en la [Configuración Avanzada](advanced-settings.md), en **Mínimo de filas agrupadas** y **Agrupamiento Inverso**.

## 2. Selección Manual de Filas

En algunos casos, el texto en un documento se extiende a través de varias columnas en una sola fila, lo que dificulta la asignación automática.

Aquí tienes un ejemplo donde la línea "PRAEF" se superpone a **Bezeichnung**, **Menge**, **ME** y **Preis in EUR**:

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-row-misalignment-es-20261009.png" alt="Tabla de una factura con una línea PRAEF cuyo texto se extiende por varias columnas."><figcaption><p>Una línea PRAEF que no coincide con la estructura de columnas.</p></figcaption></figure>

### Cómo Asignar Valores Manualmente:

1.  **Activar el Modo Formación**

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-training-mode-es-20261009.png" alt="Pantalla de Extracción De Tabla con el Modo Formación activado."><figcaption><p>Modo Formación activado.</p></figcaption></figure>


2.  **Activar el Modo de Edición de Filas**

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-row-edit-mode-es-20261009.png" alt="Pantalla de Extracción De Tabla con el Modo de edición de datos de fila activado y su texto de ayuda visible."><figcaption><p>Modo de edición de datos de fila activado.</p></figcaption></figure>

3.  **Seleccionar y Mapear Texto** Haz clic en la pieza de texto correcta y asígnala a un encabezado de columna **azul**.

    <figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-editable-columns-es-20261009.png" alt="Tabla extraída en el modo de edición de filas con los encabezados de columna azules, aún sin rellenar, que se pueden asignar manualmente."><figcaption><p>Los encabezados de columna azules se pueden rellenar manualmente.</p></figcaption></figure>

> Nota: Las columnas de color violeta ya están mapeadas por el sistema y no pueden editarse manualmente.

Este procedimiento pertenece al **modo de corrección**, en el que corriges valores manualmente. Qué puedes hacer allí y cuándo usarlo en lugar del **Modo Formación** se describe en [Entrenamiento de Campos de Línea / Tabla de Entrenamiento](README.md).

## 3. Mapeo de Columnas

El mapeo de columnas vincula tus datos extraídos con los encabezados de columna esperados, asegurando consistencia y exportabilidad.

Para mapear o remapear una columna:

1. Haz clic en el encabezado de columna en la vista de extracción.
2. Elige la columna de destino correcta en el menú desplegable.

<figure><img src="../../../../.gitbook/assets/a-training-line-fields-table-training-improving-table-extraction-with-regex-mapping-dropdown-es-20261009.png" alt="Tabla extraída con el menú desplegable del encabezado de columna abierto, mostrando las columnas de destino Descripción, Número De Artículo, Importe Neto, Posición, Cantidad, Importe Total Factura, Unidad y Precio Unitario."><figcaption><p>Elige la columna de destino en el menú desplegable del encabezado.</p></figcaption></figure>

Puedes ajustar el mapeo tantas veces como sea necesario.

Más información sobre cómo se crean tablas y columnas en general en [Definición de Tablas y Columnas](defining-tables-and-columns.md).

## 4. Extraer de Arriba / Abajo

Algunos documentos están estructurados de manera que los valores de tabla relevantes no aparecen en la misma fila que otros datos. En estos casos, DocBits te permite controlar **de dónde se deben extraer los datos**:

* **Extraer de Arriba**: Úsalo cuando el valor para la fila actual aparece **en la línea superior**.
* **Extraer de Abajo**: Úsalo cuando el valor aparece **en la línea debajo** de la fila actual.

**Dónde Encontrarlo**

1. Ingresa al **Modo Formación**.
2. Haz clic en los tres puntos (⋯) en un encabezado de columna.
3. Bajo la opción **"Extraer de"**, elige `Arriba` o `Abajo` dependiendo del diseño del documento.

## 5. Formato de Monto

Algunas columnas, como **Cantidad** o **Precio Unitario**, contienen valores numéricos o de fecha que pueden seguir diferentes convenciones de formato dependiendo del origen o la configuración regional del documento. DocBits te permite especificar el formato que estos valores deben seguir para garantizar una extracción e interpretación precisas.

**Opciones de Formato de Monto:**

* Define el formato numérico o de fecha esperado para la columna, como EE. UU. (MM/DD/AAAA, decimal con punto), Polonia (DD.MM.AAAA, decimal con coma), Alemania y otros.
* Esto ayuda a DocBits a analizar y estandarizar correctamente los valores incluso si el documento utiliza un formato regional diferente.

**Dónde Encontrarlo**

1. Ingresa al **Modo Formación**.
2. Haz clic en los tres puntos (⋯) en el encabezado de una columna compatible (por ejemplo, Cantidad, Precio Unitario).
3. Bajo la opción **Formato de Monto**, selecciona el formato deseado que coincida con la configuración regional de tu documento.

## 6. Mejorando la Extracción de Tablas con Regex

## **Qué Hace**

Esta función te permite definir una expresión regular (regex) para cada encabezado de tabla, mejorando la precisión de la extracción y garantizando resultados correctos.

## **Cómo Usarlo**

1. Abre un documento del proveedor para el cual deseas definir un regex.
2.  Navega a la vista de **Extracción De Tabla**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Habilita el **Modo Formación**.
4.  Selecciona el encabezado de tabla que deseas refinar, luego elige **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Aparecerá un popup donde puedes ingresar y definir tu regex.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Haz clic en **Validar** para verificar el regex, luego en **Guardar Cambios** para aplicarlo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Guarda la regla y confirma** para aplicar los cambios.

Cómo guardar o volver a eliminar tus reglas entrenadas de forma permanente se describe en [Guardar y Eliminar Reglas](save-and-delete-rules.md).

## Cuándo Usar Cada Función

Utiliza estas herramientas para aumentar la precisión de la extracción y reducir el trabajo manual:

* **Agrupación**: Cuando una descripción o cualquier columna abarca varias filas y necesita combinarse para mayor claridad.
* **Selección Manual de Filas**: Cuando las filas no están estructuradas de manera limpia y partes del contenido caen en las columnas incorrectas.
* **Mapeo de Columnas**: Cuando los nombres de columna detectados automáticamente no coinciden con tu estructura o necesitan refinamiento.
* **Reglas de Regex**: Cuando los encabezados de tabla varían ligeramente entre documentos del mismo proveedor o el OCR introduce inconsistencias.

Guías relacionadas en esta área:

* [Configuración Avanzada](advanced-settings.md) – agrupación, filas de encabezado y tratamiento de filas adicionales.
* [Definición de Tablas y Columnas](defining-tables-and-columns.md) – crear tablas y columnas.
* [Guardar y Eliminar Reglas](save-and-delete-rules.md) – conservar o descartar de forma permanente el diseño entrenado.
