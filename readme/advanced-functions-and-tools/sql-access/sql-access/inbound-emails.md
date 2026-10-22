# Correos electrónicos entrantes

## Tabla `public.inbound_emails`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `is_active`: boolean
* `email_senders`: interno
* `email_receiver`: interno
* `token`: interno
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_by`: interno
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `deleted_by`: interno
* `deleted_on`: marca de tiempo con zona horaria

### Análisis y descripción

## Documentación técnica: tabla `public.inbound_emails`

### Introducción

La tabla `public.inbound_emails` está diseñada para almacenar y gestionar información sobre los correos electrónicos recibidos por una organización. Esta tabla hace un seguimiento de los datos del remitente y del destinatario, del estado del correo y de diversos metadatos relacionados con la creación, modificación y eliminación de registros. Parece formar parte de un sistema de gestión de correo electrónico dentro de una organización, posiblemente utilizado para el seguimiento de las comunicaciones de correo entrante.

### Descripción de las columnas

#### id

* **Significado**: Identificador único de cada registro de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena única, probablemente un UUID, como `'42bf9383-73bf-4b46-9862-3c3a1d97ac80'`.

#### org\_id

* **Significado**: Identificador de la organización asociada con el correo entrante.
* **Función**: Clave externa, que enlaza con otra tabla que contiene los datos de la organización.
* **Contenido típico**: Una cadena única, probablemente un UUID, como `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### is\_active

* **Significado**: Indica si el registro del correo está activo actualmente.
* **Función**: Indicador de estado.
* **Contenido típico**: Un valor booleano, `True` o `False`.

#### email\_senders

* **Significado**: Almacena información sobre el o los remitentes del correo.
* **Función**: Campo de datos.
* **Contenido típico**: Una cadena de tipo JSON con los datos de los remitentes, p. ej., `"[{'email': '', 'sub_org': ''}]"`.

#### email\_receiver

* **Significado**: Dirección de correo electrónico del destinatario principal.
* **Función**: Campo de datos.
* **Contenido típico**: Una cadena con una dirección de correo electrónico. En el ejemplo está vacía, lo que sugiere un uso opcional o variable.

#### token

* **Significado**: Un token asociado con el correo, posiblemente para autenticación o identificación.
* **Función**: Campo de autenticación o seguimiento.
* **Contenido típico**: Una cadena larga generada de forma aleatoria.

#### created\_by

* **Significado**: Identificador del usuario que creó el registro.
* **Función**: Clave externa, que enlaza con una tabla de usuarios o empleados.
* **Contenido típico**: Un entero que representa un ID de usuario, como `1`.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó el registro.
* **Función**: Campo de metadatos.
* **Contenido típico**: Un valor de fecha y hora con información de zona horaria, p. ej., `datetime.datetime(2024, 11, 25, 7, 43, 54, 266771, tzinfo=datetime.timezone.utc)`.

#### last\_modified\_by

* **Significado**: Identificador del usuario que modificó el registro por última vez.
* **Función**: Clave externa, que enlaza con una tabla de usuarios o empleados.
* **Contenido típico**: Puede ser un ID de usuario o nulo si no se ha realizado ninguna modificación.

#### last\_modified\_on

* **Significado**: Marca de tiempo de cuándo se modificó el registro por última vez.
* **Función**: Campo de metadatos.
* **Contenido típico**: Un valor de fecha y hora que indica la hora de la última modificación, p. ej., `datetime.datetime(2024, 11, 25, 7, 44, 48, 505384, tzinfo=datetime.timezone.utc)`.

#### is\_deleted

* **Significado**: Indica si el registro del correo se ha marcado como eliminado.
* **Función**: Indicador de estado.
* **Contenido típico**: Un valor booleano, `True` o `False`.

#### deleted\_by

* **Significado**: Identificador del usuario que marcó el registro como eliminado.
* **Función**: Clave externa, que enlaza con una tabla de usuarios o empleados.
* **Contenido típico**: Puede ser un ID de usuario o nulo si el registro no está eliminado.

#### deleted\_on

* **Significado**: Marca de tiempo de cuándo se marcó el registro como eliminado.
* **Función**: Campo de metadatos.
* **Contenido típico**: Un valor de fecha y hora que indica el momento de la eliminación, o una fecha predeterminada si no procede, p. ej., `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`.
