# public.rest\_api\_lookup\_configurations

## Tabla `public.rest_api_lookup_configurations`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `sub_org_id`: interno
* `data_key`: interno
* `url`: interno
* `method`: interno
* `params`: text
* `headers`: text
* `body`: text
* `body_type`: interno
* `authentication_type`: interno
* `authentication_json`: text
* `data_base_path`: interno
* `column_paths`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `is_template`: boolean
* `is_dynamic`: boolean

### Análisis y descripción

## Documentación técnica: tabla `public.rest_api_lookup_configurations`

### Introducción

La tabla `public.rest_api_lookup_configurations` está diseñada para almacenar configuraciones de búsquedas (lookups) mediante API REST dentro de una organización. Esta tabla contiene la información esencial para realizar solicitudes a la API, incluidos los detalles de los endpoints, los métodos de autenticación y la configuración de solicitud y respuesta. Parece utilizarse para construir dinámicamente llamadas a la API y analizar sus resultados.

### Descripción de las columnas

#### id

* **Significado**: Un identificador único para cada entrada de configuración.
* **Función**: Clave primaria.
* **Contenido típico**: Cadenas UUID como `5e9b3637-79a1-4535-99cf-9247dfa48960`.
* **Nota**: Es la clave única para identificar una configuración de lookup de API específica.

#### org\_id

* **Significado**: Identificador de la organización propietaria de la configuración.
* **Función**: Clave externa.
* **Contenido típico**: Cadenas UUID que representan ID de organización.
* **Nota**: Vincula la configuración con una organización.

#### sub\_org\_id

* **Significado**: Identificador de una suborganización dentro de la organización principal.
* **Función**: Clave externa.
* **Contenido típico**: Cadenas UUID que representan ID de suborganización.
* **Nota**: Permite una mayor granularidad dentro de las organizaciones.

#### data\_key

* **Significado**: Una etiqueta o clave para identificar los datos o el endpoint de la API.
* **Función**: Campo descriptivo.
* **Contenido típico**: Texto descriptivo como `bank_codes`.
* **Nota**: Se utiliza para distinguir entre distintos tipos de datos o endpoints.

#### url

* **Significado**: La URL del endpoint de la API al que se debe llamar.
* **Función**: Campo descriptivo.
* **Contenido típico**: Cadenas de URL como `/M3/m3api-rest/v2/execute/CRS692MI/LstByID`.
* **Nota**: Representa el endpoint al que se envía la solicitud HTTP.

#### method

* **Significado**: Método HTTP utilizado para la solicitud a la API.
* **Función**: Campo descriptivo.
* **Contenido típico**: Métodos HTTP habituales como `GET`.
* **Nota**: Determina el tipo de solicitud HTTP que se realizará.

#### params

* **Significado**: Parámetros que se incluirán en la solicitud a la API.
* **Función**: Campo de configuración.
* **Contenido típico**: JSON o pares clave-valor (a menudo `None` si no se utiliza).
* **Nota**: Contiene los parámetros dinámicos de la solicitud.

#### headers

* **Significado**: Cabeceras HTTP que se incluirán en la solicitud.
* **Función**: Campo de configuración.
* **Contenido típico**: Datos JSON o de texto (a menudo `None` si no se utiliza).
* **Nota**: Se utiliza para incluir metadatos adicionales en la solicitud.

#### body

* **Significado**: El cuerpo de la solicitud HTTP.
* **Función**: Campo de configuración.
* **Contenido típico**: Datos JSON u otros datos serializados (a menudo `None` si no se utiliza).
* **Nota**: Contiene la carga útil de las solicitudes POST/PUT.

#### body\_type

* **Significado**: Especifica el formato del cuerpo de la solicitud.
* **Función**: Campo descriptivo.
* **Contenido típico**: Tipos MIME como `application/json`.
* **Nota**: Indica el tipo de contenido del cuerpo.

#### authentication\_type

* **Significado**: Tipo de autenticación utilizado para la solicitud a la API.
* **Función**: Campo descriptivo.
* **Contenido típico**: Métodos de autenticación como `ionapi`.
* **Nota**: Determina cómo se autenticará la solicitud.

#### authentication\_json

* **Significado**: Detalles de la configuración de autenticación en formato JSON.
* **Función**: Campo de configuración.
* **Contenido típico**: Cadenas JSON con información de autenticación.
* **Nota**: Contiene las credenciales y los detalles del endpoint para la autenticación.

#### data\_base\_path

* **Significado**: Ruta dentro de la respuesta de la API de la que se extraen los datos.
* **Función**: Campo de configuración.
* **Contenido típico**: Expresiones de ruta JSON como `$[results][0][records]`.
* **Nota**: Se utiliza para analizar los datos de la respuesta de la API.

#### column\_paths

* **Significado**: Asigna los campos de datos a las columnas para su extracción.
* **Función**: Campo de configuración.
* **Contenido típico**: Cadenas JSON que asignan campos de la respuesta de la API a nombres de columna.
* **Nota**: Facilita la extracción de datos de la respuesta de la API.

#### created\_by

* **Significado**: Identificador del usuario que creó la configuración.
* **Función**: Campo técnico.
* **Contenido típico**: ID enteros como `1`.
* **Nota**: Registra quién creó la entrada de configuración.

#### created\_on

* **Significado**: Marca de tiempo de cuándo se creó la configuración.
* **Función**: Campo técnico.
* **Contenido típico**: Marcas de tiempo como `2024-01-24T09:14:24.788788Z`.
* **Nota**: Indica la fecha y la hora de creación.

#### last\_modified\_on

* **Significado**: Marca de tiempo de la última modificación.
* **Función**: Campo técnico.
* **Contenido típico**: Marcas de tiempo (a menudo `None` si no se ha modificado).
* **Nota**: Registra la hora de la última actualización.

#### is\_deleted

* **Significado**: Indicador que señala si una configuración está marcada como eliminada.
* **Función**: Campo técnico.
* **Contenido típico**: Valores booleanos como `False`.
* **Nota**: Se utiliza para el borrado lógico de configuraciones.

#### deleted\_on

* **Significado**: Marca de tiempo de cuándo se marcó la configuración como eliminada.
* **Función**: Campo técnico.
* **Contenido típico**: Marcas de tiempo (a menudo un valor de marcador de posición si no se ha eliminado).
* **Nota**: Registra cuándo se marcó la configuración como eliminada.

#### is\_template

* **Significado**: Indica si la configuración sirve como plantilla.
* **Función**: Campo descriptivo.
* **Contenido típico**: Valores booleanos como `True`.
* **Nota**: Identifica las plantillas para su reutilización.

#### is\_dynamic

* **Significado**: Especifica si la configuración es dinámica.
* **Función**: Campo descriptivo.
* **Contenido típico**: Valores booleanos como `False`.
* **Nota**: Determina si la configuración se adapta a datos cambiantes.
