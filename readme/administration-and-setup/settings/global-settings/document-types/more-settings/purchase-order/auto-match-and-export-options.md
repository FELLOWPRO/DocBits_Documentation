# Opciones de Auto Match & Export

Tres ajustes al final de la tarjeta **Orden de compra** deciden quién ve los accesos directos de la coincidencia de OC y qué documentos pueden exportarse por sí solos después de una coincidencia. Se aplican a un tipo de documento cada vez.

<figure><img src="../../../../../../.gitbook/assets/doc-type-settings-po-options-es.png" alt="La tarjeta Orden de compra de los ajustes del tipo de documento con todas las opciones de OC"><figcaption><p>La tarjeta Orden de compra. Las tres opciones siguientes son las últimas tres filas.</p></figcaption></figure>

## Permitir exportación automática para líneas de orden de compra no coincidentes

La exportación automática después de la coincidencia de OC normalmente requiere un documento **totalmente coincidente**. Cuando este interruptor está activado, también pueden exportarse automáticamente los documentos con el estado **No hay líneas po coincidentes**. Ese estado significa que la orden de compra no tiene líneas con las que pueda emparejarse la factura.

* **Desactivado (por defecto):** solo se exportan automáticamente los documentos totalmente coincidentes.
* **Activado:** se exportan automáticamente los documentos totalmente coincidentes y los documentos sin líneas de OC coincidentes.

El interruptor solo importa cuando los documentos se exportan automáticamente, por ejemplo con [**Auto Export if PO matched 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) o con una tarjeta de exportación de DocFlow. No cambia la forma en que se emparejan las líneas.

## Coincidencia automática y exportación visibles para

La pantalla de coincidencia de OC tiene una acción **Auto Match & Export**. Empareja el documento y lo exporta justo después de la coincidencia. Este ajuste controla quién obtiene la acción:

| Valor | Quién ve la acción |
| ----- | ------------------ |
| **Solo administrador** (por defecto) | Administradores |
| **Todos los usuarios** | Todos los usuarios que pueden abrir la pantalla de coincidencia de OC |

Los administradores siempre ven la acción. El ajuste no activa la función. El módulo [**Auto Export if PO matched 100%**](../../../../document-processing/module/auto-export-if-po-matched-100.md) debe estar activo para la organización.

## Utilice el importe neto de las líneas para el total coincidente visible en

La pantalla de coincidencia de OC puede calcular el **Total coincidente** a partir del **Importe neto** de las líneas de factura coincidentes, en lugar de calcularlo de otra forma. Este ajuste controla quién puede activar ese cálculo:

| Valor | Quién ve el interruptor |
| ----- | ----------------------- |
| **Solo administrador** (por defecto) | Administradores |
| **Todos los usuarios** | Todos los usuarios que pueden abrir la pantalla de coincidencia de OC |

Cuando el interruptor está activado, el Total coincidente usa directamente los valores del Importe neto de las líneas de factura coincidentes.
