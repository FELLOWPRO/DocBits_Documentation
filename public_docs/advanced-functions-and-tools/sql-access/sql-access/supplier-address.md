# Dirección del proveedor

## Columnas

* `org_id`: ID de la organización
* `customer_number`: interno
* `supplier_number`: interno
* `address_id`: interno
* `supplier_name`: Supplier Name
* `address_1`: interno
* `address_2`: interno
* `address_3`: interno
* `address_4`: interno
* `zip_code`: interno
* `town_city`: interno
* `country_code`: interno
* `created_by`: integer
* `created_on`: marca de tiempo con zona horaria
* `last_modified_on`: marca de tiempo con zona horaria
* `is_deleted`: boolean
* `sub_org_id`: interno
* `id`: interno

## Análisis y descripción

```markdown
# Documentación técnica de la tabla `public.supplier_address`

## Introducción

La tabla `public.supplier_address` está diseñada para almacenar información relacionada con las direcciones de los proveedores. Contiene diversos campos que recogen datos como los ID de la organización, los números de cliente y de proveedor, varias líneas de dirección, datos de contacto, metadatos de creación y modificación y el estado de eliminación. Esta tabla se utiliza probablemente en un sistema para gestionar la información de los proveedores y sus direcciones, algo fundamental para la logística, la facturación y el contacto.

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
- **Contenido típico**: Nombre del proveedor, p. ej., "Cake Corp. GmbH Qualitätsstrawberrys".

### address_1
- **Significado**: Esta columna almacena la línea principal de la dirección del proveedor.
- **Función**: Campo descriptivo para la información de la dirección.
- **Contenido típico**: Dirección postal, p. ej., "Irrweg. 42, D-12345 Blastadt".

### address_2
- **Significado**: Esta columna almacena la segunda línea de la dirección del proveedor, si procede.
- **Función**: Campo complementario para la información de la dirección.
- **Contenido típico**: Datos adicionales de la dirección, con frecuencia vacíos.

### address_3
- **Significado**: Esta columna almacena la tercera línea de la dirección del proveedor, si procede.
- **Función**: Campo complementario para la información de la dirección.
- **Contenido típico**: Datos adicionales de la dirección, con frecuencia vacíos.

### address_4
- **Significado**: Esta columna almacena la cuarta línea de la dirección del proveedor, si procede.
- **Función**: Campo complementario para la información de la dirección.
- **Contenido típico**: Datos adicionales de la dirección, con frecuencia vacíos.

### zip_code
- **Significado**: Esta columna almacena el código postal de la dirección del proveedor.
- **Función**: Campo descriptivo para la identificación geográfica.
- **Contenido típico**: Código postal numérico, p. ej., "06449".

### town_city
- **Significado**: Esta columna almacena el nombre de la localidad o ciudad de la dirección del proveedor.
- **Función**: Campo descriptivo para la identificación geográfica.
- **Contenido típico**: Nombre de la localidad o ciudad, p. ej., "Aschersleben".

### country_code
- **Significado**: Esta columna almacena el código de país ISO de la dirección del proveedor.
- **Función**: Campo descriptivo para la identificación del país.
- **Contenido típico**: Código de país de dos letras, p. ej., "DE".

### created_by
- **Significado**: Esta columna almacena el identificador del usuario o del sistema que creó el registro.
- **Función**: Campo técnico para el seguimiento de la creación del registro.
- **Contenido típico**: Entero que representa un ID de usuario.

### created_on
- **Significado**: Esta columna almacena la marca de tiempo de la creación del registro.
- **Función**: Campo técnico para el seguimiento de la hora de creación del registro.
- **Contenido típico**: Marca de tiempo con zona horaria, p. ej., "2021-11-25 11:24:33 UTC".

### last_modified_on
- **Significado**: Esta columna almacena la marca de tiempo de la última modificación del registro.
- **Función**: Campo técnico para el seguimiento de la hora de la última actualización.
- **Contenido típico**: Marca de tiempo con zona horaria, con frecuencia `None`.

### is_deleted
- **Significado**: Esta columna indica si el registro está marcado como eliminado.
- **Función**: Campo técnico para la funcionalidad de borrado lógico.
- **Contenido típico**: Valor booleano, p. ej., `False`.

### sub_org_id
- **Significado**: Esta columna almacena el identificador de una suborganización, si procede.
- **Función**: Clave externa o identificador de suborganizaciones.
- **Contenido típico**: UUID, con frecuencia vacío.

### id
- **Significado**: Esta columna almacena el identificador único del registro.
- **Función**: Clave primaria de la tabla.
- **Contenido típico**: UUID que representa el registro.

```
