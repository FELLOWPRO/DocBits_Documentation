# Columnas de tabla

Las columnas de tabla definen qué columnas tiene la tabla de líneas de detalle de un tipo de documento: qué extrae DocBits en cada columna, qué ve el usuario en la pantalla de validación y qué se envía al ERP en la exportación.

**Dónde:** Configuración → Configuración global → Tipos de documentos → Columnas de tabla

<figure><img src="../../../../.gitbook/assets/table-columns_list.png" alt="Lista de columnas de tabla con los indicadores Obligatoria, Solo lectura, Oculta y Usar IA por columna"><figcaption><p>Columnas de tabla: una fila por columna, los indicadores se cambian directamente en la lista</p></figcaption></figure>

## Qué se muestra

Cada fila es una columna de una tabla. La lista muestra:

| Columna | Significado |
|---|---|
| **Nombre de columna** (*Column name*) | Nombre técnico, generado a partir del título (en mayúsculas, con guiones bajos). Se utiliza en scripts, mapeos de exportación y la API. No se puede cambiar después. |
| **Título** (*Title*) | Etiqueta que se muestra en la pantalla de validación. Se cambia con el icono de traducción de la columna *Acciones* (*Actualizar clave de traducción*). |
| **Tipo de columna** (*Column Type*) | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` o `CURRENCY`. Determina la validación y el formato. |
| **Nombre de tabla** (*Table name*) | La tabla a la que pertenece la columna, por ejemplo `INVOICE_TABLE`. |
| **Obligatoria** (*Is Required*) | El documento no se puede aprobar mientras esta columna esté vacía en alguna fila. |
| **Solo lectura** (*Read Only*) | Los usuarios ven el valor, pero no pueden editarlo. |
| **Oculta** (*Hidden*) | La columna no se muestra ni se exporta. Sirve para desactivar columnas predeterminadas que no necesitas. |
| **Usar IA** (*Use AI*) | La extracción de tablas por IA rellena esta columna, incluso cuando el proveedor tiene reglas entrenadas. |
| **Acciones** (*Actions*) | Icono de traducción: cambiar el título. Icono de información: de dónde procede la etiqueta mostrada (tu traducción, el valor predeterminado, la clave). Menú de tres puntos: *Eliminar*, solo para columnas creadas por tu organización; las columnas predeterminadas solo se pueden ocultar. |

Encima de la lista hay dos botones:

* **Crear nueva tabla**: una segunda tabla de líneas de detalle para el tipo de documento (por ejemplo, una tabla de cargos junto a la tabla de artículos).
* **Agregar nueva columna de tabla**: abre el cuadro de diálogo descrito en [Añadir una columna nueva](#adding-a-new-column).

## Columnas predeterminadas y columnas propias

Cada tipo de documento incluye un conjunto de columnas predeterminadas (para facturas: número de artículo, descripción, cantidad, precio unitario, importe total, impuesto, …). Pertenecen a DocBits, no a tu organización, por lo que no se pueden eliminar; ocúltalas en su lugar. Las columnas que añades tú pertenecen a tu organización y sí se pueden eliminar.

{% hint style="info" %}
**Los cambios solo se aplican a documentos nuevos.** Una columna que añades, ocultas o eliminas aparece en los documentos que se cargan o se reinician después del cambio. Los documentos que ya están en el panel conservan la tabla tal como se extrajo. Reinicia un documento para que adopte la nueva configuración.
{% endhint %}

## Finalidad y uso <a href="#purpose-and-use" id="purpose-and-use"></a>

Una columna de tabla es un campo de la tabla de líneas de detalle. Todo lo que DocBits hace con una tabla (extracción, validación, coincidencia de PO, exportación) funciona sobre las columnas configuradas aquí.

### Dónde aparece una columna

| Lugar | Qué hace la columna allí |
|---|---|
| **Pantalla de validación** | Una columna de la tabla de líneas de detalle. El *Título* es el encabezado; el *Tipo de columna* decide el editor (importe, fecha, texto, sí/no). Las columnas ocultas no se muestran. |
| **Entrenamiento de tablas** | Al entrenar la tabla de un proveedor, cada columna detectada se asigna a una de las columnas configuradas aquí. Solo se pueden asignar columnas configuradas. |
| **Extracción de tablas por IA** | La IA rellena las columnas configuradas. Una columna marcada como *Usar IA* la rellena la IA incluso en proveedores con reglas entrenadas. |
| **Reglas de validación** | Las comprobaciones de línea, como *cantidad × precio unitario = total de línea*, se ejecutan sobre las columnas predeterminadas `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **Coincidencia de PO** | Necesita las columnas predeterminadas número de artículo, precio unitario, cantidad e importe total. Sin ellas, el documento muestra *Line Item Table is missing Mandatory column for PO*. |
| **Exportación** | Toda columna no oculta forma parte de los datos de líneas enviados al ERP. El mapeo de exportación hace referencia al *Nombre de columna*. |
| **Scripts** | Los scripts leen y escriben columnas por su *Nombre de columna*, por ejemplo `row["TOTAL_AMOUNT"]`. |

