---
description: Cómo importar un Purchase Order BOD en DocBits manualmente mediante la API
---

# Importar Pedidos de Compra (Purchase Order BOD)

Los pedidos de compra normalmente llegan a DocBits automáticamente a través de su flujo de datos ION. Esta página describe cómo enviar un **Purchase Order BOD** manualmente — útil cuando quiere volver a importar un pedido, cargar un lote que nunca llegó o probar una asignación nueva antes de activar el flujo automático.

## Dos formas de enviar el mismo BOD

Hay dos endpoints y hacen lo mismo. La única diferencia está en cómo entrega el BOD:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-endpoints.png)

| Endpoint | Cuándo usarlo |
| --- | --- |
| `/import/purchase_order_bod` | Tiene el BOD como **archivo XML** y quiere subirlo. |
| `/import/purchase_order_bod_xml` | Quiere enviar el **contenido XML** en la petición en lugar de un archivo. El BOD hay que envolverlo en JSON, así que esto encaja con XML corto o con otro sistema que llame a la API — para un BOD completo a mano, suba el archivo. |

Ambos se describen a continuación. Los pasos 1 y 2 son iguales en los dos casos.

## Antes de empezar

Necesitará:

* **Una API key.** Consulte [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) si aún no tiene una.
* **El BOD** — un archivo XML `SyncPurchaseOrder`, o su contenido.
* **Su Org ID**, si está importando a una organización distinta de aquella a la que pertenece su clave.

Para encontrar el Org ID, vaya a **Settings → Integration & SSO** y abra la sección **ID**. Haga clic en el icono de copiar junto al campo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** muestra la suborganización que esté seleccionada en la cabecera. Con **CROSS** seleccionado — la vista de todas las suborganizaciones — muestra el mismo valor que **Org ID**, que es la razón por la que los dos campos coinciden en la captura de arriba. Cambie primero a una suborganización concreta si necesita su ID.

Si no está importando a una suborganización concreta, deje vacío el campo `sub_org_id`.
{% endhint %}

## Instrucciones paso a paso

### 1. Abrir el enlace de la API

