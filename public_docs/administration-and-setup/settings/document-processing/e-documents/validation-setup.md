# Configuración de validación y versiones aceptadas

Esta página explica el asistente de configuración, las versiones de XRechnung aceptadas y los perfiles aceptados de la página [Validación de facturas electrónicas](validation-rules.md). Solo los administradores de la organización pueden cambiar estos ajustes.

## Configuración de validación

<figure><img src="../../../../.gitbook/assets/einvoice-setup-versions-es.png" alt="Configuración de validación y versiones aceptadas"><figcaption><p>Configuración de validación y versiones de XRechnung aceptadas</p></figcaption></figure>

La tarjeta **Configuración de validación** muestra su perfil de validación actual (por ejemplo, *B2G — Public Sector Receiver*). Haga clic en **Editar respuestas** para volver a ejecutar el asistente de configuración y cambiar el estándar con el que se valida.

## Versiones de XRechnung aceptadas

La puerta **Versiones de XRechnung aceptadas** enumera todas las versiones de XRechnung. Marque las versiones que acepta: los documentos cuyo CustomizationID quede fuera de esta lista se rechazan con `VAL-VERSION-NOT-ALLOWED` antes de cualquier otra comprobación. Una lista vacía significa "aceptar todo". Cada versión se etiqueta como **current**, **deprecated** o **EOL** junto con su fecha de publicación.

## Perfiles aceptados y modelo de gravedad

<figure><img src="../../../../.gitbook/assets/einvoice-profiles-severity-es.png" alt="Perfiles aceptados y leyenda de gravedad"><figcaption><p>Perfiles aceptados y significado de cada gravedad</p></figcaption></figure>

Elija qué **perfiles** acepta (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)) mediante **Aceptar todo** / **Borrar** y luego **Guardar**.

Cada regla de validación tiene una **gravedad** que decide qué ocurre cuando se activa:

| Gravedad | Efecto |
|----------|--------|
| **FATAL** | Detiene el procesamiento de inmediato. No se comprueba ninguna capa posterior; el documento pasa a Error. |
| **ERROR** | El documento se rechaza. Los demás hallazgos del mismo documento se siguen mostrando; la notificación al proveedor (si está activada) se dispara. |
| **WARNING** | Aparece en el informe de validación, pero el documento continúa por el flujo con normalidad. |
| **INFO** | Solo registro de auditoría. Sin efecto visible para el usuario ni rechazo. |

### Qué cambia el asistente

La tarjeta **Configuración de validación**, más abajo en la página, abre un asistente con **Editar respuestas**. El asistente sustituye todo el conjunto de anulaciones de reglas de su organización. DocBits le avisa antes de guardar. Revise con atención el paso **Revisar y aplicar**.

Siguiente: [Gravedad de las reglas](validation-rule-severities.md) y [Validación para cada tipo de documento](validation-per-document-type.md).
