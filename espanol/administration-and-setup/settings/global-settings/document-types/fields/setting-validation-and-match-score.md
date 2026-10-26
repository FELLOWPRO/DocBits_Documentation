# Establecer Validación y Puntaje de Partido

En **Campos**, puede establecer los umbrales de validación y reconocimiento de un tipo de documento. Esta página utiliza **Factura** en una organización de prueba de la documentación. Explica la casilla **Forzar La Validación** y los controles de **Puntaje De Partido** actuales.

## Abrir la configuración de campos

1. Vaya a **Ajustes → Tipos De Documento → Factura → Campos**.
2. Use **Buscar por nombre** para encontrar un campo, por ejemplo `invoice_id` (que se muestra como **Número de factura**).
3. Revise la fila del campo antes de cambiar una configuración. **REQUERIDO**, **Solo Lectura**, **Oculto** y **Forzar La Validación** son casillas independientes.

<figure><img src="../../../../../.gitbook/assets/dbdc-675-fields-overview-es.png" alt="Página Campos de la Sandbox en español que muestra Configuración de reconocimiento, los controles OCR y Puntaje De Partido, las columnas de campos y Guardar ajustes"><figcaption><p>Los controles de reconocimiento aparecen encima de la lista de campos.</p></figcaption></figure>

## Forzar La Validación

Marque **Forzar La Validación** en la fila del campo para aplicar una validación más estricta a ese campo. La casilla es independiente de **REQUERIDO**: marcar un campo como requerido no selecciona Forzar La Validación automáticamente. La casilla puede no estar disponible cuando un campo está oculto o es de solo lectura. Haga clic en **Guardar ajustes** después de cambiar la configuración del campo.

Las instrucciones antiguas sugerían introducir aquí límites numéricos o expresiones regulares. La tabla de Campos actual no muestra un editor de reglas en la celda de Forzar La Validación. Para reglas específicas de cada campo, consulte [Configuración de propiedades de campo](configuring-field-properties-1.md).

## Puntaje De Partido

**Puntaje De Partido** es un umbral numérico, no un valor de referencia fijo. El control deslizante **PUNTAJE DE PARTIDO** en **Configuración de reconocimiento** aplica su valor a las filas de campos del tipo de documento; utilice el campo **Puntaje De Partido** de una fila para un valor individual. En la organización de prueba, el control deslizante y `invoice_id` muestran ambos **50**. Revise los campos afectados y haga clic en **Guardar ajustes**.

<figure><img src="../../../../../.gitbook/assets/dbdc-675-invoice-id-settings-es.png" alt="Fila del campo invoice_id en la Sandbox en español con Forzar La Validación marcada y Puntaje De Partido 50"><figcaption><p>Busque un campo para revisar su casilla Forzar La Validación y su valor de Puntaje De Partido.</p></figcaption></figure>

**OCR** es un umbral de reconocimiento independiente situado junto al Puntaje De Partido. **RESTAURAR LOS VALORES PREDETERMINADOS** restablece la configuración; utilícelo solo cuando desee descartar sus umbrales personalizados. Para otras opciones de campos, consulte la [Descripción general de Campos](README.md).
