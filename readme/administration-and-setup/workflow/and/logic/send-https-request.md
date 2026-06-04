# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de DocBits está diseñada para facilitar la interacción con sistemas externos enviando solicitudes HTTPS a las URL especificadas. Permite que los flujos de trabajo realicen acciones como la obtención, actualización o eliminación de datos mediante llamadas a la API, garantizando una integración fluida con los servicios externos.

## **Funcionalidad:**

* **Ejecución de la solicitud HTTPS:** La tarjeta envía una solicitud a una URL especificada usando el método HTTP configurado (p. ej., GET, POST, PUT, DELETE).
* **Cabeceras y parámetros:** Los usuarios pueden incluir cabeceras personalizadas y parámetros de consulta para garantizar que la solicitud cumpla los requisitos de la API externa.
* **Datos de la solicitud:** Permite a los usuarios definir la carga de datos (si procede) que se enviará con la solicitud, como JSON o datos codificados en formulario.
* **Evaluación de la respuesta:** El flujo de trabajo comprueba si el código de estado recibido coincide con el valor esperado, garantizando una comunicación correcta antes de continuar.
* **Métodos HTTP admitidos:**
  * GET: Obtiene datos de la URL especificada.
  * POST: Envía datos a la URL especificada para crear recursos.
  * PUT: Actualiza los recursos existentes en la URL especificada.
  * DELETE: Elimina recursos de la URL especificada.

## **Uso:**

Esta tarjeta es especialmente útil en escenarios donde los flujos de trabajo necesitan interactuar con API externas para el intercambio de datos, como enviar actualizaciones a un CRM, obtener estados de pedidos o publicar nuevas entradas en una base de datos.

## **Ejemplo de escenario:**

* Un usuario configura la tarjeta para enviar una solicitud POST a un sistema externo de gestión de pedidos con una carga que contiene los detalles de un nuevo pedido. Se añaden cabeceras personalizadas para incluir tokens de autenticación de la API. La tarjeta se configura para continuar solo si el código de estado de la respuesta es 201 (Created). Si el código de estado difiere, el flujo de trabajo dispara una notificación de error para intervención manual.

Al usar la tarjeta "Send HTTPS Request", las organizaciones pueden automatizar las integraciones externas, mejorar la comunicación entre sistemas y agilizar flujos de trabajo complejos.
