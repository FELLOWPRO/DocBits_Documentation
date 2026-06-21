_Engelse inhoud hieronder - Vertaling in behandeling_

# Columnas de la Tabla

<figure><img src="../../../../.gitbook/assets/docbits_table_columns_overview.png" alt="Docbits Table Columns Overview"><figcaption></figcaption></figure>

#### Visión general

La interfaz de Columnas de la Tabla en Docbits se utiliza para especificar las columnas que aparecen en las tablas de datos para cada tipo de documento. Cada columna se puede configurar para contener tipos específicos de datos, como cadenas o valores numéricos, y puede ser esencial para las funciones de ordenación, filtrado e informes dentro de Docbits.

#### Características clave y opciones

1. **Configuración de Columnas**:
* **Nombre de la Columna**: El identificador de la columna en la base de datos.
* **Título**: El título legible por humanos de la columna que aparecerá en la interfaz.
* **Tipo de Columna**: Define el tipo de datos de la columna (por ejemplo, STRING, AMOUNT), lo que determina qué tipo de datos se pueden almacenar en la columna.
* **Nombre de la Tabla**: Indica a qué tabla pertenece la columna, vinculándola a un tipo de documento específico como INVOICE\_TABLE.
2. **Acciones**:
* **Editar**: Modificar la configuración de una columna existente.
* **Eliminar**: Eliminar la columna de la tabla, lo cual es útil si los datos ya no son necesarios o si la estructura de datos del tipo de documento cambia.
3. **Agregar Nuevas Columnas y Tablas**:
* **Agregar Nueva Columna de Tabla**: Abre un cuadro de diálogo donde puedes definir una nueva columna, incluyendo su nombre, si es requerida, su tipo de datos y la tabla a la que pertenece.
* **Crear Nueva Tabla**: Permite la creación de una nueva tabla, definiendo un nombre único que se utilizará para almacenar datos relacionados con un conjunto específico de tipos de documento.

<figure><img src="../../../../.gitbook/assets/docbits_create_new_table.png" alt="Docbits Create New Table"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/docbits_table_columns_integrity.png" alt="Docbits Table Columns Integrity"><figcaption></figcaption></figure>

Esta sección es vital para mantener la integridad estructural y la usabilidad de los datos dentro del sistema de Docbits, asegurando que los datos extraídos de los documentos se almacenen de manera organizada y accesible.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2493" %}
