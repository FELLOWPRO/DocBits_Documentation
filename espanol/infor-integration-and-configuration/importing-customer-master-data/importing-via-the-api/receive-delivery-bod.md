---
description: Cómo importar un Receive Delivery BOD en DocBits manualmente mediante la API
---

# Importar Entradas de Mercancías (Receive Delivery BOD)

Las entradas de mercancías normalmente llegan a DocBits automáticamente a través de su flujo de datos ION. Esta página describe cómo enviar un **Receive Delivery BOD** manualmente — útil cuando quiere volver a importar una entrada, cargar un lote que nunca llegó o probar una asignación de campos antes de activar el flujo automático.

## Dos formas de enviar el mismo BOD

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-endpoints.png)

| Endpoint | Cuándo usarlo |
| --- | --- |
| `/import/receive_delivery_bod` | Tiene el BOD como **archivo XML** y quiere subirlo. |
| `/import/receive_delivery_bod_xml` | Quiere enviar el **contenido XML** en la petición en lugar de un archivo. El BOD hay que envolverlo en JSON, así que esto encaja con XML corto o con otro sistema que llame a la API — para un BOD completo a mano, suba el archivo. |

Ambos se describen a continuación. Los pasos 1 y 2 son iguales en los dos casos.

## Antes de empezar

Necesitará:

* **Una API key.** Consulte [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) si aún no tiene una.
* **El BOD** — un archivo XML `SyncReceiveDelivery`, o su contenido.
* **Su Org ID**, en **Settings → Integration & SSO**, en la sección **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

{% hint style="info" %}
**Sub Org ID** muestra la suborganización que esté seleccionada en la cabecera. Con **CROSS** seleccionado — la vista de todas las suborganizaciones — muestra el mismo valor que **Org ID**. Cambie primero a una suborganización concreta si necesita su ID.

Si no está importando a una suborganización concreta, deje vacío el campo `sub_org_id`.
{% endhint %}

## Instrucciones paso a paso

### 1. Abrir el enlace de la API

Abra la interfaz de prueba de la API del entorno y la región con los que esté trabajando:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Sandbox API (Estados Unidos)](https://us.sandbox.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)
* [Production API (Estados Unidos)](https://us.api.docbits.com/docs#/import/import_receive_delivery_bod_import_receive_delivery_bod_post)

Despliegue el endpoint que quiera haciendo clic en él.

{% hint style="info" %}
Use la región en la que está alojada su organización — la misma región con la que inicia sesión en DocBits. Los entornos europeo y americano están separados, así que una importación enviada a la región equivocada no aparecerá en su organización.

Las direcciones sin prefijo de región — `api.docbits.com` y `sandbox.api.docbits.com` — apuntan a Europa. Las verá en documentación antigua y en configuraciones existentes; son el mismo entorno que las direcciones `eu.` de arriba.
{% endhint %}

### 2. Autorizar

Todo lo que hay bajo **import** está bloqueado hasta que se autorice. Hay dos cosas que rellenar: su organización y su API key.

* Haga clic en el **icono del candado** a la derecha del endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-lock.png)

* Se abre el diálogo **Available authorizations** con dos entradas.
* Pegue su **Org ID** en **X-ORG-ID** y haga clic en **Authorize**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid-done.png)

* Baje hasta **X-API-KEY**, pegue su API key y haga clic en **Authorize**. En DocBits la encontrará en **Settings → Integration & SSO**, en la sección **API Key**, o puede [crear una clave nueva](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md#crear-una-clave-api).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey-done.png)

* Haga clic en **Close**.

{% hint style="info" %}
Pegue la clave sola — no escriba `Bearer` delante. Ambas autorizaciones siguen puestas hasta que recargue la página o haga clic en **Logout**.
{% endhint %}

### 3. Rellenar los campos

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-rd.png)

Haga clic en **Try it out** y rellene el formulario del endpoint que haya elegido.

#### Subir un archivo — `/import/receive_delivery_bod`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-form.png)

