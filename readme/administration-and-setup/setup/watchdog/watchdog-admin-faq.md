# Preguntas frecuentes de administración de WatchDog y resolución de problemas

<figure><img src="../../../.gitbook/assets/watchdog-troubleshooting-infographic.svg" alt="Guía rápida de resolución de problemas de WatchDog"><figcaption></figcaption></figure>

Esta documentación ayuda a los administradores a entender los mensajes de error de WatchDog y a resolver problemas.

**Ubicación en la interfaz:** Settings → Document Processing → WatchDog

---

## 1. Páginas de ajustes de WatchDog (interfaz)

### 1.1 Pestaña General

<figure><img src="../../../.gitbook/assets/watchdog_v2_01.png" alt="Pestaña General de WatchDog"><figcaption></figcaption></figure>

* **Download:** obtenga la última versión de WatchDog.exe
* **API Key:** copie el comando de configuración
* **Auto-Update Schedule:** configure la frecuencia de actualización
* **Installation Guide:** instrucciones de configuración paso a paso

### 1.2 Pestaña Configurations

* **Import Configurations:** definen las carpetas vigiladas y los tipos de documento
* **Export Configurations:** definen los destinos y métodos de exportación
* **Bulk Copy:** copia configuraciones entre suborganizaciones
* **Import/Export:** importa y exporta configuraciones como JSON

> **Importante:** Las configuraciones de exportación ahora **requieren un tipo de documento** (`doc_type`). Las configuraciones sin un tipo de documento válido serán rechazadas.

### 1.3 Pestaña Status

<figure><img src="../../../.gitbook/assets/watchdog_v2_status.png" alt="Estado del servicio WatchDog"><figcaption></figcaption></figure>

* Muestra en tiempo real el estado de conexión de WatchDog
* **Campos nuevos:** `last_restart`, `version_first_seen`, `latest_version_checked_at`
* **Información del sistema:** ruta de instalación, RAM libre, espacio libre en disco

### 1.4 Pestaña Logs

<figure><img src="../../../.gitbook/assets/watchdog_v2_05.png" alt="Registros de WatchDog"><figcaption></figcaption></figure>

* Muestra todos los eventos de WatchDog desde OpenSearch
* Se puede filtrar por tipo de evento, período de tiempo, etc.
* **Tipos de evento:**
  * `FILE_IMPORT_STARTED`: inicio de la importación de archivos
  * `FILE_IMPORT_COMPLETED`: importación correcta
  * `FILE_IMPORT_FAILED`: importación fallida
  * `EXPORT_STARTED`: inicio de la exportación
  * `EXPORT_COMPLETED`: exportación correcta
  * `EXPORT_FAILED`: exportación fallida
  * `FOLDER_VALIDATION_FAILED`: carpeta no accesible
  * `CONFIG_LOADED`: configuración cargada
  * `SERVICE_RESTART_INITIATED`: reinicio del servicio solicitado
  * `SERVICE_RESTART_COMPLETED`: servicio reiniciado

### 1.5 Pestaña XSLT Templates

<figure><img src="../../../.gitbook/assets/watchdog_v2_06.png" alt="Lista de plantillas XSLT"><figcaption></figcaption></figure>

* Cargue y gestione plantillas de transformación XSLT
* Validación en vivo con análisis de campos
* Vincule plantillas a configuraciones de exportación

---

## 2. Mensajes de error de validación de carpetas

| Error | Significado | Solución |
| :--- | :--- | :--- |
| `not_found` | La carpeta no existe | Cree la carpeta o corrija la ruta |
| `no_read_access` | Sin permiso de lectura | Establezca permisos para la cuenta de servicio de WatchDog |
| `no_write_access` | Sin permiso de escritura | Conceda permisos de escritura a la cuenta de servicio |
| `not_configured` | Ruta de carpeta no configurada | Introduzca la ruta en la configuración |

**Carpetas afectadas:**

* **Watch Folder (Import):** donde WatchDog busca archivos nuevos
* **Success Folder:** donde se mueven los archivos importados correctamente
* **Export Folder:** donde se escriben los archivos XML/PDF exportados

---

## 3. Mensajes de error de importación

| Error | Significado | Solución |
| :--- | :--- | :--- |
| `file_not_found` | El archivo se eliminó antes de la importación | Proporcione el archivo de nuevo |
| `invalid_file_type` | Solo se admiten archivos PDF | Elimine los demás tipos de archivo |
| `api_not_accessible` | No se puede acceder a la API de DocBits | Compruebe la red y el firewall, verifique la URL de la API |
| `api_check_failed` | Falló la comprobación de estado de la API | Compruebe la clave de API y la conexión |
| `upload_failed` | Falló la carga a la API | Compruebe la clave de API, la red y el estado del servidor |

---

## 4. Mensajes de error de exportación

| Error | Significado | Solución |
| :--- | :--- | :--- |
| `transformation_error` | Falló la transformación XSLT | Revise la plantilla XSLT y valide la estructura XML |
| `folder_error` | No se puede acceder a la carpeta de exportación | Cree la carpeta y revise los permisos |
| `file_write_error` | No se pudo escribir el archivo | Revise el espacio en disco, los permisos y los bloqueos de archivo |
| `permission_denied` | Sin permiso de escritura | Establezca los permisos de la cuenta de servicio |
| `creation_failed` | No se pudo crear la carpeta | Revise los permisos de la carpeta superior |
| `no_config_match` | No hay ninguna configuración de exportación coincidente | Cree una configuración de exportación con el tipo de documento correcto |

> **Nota:** Las configuraciones de exportación requieren un `doc_type`. Si ve `no_config_match`, compruebe que existe una configuración de exportación activa para el tipo del documento.

