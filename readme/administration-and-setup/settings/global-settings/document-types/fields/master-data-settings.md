# Ajustes de datos maestros

## Descripción general

En la sección de **Ajustes de datos maestros** de los **Campos** para un **Tipo de Documento** específico, puedes ver y configurar asignaciones de datos maestros a campos utilizados en la validación de campos, usando datos de [**Búsqueda de datos maestro**](../../../document-processing/master-data-lookup.md).

Estas asignaciones definen cómo se aplican los datos maestros a campos individuales durante la validación. Esta página proporciona una guía detallada sobre cómo configurar y gestionar estas asignaciones.

## **Accediendo a** Ajustes de datos maestros **Ajustes**

Para acceder a los ajustes de **Ajustes de datos maestros**:

1.  Ve a **Ajustes → Ajustes globales → Tipos de documentos**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types.png)
2.  Selecciona el **Tipo de Documento** deseado y haz clic en **Campos**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_document_types_fields.png)
3.  Haz clic en **Ajustes de datos maestros**

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_1.png)

## Búsqueda de datos maestros

En la sección de **Búsqueda de datos maestros**, puedes crear configuraciones de búsqueda a partir de tus datos maestros para utilizarlas como asignaciones de campos durante la validación de campos.

### Entradas predeterminadas

En la sección **Búsqueda de datos maestros**, ciertas entradas predeterminadas son proporcionadas por **DocBits**. Estas entradas:

* No se pueden editar ni borrar
* Se pueden desactivar si no se necesitan

Las entradas predeterminadas están claramente marcadas con una **Default tag** para facilitar su identificación.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_2.png)

### **Crear configuración de búsqueda**

Para crear una nueva configuración de búsqueda para Datos maestros:

1. Navega a la sección **Búsqueda de datos maestros**.
2.  Haz clic en **Crear configuración de búsqueda** en la esquina superior derecha.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_3.png)
3. Configura las siguientes opciones:
   * **Nombre de búsqueda**\
     El nombre de la configuración de búsqueda.
   * **Nombre del conjunto de datos**\
     Selecciona el conjunto de datos que debe usarse para esta configuración de búsqueda.
   * **Gestor de conflictos**\
     Un conflicto significa que la búsqueda encontró más de un registro. Este ajuste decide qué ocurre entonces:
     * **Best Score** – Usa la entrada que coincide con más campos. Nunca deja el campo vacío, por lo que puede elegir el registro equivocado.
     * **Return None** – Deja el campo vacío, para que un usuario elija el registro correcto.
     * **Return First** – Usa el primer valor coincidente.
   *   **Tipo de contexto**

       Especifica dónde en el documento se aplicará la configuración de búsqueda. Elige entre:

       **HEADER**

       La búsqueda se utiliza en la validación de campos. Configura lo siguiente:

       * **Coincidir con todo**\
         Cuando está habilitado, un registro debe coincidir con **todos** los campos usados. Cuando está deshabilitado (predeterminado), basta con que coincida **un** campo, lo que devuelve una lista más larga.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_4.png)

       \
       **LINE**

       La búsqueda se utiliza dentro de una tabla del documento. Configura lo siguiente:

       * **Detalle del contexto**\
         Selecciona la tabla específica a la que se debe aplicar la búsqueda.
       * **Coincidir con todo**\
         Cuando está habilitado, un registro debe coincidir con **todos** los campos usados. Cuando está deshabilitado (predeterminado), basta con que coincida **un** campo, lo que devuelve una lista más larga.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_5.png)
{% hint style="info" %}
**Coincidir con todo** y el **Gestor de conflictos** funcionan juntos y deciden si un proveedor se reconoce automáticamente. La página de configuración explica ambos con ejemplos:

{% content-ref url="../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md" %}
[fuzzy-data-configuration-with-master-data](../../../../setup/document-types/fuzzy-data-configuration-with-master-data.md)
{% endcontent-ref %}
{% endhint %}

4.  Haz clic en **Guardar** para crear la configuración de búsqueda.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_6.png)

### Acciones sobre una configuración de búsqueda existente

Para gestionar una configuración de búsqueda existente, haz clic en los tres puntos en la esquina superior derecha de la configuración que quieras modificar.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_7.png)

Están disponibles las siguientes acciones:

* **Activar / Desactivar**\
  Alterna el estado de la configuración de búsqueda.
  * Las configuraciones activas están marcadas con una etiqueta **Activo**.
  * Las configuraciones inactivas están marcadas con una etiqueta **Inactivo**.
