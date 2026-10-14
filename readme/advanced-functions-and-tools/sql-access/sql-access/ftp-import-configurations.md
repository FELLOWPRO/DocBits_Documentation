# FTP Import Configurations

## Columnas

* `id`: interno
* `org_id`: ID de la organización
* `sub_org_id`: interno
* `server_url`: interno
* `username`: interno
* `password`: interno
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `port`: integer
* `default_directory`: interno
* `ftp_type`: interno
* `token`: interno
* `file_name_matching_patterns`: interno
* `last_mtime`: interno
* `auth_failed_count`: integer
* `auth_message`: text
* `ignore_certificate`: boolean
* `move_after_import`: boolean
* `destination_directory`: interno
* `import_directory`: interno
* `include_subfolder_content`: boolean

## Análisis y descripción

```markdown
# Documentación de la tabla de configuraciones de importación FTP

## Introducción

La tabla `public.ftp_import_configurations` está diseñada para almacenar los detalles de configuración de los procesos de importación por FTP. Contiene la información necesaria para conectarse a los servidores FTP, gestionar la autenticación y procesar las importaciones de archivos. Admite los protocolos FTP y SFTP e incluye campos con los datos del servidor FTP, las credenciales de autenticación y ajustes operativos, como si se deben mover los archivos tras la importación y si se debe incluir el contenido de las subcarpetas.

## Descripción de las columnas

### id
- **Significado**: Identificador único de cada registro de configuración de importación FTP.
- **Función**: Clave primaria.
- **Contenido típico**: Formato UUID, p. ej., `9862d8c6-bb61-4373-9616-d5f8c125eeb8`.

### org_id
- **Significado**: Identificador de la organización asociada a esta configuración.
- **Función**: Clave externa.
- **Contenido típico**: Formato UUID.

### sub_org_id
- **Significado**: Identificador de una suborganización, si procede.
- **Función**: Clave externa.
- **Contenido típico**: Formato UUID o `null` si no procede.

### server_url
- **Significado**: La URL o la dirección IP del servidor FTP.
- **Función**: Campo descriptivo.
- **Contenido típico**: Nombre de dominio o dirección IP, p. ej., `sftp.it.doxee.com`.

### username
- **Significado**: Nombre de usuario utilizado para la autenticación en el servidor FTP.
- **Función**: Campo descriptivo.
- **Contenido típico**: Nombre de usuario en texto plano.

### password
- **Significado**: Contraseña utilizada para la autenticación en el servidor FTP.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena de contraseña cifrada.

### is_active
- **Significado**: Indica si la configuración está activa actualmente.
- **Función**: Indicador de estado.
- **Contenido típico**: `True` o `False`.

### created_by
- **Significado**: Identificador del usuario que creó la configuración.
- **Función**: Clave externa.
- **Contenido típico**: Entero que representa el ID de usuario.

### created_on
- **Significado**: Marca de tiempo de la creación de la configuración.
- **Función**: Campo de auditoría.
- **Contenido típico**: Fecha y hora con información de zona horaria.

### last_modified_on
- **Significado**: Marca de tiempo de la última modificación de la configuración.
- **Función**: Campo de auditoría.
- **Contenido típico**: Fecha y hora con información de zona horaria.

### is_deleted
- **Significado**: Indica si la configuración se ha marcado como eliminada.
- **Función**: Indicador de estado.
- **Contenido típico**: `True` o `False`.

### deleted_on
- **Significado**: Marca de tiempo del momento en que la configuración se marcó como eliminada.
- **Función**: Campo de auditoría.
- **Contenido típico**: Fecha y hora con información de zona horaria o una fecha predeterminada para los registros no eliminados.

### port
- **Significado**: Número de puerto utilizado para conectarse al servidor FTP.
- **Función**: Campo descriptivo.
- **Contenido típico**: Entero, p. ej., `22` para SFTP.

### default_directory
- **Significado**: La ruta del directorio predeterminado en el servidor FTP.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena con la ruta del directorio.

### ftp_type
- **Significado**: Tipo de protocolo FTP utilizado (p. ej., FTP, SFTP).
- **Función**: Campo descriptivo.
- **Contenido típico**: `FTP` o `SFTP`.

### token
- **Significado**: Token de seguridad para una autenticación o identificación adicional.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena cifrada o codificada.

### file_name_matching_patterns
- **Significado**: Patrones utilizados para identificar los nombres de archivo que se importan.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadenas de patrones o `null`.

### last_mtime
- **Significado**: Hora de la última modificación de los archivos, utilizada para filtrar las importaciones.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena que representa una marca de tiempo o `null`.

### auth_failed_count
- **Significado**: Contador de intentos de autenticación fallidos.
- **Función**: Campo descriptivo.
- **Contenido típico**: Entero, p. ej., `0` o `5`.

### auth_message
- **Significado**: Mensaje que describe el resultado del último intento de autenticación.
- **Función**: Campo descriptivo.
- **Contenido típico**: Mensaje de texto o `null`.

### ignore_certificate
- **Significado**: Indica si se debe omitir la validación del certificado SSL.
- **Función**: Indicador de estado.
- **Contenido típico**: `True` o `False`.

### move_after_import
- **Significado**: Indica si los archivos deben moverse una vez completada la importación.
- **Función**: Indicador de estado.
- **Contenido típico**: `True` o `False`.

### destination_directory
- **Significado**: Ruta del directorio al que deben moverse los archivos tras la importación.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena con la ruta del directorio o `null`.

### import_directory
- **Significado**: Ruta del directorio desde el que se importan los archivos.
- **Función**: Campo descriptivo.
- **Contenido típico**: Cadena con la ruta del directorio o `null`.

### include_subfolder_content
- **Significado**: Indica si el contenido de las subcarpetas debe incluirse en la importación.
- **Función**: Indicador de estado.
- **Contenido típico**: `True` o `False`.
```

Esta documentación ofrece una visión completa de cada columna de la tabla `public.ftp_import_configurations`: explica su finalidad, su función y su contenido típico, a partir de los datos de ejemplo y de los nombres de las columnas.
