# Cache Management

<figure><img src="../../.gitbook/assets/cache_management.png" alt="Cache Management"><figcaption><p>Página Cache Management</p></figcaption></figure>

Cache Management controla la limpieza automática de la caché de los datos a los que se accede con frecuencia. Activar el almacenamiento en caché mejora el rendimiento al reducir las llamadas repetidas a la API.

## Clear Cache

Haga clic en el botón **Clear Cache** (arriba a la derecha) para invalidar manualmente y de inmediato todos los datos almacenados en caché.

## Tabla de caché

| Columna | Descripción |
|--------|-------------|
| **Object** | El tipo de datos almacenados en caché (por ejemplo, Receive Delivery Cache, Purchase Order Cache). |
| **Status** | Interruptor para activar o desactivar el almacenamiento en caché de este objeto. |
| **TTL** | Time to Live en minutos: durante cuánto tiempo siguen siendo válidos los datos almacenados en caché antes de actualizarse automáticamente. Establezca `0` para desactivar la caducidad automática. |

## Cachés disponibles

| Caché | Descripción |
|-------|-------------|
| **Receive Delivery Cache** | Almacena en caché los datos de recepción de mercancías utilizados durante el PO matching. |
| **Purchase Order Cache** | Almacena en caché los datos de pedidos de compra para una búsqueda más rápida durante el procesamiento de documentos. |
| **Task and Notification Cache** | Almacena en caché los recuentos de tareas y los datos de notificaciones que se muestran en el panel. |
