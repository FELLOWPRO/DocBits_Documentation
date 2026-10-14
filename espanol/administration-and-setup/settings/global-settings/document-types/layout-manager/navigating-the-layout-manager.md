# Navegación por el Constructor de diseño

Utilice el **Layout Builder** para organizar los campos y grupos que las personas ven en un documento. Esta guía utiliza el diseño de **Invoice** en inglés de una organización sandbox.

## Abrir el diseño de Invoice

1. Vaya a **Configuración → Tipos de documento**.
2. Localice **Invoice** y seleccione **Layouts** en su tarjeta. Se abre el Layout Builder para ese tipo de documento.
3. Compruebe el selector de diseño en la parte superior izquierda. El ejemplo siguiente muestra **DEFAULT**.

<figure><img src="../../../../../.gitbook/assets/dbdc177-document-types-en.png" alt="Página Document Types en inglés con la tarjeta Invoice y su enlace Layouts"><figcaption>Abra **Layouts** desde la tarjeta Invoice.</figcaption></figure>

## Encontrar grupos y campos

El panel izquierdo **Elements** tiene tres secciones. **Groups** enumera las secciones del documento; el lienzo central muestra su disposición actual. Seleccione un campo en el lienzo y abra **Properties** para cambiar su configuración de visualización. Consulte [Configuración de propiedades de campo](configuring-field-properties.md) para ver las opciones disponibles.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-elements-en.png" alt="Layout Builder de Invoice en inglés con Groups en el panel Elements y los campos agrupados en el lienzo"><figcaption>La lista Groups y el lienzo del diseño de Invoice.</figcaption></figure>

Abra **Fields** para encontrar los campos de documento disponibles. Utilice su cuadro de búsqueda cuando la lista sea larga y, a continuación, arrastre el campo al grupo deseado en el lienzo. Los campos que ya están colocados en el diseño pueden aparecer como no disponibles en la lista.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-fields-en.png" alt="Panel Fields del Layout Builder en inglés con búsqueda y los campos de Invoice disponibles"><figcaption>Busque entre los campos disponibles antes de colocar uno.</figcaption></figure>

Abra **Form Elements** para ver controles visuales como Text, Label, Check Box, separador, Button y Sub Group. Arrastre el elemento que necesite al lienzo y, a continuación, compruebe sus **Properties**.

<figure><img src="../../../../../.gitbook/assets/dbdc177-layout-form-elements-en.png" alt="Panel Form Elements del Layout Builder en inglés con texto, etiquetas, casillas de verificación, botones y subgrupos"><figcaption>La paleta actual de Form Elements.</figcaption></figure>

## Organizar y guardar

- Seleccione el título de un grupo en el lienzo para cambiarlo. El **+** situado encima del lienzo añade un grupo; el icono de llaves contiguo abre el formulario avanzado de grupo en JSON.
- Pase el cursor sobre un grupo para ver las acciones de copiar JSON, subir, bajar, eliminar y el control de arrastre. Para reordenar campos, arrástrelos dentro de un grupo o entre grupos.
- Seleccione un campo en el lienzo para abrir **Properties**. Su icono de eliminar lo quita de este diseño. Para configurar la validación, el OCR o la coincidencia, utilice la [configuración de Campos](../fields/configuring-field-properties-1.md) independiente.
- Seleccione **Save** en la barra superior después de editar. Consulte [Save and Apply Changes](save-and-apply-changes.md) antes de usar las demás acciones de la barra superior, incluidas la generación de plantillas, las plantillas predeterminadas y la aplicación de un diseño a los orígenes.
