# Solución de problemas de extracción de tablas

## **Paso 1: Abrir la vista OCR para resultados de extracción deficientes**

Si los resultados del entrenamiento de extracción de tablas no son buenos:

1. Abre la **vista OCR** haciendo clic en el icono de la lupa con **OCR** escrito en él.
2. Revisa los resultados de la extracción y verifica si el proceso OCR puede mejorar la captura de datos.
3. Si los resultados siguen siendo malos, prueba con un documento diferente para verificar si el problema es específico del documento.
4. Si el problema es específico del documento, utiliza otro documento para la extracción.
   * Si el problema persiste, sigue los siguientes pasos.

## **Paso 2: Verificar la disponibilidad de E-Text**

1. Verifica si el documento tiene **e-text** disponible.
   * Puedes verificar esto utilizando una herramienta como **Adobe Acrobat**.
   * Si el documento contiene e-text, sigue el **Paso 3**.
   * Si el documento no contiene e-text, sigue el **Paso 4**.

## **Paso 3: Activar la extracción de E-Text**

Si el documento contiene e-text, tienes dos opciones:

1. **Activar la extracción de e-text solo para este proveedor**:
   * Regresa a la **Validación de Campos de Documentos**.
   * Haz clic en el cuadrado con los tres puntos en la barra de herramientas del lado izquierdo.
   * Aquí, activa la opción **Usar e-text si está disponible** para activarlo solo para este proveedor.
2. **Activar la extracción de e-text para todos los proveedores**:
   * Ve a **Configuración** > **Procesamiento de Documentos** > **Configuración OCR**.
   * En esta sección, encontrarás la opción **Usar e-text si está disponible** y puedes activarla para todos los proveedores.
3. Después de habilitar la extracción de e-text, vuelve a intentar el **entrenamiento de extracción de tablas**.
   * Si los resultados mejoran, el problema está resuelto.
   * Si los resultados siguen siendo malos, procede al **Paso 4**.

## **Paso 4: No hay E-Text disponible - Cambiar la versión de OCR de IA**

Si el documento no tiene e-text disponible:

1. Ve a **Configuración** > **Procesamiento de Documentos** > **Configuración OCR**.
2. Cambia la **Versión de OCR de IA** a una versión diferente.
3. Regresa al **Entrenamiento de Extracción de Tablas** e inténtalo de nuevo.
4. Si el resultado es mejor:
   * Verifica otros documentos de diferentes proveedores para asegurarte de que los resultados de extracción para esos proveedores no se vean afectados por este cambio.
   * **Sé cauteloso, ya que este cambio puede afectar los resultados de extracción de otros proveedores.**
   * Este cambio puede afectar a otros proveedores, así que asegúrate de verificar los resultados minuciosamente para garantizar que no afecte negativamente las extracciones de documentos de otros proveedores.
5. Si el resultado no mejoró después de cambiar la versión de OCR de IA, por favor **contáctanos** para obtener más ayuda.

## Mensajes en la tabla

La extracción puede parecer correcta y, aun así, el documento se niega a aprobarse. Estos son los mensajes que DocBits muestra en la tabla de líneas de detalle o debajo de ella, qué los provoca y cómo resolverlos.

| Mensaje | Causa | Solución |
|---|---|---|
| **Columna obligatoria vacía** (celda marcada en rojo, nombre de la columna en el tooltip) | Una columna marcada como *Obligatoria* (*Is Required*) en la configuración de columnas de tabla no tiene valor en esta fila. | Rellena la celda. Si el valor nunca existe para este tipo de documento, un administrador desmarca *Obligatoria* en Configuración → Tipos de documentos → Columnas de tabla y tú reinicias el documento. |
| **Line total does not match quantity x unit price (expected …, got …)** | DocBits comprueba cada fila: `TOTAL_AMOUNT = QUANTITY × UNIT_PRICE + CHARGES`, menos `DISCOUNT`, o × (100 − `DISCOUNT_PERCENT`) / 100, o menos `DISCOUNT_PER_UNIT × QUANTITY`, según la columna de descuento que esté rellena. Una diferencia superior a 0,02 provoca el mensaje. La comprobación solo se ejecuta cuando cantidad, precio unitario y total están rellenos. | Compara los cuatro valores con el documento. Normalmente uno de ellos se leyó en la columna equivocada; un valor de cargos o de descuento en la celda incorrecta es el caso más habitual. Corrige la celda; el mensaje desaparece al guardar. |
| **Line total does not match quantity x unit price minus discount / minus percentage discount / minus per-unit discount** | La misma comprobación, con la columna de descuento que está rellena. | Igual que arriba; revisa primero la celda del descuento. |
| **Line items add up to … but the net total is …** (advertencia) | La suma de todas las celdas `TOTAL_AMOUNT` difiere del importe neto de la cabecera. | Busca una fila que falte, una fila duplicada o un importe neto de cabecera mal leído. Una advertencia no bloquea la aprobación. |
| **Total does not add up: expected …, got …** (cabecera) | Neto + impuesto (+ envío en los diseños de EE. UU.) difiere del total de la cabecera. | Comprobación de cabecera, no un problema de la tabla: corrige los importes de la cabecera. |
| **Line Item Table is missing Mandatory column for PO like (Item Number, Unit Price, Quantity and Total amount)** | La coincidencia de PO necesita esas cuatro columnas predeterminadas y una de ellas está oculta o se sustituyó por una columna personalizada. | Administrador: vuelve a mostrar la columna predeterminada en Columnas de tabla, o asigna el valor a ella en el entrenamiento de tablas. |
| **Table is already extracted by AI. Do you want to train manually?** | Abriste el entrenamiento de tablas para un proveedor cuya tabla procede de la IA. | Confirma para entrenar; las reglas guardadas sustituyen entonces a la tabla AI para este proveedor. Cancela para conservar la tabla AI. |
| **AI Table will display here. Enable in …** | La extracción de tablas por IA está desactivada para la organización. | Administrador: Configuración → Procesamiento de documentos → Clasificación y extracción → *Extracción de tablas por IA*. |
| **No line items yet** | No se extrajo nada: no hay reglas para este proveedor y la IA no encontró ninguna tabla, o el documento no tiene texto legible. | Sigue los Pasos 1 a 4 anteriores (vista OCR, E-Text). Después entrena la tabla una vez, o añade filas manualmente con *Agregar nueva fila de tabla*. |

### La IA rellena una y otra vez una columna con el valor equivocado

Ejemplo visto en la práctica: la IA escribe el total de la línea en `CHARGES`. Entonces todas las filas fallan la comprobación del total de línea, porque los cargos se suman a cantidad × precio unitario.

1. Si el proveedor tiene reglas guardadas, desmarca *Usar IA* en esa columna (Configuración → Tipos de documentos → Columnas de tabla) para que la rellenen las reglas.
2. Si el proveedor no tiene reglas, entrena la tabla una vez para que la columna quede vinculada a su posición en la página, u oculta la columna si el proveedor nunca imprime ese valor.
3. Añade una [etiqueta de la tabla AI](../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) como *"la columna de cargos está vacía en este proveedor"*; las etiquetas se guardan por proveedor.

### Desactivar las comprobaciones de tabla

Configuración → Tipos de documentos → *tu tipo* → Más ajustes → **Omitir validación de tabla** (*Skip table validation*) marca como válida la tabla de todos los documentos de ese tipo: las discrepancias del total de línea y las columnas obligatorias vacías dejan de notificarse. Las comprobaciones de cabecera (total = neto + impuesto) se mantienen. Úsalo solo para tipos de documento cuyas tablas son informativas y no se exportan al ERP.
