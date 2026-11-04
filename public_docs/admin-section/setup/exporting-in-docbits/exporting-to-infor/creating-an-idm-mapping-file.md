# Creación de un Archivo de Mapeo de IDM

Una vez obtenido, abre el archivo en tu editor de archivos correspondiente. Para este tutorial, se utilizará VSCode.

## Editar Archivo de Mapeo

Verifica que el código del tipo de documento sea el mismo que en DocBits (por ejemplo, con el Archivo de Mapeo BOD, debe coincidir con el nombre del tipo de documento en la URL de la configuración del campo) y también verifica el nombre del tipo de documento tal como debería estar en Document Manager (IDM) en Infor.

![](https://lh7-us.googleusercontent.com/WHO0vg2W36yVFBq0ay0wBMFVzMfT6pNvHklt0o8N4tqUpM03jXJm2fykuYjyZh0z4wFTO4Eaeh39-D03re3a9utegrdVdsjHBfucmALA3B7YBWd92-9bcYr543G4MWftv0RosvTgFP3J6NNmLZAz5Dc)

**Nota**: Indica que el nombre del tipo de documento en IDM es M3\_SupplierInvoice, esto se debe a que es un ejemplo de una instancia de M3. Esto puede cambiar dependiendo de si usas LN o M3, así como de tu configuración específica de IDM.

Verifica el ID de la empresa y el ID de la entidad (SF\_MDS\_EntityType); este valor debe ser el mismo que en el Archivo de Mapeo BOD.

Asegúrate de que IndexFieldFromDocBits=IDMAttributeID (verifica si DocBits a la izquierda en la configuración del campo coincide con IDM a la derecha en Tipo de Documento → Atributos).

### Document Manager en Infor

Ve a Document Manager y selecciona el nombre del tipo de documento actual que estás intentando exportar, por ejemplo, Factura de Proveedor.

![](https://lh7-us.googleusercontent.com/EV3uw3R1L6\_RRANB7FRLwtUFMbv\_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Haz clic en el icono anterior y luego en Administración → Tipo de Documento y luego encuentra el tipo de documento que necesitas en la lista.

![](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j\_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Como se muestra a continuación, verás el nombre del tipo de documento tal como está en INFOR.

![](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj\_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW\_dpRfw\_5BXm0WvAnw4HOALmw)

Asegúrate de que así es como se muestra el nombre en el Archivo de Mapeo de IDM.

## Subir Archivo a DocBits

Una vez que el archivo esté preparado, súbelo a tu configuración de exportación en DocBits. Esto está disponible en Configuración → Exportar.

![](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F\_i5mZ42YDnjqZUYKYSJu1Cetc\_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)