| Campo | |
| --- | --- |
| **file** | Obligatorio. Haga clic en **Choose file** y seleccione su archivo XML `SyncReceiveDelivery`. |
| **org\_id** | Su Org ID — el mismo valor que puso en **X-ORG-ID** en el paso 2. Ponerlo también aquí hace explícito en qué organización escribe la petición. Tiene que ser una organización a la que su API key tenga acceso; cualquier otra se rechaza. |
| **sub\_org\_id** | Solo hace falta si está importando a una suborganización concreta. |
| **custom\_fields\_mapping** | Opcional. Campos de cabecera adicionales. Consulte [Asignaciones de campos personalizados](#asignaciones-de-campos-personalizados) más abajo. |
| **custom\_line\_fields\_mapping** | Opcional. Lo mismo, para campos adicionales en las líneas de la entrada. |
| **populate\_additional\_info** | Opcional, `false` por defecto. Póngalo a `true` para que DocBits recupere información adicional de la entrada desde el ERP después de la importación. Déjelo en `false` salvo que sepa que lo necesita — hace la importación más lenta. |

{% hint style="warning" %}
**`string` es un valor, no un marcador de posición.** Swagger rellena los campos opcionales con la palabra `string`, y se envía tal cual si la deja ahí — una importación con `org_id` puesto a `string` fallará.

Para cada campo opcional que no quiera usar, vacíe el campo. Vaciarlo habilita la casilla **Send empty value** de debajo, que entonces puede marcar.
{% endhint %}

#### Asignaciones de campos personalizados

Los dos campos de asignación aceptan un objeto JSON. El **nombre de la izquierda tiene que ser uno de los campos personalizados propios de DocBits** — de `custom_field_1` a `custom_field_10` para entradas de mercancías, el doble de los que permiten los pedidos de compra. Cualquier otro nombre se ignora sin avisar, así que una errata aquí se ve exactamente igual que una asignación que no funcionó.

El valor de la derecha es el XPath del que se lee. Escríbalo sin prefijos de espacio de nombres — DocBits los añade por su cuenta:

```json
{"custom_field_2": "//ReceiveDelivery/ReceiveDeliveryHeader/UserArea/Property/NameValue[@name='User defined 6']/text()"}
```

Las asignaciones de línea usan los mismos nombres `custom_field_1` … `custom_field_10`, pero sus XPath se leen **de forma relativa a cada línea de la entrada**, así que empiezan por `./`:

```json
{"custom_field_1": "./UserArea/Property/NameValue[@name='User defined 1']/text()"}
```

#### Pegar el XML — `/import/receive_delivery_bod_xml`

<!-- SCREENSHOT: the Try it out form of /import/receive_delivery_bod_xml -->

Este endpoint no acepta el BOD como un pegado simple. El campo **xml** es un objeto, precargado con `{"xml": "string"}`. Sustituya `string` por el contenido de su BOD, manteniendo las comillas y las llaves que lo rodean:

```json
{
  "xml": "<SyncReceiveDelivery ...>...</SyncReceiveDelivery>"
}
```

{% hint style="warning" %}
El BOD va dentro de una cadena JSON, así que cada comilla doble del XML tiene que escaparse como `\"` — y un BOD está lleno de ellas. Si el resultado no es JSON válido, la petición falla con un **422** y no se importa nada.

Para un BOD real eso es engorroso de hacer a mano, así que es preferible **subir el archivo**.
{% endhint %}

Este endpoint acepta `org_id`, `sub_org_id` y `populate_additional_info`, pero **ninguna asignación de campos** — ni de cabecera ni de línea. Si sus entradas necesitan campos personalizados, suba el archivo en su lugar.

{% hint style="warning" %}
Compruebe a qué entorno y a qué organización está apuntando antes de ejecutar. Una importación escribe directamente en los datos maestros de esa organización.
{% endhint %}

### 4. Ejecutar

Antes de ejecutar, revise el desplegable **Servers** al final del formulario. Decide a qué entorno se envía realmente la petición, y puede diferir de la página que abrió.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-execute.png)

Haga clic en **Execute**. Una importación correcta devuelve:

```json
{
  "success": true,
  "message": "BOD processed successfully."
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-rd-response.png)

Los receive delivery BOD se procesan mientras espera, así que cuando vea este mensaje los datos ya están dentro.

Si algo no estaba bien en la petición, obtiene `"success": false` junto con un mensaje que describe el problema.

### 5. Comprobar que los datos han llegado

* En DocBits, vaya a **Settings → Document Processing → Lookup Master Data**.
* Seleccione **BOD Input Data** a la izquierda y abra la pestaña de los datos que ha importado.
* Busque la entrada de mercancías o el pedido de compra al que pertenece.

<!-- SCREENSHOT: Lookup Master Data with BOD Input Data selected and the goods receipt data shown -->

{% hint style="info" %}
DocBits decide qué hacer con el BOD leyendo el tipo que lleva dentro, no por el endpoint de importación que haya usado. Si envía aquí un BOD distinto por error, se importa como ese tipo en lugar de rechazarse — así que compruebe que la pestaña en la que encuentra los datos es la que esperaba.
{% endhint %}
