# Exportación automática con coincidencia del PO del 100%

### Descripción

La opción **Auto Export if PO matched 100%**, en el módulo de pedidos de compra (PO), permite que una coincidencia completa con el PO habilite el avance de la factura o documento actual hacia la exportación automática. El pedido de compra es la referencia de comparación; esta opción no exporta el propio pedido.

### Funcionamiento

Al activarla, se comprueba el resultado de la conciliación del documento actual con el PO. Una coincidencia del 100% cumple esta condición de conciliación, pero no garantiza una exportación inmediata. La validación del documento, el flujo de exportación configurado, las aprobaciones necesarias y las tareas pendientes aún pueden bloquear o retrasar la exportación. Si la coincidencia es incompleta, esta condición bloquea la exportación automática.

### Ventajas

* **Eficiencia:** Puede reducir la intervención manual en facturas que coincidan completamente con su PO y cumplan los demás requisitos.
* **Control:** Añade el resultado de la conciliación con el PO como condición de exportación.
* **Tiempo de procesamiento:** Puede agilizar las facturas aptas; el momento de exportación depende del resto del flujo.

### Uso

1. **Activar la función:**
   * Vaya a **Configuración** → **Procesamiento de documentos** → **Módulo** → **Pedido de compra**.
   * Active el control **Auto Export if PO matched 100%**.

<figure><img src="../../../../.gitbook/assets/100%PO.png" alt=""><figcaption></figcaption></figure>

2. **Supervisar el procesamiento:**
   * Revise los estados de conciliación, validación y exportación de la factura actual.
   * Si no se exporta pese a una coincidencia del 100%, revise la configuración de exportación, las aprobaciones y las tareas pendientes.
3. **Revisar la configuración:**
   * Compruebe que los criterios de conciliación y exportación reflejen el flujo previsto.
   * Revise periódicamente las facturas exportadas y las excepciones.

### Cuándo utilizarla

* **Grandes volúmenes de facturas:** Cuando muchas facturas puedan conciliarse de forma fiable con pedidos de compra.
* **Compras habituales:** Cuando las cantidades, los precios y los demás criterios sean estables.
* **Procesos urgentes:** Cuando las facturas aptas deban avanzar automáticamente una vez cumplidas todas las condiciones.

Cuando la conciliación con pedidos está activa para el tipo de documento, la opción independiente `ALLOW_AUTO_EXPORT_FOR_NON_MATCHABLE_PO_LINES` también permite el estado `NO_MATCHABLE_PO_LINES`. No autoriza de forma general otros estados de conciliación incompleta.
