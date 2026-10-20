# Pantalla de Validación

## Revisar una factura y completar su comprobación

Sigue una factura desde el panel hasta su entrega al siguiente paso: compara proveedor, fechas, número, importes y moneda con el original y consulta un aviso de campo obligatorio. Selecciona el número directamente en el documento, confirma su asociación y conserva la regla de extracción con Guardar reglas. En este ejemplo, la factura revisada se envía después para su aprobación. Las acciones disponibles dependen de tus permisos y del proceso de tu empresa.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-review-customer/v2/es.mp4" %}


## Descripción General

<div data-full-width="false"><figure><img src="../../../.gitbook/assets/validation_screen_overview.png" alt="Descripción general de la pantalla de validación"><figcaption></figcaption></figure></div>

### Origen del Documento (Document Origin)

El origen del documento determina cómo interpreta DocBits las fechas y los formatos numéricos. Elige el país que corresponda al documento y comprueba los valores extraídos con el original.

## **Botón Guardar:**

<figure><img src="../../../.gitbook/assets/validation_screen_save_button.png" alt="Botón Guardar"><figcaption></figcaption></figure>

* **Botón Guardar:**
  * **Propósito:** Guarda el estado actual del documento o script en el que se está trabajando.
  * **Caso de Uso:** Después de realizar cambios o anotaciones en un documento, use este botón para asegurar que todas las modificaciones se guarden.

### **Agregar Reglas Especiales:**

<figure><img src="../../../.gitbook/assets/validation_screen_add_special_rules.png" alt="Botón Agregar reglas especiales"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/validation_screen_add_script_example.png" alt="Ejemplo de Agregar script"><figcaption></figcaption></figure>

* **Agregar Reglas Especiales / Agregar Script en DocBits:**
  * **Propósito:** Permite a los usuarios implementar reglas o scripts específicos que personalizan cómo se procesan los documentos.
  * **Caso de Uso:** Use esta función para automatizar tareas como la extracción de datos o la validación de formatos, mejorando la eficiencia del flujo de trabajo.

{% hint style="info" %}
Vea aquí agregar [Script en DocBits](../../../administration-and-setup/settings/global-settings/document-types/script/scripting-in-docbits/)
{% endhint %}

### **Campos Difusos:**

<figure><img src="../../../.gitbook/assets/validation_screen_fuzzy_fields.png" alt="Campos difusos"><figcaption></figcaption></figure>

* **Campos Difusos:**
  * **Propósito:** Ayuda a identificar y corregir campos donde los datos pueden no coincidir perfectamente pero son lo suficientemente cercanos.
  * **Caso de Uso:** Útil en procesos de validación de datos donde no siempre son posibles coincidencias exactas, como nombres o direcciones ligeramente mal escritos.

### **Campos Requeridos:**

<figure><img src="../../../.gitbook/assets/validation_screen_required_fields.png" alt="Campos requeridos"><figcaption></figcaption></figure>

Hay campos que son necesarios para una edición posterior, estos se pueden editar en la configuración.

Use el consejo de herramienta para averiguar si:

* Es un campo obligatorio (requerido)
* Se requiere validación
* Baja confianza
* Desajuste del monto total de impuestos

**Campos Requeridos:**

* **Propósito:** Identifica campos obligatorios dentro de los documentos que deben completarse o corregirse antes de un procesamiento posterior.
* **Caso de Uso:** Asegura que los datos esenciales se capturen con precisión, manteniendo la integridad de los datos y el cumplimiento de las reglas comerciales.

<figure><img src="https://lh7-us.googleusercontent.com/3-ZXi-fUcWlM0nUaOAQbY7bynchbIN30JReKRdijyMFvX_GIHrnbcismANdOi6UfYa6GCPvk9wnOixya0E_rBk3V8hQduS-gBZJi4k0Kq8jeN93DxC2w5J-YRqeV9IkVB6oiH8tm0-y7gWJO_8fBplo" alt=""><figcaption></figcaption></figure>

