# Contabilización automática

## Tabla `public.auto_accounting`

### Columnas

* `id`: interno
* `org_id`: ID de la organización
* `supplier_name`: Nombre del proveedor
* `description`: interno
* `item_number`: interno
* `line_amount`: double precision
* `total_amount`: double precision
* `mapped_amount`: double precision
* `ledger_account`: interno
* `doc_id`: interno

### Análisis y descripción

## Documentación técnica de la tabla `public.auto_accounting`

### Introducción

La tabla `public.auto_accounting` está diseñada para gestionar y almacenar datos contables relacionados con diversos proveedores y organizaciones. La tabla recoge información sobre transacciones financieras, incluidos importes y cuentas contables, que son esenciales para la elaboración de informes y el análisis financiero.

### Descripción de las columnas

#### id

* **Significado**: Un identificador único para cada registro de la tabla.
* **Función**: Clave primaria.
* **Contenido típico**: Una cadena UUID que representa cada entrada de forma única.
* **Nota**: Garantiza que cada registro pueda identificarse de forma inequívoca.

#### org\_id

* **Significado**: Identificador de la organización asociada con el asiento contable.
* **Función**: Clave externa.
* **Contenido típico**: Una cadena UUID que enlaza con una organización de una tabla principal.
* **Nota**: Se utiliza para asociar los asientos contables con organizaciones específicas.

#### supplier\_name

* **Significado**: El nombre del proveedor que interviene en la transacción.
* **Función**: Campo descriptivo.
* **Contenido típico**: Texto que representa el nombre del proveedor, como "Fellow Consulting AG".
* **Nota**: Proporciona información sobre el proveedor relacionado con la transacción.

#### description

* **Significado**: Una breve descripción de la transacción o del artículo.
* **Función**: Campo descriptivo.
* **Contenido típico**: Texto que describe la transacción, como el nombre de un artículo ("apple" o "Peaches").
* **Nota**: Útil para comprender la naturaleza de la transacción.

#### item\_number

* **Significado**: Identificador de un artículo específico que interviene en la transacción.
* **Función**: Campo descriptivo.
* **Contenido típico**: Podría ser un identificador de producto o SKU, aunque no se proporcionan datos de ejemplo.
* **Nota**: Útil para el seguimiento o la referencia de artículos específicos.

#### line\_amount

* **Significado**: El importe monetario de una línea específica de la transacción.
* **Función**: Campo financiero.
* **Contenido típico**: Un valor decimal que representa el importe de una línea individual.
* **Nota**: Importante para el análisis financiero detallado a nivel de línea.

#### total\_amount

* **Significado**: El importe monetario total de la transacción.
* **Función**: Campo financiero.
* **Contenido típico**: Un valor decimal que representa el importe total de la transacción.
* **Nota**: Representa la suma de todos los importes de línea de una transacción.

#### mapped\_amount

* **Significado**: El importe que se ha asignado o vinculado a una cuenta específica.
* **Función**: Campo financiero.
* **Contenido típico**: Un valor decimal que indica qué parte de la transacción se ha asignado.
* **Nota**: Útil para comprender cómo se distribuyen los fondos entre las cuentas.

#### ledger\_account

* **Significado**: El número de cuenta del libro mayor en el que se registra la transacción.
* **Función**: Campo descriptivo.
* **Contenido típico**: Texto que representa un número de cuenta, como "2200" o "2500".
* **Nota**: Fundamental a efectos contables para hacer un seguimiento de dónde se contabilizan las transacciones.

#### doc\_id

* **Significado**: Un identificador de un documento o registro relacionado.
* **Función**: Clave externa o referencia.
* **Contenido típico**: Una cadena UUID u otro identificador que enlaza con documentos relacionados.
* **Nota**: Ayuda a asociar las transacciones con documentos o registros específicos para garantizar la trazabilidad.

Esta documentación ofrece una descripción detallada de la tabla `public.auto_accounting`, con su estructura y la finalidad de cada columna, para ayudar a desarrolladores y administradores de bases de datos a comprender y utilizar los datos de forma eficaz.
