# Reglas de Transformación

## Visión general

Las reglas de transformación limpian o reescriben datos extraídos **automáticamente** — un campo en el encabezado, una columna en una tabla, filas completas de una tabla o un atributo del documento — cada vez que se procesa un documento y cada vez que se guarda. Reemplazan los pequeños scripts que muchas organizaciones solían escribir para "siempre recortar este campo", "por defecto esta columna a 1", "mapear los códigos de unidad de este proveedor" o "colapsar las líneas de este proveedor en una línea total".

Una regla se define por **tipo de documento** y se ejecuta en cada documento de ese tipo. Las reglas se ejecutan **antes** de la validación, scripts y la conciliación de órdenes de compra, por lo que todo lo que sigue ya ve los valores transformados.

## Cómo acceder

1. Navega a **Configuración → Configuración global → Tipos de documento**.
2. Abre el tipo de documento y elige **Reglas de transformación**. La lista muestra cada regla del tipo con su alcance, objetivo, prioridad y si está activa.
3. Haz clic en **Nueva regla** para abrir el constructor de reglas, o abre una regla existente para modificarla.

## Anatomía de una regla

| Parte                   | Qué es                                                                                                                                                                                                                                                     |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre / clave**      | El nombre que se muestra en listas, mensajes y el historial de conciliación, y una clave técnica que permanece estable cuando renombras la regla.                                                                                                          |
| **Alcance**             | Dónde escribe la regla: un **campo de encabezado**, una **columna de tabla**, una **tabla** (filas completas) o un **atributo del documento**. Ver más abajo.                                                                                              |
| **Objetivo**            | El campo, columna (con su tabla) o tabla a la que la regla escribe.                                                                                                                                                                                        |
| **Origen**              | Opcional. De dónde lee la regla su entrada en lugar del objetivo mismo: `header.<field>` para un campo de encabezado, `doc.<attribute>` para un atributo del documento, `row.<column>` para otra columna de la misma fila (solo alcance columna).          |
| **Cuándo**              | **Siempre**, o **solo cuando** una condición sea verdadera (ver Condiciones).                                                                                                                                                                              |
| **Acciones**            | La lista de transformaciones, aplicadas en orden; la salida de una acción es la entrada de la siguiente.                                                                                                                                                   |
| **Prioridad**           | Las reglas del mismo alcance se ejecutan en orden ascendente de prioridad (luego por clave). Úsalo cuando una regla debe ver el resultado de otra.                                                                                                         |
| **Ejecutar una vez**    | La regla se aplica a un documento **como máximo una vez**. Necesario para acciones que cambiarían el valor nuevamente en cada guardado (subcadena, reemplazo regex, extracción regex) y para reglas de tabla que no deben reconstruir las líneas otra vez. |
| **Registrar ejecución** | Escribe una línea de registro por aplicación — útil mientras ajustas una regla nueva.                                                                                                                                                                      |

### Alcances

| Alcance                    | Escribe en                                                        | Regla típica                                                                                  |
| -------------------------- | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Campo de encabezado**    | un campo extraído del encabezado (número de factura, moneda, …)   | recortar y poner en mayúsculas el número de factura; mapear "EUR€" a "EUR"                    |
| **Columna de tabla**       | una columna en cada fila de una tabla                             | poner por defecto `UNIT_PRICE_PER` a 1; eliminar el prefijo "Art.-Nr." del número de artículo |
| **Tabla**                  | las filas de una tabla                                            | limpiar las líneas y añadir una línea total para un proveedor que se concilia por el total    |
| **Atributo del documento** | un atributo del propio documento (actualmente la suborganización) | enrutar documentos de un proveedor a una suborganización                                      |

Las reglas se ejecutan alcance por alcance en este orden: encabezado → documento → tabla → columna. Por lo tanto, una regla de columna ya ve filas que una regla de tabla añadió.

### Condiciones ("solo cuando")

Una condición compara un valor del documento con una constante. El valor proviene de un campo de encabezado (`header.<field>`), un atributo del documento (`doc.<attribute>`) o, para reglas de columna, una columna de la fila actual (`row.<column>`).

| Operador                                    | Significado          |
| ------------------------------------------- | -------------------- |
| es / no es                                  | comparación exacta   |
| es uno de / no es uno de                    | valor en una lista   |
| contiene, empieza con, termina con          | comparación de texto |
| está vacío / no está vacío                  | no se necesita valor |
| mayor que, menor que, al menos, como máximo | comparación numérica |
| coincide                                    | expresión regular    |

Las condiciones pueden agruparse con **todas** (y) y **cualquiera** (o) y negarse con **no**. Ejemplo: _solo cuando `header.supplier_id` es `20723`_ — la regla se ejecuta solo para un proveedor.

### Acciones

Acciones para campos de encabezado y columnas de tabla (forman una tubería; el valor entra por arriba y sale por abajo):

