# Appearance

**Appearance** permite a un administrador dar a la copia de DocBits de la organización un aspecto propio: colores, radio de esquina, densidad y fuente. Todos los miembros de la organización ven el resultado —en modo claro y oscuro— tras la siguiente recarga. Nunca cambia el diseño ni lo que hace una función, solo cómo se dibuja.

> **Acceso:** Appearance es una página solo para administradores. Abra **Settings → Organization & Access → Appearance**.

<!-- screenshot: /settings/appearance light -->

## Quién puede cambiarlo

Solo los administradores de la organización pueden abrir **Settings → Appearance** y guardar o restablecer un tema. El resto de la organización solo ve el resultado.

## Qué hay en la página

La página se divide en un editor a la izquierda y una vista previa en vivo a la derecha.

| Área | Qué contiene |
|---|---|
| **General** | El nombre del tema, la fuente, el radio de esquina y la densidad. |
| **Colors** | Pestañas Light y Dark, un selector de color más un campo hexadecimal por color, agrupados en Surfaces, Brand, Neutrals, Status y Charts. Un panel de solo lectura «Derived colours» debajo muestra los colores que DocBits calcula por usted (estados hover, anillos de foco y similares) a partir de los colores anteriores. |
| **Advanced overrides** | Una línea `--token: value` por entrada, para el caso excepcional de que los controles de color, radio, densidad y fuente anteriores no cubran algo — véase [Advanced overrides](#advanced-overrides). |

### Cambiar colores

Cada color tiene una muestra (haga clic en ella para abrir el selector de color del navegador) y un campo hexadecimal junto a ella en el que puede escribir o pegar. Deje un color vacío para mantener el valor predeterminado de DocBits para ese token: la muestra muestra entonces un borde discontinuo. Cambie entre las pestañas **Light** / **Dark** encima de la lista de colores para ajustar el otro modo; un color que no establezca en modo oscuro conserva su propio valor predeterminado de DocBits para oscuro y no copia el valor claro.

{% hint style="info" %}
Los colores se introducen en hexadecimal (`#2388ae` o `#2388aeaa` con alfa). No hay entrada de nombres de color ni `rgb()`.
{% endhint %}

### Radio de esquina, densidad y fuente

* **Corner radius** — `None`, `Small`, `Medium` (predeterminado), `Large` o `Extra large`. Controla el redondeo de tarjetas, botones, campos de entrada y diálogos en toda la aplicación.
* **Density** — `Compact`, `Comfortable` (predeterminado) o `Spacious`. Controla la altura de botones, campos de entrada y filas de tabla, y el tamaño base del texto.
* **Font** — una lista corta de fuentes incluidas (Geist es la predeterminada de DocBits; también Inter, Roboto, IBM Plex Sans, Source Sans 3, Nunito Sans, Manrope, Kanit o la fuente del sistema del visitante). Todas las fuentes ya están incluidas, no hay nada que subir.

### Advanced overrides

Para un token de diseño que los controles anteriores no ofrecen directamente (por ejemplo, una altura concreta de fila de tabla), añada una línea en **Advanced overrides**:

```
--table-row-h: 30px
```

Una anulación por línea, `--token: value`. Una línea no válida —un token desconocido, un token que no se puede personalizar o un valor que no encaja con lo que el token espera— se muestra como error bajo la caja y no se aplica; el resto de la página se guarda con normalidad.

## Vista previa

Cada cambio actualiza inmediatamente el panel **Preview** de la derecha, sin afectar a lo que ven los demás: nunca toca la aplicación en vivo ni el tema guardado. La vista previa tiene sus propias pestañas: una vista general con claro y oscuro uno al lado del otro y, después, páginas dedicadas a botones, campos de formulario, superficies e indicadores de estado, para que pueda comprobar el contraste y la legibilidad en las partes de la interfaz más sensibles al color.

<!-- screenshot: /settings/appearance dark -->

Si un cambio deja el tema no válido (véase abajo), la vista previa sigue mostrando la última versión válida en lugar de romperse.

## Guardar y restablecer

* **Save** escribe el tema para toda la organización. Está desactivado hasta que algo ha cambiado realmente y el tema es válido.
* **Reset** pide confirmación y después elimina por completo el tema de la organización y devuelve a todos al tema predeterminado de DocBits. Esto no se puede deshacer desde la página: los colores tienen que volver a introducirse a mano (o reimportarse, véase abajo) si la organización los quiere de vuelta.
* Un guardado o restablecimiento que falla (por ejemplo, por un problema de validación) muestra el problema encima del editor y deja la página como estaba; no se aplica nada.

No hay comprobaciones de contraste antes de guardar — véase [Consejos](#consejos) más abajo.

## Exportar e importar

* **Export** descarga el tema que se muestra actualmente en el editor (guardado o no) como archivo `.json`, con el nombre del tema.
* **Import** lee un archivo de tema `.json` y lo carga en el editor. Aún hay que revisarlo y guardarlo para que surta efecto: importar por sí solo no cambia lo que ve nadie. Un archivo no válido o demasiado grande (más de 32 KB) se rechaza con un error y no cambia nada.

Exportar es una forma cómoda de respaldar un tema antes de experimentar, o de copiar el aspecto de una organización a otra.

## Qué ven los usuarios

Una vez guardado, el tema se aplica a toda la aplicación —todas las páginas, en modo claro y oscuro— para todos los miembros de la organización, tras su siguiente recarga (no de inmediato para otras sesiones abiertas). Un usuario que nunca ha cargado la organización ve el valor predeterminado de DocBits hasta que los ajustes de la organización se han cargado una vez; después el tema toma el control.

Restablecer devuelve a todos al aspecto predeterminado de DocBits en su siguiente recarga, exactamente como si nunca se hubiera definido un tema de organización.

## Consejos

* **Compruebe el contraste en ambos modos.** El editor no advierte de combinaciones de bajo contraste (por ejemplo, un color de marca claro con texto claro). Use los paneles claro y oscuro de la vista previa para comprobar que el texto sigue siendo legible antes de guardar.
* **No toque los colores de estado salvo que tenga un motivo para cambiarlos.** Destructive (errores), success, warning e info mantienen su significado en toda la aplicación: cambiarlos puede hacer que un error parezca un éxito a primera vista. Cambie el color de marca y deje los colores de estado en sus valores predeterminados, a menos que la organización necesite más que el rojo/verde/ámbar/azul convencional.
* **Empiece con una paleta completa.** Exportar el tema actual o partir del valor predeterminado de DocBits da a cada color base un valor desde el que editar, en lugar de adivinar qué tokens existen.
* **Un cambio de tema afecta a todos los usuarios de la organización en su siguiente recarga.** No hay un paso para mostrar la vista previa solo a un subconjunto de usuarios; pruebe el resultado en claro y oscuro antes de decir al equipo que está listo.
