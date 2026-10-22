# XRechnung

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits Tutorial de Factura Electrónica: Procesar XRechnung / ZUGFeRD (Factur-X), validar datos y automatizar flujos de trabajo
{% endembed %}

## Descripción general

En el panel de administración XRechnung, encontrará los siguientes componentes clave:

## 1. Transformación

### Objetivo

El proceso de Transformación es esencial para convertir datos sin procesar, generalmente en formato XML, a un formato estructurado que cumpla con requisitos específicos, como generar una factura. En XRechnung, esto se logra principalmente usando XSLT (Transformaciones de lenguaje de hoja de estilo extensible). XSLT es un lenguaje diseñado para transformar documentos XML en otro tipo de documentos, como otro XML, HTML o texto sin formato.

### Cómo funciona

• Plantilla XSLT: el archivo XSLT define cómo se procesan los datos XML y cómo debería verse el resultado final. Aplica reglas y plantillas para extraer, manipular y generar los datos del documento XML.

• Elementos y Atributos: El archivo XSLT contiene elementos y atributos específicos que controlan el proceso de transformación. Por ejemplo, \<xsl:value-of> se utiliza para extraer el valor de un nodo específico del documento XML.

### Funciones de administración

• Modifying the XSLT:

• Editar plantillas existentes: un administrador puede modificar las plantillas XSLT existentes para cambiar cómo se transforman los datos de entrada XML. Por ejemplo, si es necesario extraer información adicional del documento XML, un administrador podría agregar nuevas reglas en el archivo XSLT.

• Crear nuevas versiones: si se requieren cambios, un administrador puede crear una nueva versión de la plantilla XSLT. Esto garantiza que las versiones anteriores permanezcan intactas para referencia histórica o reversión si es necesario.

### Ejemplo:

Supongamos que la plantilla XSLT extrae el ID de la factura usando:

```xml
<xsl:value-of select="//INVOICE/INVOICE_ID/text()" />
```

Si es necesario extraer un campo nuevo, como el número de referencia de un cliente, un administrador podría agregar:

```xml
<xsl:value-of select="//INVOICE/CUSTOMER_REFERENCE_NUMBER/text()" />
```

## 2. Vista previa

### Objetivo

La función Vista previa permite a los administradores ver el resultado generado por la transformación XSLT antes de finalizarla. Este paso es crucial para garantizar que las reglas de transformación funcionen correctamente y que el resultado cumpla con los estándares requeridos.

### Cómo funciona

• Validación en tiempo real: la función de vista previa proporciona una representación en tiempo real de cómo se verán los datos transformados cuando se apliquen a un documento real (como una factura). Esto ayuda a detectar errores o problemas de formato con antelación.

• Ajustes: si la vista previa muestra discrepancias o errores, los ajustes se pueden realizar directamente en el archivo de transformación (XSLT).

### Funciones de administración

• Personalización de la vista previa:

• Modificar la configuración de vista previa: un administrador puede ajustar qué partes de la transformación se previsualizan. Por ejemplo, podrían centrarse en secciones específicas del documento o probar nuevas reglas agregadas a la plantilla XSLT.

• Guardar e iterar: después de realizar ajustes, la vista previa se puede actualizar para ver los cambios. Este proceso iterativo permite realizar ajustes hasta lograr el resultado deseado.

### Ejemplo:

Si un administrador nota que el formato de fecha en la vista previa es incorrecto (por ejemplo, muestra YYYY-MM-DD en lugar de DD-MM-YYYY), puede modificar XSLT para formatear la fecha correctamente y ver inmediatamente el resultado en la vista previa.

## 3. Rutas de extracción

### Objetivo

Las rutas de extracción definen las rutas específicas dentro de una estructura XML o JSON de la que se deben extraer los datos. Este proceso es esencial para aislar piezas clave de información dentro del documento que se utilizarán en la transformación o para otras tareas de procesamiento.

### Cómo funciona

• XPath y JSONPath: las rutas de extracción utilizan lenguajes como XPath (para XML) o JSONPath (para JSON) para especificar la ubicación de los datos dentro del documento. Estas rutas son cruciales para decirle al sistema exactamente dónde encontrar y cómo extraer la información requerida.

### Funciones de administración

• Definición y modificación de rutas:

• Modificar rutas existentes: un administrador puede modificar las rutas de extracción si la estructura de datos cambia o si es necesario extraer datos adicionales. Esto podría implicar cambiar las expresiones XPath o JSONPath.

• Agregar nuevas rutas: para nuevos campos o puntos de datos, un administrador puede definir nuevas rutas de extracción. Esto implicaría especificar la ruta correcta en el documento XML o JSON.

### Ejemplo:

En un documento de factura XML, si la ruta a el ID de la factura se define como:

```json
"invoice_id": "//INVOICE/INVOICE_ID/text()"
```

Y es necesario agregar un nuevo campo, como una dirección de envío; un administrador podría agregar:

```json
"shipping_address": "//INVOICE/SHIPPING/ADDRESS/text()"
```

## Reglas utilizadas y activación

Las reglas específicas de la organización tienen prioridad sobre las predeterminadas para el formato eDoc detectado. Compruebe la TRANSFORMATION activa y compruebe qué nodo proporciona invoice_type en el XML transformado; la ruta depende del formato. Guardar conserva un borrador; utilice la marca de verificación para activarlo después de las pruebas. Una Preview renderizada no demuestra el tipo de documento almacenado. Consulte la [guía de resolución de problemas de clasificación](../credit-note-recognized-as-invoice.md) para conocer los códigos 381/261, los scripts posteriores y las precauciones para volver a procesar documentos.
