---
hidden: true
noIndex: true
---

# M3\_OLD

## Importar una plantilla de conexión API en Infor M3

Esta guía explica cómo importar una plantilla de conexión API para configurar rápidamente los ajustes clave de la integración con Infor M3. El uso de una plantilla permite establecer una configuración de conexión predefinida, lo que simplifica el proceso y garantiza la coherencia.

<mark style="color:red;">**Nota**</mark>: Para la configuración detallada de áreas específicas como Auto Accounting, la integración de proveedores, las órdenes de compra o la extracción de tablas para elementos de costes, consulte la documentación correspondiente:

* [Auto Accounting](m3/auto-accounting.md)
* [Proveedores y Orden de Compra](m3/suppliers-and-purchase-orders.md)
* [Cómo importar todos los proveedores](m3/how-to-import-all-suppliers.md)
* [Extracción de tabla para elemento de costeo](m3/table-extraction-for-costing-element.md)

### **Descargar la plantilla**

Antes de importar, descargue la plantilla de conexión necesaria con el siguiente archivo:

{% file src="../../.gitbook/assets/DocBits-Dev-Import-Template (1).xml" %}

### Importar la plantilla

#### Pasos para importar una plantilla de conexión

1. **Acceda a Infor ION Desk:**
   *   Navegue a **InforOS** → **ION Desk** → **Conectar** → **Puntos de conexión**.

       ![Menú de navegación de Infor ION Desk con las entradas Home, Data Flows, API Flows y Mappings](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o)
2. **Importe la plantilla:**
   *   Haga clic en el botón **Import**.

       <figure><img src="../../.gitbook/assets/m3_import_2.png" alt="Página Connect de Infor ION Desk que muestra la vista Connection Points con su búsqueda y barra de herramientas"><figcaption></figcaption></figure>
   * Seleccione el **archivo de plantilla** adecuado de su sistema local.
   *   Haga clic en **OK** para iniciar el proceso de importación.

       <figure><img src="../../.gitbook/assets/m3_import_3.png" alt="Diálogo Upload Local File en Infor ION Desk con el archivo DocBits-Dev-Prod-Import-Template seleccionado para cargar" width="327"><figcaption></figcaption></figure>
3. **Confirmación:**
   *   Si la importación se realiza correctamente, se mostrará un mensaje de confirmación.

       <figure><img src="../../.gitbook/assets/m3_import_4.png" alt="Confirmación de importación en Infor ION Desk que indica que la importación de DocBits-Dev-Prod-Import-Template se realizó correctamente"><figcaption></figcaption></figure>
4. **Configuración posterior a la importación:**
   * Después de importar la plantilla, puede personalizar los ajustes de conexión específicos según sea necesario.
   * No olvide importar o configurar su **Service Account** para la autenticación y el control de acceso.

<figure><img src="../../.gitbook/assets/m3_import_5.png" alt="Página API Connection Point de DocBits-Dev-Prod-Import-Template con su nombre, ID lógico y detalles de autenticación"><figcaption></figcaption></figure>
