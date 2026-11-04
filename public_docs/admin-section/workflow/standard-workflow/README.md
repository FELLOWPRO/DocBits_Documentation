# Flujo de Trabajo Estándar

<figure><img src="../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits Flujo de trabajo Compra Pedido 4"><figcaption></figcaption></figure>

#### Visión general de los componentes del flujo de trabajo:

* **Correo de Factura AP**: El proceso probablemente comienza con una factura recibida por correo electrónico.
* **DocBits**: Esta herramienta podría ser utilizada para tareas iniciales de gestión de documentos, como capturar y digitalizar facturas.
* **Revisión Financiera**: Las facturas pasan por una revisión financiera donde se toman decisiones sobre su validez y precisión.

#### Pasos en el flujo de trabajo:

1. **Revisión Inicial**:
* Las facturas se reciben y se procesan inicialmente utilizando DocBits.
* Luego son revisadas por el equipo financiero para asegurarse de que se eliminen del flujo de trabajo si están completas, o se envíen para un procesamiento adicional.
2. **Facturas con PO vs. sin PO**:
* El flujo de trabajo distingue entre facturas relacionadas con órdenes de compra (PO) y facturas sin PO.
* Las facturas sin PO se envían para aprobación o rechazo basándose en criterios predefinidos como el ID del proveedor, cantidad, precio unitario y número de artículo.
3. **Coincidencias y Descoincidencias**:
* Las facturas se verifican con las recepciones de mercancía para asegurar que los detalles coincidan (como el ID del proveedor y la cantidad).
* Si hay descoincidencias, la factura está sujeta a una revisión adicional y posiblemente a un rechazo.
4. **Revisión Financiera y del Comprador**:
* Para facturas relacionadas con PO, se realiza un proceso detallado de coincidencia que implica una revisión del comprador.
* Pueden ser necesarios ajustes a las órdenes de compra o a las recepciones de mercancía.
5. **Decisiones Finales**:
* Las facturas que pasan todas las verificaciones son aprobadas e integradas en los sistemas financieros para su registro.
* Las facturas rechazadas generan notificaciones, y el comprador puede solicitar una nueva factura.
6. **Integración con Infor IDM & LN+M3**:
* Es probable que las facturas aprobadas se envíen al IDM de Infor para la gestión de documentos y a LN para el registro contable.
* Esta integración asegura que todos los registros financieros estén actualizados y que el flujo de trabajo se integre sin problemas en el sistema ERP más amplio.

#### Puntos de Decisión:

* A lo largo del flujo de trabajo, hay varios puntos de decisión donde una factura puede ser aprobada, rechazada o devuelta para obtener información adicional. Se envían notificaciones después de retrasos, asegurando un procesamiento oportuno.

Estos flujos de trabajo se incluirán en el Flujo de Trabajo Estándar
