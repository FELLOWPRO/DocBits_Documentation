# Operador de DocBits

## Resumen

El **Operador de DocBits** es un asistente de automatización impulsado por IA diseñado para simplificar tareas repetitivas en tus flujos de trabajo. Los usuarios crean _instrucciones paso a paso_ mejoradas con variables que guían a la IA para navegar, ingresar datos y hacer clic a través de interfaces automáticamente. Esto reduce el esfuerzo manual y acelera las operaciones de rutina.

## Habilitar el Operador de DocBits

Para habilitar el Operador de DocBits, sigue estos pasos:

1. **Navegar a Configuración**:
   * Desde el Panel de control, ve a **Configuración**.
   *   Selecciona **Procesamiento de Documentos** y luego elige **Módulo**.

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F4Yyo7aXyVeWyfJHclHpK%252Fimage.png%3Falt%3Dmedia%26token%3D0071c149-3ea8-452b-a2e3-0fbbc9d3b496\&width=768\&dpr=4\&quality=100\&sign=23009aa7\&sv=2)
2. **Habilitar la Función**:
   * Desplázate hacia abajo para localizar la opción **Operador de DocBits**.
   *   Activa el interruptor para habilitar el **Operador de DocBits**.

       <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FyqNyGI2OelO415pf3RHN%252Fimage.png%3Falt%3Dmedia%26token%3D8899a256-a1d6-486f-aaf6-b8e244f9b348&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ce097a28&#x26;sv=2" alt="" width="563"></div>

## Acceder a la Interfaz

*   Una vez habilitada la función, abre el **Operador de DocBits** desde el menú de navegación principal.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FS67AFPuaQ3CNXQ7Oe80V%252Fimage.png%3Falt%3Dmedia%26token%3D6b6d6782-cc16-48e6-8622-5c596ac54f57\&width=768\&dpr=4\&quality=100\&sign=e6d0fd8e\&sv=2)

### **1. Entrada de Instrucciones**

En la parte inferior de la pantalla, hay un campo de entrada etiquetado como _“Ingresa tu instrucción aquí…”_. Aquí es donde los usuarios escriben instrucciones para que el operador las siga.

Junto al campo de entrada hay varios botones de control:

* **Variables de Instrucción** – Abre un popup donde puedes ingresar pares clave-valor utilizados en la instrucción. Las variables se escriben usando llaves, como `{numero_factura}` o `{url}`. Estos valores se aplican solo a la instrucción actual en el campo de entrada.
* **Guardar Instrucción** – Guarda la instrucción actual. Elige guardarlo como:
  * **Instrucción de Organización** – Editable dentro de tu organización; incluye tanto la instrucción como los valores de variables definidos.
  * **Instrucción Global** – Compartida entre todos los inquilinos; incluye solo la instrucción y marcadores de posición de variables (no se guardan valores).
* **Limpiar Chat** – Borra la conversación actual con el operador, pero deja la instrucción en el campo de entrada sin cambios. Útil al reutilizar o refinar una instrucción.

Para obtener orientación detallada sobre cómo escribir instrucciones efectivas, incluyendo sintaxis, variables y ejemplos, consulta la [**Guía de Escritura de Instrucciones**](prompt-writing-guide.md).

### **2. Navegación de la Barra Lateral**

Utiliza el ícono en la parte superior izquierda para abrir o cerrar la barra lateral. La barra lateral muestra instrucciones guardadas, organizadas en dos categorías:

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252Fm08uq4Kqj0SEZWSnlnoS%252Fimage.png%3Falt%3Dmedia%26token%3D4ba4542a-a707-4907-ae5e-b06286af8240&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=ef6b0706&#x26;sv=2" alt="" width="375"></div>

* **Instrucciones de Organización**: Editables y reutilizables dentro de tu organización.
* **Instrucciones Globales**: Compartidas entre todos los inquilinos. Estas no pueden almacenar valores de variables y no se pueden editar o eliminar.
  *   Una instrucción global aún es editable y eliminable por la **organización que la creó**, donde aparece bajo Instrucciones de Organización.

      <div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlVnXjwtnxAtqsftRvYUi%252Fimage.png%3Falt%3Dmedia%26token%3D60b3d0dd-3eee-40a8-b447-c9e91087a27d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=f9b364a&#x26;sv=2" alt="" width="375"></div>
