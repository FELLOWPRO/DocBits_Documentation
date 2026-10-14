# el valor debe ser numérico.

## **Paso 1: Investigar la Orden de Compra**

**1. Verificar la Orden de Compra desde el Tablero**

* Si el estado del documento es **Error de Exportación**:
  1. Localiza el documento en el tablero.
  2. Haz clic en él y luego selecciona el botón de **Validación de Campos** para volver a la pantalla de validación de campos.
* Si el estado del documento es **Listo para Validación**:
  1. Haz clic en el documento para proceder directamente a la pantalla de **Validación de Campos**.
* Si el documento está en estado de **Aprobación Pendiente**:
  1. Navega a la **Pantalla de Aprobación**.
  2. Junto a los **Ítems de Línea de Factura**, localiza la **Tabla de Orden de Compra**.
  3. Ve al paso 3. Verifica el Número de Entrega.

**2. Verificar la Orden de Compra**

1. En la pantalla de **Validación de Campos**, asegúrate de que se haya seleccionado la Orden de Compra correcta.
2. Una vez confirmada la Orden de Compra correcta, haz clic en la Orden de Compra junto a la tabla extraída, para abrir la vista de **Tabla de Orden de Compra**.

**3. Verifica el Número de Entrega**

* En la Tabla de Orden de Compra, busca la columna de **Número de Entrega**:
  * **Si hay un Número de Entrega presente**, procede a la **Pantalla de Aprobación** y verifica nuevamente si está presente, cuando esté presente ve al **Paso 3**.
  * **Si no hay un Número de Entrega presente**, sigue el **Paso 2** para abordar este problema.

## Paso 2: Verificar la Orden de Compra en LN

Antes de enviar la Orden de Compra a DocBits, verifica que el **Número de Entrega** esté asignado correctamente en **LN**. Verifica los detalles de la **Orden de Compra** en **LN** para asegurarte de que esté completa y precisa. Si el **Número de Entrega** falta o es incorrecto, esto podría ser la causa del error de exportación.

Si la **Orden de Compra** parece correcta y contiene los detalles necesarios, puedes proceder al siguiente paso.

## **Paso 3: Abrir la Configuración de DocBits**

1. Abre **DocBits** y ve a la sección de **Configuración**.
2. Navega a **Procesamiento de Documentos**.
3. Selecciona **Exportar**.
4. En la sección de **Exportar**, haz clic en el ícono de **tres puntos** junto a la exportación que no está funcionando y selecciona **Editar**.
5. En el menú de **Editar Configuración de Exportación**, haz clic en **Descargar el archivo de Mapeo de LN**.

## **Paso 3: Editar el Archivo de Mapeo de LN**

1. Abre el archivo descargado de **Mapeo de LN**.
2. Busca el campo **IRF\_ReceiptLine**.
   * Si el campo **IRF\_ReceiptLine** está presente y configurado como **nada** (vacío), actualízalo a **TF\_delivery\_line**.
   * Si el campo **IRF\_ReceiptLine** **no está presente**, agrégalo al archivo y configura su valor como **TF\_delivery\_line**.
3. Para el campo **Campos de Recepción de Factura**, agrega **ReceiptLine** a los valores.

Debería lucir como sigue:

<figure><img src="../../../../.gitbook/assets/docbits_settings_workflow_2.png" alt="DocBits Configuración Flujo de trabajo 2" width="563"><figcaption></figcaption></figure>

## **Paso 4: Agregar el Archivo Actualizado de Vuelta a DocBits**

1. Regresa a la sección de **Exportar** en DocBits donde descargaste previamente el archivo de **Mapeo de LN**.
2. Sube el archivo de **Mapeo de LN** editado con las nuevas actualizaciones.

## Paso 5: Reintentar la Exportación

Después de confirmar que la **Orden de Compra** tiene un **Número de Entrega** y asegurarte de que el **archivo de Exportación es correcto**, sigue estos pasos para reintentar la exportación:

1. **Volver al Tablero:**
   * Regresa al tablero y encuentra el documento con el error de exportación.
2. **Reintentar el Proceso de Exportación:**
   * Haz clic en el documento con el error de exportación.
   * Si la **Orden de Compra** tiene un **Número de Entrega** válido y el **archivo de Exportación** es correcto, procede a reintentar la exportación.
3. **Verificar el Resultado de la Exportación:**
   * Después de reintentar, verifica nuevamente el proceso de exportación para ver si el problema se ha resuelto y el documento ya no muestra un error de exportación.
   * Si la exportación es exitosa, el problema debería estar resuelto.
4. **Investigación Adicional (si el problema persiste):**
   * Si el problema persiste después de reintentar la exportación, contacta al soporte para una investigación adicional sobre posibles problemas de configuración o del sistema.
