---
description: >-
  De dónde viene el valor de un campo de cabecera y cómo se crea: la
  explicación detrás de la Comprobación de campos de cabecera en la pantalla de
  validación.
---

# Comprobación de campos de cabecera: de dónde vienen los datos

El botón **Comprobación de campos de cabecera** está junto a **Guardar** en la pantalla de validación. Abre el informe *¿De dónde viene cada valor?*: para cada campo de cabecera muestra qué había en el documento, qué cambió el valor por el camino, qué muestra DocBits ahora y por qué.

Esta página explica cómo se crea un valor y qué significa cada fuente. No se necesitan conocimientos técnicos.

{% hint style="info" %}
La Comprobación de campos de cabecera forma parte del módulo **Analytics**. Si el botón aparece en gris, un administrador puede concedérselo a su rol en **Configuración › Roles**.
{% endhint %}

## Un valor siempre se crea en este orden

| Paso | Qué ocurre |
| --- | --- |
| **1. Leer** | El valor se lee del documento: mediante una regla entrenada, mediante la IA o directamente desde una factura electrónica. |
| **2. Transformar** | Los scripts y las reglas de transformación del cliente modifican el valor leído: lo acortan, lo completan o ajustan su formato. |
| **3. Buscar** | El valor se busca en los datos maestros. Si se encuentra algo, el registro de datos maestros sustituye al valor leído. |
| **4. Mostrar** | El usuario solo ve el resultado. Lo que ocurrió por el camino lo muestra la Comprobación de campos de cabecera. |

Los pasos 2 y 3 no siempre se ejecutan, pero cuando lo hacen, cambian el valor. De ahí vienen la mayoría de los casos reportados.

## Las fuentes: qué significa cada una

Los iconos son los mismos que muestra el informe en la columna **Acción** y en la barra de filtros superior.

### Regla entrenada

DocBits recuerda dónde está un campo en este tipo de documento, porque alguien lo marcó allí una vez.

* **Ejemplo:** proveedor “Bornemann”, siempre en el mismo lugar, arriba a la izquierda.
* **Si es incorrecto:** marque el lugar correcto en el documento y guarde; la regla aprende de ello.

### IA

Sin patrón fijo. La IA lee el documento como una persona y decide por sí misma qué texto pertenece a qué campo.

* **Ejemplo:** fecha de factura, importes, condiciones de pago.
* **Si es incorrecto:** corríjalo. Puede activarse y desactivarse en **Configuración › Campos de cabecera OCR**.

### Factura electrónica

Con XRechnung o ZUGFeRD no se reconoce nada: el valor ya es un campo de datos en el documento y se toma directamente.

* **Ejemplo:** número de factura del campo XML del remitente.
* **Si es incorrecto:** el error está en el remitente. DocBits muestra exactamente de qué campo XML procede el valor.

### Script / regla de transformación

Tras la lectura interviene la lógica del cliente y remodela el valor. El documento sigue igual; el valor no.

* **Ejemplo:** `1001 / LS 206776` se convierte en `1001`.
* **Si es incorrecto:** no lo busque en el documento. Revise **Configuración › Scripts** o **Reglas de transformación**.

### Datos maestros

El valor leído se busca en sus propios datos: pedidos, proveedores. Una coincidencia sustituye el valor y arrastra otros campos.

* **Ejemplo:** `1001` encuentra el pedido `06O051001`, y el proveedor y el comprador también provienen de allí.
* **Si es incorrecto:** revise **Configuración › Configuración de Lookup**. Allí se indica si la búsqueda es exacta o si también acepta coincidencias parciales.

### Calculado

No se lee, sino que se calcula a partir de otros campos.

* **Ejemplo:** fecha de vencimiento a partir de la fecha de factura más las condiciones de pago.
* **Si es incorrecto:** normalmente uno de los campos a partir de los cuales se calcula es incorrecto.

### Código de barras

Leído de un código de barras o código QR del documento.

* **Ejemplo:** el número de factura está codificado en el código QR.
* **Si es incorrecto:** revise la configuración de códigos de barras del tipo de documento.

## Lo que más se malinterpreta

{% hint style="warning" %}
Cuando un campo contiene de repente un valor que no aparece así en el documento, casi nunca fue la IA, sino el paso 2 o el paso 3. Lo más habitual es la coincidencia en datos maestros, que también acepta coincidencias parciales: `1001` coincide con `06O051001`, y con el pedido encontrado cambia también el proveedor.
{% endhint %}

En el informe, ese campo aparece marcado en rojo. La columna **Acción** muestra el registro de datos maestros junto con un chip rojo *solo coincidencia parcial*, y la parte coincidente del valor aparece resaltada.

## Cómo leer el informe

* **Chips de estado** en la parte superior cuentan los campos que vinieron sin cambios del documento, los que cambiaron por el camino y los que no están en el documento tal como se muestran. Haga clic en un chip para ver solo esos campos; vuelva a hacer clic para ver todos.
* **Filtro de fuente:** la fila de iconos muestra cada método de extracción. Haga clic en uno para ver solo los campos que pasaron por él.
* **Acción:** cada paso por el que pasó el valor, con el icono de su fuente. El paso del que procede el valor actual aparece resaltado. Pase el cursor para ver qué hizo cada paso, de qué valor a cuál.
* **Motivo:** el estado del campo. El icono (i) explica por qué el valor es el que es. Si indica *El campo no existía*, el campo no estaba en el documento.
* Los valores largos se acortan con …; pase el cursor para ver el valor completo.
