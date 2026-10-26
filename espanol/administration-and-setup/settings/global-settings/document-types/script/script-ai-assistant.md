# Asistente de IA en el editor de scripts

El editor de scripts tiene un **Asistente de IA** integrado que escribe y explica scripts de DocBits por usted. Usted describe con palabras sencillas lo que debe hacer el script y el asistente responde con código Python que puede copiar al editor.

{% hint style="info" %}
El Asistente de IA forma parte de **DocNet**. Su organización necesita una suscripción activa a DocNet para usarlo. Consulte [Plan de suscripción](../../subscription-plan/README.md) y [Módulos](../../../document-processing/module/README.md).
{% endhint %}

## Abrir el asistente

1. Vaya a **Configuración → Tipos de documento**, abra el tipo de documento y haga clic en **Guiones** (Scripts).
2. Haga clic en **Nuevo** o abra una versión de script existente como borrador.
3. Haga clic en el icono del robot junto al nombre del script. A la derecha del editor se abre el panel **Asistente de IA**.

## Qué conoce el asistente

Con cada pregunta, DocBits envía al asistente:

* la **referencia de scripting** (las funciones descritas en [Programación en DocBits](scripting-in-docbits/README.md)),
* el **tipo de documento** del script,
* el **script actual** del editor,
* los **nombres de campos y columnas de tabla** que su organización utiliza para este tipo de documento.

Gracias a los nombres de campo, el asistente utiliza sus campos reales, por ejemplo `invoice_date` o `purchase_order`, en `get_field_value()` y `set_field_value()`.

## Escribir un script con el asistente

1. Escriba su petición en el cuadro de la parte inferior del panel, por ejemplo: *Establece la moneda en EUR si está vacía.*
2. Pulse **Intro** o haga clic en el icono de enviar. La respuesta va apareciendo poco a poco.
3. Haga clic en el icono de copiar junto a un bloque de código (información sobre herramientas **Copiar al editor**) para pasar el código al editor de scripts.
4. Revise el código, asigne un nombre y guarde el script como borrador.

Las preguntas de seguimiento funcionan en el mismo panel. Pegue un mensaje de error o pregunte *¿Por qué este script no establece la fecha de vencimiento?* y el asistente verá el script actual del editor.

## Compruebe siempre el resultado

{% hint style="warning" %}
El asistente puede equivocarse. Lea el código generado, compruebe que los nombres de campo coinciden con su tipo de documento y pruebe el script con un documento de prueba antes de activarlo. Consulte [Prueba de scripts](testing-scripts.md).
{% endhint %}

Los scripts solo se ejecutan con las funciones de script autorizadas. Si un script llama a una función que no existe, DocBits lo rechaza con el mensaje *Unknown function*.

## Uso y límites

* Debajo de cada respuesta se muestra cuántos tokens ha consumido (entrada, salida y total).
* El uso se registra como uso de DocNet de su organización.
* DocBits rechaza la solicitud cuando falta la suscripción a DocNet (*DocNet subscription required*), ha caducado (*DocNet subscription expired*) o se ha agotado la cuota (*DocNet quota exhausted*).

## Páginas relacionadas

* [Creación y edición de scripts](creating-and-editing-scripts.md)
* [Funciones de campo](scripting-in-docbits/field-functions.md)
* [Scripts de ejemplo](scripting-in-docbits/sample-scripts/README.md)
* [Activación y administración de scripts](script-activation-and-management.md)
