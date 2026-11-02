# Crear su aplicación personalizada en Infor OS



{% embed url="https://youtu.be/TituJ3ljVQA?si=_9VWR1EAhWYjpBRb" %}



{% hint style="warning" %}
Cuando su aplicación personalizada importe la especificación de la API de DocBits, utilice la especificación **Swagger 2.0** (`/openapi-swagger2.json`), no la de OpenAPI 3.0. El swagger-ui más antiguo de Infor OS necesita el dialecto 2.0 para generar correctamente las cargas de archivos; de lo contrario, las cargas fallan con `400 — Missing boundary in multipart`. Consulte [Infor OS con la integración de la API de DocBits](infor-os-with-docbits-api-integration.md) para ver la explicación completa y cómo copiar la URL.
{% endhint %}
