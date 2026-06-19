# Reglas de validación

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_setup.png" alt="Configuración de validación y versiones aceptadas"><figcaption><p>Configuración de validación y versiones de XRechnung aceptadas</p></figcaption></figure>

La página **Reglas de validación** (**Documentos electrónicos → Reglas**) controla cómo DocBits valida las facturas electrónicas entrantes. Se basa en el conjunto oficial de reglas **KoSIT XRechnung + ZUGFeRD** más los códigos de hallazgo internos del validador, y le permite anular la gravedad de cada regla para su organización.

## Configuración de validación

La tarjeta **Configuración de validación** muestra su perfil de validación actual (por ejemplo, *B2G — Public Sector Receiver*). Haga clic en **Editar respuestas** para volver a ejecutar el asistente de configuración y cambiar el estándar con el que se valida.

## Versiones de XRechnung aceptadas

La puerta **Versiones de XRechnung aceptadas** enumera todas las versiones de XRechnung. Marque las versiones que acepta: los documentos cuyo CustomizationID quede fuera de esta lista se rechazan con `VAL-VERSION-NOT-ALLOWED` antes de cualquier otra comprobación. Una lista vacía significa "aceptar todo". Cada versión se etiqueta como **current**, **deprecated** o **EOL** junto con su fecha de publicación.

## Perfiles aceptados y modelo de gravedad

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_severity.png" alt="Perfiles aceptados y leyenda de gravedad"><figcaption><p>Perfiles aceptados y significado de cada gravedad</p></figcaption></figure>

Elija qué **perfiles** acepta (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)) mediante **Aceptar todo** / **Borrar** y luego **Guardar**.

Cada regla de validación tiene una **gravedad** que decide qué ocurre cuando se activa:

| Gravedad | Efecto |
|----------|--------|
| **FATAL** | Detiene el procesamiento de inmediato. No se comprueba ninguna capa posterior; el documento pasa a Error. |
| **ERROR** | El documento se rechaza. Los demás hallazgos del mismo documento se siguen mostrando; la notificación al proveedor (si está activada) se dispara. |
| **WARNING** | Aparece en el informe de validación, pero el documento continúa por el flujo con normalidad. |
| **INFO** | Solo registro de auditoría. Sin efecto visible para el usuario ni rechazo. |

## Anular la gravedad de las reglas

<figure><img src="../../../../.gitbook/assets/edoc_validation_rules_table.png" alt="La tabla de reglas de validación"><figcaption><p>La tabla completa de reglas con anulación de gravedad por regla</p></figcaption></figure>

La tabla de reglas enumera todas las reglas de validación (más de 1.600 en total). Filtre por **Capa (Layer)**, **Perfil** o **Versión**, o busque por código o campo. Para cada regla puede anular la **Gravedad** desde el menú desplegable para ajustarla a la política de su organización; por ejemplo, bajar una regla de `ERROR` a `WARNING` para que deje de rechazar el documento.
