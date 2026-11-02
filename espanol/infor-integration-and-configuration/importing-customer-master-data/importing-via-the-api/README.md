---
description: Enviar datos maestros a DocBits manualmente mediante la API
---

# Importar mediante la API

Los datos maestros normalmente llegan a DocBits automáticamente a través de su flujo de datos ION. Las páginas de esta sección describen cómo enviar los mismos datos manualmente mediante la interfaz de prueba de la API — útil cuando quiere volver a importar un registro, cargar algo que nunca llegó o probar una nueva asignación de campos antes de activar el flujo automático.

Cada página sigue los mismos cinco pasos: abrir el enlace de la API de su entorno, autorizarse con su Org ID y su API key, rellenar el formulario, ejecutar y comprobar que los datos han llegado.

* [Importar Proveedores (Supplier BOD)](supplier-bod.md)
* [Importar Pedidos de Compra (Purchase Order BOD)](purchase-order-bod.md)
* [Importar Entradas de Mercancías (Receive Delivery BOD)](receive-delivery-bod.md)
* [Importar Datos Maestros desde XML](master-data-xml.md)

## Qué necesita

* **Una API key** — consulte [API Key Management](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md).
* **Su Org ID** — en **Settings → Integration & SSO**, en la sección **ID**.
* **Los datos en sí**, como archivo XML o como contenido XML que pueda pegar.

{% hint style="warning" %}
Una importación escribe directamente en los datos maestros de su organización. Compruebe a qué entorno, a qué región y a qué organización está apuntando antes de ejecutar.
{% endhint %}
