# Guía de Escritura de Prompts

Esta guía explica cómo escribir prompts efectivos para el Operador de DocBits. Los prompts son instrucciones paso a paso que dirigen al operador a realizar tareas específicas, como navegar por páginas web, interactuar con elementos de la interfaz de usuario e ingresar datos.

## ¿Qué es un Prompt?

Un prompt es una secuencia de instrucciones escritas en texto que guían al operador para ejecutar un flujo de trabajo. Los prompts pueden incluir comandos como hacer clic en botones, completar formularios, esperar a que se carguen páginas o elementos, y más.

## Sintaxis y Estructura de los Prompts

* Cada instrucción debe estar escrita como un paso numerado.
* Utiliza un lenguaje claro y conciso para describir cada acción.
* Especifica elementos de la interfaz de usuario por nombre, etiqueta o número de índice para garantizar precisión.
* Utiliza un formato consistente para mejorar la legibilidad.

## Uso de Variables en los Prompts

Las variables te permiten hacer que los prompts sean dinámicos al insertar diferentes valores en tiempo de ejecución. En lugar de codificar valores como fechas o números de documento, utiliza marcadores de posición dentro de llaves, por ejemplo: `{numero_factura}`, `{url}`, o `{orden_compra}`.

Esto hace que los prompts sean reutilizables y adaptables en diferentes flujos de trabajo o conjuntos de datos.

### Cómo Usar Variables

* Escribe variables dentro de llaves en tu texto de prompt:
  * Ingresa el número de factura: {numero\_factura} en el campo 'Número de factura HP'.
* Cada variable debe tener un nombre único (por ejemplo, `numero_factura`, `url`, `tipo_documento`).
* Los nombres de variables no deben incluir espacios ni caracteres especiales (los guiones bajos están permitidos).
* Para flujos de trabajo, los nombres de variables deben coincidir exactamente con los IDs de campo del documento para habilitar el mapeo automático de datos.

## Ventana Emergente de Variables de Prompt

Para abrir la ventana emergente de Variables de Prompt, haz clic en el icono de **engranaje** ubicado junto al campo de entrada de prompt.

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FvEC6vmU6CCsAa36OK9V6%252Fimage.png%3Falt%3Dmedia%26token%3Dfd26ce70-0de4-4bdb-adf4-85d0052f9d53&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=fc29eaa3&#x26;sv=2" alt="" width="375"></div>

## Diseño y Controles de la Ventana Emergente

<div align="left"><img src="https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F~%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FftlMKp0ql0miqBTdCtt3%252Fimage.png%3Falt%3Dmedia%26token%3D979b7c8e-0728-4a10-bb8a-3275203c4c3d&#x26;width=768&#x26;dpr=4&#x26;quality=100&#x26;sign=b07844a9&#x26;sv=2" alt="" width="375"></div>

* **Campo de Entrada de Clave:** Ingresa el nombre de la variable aquí (sin llaves).
* **Campo de Entrada de Valor:** Ingresa el valor a utilizar para esta variable cuando se ejecute el prompt.
* **Guardar como Sensible (Checkbox):** Cuando está marcado, esto marca el valor de la variable como sensible. Los valores sensibles están encriptados y ocultos en flujos de trabajo para proteger la información confidencial de usuarios no autorizados.
* **Botón Agregar (+):** Haz clic para agregar otra fila de entrada de par clave-valor.
* **Ícono de Eliminar (Papelera):** Cuando existen múltiples pares clave-valor, todos los pares excepto el primero muestran un pequeño ícono de papelera para eliminar ese par específico.
* **Botón Limpiar:** Restablece la ventana emergente al borrar todos los pares clave-valor y valores ingresados.
* **Botón Guardar:** Guarda todas las variables definidas y sus valores para el prompt actual.
