# Configuración de LN

## Requisitos previos

Has creado:

* An ION API Endpoint
* An ION API File
* Un archivo de mapeo BOD
* Un archivo de mapeo IDM

## Importar archivos de asignación

Antes de configurar el flujo de datos, debe importar los archivos de mapeo a InforOS

En ION Desk → Conectar y abrir Mappings

![Navegación de ION Desk con el grupo Connect desplegado y las entradas Data Flows, API Flows, Connection Points, File Templates y Enterprise Locations](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu\_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ\_aAIxcJil5LNiep4U6KZr3\_tBfs1RRwXoW749q3FUxurXy\_pT\_k)

Click on the Import icon

![Barra de herramientas de la página Mappings en ION Desk con el icono redondo verde de importación](https://lh7-us.googleusercontent.com/d\_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn\_Vd\_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* Desde aquí, deberá seleccionar los diversos archivos de mapeo que necesitará, que incluyen: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.
* Una vez que haya importado todos los archivos de asignaciones, asegúrese de aprobar cada uno de ellos haciendo clic en el ícono de marca dentro de cada uno de sus cuadrados en el panel de asignaciones.

## De DocBits a LN

El siguiente paso es configurar el flujo de datos en ION Desk, navegar hasta la aplicación ION Desk y seleccionar Flujo de datos → + ADD → Flujo de documentos como se muestra a continuación.

![Página Data Flows en ION Desk con la navegación a la izquierda, el flujo DF_SLTStAPI en la lista y las entradas de menú Document Flow y Data Lake Flow](https://lh7-us.googleusercontent.com/rjPVR1EFKw\_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a\_Fn3s1HSYDRmQVvgZtX\_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Luego verá esta página, aquí es donde creará el flujo de información desde DocBits hasta M3

![Nuevo Document Flow con el panel de propiedades vacío y los mensajes Document flow name must be specified y The document flow has no activities](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x\_-lVRbK6tpTxvbRYKvwyWO\_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

Un flujo de datos LN será similar al que se muestra a continuación (hay múltiples rutas debido a que cada ruta individual está destinada a un tipo de documento específico; para esta explicación nos centraremos en el flujo de datos de la factura).

![Lienzo del flujo de datos con varios recorridos para distintos tipos de documento, cada recorrido formado por un punto de conexión DocBits, un mapeo y un punto de conexión LN](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn\_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD\_3myQY4Qcd9motySYh9U)

Todas las partes de la cadena se arrastran y sueltan desde la sección superior.

En la cadena, DocBits y LN son aplicaciones, mientras que entre ellas hay asignaciones que convierten los datos en un formato que pueda ser entendido por la siguiente sección del flujo de datos y “map” la información para que vaya a donde se necesita o también se desea.

![Detalle del lienzo del flujo de datos con los nodos DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder y los puntos de conexión LN-200-41 y LN-200-4](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0\_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC\_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### Aplicación DocBits

Asígnele el nombre apropiado, como “DocBits”, luego seleccione el signo más y busque el punto de conexión que creó anteriormente, como DocBits\_Export o similar y haga clic en él.

Para crear este punto de conexión, vaya a ION Desk → Conectar → Puntos de conexión

![Navegación de ION Desk con el grupo Connect desplegado y las entradas Data Flows, API Flows, Mappings y Connection Points](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l\_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Click “+ Add”

![Página Connection Points en ION Desk con el grupo Connect abierto en la navegación](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc\_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ\_vj\_-XPdegP1P0ySdos)

Seleccione “IMS via API Gateway” y complete la siguiente información

![Diálogo Infor Application Connection Point para IMS via API Gateway con el nombre DocBits-Sandbox-Export, el ION API Client Id y el Logical ID infor.ims.docbits-sandbox-export](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

El cliente ION API ID está en el archivo ION API que creó en Cómo crear un archivo ION API bajo el valor “ci”.

Cambie a la pestaña del documento y agregue Sync.CaptureDocument BOD al punto de conexión DocBits como se muestra a continuación.

![Punto de conexión DocBits-Sandbox-Export con la pestaña Documents abierta y el documento Sync.CaptureDocument asignado](https://lh7-us.googleusercontent.com/Wy2BIr1z\_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE\_333uCWuKvKiVoo99FrXVg)

Luego guarde el punto de conexión presionando el ícono del disco en la esquina superior izquierda.

Vuelva a la sección Flujo de datos de ION Desk para acceder a su flujo de datos. Su aplicación DocBits debería verse similar a lo que se muestra a continuación.

![Panel Application Activity Properties de la aplicación DocBits con el nombre DocBits-Sandbox-Export y la descripción DocBits-Sandbox-Export](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa\_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)

### Asignación 1

El primer nodo de mapeo debería tener el siguiente aspecto

![Panel Mapping Properties del primer nodo de mapeo con los campos Name y Description y la lista desplegable Mapping](https://lh7-us.googleusercontent.com/9tlIun\_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw\_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Asignación 2

El segundo nodo de mapeo debería tener el siguiente aspecto

![Panel Mapping Properties del segundo nodo de mapeo con los campos Name y Description y la lista desplegable Mapping](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### Aplicación LN

Ya debería haber un punto de conexión LN o un punto de conexión con un nombre similar (para la empresa LN apropiada) creado en INFOR, así que, al igual que la aplicación DocBits, selecciónela haciendo clic en el signo “+” y debería verse de la siguiente manera

![Panel Application Activity Properties de la aplicación LN con el nombre LN-200 y la descripción In01_0200 LN Farm](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O\_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![Lienzo del flujo de datos con los nodos DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder y AdvancedShip sobre la entrada End](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

Las siguientes configuraciones deberían verse así:

#### Primero

![Lista desplegable Documents del primer nodo con la entrada Sync.CaptureDocument](https://lh7-us.googleusercontent.com/rj\_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn\_lmxtqUDVTm\_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Segundo

![Lista desplegable Documents del segundo nodo con la entrada Load.SupplierInvoice](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y\_MF\_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc\_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Tercero

![Lista desplegable Documents del tercer nodo con la entrada Process.SupplierInvoice](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q\_epAj9\_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ\_rbCCixhWcaJg2kHyyYw)

El último icono debe estar vacío ya que no contiene ningún documento o información.

Una vez que haya agregado todos los nodos necesarios al flujo de datos, presione este botón para activar el flujo de datos.

![Barra de herramientas del Document Flow con los botones para añadir y quitar puntos de conexión y el botón para activar el flujo de datos, bajo el nombre DocBits-Export-M3](https://lh7-us.googleusercontent.com/WjQeGz\_effl\_RlkWC4CdJS9Dg\_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
