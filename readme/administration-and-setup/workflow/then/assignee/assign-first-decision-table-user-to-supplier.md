# Asignar el primer usuario de la tabla de decisión al proveedor

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_supplier_user_first_return_of_dt_v2-es-es.png" alt="Asignar el primer usuario de la tabla de decisión al proveedor, Versión 2" width="634"><figcaption><p>Versión 2</p></figcaption></figure>

## Propósito:

Esta tarjeta de flujo de trabajo establece el usuario asignado de un proveedor registrado a partir de una tabla de decisión. El primer usuario devuelto por la tabla de decisión pasa a ser el usuario asignado del proveedor, el contacto interno responsable del proveedor. Los usuarios devueltos también pueden recibir información por correo electrónico.

Al igual que **Assign User to Supplier**, la tarjeta no trabaja sobre un documento: está pensada para flujos de trabajo que se inician por un cambio de estado de un proveedor, por ejemplo con la tarjeta When **Supplier status changed**. El usuario no se selecciona en la tarjeta, sino que lo determina una tabla de decisión evaluada antes en el mismo flujo de trabajo, por ejemplo con la tarjeta **Decision Table has Returns**.

## Componentes de la tarjeta:

1. **Enviar correo electrónico**
   * **Descripción:** El ajuste de correo electrónico de la tarjeta.
   * **Opciones:** **Verdadero** o **Falso**.
   * **Detalle:** Con **Verdadero**, los correos electrónicos se envían con las plantillas de correo electrónico seleccionadas. Con **Falso**, no se envía ningún correo electrónico. Si **Enviar correo electrónico** no está definido, tampoco se envía ningún correo electrónico.
2. **Plantillas de correo electrónico**
   * **Descripción:** Las plantillas de correo electrónico utilizadas para el correo electrónico.
   * **Detalle:** Se pueden seleccionar una o varias plantillas de correo electrónico de la organización. Las plantillas se utilizan cuando **Enviar correo electrónico** es **Verdadero**.

## Funcionalidad:

* **Lectura de la tabla de decisión:** La tarjeta lee los usuarios devueltos por la tabla de decisión anteriormente en el flujo de trabajo. Solo se tienen en cuenta los usuarios devueltos, no los grupos.
* **Notificación por correo electrónico:** Cuando se envían correos electrónicos, van a todos los usuarios devueltos por la tabla de decisión, no solo al primero. Los correos electrónicos se envían antes de asignar el usuario al proveedor.
* **Ejecución de la acción:** El primer usuario devuelto se guarda como usuario asignado del proveedor cuyo estado ha cambiado. Si el proveedor ya tiene un usuario asignado, ese usuario se sustituye. El resultado se anota en el registro del flujo de trabajo.
* **Datos que faltan:**
  * Si la tabla de decisión no ha devuelto ningún usuario, no se asigna nada y la tarjeta registra los datos que faltan en el registro del flujo de trabajo.
  * Si **Enviar correo electrónico** es **Verdadero** pero no hay ninguna plantilla de correo electrónico seleccionada, la tarjeta se detiene sin asignar el usuario y registra los datos que faltan.
  * Si **Enviar correo electrónico** no está definido, el registro del flujo de trabajo indica el ajuste que falta y el usuario se asigna sin correo electrónico.
* **Errores:** Si el servicio de correo electrónico o el de proveedores rechaza la solicitud o no responde a tiempo, la tarjeta termina con un error. Si falla el envío de los correos electrónicos, el usuario no se asigna al proveedor.

## Configuración:

* La tarjeta se puede utilizar en un flujo de trabajo que se inicia por un cambio de estado de un proveedor. Una tabla de decisión que devuelva usuarios debería evaluarse antes en el mismo flujo de trabajo.
* La tarjeta se puede añadir desde la categoría **Asignado a**. A continuación se puede definir **Enviar correo electrónico** y seleccionar una o varias plantillas de correo electrónico.

## Conclusión:

La tarjeta de flujo de trabajo «Assign First Decision Table User to Supplier» asigna un contacto responsable a un proveedor según reglas mantenidas en una tabla de decisión. El correo electrónico opcional permite que los usuarios devueltos conozcan de inmediato al proveedor.
