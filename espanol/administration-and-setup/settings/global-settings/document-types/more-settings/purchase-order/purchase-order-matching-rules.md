# Reglas de Coincidencia de Órdenes de Compra

## Introducción: Órdenes de Compra y Gestión de Reglas de OC

La Coincidencia de Órdenes de Compra (OC) es un proceso crítico para asegurar la consistencia entre las Órdenes de Compra (OC) y las facturas entrantes o recibos de mercancías correspondientes. Un conjunto robusto de reglas es esencial para lograr una alta tasa de coincidencia automática, prevenir fraudes y garantizar pagos correctos.

Esta página de configuración se utiliza para definir y gestionar las reglas que determinan _cómo_ los ítems de línea de la OC se emparejan con el documento entrante correspondiente (Factura, Confirmación de Pedido).

{% hint style="info" %}
**Requisito previo:** las reglas de coincidencia solo se usan cuando **PO match server side** está activado para el tipo de documento (Configuración → Tipos de Documento → Más Configuraciones → Orden de Compra). Con el interruptor apagado, DocBits realiza la coincidencia con su comparador incorporado (cantidad, precio unitario, número de ítem, número de orden de compra) e ignora el conjunto de reglas.
{% endhint %}

***

## Cómo Acceder

1.  Navegue a **Configuración --> Configuración Global --> Tipos de Documento**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Seleccione el tipo de documento deseado y haga clic en **Más Configuraciones**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Luego vaya a la Sección Orden de Compra y haga clic en el botón (PO match server side), después haga clic en Configurar Reglas de Coincidencia de OC

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Configuración Global (Reglas Base)

Estas configuraciones establecen el marco que se aplica a todas las reglas de coincidencia:

* **Configuración:** Coincidir Cantidad En
  * **Propósito:** Define qué cantidad de la línea de la orden de compra se compara con la línea del documento — por ejemplo, la cantidad ordenada o la **cantidad abierta de factura** (ordenada menos ya facturada), que es la elección habitual para facturas.
  * **Valores Válidos:** Cantidad u otros campos de cantidad disponibles en el sistema, dependiendo de la estructura de datos (por ejemplo, un campo alternativo de cantidad normalizada).
  * **Dependencia:** Determina la base para todas las reglas de coincidencia que incluyen cantidad en sus criterios de comparación.
* **Configuración:** Tolerancia Estándar (Tolerancia por Defecto)
  * **Propósito:** Define cuánto puede desviarse un valor numérico en el documento respecto al valor de la orden de compra y aún contar como coincidencia. Compensa diferencias de redondeo. Se aplica a **todas las columnas numéricas** con la opción "Permitir Tolerancia" activada — tanto cantidad como precio unitario.
  * **Valor Válido:** Un número decimal. Si se interpreta como un **valor absoluto** (0.005 = una desviación de hasta 0.005 en la cantidad o precio comparado) o como un **porcentaje** (0.5 = 0.5 % del valor comparado) se establece por el **tipo de tolerancia** del conjunto de reglas (`value` o `percent`; los conjuntos nuevos usan `value`). Las tolerancias por ítem (ver [Configuración de tolerancias](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)) anulan la tolerancia estándar para ese ítem.
  * **Dependencia:** Se aplica a reglas que usan campos numéricos para la coincidencia y tienen activada la opción "Permitir Tolerancia".

***

## Lista de Reglas

La Lista de Reglas muestra todas las reglas de coincidencia disponibles y gestiona su orden de ejecución.

#### Estructura y Ejecución

* **Prioridad:** Este campo numérico (por ejemplo, 1, 2, 3) dicta la secuencia de ejecución de las reglas. Las reglas con un número de prioridad menor se intentan primero. Esto permite a los administradores estructurar una jerarquía, comenzando típicamente con las reglas más específicas y estrictas (por ejemplo, coincidencia por número de línea y número de parte) y recurriendo a reglas más amplias o menos restrictivas.
* **Nombre y Descripción:** Proporciona identificación clara y contexto para la regla, explicando los criterios principales usados (por ejemplo, "Regla Estándar No. 1: Coincidencia basada en Número de Línea, ID de Parte y Cantidad").
* **Activo:** Un interruptor simple que permite activar o desactivar instantáneamente la regla sin necesidad de eliminar su configuración.

