# Nuestro Sistema de Prioridad de Documentos

En nuestro sistema de procesamiento de documentos, manejamos un gran volumen de documentos de múltiples clientes a diario. Para garantizar que los documentos de cada cliente se procesen de manera oportuna, hemos implementado un sofisticado sistema de prioridad. Este sistema ajusta dinámicamente las prioridades en función del número de documentos pendientes que tiene un cliente, asegurando **equidad** y **eficiencia**. Vamos a profundizar en cómo funciona este sistema de prioridad y cuándo se restablece el contador de tareas.

**Conceptos Clave del Sistema de Prioridad**

Nuestro sistema de prioridad gira en torno a algunos conceptos clave:

1. **Documentos Pendientes**: Este es un conteo de los documentos que un cliente ha enviado pero que aún no han sido procesados.
2. **Intervalo de Restablecimiento**: El sistema restablece periódicamente el conteo de documentos pendientes a cero para asegurar que ningún cliente pueda monopolizar los recursos de procesamiento indefinidamente.

**Cómo se Determina la Prioridad**

Aquí hay una explicación paso a paso de cómo se determina la prioridad para el procesamiento de documentos:

1. **Seguimiento de Documentos Pendientes**: Cada cliente tiene un conteo de documentos pendientes. Este conteo nos ayuda a saber cuántos documentos están esperando ser procesados para cada cliente.
2. **Restablecimiento del Conteo**: Para mantener la equidad, restablecemos el conteo de documentos pendientes a cero si ha pasado un tiempo determinado (el intervalo de restablecimiento) desde la última actualización. Este intervalo se establece en 1500 segundos (o 25 minutos) por defecto.
3. **Actualización del Conteo**: Si el intervalo de restablecimiento no ha pasado, reducimos el conteo de documentos pendientes en uno cada vez que verificamos, simulando el procesamiento de un documento.
4. **Establecimiento de Prioridades**: La prioridad para el procesamiento de tareas se basa en el número de documentos pendientes. Cuantos menos documentos pendientes haya, mayor será la prioridad, lo que significa que esas tareas se procesarán antes. Tenemos umbrales específicos para asignar niveles de prioridad del 1 (máxima prioridad) al 9 (mínima prioridad).

**Niveles de Prioridad**

Los niveles de prioridad se asignan en función del conteo de documentos pendientes de la siguiente manera:

* **Prioridad 9**: Si el conteo de documentos pendientes es menor que -20
* **Prioridad 8**: Si el conteo de documentos pendientes es menor que -14
* **Prioridad 7**: Si el conteo de documentos pendientes es menor que -12
* **Prioridad 6**: Si el conteo de documentos pendientes es menor que -10
* **Prioridad 5**: Si el conteo de documentos pendientes es menor que -8
* **Prioridad 4**: Si el conteo de documentos pendientes es menor que -6
* **Prioridad 3**: Si el conteo de documentos pendientes es menor que -4
* **Prioridad 2**: Si el conteo de documentos pendientes es menor que -2
* **Prioridad 1**: Si el conteo de documentos pendientes es mayor o igual a -2

{% hint style="info" %}
En términos más simples, a medida que aumenta el número de documentos pendientes, el nivel de prioridad disminuye, lo que significa que esos documentos se procesan más tarde en comparación con otros con prioridades más altas.
{% endhint %}

**Cuándo se Restablece el Contador**

El contador de documentos pendientes se restablece a cero si ha pasado más del intervalo de restablecimiento (**1500** segundos) desde la última actualización. Este mecanismo asegura que ningún cliente pueda acumular documentos pendientes indefinidamente y acaparar los recursos del sistema. Al restablecer periódicamente el contador, garantizamos que cada cliente obtenga una parte justa del tiempo de procesamiento.
