# Aprobar o rechazar una factura

## ¿Qué sigue a una decisión de aprobación comercial?

<figure><img src="../../.gitbook/assets/process-approval-es-20261028.png" alt="Aprobar o rechazar factura: Distinguir entre examen, decisión y posterior entrega."><figcaption><p>Distinguir entre examen, decisión y posterior entrega. El diagrama es esquemático; La configuración activa de su organización determina el comportamiento real.</p></figcaption></figure>

La validación técnica verifica los datos del documento; La aprobación registra la decisión comercial de un revisor autorizado. Incluso una factura técnicamente válida puede requerir una o más aprobaciones.

1. **Verificar responsabilidad:** Abra la factura asignada y verifique qué nivel de aprobación puede decidir.
2. **Revise la factura:** Compare los valores del encabezado, las partidas y los impuestos con el documento original y los requisitos de su empresa.
3. **Decisión de documento:** Aprobar una factura correcta o rechazarla con un motivo específico. Espere la respuesta y luego verifique el historial de aprobación.
4. **Identifique el siguiente paso:** Si se configuran etapas de aprobación adicionales, la factura espera sus decisiones. Después del rechazo, aclaración, corrección y cualquier reenvío, siga el proceso configurado. El proceso de exportación independiente determina si los datos han llegado al sistema de destino.

### Tres afirmaciones que no significan lo mismo

| declaración | Lo que no prueba automáticamente |
| --- | --- |
| **Los datos están validados.** | Que un revisor empresarial autorizado lo haya aprobado. |
| **Un revisor aprobado.** | Que se hayan completado todas las etapas de aprobación requeridas. |
| **Se han completado las aprobaciones.** | Que la factura ya haya sido exportada o contabilizada en ERP. |

Utilice [Tareas de documentos](tasks.md) para procesar el trabajo asignado y [Estado del documento](dashboard/document-status.md) para clasificar el estado actual.

El vídeo muestra la aprobación desde el punto de vista de una revisora.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-approval-customer/v1/es.mp4" %}
Aprobar o rechazar una factura
{% endembed %}

[Ver video con subtítulos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/invoice-approval-customer/v1/es.html)

Se muestra la aplicación real. Los nombres de las opciones pueden variar según la versión utilizada.

Utilice la aprobación para dejar constancia de su decisión tras revisar una factura que ya ha sido validada. Necesita acceso al documento y permiso para su etapa de aprobación actual. El video utiliza una cuenta normal de revisión.

## Revisar y decidir

1. Abra la factura asignada a usted y verifique la etapa de aprobación actual.
2. Compare el número de factura, el proveedor, las fechas y el total con el original. Revise también las líneas de la factura y los impuestos. La validación técnica no reemplaza su revisión del contenido.
3. Registre una nota de revisión clara. Apruebe una factura correcta o rechácela con un motivo específico cuando necesite aclaración. Espere a que se complete la operación.
4. Vuelva a abrir el documento e inspeccione su historial de aprobación. Compruebe que la persona revisora, la hora, la decisión y la nota completa se hayan guardado correctamente.

<figure><img src="../../.gitbook/assets/customer-check-es-ff5f8b65f333.png" alt="Formulario de factura completado en comparación con el original."><figcaption><p>Formulario de factura completado en comparación con el original.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/customer-rejected-es-ff5f8b65f333.png" alt="Rechazo guardado con su motivo."><figcaption><p>Rechazo guardado con su motivo.</p></figcaption></figure>

## Comprobar la siguiente etapa

Cuando se configura una segunda aprobación, su primera aprobación deja la factura esperando a otro revisor autorizado. Aún no está completamente aprobada. Un rechazo necesita aclaración del contenido; la corrección y la nueva presentación siguen su proceso configurado.

Una entrada en el historial de aprobación no prueba que los datos hayan llegado a un sistema ERP. En este ejemplo aislado, el canal de recuperación no tiene un destino ERP externo. El estado técnico `pending_data_fetch`, cuando se muestra, significa que el documento está esperando la recuperación de datos.

## Páginas relacionadas

- [Pantalla de validación](validation-screen/README.md)
- [Tareas de documentos](tasks.md)
