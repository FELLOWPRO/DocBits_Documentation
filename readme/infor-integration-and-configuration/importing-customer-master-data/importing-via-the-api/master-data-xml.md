---
description: Cómo importar datos maestros en un conjunto de datos de búsqueda desde un archivo XML
---

# Importar Datos Maestros desde XML

Además de las importaciones de BOD, DocBits puede leer datos maestros de **cualquier archivo XML** hacia el conjunto de datos de búsqueda que usted elija. Usted le indica en qué conjunto escribir y de qué XPath debe leerse cada columna, así que el XML no tiene por qué seguir ningún formato BOD.

Úselo para datos maestros que no llegan como BOD — listas de precios, centros de coste, atributos de artículo, cualquier cosa que su ERP pueda exportar como XML.

## Dos formas de enviar el XML

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-endpoints.png)

| Endpoint | Cuándo usarlo |
| --- | --- |
| `/master_data_lookup/xml/import_xml_file` | Tiene los datos como **archivo XML** y quiere subirlo. |
| `/master_data_lookup/xml/import_xml_data` | Quiere **pegar el XML** en la petición. A diferencia de los endpoints de BOD, este acepta el XML como texto plano — sin envoltorio JSON. |

Ambos se describen a continuación. Los pasos 1 y 2 son iguales en los dos casos.

## Antes de empezar

Necesitará:

* **Una API key.** Consulte [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md) si aún no tiene una.
* **El XML** — como archivo o como contenido que pueda pegar.
* **Un tipo de datos** — el nombre del conjunto de datos de búsqueda en el que escribir.
* **Asignaciones de campos** — qué XPath rellena qué columna.
* **Su Org ID**, en **Settings → Integration & SSO**, en la sección **ID**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-org-id.png)

## Instrucciones paso a paso

### 1. Abrir el enlace de la API

Abra la interfaz de prueba de la API del entorno y la región con los que esté trabajando:

* [Sandbox API (Europa)](https://eu.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Sandbox API (Estados Unidos)](https://us.sandbox.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Europa)](https://eu.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)
* [Production API (Estados Unidos)](https://us.api.docbits.com/docs#/master%20data%20lookup/import_xml_file_master_data_lookup_xml_import_xml_file_post)

Estos endpoints están bajo **master data lookup** y no bajo **import**, más abajo en la página.

{% hint style="info" %}
Use la región en la que está alojada su organización — la misma región con la que inicia sesión en DocBits. Los entornos europeo y americano están separados, así que una importación enviada a la región equivocada no aparecerá en su organización.
{% endhint %}

### 2. Autorizar

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-lock.png)

Autorizarse funciona exactamente igual que en las importaciones de BOD: haga clic en el **icono del candado**, pegue su **Org ID** en **X-ORG-ID**, pegue su API key en **X-API-KEY** y haga clic en **Authorize** en cada una.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-orgid.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-authorize-apikey.png)

### 3. Rellenar los campos

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-tryitout-xml.png)

Haga clic en **Try it out** y rellene el formulario.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-form.png)

| Campo | |
| --- | --- |
| **data\_type** | Obligatorio. El conjunto de datos de búsqueda en el que escribir. Se pasa a minúsculas automáticamente, así que `PriceList` y `pricelist` son el mismo conjunto. |
| **field\_mappings** | Obligatorio. Un objeto JSON que empareja cada columna con el XPath del que se lee. Véase más abajo. |
| **file** | Obligatorio en `import_xml_file`. Haga clic en **Choose file** y seleccione su XML. |
| **xml** | Obligatorio en `import_xml_data` en lugar del archivo — pegue el XML como texto plano. |
| **org\_id** | Su Org ID — el mismo valor que puso en **X-ORG-ID** en el paso 2. |
| **sub\_org\_id** | Solo hace falta si está importando a una suborganización concreta. |

#### Asignaciones de campos

`field_mappings` es un objeto JSON con una entrada por columna. A diferencia de las importaciones de BOD, donde los nombres están fijados a `custom_field_1` … `custom_field_5`, aquí los elige usted:

