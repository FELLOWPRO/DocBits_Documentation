# Exportar con exportación alternativa

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-379e4b3a5355-es.png" alt="Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados." width="563"><figcaption><p>Campos de la tarjeta en la versión mostrada. Los campos aún no están configurados.</p></figcaption></figure>

## **Propósito**

La tarjeta de flujo de trabajo **"Exportar documento con exportación alternativa"** posibilita exportar un documento usando una configuración de exportación alternativa. Ofrece flexibilidad al permitir a los usuarios omitir la configuración de exportación predeterminada y usar una alternativa, garantizando la compatibilidad con requisitos o escenarios específicos.

## **Componentes de la tarjeta**

**Configuración de exportación alternativa**

* **Descripción**: Especifica la configuración de exportación que se utilizará para el documento.
* **Detalle**: Esta configuración anula los ajustes predeterminados y aplica la configuración de exportación alternativa especificada en el flujo de trabajo.

## **Funcionalidad**

* **Evaluación de la condición**:\
  El sistema evalúa las condiciones establecidas en las secciones **"Donde"** y **"Y"** del flujo de trabajo. La tarjeta se ejecuta solo si todas las condiciones son verdaderas.
* **Exportación del documento**:\
  Una vez ejecutada, la tarjeta usa la configuración de exportación alternativa para procesar y exportar el documento. Esto posibilita un manejo de exportación adaptado a flujos de trabajo específicos.

## **Configuración**

Para configurar esta tarjeta:

1. Asegúrese de que las secciones **"Donde"** y **"Y"** estén configuradas correctamente, ya que la tarjeta solo se ejecuta si estas condiciones se evalúan como verdaderas.
2. Verifique que la configuración de exportación alternativa sea válida y esté activa en el sistema.

## **Conclusión**

La tarjeta de flujo de trabajo **"Exportar documento con exportación alternativa"** mejora la flexibilidad y el control en los procesos de exportación de documentos. Al permitir la selección de una configuración de exportación alternativa, se adapta a diversos requisitos de exportación a la vez que mantiene una automatización eficiente del flujo de trabajo.