---

## 5. Configuración desactivada: motivos

Cuando se desactiva una configuración, aparece uno de estos motivos:

| Motivo de desactivación | Significado |
| :--- | :--- |
| `Watch folder: not_found` | La carpeta de importación no existe |
| `Watch folder: no_read_access` | La carpeta de importación no se puede leer |
| `Export folder: not_found` | La carpeta de exportación no existe |
| `Export folder: no_write_access` | La carpeta de exportación no admite escritura |
| `Success folder: not_found` | La carpeta de éxito no existe |
| `Success folder: no_write_access` | La carpeta de éxito no admite escritura |

**Reactivación automática:** WatchDog comprueba las carpetas con regularidad (cada 60 segundos). En cuanto la carpeta vuelve a estar accesible, la configuración se reactiva automáticamente.

---

## 6. Carpeta de errores (`_error`)

Los archivos fallidos se mueven a la carpeta `_error`:

**Ubicación:** `{import_folder}/_error/{error_type}/`

**Formato de archivo:** `{original_name}_{YYYYMMDD_HHMMSS}.pdf`

**Archivo complementario (sidecar):** cada archivo fallido tiene un archivo complementario `.error` con:

```
Error Type: transformation_error
Error Message: XSLT template not found
Timestamp: 2026-03-26 08:30:15
Original File: invoice_001.pdf
Original Path: C:\WatchDog\Import\invoice_001.pdf
```

---

## 7. Heartbeat y estado de la conexión

WatchDog envía un heartbeat a DocBits aproximadamente cada 10 segundos con información del sistema:

| Datos enviados | Descripción |
| :--- | :--- |
| Timestamp | Hora actual |
| Version | Versión de WatchDog instalada |
| Last Restart | Hora del último reinicio del servicio |
| Auto-Update Enabled | Si la actualización automática está activa |
| Latest Version | Versión más reciente disponible |
| Installation Path | Dónde está instalado WatchDog |
| Free RAM / Disk | Recursos del sistema disponibles |

### Estado de la conexión

| Estado | Significado |
| :--- | :--- |
| ✅ **Online** | WatchDog está conectado y activo |
| ⚠️ **Offline** | Sin heartbeat desde hace más de 30 segundos |
| ❌ **Not Installed** | WatchDog nunca se ha conectado |

**Errores de heartbeat:**

* `Heartbeat failed - invalid API key` → la clave de API no es válida
* `Heartbeat failed: 401` → falló la autenticación
* `Heartbeat failed: 5xx` → problema del servidor

---

## 8. Problemas frecuentes y soluciones

### Problema: WatchDog no importa archivos

1. Compruebe si el servicio se está ejecutando: `services.msc` → WatchDog
2. Revisar los registros: Configuración → WatchDog → Pestaña Registros
3. Revise los permisos de carpeta de la cuenta de servicio de WatchDog
4. Pruebe la conexión con la API: `WatchDog.exe debug` en CMD
5. Verifique que el tipo de archivo sea PDF

### Problema: la exportación no funciona

1. ¿Existe una configuración de exportación con el tipo de documento correcto?
2. ¿Coincide el tipo de documento entre el documento y la configuración?
3. ¿Está vinculada la plantilla XSLT (para la exportación a carpeta)?
4. ¿Puede la cuenta de servicio escribir en la carpeta de exportación?
5. Para exportaciones a Infor: ¿están bien configuradas las credenciales de ION?

### Problema: la configuración está desactivada

1. ¿Existe la ruta de la carpeta?
2. ¿Hay permisos para `NT AUTHORITY\LOCAL SERVICE` o la cuenta de servicio?
3. ¿Se puede acceder a la unidad de red? (Revise las rutas UNC)
4. WatchDog se reactivará automáticamente cuando las carpetas vuelvan a estar disponibles

### Problema: falla la transformación XSLT

1. ¿Es válida la plantilla XSLT? (use la pestaña XSLT Templates → Validate)
2. ¿Corresponde la plantilla al tipo de documento?
3. Revise la estructura XML del documento
4. La exportación a carpeta V3 utiliza transformación en el servidor: compruebe la conectividad con la API

### Problema: falla la exportación por REST API

1. ¿Están configuradas las credenciales ION OAuth en la configuración de exportación?
2. ¿Se puede acceder al endpoint de la API de destino desde el servidor de WatchDog?
3. Compruebe que el formato del payload coincide con lo que espera la API de destino
4. Revise la configuración de la cadena de solicitudes en busca de errores de JSONPath

---

## 9. Comandos de línea de comandos

```bash
# Configure API connection
WatchDog.exe -api YOUR_API_KEY

# Install Service
WatchDog.exe install

# Start Service
WatchDog.exe start

# Stop Service
WatchDog.exe stop

# Run in debug mode (console output)
WatchDog.exe debug

# Uninstall Service
WatchDog.exe remove

# Show version
WatchDog.exe --version

# List watch folders
WatchDog.exe --list-folders

# Add/remove watch folder
WatchDog.exe --add-folder "C:\Import\Invoices"
WatchDog.exe --remove-folder "C:\Import\Invoices"

# Check Windows service status
sc query WatchDog
```

---

## 10. Archivos de registro

**Ubicación:** `C:\WatchDog\logs\{module}\`

**Formato de registro:**
```
INFO  - 2026-03-26 10:00:00 - module_name - Message - function=func_name - line=42
```

**Nivel de registro:** DEBUG, INFO, WARNING, ERROR

**Registros remotos:** WatchDog también envía registros a DocBits (visibles en la pestaña Logs) y, opcionalmente, al registro en la nube de Logtail.
