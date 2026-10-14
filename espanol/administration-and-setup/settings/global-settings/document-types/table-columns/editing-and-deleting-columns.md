# Editar y eliminar columnas

Todo excepto el título se cambia directamente en la lista; no hay cuadro de diálogo de edición.

**Dónde:** Settings → Global Settings → Document Types → Table Columns

## Cambiar un indicador

Marque o desmarque la casilla de la fila. El cambio se guarda de inmediato (*Successfully saved*).

| Indicador | Activado | Desactivado |
|---|---|---|
| **Is Required** | La aprobación se bloquea mientras la columna esté vacía en alguna fila; la pantalla de validación marca la celda. | Se permiten celdas vacías. |
| **Read Only** | El valor se muestra pero no se puede sobrescribir. Utilícelo para valores procedentes de una consulta o de un script. | Los usuarios pueden editar la celda. |
| **Hidden** | La columna desaparece de la pantalla de validación y de la exportación. Sus datos se conservan. | La columna se muestra y se exporta. |
| **Use AI** | La extracción de tablas con IA rellena esta columna, también para proveedores con reglas entrenadas. | La columna la rellenan las reglas entrenadas, o la IA cuando no existen reglas. |

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
