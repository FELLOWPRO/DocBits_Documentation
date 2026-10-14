# Búsqueda de datos maestros

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}

La **Búsqueda de datos maestros** (barra lateral: **Lookup Master Data**) le permite ver y gestionar los datos maestros que DocBits utiliza para validar los datos extraídos de los documentos frente a su sistema ERP. Es esencial para un PO matching preciso, la validación de proveedores y el autocompletado de campos. Ábrala desde **Configuración → Procesamiento de documentos → Lookup Master Data**.

<figure><img src="../../../.gitbook/assets/master_data_lookup_overview.png" alt="Búsqueda de datos maestros"><figcaption><p>Página de Búsqueda de datos maestros: fuentes de datos y la tabla de datos</p></figcaption></figure>

## Fuentes de datos

El panel izquierdo enumera cuatro categorías de fuentes de datos:

| Fuente | Descripción |
|--------|-------------|
| **BOD Input Data** | Datos recibidos a través de mensajes Infor BOD (Business Object Document). |
| **ERP API Data** | Datos obtenidos directamente de su sistema ERP mediante API. Haga clic en el icono de engranaje para configurar la conexión API. |
| **Imported** | Datos importados manualmente (por ejemplo, mediante carga de CSV). Haga clic en el icono **+** para añadir nuevos datos. |
| **DocBits Master Data** | Datos maestros internos gestionados dentro de DocBits. |

## Tabla de datos

Al seleccionar una fuente de datos, sus datos se abren en una tabla con búsqueda y ordenación a la derecha:

* **Pestañas**: cada pestaña es un tipo de dato maestro (por ejemplo, Proveedor, Orden de compra, Artículo).
* **Búsqueda**: filtre por columna (**Search by column**) o busque por texto (**Search String**).
* **Acciones**: actualizar etiquetas de columnas, ocultar columnas vacías, actualizar alias o descargar los datos como CSV.
* **Paginación**: navegue por grandes conjuntos de datos con los controles de página.

Las tablas de Proveedor y Orden de compra incluyen columnas como ID de proveedor, Nombre del proveedor, Dirección, Bank Id, Número de PO, ID de artículo, Descripción, Cantidad, Precio unitario, Importe total, Moneda y Estado, además de los campos personalizados.

## Configuración

Haga clic en **Settings** (icono de engranaje) en la parte inferior izquierda del panel de fuentes de datos para abrir la configuración de datos maestros.

<figure><img src="../../../.gitbook/assets/master_data_lookup_settings.png" alt="Configuración de la Búsqueda de datos maestros"><figcaption><p>Configuración de Supplier BOD y eliminación de órdenes de compra</p></figcaption></figure>

### Supplier BOD

**Allow Multiple Supplier Accounts Sync**

* **Activado**: un único proveedor puede tener varios elementos `<FinancialParty>` en el BOD (a menudo debido a varios IBAN o cuentas financieras). Todas las entradas `<FinancialParty>` se extraen y se guardan en la tabla de proveedores, de modo que se pueden almacenar varios atributos financieros.
* **Desactivado**: solo se extrae el último elemento `<FinancialParty>` encontrado para el proveedor. Los atributos financieros anteriores (por ejemplo, IBAN adicionales) se ignoran y solo se guardan los datos de la última aparición.

### Purchase Order Deletion Assistant

**Delete Purchase Order After**: elija cuándo deben eliminarse las órdenes de compra cerradas. Tras el período seleccionado, los registros se eliminan automáticamente.

{% hint style="info" %}
Para saber cómo cargar datos maestros en DocBits, consulte [Importar datos maestros](../../../infor-integration-and-configuration/importing-customer-master-data/).
{% endhint %}
