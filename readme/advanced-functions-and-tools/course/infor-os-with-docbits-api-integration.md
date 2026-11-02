# Infor OS con la integración de la API de DocBits



{% embed url="https://youtu.be/0aeSDWi9cV8" %}



## Importar la API de DocBits en Infor OS: utilice la especificación Swagger 2.0

Cuando conecta Infor OS con la API de DocBits (por ejemplo, al crear una aplicación personalizada o un flujo de API en Infor OS), Infor importa la especificación de la API de DocBits. **Para Infor OS, utilice la especificación Swagger 2.0, no la de OpenAPI 3.0.**

DocBits publica su especificación de API en dos dialectos:

| Especificación | Ruta | Para qué sirve |
| --- | --- | --- |
| OpenAPI 3.0 / 3.1 | `/openapi.json` | Clientes de API estándar, generación de SDK, la documentación normal de la API |
| **Swagger 2.0** | `/openapi-swagger2.json` | **Infor OS** (y cualquier otra herramienta que utilice un swagger-ui más antiguo) |

{% hint style="warning" %}
**¿Por qué Swagger 2.0 para Infor?** Infor OS utiliza una versión antigua de swagger-ui que no puede generar una solicitud de carga de archivos a partir de la representación moderna de OpenAPI 3.0 (un `requestBody` con `format: binary`). Envía la carga **sin un límite multipart (boundary)** y la API la rechaza con:

`400 — Missing boundary in multipart`

La especificación Swagger 2.0 declara las cargas de archivos como `in: formData, type: file`, que el swagger-ui de Infor genera correctamente (con boundary). Los mismos endpoints y los mismos datos; solo cambia el dialecto de la especificación.
{% endhint %}

### Cómo obtener la URL de Swagger 2.0

1. Abra la documentación de la API de DocBits en su navegador (por ejemplo, `https://api.docbits.com/docs`).
2. En la parte superior de la página, abra el **desplegable de especificaciones** y seleccione **Swagger 2.0 (Infor OS)**.
3. Copie la URL que se muestra para esa especificación: es la URL base de su API de DocBits seguida de `/openapi-swagger2.json`.

Utilice esa URL siempre que Infor OS solicite la especificación de la API o de Swagger. Copiarla desde el desplegable garantiza el host correcto para su región y su entorno.

{% hint style="info" %}
Todo lo demás de la integración (autenticación con clave de API o token, endpoints y payloads) no cambia. Solo cambia el dialecto de la especificación que importa en Infor.
{% endhint %}
