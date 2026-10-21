# Invertir casilla de verificación

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-d1f382afe206-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para invertir el estado actual de un campo de casilla de verificación. Si la casilla está marcada (true), se desmarcará (false), y viceversa. La inversión se produce según las condiciones establecidas en las secciones **"Cuando"** y **"Y"**. Esta tarjeta ayuda a automatizar flujos de trabajo en los que una condición requiere alternar una casilla de verificación según criterios específicos.

## **Componentes de la tarjeta:**

1. **Nombre de campo**
   * **Descripción**: Especifica el campo de casilla de verificación que se invertirá.
   * **Detalle**: El campo de casilla de verificación seleccionado verá su estado alternado de true a false o de false a true según su estado actual.

## **Funcionalidad:**

* **Evaluación de la condición**: El sistema evalúa las condiciones definidas en las secciones **"Cuando"** y **"Y"**:
  * Si **ambas condiciones son verdaderas**, se ejecutará la acción de la **sección "Then"**, lo que en este caso significa que se alternará el campo de casilla de verificación.
  * Si **cualquiera de las condiciones es falsa**, la tarjeta no se ejecutará y no se realizará ningún cambio en el campo de casilla de verificación.
* **Ejecución de la acción**: Si las condiciones de las secciones **"Cuando"** y **"Y"** se evalúan como verdaderas, el estado del campo de casilla de verificación se invertirá:
  * Si la casilla está marcada (true), se desmarcará (false).
  * Si la casilla está sin marcar (false), se marcará (true).

## **Configuración:**

Para configurar esta tarjeta, los usuarios deben:

1. **Seleccionar el campo de casilla de verificación** (Field Name) que se invertirá. Los campos de casilla de verificación disponibles en el documento se enumeran para su selección.
2. El campo de casilla de verificación solo se invertirá si las condiciones de las secciones **"Cuando"** y **"Y"** son verdaderas.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Invert checkbox \[Field Name]"** ofrece una herramienta de automatización sencilla pero potente para alternar los valores de las casillas de verificación según condiciones específicas. Al reducir la necesidad de ajustes manuales de las casillas, esta tarjeta mejora la eficiencia en el procesamiento de documentos y garantiza la coherencia en los flujos de trabajo.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo usarlo:** Alternar un valor booleano cuando esa sea la operación comercial prevista.

**Configuración:** Seleccione la casilla de verificación `demo_flag` con el valor inicial `false`.

**Resultado esperado y contraejemplo:** Una ejecución lo convierte en `true`; una segunda ejecución hace que sea `false` nuevamente. Utilice la casilla de verificación Establecer en su lugar cuando los reintentos deban dejar siempre el mismo valor.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
