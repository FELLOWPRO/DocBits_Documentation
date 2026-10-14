# Send HTTPS request to

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_1.png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

La tarjeta de flujo de trabajo **"Send HTTPS Request"** permite a los usuarios enviar solicitudes HTTPS a una URL especificada con cabeceras, parámetros y carga de datos personalizables. Esta tarjeta es ideal para integrar API externas o servicios web directamente en el flujo de trabajo.

## Componentes de la tarjeta:

1. **URL**
   * **Descripción:** Especifica el endpoint donde se enviará la solicitud HTTPS.
   * **Detalle:** Introduzca la URL completa de la API o el servicio web con el que conectarse.
2. **Headers**
   * **Descripción:** Define las cabeceras que se incluirán en la solicitud HTTPS.
   * **Detalle:** Proporcione **pares clave-valor** en un **formato JSON válido** para especificar cabeceras como tokens de autenticación o tipos de contenido. Ejemplo: {"Authorization": "Bearer example\_value"}
3. **Method**
   * **Descripción:** Especifica el método HTTP que se utilizará para la solicitud.
   * **Opciones:**
     * **GET:** Obtiene datos del endpoint.
     * **POST:** Envía datos al endpoint para crear o actualizar recursos.
     * **PUT:** Actualiza los recursos existentes en el endpoint.
     * **DELETE:** Elimina recursos del endpoint.
4. **Parameters**
   * **Descripción:** Pares clave-valor que se incluirán en la URL como parámetros de consulta.
   * **Detalle:** Utilícelo para enviar filtros o datos adicionales requeridos por el endpoint en un formato JSON válido. Consulte el ejemplo de Headers.
5. **Data**
   * **Descripción:** El cuerpo de la solicitud HTTPS.
   * **Detalle:** Proporcione la carga en un formato JSON válido. Consulte el ejemplo de Headers.

## Funcionalidad:

* **Evaluación de la condición:** La tarjeta solo envía la solicitud HTTPS si las secciones **"Where"** y **"And"** se evalúan como verdaderas.&#x20;
  * Si cualquiera de las condiciones es falsa, la solicitud no se envía.
* **Ejecución de la solicitud:**
  * Cuando se cumplen las condiciones, el sistema envía la solicitud HTTPS con las configuraciones especificadas.

## Configuración:

1. **Definir la URL:** Introduzca el endpoint donde debe enviarse la solicitud HTTPS.
2. **Establecer las Headers:** Proporcione las cabeceras necesarias como pares clave-valor.
3. **Seleccionar el HTTP Method:** Elija el método adecuado (**GET**, **POST**, **PUT** o **DELETE**) según la acción que se vaya a realizar.
4. **Añadir parámetros:** Especifique los parámetros de consulta requeridos por el endpoint.
5. **Proporcionar la carga de datos:** Introduzca el cuerpo de la solicitud en el formato requerido (p. ej., JSON) si es necesario.
6. **Configurar las condiciones:** Defina las secciones **"Where"** y **"And"** para garantizar que la solicitud se envíe solo cuando se cumplan condiciones específicas.

## Tarjeta de ejemplo:

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_2.png" alt="" width="375"><figcaption></figcaption></figure>

## Conclusión:

La tarjeta de flujo de trabajo **"Send HTTPS Request"** simplifica la integración de API al permitir a los usuarios realizar solicitudes personalizadas a servicios externos directamente desde sus flujos de trabajo. Al automatizar el proceso de envío de solicitudes HTTPS y la gestión de las respuestas, esta tarjeta mejora la flexibilidad y la funcionalidad del flujo de trabajo.
