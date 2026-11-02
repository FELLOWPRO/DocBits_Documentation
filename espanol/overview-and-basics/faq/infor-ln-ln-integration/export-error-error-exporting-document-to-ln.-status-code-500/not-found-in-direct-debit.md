# no encontrado en débito directo

## **Paso 1: Verificar la Configuración de LN**

1. Inicie sesión en **LN CE**.
2. Vaya al menú de **Opciones** y seleccione **Ejecutar Programa**.
3. En el campo de entrada, escriba **Parámetros ACP** y presione Enter para abrir el programa.
4. Haga clic en la flecha junto al campo **Conjunto Actual** para expandir la configuración.
5. Vaya a la sección de **Coincidencias**.
   * **Verificar la Configuración de Coincidencia Automática:**
     * Si la **Coincidencia Automática** está configurada en **Coincidir con el Recibo de Compra**, continúe con el siguiente paso.
     * Si no está configurada en **Coincidir con el Recibo de Compra**, pero aún así obtiene este error, contáctenos.

## **Paso 2: Abrir Configuraciones de DocBits**

Si la **Coincidencia Automática** está configurada en **Coincidir con el Recibo de Compra**, continúe con los siguientes pasos en DocBits:

1. Abra **DocBits** y vaya a la sección de **Configuraciones**.
2. Vaya a **Procesamiento de Documentos**.
3. Seleccione **Exportar**.
4. En la sección de **Exportar**, haga clic en el ícono de **tres puntos** junto a la exportación que no está funcionando y seleccione **Editar**.
5. En el menú de **Editar Configuraciones de Exportación**, haga clic en **Descargar el archivo de Mapeo de LN**.

## **Paso 3: Editar el Archivo de Mapeo de LN**

1. Abra el archivo de **Mapeo de LN** descargado.
2. Busque el campo **IRF\_PackingSlip**.
   * Si el campo **IRF\_PackingSlip** está presente y configurado en **nada** (vacío), actualícelo a **TF\_packing\_slip**.
   * Si el campo **IRF\_PackingSlip** **no está presente**, agréguelo al archivo y configure su valor en **TF\_packing\_slip**.
3. Para el campo **Campos de Recibo de Factura**, agregue **PackingSlip** a los valores.

Debería verse así:

<figure><img src="../../../../.gitbook/assets/docbits_table_invoice_3.png" alt="DocBits Tabla Factura 3"><figcaption></figcaption></figure>

## **Paso 4: Agregar el Archivo Actualizado de Vuelta a DocBits**

1. Regrese a la sección de **Exportar** en DocBits donde descargó previamente el archivo de **Mapeo de LN**.
2. Cargue el archivo de **Mapeo de LN** editado con las nuevas actualizaciones.

## Si aún encuentra el **Error al exportar el documento a LN** con el código de estado **500**, contáctenos
