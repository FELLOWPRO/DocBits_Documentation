# Reglas de validación personalizadas



{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/es.mp4" %}

## Descripción general

Las reglas de validación personalizadas permiten a un administrador definir **sus propias comprobaciones** sobre los datos que DocBits extrae de un documento, sin escribir un script y sin esperar a un cambio del producto.

Una regla responde a tres preguntas:

1. **Dónde** se muestra el problema. En un campo de cabecera o en una celda de una fila de tabla.
2. **Cuándo** se aplica la regla. Siempre, o solo para los documentos (o filas) que cumplen una condición; consulte [Rule Conditions (Applies when)](rule-conditions-applies-when.md).
3. **Qué** debe cumplirse. Un campo debe estar rellenado, coincidir con un formato, estar dentro de un rango, coincidir con una lista, compararse correctamente con otro campo o cuadrar.

Cuando la comprobación falla, DocBits marca el campo o la celda en la **pantalla de validación** y muestra su mensaje, exactamente igual que una comprobación integrada. Con la gravedad **Error**, el documento no se puede validar hasta que se corrija el problema; con **Advertencia**, el usuario solo ve un aviso.

Las reglas se definen por **tipo de documento** y se ejecutan en cada documento de ese tipo: durante el procesamiento y cada vez que se guarda el documento.

### Problemas que resuelven

| Requisito de negocio | Sin reglas personalizadas | Con una regla personalizada |
| --- | --- | --- |
| Las facturas alemanas de más de 250 EUR deben mostrar el número de identificación fiscal del proveedor | un script, o los usuarios deben recordarlo | **Obligatorio** en Supplier Tax ID, *applies when* el origen es DE y el importe total es mayor que 250 |
| Los números de factura de un proveedor siempre tienen el aspecto `INV-123456` | los errores tipográficos llegan al ERP | **Patrón** `^INV-\d{6}$` en Invoice Number para ese proveedor |
| Cada línea de artículo necesita una cantidad superior a cero | se exportan líneas con cantidad 0 | **Rango** (mínimo 0,01) en la columna Quantity |
| La fecha de vencimiento no debe ser anterior a la fecha de la factura | ejecuciones de pago erróneas | **Comparar campos**: Due Date igual o posterior a Invoice Date |
| Las líneas deben sumar el importe neto | solo la comprobación integrada fija | **Fórmula** `sum(row.NET_AMOUNT) == header.total_net_amount` con su propia tolerancia |
| Solo se permiten las monedas que conoce su ERP | errores de exportación en el ERP | **Lista de valores** en Currency |
| Avisar a los usuarios de valores inusuales sin bloquearlos | no es posible | cualquier regla con la gravedad **Advertencia** |


## Activar las reglas de validación personalizadas

Las reglas de validación personalizadas se activan **por tipo de documento**. No existe un interruptor para toda la organización.

1. Vaya a **Ajustes → Ajustes generales → Tipos de documento**.
2. En la tarjeta del tipo de documento, haga clic en el icono de **ajustes** (engranaje).
3. Abra la sección **Reglas de validación personalizadas** y active el interruptor.
4. Haga clic en **Gestionar reglas de validación** para abrir la lista de reglas.

<figure><img src="../../../../.gitbook/assets/validation-cvr-toggles.png" alt="Los interruptores de reglas en los ajustes adicionales de un tipo de documento"><figcaption><p>Los interruptores de Manage Layouts, Custom Validation Rules y Transformation Rules</p></figcaption></figure>

A partir de ese momento, la tarjeta del tipo de documento también muestra un enlace **Reglas de validación** y un enlace **Registros** para los registros de ejecución.

<figure><img src="../../../../.gitbook/assets/validation-cvr-card-links.png" alt="La tarjeta del tipo de documento con el enlace Validation Rules"><figcaption><p>Los enlaces de la tarjeta del tipo de documento</p></figcaption></figure>

{% hint style="warning" %}
**El interruptor sustituye las comprobaciones de importes integradas.** Mientras las reglas de validación personalizadas estén activadas para un tipo de documento, las comprobaciones fijas “importe total = importe neto + importe de impuestos” y las comprobaciones de importe de línea / descuento **no** se ejecutan para él; las reglas configurables ocupan su lugar. Recree como reglas las comprobaciones en las que confía (consulte las [recetas](#recetas)) antes de activarlo. Al desactivar el interruptor se restablecen las comprobaciones integradas. El resto de las validaciones de campos (campos obligatorios, formatos, datos maestros) siguen ejecutándose.
{% endhint %}

## La lista de reglas

**Tipos de documento → (tipo de documento) → Reglas de validación** muestra todas las reglas del tipo de documento.

<figure><img src="../../../../.gitbook/assets/s150-validation-rules-list-es.png" alt="Reglas de validación personalizadas con los nombres ocultos."><figcaption><p>Reglas de validación personalizadas con los nombres ocultos.</p></figcaption></figure>

Cada tarjeta muestra el nombre y la descripción de la regla, y las insignias de su **nivel** (Header / Line / Table), **gravedad** (Error / Warning), el **campo** al que se asocia el error y su **origen**. Utilice el interruptor de la derecha para activar o desactivar una regla, y el menú **⋮** para duplicarla o eliminarla. Filtre la lista por nivel (**All / Header / Line / Table**) y por estado (**All / Active / Inactive**), o búsquela.

### Sistema de Reglas por defecto, Personalizadas y Personalizadas

| Origen | Qué es | Qué puede hacer |
| --- | --- | --- |
| **Configuración predeterminada del sistema** | Una regla incluida con DocBits para todas las organizaciones. | No se puede editar directamente: el constructor muestra “This is a system default rule and cannot be edited.” Haga clic en **Personalizar** para crear su propia copia editable, o desactívela para detenerla en su organización. |
| **Personalizado** | Una regla System default que su organización ha modificado o desactivado. | Edítela como una regla propia. **Restablecer a valores predeterminados** elimina su copia y restaura la original. |
| **A medida** | Una regla creada por su organización. | Editar, **Duplicar**, **Borrar**. |

Los cambios en las reglas System default nunca afectan a otras organizaciones.

## Crear una regla

Haga clic en **Nueva regla**. El constructor tiene tres pasos. **Regla de prueba** y **Guardar** están en la parte superior derecha.

### Paso 1 — Name & scope

<figure><img src="../../../../.gitbook/assets/validation-cvr-step1.png" alt="Paso 1 del constructor de reglas de validación para una regla de campo de cabecera"><figcaption><p>Paso 1 para una regla de campo de cabecera</p></figcaption></figure>

| Ajuste | Qué hace |
| --- | --- |
| **Nivel de regla** | Qué examina la regla y dónde se muestra el error; consulte [Niveles de regla](#niveles-de-regla). |
| **Gravedad** | **Error** marca el campo como no válido y bloquea la validación. **Advertencia** muestra el mensaje pero nunca bloquea. |
| **Nombre de la regla** | Se muestra en la lista y a los administradores. Haga que describa la regla (“Supplier tax ID required for German invoices”). |
| **Clave de la regla** | Una clave técnica generada a partir del nombre. Se mantiene igual cuando más adelante cambia el nombre de la regla. Haga clic en el lápiz para elegir su propia clave antes del primer guardado; después queda fija. |
| **Descripción** | Explicación opcional para otros administradores. |
| **Nombre de la tabla** | *Solo Table line.* La tabla cuyas filas se comprueban, por ejemplo `INVOICE_TABLE`. |
| **Attach error to field / column** | El campo (o, en las líneas de tabla, la columna) que muestra el error en la pantalla de validación. |

#### Niveles de regla

| Nivel | Se ejecuta | El error se muestra en | Puede leer | Regla típica |
| --- | --- | --- | --- | --- |
| **Campo de encabezado** | una vez por documento | un campo de cabecera | `header.*`, `doc.*` | “Supplier tax ID is required for German invoices” |
| **Línea de la tabla** | una vez por cada fila de la tabla seleccionada | la celda de la fila que falla | `row.*` (la fila actual), `header.*`, `doc.*` | “Quantity must be greater than zero” |
| **Tabla entera** | una vez por documento, considerando todas las filas conjuntamente | un campo de cabecera | totales de las filas (`sum()`, `count()`, `min()`, `max()`), `header.*`, `doc.*` | “The line net amounts must add up to the net amount” |

<figure><img src="../../../../.gitbook/assets/validation-cvr-line-step1.png" alt="Paso 1 para una regla de línea de tabla"><figcaption><p>Una regla de línea de tabla: la tabla y la columna que muestra el error</p></figcaption></figure>

### Paso 2 — Applies when

Decida si la regla se ejecuta para todos los documentos o solo para algunos. Déjelo vacío para comprobar todos los documentos. En caso contrario, añada líneas de condición (por ejemplo, “Document Origin is Deutsch” y “Total Amount greater than 250”) y combínelas con **Todos** / **CUALQUIER** y grupos anidados.

<figure><img src="../../../../.gitbook/assets/validation-cvr-applies-when.png" alt="Una condición Applies when"><figcaption><p>La comprobación solo se ejecuta para documentos alemanes de más de 250 con EUR o sin moneda</p></figcaption></figure>

En las reglas de línea de tabla, la condición también puede utilizar las columnas de la fila actual y se evalúa **fila por fila**: las filas que no coinciden simplemente no se comprueban.

<figure><img src="../../../../.gitbook/assets/validation-cvr-row-condition.png" alt="Una condición de fila"><figcaption><p>Solo se comprueban las líneas de artículo (filas con número de artículo)</p></figcaption></figure>

Las condiciones se explican en detalle (cada campo, operador y regla de comparación, con muchos ejemplos) en [Rule Conditions (Applies when)](rule-conditions-applies-when.md).

### Paso 3 — Verificar: lo que debe ser cierto

Elija una comprobación. Los ajustes situados debajo de las tarjetas cambian según la comprobación elegida.

<figure><img src="../../../../.gitbook/assets/validation-cvr-step3-checks.png" alt="Paso 3 con la comprobación Required seleccionada"><figcaption><p>Las siete comprobaciones. Required no necesita más ajustes</p></figcaption></figure>

#### Required — el campo debe tener un valor

<figure><img src="../../../../.gitbook/assets/validation-cvr-an-required.png" alt="Una comprobación Required"><figcaption><p>Una comprobación Required: sin más ajustes</p></figcaption></figure>

Falla cuando el campo está vacío (ausente o solo con espacios). Sin más ajustes.

Úsela junto con **Se aplica cuando** para que un campo sea obligatorio **de forma condicional**. Un campo que siempre debe estar rellenado se configura mejor como campo obligatorio en los ajustes de campos.

> *Se requiere Impuesto de Proveedor ID* — se aplica cuando *El Origen del Documento es Deutsch* y *Monto Total mayor a 250*.

#### Formula — los importes deben cuadrar

<figure><img src="../../../../.gitbook/assets/validation-cvr-an-formula.png" alt="Una comprobación Formula"><figcaption><p>Una fórmula de tabla completa con una tolerancia y marcadores de posición en el mensaje</p></figcaption></figure>

Una comparación aritmética. La expresión contiene exactamente **una** comparación (`==`, `!=`, `>`, `>=`, `<`, `<=`); ambos lados pueden usar `+ - * /`, números, paréntesis y referencias a campos.

* Haga clic en los chips situados debajo de la expresión para insertar funciones y prefijos de campos: `sum()`, `count()`, `min()`, `max()`, `default()`, `coalesce()`, `header.`, `doc.`. Mientras escribe un nombre de campo, se abre una lista de campos coincidentes.
* `sum(row.NET_AMOUNT)`, `count(row.ITEM_NUMBER)`, `min(...)`, `max(...)` funcionan sobre todas las filas y solo están disponibles en el nivel **Tabla entera**. `count()` cuenta las filas en las que la columna está rellenada.
* `default(header.discount, 0)` usa `0` cuando el campo está vacío; `coalesce(header.a, header.b, 0)` usa el primer valor rellenado.
* **Tolerancia**: para `==` y `!=`, las diferencias de hasta este importe se consideran iguales. Utilice `0.01` o `0.05` para absorber redondeos. No tiene efecto en `<`, `>`, `<=` ni `>=`.
* Los importes vacíos o ilegibles cuentan como `0`. Una división por cero omite la regla en lugar de provocar un error.
* En el mensaje de error, `{actual}` se sustituye por el resultado del lado izquierdo y `{expected}` por el resultado del lado derecho.

Ejemplos:

| Finalidad | Nivel | Expresión | Tolerancia |
| --- | --- | --- | --- |
| Los totales de cabecera son coherentes | Header field | `header.total_amount == header.total_net_amount + header.total_tax_amount` | 0.01 |
| Las líneas suman el importe neto | Whole table | `sum(row.NET_AMOUNT) == header.total_net_amount` | 0.05 |
| Importe de línea = cantidad × precio unitario | Table line | `row.NET_AMOUNT == row.QUANTITY * row.UNIT_PRICE` | 0.01 |
| Impuestos no superiores al 19 % del importe neto | Header field | `header.total_tax_amount <= header.total_net_amount * 0.19` | – |
| Al menos una línea | Whole table | `count(row.ITEM_NUMBER) >= 1` | 0 |

#### Pattern — coincidir con un formato / regex

<figure><img src="../../../../.gitbook/assets/validation-cvr-an-pattern.png" alt="Una comprobación Pattern"><figcaption><p>Una comprobación Pattern con una expresión regular</p></figcaption></figure>

El valor debe coincidir con una **expresión regular**. La expresión busca dentro del valor, por lo que debe anclarla con `^` (inicio) y `$` (fin) cuando todo el valor deba coincidir. Marque **Coincidencia que no distingue entre mayúsculas y minúsculas** si las mayúsculas y minúsculas no importan.

| Formato | Expresión regular |
| --- | --- |
| `INV-` seguido de seis dígitos | `^INV-\d{6}$` |
| NIF-IVA alemán | `^DE\d{9}$` |
| Pedido de compra que empieza por 45 y tiene 10 dígitos | `^45\d{8}$` |
| Solo dígitos | `^\d+$` |
| IBAN (comprobación aproximada) | `^[A-Z]{2}\d{2}[A-Z0-9]{11,30}$` |

#### Range — entre mínimo y máximo

<figure><img src="../../../../.gitbook/assets/validation-cvr-an-range.png" alt="Una comprobación Range"><figcaption><p>Range solo con mínimo: las cantidades deben ser al menos 0,01</p></figcaption></figure>

El valor debe ser un número comprendido entre **Mínimo** y **Máximo** (ambos incluidos). Rellene uno o ambos. Un valor que no sea un número falla. Se entienden importes con formato como `1.234,56`.

#### Compare fields — p. ej., fecha de vencimiento ≥ fecha de factura

<figure><img src="../../../../.gitbook/assets/validation-cvr-an-compare.png" alt="Una comprobación Compare fields"><figcaption><p>Compare fields: comparar un campo con otro campo, con hoy o con un valor fijo</p></figcaption></figure>

Compara el valor de un campo con otro campo, con **hoy** o con un valor fijo, mediante *igual a*, *distinto de*, *mayor que*, *menor que*, *igual o posterior a (≥)* o *igual o anterior a (≤)*. Los números se comparan como números y las fechas como fechas.

* Due Date **igual o posterior a (≥)** Invoice Date
* Invoice Date **igual o anterior a (≤)** hoy: sin facturas con fecha futura
* Discount **menor que** 100

#### Valores permitidos — de una lista fija

<figure><img src="../../../../.gitbook/assets/validation-cvr-an-allowed.png" alt="Una comprobación Allowed values"><figcaption><p>Allowed values: un valor por línea, opcionalmente sin distinguir mayúsculas</p></figcaption></figure>

El valor debe ser uno de los valores que usted escriba, **un valor por línea**. Opcionalmente, sin distinguir mayúsculas de minúsculas. Adecuado para listas cortas y estables (`EUR`, `CHF`, `USD`).

#### List of Values — de un LOV con nombre

<figure><img src="../../../../.gitbook/assets/validation-cvr-an-lov.png" alt="Una comprobación List of Values"><figcaption><p>List of Values: los valores proceden de una lista con nombre de los ajustes</p></figcaption></figure>

Como *Allowed values*, pero los valores proceden de una **Lista de valores** compartida que se gestiona en **Settings › List of Values**. Elija la lista en lugar de volver a escribirla; cuando la lista cambia, la regla usa los nuevos valores (tras un breve retraso de caché). Solo cuentan los valores de las entradas de la lista, no sus etiquetas.

{% hint style="info" %}
Salvo **Obligatorio**, todas las comprobaciones **se superan cuando el valor está vacío**. Una regla Pattern sobre el pedido de compra no se queja de las facturas sin pedido de compra. Si un valor vacío también es un problema, añada una regla Required o limite la regla con *Applies when … is not empty*.
{% endhint %}

#### Mensaje de error y código de error

* **Mensaje de error mostrado al usuario que procesa el mensaje.**: el texto de la pantalla de validación. Indique qué está mal **y** qué hacer: “Supplier tax ID is missing. German invoices over 250 EUR must show it.”
* **Código de error**: un código técnico corto, por ejemplo `REQUIRED_CONDITIONAL`, `FORMAT_MISMATCH`, `OUT_OF_RANGE`, `DATE_ORDER`, `LINES_HEADER_MISMATCH`, `VALUE_NOT_ALLOWED`. Aparece en las exportaciones y permite agrupar errores.

## Probar regla

Haga clic en **Regla de prueba** para ejecutar la versión actual de la regla, guardada o no, contra un documento. Introduzca un **ID del documento** o cambie a **Por documento JSON** y pegue datos extraídos. **No se guarda nada** y el documento no se modifica.

El resultado es uno de tres desenlaces:

| Resultado | Significado |
| --- | --- |
| **La regla falló: se produjo un error.** | La condición coincidió y la comprobación falló. El mensaje se muestra exactamente como lo vería el usuario. |
| **Se aprobó la regla** | La condición coincidió y la comprobación se superó. Las reglas de línea de tabla muestran el resultado por fila (“4 of 4 checked rows passed”). |
| **Regla omitida: el ámbito no coincide.** | La condición *Applies when* era falsa para este documento, por lo que no se comprobó nada y no se generó ningún error. |

<figure><img src="../../../../.gitbook/assets/validation-cvr-test-dialog.png" alt="Test rule: regla fallida"><figcaption><p>La factura alemana no tiene número de identificación fiscal del proveedor: la regla falla con el mensaje configurado</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/validation-rule-test-skipped.png" alt="Test rule: regla omitida"><figcaption><p>La misma regla con el umbral elevado a 1000: la factura (469,18) queda fuera del ámbito, por lo que la regla se omite</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/validation-rule-line-test.png" alt="Test rule: resultados por fila"><figcaption><p>Una regla de línea de tabla informa de cada fila comprobada</p></figcaption></figure>

Pruebe cada regla nueva al menos con un documento que deba fallar, uno que deba superarla y uno que deba omitirse.

## Cuándo se ejecutan las reglas

* **Durante el procesamiento**, junto con las demás validaciones, después de las reglas de extracción y transformación.
* **En cada guardado** del documento en la pantalla de validación.
* **Tras un cambio de regla**, los documentos existentes **no** se vuelven a comprobar todos a la vez. Cada documento se vuelve a comprobar con las nuevas reglas la próxima vez que se guarde o se reprocese. Los documentos ya exportados no se ven afectados.
* Las reglas se ejecutan por orden de prioridad (y después por clave). Un campo muestra **un** error: si dos reglas fallan en el mismo campo, gana la primera; las reglas posteriores no lo sobrescriben.
* Las advertencias se recopilan por separado y nunca ocultan un error.
* Si una regla no se puede evaluar (por ejemplo, una división por cero en una fórmula), se omite. Una regla defectuosa nunca marca un documento como no válido por error.


## Recetas

Copie estas reglas como punto de partida. Las claves de campos y columnas son las del tipo de documento estándar **Factura**; adáptelas a sus tipos de documento.

**1. Número de identificación fiscal del proveedor en facturas alemanas de más de 250 EUR**
Header field · Error · asociar a *Supplier Tax ID* · Applies when **Todos**: *Document Origin* is *Deutsch*, *Total Amount* greater than *250* · Check **Obligatorio** · Mensaje “Supplier tax ID is missing. German invoices over 250 EUR must show it.” · Código `REQUIRED_CONDITIONAL`.

**2. Los totales de cabecera cuadran** (sustituye la comprobación integrada)
Header field · Error · asociar a *Total Amount* · siempre · **Fórmula** `header.total_amount == header.total_net_amount + header.total_tax_amount`, tolerancia `0.01` · Mensaje “Total {actual} does not equal net plus tax ({expected}).”

**3. Las líneas suman el importe neto** (sustituye la comprobación integrada)
Whole table · Error · asociar a *Total Net Amount* · siempre · **Fórmula** `sum(row.NET_AMOUNT) == header.total_net_amount`, tolerancia `0.05` · Mensaje “Line net amounts add up to {actual}, but the invoice net amount is {expected}.” · Código `LINES_HEADER_MISMATCH`.

**4. La cantidad debe ser positiva en las líneas de artículo**
Table line · Error · tabla `INVOICE_TABLE`, columna `QUANTITY` · Applies when *row.ITEM_NUMBER* is not empty · **Rango** mínimo `0.01` · Código `OUT_OF_RANGE`.

**5. Importe de línea = cantidad × precio unitario**
Table line · Warning · columna `NET_AMOUNT` · siempre · **Fórmula** `row.NET_AMOUNT == row.QUANTITY * row.UNIT_PRICE`, tolerancia `0.01`.

**6. Formato del número de factura de un proveedor**
Campo de encabezado · Error · *Número de factura* · Aplica cuando *Proveedor ID* es *20723* · **Patrón** `^INV-\d{6}$`.

**7. La fecha de vencimiento no es anterior a la fecha de la factura**
Header field · Error · *Due Date* · siempre · **Comparar campos** Due Date *on or after (≥)* Invoice Date · Código `DATE_ORDER`.

**8. Sin facturas con fecha futura**
Campo de encabezado · Error · *Fecha de factura* · siempre · **Comparar campos** Fecha de factura *en o antes (≤)* hoy.

**9. Solo monedas aprobadas (solo aviso)**
Header field · **Advertencia** · *Currency* · siempre · **Lista de valores** *approved_currencies* · Código `VALUE_NOT_ALLOWED`.

**10. Pedido de compra obligatorio a partir de 5.000**
Campo de encabezado · Error · *Orden de Compra* · Aplica cuando *Monto Total* mayor a *5000* · **Obligatorio**.

## Buenas prácticas

* **Empiece como advertencia.** Guarde una regla nueva con la gravedad **Advertencia**, obsérvela durante unos días (Test rule) y después cámbiela a **Error**.
* **Una regla, un mensaje.** Varias reglas pequeñas con mensajes claros son más fáciles de entender que una fórmula grande.
* **Utilice Applies when en lugar de copias.** Una regla con una condición es mejor que cinco copias para cinco proveedores.
* **Sea tolerante con el dinero.** Dé siempre una tolerancia a las fórmulas de importes.
* **Ponga a las reglas el nombre de la regla de negocio**, no de la técnica (“Due date not before invoice date”, no “Compare rule 3”).

## Resolución de problemas

| Síntoma | Qué comprobar |
| --- | --- |
| La regla nunca genera un error | ¿Está activada la función para el tipo de documento y la regla está **Activo**? Ejecute **Regla de prueba** en el documento: “skipped” significa que *Applies when* era falso. |
| No se informa de un campo vacío | Solo **Obligatorio** informa de valores vacíos. Añada una regla Required. |
| Las comprobaciones de totales integradas han desaparecido | Es lo esperado mientras las reglas personalizadas están activadas. Recréelas como reglas Formula (recetas 2 y 3). |
| Una regla modificada no tiene efecto en un documento | Los documentos se vuelven a comprobar en su siguiente guardado. Guarde o reprocese el documento. |
| Un Pattern coincide con valores que no debería | Los patrones buscan dentro del valor. Ancle con `^` y `$`. |
| Solo se muestra uno de dos errores en un campo | Un campo solo muestra la primera regla que falla. Ajuste las prioridades o asocie una de las reglas a otro campo. |
| Faltan columnas de tabla en *Applies when* | Solo están disponibles en el nivel **Línea de la tabla**. |
| La regla System default no se puede cambiar | Haga clic en **Personalizar** para crear su propia copia. |

## Relacionado

* [Rule Conditions (Applies when)](rule-conditions-applies-when.md) — las condiciones en profundidad
* [Transformation Rules](transformation-rules.md) — corrija los valores antes de que se validen
* [Layout Selection Rules](layout-manager/layout-selection-rules.md) — elija el diseño que utiliza un documento
* [Validación de configuración y puntuación de coincidencia](fields/setting-validation-and-match-score.md) — ajustes de validación por campo
