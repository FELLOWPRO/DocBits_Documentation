# Exportación alternativa

## **Paso 1: Crear una nueva exportación**

1. Vaya a **Configuración** > **Procesamiento de documentos** > **Exportar**.
2. Haga clic en **Create New Export** para definir una nueva configuración de exportación.
3. Guarde la configuración y asegúrese de que la exportación esté **desactivada**.

<figure><img src="../../.gitbook/assets/image (368).png" alt="Lista de ajustes de exportación con las filas Alternate-Export-Invoice-LN-IDM-BOD y Export-Invoice-LN para el tipo de documento Invoice, método de exportación Infor-IoN-Cloud e iconos de acción"><figcaption></figcaption></figure>

### **Paso 2: Activar la exportación alternativa**

1. Vaya a **Configuración** > **Configuración global** > **Tipo de documento** > **Más configuraciones**.
2. Localice el ajuste **Alternate Export** y actívelo.
3. Configure lo siguiente:
   * **Document Status**: especifique el estado de los documentos después de la exportación alternativa.
   * **Export Configuration**: seleccione la configuración de exportación recién creada que se utilizará para la exportación alternativa.

<figure><img src="../../.gitbook/assets/image (369).png" alt="Página More Settings del tipo de documento Invoice que muestra la opción Alternate Export con el estado Pending approval y el Export Configuration Alternate-Export-Invoice-LN-IDM-BOD-8203"><figcaption></figcaption></figure>

## Uso de la exportación alternativa

**En la pantalla de PO-Matching**

* Después de activar la exportación alternativa, tendrá la opción de seleccionarla directamente en la pantalla de **PO-Matching**.

<figure><img src="../../.gitbook/assets/image (370).png" alt="Pantalla de PO Matching con la búsqueda del número de pedido 100000300, los botones CONFIRM &amp;amp; EXPORT y Reject y el panel Document Alternate Export"><figcaption></figcaption></figure>

**Con la tarjeta de flujo de trabajo**

* La tarjeta de flujo de trabajo **Alternate Export** también se puede utilizar para automatizar este proceso. Configure la tarjeta según sea necesario para aplicar la lógica de exportación alternativa a su flujo de trabajo.
