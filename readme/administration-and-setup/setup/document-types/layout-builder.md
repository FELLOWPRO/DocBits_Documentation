# Editor de diseños

Utilice el editor de diseños para organizar los campos y los controles que las personas ven al validar o aprobar un documento. Un diseño pertenece a un único tipo de documento, un único origen y un único tipo de diseño, así que compruebe estos tres elementos en la parte superior de la página antes de guardar.

## Abrir el diseño

1. Abra **Configuración → Tipos de Documento**.
2. Seleccione el tipo de documento que desea editar y abra el **editor de diseños**. En el caso de un subtipo de documento, abra la acción editor de diseños de ese subtipo.
3. Compruebe el encabezado. El selector de la izquierda es el **Origen** (por ejemplo, **Defecto**), seguido del **Tipo de Documento** (por ejemplo, **Factura**) y del **Tipo de diseño** (por ejemplo, **Validación de campos**). Cada selector abre una lista; al elegir otra entrada se carga ese diseño. Si el editor de diseños no está disponible, es posible que un administrador deba activar el módulo para su organización.

<figure><img src="../../../.gitbook/assets/layout-builder-overview-es.png" alt="El editor de diseños de una factura en DocBits, con los selectores de origen, tipo de documento y tipo de diseño, las pestañas Estructura, Campos y Elementos, el lienzo del diseño y el panel Propiedades a la derecha"><figcaption><p>El editor de diseños: los selectores del encabezado, las listas de elementos a la izquierda, el lienzo en el centro y el panel Propiedades a la derecha.</p></figcaption></figure>

## Trabajar con el encabezado

* **Tipo de Documento** y **Tipo de diseño** permiten cambiar de diseño. La página vuelve a cargar el diseño que elija.
* Junto a **Guardar**, DocBits indica si el diseño tiene **Cambios no guardados**. Después de guardar, muestra cuándo se guardó por última vez.
* **Guardar** almacena el diseño para el tipo de documento, el origen y el tipo de diseño seleccionados.
* El menú **Más** (tres puntos) contiene **Autogenerar plantilla**, **Aplicar diseño predeterminado a los orígenes**, **Usar plantilla predeterminada**, **Editar json**, **Copiar JSON** y **Configuración de diseño**. **Autogenerar plantilla** y **Usar plantilla predeterminada** sustituyen un diseño personalizado, así que compruebe antes el tipo de documento y el diseño seleccionados. **Editar json** está pensado para la configuración avanzada y solo debe utilizarse si comprende el formato de la plantilla.
* Si abandona la página con cambios sin guardar, DocBits le pregunta si desea guardarlos o descartarlos.

## Encontrar elementos: Estructura, Campos, Elementos

La parte izquierda tiene tres pestañas:

| Pestaña | Para qué sirve |
| --- | --- |
| **Estructura** | Ver el diseño como un árbol. Los grupos y sus campos aparecen en el orden en que se muestran en el lienzo, junto con el número de campos colocados y disponibles. |
| **Campos** | Todos los campos configurados para el tipo de documento, agrupados por grupo de campos y contraídos de forma predeterminada. El filtro alterna entre los campos **Todos**, **No usado** y **Oculto**, y el nombre técnico del campo se muestra debajo de su etiqueta. |
| **Elementos** | Controles de presentación e interacción como Texto, Etiqueta, Casilla de verificación, separadores, tablas, botones y subgrupos. |

<figure><img src="../../../.gitbook/assets/layout-builder-structure-es.png" alt="La pestaña Estructura del editor de diseños mostrando los grupos Detalles de la factura, Detalles de pago, Orden de compra y Detalles de entrega desplegados en sus campos"><figcaption><p>La pestaña Estructura muestra el diseño creado como un árbol de grupos y campos.</p></figcaption></figure>

Seleccione un elemento para añadirlo o arrástrelo al lienzo. El título de un grupo indica a quien valida el documento qué corresponde a esa sección. Cree o cambie el nombre de los campos de documento reutilizables primero en [Tipos de Documento](README.md).

## Trabajar en el lienzo

* **Diseño principal** muestra el diseño del propio documento. **Tabla** muestra el diseño de tabla que se utiliza para las líneas de artículos.
* **Documento** abre o cierra el documento de ejemplo junto al lienzo, de modo que pueda comparar el diseño con un documento real.
* Los grupos se representan como tarjetas; los campos de un grupo pueden organizarse en filas y tener anchos distintos.

## Cambiar las propiedades de un elemento

Seleccione un elemento o un grupo en el lienzo. El panel **Propiedades**, a la derecha, está siempre visible y se organiza en secciones:

* **Visualización**: etiqueta, nombre del campo, posición de la etiqueta y ancho del elemento.
* **Comportamiento**: solo lectura, oculto e índice de pestañas.
* **Valores y listas**: los valores que se ofrecen para el elemento.
* **Automatización**: reglas que rellenan o modifican el elemento.
* **Bordes y espaciado**: el aspecto del elemento.

Para el ancho, elija uno de los valores predefinidos (25, 33, 50, 66, 75 o 100 por ciento) en lugar de escribir un valor, y compruebe el resultado en el lienzo. Las secciones y opciones que aparecen dependen del elemento seleccionado. Para más detalles, consulte [Configurar las propiedades de los campos](../../settings/global-settings/document-types/layout-manager/configuring-field-properties.md).

## Revisar y guardar

Organice los grupos y los campos, compruebe el diseño en el lienzo y utilice **Guardar** en el encabezado cuando el resultado sea correcto. Para los diseños específicos de un origen, consulte [Diseños por origen](origin-layouts.md).

{% hint style="info" %}
Las capturas de pantalla muestran configuraciones sintéticas en la organización de prueba de DocBits, con el español seleccionado en la aplicación. No se guardó ni se sustituyó ningún diseño al realizarlas.
{% endhint %}
