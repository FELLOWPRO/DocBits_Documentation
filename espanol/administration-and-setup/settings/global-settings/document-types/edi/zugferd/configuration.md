# Configuración de ZUGFeRD

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
Tutorial de factura electrónica de DocBits: procesar XRechnung / ZUGFeRD (Factur-X), validar datos y automatizar flujos de trabajo
{% endembed %}

## **Versiones compatibles de ZUGFeRD**

DocBits es compatible con todas las versiones principales de ZUGFeRD, incluyendo:

* **1.0**
* **2.0**
* **2.1** (cumple con FACTUR-X 1.0.05)
* **2.2**
* **2.3** (cumple con FACTUR-X 1.07.2)
* **2.3.2**

#### Activación y modificación estándar

El estándar ZUGFeRD siempre está activo de forma predeterminada, pero puede realizar modificaciones si es necesario.

### **Pasos para modificar la configuración de ZUGFeRD:**

1. Vaya a **Configuración → Configuración global → Tipos de documento → Factura**.
2. Haga clic en **E-Doc**.\\
3. Aparecerá una lista de todos los e-docs disponibles.
4. Localice la versión de **ZUGFeRD** que desea modificar.\\

## **Configuración de transformación y ruta XML:**

En la **configuración de transformación**, puede definir la ruta para localizar información específica dentro del archivo XML y guardarla en una nueva estructura, lo que facilita el acceso a los datos.\
<mark style="color:red;">**Nota**</mark>: Si utiliza esta funcionalidad, debe usar las rutas XML recién creadas, no las rutas XML originales, en la **Vista previa** y la **Ruta de extracción**.

### **Pasos para modificar el archivo de transformación:**

1. Abra la **Transformación**.
2. Cree un nuevo borrador haciendo clic en el **icono del lápiz**.
3. Seleccione el borrador recién creado.
4. Cree un nuevo campo o modifique uno existente.
5. Establezca la ruta deseada para la extracción de datos.
6. Haga clic en **Guardar**.

### Notas importantes:

* El **archivo de vista previa** se utiliza solo para **FACTUR-X** y no para **ZUGFeRD**. ZUGFeRD utilizará el **PDF** original.

## Configuración de vista previa en PDF

La **Configuración de vista previa en PDF** se utiliza para generar una versión del documento legible para el usuario. Puede personalizarla con HTML para adaptarla a sus necesidades.

### **Pasos para modificar el archivo de vista previa:**

1. Abra la **Vista previa**.
2. Cree un nuevo borrador haciendo clic en el **icono del lápiz**.
3. Seleccione el borrador recién creado.
4. Cree un nuevo campo o modifique uno existente.
5. Establezca la ruta deseada para la extracción de datos.
6. Haga clic en **Guardar**.

## Configuración de rutas de extracción

La **Configuración de rutas de extracción** se utiliza para extraer datos y completar campos en la **pantalla de validación**, como la tabla de facturas o los campos configurados en el diseño de la factura.

### **Pasos para modificar** **las rutas de extracción**:

1. Abra las **Rutas de extracción**.
2. Cree un nuevo borrador haciendo clic en el **icono del lápiz**.
3. Seleccione el borrador recién creado.
4. Cree un nuevo campo o modifique uno existente.
5. El lado izquierdo representa el **ID del campo de DocBits**, que se puede encontrar en **Configuración → Configuración global → Tipos de documento → Factura → Campos**.\\
6. El lado derecho representa la **ruta al campo** creado en la Transformación.
7. Haga clic en **Guardar**.

Al seguir estos pasos, puede garantizar una extracción y validación de datos precisas para las facturas ZUGFeRD.

## Reglas utilizadas y activación

Las reglas específicas de la organización tienen prioridad sobre las predeterminadas para el formato eDoc detectado. Compruebe la TRANSFORMATION activa y compruebe qué nodo proporciona invoice_type en el XML transformado; la ruta depende del formato. Guardar conserva un borrador; utilice la marca de verificación para activarlo después de las pruebas. Una Preview renderizada no demuestra el tipo de documento almacenado. Consulte la [guía de resolución de problemas de clasificación](../credit-note-recognized-as-invoice.md) para conocer los códigos 381/261, los scripts posteriores y las precauciones para volver a procesar documentos.
