# Asignar usuario al proveedor

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_user_to_supplier_v2-es-es.png" alt="Asignar usuario al proveedor, Versión 2" width="634"><figcaption><p>Versión 2</p></figcaption></figure>

## Propósito:

Esta tarjeta de flujo de trabajo establece el usuario asignado de un proveedor registrado. El usuario asignado es el contacto interno responsable del proveedor. La tarjeta no trabaja sobre un documento: está pensada para flujos de trabajo que se inician por un cambio de estado de un proveedor, por ejemplo con la tarjeta When **Supplier status changed**. El proveedor cuyo estado ha cambiado es el proveedor al que se asigna el usuario.

## Componentes de la tarjeta:

1. **Usuario**
   * **Descripción:** El usuario que pasa a ser el usuario asignado del proveedor.
   * **Detalle:** Se puede seleccionar un usuario de la organización. Si el proveedor ya tiene un usuario asignado, ese usuario se sustituye.

## Funcionalidad:

* **Ejecución de la acción:** La tarjeta toma el proveedor de la ejecución del flujo de trabajo y guarda el usuario seleccionado como usuario asignado del proveedor. El resultado se anota en el registro del flujo de trabajo.
* **Uso con correos electrónicos:** Una vez asignado un usuario, se pueden dirigir correos electrónicos a este usuario con la opción **Usuario asignado al proveedor**, por ejemplo en la tarjeta **Send Email**.
* **Datos que faltan:** Si no hay ningún usuario seleccionado en la tarjeta, la tarjeta no se ejecuta y registra los datos que faltan en el registro del flujo de trabajo.
* **Errores:** Si el servicio de proveedores rechaza la solicitud o no responde a tiempo, la tarjeta termina con un error.

## Configuración:

* La tarjeta se puede utilizar en un flujo de trabajo que se inicia por un cambio de estado de un proveedor.
* La tarjeta se puede añadir desde la categoría **Asignado a**. A continuación se selecciona en el campo **Usuario** el usuario que debería ser responsable del proveedor.

## Conclusión:

La tarjeta de flujo de trabajo «Assign User to Supplier» asigna automáticamente a cada proveedor un contacto responsable cuando cambia su estado, por ejemplo después del registro. Los pasos posteriores, como los correos electrónicos al usuario asignado, pueden basarse en esta asignación.
