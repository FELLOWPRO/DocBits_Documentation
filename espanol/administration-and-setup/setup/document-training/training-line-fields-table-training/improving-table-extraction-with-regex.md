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

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FVino2M4Esor3IRHGqBd5Brx7_lKPIwEOlRYBHzMXw4WoacFNW39hbWuwoUNGocubx4Bh9_BvUBqZSWA4U_NmU8FBw4Q1_AiTASgMx-2MLKvsHLJY057oqyks0fQ5b7mI577JTX5rBKdEG90O9F5TcoU\&width=768\&dpr=4\&quality=100\&sign=ae0bd75a\&sv=2)

Inicialmente, DocBits extrae cada fila por separado:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FUX5OdkW59HPVROnNzSeZbDw4NYTPbfayDLIXBQi0pwHzUEJ1B5t7I9uKBNc0dmOB3Cile8Xv6AdgVXuUd0aMbQFGWagBCEetw8P-N4zgG_cGTjWHhpDtGQZg27UZKdCDJ5FeEDJgFAYtTB8kZrMSdho\&width=768\&dpr=4\&quality=100\&sign=b6990876\&sv=2)

Luego puedes **agrupar filas basadas en una columna**, como "Posición". Esto fusiona líneas relacionadas en una entrada única y estructurada:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FPxA6h2udUuYd1YmHV97t-bzfZzipFpdA5t8gjpGXWx9sA-I4tW3tYwD28icv88UEmitz0EAaWuGkU5ZwqAjcQnoOkmg9u1AcBJW3nITU6eFa0foHB-AQPb0qv0AWaaEwM6WvwaEcAODEUzKtvRZOMN0\&width=768\&dpr=4\&quality=100\&sign=36b99bc7\&sv=2)

## 2. Selección Manual de Filas

En algunos casos, el texto en un documento se extiende a través de varias columnas en una sola fila, lo que dificulta la asignación automática.

Aquí tienes un ejemplo donde la línea "PRAEF" se superpone a **Bezeichnung**, **Menge**, **ME** y **Preis in EUR**:

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FLbVbmfdOBpeCWDftPvW0qjEHjbLmWYRrAGTZHVW8VEHQTEvl5GoqH2wkFE5iUOySmF50b1V8CDAZhfMzPTeMQscmc61SDKaqSCW-y0Z7fjlwOjhtjxWD44oCsgHmwrgrBD4cuEGgn9JY_UX3t9jRlPs\&width=768\&dpr=4\&quality=100\&sign=5ff4a2e1\&sv=2)

### Cómo Asignar Valores Manualmente:

1.  **Activar el Modo de Entrenamiento**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F4D8iCXk0p_Mur8bX_11ne_2iA-GOxoFi2OQWlSEvrH1auoE0ksnYXpZx3Pw3PUJJRZJN85dnQlSSBB369FfafXAy8adjFZcnepQnODSaaIj69cxtUKFAXPgn5eyPE6jbJuzStJALMgumlt49Z1Pv3FY\&width=768\&dpr=4\&quality=100\&sign=232c58a9\&sv=2)


2.  **Activar el Modo de Edición de Filas**

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2F8YQmo_WRuKKVjk1a_eoxSBiQr0GncuS4BmCA0aI9aOlrbsIvdj8dZlurxxBHp2lH4ozT4HPWw9qYDW7xLQ7u2DSyU8DrNzSBC7LjzKLTDJ2tudY9a_DENDoK5Aya6L1hcf1WF1RD92S_DzhGVV4Gh6Q\&width=768\&dpr=4\&quality=100\&sign=8fc5c089\&sv=2)

    modo de edición de filas
3.  **Seleccionar y Mapear Texto** Haz clic en la pieza de texto correcta y asígnala a un encabezado de columna **azul**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2Fi2tlbwl9qFE0clthaoRPe7kcPRiURCvemuLEjBK4uAnfsR4auXbftMfEY1ZW5WXwezTBVSG5hbNRkddwIeLtrgJUvZoeKGdPKN8f75O_dPdIWkm4EFALfAj-evDUI3UKrgNOTNjF37C1bBLtE95OA1w\&width=768\&dpr=4\&quality=100\&sign=842a42\&sv=2)

> Nota: Las columnas de color violeta ya están mapeadas por el sistema y no pueden editarse manualmente.

## 3. Mapeo de Columnas

El mapeo de columnas vincula tus datos extraídos con los encabezados de columna esperados, asegurando consistencia y exportabilidad.

Para mapear o remapear una columna:

1. Haz clic en el encabezado de columna en la vista de extracción.
2. Elige la columna de destino correcta en el menú desplegable.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FX_65pCWrI4HMFr_aiA0eoSDp-yIYy49lULzAZaiIgnr0aIowlLSed21MuehkGLs4UIdQousdfhiZi5pnQtpZ0uUn6dxlzii7WPQvov-kN1_Jimsi6U6zowOLxjBzZzZ47kaRhduAVBd_Ya9QQtXTpJ4\&width=768\&dpr=4\&quality=100\&sign=4e2a3bdc\&sv=2)