### Alcance

* Las columnas de tabla se configuran **por tabla**, y una tabla pertenece a un **tipo de documento**. Las columnas de factura no afectan a los albaranes.
* La configuración es **por organización**. Las suborganizaciones la heredan.
* Qué columnas se *rellenan* para un proveedor concreto lo decide el entrenamiento de ese proveedor o la IA; la configuración de columnas solo indica qué columnas existen.

### Motivos habituales para cambiar la configuración

* Hay que capturar por línea un valor específico del cliente (centro de coste, número de proyecto, número de artículo interno) → añade una columna.
* Una columna predeterminada nunca se usa y estorba en la pantalla de validación → ocúltala.
* Una columna debe estar siempre rellena antes de exportar → márcala como *Obligatoria*.
* Un valor procede de la búsqueda en el ERP y los usuarios no deben editarlo → márcalo como *Solo lectura*.
* La IA captura una columna mejor que las reglas entrenadas (por ejemplo, descripciones de texto libre) → márcala como *Usar IA*.

## Añadir una columna nueva <a href="#adding-a-new-column" id="adding-a-new-column"></a>

Añade una columna cuando haya que capturar por línea un valor que las columnas predeterminadas no cubren: un centro de coste, un número de proyecto, un número de artículo interno.

### Antes de empezar

* Decide a qué **tabla** pertenece la columna. La mayoría de los tipos de documento tienen una sola tabla (por ejemplo `INVOICE_TABLE`). Si la lista está vacía, haz clic primero en **Crear nueva tabla**; el cuadro de diálogo solo pide un nombre de tabla.
* Decide el **tipo**: `AMOUNT` para importes, `NUMBER` para cantidades, `DATE`, `BOOLEAN` para sí/no, `CURRENCY` para un código de moneda ISO, `STRING` para todo lo demás. El tipo no se puede cambiar después de guardar.
* Comprueba si ya existe una **columna predeterminada** con el mismo significado pero oculta. Las columnas ocultas aparecen en la lista con el indicador *Oculta* activado; desactívalo en lugar de crear un duplicado.

### Pasos

1. Abre **Configuración → Configuración global → Tipos de documentos → Columnas de tabla**.
2. Haz clic en **Agregar nueva columna de tabla**.

<figure><img src="../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Cuadro de diálogo Agregar nueva columna de tabla con Título, Columna obligatoria, Seleccionar tipo de columna y Seleccionar tabla"><figcaption><p>Agregar nueva columna de tabla</p></figcaption></figure>

3. Rellena el cuadro de diálogo:

| Campo | Qué introducir |
|---|---|
| **Título** (*Title*) | Etiqueta que el usuario ve en la pantalla de validación, por ejemplo `Cost Centre`. Solo letras y números. DocBits deriva de ella el *Nombre de columna* técnico (`COST_CENTRE`). |
| **¿Es obligatoria la columna?** (*Is column required?*) | Márcalo cuando el documento no deba aprobarse mientras la columna esté vacía en alguna fila. |
| **Seleccionar tipo de columna** (*Select column type*) | Consulta la lista de tipos anterior. |
| **Seleccionar tabla** (*Select Table*) | La tabla que recibe la columna. |