* **Funcionalidad de Búsqueda:** una barra de búsqueda en la parte superior de la barra lateral permite a los usuarios encontrar rápidamente instrucciones guardadas por nombre o palabra clave.
* **Referencia de Iconos:** Cada instrucción guardada tiene un conjunto de iconos de acción
  * **Flecha** – Iniciar la instrucción
  * **Pluma** – Editar la instrucción (disponible solo para instrucciones de tu propia organización)
  * **Papelera** – Eliminar la instrucción (disponible solo para instrucciones de tu propia organización)

### 3. Guardar Instrucción

Al hacer clic en el botón **Guardar Instrucción** se abre un popup donde puedes guardar la instrucción actual para uso futuro.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FgrBpDnbo80nPkozFhgCE%252Fimage.png%3Falt%3Dmedia%26token%3Dd31c06fc-dcd0-4fbe-9e1e-6c5bc001e4bb&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=900c948&#x26;sv=2" alt="" width="375"></div>

#### **Campos del Popup de Guardar Instrucción**

* **Nombre de la Instrucción:** Ingresa un nombre para identificar la instrucción.
* **Guardar Instrucción Públicamente (Casilla de Verificación):** Cuando está marcado, la instrucción se guardará como una **Instrucción Global**. Las Instrucciones Globales se comparten entre todos los inquilinos y no pueden almacenar **valores** de variables (solo **nombres** de variables).
* **Editar Variables:** Abre el [**Popup de Variables de Instrucción**](prompt-writing-guide.md) para revisar o ajustar las definiciones de variables antes de guardar.

**Acciones**

* **Cancelar:** Cierra el popup sin guardar.
* **Guardar:** Guarda la instrucción utilizando el nombre especificado y la configuración de visibilidad.

### 4. Controles de Ejecución de Instrucción

Cuando una instrucción está en ejecución, los usuarios tienen varias opciones de control para administrar o intervenir en el proceso de ejecución:

* **Pausar Instrucción:** Detiene temporalmente la ejecución actual. Útil si deseas observar el estado actual o preparar el sistema para los próximos pasos.\
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG9U15jmVTb202efDR5l%252Fimage.png%3Falt%3Dmedia%26token%3Dee52f250-15d4-4139-b612-ba5ff1876841\&width=300\&dpr=4\&quality=100\&sign=329efe81\&sv=2)
* **Reanudar Instrucción:** Continúa la ejecución desde el punto donde se pausó. ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FewGCZ9wSXt7VsvS8RjZH%252Fimage.png%3Falt%3Dmedia%26token%3D92ec27df-07b4-4e9f-a125-6f0a87d9db47\&width=300\&dpr=4\&quality=100\&sign=8e03589c\&sv=2)
* **Cancelar Instrucción:** Detiene completamente la ejecución y restablece la sesión. Esto es útil si la instrucción necesita ser abortada o reiniciada debido a un comportamiento incorrecto o cambios en la entrada.\
  ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FYUKk03iazolJlx6reOO3%252Fimage.png%3Falt%3Dmedia%26token%3Da722c82b-e4c1-4c23-8c56-a31f2685cce7\&width=300\&dpr=4\&quality=100\&sign=170c122e\&sv=2)
* **Tomar Control:** Permite al usuario intervenir manualmente interactuando directamente con el sistema. Esto es útil si el operador se queda atascado o interpreta incorrectamente un paso. Tomar control **pausa automáticamente** la instrucción y cambia a modo manual hasta que elijas reanudar o cancelar.

### 5. Vista Detallada del Operador

Una vez que se inicia una instrucción, se vuelve disponible un botón adicional que permite a los usuarios cambiar a una **vista de ejecución detallada**.\
![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F9kObRWZFb3woomL045KL%252FDetailed%2520view%2520.jpg%3Falt%3Dmedia%26token%3Dbd0f94e2-84f2-4fd0-ae89-82408e85e03a\&width=300\&dpr=4\&quality=100\&sign=3aefc79\&sv=2)

* **Abrir Vista Detallada:** Este botón te lleva a una vista dedicada que muestra, paso a paso, lo que el operador está haciendo en tiempo real.

En la vista detallada, los usuarios pueden:

* Monitorear cada acción realizada (por ejemplo, clics, entradas, esperas).
* Ver qué paso está activo actualmente.
* Identificar dónde ocurren problemas si la instrucción encuentra dificultades.
* Utilizar las mismas acciones de **Pausa**, **Reanudar**, **Cancelar** y **Tomar Control**.
