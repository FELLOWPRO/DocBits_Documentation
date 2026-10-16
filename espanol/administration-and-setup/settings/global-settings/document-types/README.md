# Tipos de Documentos

{% embed url="https://youtu.be/pFz_6tvNlU4" %}
DocBits Document Types Explained: Create, Configure & Assign Processing Settings
{% endembed %}

<figure><img src="../../../../.gitbook/assets/image (78).png" alt="Document Types"><figcaption><p>Página Document Types</p></figcaption></figure>

## Descripción general

La página Document Types muestra todos los tipos de documento que DocBits reconoce y procesa. Está dividida en dos secciones:

* **Default Document Types**: tipos preconfigurados proporcionados por DocBits (Invoice, Credit Note, Delivery Note, Order Confirmation, Contract, ZUGFeRD, etc.). No se pueden eliminar.
* **Custom Document Types**: tipos que usted crea para sus necesidades empresariales específicas. Se pueden editar y eliminar.

## Controles por tipo de documento

Cada tarjeta de tipo de documento muestra:

| Control                           | Descripción                                                                               |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| **Activate**                      | Interruptor para activar o desactivar este tipo de documento para su procesamiento.       |
| **Extraction**                    | Interruptor para activar o desactivar la extracción de datos basada en IA para este tipo. |
| **Settings** (icono de engranaje) | Abre opciones de configuración adicionales para el tipo de documento.                     |

## Pestañas de configuración

Debajo de cada tipo de documento puede acceder a las siguientes pestañas de configuración:

| Pestaña                | Descripción                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------- |
| **Labels**             | Gestione las etiquetas de visualización y las traducciones del tipo de documento.                       |
| **Edit layout**        | Modifique cómo aparece el documento en la vista de validación, incluidas las posiciones de los campos.  |
| **Document Sub Types** | Configure subcategorías para este tipo de documento (por ejemplo, distintos formatos de factura).       |
| **Table columns**      | Personalice qué columnas de datos aparecen en la tabla de posiciones.                                   |
| **Fields**             | Gestione los campos de datos extraídos del documento (añadir, editar o eliminar campos).                |
| **Model Training**     | Configure y entrene el modelo de IA utilizado para reconocer y extraer datos.                           |
| **Regex**              | Configure expresiones regulares para la extracción de datos basada en patrones.                         |
| **Scripts**            | Escriba scripts de procesamiento personalizados que se ejecutan durante el procesamiento de documentos. |
| **E-Doc**              | Configure estándares de documentos electrónicos (XRechnung, ZUGFeRD, EDI, FatturaPA).                   |

## Custom Validation Rules

Abra un tipo de documento y seleccione **Custom Validation Rules** para gestionar sus propias reglas de validación. Para reutilizar una regla existente sin volver a crearla, siga [Duplicate a Custom Validation Rule](duplicate-a-custom-validation-rule.md). La guía explica el nombre de la regla, la clave de la regla y los controles de confirmación.

## Creación de un tipo de documento personalizado

1. Desplácese hacia abajo hasta la sección **Custom Document Types**.
2. Haga clic en **+ New**.
3. Introduzca un nombre para el nuevo tipo de documento.
4. Configure los campos, el diseño y los ajustes de extracción según sea necesario.

{% hint style="info" %}
Consulte [Setup Document Type](../../../setup/document-types/) para obtener instrucciones de configuración detalladas.
{% endhint %}