**Flujo de Ejecución:** El sistema realiza la coincidencia en una secuencia en cascada. Si una regla (por ejemplo, Prioridad 1) coincide exitosamente con un ítem de línea, el proceso para ese ítem se detiene. Si no se encuentra coincidencia, el sistema procede a la siguiente regla en la secuencia de prioridad (por ejemplo, Prioridad 2). Cada ejecución queda registrada en el documento; el **historial de coincidencias** en la pantalla de Coincidencia de Órdenes de Compra muestra qué regla se intentó, cuál coincidió y cuáles se omitieron y por qué.

***

## Configuración de la Regla (Configuraciones Detalladas)

Esta área de configuración detallada define la lógica y criterios específicos para una regla individual.

#### Parámetros Base

* **Tipo de Regla:** Especifica la cardinalidad de la coincidencia.

| Tipo de regla       | Qué hace                                                                                                                                                                                                | Uso típico                                                                      |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| **Coincidencia simple** | Una línea de orden de compra con una línea de documento. Cada columna configurada debe coincidir (dentro de la tolerancia donde esté permitida).                                                         | El caso estándar.                                                              |
| **Coincidencia múltiple** | Varias líneas de orden de compra con una línea de documento, o varias líneas de documento con una línea de orden de compra. Las cantidades se **suman**, el precio unitario se compara como un **promedio**, las otras columnas deben coincidir. | Entregas divididas, una línea de factura que cubre varias líneas de pedido.    |
| **Coincidencia por total** | Compara un **importe** — usualmente el importe neto de la línea del documento contra el **total** de la orden de compra — y coincide toda la orden de compra de una vez.                                | Proveedores que facturan un monto global, facturas de servicios, facturas de una línea. |

* **Coincidencia Automática:** Si está activado, el sistema intentará aplicar esta regla completamente de forma automática. Se requiere alta confianza en los criterios para el procesamiento automático.
* **Coincidencia Manual:** Si está activado, esta regla puede ser presentada o aplicada por un usuario durante el paso de conciliación manual, ofreciéndole un conjunto predefinido de criterios de comparación para resolver excepciones.
* **Regla de Reserva:** Una regla marcada como reserva se ejecuta en una fase posterior, solo para los pares de líneas que aún no han sido coincidentes después de que todas las reglas regulares se hayan ejecutado. Úsela para la regla "más flexible" que debería capturar lo que las reglas estrictas no lograron.

#### Condiciones de Activación

Una regla puede tener **condiciones de activación** — expresiones que deben ser verdaderas antes de que la regla se ejecute. Si una condición es falsa, la regla se **omite para este documento** (el historial de coincidencias la muestra como "no ejecutada" con la razón). Las expresiones usan los conteos de las líneas que se están comparando:

| Expresión                | Significado                                                        |
| ------------------------ | ----------------------------------------------------------------- |
| `[[count(po_lines)]]`    | número de líneas de orden de compra disponibles para la coincidencia |
| `[[count(table_lines)]]` | número de ítems de línea en el documento que están mapeados para la coincidencia |

Compárelos con `==`, `!=`, `>`, `>=`, `<`, `<=` y combine varias condiciones con `&` (y). Ejemplos:

* `([[count(po_lines)]] > 1) & ([[count(table_lines)]] > 1)` — solo para documentos con varias líneas en ambos lados (típico para una regla de coincidencia múltiple).
* `([[count(po_lines)]] == 1) & ([[count(table_lines)]] == 1)` — solo para documentos de una línea contra una orden de una línea.
* `([[count(po_lines)]] >= 1) & ([[count(table_lines)]] >= 1)` — siempre que haya algo para coincidir.

{% hint style="warning" %}
Las condiciones de activación son la razón más común por la que una regla "no hace nada". Una regla de coincidencia por total con la condición `[[count(table_lines)]] > 1` nunca se ejecuta para una factura de una línea — y una [regla de transformación](../../transformation-rules.md) que colapsa la factura en una línea total produce exactamente ese tipo de documento. Verifique los conteos en el historial de coincidencias antes de cambiar la regla en sí.
{% endhint %}

#### Comparación de Columnas (Criterios de Coincidencia)

Esta es la definición central de la lógica de la regla, especificando qué campos deben coincidir entre los documentos.