| Acción          | Efecto                                                                                                                             |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `trim`          | eliminar espacios en blanco (o caracteres dados) a la izquierda, derecha o ambos lados                                             |
| `case`          | poner en mayúsculas, minúsculas, título o capitalizar                                                                              |
| `pad`           | rellenar hasta una longitud con un carácter, a la izquierda o derecha                                                              |
| `truncate`      | cortar a una longitud máxima                                                                                                       |
| `affix`         | añadir un prefijo o sufijo, o eliminar uno                                                                                         |
| `sanitize`      | conservar solo una clase de caracteres (alfanumérico, alfa, numérico, alfanumérico + espacio) o eliminar un conjunto de caracteres |
| `substring`     | tomar una parte del valor por inicio y longitud o fin                                                                              |
| `regex_replace` | reemplazar lo que coincida con una expresión regular                                                                               |
| `regex_extract` | conservar lo que captura una expresión regular                                                                                     |
| `value_map`     | mapear valores a otros valores (opcionalmente sin distinguir mayúsculas, con un valor por defecto)                                 |
| `date_format`   | reformatear una fecha (la entrada debe ser la fecha ISO que DocBits almacena en `value`)                                           |
| `number_format` | reformatear un número                                                                                                              |
| `default`       | establecer un valor solo cuando el campo está vacío                                                                                |
| `set_value`     | establecer un valor fijo, sea cual sea el contenido del campo                                                                      |
| `clear`         | vaciar el campo                                                                                                                    |

Acciones para alcance **tabla** (trabajan sobre filas, no sobre valores, y no pueden mezclarse con las acciones anteriores):

| Acción       | Efecto                                                                                                                                                            |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clear_rows` | eliminar todas las filas de la tabla                                                                                                                              |
| `add_row`    | añadir una fila al final o al principio; cada columna recibe un valor fijo o un valor leído del encabezado (`header.<field>`) o del documento (`doc.<attribute>`) |

{% hint style="info" %}
`substring`, `regex_replace` y `regex_extract` cambian un valor nuevamente cuando se ejecutan sobre un valor ya transformado. Combínalas con **Ejecutar una vez**, o escribe la expresión regular para que una segunda ejecución no tenga nada que cambiar.
{% endhint %}

## Cuándo se ejecutan las reglas

* Durante el procesamiento, después de la extracción y antes de la validación, scripts y conciliación de órdenes de compra.
* En **cada guardado** del documento en el que los datos extraídos hayan cambiado. Las reglas sin **Ejecutar una vez** se aplican nuevamente en cada guardado; porque cada acción excepto las tres anteriores es idempotente, un valor que ya está en la forma objetivo permanece igual.

## Reglas de transformación y conciliación de órdenes de compra

Las reglas de tabla y columna cambian lo que ve el conciliador de órdenes de compra:

* Una regla de tabla que **reconstruye** líneas (por ejemplo, limpiar todas las filas y añadir una línea total) mantiene una conciliación existente mientras produzca **las mismas líneas nuevamente** — los valores se comparan por significado, por lo que `1.0` y `1.00` son la misma línea. Las líneas mantienen su identidad y la conciliación sobrevive a cada guardado.
* Si una regla **reemplaza o elimina líneas que estaban conciliadas**, la conciliación no puede mantenerse. El documento entonces registra qué regla la eliminó, la pantalla de Conciliación de Órdenes de Compra muestra esto como motivo ("_No se pudo guardar la conciliación: la regla de transformación "…" reconstruyó la tabla_") y los administradores reciben un enlace a la regla. El **historial de conciliación** del documento muestra un paso _Reglas de transformación_ antes de la primera etapa de conciliación con las reglas que se ejecutaron.
* El número de líneas después de las reglas es lo que cuentan las [condiciones de activación](https://github.com/Fellow-Consulting-AG/docbits/tree/es/readme/administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) de las reglas de conciliación. Una regla que colapsa una factura en **una** línea solo tiene sentido junto con una regla de conciliación por total que esté activa para documentos de una línea (`[[count(table_lines)]] >= 1`).

## Ejemplos

**Limpiar el número de factura** — campo de encabezado `invoice_id`, siempre: `trim` → `case` upper.

**Poner por defecto la base del precio** — columna de tabla `UNIT_PRICE_PER` de la tabla de líneas, siempre: `default` `1`.

**Mapear los códigos de unidad de un proveedor** — columna de tabla `UNIT` de la tabla de líneas, solo cuando `header.supplier_id` es `10040`: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Una línea total para un proveedor que se concilia por el total** — alcance tabla en la tabla de líneas, solo cuando `header.supplier_id` es `20723`: `clear_rows`, luego `add_row` con `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Combínalo con una regla de conciliación por total cuya condición de activación acepte un documento de una línea.

**Enrutar un proveedor a una suborganización** — atributo del documento `sub_org_id`, solo cuando `header.supplier_id` es uno de `[…]`: `set_value` `<id de suborganización>`.

## Solución de problemas

| Síntoma                                                                 | Qué verificar                                                                                                                                                                                               |
| ----------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| La regla no cambió nada                                                 | ¿Está activa? ¿Coincide el tipo de documento? ¿Es verdadera la condición para este documento (compara el valor exacto, incluyendo espacios)? ¿Ya se aplicó una regla con **Ejecutar una vez** al documento? |
| El valor cambia nuevamente en cada guardado                             | La tubería contiene `substring`, `regex_replace` o `regex_extract`. Activa **Ejecutar una vez** o haz la expresión idempotente.                                                                             |
| Se pierde la conciliación de la orden de compra tras guardar            | Una regla de tabla reemplazó las líneas conciliadas. El motivo en el documento nombra la regla; haz que la regla reproduzca las mismas líneas, o configúrala para **Ejecutar una vez**.                     |
| Una regla de conciliación nunca se ejecuta después de la transformación | La regla cambió el número de líneas; ajusta la condición de activación de la regla de conciliación.                                                                                                         |
