# Create your Custom App in Infor OS



{% embed url="https://youtu.be/TituJ3ljVQA?si=_9VWR1EAhWYjpBRb" %}



{% hint style="warning" %}
When your custom app imports the DocBits API specification, use the **Swagger 2.0** specification (`/openapi-swagger2.json`), not the OpenAPI 3.0 one. Infor OS's older swagger-ui needs the 2.0 dialect to build file uploads correctly — otherwise uploads fail with `400 — Missing boundary in multipart`. See [Infor OS with DocBits API Integration](infor-os-with-docbits-api-integration.md) for the full explanation and how to copy the URL.
{% endhint %}