4. Haz clic en **Continuar** (*Proceed*). La columna aparece en la lista con *Solo lectura*, *Oculta* y *Usar IA* desactivados. Cambia esos indicadores en la lista si lo necesitas; consulta [Editar y eliminar columnas](#editing-and-deleting-columns).

### Después de añadirla

* La columna está **vacía en los documentos existentes**. Se rellena en los documentos cargados o reiniciados después del cambio.
* En proveedores con **reglas entrenadas**, abre uno de sus documentos en el entrenamiento de tablas y asigna la nueva columna; de lo contrario, la columna se queda vacía para ese proveedor. Consulta [Definición de tablas y columnas](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* Con la **extracción de tablas por IA**, la IA rellena la columna si el valor es reconocible en el documento. Marca la columna como *Usar IA* si el proveedor tiene reglas entrenadas pero esta columna debe seguir viniendo de la IA.
* Añade la columna al **mapeo de exportación** si el ERP debe recibirla; consulta [Exportar](../../document-processing/export.md).

### Mensajes

| Mensaje | Significado |
|---|---|
| *Column name already exists* | Ya hay una columna con este nombre técnico en la tabla. Elige otro título. |
| *Column name already exists – Please activate it in Table Column settings* | Una columna predeterminada oculta tiene este nombre. Desactiva su indicador *Oculta* en lugar de crear una nueva. |
| *No table exists. Please create table before creating columns.* | El tipo de documento aún no tiene tabla: haz clic primero en **Crear nueva tabla**. |

## Editar y eliminar columnas <a href="#editing-and-deleting-columns" id="editing-and-deleting-columns"></a>

Todo excepto el título se cambia directamente en la lista; no hay cuadro de diálogo de edición.

**Dónde:** Configuración → Configuración global → Tipos de documentos → Columnas de tabla

### Activar o desactivar un indicador

Marca o desmarca la casilla de la fila. El cambio se guarda de inmediato (*Successfully saved*).

| Indicador | Activado | Desactivado |
|---|---|---|
| **Obligatoria** (*Is Required*) | La aprobación se bloquea mientras la columna esté vacía en alguna fila; la pantalla de validación marca la celda. | Se permiten celdas vacías. |
| **Solo lectura** (*Read Only*) | El valor se muestra, pero no se puede sobrescribir. Úsalo para valores que proceden de una búsqueda o de un script. | Los usuarios pueden editar la celda. |
| **Oculta** (*Hidden*) | La columna desaparece de la pantalla de validación y de la exportación. Sus datos se conservan. | La columna se muestra y se exporta. |
| **Usar IA** (*Use AI*) | La extracción de tablas por IA rellena esta columna, también en proveedores que tienen reglas entrenadas. | La columna la rellenan las reglas entrenadas, o la IA cuando no existen reglas. |

{% hint style="info" %}
Los indicadores surten efecto en los documentos cargados o reiniciados **después** del cambio. Los documentos abiertos conservan su tabla actual hasta que se reinician.
{% endhint %}

### Cambiar el título

Haz clic en el icono de traducción de la columna *Acciones* (*Actualizar clave de traducción*), introduce la nueva etiqueta y confirma. El icono de información contiguo muestra qué etiqueta está en vigor y de dónde procede. Solo cambia la etiqueta; el *Nombre de columna* técnico se mantiene, de modo que los scripts, los mapeos de exportación y las reglas entrenadas siguen funcionando.

### Cambiar el tipo o la tabla

No es posible. Oculta la columna (o elimínala si es tuya) y añade una nueva con el tipo correcto.

### Eliminar una columna

La acción de eliminar solo se ofrece para columnas creadas por tu organización. Las columnas predeterminadas no se pueden eliminar; ocúltalas.

1. Abre el menú de tres puntos de la columna *Acciones* y elige **Eliminar**. En las columnas predeterminadas esta entrada no aparece.
2. Confirma.

Qué ocurre:

* La columna se elimina de la configuración. Los documentos procesados **a partir de ahora** ya no la tienen.
* Los documentos ya extraídos conservan la columna y sus valores hasta que se reinician.
* Las reglas entrenadas que asignaban esta columna siguen funcionando para las demás columnas; la asignación de la columna eliminada se ignora.
* Si la columna está referenciada en un mapeo de exportación o en un script, elimina esa referencia; de lo contrario, la exportación o el script fallará con un error de columna inexistente.

### Deshacer una eliminación

Una columna eliminada no se puede restaurar desde la lista. Añádela de nuevo con el mismo título: el nombre técnico se deriva del título, así que una columna creada con el mismo título recibe el mismo *Nombre de columna* y los mapeos existentes vuelven a coincidir.

## Mejores prácticas <a href="#best-practices" id="best-practices"></a>

### Conserva las columnas predeterminadas de importes y cantidades

Las comprobaciones de línea (*cantidad × precio unitario = total de línea*) y la coincidencia de PO buscan las columnas predeterminadas `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER`. Si en su lugar creas columnas propias para estos valores, las comprobaciones no se ejecutan y la coincidencia de PO informa de columnas obligatorias que faltan. Cambia el *título* si la redacción no te convence; conserva la columna.

### Oculta, no elimines

Las columnas predeterminadas que no necesitas se ocultan, no se eliminan; de todos modos no se pueden eliminar. Para tus propias columnas, ocultar también es la opción más segura mientras no tengas claro si algún script o mapeo de exportación sigue haciendo referencia a la columna.

### Marca como obligatorio solo lo que bloquea la exportación

Toda columna obligatoria tiene que estar rellena en cada fila antes de que un usuario pueda aprobar el documento. Úsalo para valores que el ERP rechaza cuando faltan (por ejemplo, el centro de coste en una exportación contable), no para valores que simplemente resultan útiles.

### Usa *Solo lectura* para valores obtenidos por búsqueda

Los valores que un script o una búsqueda de datos maestros escriben en la tabla (descripción del artículo desde el maestro de artículos, código de impuesto desde el proveedor) deberían ser de solo lectura, para que los usuarios corrijan el origen y no la copia.

### Usa la IA por columna, no por proveedor

En un proveedor con reglas entrenadas, la mayoría de las columnas salen bien de las reglas. Si una columna es poco fiable (descripciones largas que saltan de línea, un descuento que a veces está en otro sitio), activa *Usar IA* solo en esa columna. Las reglas se encargan del resto.

### Nombra las columnas pensando en el ERP, no en el documento

El *Nombre de columna* acaba en los mapeos de exportación y en los scripts. `COST_CENTRE` es más fácil de mapear que `KST` y no cambia cuando un proveedor lo imprime de otra manera.

### Prueba con un documento reiniciado

Después de un cambio, reinicia un documento existente del tipo de documento y ábrelo: la nueva columna aparece, la oculta ha desaparecido y las celdas obligatorias están marcadas. Solo entonces despliégalo a los usuarios.

### Una tabla por estructura de líneas

Crea una segunda tabla solo cuando un tipo de documento tenga realmente dos tablas independientes (por ejemplo, líneas de artículos y una tabla de cargos aparte). Las tablas vacías adicionales aparecen en todos los documentos del tipo.

## Solución de problemas <a href="#troubleshooting" id="troubleshooting"></a>

### La nueva columna no aparece en la pantalla de validación

* El documento se procesó antes de añadir la columna. Los cambios se aplican a los documentos cargados o reiniciados después; **reinicia el documento** (Panel → menú del documento → Reiniciar).
* La columna está **Oculta**. Comprueba el indicador en la lista de Columnas de tabla.
* La columna se añadió a una **tabla distinta** de la que se muestra. La pantalla de validación muestra las tablas del tipo de documento; compara la columna *Nombre de tabla*.
* El documento no es del tipo de documento que configuraste.

### La columna está, pero siempre vacía

* El proveedor tiene **reglas entrenadas** y la nueva columna no está asignada en ellas. Abre uno de los documentos del proveedor en el entrenamiento de tablas y asigna la columna, o activa *Usar IA* en la columna.
* Con la extracción por IA, el valor no es reconocible en el documento (sin encabezado, abreviado, en otro idioma). Añade una [etiqueta de tabla AI](../../../../end-user-and-partner-section/end-user-section/ai-table/ai-table-tags.md) que nombre la columna, o asígnala en el entrenamiento.

### "Column name already exists"

Ya hay una columna con el mismo nombre técnico en la tabla. Si no está en la lista, es una columna predeterminada oculta: el mensaje dice *Please activate it in Table Column settings*. Desactiva *Oculta* en esa columna en lugar de crear una nueva.

### La aprobación está bloqueada por una columna obligatoria

El mensaje en la tabla nombra la columna. Rellena la celda en todas las filas o, si el valor no existe en este documento, desmarca *Obligatoria* en la columna, reinicia el documento e inténtalo de nuevo. Plantéate si la columna debe ser obligatoria en absoluto (consulta [Mejores prácticas](#best-practices)).

### La IA rellena una columna con el valor equivocado

Caso típico: `CHARGES` recibe el total de la línea y entonces todas las filas fallan la comprobación del total de línea con *Line total does not match quantity x unit price (expected …, got …)*, porque los cargos forman parte de la fórmula `cantidad × precio unitario + cargos`.

* Desmarca *Usar IA* en la columna si las reglas entrenadas la capturan correctamente.
* Si el proveedor no tiene reglas, entrena la tabla una vez (entrenamiento de tablas) para que la columna quede vinculada a la posición correcta, u oculta la columna si el proveedor nunca imprime ese valor.
* Como último recurso, *Omitir validación de tabla* (*Skip table validation*) en Más ajustes del tipo de documento desactiva todas las comprobaciones de tabla para todo el tipo de documento; la discrepancia deja de detectarse, y también las columnas obligatorias vacías.

### Coincidencia de PO: "Line Item Table is missing Mandatory column"

La coincidencia de PO necesita las columnas predeterminadas número de artículo, precio unitario, cantidad e importe total. Una de ellas está oculta o se sustituyó por una columna personalizada. Muestra de nuevo la columna predeterminada o asigna el valor a ella en el entrenamiento de tablas.

### Un script o una exportación falla después de eliminar una columna

El script o el mapeo de exportación sigue haciendo referencia al *Nombre de columna* eliminado. Elimina la referencia o añade de nuevo la columna con el mismo título; el nombre técnico se deriva del título y vuelve a coincidir.

## Páginas relacionadas

* [Solución de problemas de extracción de tablas](../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md): calidad de extracción, OCR, E-Text
* [Entrenamiento de Campos de Línea / Tabla de Entrenamiento](../../../setup/document-training/training-line-fields-table-training/README.md): enseña a DocBits dónde está la tabla de un proveedor
* [Tabla AI](../../../../end-user-and-partner-section/end-user-section/ai-table/README.md): lo que el usuario ve en la pantalla de validación
