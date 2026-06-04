# Standard Workflow

<figure><img src="../../../../.gitbook/assets/docbits_workflow_purchase_order_4.svg" alt="DocBits Flujo de trabajo Compra Pedido 4"><figcaption></figcaption></figure>

#### Resumen de los componentes del flujo de trabajo:

* **AP Invoice Email**: El proceso probablemente comienza con una factura recibida por correo electrónico.
* **DocBits**: Esta herramienta puede utilizarse para las tareas iniciales de gestión de documentos, como la captura y digitalización de facturas.
* **Finance Review**: Las facturas pasan por una revisión financiera en la que se toman decisiones sobre su validez y exactitud.

#### Pasos del flujo de trabajo:

1. **Initial Review**:
   * Las facturas se reciben y se procesan inicialmente con DocBits.
   * Luego son revisadas por el equipo financiero para garantizar que se retiren del flujo de trabajo si están completas, o que avancen para su procesamiento posterior.
2. **PO vs Non-PO Invoices**:
   * El flujo de trabajo distingue entre facturas relacionadas con pedidos de compra (PO) y facturas sin PO.
   * Las facturas sin PO se enrutan para su aprobación o rechazo según criterios predefinidos como el ID del proveedor, la cantidad, el precio unitario y el número de artículo.
3. **Matching and Mismatching**:
   * Las facturas se cotejan con los recibos de mercancías para garantizar que los detalles coincidan (como el ID del proveedor y la cantidad).
   * Si se producen discrepancias, la factura queda sujeta a una revisión adicional y posiblemente al rechazo.
4. **Finance and Buyer Review**:
   * Para las facturas relacionadas con PO, se lleva a cabo un proceso detallado de cotejo que implica una revisión por parte del comprador.
   * Pueden ser necesarios ajustes en los pedidos de compra o en los recibos de mercancías.
5. **Final Decisions**:
   * Las facturas que superan todas las comprobaciones se aprueban y se integran en los sistemas financieros para su registro.
   * Las facturas rechazadas generan notificaciones, y el comprador puede solicitar una nueva factura.
6. **Integration with Infor IDM & LN+M3**:
   * Las facturas aprobadas probablemente se envían a IDM de Infor para la gestión documental y a LN para el registro contable.
   * Esta integración garantiza que todos los registros financieros estén actualizados y que el flujo de trabajo se integre sin problemas en el sistema ERP más amplio.

#### Puntos de decisión:

* A lo largo del flujo de trabajo hay varios puntos de decisión en los que una factura puede aprobarse, rechazarse o devolverse para obtener información adicional. Se envían notificaciones tras los retrasos, garantizando un procesamiento oportuno.

Estos flujos de trabajo se incluirán en el Standard Workflow
