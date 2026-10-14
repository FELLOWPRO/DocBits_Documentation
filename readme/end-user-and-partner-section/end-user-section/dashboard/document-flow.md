# Document Flow

**Document Flow** muestra los pasos de procesamiento de un documento. Utilícelo para ver qué pasos se han completado, cuál está en espera y cuánto tiempo ha tardado el procesamiento. El ejemplo siguiente utiliza una factura sintética en el Sandbox en inglés.

## Abrir desde el dashboard

En el **Dashboard**, localice el documento. En su columna **Actions**, seleccione los tres puntos y, a continuación, **Document flow**. Esta opción abre el flujo de ese documento; no modifica el documento.

<figure><img src="../../../.gitbook/assets/document-flow-dashboard-menu-en.png" alt="Dashboard en inglés con el menú Actions abierto para una factura sintética; Document flow aparece debajo de Assign to."><figcaption>Elija Document flow en el menú Actions del documento.</figcaption></figure>

## Abrir desde Field Validation

Abra el documento. En **Field Validation**, seleccione los tres puntos de la barra de acciones derecha y, a continuación, **Document Flow** en **More options**.

<figure><img src="../../../.gitbook/assets/document-flow-validation-menu-en.png" alt="Pantalla Field Validation en inglés con el menú More options y su elemento Document Flow junto a una factura sintética."><figcaption>El mismo flujo está disponible desde la vista del documento.</figcaption></figure>

## Leer el flujo

**Process Statistics**, a la izquierda, resume el número de pasos, los pasos completados y en espera, los reinicios, el tiempo total, el estado actual y el progreso general. Cada tarjeta numerada muestra un paso de procesamiento y su estado actual. Desplácese hacia abajo para ver los pasos posteriores.

<figure><img src="../../../.gitbook/assets/document-flow-overview-en.png" alt="Document Flow en inglés con Process Statistics a la izquierda y las primeras tarjetas de paso numeradas: Imported, Document Imported y OCR."><figcaption>Los primeros pasos del flujo de una factura sintética.</figcaption></figure>

<figure><img src="../../../.gitbook/assets/document-flow-later-steps-en.png" alt="Document Flow en inglés tras desplazarse hacia abajo; las tarjetas posteriores incluyen Classification, Field Extraction, Table Extraction, Transformer, Metadata Populator, Lookup Data y Validator."><figcaption>Desplácese para seguir la secuencia a través de los pasos posteriores.</figcaption></figure>

Seleccione la tarjeta de un paso para abrir **Step Details** a la izquierda. Muestra el módulo y su estado. También puede abrirse un panel **Task Logs** a la derecha; los detalles del registro dependen de lo que esté disponible para esa tarea. Seleccione **×** en Step Details para cerrar el panel.

<figure><img src="../../../.gitbook/assets/document-flow-step-details-en.png" alt="Document Flow en inglés con la tarjeta OCR seleccionada; Step Details, debajo de Process Statistics, muestra Module OCR y Status Completed."><figcaption>Step Details explica el estado del módulo seleccionado.</figcaption></figure>