## Tabla extraída (líneas de detalle)

<figure><img src="../../../.gitbook/assets/validation_screen_line_items_table.png" alt="Tabla de líneas de detalle en la pantalla de validación con la barra de herramientas de la tabla"><figcaption><p>La tabla extraída debajo de los campos de cabecera</p></figcaption></figure>

Debajo de los campos de cabecera, DocBits muestra la tabla de líneas de detalle del documento: una fila por línea de factura y una columna por cada [columna de tabla](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md) configurada para el tipo de documento. Cuando un tipo de documento tiene varias tablas (por ejemplo, artículos y cargos), cada tabla tiene su propia pestaña encima de la cuadrícula.

### De dónde procede la tabla

Encima de la cuadrícula hay una pestaña por cada ruta de extracción que la organización tiene activada:

| Pestaña | Significado |
|---|---|
| **Extracted table** | Extracción basada en reglas (ajuste *Table Extraction*). En un proveedor con tabla entrenada, estas filas proceden de las reglas guardadas y se extraen de la misma manera en todos los documentos de ese proveedor; en un proveedor sin entrenar, la pestaña puede estar vacía. |
| **AI Extracted table** | La extracción de tablas por IA (ajuste *AI Table Extraction*). Se rellena cuando el proveedor no tiene reglas guardadas, y en las columnas marcadas como *Use AI* incluso cuando existen reglas. Un tooltip *AI table not found* en la pestaña significa que la IA no devolvió nada para este documento. |
| **PO Tables** | Solo en el constructor de diseños: las líneas de la orden de compra usadas para la coincidencia. |

Si no aparece ninguna de las pestañas, ambos ajustes de tabla están desactivados para la organización (Settings → Document Processing → Classification and Extraction). El nivel de IA que lee la tabla se establece por organización y se puede sobrescribir por proveedor; consulte [Modelo de IA específico del proveedor](supplier-specific-ai-model-for-field-and-table-extraction.md).

### Trabajar en la tabla

* **Editar una celda**: haga clic en ella y escriba. Las columnas de importe, número y fecha se validan mientras escribe.
* **Add new table row**: añade una fila vacía al final. Úselo cuando no se haya reconocido una línea.
* **Eliminar una fila**: el icono de la papelera al final de la fila.
* **Add empty mapped columns**: muestra las columnas configuradas que la IA dejó vacías, para que pueda rellenarlas a mano.
* **Restore Table Column**: recupera una columna que quitó de la vista en este documento.
* **Delete table**: borra todas las filas de esta tabla en este documento. La configuración no se toca.
* **Add new table column** (administradores): el mismo cuadro de diálogo que en la configuración de columnas de tabla, sin salir del documento.
* **Tags** (solo tabla AI): indicaciones breves en texto para la IA, por ejemplo *"la última columna es el importe neto"*. Consulte [Etiquetas de la tabla AI](../ai-table/ai-table-tags.md).
* **Apply** / **Save** / **Delete** junto a las etiquetas: *Apply* vuelve a ejecutar la tabla AI para este documento con las etiquetas y los cambios de columnas que haya hecho, sin guardar nada (si el documento tiene líneas coincidentes con una PO, DocBits avisa de que las coincidencias se eliminan); *Save Rules* guarda la asignación de columnas y las etiquetas actuales para este proveedor; *Delete Rules* las elimina y vuelve a ejecutar la extracción por IA para este documento.
* **Export**: descarga la tabla como archivo CSV.
* **Go to table extraction view**: abre el entrenamiento de tablas para este documento. Úselo cuando el mismo proveedor salga mal una y otra vez: dibuje la tabla una vez, asigne las columnas y haga clic en *Save Rules*; a partir de entonces las filas aparecen en la pestaña *Extracted table*. Consulte [Entrenamiento de Campos de Línea / Tabla de Entrenamiento](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md).

