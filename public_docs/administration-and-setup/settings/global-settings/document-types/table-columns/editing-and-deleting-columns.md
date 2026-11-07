# Editar y eliminar columnas

Las casillas controlan obligatoriedad, edición y visibilidad. Use AI se configura por separado mediante el desplegable de tres estados explicado abajo.

Todo excepto el título se cambia directamente en la lista; no hay cuadro de diálogo de edición.

**Dónde:** Settings → Document Processing → Document Types → Table Columns

## Cambiar un indicador

Marque o desmarque la casilla de la fila. El cambio se guarda de inmediato (*Successfully saved*).

| Indicador | Activado | Desactivado |
|---|---|---|
| **Is Required** | La aprobación se bloquea mientras la columna esté vacía en alguna fila; la pantalla de validación marca la celda. | Se permiten celdas vacías. |
| **Read Only** | El valor se muestra pero no se puede sobrescribir. Utilícelo para valores procedentes de una consulta o de un script. | Los usuarios pueden editar la celda. |
| **Hidden** | La columna desaparece de la pantalla de validación y de la exportación. Sus datos se conservan. | La columna se muestra y se exporta. |


{% hint style="info" %}
Los indicadores surten efecto en los documentos cargados o reiniciados **después** del cambio. Los documentos abiertos conservan su tabla actual hasta que se reinician.
{% endhint %}

## Cambiar el título

Haga clic en el icono de traducción de la columna *Actions* (*Update translation key*), introduzca la nueva etiqueta y confirme. El icono de información situado junto a él muestra qué etiqueta está en vigor actualmente y de dónde procede. Solo cambia la etiqueta; el *Column name* técnico permanece igual, de modo que los scripts, los mapeos de exportación y las reglas entrenadas siguen funcionando.

## Cambiar el tipo o la tabla

No es posible. Oculte la columna (o elimínela si es suya) y añada una nueva con el tipo correcto.

## Eliminar una columna

La acción de eliminar solo se ofrece para columnas creadas por su organización. Las columnas predeterminadas no se pueden eliminar; ocúltelas.

1. Abra el menú de tres puntos de la columna *Actions* y elija **Delete**. La entrada no aparece en las columnas predeterminadas.
2. Confirme.

Qué ocurre:

* La columna se elimina de la configuración. Los documentos procesados **a partir de ahora** ya no la tienen.
* Los documentos ya extraídos conservan la columna y sus valores hasta que se reinician.
* Las reglas entrenadas que asignaban esta columna siguen funcionando para las demás columnas; el mapeo de la columna eliminada se ignora.
* Si la columna se utiliza en un mapeo de exportación o en un script, elimine esa referencia; de lo contrario, la exportación o el script fallará con un error de columna inexistente.

## Deshacer una eliminación

Una columna eliminada no se puede restaurar desde la lista. Vuelva a añadirla con el mismo título: el nombre técnico se deriva del título, por lo que una columna creada con el mismo título obtiene el mismo *Column name* y los mapeos existentes vuelven a coincidir.

## Use AI: Predeterminado, Sí o No

Abra las [columnas de tabla](README.md) del tipo de documento y tabla correctos. **Utilizar IA (Use AI)** es un desplegable de tres estados, no una casilla. Se guarda inmediatamente.

| Opción actual | Efecto en el esquema base |
| --- | --- |
| **Default · solicitado** o **Default · no solicitado** | Usa la selección predeterminada de DocBits para ese tipo y nombre de columna. No significa siempre activado ni siempre desactivado. |
| **Yes · solicitado** | Solicita expresamente la columna configurada. |
| **No · no solicitado** | La excluye del esquema base, incluso si normalmente se solicita. |

Volver a **Default** elimina la elección explícita. Una columna propia nueva normalmente no pertenece a la selección predeterminada de IA: seleccione **Yes** para solicitarla. Las columnas predeterminadas de IA no son todas las columnas incluidas en DocBits; compruebe el efecto indicado y la vista previa.

**Required**, **Read Only** y **Hidden** controlan integridad, edición y visibilidad; no sustituyen la elección de IA. **No** no elimina la columna ni borra valores, y no impide que reglas, scripts u otras fuentes la rellenen. El entrenamiento y las etiquetas adicionales pueden ampliar la solicitud del proveedor: resuelva también allí las contradicciones. Este ajuste no sustituye automáticamente un resultado obtenido solo mediante reglas.

[Structured Output para tablas](../../../../../end-user-and-partner-section/end-user-section/ai-table/structured-output.md).
