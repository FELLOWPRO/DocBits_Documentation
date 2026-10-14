# Configuración de propiedades de campo

Utilice **Configuración → Tipos de documento → Campos** para controlar cómo se comportan los campos de un tipo de documento. Seleccione primero el tipo de documento; el siguiente ejemplo muestra **Invoice** en la interfaz en inglés.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-overview-en.png" alt="Configuración de campos de Invoice en inglés con umbrales de reconocimiento, búsqueda, columnas de propiedades de campo y Save Settings"><figcaption>Configuración de campos de Invoice en una organización sandbox de DocBits.</figcaption></figure>

## Buscar un campo y cambiar sus propiedades

1. En **Search by Name**, introduzca el nombre o la etiqueta del campo. Esto filtra la lista; no modifica el campo.
2. Localice la fila del campo. Por ejemplo, **Invoice number** tiene el nombre técnico `invoice_id`.
3. Ajuste los controles de esa fila y, a continuación, seleccione **Save Settings**. El mismo botón de guardado está disponible encima y debajo de la tabla.

<figure><img src="../../../../../.gitbook/assets/dbdc155-field-properties-filtered-en.png" alt="Campo Invoice number en inglés con los controles Required, Read Only, Hidden, Force Validation, Use AI, OCR y Match Score"><figcaption>La fila Invoice number tras buscar `invoice_id`.</figcaption></figure>

| Control | Para qué se utiliza |
| --- | --- |
| **Required** | Marca la información que debe estar presente para la validación. Compruebe el resultado de validación del documento después de cambiar esta configuración. |
| **Read Only** | Muestra un campo sin permitir que los usuarios editen su valor. |
| **Hidden** | Mantiene el campo fuera de la vista normal del documento. |
| **Force Validation** | Exige que el campo supere la validación. Configure las reglas detalladas por separado; esta casilla no es un editor de reglas. |
| **Use AI** | Solicita o detiene la extracción mediante IA para este campo. La fila muestra si la extracción está solicitada. |
| **OCR** | Introduzca el umbral de confianza de OCR del campo. Es un número, no un interruptor de activación ni una configuración de idioma. |
| **Match Score** | Introduzca el umbral de coincidencia del campo. Es un número, no un interruptor de activación. |

Los controles deslizantes **OCR** y **Match Score** de **Recognition Settings** aplican valores a toda la lista de campos. Las casillas situadas justo debajo de los títulos de las columnas aplican **Required**, **Read Only**, **Hidden** o **Force Validation** a toda la lista. Revise las filas afectadas antes de seleccionar **Save Settings**. **Restore Defaults** restablece la configuración de los campos; utilícelo solo cuando desee reemplazar sus cambios.

## Otros controles de esta vista

- **Create new group** y **Create field** añaden un grupo o un campo. Consulte [Adding and Editing Fields](adding-and-editing-fields.md).
- **Master Data Settings** abre la [configuración de datos maestros](master-data-settings.md).
- Las casillas situadas en el extremo izquierdo seleccionan campos. El menú contiguo ofrece **Reassign Field Group** para los campos seleccionados.
- El botón más de **Formula** abre el editor de fórmulas de ese campo. El icono de **info** muestra información del campo. El icono de eliminar no está disponible para los campos estándar.

Para más información sobre validación y coincidencia, consulte [Setting Validation and Match Score](setting-validation-and-match-score.md).
