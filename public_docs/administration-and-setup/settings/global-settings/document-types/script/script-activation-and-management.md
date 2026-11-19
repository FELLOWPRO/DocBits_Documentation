# Activación y administración de scripts

Los administradores pueden usar **Scripts** para gestionar las reglas de procesamiento de un tipo de documento. Esta guía muestra dónde encontrar los scripts, cómo activarlos o desactivarlos y cómo cambiar de forma segura un script ya publicado.

## Videotutorial: administrar scripts

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-manage-scripts/v4/es.mp4" %}
Administrar los scripts de un tipo de documento
{% endembed %}

El vídeo muestra la lista de scripts con filtro y orden, cómo activar y desactivar, copiar, el historial de versiones y la eliminación con confirmación.

## Buscar un script

1. Abra **Ajustes → Tipos de Documento**.
2. En el tipo de documento que quiera gestionar, seleccione **Guiones**. La página muestra la lista de scripts de ese tipo de documento.
3. Busque por nombre o use **Todo**, **Activo** e **Inactivo** para acotar la lista. La lista se ordena por orden de ejecución de forma predeterminada; el control de ordenación permite ordenarla por orden de ejecución, por nombre (**A-Z** / **Z-A**) o por fecha de modificación.

Cada tarjeta muestra el nombre del script, su orden de ejecución como una etiqueta numerada, el disparador, la versión y el estado. El lápiz abre el editor; el icono de copiar duplica el script. **Nuevo** abre el editor para crear un script nuevo.

<figure><img src="../../../../../.gitbook/assets/dbdc-654-script-scripts-list-es-20261110.png" alt="Lista de scripts con el buscador, los filtros Todo, Activo e Inactivo, el control de ordenación y tres tarjetas; cada tarjeta muestra junto al nombre una etiqueta numerada con el orden de ejecución 10, 20 o 30"><figcaption><p>La etiqueta numerada de cada tarjeta es el orden de ejecución del script.</p></figcaption></figure>

## Definir el orden de ejecución

El campo **Execution order** controla el orden en que se ejecutan los scripts: los números más bajos se ejecutan primero. El campo mantiene la etiqueta en inglés también en la interfaz en español.

1. Abra el script en el editor.
2. Introduzca un número entero a partir de 0 en el campo **Execution order**. Deje el campo vacío para mantener 0.
3. Guarde el script. Las letras, los decimales y los números negativos se rechazan con un mensaje de error en el campo y no se guarda nada.

Si cambia el orden de ejecución y después activa una versión, DocBits guarda primero el script y solo activa la versión cuando ese guardado se ha realizado correctamente.

<figure><img src="../../../../../.gitbook/assets/dbdc-654-script-execution-order-field-es-20261110.png" alt="Fila de campos del editor de scripts con Nombre, Tipo de documento, Activar, el campo Execution order con el valor 10 y la selección del subdocumento"><figcaption><p>El orden de ejecución se introduce en el campo <strong>Execution order</strong>.</p></figcaption></figure>

## Activar o desactivar un script

Use el interruptor **Activo/Inactivo** de la tarjeta del script. El cambio se guarda de inmediato; los contadores de la lista se actualizan para mostrar el resultado. Un script inactivo sigue disponible para consultarlo o editarlo, pero no se ejecuta durante el procesamiento de documentos.

**Compruebe el estado después de crear un script.** En la interfaz actual del Sandbox, al guardar un script nuevo se crea una versión activa y la tarjeta queda en **Activo**. Páselo a **Inactivo** si solo es un borrador o un ejemplo de prueba.

<figure><img src="../../../../../.gitbook/assets/dbdc-654-script-card-status-es-20261110.png" alt="Tarjeta de script con la etiqueta del orden de ejecución 10, el disparador Después de la extracción, la versión v2, los iconos de editar, copiar y eliminar y el interruptor Inactivo"><figcaption><p>A la derecha de la tarjeta: lápiz para editar, copiar, papelera para eliminar y el interruptor <strong>Activo/Inactivo</strong>.</p></figcaption></figure>

## Cambiar un script existente

1. Seleccione la tarjeta del script o su icono de lápiz. Una versión publicada es de solo lectura, así que no puede escribir sobre ella directamente.
2. En **Historial de versiones**, seleccione el icono de lápiz de la versión que quiera cambiar. Esto crea un **Borrador** a partir de esa versión.
3. Edite el borrador y seleccione el icono **Guardar**. Revise el nombre, el tipo de documento, el disparador y el código antes de guardar.
4. Pruebe el script modificado con documentos representativos en un entorno de pruebas. Cuando esté listo, seleccione el icono de verificación del borrador en **Historial de versiones** para convertir esa versión en la activa.
5. Vuelva a la lista de Scripts y compruebe el interruptor **Activo/Inactivo** de la tarjeta. La versión marcada como **ACTIVO** en el Historial de versiones indica la versión seleccionada; el interruptor de la tarjeta controla si el script se ejecuta.

<figure><img src="../../../../../.gitbook/assets/dbdc-654-script-published-version-es-20261110.png" alt="Versión publicada del script mostrada como solo lectura, con el mensaje para clonarla como borrador y el Historial de versiones a la derecha"><figcaption><p>Una versión publicada no se puede editar directamente. Use el lápiz del Historial de versiones para crear un borrador.</p></figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-654-script-editable-draft-es-20261110.png" alt="Borrador editable en el Historial de versiones junto a la versión activa del script"><figcaption><p>Guarde y revise el borrador antes de convertirlo en la versión activa.</p></figcaption></figure>

Para ver ejemplos de scripts y las funciones disponibles, consulte [Programación en DocBits](scripting-in-docbits/README.md).
