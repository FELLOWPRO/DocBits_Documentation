# Standard Workflow

El constructor **Standard Workflow** es el editor lineal basado en tarjetas para automatizar el procesamiento de documentos. Un flujo de trabajo se compone de tres grupos de tarjetas: **When** (el disparador), **And** (condiciones adicionales) y **Then** (las acciones a ejecutar). Cuando un documento cumple las condiciones When/And, las acciones Then se ejecutan automáticamente.

## Cómo acceder

Abra **Workflow Dashboard → Workflow List** y, a continuación, haga clic en **Add Workflow** para crear un nuevo flujo de trabajo Standard, o haga clic en un flujo de trabajo existente para editarlo.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Lista de flujos de trabajo con tipo, orden de ejecución y disparador"><figcaption><p>El Workflow List — cada fila es un flujo de trabajo que puede abrir, activar/desactivar o editar.</p></figcaption></figure>

## El modelo When / And / Then

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="Lienzo de Standard Workflow con tarjetas When, And y Then"><figcaption><p>El lienzo de Standard Workflow. Este ejemplo se dispara con facturas en una suborganización y se las asigna a un usuario.</p></figcaption></figure>

- **When** — el disparador que inicia el flujo de trabajo (p. ej. *Document type is Invoice*).
- **And** — condiciones adicionales que también deben cumplirse (p. ej. *Document is part of sub-organization*). Déjelo vacío para ejecutarlo en cada coincidencia de la tarjeta When.
- **Then** — las acciones a realizar (p. ej. *Assign the document to the user*, crear una tarea, llamar a una API, enviar un correo electrónico).

## Añadir tarjetas

Haga clic en **Add Card** en cualquier grupo para abrir la biblioteca de tarjetas. Las tarjetas están organizadas por categoría para que pueda encontrar el bloque de construcción que necesita:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card agrupada por categoría"><figcaption><p>La biblioteca <strong>Add Card</strong> — tarjetas de condición, tarjetas de comparación, tarjetas de acción y más, agrupadas por categoría.</p></figcaption></figure>

Guarde con **Save Workflow**, o guarde el diseño como una plantilla reutilizable con **Save Template**.

## Próximos pasos

- Vea qué hace cada tarjeta en la sección **Cards**.
- Combine tarjetas en soluciones probadas con las **Workflow Pattern Guides**.
- Para flujos con ramificaciones y rutas paralelas (Wait ALL / Wait ANY / OR), utilice el constructor **Advanced Workflow**.