*   **Duplicar**\
    Después de introducir un nombre y hacer clic en **Hecho**, se crea una copia de la configuración de búsqueda seleccionada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_8.png)
* **Editar/Vista**\
  Te permite modificar la configuración de búsqueda seleccionada.\
  Después de realizar los cambios, haz clic en **Guardar** para aplicarlos.\
  <mark style="color:red;">**Nota**</mark>: Las configuraciones de búsqueda predeterminadas solo se pueden ver, no editar. La opción **Editar** se reemplazará por **Vista**.
*   **Borrar**\
    Elimina permanentemente la configuración de búsqueda seleccionada tras la confirmación.\
    <mark style="color:red;">**Nota**</mark>: Solo se pueden borrar configuraciones sin la **Default** tag.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

### Crear nuevo campo

Para añadir un nuevo campo a tu configuración de búsqueda:

1. Abre la configuración de búsqueda deseada.
2.  Haz clic en **Crear** en la esquina superior derecha.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_10.png)
3. Configura las opciones necesarias.
   * **Campo de búsqueda**\
     El campo que se buscará dentro del conjunto de datos seleccionado para la búsqueda.
   * **Campo de validación**\
     El campo que se mostrará durante la validación de campos.
   * **Campo padre** (opcional)\
     Este campo se utiliza para validar la corrección del valor en el **Campo de validación** asegurando que coincida con la entrada padre correspondiente en el conjunto de datos de búsqueda.
   * **Operador de búsqueda** (opcional)\
     Elige cómo **DocBits** busca coincidencias en el conjunto de datos:
     * **Smart** – _(Predeterminado)_ Ignora espacios y signos de puntuación y busca el término en **cualquier parte** del campo. Por eso "Meier" también encuentra "Meier Bau GmbH".
     * **Contiene** – Busca entradas que contengan el término exacto en cualquier parte del campo.
     * **termina con** – Busca entradas que terminen con el término especificado.
     * **Exacto** – Busca una coincidencia exacta de todo el valor.
     * **comienza con** – Busca entradas que comiencen con el término especificado.
   * **Disparador automático** (opcional)\
     Cuando está habilitado, DocBits completará automáticamente todos los campos en la configuración de búsqueda tan pronto como se complete este campo.
   *   **Buscable** (opcional)\
       Cuando está habilitado, los usuarios pueden buscar manualmente datos maestros durante la validación de campos **y** el campo participa en la búsqueda automática. Déjalo sin marcar si el campo no debe influir en el resultado automático.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_12.png)



       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_13.png)
4.  Haz clic en **Guardar** para crear el nuevo campo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_11.png)

### Acciones sobre un campo existente

Para gestionar un campo existente, haz clic en los tres puntos en la columna **Comportamiento** junto al campo que deseas modificar.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_14.png)

Están disponibles las siguientes acciones:

* **Editar/Vista**\
  Te permite modificar el campo seleccionado.\
  Después de realizar los cambios, haz clic en **Guardar** para aplicarlos.\
  <mark style="color:red;">**Nota**</mark>: Los campos predeterminados solo se pueden ver, no editar. En estos casos, la opción **Editar** aparecerá como **Vista**.
*   **Borrar**\
    Elimina permanentemente el campo seleccionado tras la confirmación.\
    <mark style="color:red;">**Nota**</mark>: Solo se pueden borrar campos sin la **Default** tag.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_9.png)

## Datos maestros LOV

La sección **Datos maestros LOV** te permite crear configuraciones de menús desplegables usando valores de tus datos maestros. Estos desplegables pueden ser independientes o dependientes de otros desplegables, habilitando el filtrado dinámico y selecciones en cascada durante la validación de campos.

### Crear Lov Lookup Config

Una configuración de búsqueda lov define cómo se obtienen las opciones del desplegable de una tabla de datos maestros y cómo se muestran y rellenan esos valores en los campos del documento.

**Para crear un nuevo Lov Lookup Config:**

