# Creare la tua app personalizzata in Infor OS



{% embed url="https://youtu.be/TituJ3ljVQA?si=_9VWR1EAhWYjpBRb" %}



{% hint style="warning" %}
Quando la tua app personalizzata importa la specifica API di DocBits, utilizza la specifica **Swagger 2.0** (`/openapi-swagger2.json`), non quella OpenAPI 3.0. Il swagger-ui più datato di Infor OS richiede il dialetto 2.0 per costruire correttamente i caricamenti di file; in caso contrario i caricamenti falliscono con `400 — Missing boundary in multipart`. Consulta [Infor OS con l'integrazione API di DocBits](infor-os-with-docbits-api-integration.md) per la spiegazione completa e per sapere come copiare l'URL.
{% endhint %}
