# Asignar documento al grupo de instalación

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_doc_to_facility_group_v2-es-es.png" alt="Asignar documento al grupo de instalación, Versión 2" width="634"><figcaption><p>Versión 2</p></figcaption></figure>

## Propósito:

Esta tarjeta de flujo de trabajo asigna un documento al grupo responsable de la instalación de su orden de compra. La instalación no se selecciona en la tarjeta: se toma de las órdenes de compra con las que está emparejado el documento. A continuación, la tarjeta busca un grupo de usuarios cuyo nombre contenga tanto el nombre de grupo introducido en la tarjeta como el código de la instalación, y asigna el documento a ese grupo.

Esto resulta útil cuando existe el mismo tipo de equipo una vez por instalación, por ejemplo un grupo de aprobación por planta o almacén, y cada documento debería ir al equipo de la instalación para la que se pidió.

Para una asignación que se añade a una secuencia de aprobadores en lugar de realizarse directamente, se puede utilizar la tarjeta **Assign Sequentially to Facility Group**.

## Componentes de la tarjeta:

1. **Nombre del grupo**
   * **Descripción:** La parte del nombre que tienen en común los grupos de instalación.
   * **Detalle:** Un texto que se compara con los nombres de los grupos de usuarios de la organización. Un grupo coincide si su nombre contiene este texto y el código de instalación de la orden de compra. La comparación no distingue entre mayúsculas y minúsculas. Por ejemplo, con el nombre de grupo **Approver** y una orden de compra de la instalación **1000**, coincidiría un grupo llamado **Approver 1000**.

## Funcionalidad:

* **Determinación de la instalación:** La tarjeta lee las órdenes de compra con las que está emparejado el documento y recoge el código de instalación (la ubicación de la orden de compra) de cada una de ellas.
* **Determinación del grupo:** Para cada código de instalación, la tarjeta busca grupos de usuarios cuyo nombre contenga tanto el **Nombre del grupo** de la tarjeta como el código de instalación. Los códigos de instalación para los que no se encuentra ningún grupo se indican en el registro del flujo de trabajo.
* **Ejecución de la acción:** El documento se asigna al grupo coincidente. Si coinciden varios grupos, por ejemplo porque el documento está emparejado con órdenes de compra de distintas instalaciones, el documento se asigna solo a uno de ellos; la tarjeta no determina a cuál.
* **Datos que faltan:**
  * Si no se ha introducido ningún nombre de grupo en la tarjeta, la tarjeta no se ejecuta y registra los datos que faltan en el registro del flujo de trabajo.
  * Si el documento no está emparejado con ninguna orden de compra, la tarjeta registra los datos que faltan en lugar de asignar el documento.
  * Si ningún grupo coincide con ninguno de los códigos de instalación, el documento no se asigna y el registro del flujo de trabajo indica que no se ha encontrado ningún grupo coincidente.

## Configuración:

* Los grupos de usuarios deberían nombrarse de forma que cada nombre contenga la parte común del nombre y el código de instalación, por ejemplo **Approver 1000**, **Approver 2000**.
* La tarjeta se puede añadir desde la categoría **Asignado a**. A continuación se introduce la parte común del nombre de los grupos en el campo **Nombre del grupo**.
* Como la instalación procede de las órdenes de compra emparejadas, lo más adecuado es utilizar la tarjeta en flujos de trabajo para documentos que ya se han emparejado con una orden de compra.

## Conclusión:

La tarjeta de flujo de trabajo «Assign Document to Facility Group» dirige los documentos al equipo de la instalación para la que se pidieron. Una sola tarjeta cubre todas las instalaciones, siempre que los grupos de usuarios sigan un esquema de nombres coherente con el código de instalación en sus nombres.
