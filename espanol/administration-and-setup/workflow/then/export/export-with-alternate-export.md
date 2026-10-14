# Export with alternate Export

<figure><img src="../../../../.gitbook/assets/image (286).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

La tarjeta de flujo de trabajo **"Export Document with Alternate Export"** posibilita exportar un documento usando una configuración de exportación alternativa. Ofrece flexibilidad al permitir a los usuarios omitir la configuración de exportación predeterminada y usar una alternativa, garantizando la compatibilidad con requisitos o escenarios específicos.

## **Componentes de la tarjeta**

**Alternate Export Configuration**

* **Descripción**: Especifica la configuración de exportación que se utilizará para el documento.
* **Detalle**: Esta configuración anula los ajustes predeterminados y aplica la configuración de exportación alternativa especificada en el flujo de trabajo.

## **Funcionalidad**

* **Evaluación de la condición**:\
  El sistema evalúa las condiciones establecidas en las secciones **"Where"** y **"And"** del flujo de trabajo. La tarjeta se ejecuta solo si todas las condiciones son verdaderas.
* **Exportación del documento**:\
  Una vez ejecutada, la tarjeta usa la configuración de exportación alternativa para procesar y exportar el documento. Esto posibilita un manejo de exportación adaptado a flujos de trabajo específicos.

## **Configuración**

Para configurar esta tarjeta:

1. Asegúrese de que las secciones **"Where"** y **"And"** estén configuradas correctamente, ya que la tarjeta solo se ejecuta si estas condiciones se evalúan como verdaderas.
2. Verifique que la configuración de exportación alternativa sea válida y esté activa en el sistema.

## **Conclusión**

La tarjeta de flujo de trabajo **"Export Document with Alternate Export"** mejora la flexibilidad y el control en los procesos de exportación de documentos. Al permitir la selección de una configuración de exportación alternativa, se adapta a diversos requisitos de exportación a la vez que mantiene una automatización eficiente del flujo de trabajo.
