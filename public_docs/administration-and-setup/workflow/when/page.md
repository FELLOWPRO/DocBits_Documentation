# Operación de Tipo de Documento

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v1-es-es.png" alt="Operación de Tipo de Documento, Versión 1" width="634"><figcaption><p>Versión 1</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/workflow_card_condition_doc_type_is_isnot_v2-es-es.png" alt="Operación de Tipo de Documento, Versión 2" width="634"><figcaption><p>Versión 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/es.mp4" %}

**Vídeo:** Tarjeta: Tipo de documento es / no es · 0:30 · [Subtítulos (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/es.vtt)

<details>

<summary>Transcripción</summary>

**Tipo de documento es / no es** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/es.mp4#t=0.25)

La tarjeta Tipo de documento comprueba el tipo de un documento. Elija Es o No es y luego el tipo, por ejemplo Factura. No es coincide con todos los tipos salvo el elegido.

**Ejemplo: solo facturas** · [0:17](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-type/v1/es.mp4#t=17.183)

Por ejemplo, un Workflow solo para facturas: Tipo de documento es Factura como tarjeta Cuando y luego una tarjeta de asignación. Para notas de crédito, presupuestos o pedidos, este Workflow no se inicia.

</details>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada específicamente para realizar operaciones predefinidas en documentos categorizados por tipo. Simplifica el manejo de diversas formas de documentos dentro de un sistema ERP, asegurando que cada tipo se procese de acuerdo con sus requisitos únicos y políticas organizativas.

## **Funcionalidad:**

* **Validación de Tipo de Documento**: Esta tarjeta verifica si un documento coincide con un tipo particular, permitiendo a los usuarios confirmar su categorización.
* **Operador**: Los usuarios pueden establecer condiciones para determinar el tipo de documento. Los operadores disponibles incluyen:
  * **Es**: Confirma que el documento coincide con el tipo de documento especificado.
  * **No es**: Asegura que el documento no coincide con el tipo de documento especificado.
* **Tipos de Documentos**: Los tipos de documentos admitidos incluyen:
  * **Factura**
  * **Nota de Débito**
  * **Nota de Crédito**
  * **Orden de Compra**
  * **Confirmación de Pedido**
  * **Aviso de Envío Anticipado**

## **Uso**:

Esta tarjeta es útil para los administradores de documentos y administradores que necesitan asegurarse de que los documentos estén clasificados correctamente para un procesamiento simplificado. Validar los tipos de documentos mejora la automatización del flujo de trabajo, permite acciones específicas de documentos y mantiene los registros organizados.

## **Escenario de Ejemplo**:

* Un usuario carga un documento etiquetado como "Nota de Débito". Utilizando el operador "Es", la tarjeta confirma que el tipo de documento es realmente "Nota de Débito", lo que permite que el sistema aplique reglas de procesamiento relevantes y lo categorice adecuadamente.

Al implementar la tarjeta "Tipo de Documento", las organizaciones pueden automatizar la clasificación de documentos, garantizar la consistencia en el manejo de documentos y mejorar la eficiencia de los flujos de trabajo de gestión de documentos.