Puedes ajustar el mapeo tantas veces como sea necesario.

## 4. Extraer de Arriba / Abajo

Algunos documentos están estructurados de manera que los valores de tabla relevantes no aparecen en la misma fila que otros datos. En estos casos, DocBits te permite controlar **de dónde se debe extraer los datos**:

* **Extraer de Arriba**: Úsalo cuando el valor para la fila actual aparece **en la línea superior**.
* **Extraer de Abajo**: Úsalo cuando el valor aparece **en la línea debajo** de la fila actual.

**Dónde Encontrarlo**

1. Ingresa al **Modo de Entrenamiento**.
2. Haz clic en los tres puntos (⋯) en un encabezado de columna.
3. Bajo la opción **"Extraer de"**, elige `Arriba` o `Abajo` dependiendo del diseño del documento.

## 5. Formato de Monto

Algunas columnas, como **Cantidad** o **Precio Unitario**, contienen valores numéricos o de fecha que pueden seguir diferentes convenciones de formato dependiendo del origen o la ubicación del documento. DocBits te permite especificar el formato que estos valores deben seguir para garantizar una extracción e interpretación precisas.

**Opciones de Formato de Monto:**

* Define el formato numérico o de fecha esperado para la columna, como EE. UU. (MM/DD/AAAA, decimal con punto), Polonia (DD.MM.AAAA, decimal con coma), Alemania y otros.
* Esto ayuda a DocBits a analizar y estandarizar correctamente los valores incluso si el documento utiliza un formato regional diferente.

**Dónde Encontrarlo**

1. Ingresa al **Modo de Entrenamiento**.
2. Haz clic en los tres puntos (⋯) en el encabezado de una columna compatible (por ejemplo, Cantidad, Precio Unitario).
3. Bajo la opción **Formato de Monto**, selecciona el formato deseado que coincida con la ubicación de tu documento.

## 6. Mejorando la Extracción de Tablas con Regex

## **Qué Hace**

Esta función te permite definir una expresión regular (regex) para cada encabezado de tabla, mejorando la precisión de la extracción y garantizando resultados correctos.

## **Cómo Usarlo**

1. Abre un documento del proveedor para el cual deseas definir un regex.
2.  Navega a la vista de **Extracción de Tabla**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FDdlNrO6hG6jnEeWU9DuZ%252Fimage.png%3Falt%3Dmedia%26token%3Dca11a537-27a4-4b00-b3e7-f77540c28c2b\&width=768\&dpr=4\&quality=100\&sign=fd47355a\&sv=2)
3. Habilita el **Modo de Entrenamiento**.
4.  Selecciona el encabezado de tabla que deseas refinar, luego elige **Regex**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fes6PsB9sHHXp0CNRj6YF%252Fimage.png%3Falt%3Dmedia%26token%3D6e31e4db-fd2f-487c-ac19-f1d6add81ad1\&width=768\&dpr=4\&quality=100\&sign=32264560\&sv=2)
5.  Aparecerá un popup donde puedes ingresar y definir tu regex.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FWB7hjuuyVVAewRqrnhYj%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135020.jpg%3Falt%3Dmedia%26token%3D6a31253d-18d7-4d8f-a00e-acd89a744127\&width=768\&dpr=4\&quality=100\&sign=d8d2d94a\&sv=2)
6.  Haz clic en **Validar** para verificar el regex, luego en **Guardar Cambios** para aplicarlo.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FC4R2o2W10ct1o0oesTLZ%252FiScreen%2520Shoter%2520-%2520Google%2520Chrome%2520-%2520250303135153.jpg%3Falt%3Dmedia%26token%3D43e53a05-53fe-4503-ba51-55c85910bd82\&width=768\&dpr=4\&quality=100\&sign=9ec6eb7b\&sv=2)
7. **Guarda la regla y confirma** para aplicar los cambios.

## Cuándo Usar Cada Función

Utiliza estas herramientas para aumentar la precisión de la extracción y reducir el trabajo manual:

* **Agrupación**: Cuando una descripción o cualquier columna abarca varias filas y necesita combinarse para mayor claridad.
* **Selección Manual de Filas**: Cuando las filas no están estructuradas de manera limpia y partes del contenido caen en las columnas incorrectas.
* **Mapeo de Columnas**: Cuando los nombres de columna detectados automáticamente no coinciden con tu estructura o necesitan refinamiento.
* **Reglas de Regex**: Cuando los encabezados de tabla varían ligeramente entre documentos del mismo proveedor o el OCR introduce inconsistencias.
