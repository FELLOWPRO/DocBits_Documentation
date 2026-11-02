# Entrenamiento de campos de línea y tablas

## Entrenamiento de tablas: cuándo y cómo utilizarlo

DocBits utiliza la extracción de tablas basada en AI de forma predeterminada, que funciona con todos los proveedores. Sin embargo, cuando necesite más control sobre cómo se extraen las líneas de pedido para un proveedor específico, puede usar **entrenamiento de tablas** para definir la estructura manualmente.

#### &#x20;**Importante: entrenamiento específico del proveedor**

El entrenamiento de tablas es **específica de cada proveedor**. Si entrena un diseño de tabla para un proveedor, las reglas se aplican solo a los documentos de ese proveedor.\
Otros proveedores seguirán utilizando la extracción de tablas basada en AI a menos que reciban capacitación por separado.

#### ¿Cuándo debe utilizar el entrenamiento de tablas?

Utilice entrenamiento de tablas **solo cuando el diseño del documento sea estable** y desee garantizar una extracción consistente y de alta calidad. Es más adecuado para proveedores que:

* Utilice un formato de factura **fijo** a lo largo del tiempo.
* Requerir **asignación precisa** de líneas de detalle a campos específicos.
* Son **proveedores de gran volumen**, donde la automatización constante es valiosa.

#### Cuándo no utilizar el entrenamiento de tablas

Evite utilizar entrenamiento de tablas si:

* El proveedor **cambia con frecuencia el diseño de su factura** (por ejemplo, cada dos meses).
* No recibe regularmente documentos de ese proveedor.
* La extracción predeterminada AI funciona **bastante bien** sin entrenamiento manual.

En tales casos, volver a entrenar la tabla repetidamente sería ineficaz y llevaría mucho tiempo.



## Cómo utilizarlo:

**Modo de entrenamiento** se utiliza para enseñar a DocBits cómo extraer correctamente líneas de detalle del diseño de documento de un proveedor específico.

Cuando estás en el modo de entrenamiento, defines:

* **Dónde está ubicada la tabla** en el documento.
* **Qué áreas corresponden a cada columna** (p. ej., Cantidad, Descripción, Precio unitario).

Este modo crea una **plantilla de extracción reutilizable** para ese proveedor, por lo que los documentos futuros con el mismo diseño se procesarán automáticamente, sin necesidad de volver a entrenar el modelo.

**Key Characteristics:**

* **Las columnas asignadas son de solo lectura**: no puedes cambiar el texto manualmente.
* Usted **no puede agregar ni eliminar filas**.
* La atención se centra en **mapear posiciones**, no en corregir valores.
* Una vez que haya terminado de mapear la tabla y sus columnas, haga clic en **“Save Rules”** para que DocBits aprenda y aplique este entrenamiento a documentos similares del mismo proveedor.



**Modo de corrección** le permite **corregir errores de extracción** en los datos de la tabla del documento actual. Se utiliza cuando DocBits ya ha intentado extraer la tabla, pero los resultados necesitan pequeñas correcciones.

Utilice el modo de corrección cuando:

* Algunos valores de **faltan o están desalineados**.
* Se extrajo una **línea vacía o duplicada** y es necesario eliminarla.

**Qué puedes hacer en el modo de corrección:**

* **Ajustar manualmente los valores** en las columnas asignadas (por ejemplo, corregir ubicaciones extraviadas).
* **Eliminar filas** que no deberían formar parte de la tabla.
* **Agregue filas** que se omitieron por completo durante la extracción.