Abra la interfaz de prueba de la API del entorno y la región con los que esté trabajando:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Sandbox API (Estados Unidos)](https://us.sandbox.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)
* [Production API (Estados Unidos)](https://us.api.docbits.com/docs#/import/import_purchase_order_bod_import_purchase_order_bod_post)

Despliegue el endpoint que quiera haciendo clic en él.

{% hint style="info" %}
Use la región en la que está alojada su organización — la misma región con la que inicia sesión en DocBits. Los entornos europeo y americano están separados, así que una importación enviada a la región equivocada no aparecerá en su organización.

Las direcciones sin prefijo de región — `api.docbits.com` y `sandbox.api.docbits.com` — apuntan a Europa. Las verá en documentación antigua y en configuraciones existentes; son el mismo entorno que las direcciones `eu.` de arriba.
{% endhint %}

### 2. Autorizar

Todo lo que hay bajo **import** está bloqueado hasta que se autorice. Hay dos cosas que rellenar: su organización y su API key.

* Haga clic en el **icono del candado** a la derecha del endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-swagger-lock.png)

* Se abre el diálogo **Available authorizations** con dos entradas.
* Pegue su **Org ID** en **X-ORG-ID** y haga clic en **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

* La entrada muestra ahora **Authorized** y oculta el valor.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Baje hasta **X-API-KEY**, pegue su API key y haga clic en **Authorize**. En DocBits la encontrará en **Settings → Integration & SSO**, en la sección **API Key**, o puede [crear una clave nueva](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#crear-una-clave-api).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Haga clic en **Close**.

{% hint style="info" %}
Pegue la clave sola — no escriba `Bearer` delante. Ambas autorizaciones siguen puestas hasta que recargue la página o haga clic en **Logout**.
{% endhint %}

### 3. Rellenar los campos

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-po.png)

Haga clic en **Try it out** y rellene el formulario del endpoint que haya elegido.

#### Subir un archivo — `/import/purchase_order_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-form.png)

| Campo | |
| --- | --- |
| **file** | Obligatorio. Haga clic en **Choose file** y seleccione su archivo XML `SyncPurchaseOrder`. |
| **org\_id** | Su Org ID — el mismo valor que puso en **X-ORG-ID** en el paso 2. Ponerlo también aquí hace explícito en qué organización escribe la petición. Tiene que ser una organización a la que su API key tenga acceso; cualquier otra se rechaza. |
| **sub\_org\_id** | Solo hace falta si trabaja con suborganizaciones. Si no, déjelo vacío. |
| **custom\_fields\_mapping** | Opcional. Lee campos de cabecera adicionales del BOD hacia los campos personalizados del pedido. Consulte [Asignaciones de campos personalizados](#asignaciones-de-campos-personalizados) más abajo. |
| **custom\_line\_fields\_mapping** | Opcional. Lo mismo, para campos adicionales en las líneas del pedido. |

{% hint style="warning" %}
**`string` es un valor, no un marcador de posición.** Swagger rellena los campos opcionales con la palabra `string`, y se envía tal cual si la deja ahí — una importación con `org_id` puesto a `string` fallará.

Para cada campo opcional que no quiera usar, vacíe el campo. Vaciarlo habilita la casilla **Send empty value** de debajo, que entonces puede marcar. En la captura de arriba esto se ha hecho con `sub_org_id`.
{% endhint %}

#### Asignaciones de campos personalizados

Los dos campos de asignación aceptan un objeto JSON. El **nombre de la izquierda tiene que ser uno de los campos personalizados propios de DocBits** — de `custom_field_1` a `custom_field_5` para pedidos de compra. Cualquier otro nombre se ignora sin avisar, así que una errata aquí se ve exactamente igual que una asignación que no funcionó.

El valor de la derecha es el XPath del que se lee. Escríbalo sin prefijos de espacio de nombres — DocBits los añade por su cuenta:

```json
{"custom_field_2": "//PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

Las asignaciones de línea usan los mismos nombres `custom_field_1` … `custom_field_5`, pero sus XPath se leen **de forma relativa a cada línea del pedido**, así que empiezan por `./`:

```json
{"custom_field_1": "./UserArea/Property/NameValue[@name='User defined 1']/text()"}
```

#### Pegar el XML — `/import/purchase_order_bod_xml`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-po-bod-xml-form.png)

Este endpoint no acepta el BOD como un pegado simple. El campo **xml** es un objeto, precargado con:

```json
{
  "xml": "string"
}
```

Sustituya `string` por el contenido de su BOD, manteniendo las comillas y las llaves que lo rodean:

```json
{
  "xml": "<SyncPurchaseOrder ...>...</SyncPurchaseOrder>"
}
```

{% hint style="warning" %}
El BOD va dentro de una cadena JSON, así que cada comilla doble del XML tiene que escaparse como `\"` — y un BOD está lleno de ellas (`releaseID="9.2"`, `xmlns="..."`). Si el resultado no es JSON válido, la petición falla con un **422** y no se importa nada.

Para un BOD real eso es engorroso de hacer a mano, así que es preferible **subir el archivo**. Este endpoint es la mejor opción cuando el XML es corto, o cuando otro sistema construye la petición y puede codificar el JSON por su cuenta.
{% endhint %}

Los campos `org_id`, `sub_org_id` y `custom_fields_mapping` funcionan exactamente igual que arriba. Este endpoint no tiene campo para asignaciones de línea.

{% hint style="warning" %}
Compruebe a qué entorno y a qué organización está apuntando antes de ejecutar. Una importación escribe directamente en los datos maestros de esa organización.
{% endhint %}

### 4. Ejecutar

Antes de ejecutar, revise el desplegable **Servers** al final del formulario. Decide a qué entorno se envía realmente la petición, y puede diferir de la página que abrió.

Haga clic en **Execute**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

**Si ha subido un archivo**, la respuesta es:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-response.png)

```json
{
  "success": true,
  "message": "BOD processing started in the background."
}
```

{% hint style="info" %}
**Esto significa que el archivo se aceptó, no que la importación haya terminado.** Los archivos de pedidos de compra subidos se procesan en segundo plano para que los pedidos grandes no bloqueen el resto del sistema. Espere un momento y compruebe el resultado como se describe abajo.
{% endhint %}

**Si ha pegado el XML**, la importación se ejecuta de inmediato y la respuesta es `"BOD processed successfully."` — cuando la vea, los datos ya están dentro.

Si algo no estaba bien en la petición, obtiene `"success": false` junto con un mensaje que describe el problema. Las causas más habituales son contenido que no es un BOD `SyncPurchaseOrder` y un Org ID al que su API key no tiene acceso.

### 5. Comprobar que los datos han llegado

* En DocBits, vaya a **Settings → Document Processing → Lookup Master Data**.
* Seleccione **BOD Input Data** a la izquierda y abra la pestaña **Purchase Order**.
* Busque el número de pedido de su BOD.

<!-- SCREENSHOT F: Lookup Master Data with BOD Input Data selected and the Purchase Order tab open -->

Si el pedido aparece en la lista, la importación funcionó y el pedido de compra está disponible para el PO matching.

{% hint style="info" %}
DocBits decide qué hacer con el BOD leyendo el tipo que lleva dentro, no por el endpoint de importación que haya usado. Si envía aquí un supplier BOD por error, se importa como datos de proveedor en lugar de rechazarse — así que compruebe que la pestaña en la que encuentra los datos es la que esperaba.
{% endhint %}
