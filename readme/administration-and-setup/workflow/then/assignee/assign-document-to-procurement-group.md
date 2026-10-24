# Asignar documento al grupo de compras

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_doc_to_procurement_group_v2-es-es.png" alt="Asignar documento al grupo de compras, Versión 2" width="634"><figcaption><p>Versión 2</p></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Assign to Procurement Group"** se utiliza para asignar un documento a un grupo de compras especificado dentro del sistema. Esto ayuda a agilizar la gestión de documentos al garantizar que el equipo adecuado se ocupe del documento según su grupo de compras asignado.

## **Componentes de la tarjeta:**

1. **Grupo de adquisiciones**
   * **Descripción:** Especifica el grupo de compras al que se asignará el documento.
   * **Detalle:** El grupo de compras seleccionado será responsable de procesar y gestionar el documento.

## **Funcionalidad:**

* **Evaluación de la condición:**\
  La tarjeta solo ejecuta su acción si las secciones **"Cuando"** y **"Y"** se evalúan como verdaderas.
* **Ejecución de la acción:**\
  Si ambas condiciones son verdaderas, el documento se asigna al grupo de compras especificado. Si cualquiera de las condiciones es falsa, no se realiza ninguna acción y el documento permanece sin asignar.

## **Configuración:**

* **Seleccionar el grupo de adquisiciones:** Elija el grupo de compras al que asignar el documento de la lista desplegable.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Assign to Procurement Group"** proporciona una forma sencilla pero eficaz de garantizar que los documentos se asignen automáticamente al equipo de compras correcto para su procesamiento adicional.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo utilizar:** Enviar una excepción de compra a su grupo de adquisiciones.

**Configuración:** Seleccione el grupo configurado `Demo Procurement`.

**Resultado esperado y contraejemplo:** El documento se asigna a ese grupo de adquisiciones. No se debe suponer que un grupo ordinario con un nombre similar sea el mismo objetivo configurado.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
