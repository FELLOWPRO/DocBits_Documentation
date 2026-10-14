# Debug Collector

El Debug Collector captura una instantánea completa de su sesión de DocBits — actividad de red, errores, entorno del navegador y métricas de rendimiento — la empaqueta como un informe JSON y, opcionalmente, abre un ticket de soporte directamente desde el mismo diálogo.

## Cómo acceder

Pulse <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> en Windows y Linux, o <kbd>Cmd</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> en macOS. El diálogo Performance Report se abre de inmediato.

<figure><img src="../../.gitbook/assets/debug-collector-dialog.png" alt="Diálogo Debug Collector"><figcaption><p>El diálogo Performance Report muestra la instantánea capturada y un formulario integrado para crear el ticket de soporte.</p></figcaption></figure>

## Qué se captura

* **Llamadas a la API** — las últimas 60 llamadas REST y WebSocket, con tiempos, códigos de estado y URLs invocadas. Las llamadas que superan los dos segundos se marcan aparte.
* **Errores** — errores recientes de JavaScript y rechazos de promesas no capturados de la consola del navegador.
* **Registros de consola** — los mensajes de log más recientes de la aplicación.
* **Entorno** — versión del navegador, sistema operativo, tamaño de pantalla y banderas de funcionalidad activas.
* **Contexto de usuario** — su rol, organización y la página en la que estaba al tomar la instantánea.
* **Métricas de rendimiento** — tiempos de carga de la página (LCP, FCP), uso de memoria y tamaño del DOM.
* **Trace IDs** — identificadores de correlación que enlazan la instantánea con los registros del backend.

## Crear un ticket de soporte desde el diálogo

No es necesario descargar ni adjuntar nada manualmente — el diálogo incluye un formulario **Create Support Ticket**.

1. Rellene su email, deje el asunto sugerido o sustitúyalo, elija una prioridad y añada cualquier nota que explique lo que estaba haciendo cuando ocurrió el problema.
2. Haga clic en **Send Report**. La instantánea JSON se adjunta y el ticket se crea en un único paso.

Listo — el equipo de soporte recibe el ticket con todos los datos necesarios para reproducir el caso.

Si desea una copia local de la instantánea, use **Copy Debug Data** para copiar el JSON al portapapeles, o use Guardar como del navegador para mantener el informe como un archivo `.json`.

## Privacidad y manejo de datos

* Los tokens de autenticación y las cabeceras sensibles se ocultan en las llamadas API capturadas antes de construir la instantánea.
* Nada sale de su navegador hasta que pulse **Send Report** — el atajo solo abre el diálogo.

<mark>Revise la instantánea antes de enviarla si estaba trabajando con documentos que contienen datos de clientes. Los identificadores de documento visibles en las URLs aparecerán en el informe.</mark>
