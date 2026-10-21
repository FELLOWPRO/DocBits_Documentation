# Tarjetas lógicas: variables, conversiones, JSON y triggers

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-e019409102f9-es.png" alt="Tarjetas de conversión y JSON en la biblioteca. Las tarjetas de variables de organización requieren Advanced Builder; las plantillas visibles también dependen de la versión. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos."><figcaption><p>Tarjetas de conversión y JSON en la biblioteca. Las tarjetas de variables de organización requieren Advanced Builder; las plantillas visibles también dependen de la versión. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

Utilice estas tarjetas en el Generador de flujo de trabajo avanzado donde esté disponible la tarjeta seleccionada. La visibilidad de la tarjeta depende de su versión y de las plantillas habilitadas. Las referencias siguientes describen la versión 2. Tenga en cuenta la versión almacenada en un flujo de trabajo existente al comparar sus campos con esta guía.

## Elija la tienda de valor adecuada

Una variable de flujo de trabajo de la organización seleccionada en el panel Variables se comparte entre flujos de trabajo y se guarda independientemente del lienzo. Una etiqueta con nombre utilizada por las tarjetas de conversión, JSON y de comparación de etiquetas pertenece al contexto de ejecución actual. La creación de una etiqueta no crea una variable de organización. Ingrese el nombre de la etiqueta sin un prefijo de almacenamiento interno. Un campo de documento es una tercera fuente de datos independiente.

Una variable de organización y una etiqueta de ejecución permanecen separadas incluso cuando sus nombres coinciden. Seleccione un campo variable compatible o proporcione explícitamente el valor que espera la tarjeta receptora. Consulte [Variables](../advanced-workflow/variables.md) para conocer el alcance de la organización y la persistencia inmediata.

## Acciones de variables organizativas

Primero cree la variable con el tipo correcto y selecciónela en la tarjeta. Una referencia de variable ausente informa `MISSING_VARIABLE`. Las tarjetas que establecen variables registran el valor anterior y nuevo en el registro de tarjetas. Evite datos personales o confidenciales reales en valores de prueba y registros compartidos.

| tarjeta | Entrada requerida | Resultado y ejemplo | Caso de falla o límite |
| --- | --- | --- | --- |
| `ACTION_LOGIC_SET_TEXT_VAR` | Variable de texto y `value` | Almacena texto; por ejemplo, establezca una etiqueta de ruta en `review`. | Un valor faltante es diferente de un valor de texto intencionalmente vacío. |
| `ACTION_LOGIC_SET_NUMBER_VAR` | Variable de tipo Número y numérica `value` | Almacena un número finito; por ejemplo, establezca un umbral en `1000.50`. | Se rechazan los textos numéricos no válidos, infinito y NaN. Utilice un punto decimal, sin símbolo de moneda. |
| `ACTION_LOGIC_CALC_NUMBER` | Variable numérica y `expression` | Almacena el resultado aritmético; `(100 + 20) / 2` da `60`. | Admite literales numéricos, paréntesis, `+`, `-`, `*`, `/`, `%` y `**`. En la expresión no se aceptan nombres, llamadas a funciones ni referencias a campos de documentos. Las expresiones no válidas o la división por cero fallan. |
| `ACTION_LOGIC_SET_BOOLEAN_VAR` | Sí/No variable y `value` | Establece la bandera en Sí o No. | Utilice el valor booleano que ofrece la tarjeta en lugar de un sinónimo de texto libre traducido. |
| `ACTION_LOGIC_INVERT_BOOLEAN` | Sí/No variable | Invierte su valor actual; El sí se convierte en no. | Inicialice la variable antes de confiar en un primer resultado en particular. |

### Acción de referencia de documento

`ACTION_LOGIC_SET_DOCUMENT_VAR` almacena el ID del documento actual en una variable de documento seleccionada. Necesita un documento vigente; sin uno informa `NO_DOCUMENT`. Un flujo de trabajo desencadenado recibe el ID del documento, no un objeto de documento serializado. La implementación marcada no tiene una plantilla de tarjeta de interfaz de usuario inicializada para esta acción, por lo que no espere que aparezca en todos los selectores de tarjetas. Úselo sólo si su administrador confirma que hay una plantilla coincidente disponible; ingresar un ID de documento en el formulario de creación de variables no es un sustituto.

## Etiquetas y conversiones de tipos

