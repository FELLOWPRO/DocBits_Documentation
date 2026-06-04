# And

## Comprender las tarjetas "And"

### **Propósito de las tarjetas "And":**

* Las tarjetas **And** funcionan como tarjetas de condición que especifican criterios que deben cumplirse para que el flujo de trabajo continúe. Actúan eficazmente como operadores lógicos "AND", lo que significa que todas las condiciones especificadas en estas tarjetas deben cumplirse para que se dispare la acción posterior.

#### Categorías de tarjetas "And"

A partir de las capturas de pantalla, queda claro que estas tarjetas cubren una amplia gama de condiciones, que incluyen:

* **Compare with Purchase Order**:
  * Condiciones relacionadas con la validación y la comparación frente a órdenes de compra, como comparar fechas de entrega, precios unitarios o diferencias de cantidad. Son cruciales para garantizar que las transacciones se ajusten a los términos acordados.

<figure><img src="../../../.gitbook/assets/image (14) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document Field**:
  * Implican condiciones basadas en campos específicos dentro de los documentos, como casillas de verificación marcadas, comparación de valores de campo o garantizar que un campo de documento cumpla una tolerancia especificada. Esto es especialmente importante para la integridad de los datos y las comprobaciones automatizadas dentro de formularios o sistemas de gestión de documentos.

<figure><img src="../../../.gitbook/assets/image (15) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Date & Time:**
  * Condiciones basadas en fechas y horas.

<figure><img src="../../../.gitbook/assets/image (17) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Document**:
  * Condiciones basadas en características del documento, como el tipo o la asociación con una suborganización concreta. Estas condiciones pueden dirigir los flujos de trabajo en función de la categorización del documento o la participación departamental.

<figure><img src="../../../.gitbook/assets/image (18) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Logic**:
  * Condiciones lógicas que pueden implicar evaluaciones como "Continuar con una probabilidad del X %" o ejecutar solicitudes HTTPS, que son vitales para las integraciones y la toma de decisiones probabilística dentro de los flujos de trabajo.

<figure><img src="../../../.gitbook/assets/image (19) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Status**:
  * Centradas en el estado de los documentos o las tareas, estas condiciones garantizan que solo los elementos en ciertos estados disparen flujos de trabajo específicos, lo que es crucial para la gestión de procesos basada en el estado.

<figure><img src="../../../.gitbook/assets/image (20) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Table**:
  * Implican condiciones basadas en datos de tablas, como la coincidencia de patrones regex o la comparación de valores dentro de una tabla. Estas condiciones son esenciales para validar y manipular grandes conjuntos de datos.

<figure><img src="../../../.gitbook/assets/image (22) (1) (1).png" alt=""><figcaption></figcaption></figure>

* **Assignee**:
  * Condiciones basadas en los asignatarios de tareas o documentos. Esto garantiza que las acciones solo se realicen cuando ciertos usuarios estén implicados, mejorando la responsabilidad y la especificidad de las tareas.

<figure><img src="../../../.gitbook/assets/image (24) (1) (1).png" alt=""><figcaption></figcaption></figure>

### Aplicación práctica

Estas tarjetas "And" se configuran dentro del flujo de trabajo para realizar comprobaciones y validaciones que garantizan que el proceso se ajuste estrictamente a las reglas de negocio y los estándares de integridad de datos. Por ejemplo:

* **Un flujo de trabajo podría usar una tarjeta "And" para verificar que el importe total de una factura coincide con la orden de compra antes de disparar el pago.**
* **Otro flujo de trabajo podría usar una tarjeta "And" para garantizar que un documento sea revisado por miembros específicos del equipo antes de que avance a la siguiente etapa.**

### Conclusión

Las tarjetas "And" son un componente fundamental de los sistemas de flujo de trabajo que requieren un control preciso de la ejecución del proceso en función de múltiples condiciones. Garantizan que cada paso de un flujo de trabajo solo avance cuando se cumplan rigurosamente todos los criterios necesarios, automatizando así árboles de decisión complejos dentro de los procesos de negocio.

Comprender y configurar correctamente estas tarjetas es crucial para aprovechar todas las capacidades de su sistema de gestión de flujos de trabajo y mejorar la eficiencia, la precisión y el cumplimiento dentro de los procesos de la organización.