1. Navega a la sección **Datos maestros LOV**.
2.  Haz clic en **Crear Lov Lookup Config** en la esquina superior derecha.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_15.png)
3. Configura las siguientes opciones:
   * **Buscar Lov Nombre**\
     El nombre de la configuración de búsqueda lov.
   * **Lookup Lov Dataset Name**\
     Selecciona la tabla de datos maestros que debe usarse para esta configuración de búsqueda lov.
   *   **Tipo de contexto**\
       Especifica dónde en el documento se aplicará la configuración de búsqueda lov:

       **HEADER**

       La configuración de búsqueda lov se utiliza en la validación de campos. Configura lo siguiente:

       * **Campo de etiqueta de búsqueda**\
         Selecciona la columna cuyo valor se mostrará en el desplegable.
       * **Campo de valor de búsqueda**\
         Selecciona la columna cuyo valor se almacenará internamente y se utilizará para el filtrado cuando se realice una selección. Este valor no se muestra al usuario.
       * **Campo exterior**\
         Define el campo en la validación de campos que recibirá la etiqueta seleccionada del desplegable.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_16.png)

       \
       **LINE**

       La configuración de búsqueda lov se utiliza dentro de una tabla del documento. Configura lo siguiente:

       * **Detalle del contexto**\
         Selecciona la tabla específica donde esta configuración de búsqueda lov debe estar activa.
       * **Campo de etiqueta de búsqueda**\
         La columna cuyo valor se mostrará en el desplegable.
       * **Campo de valor de búsqueda**\
         Selecciona la columna cuyo valor se almacenará internamente y se utilizará para el filtrado cuando se realice una selección. Este valor no se muestra al usuario.
       * **Campo exterior**\
         Especifica el campo de destino en la tabla donde se rellenará la etiqueta seleccionada.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_17.png)
4.  Haz clic en **Guardar** para crear la configuración de búsqueda lov.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_18.png)

### Acciones sobre una configuración de búsqueda existente

Para gestionar una configuración de búsqueda lov existente, haz clic en los tres puntos en la esquina superior derecha de la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_19.png)

**Acciones disponibles:**

* **Activar / Desactivar**\
  Alterna el estado de la configuración de búsqueda lov.
  * Las configuraciones **Activo** están marcadas con una etiqueta **Activo**.
  * Las configuraciones **Inactivo** están marcadas con una etiqueta **Inactivo**.
*   **Duplicar**\
    Después de introducir un nombre y hacer clic en **Hecho**, se crea una copia de la configuración de búsqueda lov seleccionada.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_21.png)
* **Editar / Vista**\
  Modifica la configuración seleccionada. Después de realizar cambios, haz clic en **Guardar**.
*   **Borrar**\
    Elimina permanentemente la configuración tras la confirmación.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)

### Crear nuevo campo

Dentro de cada configuración de búsqueda lov, puedes definir campos adicionales como desplegables que actúan como prefiltros para la lógica principal de lov.

Estos campos se evalúan antes de que se cargue el desplegable principal de lov. En función de los valores seleccionados en estos campos, los resultados del campo lov principal se filtran dinámicamente, habilitando desplegables dependientes.\
Por ejemplo, seleccionar un país en un campo de prefiltro puede reducir las opciones de ciudad en el desplegable principal de lov.

Además de crear nuevos campos, también puedes usar campos existentes como prefiltros. Cuando se configuran de esta manera, el valor seleccionado en el campo existente filtrará automáticamente el desplegable principal de lov.

**Para añadir un nuevo campo:**

1. Abre la configuración de búsqueda lov deseada.
2.  Haz clic en **Crear** en la esquina superior derecha.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_22.png)
3.  Configura las opciones necesarias.

    **Opciones de configuración de campo (aplican a los contextos HEADER y LINE):**

    * **Campo de búsqueda**\
      La columna que se buscará en el conjunto de datos seleccionado para los valores del desplegable.
      * **Campo de filtro**\
        Especifica el campo cuyo valor se utiliza para prefiltar los resultados de la configuración de búsqueda lov antes de que se cargue el desplegable principal.
      * **Valor del filtro** (opcional)\
        Añade filtros estáticos para acotar aún más los resultados de la búsqueda.
      * **Requerido**\
        Cuando está habilitado, este campo debe completarse antes de que se puedan rellenar los desplegables dependientes.
4.  Haz clic en **Guardar** para crear el nuevo campo.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_23.png)

### Acciones sobre un campo existente

Para gestionar un campo existente dentro de una configuración de búsqueda lov, haz clic en los tres puntos en la columna **Comportamiento** junto al campo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_24.png)

**Acciones disponibles:**

* **Editar**\
  Modifica el campo seleccionado. Tras los cambios, haz clic en **Guardar** para aplicar.
*   **Borrar**\
    Elimina permanentemente el campo tras la confirmación.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/fields_master_data_settings_20.png)
