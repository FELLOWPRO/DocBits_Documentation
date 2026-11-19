# Estado de la caché PWA

La página **PWA Cache Status** es una herramienta de diagnóstico para administradores que investigan una **pantalla en blanco** o una aplicación que carga archivos obsoletos. DocBits puede usar Service Workers y la caché del navegador para cargar los archivos de la aplicación. Esta página muestra la instantánea de diagnóstico actual del navegador y ofrece acciones de mantenimiento para problemas relacionados con la caché. La instantánea por sí sola no establece la causa de una pantalla en blanco ni demuestra que una instalación PWA esté en buen estado.

## Cómo acceder

La página está pensada para administradores y no está enlazada en la barra lateral. Hay dos formas de abrirla:

* Abra la URL directamente: `https://app.docbits.com/debug/pwa-cache-status`
* Desde la aplicación principal (por ejemplo, el Panel), pulse <kbd>Ctrl</kbd> + <kbd>K</kbd> (o <kbd>Cmd</kbd> + <kbd>K</kbd> en macOS) para abrir la [Búsqueda Rápida Global](../global-quick-search.md), escriba "PWA Cache Status" y pulse <kbd>Enter</kbd> sobre ese resultado.

<figure><img src="../../../.gitbook/assets/dbdc-990-pwa-cache-status-page-es-20261111.png" alt="Página de diagnóstico PWA Cache con el estado del Service Worker, la información de versión, la lista de elementos en caché y los cuatro botones de acción"><figcaption><p>La página de diagnóstico PWA Cache en una sesión en español: paneles de estado, las cuatro acciones y el aviso de depuración. Los textos de esta página de diagnóstico siguen en inglés porque la aplicación todavía no los traduce. Los valores de versión y los recuentos de registros y de caché varían según el navegador y el entorno.</p></figcaption></figure>

## Leer los paneles de estado

* **Service Worker** — **Available: Yes/No** indica si el navegador admite la API de Service Worker. **Registrations** cuenta los registros del origen actual del navegador. Estos valores no demuestran que DocBits esté instalado como PWA, que un worker controle esta página ni que la instalación esté en buen estado.
* **Version** — **Current** es la versión de la aplicación que entrega la compilación cargada. **Stored** es la línea base guardada para este paquete de la aplicación en el navegador; no es un inventario de las versiones de todos los archivos en caché. **Mismatch: Yes** aparece solo cuando ambos valores se conocen y difieren. Una versión actual vacía o **Stored: Not set** no demuestran que las cachés estén al día, aunque **Mismatch** muestre _No_.
* **Cached Items** — enumera los nombres de todas las cachés de CacheStorage del origen actual, no archivos individuales ni solo cachés de DocBits. El recuento es el número de nombres de caché. _No caches found_ significa que esta instantánea no contiene nombres de caché de CacheStorage; no dice nada sobre otros almacenamientos del navegador ni sobre la caché HTTP normal del navegador.

Los valores vacíos o un recuento de cero también pueden deberse a API no disponibles o a lecturas de diagnóstico fallidas; no demuestran que el navegador no tenga recursos en caché.

Un origen es la combinación de protocolo, host y puerto. Estas herramientas actúan sobre todas las cachés y todos los registros de ese origen, incluidos los que usan otras rutas de la aplicación.

## Las cuatro acciones

| Acción | Qué hace |
| --- | --- |
| **Reload Page** | Realiza una recarga normal de la página. No borra cachés de forma explícita ni omite un Service Worker. |
| **Clear All Caches** | Intenta eliminar todas las cachés de CacheStorage de este origen y actualiza la instantánea de diagnóstico. Las cargas siguientes pueden necesitar descargar los archivos de nuevo. |
| **Unregister Service Workers** | Intenta anular el registro de todos los Service Workers de este origen y actualiza la instantánea de diagnóstico. Compruebe el estado resultante antes de dar por hecho que la limpieza ha funcionado. |
| **Emergency Cleanup** | Intenta eliminar las cachés y anular el registro de los Service Workers a la vez, y después programa una recarga normal de la página. Solo intenta guardar la línea base de la versión actual cuando los dos pasos de limpieza informan de éxito y hay una versión actual de la aplicación disponible. Un fallo de almacenamiento del navegador puede impedir igualmente que se guarde la línea base. Si uno de los dos pasos de limpieza falla, se conserva la línea base anterior. |

⚠️ **Advertencia:** Estas herramientas son solo para depuración. Use **Emergency Cleanup** únicamente ante un problema de pantalla en blanco. El borrado de cachés puede eliminar datos en caché y recursos sin conexión de aplicaciones del mismo origen; no dé por hecho que las cachés solo contienen archivos prescindibles de la aplicación. La siguiente carga puede ser más lenta o requerir una conexión de red disponible. Una notificación de éxito o una recarga programada por sí solas no demuestran que todas las operaciones de limpieza hayan funcionado.

## Flujo típico de solución de problemas

1. Abra la página PWA Cache Status y anote **Current**, **Stored**, **Mismatch**, el recuento de registros y los nombres de caché. Una discrepancia es una pista de diagnóstico, no un diagnóstico completo.
2. Si corresponde a su sesión de solución de problemas, pruebe **Reload Page**. Es una recarga normal y puede seguir usando respuestas en caché.
3. Si la pantalla sigue en blanco, revise el origen y la advertencia anterior antes de usar **Clear All Caches**; después recargue la página y vuelva a inspeccionar su estado.
4. Use **Emergency Cleanup** solo si el problema de pantalla en blanco continúa. Intenta las dos operaciones de limpieza y programa una recarga; la línea base solo cambia bajo las condiciones de éxito descritas arriba. Si la limpieza falla, conserve la línea base anterior como pista y contacte con el soporte en lugar de dar por resuelto el problema.
5. Si nada de esto ayuda, recopile el diagnóstico con el **Recopilador de depuración** (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>) y envíelo al soporte; consulte [Recopilador de depuración](../debug-collector.md). Revise el diagnóstico en busca de información sensible antes de compartirlo.
