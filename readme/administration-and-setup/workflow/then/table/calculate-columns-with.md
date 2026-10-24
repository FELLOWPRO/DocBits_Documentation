# Calcular columnas con

La tarjeta calcula una operación entre dos columnas de una tabla y guarda el resultado en otra columna de cada fila.

## Cuándo y dónde utilizarla

Utilícela cuando necesite calcular importes por línea antes de la siguiente acción del flujo de trabajo; por ejemplo, **cantidad × precio unitario**. Añádala a **Entonces**, en la categoría de tarjetas de tabla que esta versión de la interfaz denomina **Cuadro**. Compruebe primero que los valores de entrada son numéricos y están completos.

<figure><img src="../../../../.gitbook/assets/workflow-card-calc-columns-v2-configured-es-20261024.png" alt="Tarjeta versión 2: INVOICE_TABLE, Cantidad × Precio unitario → columna TOTAL_AMOUNT. La interfaz muestra «Importe total factura» para esta columna de resultado por línea y repite el nombre de la tabla." width="650"><figcaption><p>Tarjeta versión 2: INVOICE_TABLE, Cantidad × Precio unitario → columna TOTAL_AMOUNT. La interfaz muestra «Importe total factura» para esta columna de resultado por línea y repite el nombre de la tabla.</p></figcaption></figure>

## Vídeo de administración

**35 segundos · español.** Javier explica cuándo utiliza la tarjeta, configura la multiplicación y muestra los resultados guardados.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v1/es.mp4" %}

[Reproducir el vídeo con subtítulos en español](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v1/es.html) · [Leer la transcripción](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/workflow-card-calc-columns-admin/v1/es.txt)

El administrador y su voz son sintéticos. La interfaz corresponde a una organización de demostración de DocBits con una factura ficticia.

## Configuración de la tarjeta

| Campo | Selección del ejemplo |
| --- | --- |
| Tabla | `INVOICE_TABLE` |
| Primera columna | `QUANTITY` — Cantidad |
| Operación | `*` — multiplicación |
| Segunda columna | `UNIT_PRICE` — Precio unitario |
| Columna de resultado | `TOTAL_AMOUNT` |

También están disponibles `+` (sumar), `-` (restar) y `/` (dividir). El orden de las columnas importa para la resta y la división. Seleccione los identificadores configurados en su organización.

<!-- workflow-card-practical-example-20261021 -->

## Ejemplo práctico

Una factura contiene las siguientes posiciones. La columna de resultado aún no existe antes del cálculo:

| Fila | Cantidad | Precio unitario | Resultado guardado en `TOTAL_AMOUNT` |
| --- | ---: | ---: | ---: |
| 1 | 2 | 10 | 20 |
| 2 | 3 | 4 | 12 |

En el ejemplo del vídeo, la tarjeta crea la columna de resultado y los valores **20,00** y **12,00** siguen visibles después de volver a abrir la factura. Los importes originales de `NET_AMOUNT` se conservan. Si ya hay valores en la columna de resultado elegida, el cálculo los sustituye.

## Comprobaciones y contraejemplos

- Revise las dos columnas de entrada y compruebe los valores guardados después del cálculo.
- Un precio ausente puede producir cero en el ejemplo mostrado; ese cero no demuestra que los datos estén completos. Valide los datos de entrada antes de calcular.
- Un texto como `ABC` en lugar de un número provoca un error de cálculo. Corrija el dato y vuelva a comprobar el caso.
- Los casos de precio ausente y texto no numérico de la gráfica son resultados esperados para ilustrar las comprobaciones; no son ejecuciones de la factura de dos filas mostrada.
