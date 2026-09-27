# Infor OS with DocBits API Integration



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## Importing the DocBits API into Infor OS — use the Swagger 2.0 specification

When you connect Infor OS to the DocBits API (for example when creating a custom application or an API flow in Infor OS), Infor imports DocBits's API specification. **For Infor OS, use the Swagger 2.0 specification — not the OpenAPI 3.0 one.**

DocBits publishes its API specification in two dialects:

| Specification | Path | Use it for |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | Standard API clients, SDK generation, the normal API docs |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS** (and any other tool that uses an older swagger-ui) |

{% hint style="warning" %}
**Why Swagger 2.0 for Infor?** Infor OS uses an older version of swagger-ui that cannot build a file-upload request from the modern OpenAPI 3.0 representation (a `requestBody` with `format: binary`). It sends the upload **without a multipart boundary**, and the API rejects it with:

`400 — Missing boundary in multipart`

The Swagger 2.0 specification declares file uploads as `in: formData, type: file`, which Infor's swagger-ui builds correctly (with a boundary). Same endpoints, same data — only the specification dialect differs.
{% endhint %}

### How to get the Swagger 2.0 URL

1. Open the DocBits API documentation in your browser (e.g. `https://api.docbits.com/docs`).
2. At the top of the page, open the **specification dropdown** and select **Swagger 2.0 (Infor OS)**.
3. Copy the URL shown for that specification — it is your DocBits API base URL followed by `/openapi-swagger2.json`.

Use that URL wherever Infor OS asks for the API / Swagger specification. Copying it from the dropdown guarantees the correct host for your region and environment.

{% hint style="info" %}
Everything else about the integration — authentication (API key / token), endpoints and payloads — is unchanged. Only the specification dialect you import into Infor differs.
{% endhint %}
