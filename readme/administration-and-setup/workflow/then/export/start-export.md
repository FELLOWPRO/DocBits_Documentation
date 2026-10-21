# Iniciar exportación

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-f55f53ace7e0-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## **Propósito:**

La tarjeta de flujo de trabajo **"Iniciar exportación"** está diseñada para iniciar el proceso de exportación de un documento. Esta tarjeta funciona como un activador dentro del flujo de trabajo para iniciar sin problemas la operación de exportación una vez que se cumplan las condiciones de las secciones anteriores.

## **Componentes de la Tarjeta:**

1. **Acción**
   1. **Descripción**: Inicia el proceso de exportación del documento.
   2. **Detalle**: La tarjeta utiliza los ajustes de exportación configurados en el sistema para procesar y exportar el documento.

## **Funcionalidad:**

* **Evaluación de condición**: el sistema evalúa las condiciones establecidas en **"Dónde"** y **"Y secciones"** del flujo de trabajo. Si todas las condiciones son verdaderas, comienza el proceso de exportación.
* **Exportación de documento**: El documento se procesa y exporta utilizando la configuración de exportación predeterminada o previamente definida.

## **Instalación y configuración:**

Las versiones anteriores utilizan la configuración de exportación ya definida en el sistema. En la versión 4, configure la validación y seleccione Estado después de la exportación. Comprueba también que:

1. Las condiciones **"Dónde"** y **"Y secciones"** están configuradas correctamente, ya que la tarjeta solo se ejecuta si estas condiciones se evalúan como verdaderas.
2. Una configuración de exportación válida está asociada al documento en el sistema.

## **Conclusión:**

La tarjeta de flujo de trabajo **"Iniciar exportación"** proporciona una forma simplificada y automatizada de activar el proceso de exportación. Al confiar en configuraciones preconfiguradas y evaluaciones condicionales, garantiza un procesamiento de documentos eficiente y preciso.

## Versiones de tarjetas y estado de resultados

La afirmación anterior sobre la ausencia de configuración específica de la tarjeta se aplica a la tarjeta Iniciar exportación anterior. Iniciar exportación con validación v4 incluye validación y **Estado después de la exportación**. Elija `finished` para cerrar un documento exportado correctamente o `exported` para mantenerlo abierto para su posterior procesamiento. Las versiones anteriores conservan `finished`. Consulte [Exportar tarjetas y estado de resultados](../../cards-overview/export-cards-guide.md) para conocer los valores predeterminados, errores y pruebas.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

**Cuándo utilizar:** Exportar un documento después de que hayan pasado las comprobaciones requeridas.

**Configuración:** Seleccione el estado posterior a la exportación admitido, por ejemplo `exported` cuando el documento debe permanecer disponible para su posterior procesamiento. Asegúrese de que el exportador configurado y los datos requeridos estén listos.

**Resultado esperado y contraejemplo:** Después de una exportación exitosa, se aplica el estado del resultado seleccionado. Un error del exportador no es una exportación completa; inspeccione su registro y pruebe la rama de falla.

Esta es una configuración ilustrativa y un resultado esperado. Utilice campos, usuarios y grupos configurados en su organización de prueba; no es una afirmación de que este ejemplo haya sido ejecutado.