```json
{
  "ID": "//Item/ID",
  "Description": "//Item/Description",
  "Price": "//Item/UnitPrice"
}
```

Los nombres de la izquierda se convierten en las columnas del conjunto de datos y son cosa suya. Los valores de la derecha tienen que corresponderse con la estructura del XML que está subiendo — en el ejemplo de arriba, `//Item/ID` recoge el elemento `<ID>` dentro de cada `<Item>`. Los dos lados son independientes: la asignación de arriba lee `<UnitPrice>` hacia una columna llamada `Price`.

{% hint style="warning" %}
Solo se rechazan los XPath **mal formados**, con un `400` que nombra el campo. Un XPath que es válido pero no encuentra nada en su XML pasa en silencio y simplemente deja esa columna vacía — así que una errata en una ruta parece una importación que funcionó pero perdió una columna. Si la ruta que no encuentra nada es la de `ID`, la importación falla en su lugar e informa de que falta la columna `ID` para ese registro.
{% endhint %}

{% hint style="warning" %}
**Una de las columnas tiene que llamarse `ID`.** Es lo que identifica un registro: importar los mismos datos otra vez actualiza la fila con ese ID en lugar de añadir un duplicado. El nombre no distingue mayúsculas de minúsculas, así que `ID`, `Id` e `id` valen todos, pero un nombre como `ItemID` no cuenta — la petición se rechaza con `ID_FIELD_IS_MISSING` y no se escribe nada.
{% endhint %}

{% hint style="warning" %}
**Una petición importa un registro.** Cada XPath se lee una vez, así que si su XML contiene varios elementos solo se usa la primera coincidencia de cada uno. Para cargar una lista, envíe una petición por registro o use una importación CSV en su lugar.
{% endhint %}

#### Elegir un tipo de datos

`data_type` es la clave del conjunto de datos en el que está escribiendo. Se pasa a minúsculas y se recorta, así que `Items` e `items` son el mismo conjunto. Cualquier nombre que no esté ya cogido crea un conjunto propio — `items_example`, `cost_centres`, `price_list` — y volver a importar en él lo actualiza.

{% hint style="danger" %}
Algunos nombres no están libres: son las tablas de datos maestros propias de DocBits, e importar en una de ellas escribe directamente dentro.

| Nombre | |
| --- | --- |
| `purchase_order_header`, `purchase_order_address` | Se rechazan con `RESERVED_DATASET_NAME`. |
| `supplier`, `supplier_accounts`, `purchase_order`, `receive_delivery`, `receive_delivery_lines`, `costing_element`, `customer_erp_items`, `supplier_item_price`, `supplier_item_number_mapping` | **Se aceptan y sobrescriben datos maestros reales.** Úselos solo si es realmente lo que pretende. |

Para cualquier otra cosa, elija un nombre propio.
{% endhint %}

{% hint style="warning" %}
Compruebe a qué entorno y a qué organización está apuntando antes de ejecutar. Una importación escribe directamente en los datos maestros de esa organización.
{% endhint %}

### 4. Ejecutar

Antes de ejecutar, revise el desplegable **Servers** al final del formulario.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-execute.png)

Haga clic en **Execute**. Una importación correcta devuelve:

```json
{
  "success": true,
  "message": "Record(s) created/updated successfully"
}
```

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import-xml-response.png)

A diferencia de las importaciones de BOD, estos endpoints informan de los problemas con un estado de error propiamente dicho en lugar de un `200` que lleva `"success": false` — un **400** significa que la petición se rechazó y no se escribió nada.

### 5. Comprobar que los datos han llegado

* En DocBits, vaya a **Settings → Document Processing → Lookup Master Data**.
* Seleccione **Imported** a la izquierda y abra la pestaña de su tipo de datos.
* Las columnas son los nombres que usó en el lado izquierdo de `field_mappings`.

<!-- SCREENSHOT: Lookup Master Data with Imported selected and the new dataset open -->
