# Cálculo de IA para recargos por aumento de costos

<figure><img src="../../../../../.gitbook/assets/workflow-card-qa-20261021-card-2dff6d842a5a-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## Cuando usar esta tarjeta

Utilice esta acción para solicitar el cálculo del recargo de material y energía MTZ/ETZ configurado para el documento actual. Primero, prepare los datos del documento y la configuración del servicio de cálculo requeridos por su organización.

## Configuración real

La tarjeta mostrada no tiene entradas de Factor de aumento de costo, Campo de costo base o Campo de recargo. Delega el cálculo al servicio configurado. No busque estos controles de tarjeta inexistentes ni asuma una fórmula de porcentaje fijo a partir del nombre de la tarjeta.

## Resultado y verificación

Una respuesta de servicio exitosa marca que la tarjeta fue exitosa. Un tiempo de espera agotado o una respuesta fallida produce un error de tarjeta. Inspeccionar el registro de la tarjeta y los datos de recargo resultantes del documento; El éxito de la llamada por sí solo no documenta una cantidad particular.

En el modo de prueba de tarjeta, se omite la llamada y se simula el éxito. Esto es útil para probar la estructura del flujo de trabajo, pero no prueba que el servicio se haya ejecutado ni que se haya calculado ningún recargo.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo utilizar:** Solicite el cálculo del recargo de material/energía configurado para una factura preparada.

**Configuración:** Utiliza factura sintética `DEMO-001` con los datos que requiere tu servicio MTZ/ETZ configurado. Agregue esta acción después de las condiciones de validación del documento.

**Resultado esperado y contraejemplo:** Una respuesta de servicio exitosa marca que la tarjeta fue exitosa; un tiempo de espera o una respuesta fallida produce un error de tarjeta. Inspeccione los campos del documento y el resultado del cálculo por separado. El modo de prueba de tarjeta simula el éxito y no llama al servicio, por lo que no puede demostrar un resultado real de recargo.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
