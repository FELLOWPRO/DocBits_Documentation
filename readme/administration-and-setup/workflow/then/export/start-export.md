# Start Export

<figure><img src="../../../../.gitbook/assets/image (285).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Start Export"** está diseñada para iniciar el proceso de exportación de un documento. Esta tarjeta funciona como un disparador dentro del flujo de trabajo para iniciar de forma fluida la operación de exportación una vez que se cumplen las condiciones de las secciones anteriores.

## **Componentes de la tarjeta:**

1. **Action**
   1. **Descripción**: Inicia el proceso de exportación del documento.
   2. **Detalle**: La tarjeta usa los ajustes de exportación configurados en el sistema para procesar y exportar el documento.

## **Funcionalidad:**

* **Evaluación de la condición**: El sistema evalúa las condiciones establecidas en las secciones **"Where"** y **"And"** del flujo de trabajo. Si todas las condiciones son verdaderas, comienza el proceso de exportación.
* **Exportación del documento**: El documento se procesa y se exporta usando la configuración de exportación predeterminada o previamente definida.

## **Configuración:**

Esta tarjeta no requiere una configuración específica, ya que usa los ajustes de exportación ya definidos en el sistema. Los usuarios deben asegurarse de que:

1. Las condiciones de las secciones **"Where"** y **"And"** estén configuradas correctamente, ya que la tarjeta solo se ejecuta si estas condiciones se evalúan como verdaderas.
2. Haya una configuración de exportación válida asociada al documento en el sistema.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Start Export"** proporciona una forma ágil y automatizada de disparar el proceso de exportación. Al basarse en ajustes preconfigurados y evaluaciones condicionales, garantiza un procesamiento de documentos eficiente y preciso.
