# Créer votre application personnalisée dans Infor OS



{% embed url="https://youtu.be/TituJ3ljVQA?si=_9VWR1EAhWYjpBRb" %}



{% hint style="warning" %}
Lorsque votre application personnalisée importe la spécification de l'API DocBits, utilisez la spécification **Swagger 2.0** (`/openapi-swagger2.json`), et non celle d'OpenAPI 3.0. L'ancien swagger-ui d'Infor OS a besoin du dialecte 2.0 pour construire correctement les envois de fichiers ; sinon, les envois échouent avec `400 — Missing boundary in multipart`. Consultez [Infor OS avec l'intégration de l'API DocBits](infor-os-with-docbits-api-integration.md) pour l'explication complète et la manière de copier l'URL.
{% endhint %}
