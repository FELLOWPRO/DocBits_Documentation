---
description: "P1: Comprobar llamadas API y uso posterior de respuestas"
---

# P1: Comprobar llamadas API y uso posterior de respuestas

**Call API** v2 añade la ruta configurada a la base API de DocBits y usa el contexto organizativo actual. **Send HTTPS Request** v2 utiliza una URL externa y sus propios encabezados. Una URL externa completa no sustituye una ruta de Call API. Ambas tarjetas simulan el envío en Advanced Test.

La acción HTTPS revisada registra estado y texto de respuesta, pero no expone un almacén JSON de nombre libre para las tarjetas siguientes. Call API convierte el texto de respuesta a booleano. HTTP 200, JSON válido y procesamiento posterior correcto necesitan pruebas independientes. No invente sintaxis como `api.response.cost_center`.

Para `{"cost_center":"4711"}` externo, acuerde un mecanismo de escritura o callback expresamente admitido hacia un campo documental. Verifique el campo guardado y léalo en la ejecución posterior prevista. Transferir datos directamente exige una tarjeta o extensión con contrato de salida documentado. JSON en la configuración tampoco demuestra los bytes JSON realmente enviados.

Use un destino propio de prueba y examine método, encabezados, cuerpo real, estado y esquema. Cubra 4xx, 5xx, timeout, JSON inválido y doble evento. Repita escrituras solo tras comprobar la recepción del primer intento. La URL del ejemplo es un marcador reservado y no se ha probado como servicio accesible.

## Tarjetas y parámetros de ejemplo

Los valores describen parámetros de tarjetas, no un workflow completo importable. Sustituya YOUR_* por selecciones propias de prueba. El diseñador gestiona el ID oculto del llamante. Catálogo: Dev, DocFlow 2.10.38, 21 de octubre de 2026; compruebe versiones y permisos de su organización.

### `call_api` · v2

Identidad: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

Identidad: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| Parámetro | Tipo / opciones | Ejemplo |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## Casos de prueba de negocio

| Caso | Entrada / configuración | Resultado esperado |
| --- | --- | --- |
| API-01 | Advanced Test | simulado; sin prueba de entrega |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | compruebe recepción antes de repetir |
| API-04 | {"cost_center":"4711"} | sin api.response.cost_center automático |
| API-05 | POST × 2 | compruebe duplicados en destino |

## Pruebas y límites

Parámetros y comportamiento se contrastaron con el catálogo Dev y el código revisado. Los casos de negocio son instrucciones de aceptación. No se realizaron aprobaciones personales, cambios reales ni entregas para este capítulo.

[Continuar aprendiendo](../workflow-learning-path.md) · [Paquete de formación](../workflow-training-kit.md)
