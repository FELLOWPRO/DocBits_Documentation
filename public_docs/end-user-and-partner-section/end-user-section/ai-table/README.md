# AI Table

Con AI Table puede revisar posiciones extraídas, corregir columnas y guardar instrucciones para el diseño de un proveedor. Elija la guía para su tarea. Structured Output tiene su propia guía con Predeterminado/Sí/No, configuraciones específicas, vista previa y un ejemplo completo.

* [Ajustes y configuraciones específicas](configuration.md)
* [Structured Output para tablas](structured-output.md)
* [Columnas y correcciones](columns-and-corrections.md)
* [Instrucciones de IA](ai-instructions.md)
* [Etiquetas de la tabla AI](ai-table-tags.md)
* [Explicar la extracción y diagnosticar](explain-extraction.md)
* [Asistente y permisos](assistant-and-permissions.md)
* [Vídeos](videos.md)

<figure><img src="../../../.gitbook/assets/anatomy-ai-table.svg" alt="Ilustración isométrica de un lector de tablas: un cabezal lector con un cartucho de instrucciones escanea la tabla de un documento, un panel de conexiones enchufa cada columna devuelta en una columna configurada, y las columnas configuradas se alzan como contenedores con un mando de tres posiciones Use AI cada una."><figcaption><p>La IA lee la tabla y devuelve columnas. Cada columna devuelta se asigna a una columna de tabla configurada (una columna devuelta sin asignación permanece oculta), cada columna configurada tiene su propio ajuste Use AI (Predeterminado, Sí o No), y las instrucciones de IA y <strong>Guardar como entrenamiento</strong> determinan cómo se leen los siguientes documentos del diseño del proveedor.</p></figcaption></figure>

## Cuándo obtienes la tabla AI

* Un administrador ha activado la **Extracción de tabla de IA** (Ajustes → Procesamiento de documentos → Clasificación y extracción; consulta [Ajustes para administradores](#ajustes-para-administradores)). Si está desactivada, el área de la tabla muestra *La tabla AI se mostrará aquí. Habilitar en …*.
* Compruebe el texto legible o la entrada Vision. Las reglas clásicas guardadas pueden seguir determinando la ruta; verifique [qué ruta se utilizó realmente](../../../overview-and-basics/faq/document-processing/which-extraction-path-was-used.md).
* Cada columna dispone de una selección Use AI de tres estados. Compruebe también la fuente efectiva y las reglas del proveedor; Structured Output no sustituye todas las tablas basadas en reglas.

El nivel de IA que lee la tabla (Fast, Full, Nexus) se establece por organización y se puede sobrescribir por proveedor; consulta Modelo de IA Específico del Proveedor para Extracción de Campos y Tablas.

## La tabla AI de un vistazo

<figure><img src="../../../.gitbook/assets/ai-table-overview-es.png" alt="Tabla AI extraída con los encabezados de columna y cuatro filas"><figcaption><p>Las dos pestañas, la Tabla AI extraída y sus encabezados de columna.</p></figcaption></figure>

* **Pestañas.** *Tabla AI extraída* es lo que ha leído la IA. *Tabla extraída* es la tabla clásica de las reglas entrenadas. La pestaña de IA se abre por defecto cuando el documento tiene una tabla AI.
* **Encabezado de columna.** Cada columna muestra su nombre, un pequeño símbolo de **origen** (pasa el cursor por encima: *IA · cartografía*, *IA · sinónimo*, etc. indican cómo hizo coincidir la IA la columna), un menú de **tres puntos** y, en una columna asignada, un **botón con el nombre** en el que puedes hacer clic para cambiar de qué columna se trata.
* **Botones de fila.** La **x** al principio de una fila elimina esa fila. Haz clic con el botón derecho en una fila para ver *Seleccionar como costo adicional* / *Remove as additional cost*.
* **Barra de herramientas del pie.** Los iconos de la parte inferior de la pantalla añaden o ocultan columnas y filas; consulta [Barra de herramientas del pie](#barra-de-herramientas-del-pie).
* **Tarjeta Instrucciones para la IA** debajo de la tabla: prompt, columnas adicionales, **Cambio de prueba**, **Aplicar**, **Guardar como entrenamiento**, **Borrar**, **Exportar**; consulta [Dar instrucciones a la IA](#dar-instrucciones-a-la-ia).

{% hint style="info" %}
Los controles de columna solo funcionan cuando puedes editar el documento. Si aparecen en gris, el documento es de solo lectura o está bloqueado en otra sesión. Cuando el banner rojo indica que el documento está bloqueado por tu propio usuario en otra sesión, **Desbloquear** toma el bloqueo.
{% endhint %}


## Ajustes para administradores

Continuar aquí: [Ajustes y configuraciones específicas](configuration.md).

### Utilizar IA por columna

Continuar aquí: [Structured Output para tablas](structured-output.md).

<a id="elegir-la-columna-correcta-reasignar"></a>
<a id="el-menú-de-tres-puntos"></a>
<a id="el-menu-de-tres-puntos"></a>
<a id="barra-de-herramientas-del-pie"></a>

## Cambiar una columna

Continuar aquí: [Columnas y correcciones](columns-and-corrections.md).

<a id="sugerir-con-nexus"></a>
<a id="probar-aplicar-guardar-qué-hace-cada-botón"></a>
<a id="probar-aplicar-guardar-que-hace-cada-boton"></a>

## Dar instrucciones a la IA

Continuar aquí: [Instrucciones de IA](ai-instructions.md).


## Ver lo que hizo la IA

Continuar aquí: [Explicar la extracción y diagnosticar](explain-extraction.md).


## Ejemplos prácticos

Continuar aquí: [Explicar la extracción y diagnosticar](explain-extraction.md).

<a id="sugerir-una-regla-a-tu-administrador"></a>

## El Asistente y la tabla AI

Continuar aquí: [Asistente y permisos](assistant-and-permissions.md).


## Quién puede hacer qué

Continuar aquí: [Asistente y permisos](assistant-and-permissions.md).

<a id="1-leer-la-tabla-ai"></a>
<a id="2-corregir-una-columna-y-enseñar-a-docbits"></a>
<a id="2-corregir-una-columna-y-ensenar-a-docbits"></a>
<a id="3-dos-problemas-típicos"></a>
<a id="3-dos-problemas-tipicos"></a>
<a id="4-lo-que-la-ia-lee-bien"></a>
<a id="5-el-asistente-y-quién-puede-cambiar-qué"></a>
<a id="5-el-asistente-y-quien-puede-cambiar-que"></a>

## Serie de vídeos

Continuar aquí: [Vídeos](videos.md).

## Páginas relacionadas

* [Etiquetas de la tabla AI](ai-table-tags.md)
* [Entrenamiento de Campos de Línea / Tabla de Entrenamiento](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [Touchless Intelligence](../../../administration-and-setup/touchless-intelligence.md)