1. Definición de las Columnas a Comparar:
   * **Columnas de OC:** El campo extraído de los datos de la Orden de Compra (por ejemplo, número de línea).
   * **Columnas de Tabla Extraídas:** El campo correspondiente extraído o analizado del documento entrante (Factura/Confirmación de Pedido) (por ejemplo, `POSITION`).
2. **Tipo de Comparación:** Define la naturaleza de la coincidencia requerida (por ejemplo, Tt para comparación de Texto/Cadena, requiriendo coincidencia exacta carácter por carácter; # para comparación Numérica).
3. **Permitir Tolerancia:** Para campos numéricos (cantidad, precio), activar esta opción indica al sistema que aplique la Tolerancia Estándar Global definida anteriormente. Si _no_ está activada para un campo numérico, los valores deben coincidir exactamente.
4. **Ignorar en Coincidencia Manual:** Si está marcado, este criterio se relaja durante la intervención manual. Esto es útil para campos como descripciones o referencias internas que pueden variar ligeramente, permitiendo al usuario ignorar pequeñas discrepancias no críticas.

**Qué columnas pueden compararse**

| Columna                         | Lado del documento                         | Lado de la orden de compra               | Nota                                                                                                                                                                                                                             |
| ------------------------------- | ------------------------------------------ | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número de línea                 | `POSITION`                                 | `line_number`                            | Texto, exacto. Solo útil cuando el proveedor imprime los números de línea del pedido en el documento.                                                                                                                            |
| Identificador de ítem           | `ITEM_IDENTIFIER`                          | `item_identifier`                        | Texto, exacto. Número de ítem o número de ítem del proveedor, también vía el [Mapa de Número de Ítem del Proveedor](supplier-item-number-map-admin-documentation.md).                                                             |
| Cantidad normalizada efectiva   | `QUANTITY_EFFECTIVE_NORMALIZED`            | `quantity_effective_normalized`          | Numérico. La cantidad seleccionada por **Coincidir Cantidad En**, convertida a la misma unidad en ambos lados (conversión de código de unidad, cantidades "por").                                                                 |
| Precio unitario normalizado efectivo | `UNIT_PRICE_EFFECTIVE_NORMALIZED`          | `unit_price_effective_normalized`        | Numérico. El precio unitario por unidad después de descuentos y después de **Precio Unitario Por** — y, si está activado [Calcular precio unitario de OC](calculate-po-unit-price.md), el precio calculado a partir del importe y cantidad de la línea de pedido. |
| Importe neto                   | `NET_AMOUNT`                               | `total_amount`                           | Numérico. Usado por reglas de coincidencia por total.                                                                                                                                                                           |

**Ejemplo: Regla estricta de coincidencia de OC (`DefaultRule#1`)**

Una regla estricta típica combina verificaciones obligatorias de identidad con verificaciones de valores:

* **Identidad Obligatoria:** Número de Línea e Identificador de Ítem deben coincidir exactamente (comparación de texto, sin tolerancia).
* **Verificaciones de Valor:** Cantidad Normalizada Efectiva y Precio Unitario Normalizado Efectivo deben coincidir (comparación numérica, con tolerancia permitida). Solo si se cumplen los cuatro criterios (con tolerancia para valores) se ejecuta una coincidencia automática.

***

## El conjunto de reglas por defecto

Cada organización comienza con el mismo conjunto de reglas por defecto. Es una buena referencia cuando construya el suyo propio:

| Regla                      | Tipo / prioridad                 | Columnas comparadas                                                       | Condición de activación                                |
| -------------------------- | ------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------------------- |
| `DefaultRule#1`            | coincidencia simple, prioridad 1 | número de línea, identificador de ítem, cantidad (tol.), precio unitario (tol.) | siempre                                              |
| `DefaultMultiMatchRules#1` | coincidencia múltiple, prioridad 1, reserva | identificador de ítem, cantidad (tol.), precio unitario (tol.)         | `count(po_lines) > 1` y `count(table_lines) > 1`      |
| `DefaultTotalMatchRules#1` | coincidencia por total, prioridad 1 | importe neto ↔ total de orden de compra (sin tolerancia)                | `count(po_lines) >= 1` y `count(table_lines) > 1`     |
| `DefaultRule#2`            | coincidencia simple, prioridad 2, reserva | identificador de ítem, cantidad (tol.), precio unitario (tol.)         | siempre                                              |
| `DefaultRule#3`            | coincidencia simple, prioridad 2, reserva | cantidad (tol.), precio unitario (tol.)                                | `count(po_lines) == 1` y `count(table_lines) == 1`    |

Leyéndolo de arriba hacia abajo: primero la regla estricta (número de línea e ítem deben estar impresos en el documento), luego las reservas sin el número de línea, luego un último recurso para documentos de una línea que compara solo cantidad y precio.

***

## Impacto en el Proceso de Coincidencia de OC

El conjunto de reglas definido gobierna directamente la eficiencia e integridad del flujo de trabajo de coincidencia de OC:

* **Priorización y Reservas:** La Prioridad definida asegura que el sistema intente primero el método de coincidencia más confiable. Si las reglas estrictas y de alta prioridad fallan, el sistema recurre a reglas más amplias, buscando minimizar el número de excepciones que se envían a los usuarios.
* **Control de la Calidad de Coincidencia:** Reglas más estrictas (que requieren coincidencias más exactas y menos tolerancia) resultan en menos coincidencias automáticas, pero altamente confiables. Reglas más flexibles aumentan la tasa de coincidencia automática pero elevan el riesgo de falsos positivos.
* **Manejo de Excepciones (Coincidencia Manual):** Al habilitar reglas para Coincidencia Manual, el sistema ofrece opciones estructuradas para los usuarios. Si una transacción no cumple los criterios de coincidencia automática, se convierte en una excepción. El usuario puede entonces intentar resolver la excepción aplicando una regla manual predefinida, que podría tener criterios relajados (por ejemplo, ignorar una pequeña discrepancia de texto según la configuración "Ignorar en Coincidencia Manual").

## Qué más influye en el resultado

* **Cuándo se ejecuta la coincidencia:** durante el procesamiento del documento, cuando un usuario hace clic en **Auto PO Match**, y **en cada guardado** en el que el número de orden de compra cambió o nunca fue consultado antes (por ejemplo, cuando los datos maestros lo completaron después del procesamiento). Un guardado nunca sobrescribe una coincidencia que ya existe.
* **[Reglas de transformación](../../transformation-rules.md)** se ejecutan antes de la coincidencia y pueden cambiar los ítems de línea — y con ellos los conteos de líneas que las condiciones de activación evalúan. Una regla de tabla que reconstruye las líneas mantiene una coincidencia existente mientras las líneas permanezcan iguales; si reemplaza líneas coincidentes, la coincidencia se pierde y el nombre de la regla se muestra como motivo.
* **[Calcular precio unitario de OC](calculate-po-unit-price.md)** cambia qué precio unitario comparan las reglas en el lado de la orden de compra.
* **[Configuración de tolerancias](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)** y **[estatus deshabilitados](purchase-order-disable-statuses.md)** deciden qué tan estricta es la comparación y qué líneas de orden de compra se ofrecen en absoluto.

## Solución de problemas

| Síntoma                                                        | Qué verificar                                                                                                                                                                                    |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| "Sin coincidencia" aunque todos los valores coincidan          | Abra el historial de coincidencias: qué regla se ejecutó, en qué columna falló (la desviación se muestra por columna), ¿la regla fue omitida por una condición de activación?                      |
| Precio unitario no coincide exactamente por la tasa de impuesto | El total de la orden de compra incluye impuestos; active [Calcular precio unitario de OC](calculate-po-unit-price.md) (importe neto primero) o compare el importe neto de la línea.                 |
| Una regla de coincidencia por total nunca se ejecuta           | Su condición de activación requiere más de una línea de documento. Establezca `[[count(table_lines)]] >= 1` o no colapse las líneas con una regla de transformación.                               |
| El conjunto de reglas no tiene ningún efecto                   | **PO match server side** está desactivado para el tipo de documento, o el conjunto de reglas modificado aún está en borrador — active la versión.                                               |

***

## Personalizar las Reglas de Coincidencia de OC

Para editar las reglas de Coincidencia de OC, la versión por defecto puede clonarse haciendo clic en **"Configurar Versionado"** y usando la opción **"Clonar como Borrador"** desde las opciones disponibles en la tarjeta

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>