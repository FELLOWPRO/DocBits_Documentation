# Buenas prácticas

## Conserve las columnas predeterminadas para importes y cantidades

Las comprobaciones de líneas (*cantidad × precio unitario = total de línea*) y el PO matching buscan las columnas predeterminadas `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT` e `ITEM_NUMBER`. Si en su lugar crea columnas propias para estos valores, las comprobaciones no se ejecutan y el PO matching informa de que faltan columnas obligatorias. Cambie el *título* si la denominación no le convence; conserve la columna.

## Oculte, no elimine

Las columnas predeterminadas que no necesita se ocultan, no se eliminan; de todos modos, no se pueden eliminar. En el caso de sus propias columnas, ocultar también es la opción más segura mientras no esté seguro de si un script o un mapeo de exportación sigue haciendo referencia a la columna.

## Marque como obligatorio solo lo que bloquea la exportación

Toda columna obligatoria debe rellenarse en todas las filas antes de que un usuario pueda aprobar el documento. Utilícelo para valores que el ERP rechaza cuando faltan (por ejemplo, el centro de coste en una exportación contable), no para valores que simplemente resultan útiles.

## Utilice *Read Only* para valores consultados

Los valores que un script o una consulta de datos maestros escribe en la tabla (descripción del artículo desde el maestro de artículos, código de impuesto del proveedor) deberían ser de solo lectura, para que los usuarios corrijan el origen en lugar de la copia.

## Utilice la IA por columna, no por proveedor

Para un proveedor con reglas entrenadas, la mayoría de las columnas salen bien a partir de las reglas. Si una columna no es fiable (descripciones largas que se desbordan a otra línea, un descuento que a veces está en otro lugar), active *Use AI* solo en esa columna. Las reglas se encargan del resto.

## Nombre las columnas para el ERP, no para el documento

El *Column name* acaba en los mapeos de exportación y en los scripts. `COST_CENTRE` es más fácil de mapear que `KST` y no cambia cuando un proveedor lo imprime de otra forma.

## Pruebe con un documento reiniciado

Tras un cambio, reinicie un documento existente del tipo de documento y ábralo: aparece la nueva columna, desaparece la oculta y las celdas obligatorias están marcadas. Solo entonces despliegue el cambio a los usuarios.

## Una tabla por estructura de líneas

Cree una segunda tabla solo cuando un tipo de documento tenga realmente dos tablas independientes (por ejemplo, líneas de artículos y una tabla de cargos aparte). Las tablas vacías adicionales aparecen en todos los documentos del tipo.