Estas acciones utilizan nombres de etiquetas en el contexto de ejecución actual. Produzca la etiqueta de entrada antes de leerla. Falta una etiqueta de entrada o un nombre faltante informa `MISSING_VARIABLE`; una conversión numérica no válida informa un error de configuración. El resultado es una etiqueta nueva o sobrescrita, no un campo de documento extraído.

| tarjeta | Entradas | Salida y ejemplo |
| --- | --- | --- |
| `ACTION_LOGIC_CREATE_TEXT_TAG` | `tag_name`, `value` | Crea una etiqueta de texto; `raw_amount` con valor `125.50`. Se permite un valor de texto vacío. |
| `ACTION_LOGIC_CONVERT_TO_NUMBER` | `input_tag`, `output_tag` | Convierte `125.50` al número `125.5`. Un booleano se convierte en `1` o `0`. Texto como `EUR 125,50` no es una entrada numérica válida. |
| `ACTION_LOGIC_CONVERT_TO_TEXT` | `input_tag`, `output_tag` | Convierte el valor almacenado en texto. No formatea una moneda ni localiza separadores decimales. |
| `ACTION_LOGIC_CONVERT_TO_BOOLEAN` | `input_tag`, `output_tag` | Convierte un booleano existente directamente; un número distinto de cero se vuelve verdadero y cero se vuelve falso. Utilice `true` o `false` para ingresar texto predecible y probar otras representaciones aceptadas. |

### Ejemplo de conversión

1. Cree una etiqueta de texto `raw_amount` con el valor `125.50`.
2. Convierta `raw_amount` a Número, escribiendo en `amount_number`.
3. Utilice un número mayor que con `tag_name` configurado en `amount_number` y `value` configurado en `100`.
4. Verifique que la condición se cumpla correctamente para `125.50`, falle para `100` e informe un error de conversión para `EUR 125,50` en el paso 2.

## Leer valores de JSON

Las tres tarjetas de lectura toman `json_text`, `json_path` y `output_tag`. A pesar de su nombre, `json_text` es el nombre de una etiqueta que contiene JSON, no un cuadro para pegar un documento JSON literal. Produzca esa etiqueta primero, por ejemplo con Crear etiqueta de texto.

Las rutas son claves separadas por puntos e índices de lista basados en cero: `invoice.lines.0.amount`. No utilice la sintaxis JSONPath como `$.invoice.lines[0].amount`. Si falta una clave, un índice no es válido o JSON no es válido, el resultado es `ERROR_CARD_SETUP`; una etiqueta de origen faltante informa `MISSING_VARIABLE`.

| tarjeta | Salida |
| --- | --- |
| `ACTION_LOGIC_JSON_TO_NUMBER` | Valor numérico; El texto numérico se convierte y un booleano se convierte en `1` o `0`. El texto numérico no válido falla. |
| `ACTION_LOGIC_JSON_TO_TEXT` | Representación textual del valor seleccionado. Esta no es una promesa de serialización JSON para objetos anidados. |
| `ACTION_LOGIC_JSON_TO_BOOLEAN` | Un booleano; El texto `true`, `1` o `yes` es verdadero después de minúsculas, mientras que el resto del texto es falso. Los números siguen su valor cero/distinto de cero. |

Para una etiqueta `payload` que contiene el siguiente JSON, leer `invoice.lines.0.amount` en `amount` con JSON en número produce `125.5`:

```json
{"invoice":{"lines":[{"amount":"125.50"}],"approved":false}}
```

Pruebe también una ruta inexistente, un índice fuera de rango y un JSON con formato incorrecto. Una lectura fallida no debe tratarse como un cero válido o una aprobación exitosa.

## Actualizar JSON

Las cuatro tarjetas de escritura toman `json_tag`, `json_path` y `value`. `json_tag` nombra una etiqueta existente que contiene JSON. Actualizan esa etiqueta con JSON serializado. Se aplica la misma sintaxis de ruta separada por puntos; Se pueden crear claves de objetos intermedios faltantes, pero los índices de lista deben identificar los elementos existentes. No amplían una lista ni admiten rutas con comodines.

| tarjeta | Valor y efecto |
| --- | --- |
| `ACTION_LOGIC_JSON_SET_NUMBER` | Un valor numérico, como `125.5`; almacena un número JSON. El texto numérico no válido falla. |
| `ACTION_LOGIC_JSON_SET_TEXT` | Texto, como `review`; almacena una cadena JSON. |
| `ACTION_LOGIC_JSON_SET_BOOLEAN` | El texto `true`, `1` o `yes` se establece como verdadero después de minúsculas; otro texto establece falso. Prefiere `true` y `false`. |
| `ACTION_LOGIC_JSON_SET_JSON` | JSON válido, como `{"status":"review"}`; inserta ese valor analizado, no su texto citado. Error en JSON no válido. |

