# Tabla supplier\_address

## Columnas

* `org_id`: ID to organisation
* `customer_number`: internal
* `supplier_number`: internal
* `address_id`: internal
* `supplier_name`: Supplier Name
* `address_1`: internal
* `address_2`: internal
* `address_3`: internal
* `address_4`: internal
* `zip_code`: internal
* `town_city`: internal
* `country_code`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: internal
* `id`: internal

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.supplier_address`

## Introducción

La tabla `public.supplier_address` está diseñada para almacenar información relacionada con las direcciones de los proveedores. Contiene diversos campos que recogen datos como los ID de organización, los números de cliente y de proveedor, varias líneas de dirección, datos de contacto, metadatos de creación y modificación y el estado de eliminación. Es probable que esta tabla se utilice en un sistema para gestionar la información de los proveedores y sus respectivas direcciones, lo que puede ser fundamental para la logística, la facturación y el contacto.

## Descripción de las columnas

### org_id
- **Significado**: Esta columna almacena el identificador único de la organización.
- **Función**: Clave externa, posiblemente vinculada a una tabla de organizaciones.
- **Contenido típico**: UUID que representa una organización.

### customer_number
- **Significado**: Esta columna puede almacenar un número único asignado a los clientes.
- **Función**: Identificador de clientes.
- **Contenido típico**: Cadena alfanumérica que representa los números de cliente.

### supplier_number
- **Significado**: Esta columna almacena un número único asignado a los proveedores.
- **Función**: Identificador de proveedores.
- **Contenido típico**: Cadena numérica que representa los números de proveedor.

### address_id
- **Significado**: Esta columna probablemente almacena el tipo de dirección, como 'Discrete' o 'Text'.
- **Función**: Campo descriptivo para la categorización de direcciones.
- **Contenido típico**: Valores como 'Discrete', 'Text'.

### supplier_name
- **Significado**: Esta columna almacena el nombre del proveedor.
- **Función**: Campo descriptivo para la identificación del proveedor.
- **Contenido típico**: Nombre del proveedor, por ejemplo, "Cake Corp. GmbH Qualitätsstrawberrys".

### address_1
- **Significado**: Esta columna almacena la línea principal de la dirección del proveedor.
- **Función**: Campo descriptivo de la información de la dirección.
- **Contenido típico**: Dirección postal, por ejemplo, "Irrweg. 42, D-12345 Blastadt".

### address_2
- **Significado**: Esta columna almacena la segunda línea de la dirección del proveedor, si procede.
- **Función**: Campo complementario de la información de la dirección.
- **Contenido típico**: Detalles adicionales de la dirección, a menudo vacío.

### address_3
- **Significado**: Esta columna almacena la tercera línea de la dirección del proveedor, si procede.
- **Función**: Campo complementario de la información de la dirección.
- **Contenido típico**: Detalles adicionales de la dirección, a menudo vacío.

### address_4
- **Significado**: Esta columna almacena la cuarta línea de la dirección del proveedor, si procede.
- **Función**: Campo complementario de la información de la dirección.
- **Contenido típico**: Detalles adicionales de la dirección, a menudo vacío.

### zip_code
- **Significado**: Esta columna almacena el código postal de la dirección del proveedor.
- **Función**: Campo descriptivo para la identificación geográfica.
- **Contenido típico**: Código postal numérico, por ejemplo, "06449".

### town_city
- **Significado**: Esta columna almacena el nombre de la localidad o ciudad de la dirección del proveedor.
- **Función**: Campo descriptivo para la identificación geográfica.
- **Contenido típico**: Nombre de la localidad o ciudad, por ejemplo, "Aschersleben".

### country_code
- **Significado**: Esta columna almacena el código ISO del país de la dirección del proveedor.
- **Función**: Campo descriptivo para la identificación del país.
- **Contenido típico**: Código de país de dos letras, por ejemplo, "DE".

### created_by
- **Significado**: Esta columna almacena el identificador del usuario o del sistema que creó el registro.
- **Función**: Campo técnico para el seguimiento de la creación de registros.
- **Contenido típico**: Entero que representa un ID de usuario.

### created_on
- **Significado**: Esta columna almacena la marca de tiempo del momento en que se creó el registro.
- **Función**: Campo técnico para el seguimiento de la hora de creación del registro.
- **Contenido típico**: Marca de tiempo con zona horaria, por ejemplo, "2021-11-25 11:24:33 UTC".

### last_modified_on
- **Significado**: Esta columna almacena la marca de tiempo de la última modificación del registro.
- **Función**: Campo técnico para el seguimiento de la hora de la última actualización.
- **Contenido típico**: Marca de tiempo con zona horaria, a menudo `None`.

### is_deleted
- **Significado**: Esta columna indica si el registro está marcado como eliminado.
- **Función**: Campo técnico para la funcionalidad de eliminación lógica (soft delete).
- **Contenido típico**: Valor booleano, por ejemplo, `False`.

### sub_org_id
- **Significado**: Esta columna almacena un identificador de una suborganización, si procede.
- **Función**: Clave externa o identificador de suborganizaciones.
- **Contenido típico**: UUID, a menudo vacío.

### id
- **Significado**: Esta columna almacena el identificador único del registro.
- **Función**: Clave primaria de la tabla.
- **Contenido típico**: UUID que representa el registro.

```
