# Configuración del país fiscal predeterminado para la exportación a Infor ERP / SAP

### Descripción general

El país fiscal (Tax Country) predeterminado para la exportación es **DE (Alemania)** para evitar errores de exportación. Puede cambiarse en el archivo de asignación de una de estas maneras:

* Definiendo un valor estático diferente.
* Asignándolo dinámicamente a un campo de DocBits.

<mark style="color:red;">**Nota:**</mark> Si el campo especificado no existe o está vacío, la exportación volverá a utilizar **DE**.

### Pasos para modificar el país fiscal

#### 1. Obtener el archivo de asignación

* Navegue a **DocBits → Settings → Document Processing → Export**.
* Abra la configuración de exportación que desea modificar.
*   Haga clic en **Download** para obtener el archivo de asignación.\\

    <figure><img src="../../../../.gitbook/assets/iScreen Shoter - Google Chrome - 250220120028.jpg" alt=""><figcaption></figcaption></figure>
* Abra el archivo en un editor de texto.

#### 2. Modificar el archivo de asignación

Elija una de las dos opciones siguientes y aplique los cambios necesarios.

**Opción 1: valor estático**

Para establecer un valor estático de país fiscal, siga estos pasos:

1.  Defina un nuevo campo estático añadiendo `,TaxCountry` a la línea `StaticFields`.

    ```properties
    StaticFields=FinancialCompany...,TaxCountry
    ```
2.  Establezca el código de país añadiendo la siguiente línea:

    ```properties
    SF_TaxCountry=CountryCode
    ```

    Sustituya `CountryCode` por el código de país real, por ejemplo, `ES` para España o `DE` para Alemania:

    ```properties
    SF_TaxCountry=ES
    ```

**Ejemplo:**

```properties
StaticFields=FinancialCompany,TaxCountry
SF_TaxCountry=FR
```

<figure><img src="../../../../.gitbook/assets/image (415).png" alt=""><figcaption></figcaption></figure>

**Opción 2: asignación dinámica desde un campo de DocBits**

Para asignar dinámicamente el país fiscal desde un campo de DocBits:

1.  Añada `,TaxCountry` a la línea `HeaderFields`:

    ```properties
    HeaderFields=SupplierCode,...,TaxCountry
    ```
2.  Defina la asignación de campo correspondiente:

    ```properties
    HF_TaxCountry=DocBits_Field_name
    ```

    Sustituya `DocBits_Field_Name` por el nombre real del campo en DocBits:

    ```properties
    HF_TaxCountry=tax_country_1
    ```

**Ejemplo:**

```properties
HeaderFields=SupplierCode,TaxCountry
HF_TaxCountry=tax_country_1
```

<figure><img src="../../../../.gitbook/assets/image (411).png" alt=""><figcaption></figcaption></figure>

### Resumen

* Si el país fiscal **no está definido o el campo está vacío**, se utiliza **DE** por defecto.
* **Utilice un valor estático** si el país fiscal es el mismo para todas las exportaciones.
* **Utilice una asignación dinámica de campo** si el país fiscal varía según el documento.

Siguiendo estos pasos, podrá modificar correctamente la asignación del país fiscal para adaptarla a sus necesidades.
