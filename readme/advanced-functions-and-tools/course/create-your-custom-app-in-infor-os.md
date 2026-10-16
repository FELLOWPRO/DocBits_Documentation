# 在 Infor OS 中创建自定义应用



{% embed url="https://youtu.be/TituJ3ljVQA?si=_9VWR1EAhWYjpBRb" %}



{% hint style="warning" %}
自定义应用导入 DocBits API 规范时，请使用 **Swagger 2.0** 规范（`/openapi-swagger2.json`），而不要使用 OpenAPI 3.0 规范。Infor OS 使用的旧版 swagger-ui 需要 2.0 方言才能正确构建文件上传请求，否则上传会失败并显示 `400 — Missing boundary in multipart`。完整说明及 URL 的复制方法请参阅 [Infor OS 与 DocBits API 集成](infor-os-with-docbits-api-integration.md)。
{% endhint %}
