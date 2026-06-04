# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para invertir el estado actual de un campo de casilla de verificación. Si la casilla está marcada (true), se desmarcará (false), y viceversa. La inversión se produce según las condiciones establecidas en las secciones **"Where"** y **"And"**. Esta tarjeta ayuda a automatizar flujos de trabajo en los que una condición requiere alternar una casilla de verificación según criterios específicos.

## **Componentes de la tarjeta:**

1. **Field Name**
   * **Descripción**: Especifica el campo de casilla de verificación que se invertirá.&#x20;
   * **Detalle**: El campo de casilla de verificación seleccionado verá su estado alternado de true a false o de false a true según su estado actual.

## **Funcionalidad:**

* **Evaluación de la condición**: El sistema evalúa las condiciones definidas en las secciones **"Where"** y **"And"**:
  * Si **ambas condiciones son verdaderas**, se ejecutará la acción de la **sección "Then"**, lo que en este caso significa que se alternará el campo de casilla de verificación.
  * Si **cualquiera de las condiciones es falsa**, la tarjeta no se ejecutará y no se realizará ningún cambio en el campo de casilla de verificación.
* **Ejecución de la acción**: Si las condiciones de las secciones **"Where"** y **"And"** se evalúan como verdaderas, el estado del campo de casilla de verificación se invertirá:
  * Si la casilla está marcada (true), se desmarcará (false).
  * Si la casilla está sin marcar (false), se marcará (true).

## **Configuración:**

Para configurar esta tarjeta, los usuarios deben:

1. **Seleccionar el campo de casilla de verificación** (Field Name) que se invertirá. Los campos de casilla de verificación disponibles en el documento se enumeran para su selección.
2. El campo de casilla de verificación solo se invertirá si las condiciones de las secciones **"Where"** y **"And"** son verdaderas.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Invert checkbox \[Field Name]"** ofrece una herramienta de automatización sencilla pero potente para alternar los valores de las casillas de verificación según condiciones específicas. Al reducir la necesidad de ajustes manuales de las casillas, esta tarjeta mejora la eficiencia en el procesamiento de documentos y garantiza la coherencia en los flujos de trabajo.