{% hint style="info" %}
Si la tabla la extrajo la IA y abre el entrenamiento de tablas, DocBits pregunta *Table is already extracted by AI. Do you want to train manually?* Después de guardar las reglas, la tabla AI deja de usarse para este proveedor.
{% endhint %}

### Volver a extraer la tabla

* **Mismo documento, tabla AI:** añada o cambie etiquetas y haga clic en **Apply**; la tabla AI se reconstruye solo para este documento. Para descartar también las etiquetas y el formato guardados del proveedor, haga clic en **Delete** (*Delete Rules*): DocBits confirma *Rules has been deleted successfully* y vuelve a ejecutar la extracción por IA.
* **Mismo documento, reglas entrenadas:** abra *Go to table extraction view*, corrija la tabla y haga clic en *Save & re-extract*.
* **Todo el documento de nuevo (cabecera y tabla):** Dashboard → menú del documento → *Restart*. Es necesario después de que un administrador cambie las columnas de tabla o los ajustes de extracción.

### Qué bloquea la aprobación

La tabla se comprueba al guardar o aprobar. Una celda en rojo o un mensaje debajo de la tabla significa una de estas situaciones:

| Mensaje | Causa | Qué hacer |
|---|---|---|
| Required column empty | Una columna marcada como *Is Required* no tiene valor en esta fila. | Rellene la celda o pregunte a un administrador si la columna debe ser obligatoria. |
| *Line total does not match quantity x unit price (expected …, got …)* | `quantity × unit price + charges − discount` difiere del total de línea en más de 0,02. A menudo, uno de los cuatro valores se leyó en la columna equivocada. | Corrija el valor que está mal respecto al documento; si una columna como *Charges* se rellena sistemáticamente con el valor equivocado, avise a su administrador (consulte [Solución de problemas](../../../administration-and-setup/settings/global-settings/document-types/table-columns/troubleshooting-1.md)). |
| *Line items add up to … but the net total is …* | La suma de los totales de línea difiere del importe neto de la cabecera. | Compruebe si falta una fila o hay una duplicada, o si un importe de cabecera se leyó mal. |
| *Line Item Table is missing Mandatory column for PO* | La coincidencia de PO necesita número de artículo, precio unitario, cantidad e importe total; una de esas columnas está oculta. | Administrador: vuelva a mostrar la columna en Table Columns. |

Un administrador puede desactivar todas las comprobaciones de tabla de un tipo de documento con *Skip table validation* (Document Types → More Settings); las discrepancias de línea y las columnas obligatorias vacías dejan entonces de notificarse.

Más información sobre las comprobaciones: [Comprobaciones Automáticas en la Pantalla de Validación](automatic-checks-on-the-validation-screen.md) y [Solución de problemas de extracción de tablas](../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md).

### **Lupa:**

<figure><img src="../../../.gitbook/assets/validation_screen_magnifying_glass.png" alt="Icono de lupa" width="118"><figcaption></figcaption></figure>

* **Lupa:**
  * **Propósito:** Proporciona una vista ampliada de un área seleccionada del documento.
  * **Caso de Uso:** Ayuda a examinar detalles finos o texto pequeño en documentos, asegurando precisión en la entrada o revisión de datos.

<figure><img src="../../../.gitbook/assets/validation_screen_zoomed_view.png" alt="Vista ampliada del documento"><figcaption></figcaption></figure>

### **Abrir nueva ventana:**

<figure><img src="../../../.gitbook/assets/validation_screen_open_new_window.png" alt="Icono de abrir nueva ventana" width="130"><figcaption></figcaption></figure>

* **Abrir Nueva Ventana:**
  * **Propósito:** Abre una nueva ventana para la comparación de documentos lado a lado o multitarea.
  * **Caso de Uso:** Útil al comparar dos documentos o al referenciar información adicional sin salir del documento actual.

### **Atajos de teclado:**

