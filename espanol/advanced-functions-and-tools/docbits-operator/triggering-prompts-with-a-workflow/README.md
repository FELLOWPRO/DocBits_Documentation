# Activación de Prompts con un Flujo de Trabajo

Esta guía explica cómo configurar un flujo de trabajo de DocBits para activar automáticamente un prompt guardado. Esto le permite integrar prompts de operador en flujos de procesamiento de documentos sin entrada manual.

## Paso 1: Crear un Prompt

Antes de vincular un prompt a un flujo de trabajo:

* Asegúrese de que su prompt ya esté creado
* Incluya todas las **variables** necesarias en el cuerpo del prompt.

Si necesita ayuda para escribir o guardar prompts, consulte la [Guía de Escritura de Prompts](../prompt-writing-guide.md) y la [Descripción General de la Interfaz del Operador](../).

## Paso 2: Configurar el Flujo de Trabajo

Antes de configurar la tarjeta de Prompt del Operador, asegúrese de que su flujo de trabajo esté creado correctamente.

1. Vaya al **Constructor de Flujos de Trabajo** en la interfaz de DocBits.
2. Cree un nuevo flujo de trabajo o abra uno existente.
3. Defina las **condiciones de activación**—estas determinan cuándo comenzará el flujo de trabajo (por ejemplo, tipo de documento, estado, presencia de campo, etc.).
4. Agregue los pasos de **acción necesarios** a su flujo de trabajo según sea necesario.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fd3qJJhFDHTXDUfUedjaF%252Fimage.png%3Falt%3Dmedia%26token%3D310f9e9c-9e79-4987-af01-2d914f1abbe7&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=873cf566&#x26;sv=2" alt="" width="375"></div>

## Paso 3: Configurar la Tarjeta de Prompt del Operador en el Flujo de Trabajo

En el Constructor de Flujos de Trabajo, use la **tarjeta de Prompt del Operador** para configurar un prompt que debe ejecutarse cuando se cumplan las condiciones del flujo de trabajo.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fg11jtpdL4j3mJveYvWSX%252Fimage.png%3Falt%3Dmedia%26token%3Db208669e-b6a8-4879-b08b-d9ba353e908d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=974876f7&#x26;sv=2" alt="" width="375"></div>

### Opciones de Configuración Clave

* **Script:** Seleccione el **Prompt de Organización** guardado que se ejecutará.
* **Datos del Script (Variables):** Si el prompt seleccionado contiene variables, defina sus valores aquí utilizando pares clave-valor.
  * Si se deja vacía una variable aquí, el sistema intentará completarla automáticamente **desde el documento**.
  * Para que esto funcione, el nombre de la variable en el prompt debe coincidir **exactamente con** el **ID del campo** del atributo del documento.
* **Máx. Pasos:** Defina el número máximo de pasos que se permiten ejecutar al operador durante este prompt.
* **Máx. Intentos:** Establezca cuántas veces el sistema debe intentar el prompt en caso de fallo.
* **Modo de Ejecución:** Elija si el prompt debe ejecutarse:
  * **En la Nube**
  * **Localmente** (requerido si su ERP o sistema de destino está alojado localmente)