Por ejemplo, establezca la ruta `invoice.approved` en `true` en `payload` con JSON configurado como booleano. Luego lea la misma ruta con JSON a booleano y verifique que sea verdadero. Antes de continuar, se debe diagnosticar una etiqueta de origen faltante, un JSON no válido o una ruta de acceso no válida en el registro de la tarjeta.

## Condiciones

Las seis condiciones siguientes son la versión 2. Una condición falsa es un resultado empresarial, no una acción exitosa ni un error de ejecución. En una secuencia de condiciones de estilo estándar, evita las siguientes acciones; en un flujo de trabajo avanzado, conecte el resultado a la rama deseada.

| tarjeta | Campos | Evaluación y límite importante. |
| --- | --- | --- |
| `CONDITION_LOGIC_VALUE_EQUALS` | `tag_name`, `value` | Compara exactamente las representaciones de texto, incluido el caso. No utilice esto como verificación de presencia: una etiqueta faltante no se informa automáticamente como un error. |
| `CONDITION_LOGIC_BOOLEAN_IS` | `tag_name` | Comprueba si la etiqueta es verdadera. Una etiqueta faltante se evalúa como falsa. Utilice un booleano real para obtener resultados confiables. |
| `CONDITION_LOGIC_TEXT_CONTAINS` | `tag_name`, `value` | Búsqueda de subcadenas que distingue entre mayúsculas y minúsculas. Una etiqueta faltante se trata como texto vacío. Una cadena de búsqueda vacía coincide; establezca siempre el valor de búsqueda deliberadamente. |
| `CONDITION_LOGIC_NUMBER_LESS` | `tag_name`, numérico `value` | Estrictamente menos que. Una etiqueta faltante o un valor de comparación omitido tiene como valor predeterminado cero; Los datos numéricos no válidos son un error de configuración. |
| `CONDITION_LOGIC_NUMBER_GREATER` | `tag_name`, numérico `value` | Estrictamente mayor que. Un valor igual al umbral no cumple esta condición. Se aplican los mismos valores predeterminados de cero y el mismo comportamiento de error numérico. |
| `CONDITION_LOGIC_EXPRESSION` | `value1`, `operator`, `value2` | Admite `==`, `!=`, `<`, `<=`, `>`, `>=`, `contains`, `not_contains`. Primero intenta la comparación numérica y, de lo contrario, compara el texto. No es un campo arbitrario de expresión de Python. |

Para un número mayor que `100`, pruebe `99`, `100` y `101`. Para Texto contiene `ABC`, pruebe `ABC`, `abc` y una búsqueda vacía. Verifique tanto la rama como el registro; Se omitió un nodo gris y no demuestra una comparación exitosa.

## Desencadenantes

| tarjeta | Configuración | cuando coincide |
| --- | --- | --- |
| `CONDITION_LOGIC_VAR_CHANGED` | Seleccione una variable de organización. La referencia almacenada usa su ID, por lo que cambiar el nombre de la variable no cambia intencionalmente el destino. | Los valores de las variables actuales y anteriores suministrados difieren. Repetir el mismo valor no es un cambio. Una referencia de variable faltante informa `MISSING_VARIABLE`. |
| `CONDITION_LOGIC_WEBHOOK_EVENT` | Opcional `event_name`. | Una carga útil de webhook está presente en el contexto de ejecución del flujo de trabajo. Con un nombre, el valor `event` de la carga útil debe coincidir exactamente; sin nombre, cualquier evento de webhook proporcionado coincide. Ningún evento significa falso. |

Seleccionar el evento Webhook no crea un punto final de webhook público ni su autenticación. Su integración debe suministrar el evento a través de un punto de entrada configurado. Pruebe el evento coincidente, otro evento y ningún evento. Para un disparador de variable, pruebe un cambio de valor real y un valor sin cambios, y evite una cadena que reescriba repetidamente la misma variable compartida.

## Probar y diagnosticar

Valide el gráfico, pruebe cada rama con información representativa e inspeccione los [Registros de flujo de trabajo](../workflow-logs.md). Incluya etiquetas faltantes, JSON no válido, tipos de variables incorrectos, límites numéricos y condiciones falsas. Una prueba sin documento no puede probar una acción dependiente de un documento. Vuelva a verificar la versión de la tarjeta guardada y el estado habilitado antes de confiar en la ejecución automática.
