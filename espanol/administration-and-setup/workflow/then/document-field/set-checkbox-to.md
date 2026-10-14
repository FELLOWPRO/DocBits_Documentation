# Set Checkbox to

<figure><img src="../../../../.gitbook/assets/image (279).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Esta tarjeta de flujo de trabajo está diseñada para establecer un campo de casilla de verificación a un valor especificado (true o false) según las condiciones definidas en las secciones **"Where"** y **"And"**. Proporciona una forma sencilla pero eficaz de automatizar las actualizaciones de las casillas de verificación cuando se cumplen ciertos criterios, garantizando un procesamiento de documentos ágil.

## **Componentes de la tarjeta:**

1. **Field Name:**
   * **Descripción**: Especifica el campo donde se establecerá la casilla de verificación.
   * **Detalle**: El campo de casilla de verificación que se actualizará se identifica por el nombre del campo.
2. **Boolean**
   * **Descripción**: Define el valor al que se establecerá el campo de casilla de verificación cuando las condiciones de las secciones **Where** y **And** sean ambas verdaderas.
   * **Opciones**:
     * **True**: La casilla se establecerá en **true** si se cumplen las condiciones.
     * **False**: La casilla se establecerá en **false** si se cumplen las condiciones.

## **Funcionalidad:**

* **Evaluación de la condición**: El sistema evalúa las condiciones de las secciones **"Where"** y **"And"**.&#x20;
* **Ejecución de la acción**: Si las secciones **"Where"** y **"And"** se evalúan como verdaderas, el campo de casilla de verificación se actualizará al valor especificado (true o false). Si cualquiera de las condiciones es falsa, no se realiza ninguna acción y la casilla permanece como estaba.

## **Configuración:**

Para configurar esta tarjeta, los usuarios deben:

1. **Especificar el campo de casilla de verificación de destino** que se establecerá en true o false cuando se cumplan las condiciones.
2. **Elegir el valor (true o false)** al que se establecerá la casilla tras la evaluación de la condición.
3. La tarjeta solo ejecuta su acción si ambas condiciones de las secciones **"Where"** y **"And"** se evalúan como verdaderas.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Set Checkbox"** es una herramienta de automatización sencilla y eficaz para actualizar los campos de casilla de verificación según condiciones específicas. Al garantizar que se cumplan las secciones **"Where"** y **"And"**, permite a los usuarios automatizar procesos y reducir la intervención manual, garantizando un procesamiento de documentos más fluido y eficiente.
