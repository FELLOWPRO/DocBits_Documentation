# Patrón de integración API

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-card-6a1c780ee588-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

<!-- workflow-card-api-pattern-contract-20261022 -->

Este patrón utiliza la tarjeta real de la API DocBits descrita a continuación. No proporciona un flujo externo importable, mapeo automático de respuestas JSON ni un motor integrado de reintentos o caché. Los servicios externos requieren una configuración HTTPS independiente y verificada.

## Finalidad

Use `call_api` para llamar a un endpoint de la API de DocBits configurada. El endpoint es una ruta relativa que se añade a su dirección base. Una URL externa arbitraria no configura una integración con otra API.

## Configuración

Introduzca la ruta, el método HTTP, los parámetros de consulta y los datos admitidos por el endpoint. La petición utiliza el contexto del usuario actual de DocBits. Los valores ausentes de `org_id` y `triggered_by_docflow` se añaden automáticamente. Los objetos de parámetros y datos, o su representación textual admitida, deben respetar el formato de esta versión. No existe una asignación general de campos de respuesta JSON.

## Resultado y límites

El texto de respuesta se convierte en un booleano: `true`, `1`, `yes` u `on` sin contenido adicional producen verdadero; una respuesta no reconocida, incluido un objeto JSON arbitrario, produce falso por defecto. El estado HTTP por sí solo no determina el booleano. Un tiempo de espera agotado o un error de petición produce falso. La prueba de tarjeta simula la llamada y devuelve verdadero sin enviar la petición; no demuestra autenticación, conectividad ni comportamiento del endpoint.



## Ejemplo práctico

Utilice esta tarjeta después de las condiciones necesarias cuando necesite un booleano de un endpoint configurado de la API de DocBits. Para una prueba aislada, seleccione un endpoint existente, documentado y de solo lectura con el contrato de respuesta booleano adecuado y el método correspondiente, por ejemplo `GET`. Use únicamente los parámetros de demostración admitidos.

Resultado esperado y contraejemplo: una respuesta HTTP `200` hipotética cuyo texto completo sea `true` produce verdadero; `false` produce falso. Un objeto como `{"approved": true}` no se convierte automáticamente en verdadero. Compruebe por separado la respuesta real y los registros. Ejemplo revisado contra el código de ejecución; no se ejecutó ninguna petición ni flujo.

## Referencia

[Llamar a la API de DocBits](../then/action/call-api-guide.md)
