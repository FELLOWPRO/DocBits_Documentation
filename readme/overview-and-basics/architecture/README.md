# Arquitectura

## **Cliente de DocBits Cloud**

<figure><img src="../../.gitbook/assets/docbits_cloud_customer_architecture.png" alt="Arquitectura del cliente de DocBits Cloud"><figcaption></figcaption></figure>

## DocBits en instalación local

<figure><img src="../../.gitbook/assets/docbits_on_premise_architecture.png" alt="Arquitectura de DocBits On Premise"><figcaption></figcaption></figure>

Doc**Bits** se integra sin problemas con Infor LN/M3 a través de ION API, ION Desk y los BODs estándar de Infor. Nuestra integración API nos permite exportar datos a Infor y realizar la validación de datos maestros en Doc**Bits**.

## **Arquitectura de DocBits Operator**

Todas las conexiones entre componentes están protegidas mediante protocolos de cifrado estándar del sector. SSH, HTTPS y otros canales seguros garantizan la integridad y la confidencialidad de los datos en todo el sistema.

**En la instalación local:**

<figure><img src="../../.gitbook/assets/Operator_On-Prem.png" alt=""><figcaption></figcaption></figure>

{% content-ref url="prefect-local-setup-requirements.md" %}
[prefect-local-setup-requirements.md](prefect-local-setup-requirements.md)
{% endcontent-ref %}

**Cloud**:

<figure><img src="../../.gitbook/assets/Operator Cloud .png" alt=""><figcaption></figcaption></figure>

## Exportación de datos a Infor

Utilizamos la ION API para enviar el PDF con atributos a IDM y el BOD Sync.CaptureDocument a ION Desk. En ION Desk, transformamos el [Sync.CaptureDocument](../../infor-integration-and-configuration/exporting-in-docbits/) en los BODs de destino deseados según el tipo de documento que se esté procesando. Estos BODs de Infor transformados se importan automáticamente a LN o M3.

{% hint style="info" %}
Exportar a [Infor](../../infor-integration-and-configuration/exporting-to-infor/)
{% endhint %}

## Validación de datos maestros en DocBits

Para identificar al proveedor o comparar/igualar líneas de pedidos de compra, activamos un disparador en LN/M3 que envía los BODs Sync.RemitToPartyMaster, Sync.SupplierPartyMaster y Sync.PurchaseOrder a Doc**Bits**. Configuramos este proceso en ION Desk definiendo el flujo de datos hacia un punto de conexión específico de Doc**Bits**.

<figure><img src="../../.gitbook/assets/docbits_architecture (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
[Validación de datos maestros](../../infor-integration-and-configuration/importing-customer-master-data/)
{% endhint %}

## Importación de correo electrónico con OAuth Office365

<figure><img src="../../.gitbook/assets/o365_architecture.png" alt=""><figcaption></figcaption></figure>
