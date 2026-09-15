# Tabla AI

La Tabla Extraída por IA es la tabla de líneas de detalle que DocBits lee con IA cuando un proveedor no tiene reglas de tabla entrenadas. Aparece en la pantalla de validación, debajo de los campos de cabecera. Esta página explica cuándo la obtienes, cómo volver a ejecutarla y cómo influir en lo que extrae.

## Cuándo obtienes la tabla AI

* Un administrador ha activado la **Extracción de tablas por IA** (Configuración → Procesamiento de documentos → Clasificación y extracción). Si está desactivada, el área de la tabla muestra *AI Table will display here. Enable in …*.
* El proveedor **no tiene reglas guardadas**. En cuanto alguien entrena la tabla del proveedor y hace clic en *Guardar reglas*, las reglas guardadas sustituyen a la tabla AI para ese proveedor; las filas aparecen entonces en la pestaña *Tabla extraída* en lugar de en la pestaña *Tabla extraída por IA*.
* Excepción: las columnas marcadas como **Usar IA** en la configuración de columnas de tabla las rellena la IA incluso en proveedores con reglas guardadas; consulta [Usar IA por columna](#usar-ia-por-columna).

El nivel de IA que lee la tabla (Fast, Full, Nexus) se establece por organización y se puede sobrescribir por proveedor en *Más ajustes* de la pantalla de validación; consulta [Modelo de IA específico del proveedor](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## Volver a extraer la tabla AI

Úsalo cuando falten filas o una columna esté desplazada y quieras que la IA lo intente de nuevo, por ejemplo después de añadir una [etiqueta](ai-table-tags.md):

1. Añade o cambia [etiquetas](ai-table-tags.md) en el campo debajo de la tabla y haz clic en **Aplicar**. La IA reconstruye la tabla de este documento con tus etiquetas y cambios de columnas; todavía no se guarda nada para el proveedor. Si el documento tiene líneas coincidentes con una PO, DocBits avisa de que la reconstrucción elimina las coincidencias.
2. ¿Satisfecho con el resultado? Haz clic en **Guardar** (*Guardar reglas*) para que el siguiente documento de este proveedor se extraiga de la misma manera.
3. Para empezar de cero, haz clic en **Eliminar** (*Eliminar reglas*): DocBits confirma *Rules has been deleted successfully* y vuelve a ejecutar la extracción por IA sin etiquetas ni formato guardados.

*Eliminar reglas* elimina las etiquetas y las reglas de formato guardadas para este proveedor, no la configuración de columnas de tabla. Para volver a extraer todo el documento (cabecera y tabla) después de que un administrador cambie ajustes o columnas, usa *Reiniciar* en el menú del documento del panel.

## Usar IA por columna

Cada columna de tabla tiene un indicador **Usar IA** (Configuración → Configuración global → Tipos de documentos → [Columnas de tabla](../../../administration-and-setup/settings/global-settings/document-types/table-columns.md)). Con el indicador activado, la IA rellena esa columna aunque el proveedor tenga reglas guardadas; las demás columnas siguen viniendo de las reglas. Uso típico: una columna de descripción de texto libre que las reglas entrenadas capturan mal, o un valor que cambia de posición en la página.

Ten en cuenta que la IA entonces deduce esa columna a partir de toda la fila. Si pone sistemáticamente el valor equivocado (por ejemplo, el total de línea en *Cargos*), la comprobación del total de línea falla en todas las filas. En ese caso, desactiva *Usar IA* en esa columna o añade una etiqueta que le diga a la IA qué es la columna.

## Extracción estructurada

Con **Usar extracción estructurada (IA)** activado en la configuración de la organización, la IA devuelve la tabla en una estructura fija que se asigna directamente a las columnas de tabla configuradas, en lugar de copiar los encabezados de columna del proveedor. Los nombres de columna coinciden entonces siempre con tu configuración; una columna que el proveedor imprime pero que no has configurado no se extrae. Pide a tu administrador que lo active cuando los encabezados de los proveedores varíen mucho y pierdas tiempo reasignando columnas.

## Trabajar con la tabla extraída

Aquí se presentan las capacidades clave y las instrucciones de uso:

* **Eliminar Columnas**: Si ciertas columnas en la tabla extraída no son necesarias, los usuarios pueden eliminarlas fácilmente haciendo clic en el icono "Eliminar columna" (representado por tres puntos verticales) junto al encabezado de la columna. Esto ayuda a limpiar la tabla y enfocarse solo en la información relevante.

<figure><img src="../../../.gitbook/assets/ai-table1.png" alt=""><figcaption></figcaption></figure>

* **Cambiar Formato de Moneda**: El formato de moneda se puede cambiar seleccionando el formato deseado en el menú desplegable junto al campo "Moneda". Esto asegura que los valores de la moneda se muestren en el formato preferido, facilitando su interpretación y análisis de los datos financieros.

<figure><img src="../../../.gitbook/assets/ai-table2.png" alt=""><figcaption></figcaption></figure>

* **Mostrar/Ocultar Columnas no Mapeadas**: Por defecto, solo las columnas mapeadas (columnas con datos extraídos) son visibles en la tabla. Sin embargo, los usuarios pueden optar por mostrar u ocultar las columnas no mapeadas haciendo clic en el botón "Ocultar columnas no mapeadas" o "Mostrar columnas no mapeadas" en la parte inferior de la tabla. Esta función es útil cuando los usuarios desean revisar todas las columnas disponibles, incluso si actualmente no contienen datos.

<figure><img src="../../../.gitbook/assets/ai-table3.png" alt=""><figcaption></figcaption></figure>

* **Cambiar Encabezados de la Tabla**: Los encabezados de la tabla (nombres de las columnas) se pueden modificar haciendo clic en el encabezado e ingresando el nombre deseado. Esta función permite a los usuarios personalizar los nombres de las columnas para que se ajusten mejor a su terminología o preferencias, haciendo que los datos sean más legibles y comprensibles.

<figure><img src="../../../.gitbook/assets/ai-table4.png" alt=""><figcaption></figcaption></figure>

* **Guardar lo que has cambiado**: **Guardar** junto a las etiquetas (tooltip *Guardar reglas*) almacena la asignación de columnas actual, las columnas ocultas y las etiquetas para este proveedor. El siguiente documento del proveedor se extrae con ellas.

Estas funciones te dan control sobre los datos extraídos. Cuando el mismo proveedor necesita las mismas correcciones cada vez, entrena la tabla una sola vez ([Entrenamiento de Campos de Línea / Tabla de Entrenamiento](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)) y la tabla AI deja de usarse para ese proveedor.