<figure><img src="../../../.gitbook/assets/validation_screen_keyboard_shortcuts.png" alt="Icono de atajos de teclado" width="145"><figcaption></figcaption></figure>

1. **Atajos de Teclado:**
   * **Propósito:** Permite a los usuarios realizar acciones rápidamente usando combinaciones de teclado.
   * **Caso de Uso:** Mejora la velocidad y eficiencia en la navegación y procesamiento de documentos al minimizar la dependencia de la navegación con el ratón.

### **Tareas:**

<figure><img src="../../../.gitbook/assets/validation_screen_tasks_button.png" alt="Botón Tareas" width="55"><figcaption></figcaption></figure>

Para compartir información interna, puede crear tareas y asignarlas a un empleado o grupo específico dentro de la empresa.

* **Tareas:**
  * **Propósito:** Permite a los usuarios crear tareas relacionadas con documentos y asignarlas a miembros del equipo.
  * **Caso de Uso:** Facilita la colaboración y gestión de tareas dentro de los equipos, asegurando que todos conozcan sus responsabilidades.

<figure><img src="../../../.gitbook/assets/validation_screen_task_creation.png" alt="Cuadro de diálogo de creación de tareas" width="218"><figcaption></figcaption></figure>

### Historial de aprobaciones

<figure><img src="../../../.gitbook/assets/approval_history_button.png" alt="Botón Historial de aprobaciones"><figcaption></figcaption></figure>

**Nota:** El historial de aprobaciones debe estar activado antes de que pueda mostrarse aquí.

**Historial de aprobaciones:**

* **Propósito**: Muestra el historial de aprobación del documento en la validación de campos; el rojo indica rechazado y el color de la aplicación indica aprobado.
* **Caso de Uso**: Útil para organizaciones que requieren un registro transparente de las acciones de aprobación durante la validación de campos.

<figure><img src="../../../.gitbook/assets/approval_history_list_view.png" alt="Vista de lista del historial de aprobaciones"><figcaption></figcaption></figure>

### **Modo de anotación:**

<figure><img src="../../../.gitbook/assets/validation_screen_annotation_mode.png" alt="Botón Modo de anotación" width="187"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/annotation_mode_example.png" alt="Ejemplo del modo de anotación"><figcaption></figcaption></figure>


Puede dejar anotaciones en un documento. Esto puede ser útil para dejar información a otros usuarios que sigan editando este documento.

* **Modo de Anotación:**
  * **Propósito:** Permite a los usuarios dejar notas o anotaciones directamente en el documento.
  * **Caso de Uso:** Útil para proporcionar comentarios, instrucciones o notas importantes a otros miembros del equipo que trabajarán en el documento más tarde.

### **Combinar:**

<figure><img src="../../../.gitbook/assets/validation_screen_merge_documents.png" alt="Botón Combinar documentos" width="60"><figcaption></figcaption></figure>

Los documentos se pueden combinar aquí, por ejemplo, si faltaba una página de una factura, estas páginas se pueden combinar más tarde de esta manera sin tener que eliminar o volver a cargar todo el documento.

* **Combinar Documentos:**
  * **Propósito:** Combina múltiples documentos en un solo archivo.
  * **Caso de Uso:** Útil en escenarios donde partes de un documento se escanean por separado y necesitan ser consolidadas.

### **Vista OCR:**

<figure><img src="../../../.gitbook/assets/validation_screen_ocr_view_button.png" alt="Botón Vista OCR" width="77"><figcaption></figcaption></figure>

En la vista OCR, el texto se filtra automáticamente del documento. Esto se utiliza para reconocer características relevantes, como el código postal, número de contrato, número de factura y la clasificación de un documento.

* **Vista OCR:**
  * **Propósito:** Reconoce automáticamente el texto dentro de los documentos utilizando tecnología de Reconocimiento Óptico de Caracteres.
  * **Caso de Uso:** Optimiza el proceso de digitalización de textos impresos o manuscritos, haciéndolos buscables y editables.

