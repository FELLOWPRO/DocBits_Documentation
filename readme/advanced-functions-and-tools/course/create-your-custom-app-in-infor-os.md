# Crie seu Aplicativo Personalizado no Infor OS



{% embed url="https://youtu.be/TituJ3ljVQA?si=_9VWR1EAhWYjpBRb" %}



{% hint style="warning" %}
Quando o seu aplicativo personalizado importar a especificação da API do DocBits, use a especificação **Swagger 2.0** (`/openapi-swagger2.json`), e não a OpenAPI 3.0. O swagger-ui mais antigo do Infor OS precisa do dialeto 2.0 para montar corretamente os uploads de arquivos — caso contrário, os uploads falham com `400 — Missing boundary in multipart`. Veja [Integração da API DocBits com Infor OS](infor-os-with-docbits-api-integration.md) para a explicação completa e como copiar a URL.
{% endhint %}