<figure><img src="../../../.gitbook/assets/validation_screen_ocr_view_example.png" alt="Ejemplo de la vista OCR"><figcaption><p>OCR</p></figcaption></figure>

### **Crear ticket:**

<figure><img src="../../../.gitbook/assets/validation_screen_create_ticket_button.png" alt="Botón Crear ticket" width="97"><figcaption></figcaption></figure>

A diferencia de las tareas que se transmiten internamente dentro de la empresa, este ticket de soporte es importante para notificarnos y crear inmediatamente un ticket en caso de errores y/o discrepancias. Esto facilita mucho el proceso porque puede enviar inmediatamente el error con el documento correspondiente. También existe la opción de establecer prioridad, tomar una captura de pantalla del documento o cargar una.

* **Crear Ticket:**
  * **Propósito:** Permite a los usuarios reportar problemas o discrepancias creando un ticket de soporte.
  * **Caso de Uso:** Esencial para la rápida resolución de problemas y errores, ayudando a mantener la integridad y el buen funcionamiento del sistema.

<figure><img src="../../../.gitbook/assets/validation_screen_create_ticket_form.png" alt="Formulario de creación de ticket" width="237"><figcaption></figcaption></figure>

### **Registros de scripts de documentos:**

<figure><img src="../../../.gitbook/assets/validation_screen_script_logs_button.png" alt="Botón Registros de scripts de documentos" width="160"><figcaption></figcaption></figure>

Los scripts se pueden crear en la configuración bajo Tipos de Documentos; esta información se mostrará aquí.

* **Registros de Scripts de Documentos:**
  * **Propósito:** Muestra registros relacionados con scripts que se han implementado para diferentes tipos de documentos.
  * **Caso de Uso:** Útil para rastrear y depurar acciones de scripts en documentos, ayudando a los usuarios a comprender los procesos automatizados y corregir cualquier problema.

<figure><img src="../../../.gitbook/assets/document_script_logs_view.png" alt="Vista de registros de scripts de documentos"><figcaption></figcaption></figure>

### **Más configuraciones:**

<figure><img src="../../../.gitbook/assets/more_settings_menu_icon.png" alt="Icono del menú Más configuraciones"><figcaption></figcaption></figure>

### **Flujo de Documento:**

Allí encontrará el flujo del documento

* **Propósito:** Muestra la secuencia y progresión del procesamiento de documentos dentro del sistema.
* **Caso de Uso:** Ayuda a rastrear el estado del documento a través de diferentes etapas, asegurando que se sigan todos los pasos de procesamiento necesarios.

### **Ir a la plantilla de diseño:**

* Con esta opción será redirigido y podrá editar su diseño o usar la plantilla predeterminada
* **Ir a la Plantilla de Diseño:**
  * **Propósito:** Redirige a los usuarios a un editor de diseño donde pueden modificar plantillas existentes o aplicar una predeterminada.
  * **Caso de Uso:** Permite la personalización de los diseños de documentos para satisfacer necesidades o preferencias comerciales específicas, mejorando la alineación visual y funcional del documento con los estándares de la empresa.

### Utilizar E-Texto si Está Disponible

* **Propósito:** Permite que DocBits utilice e-texto para todos los documentos de un proveedor específico si está disponible, mejorando la precisión de la extracción.
* **Caso de Uso:** Mejora la extracción de texto aprovechando el texto incrustado en lugar de OCR, lo que puede llevar a resultados más precisos para este proveedor.

### [Modelo de IA Basado en Proveedor](supplier-specific-ai-model-for-field-and-table-extraction.md)

* **Propósito:** Permite la selección entre tres modelos de IA diferentes para optimizar los resultados de extracción para un proveedor específico.
* **Caso de Uso:** Asegura una mejor precisión de extracción al elegir el modelo de IA más adecuado para la estructura y contenido del documento de cada proveedor.
