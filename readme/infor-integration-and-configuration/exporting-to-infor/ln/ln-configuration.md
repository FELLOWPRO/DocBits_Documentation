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

![Sección Connect de ION Desk que muestra la página Mappings con los archivos de asignación listados](https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu\_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ\_aAIxcJil5LNiep4U6KZr3\_tBfs1RRwXoW749q3FUxurXy\_pT\_k)

Click on the Import icon

![Barra de herramientas de la página Mappings en ION Desk con el icono de importación resaltado](https://lh7-us.googleusercontent.com/d\_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn\_Vd\_b6rJaQng8A92JTa5YKBms4RuIvwmb0)

* Desde aquí, deberá seleccionar los diversos archivos de mapeo que necesitará, que incluyen: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice, and LoadSupplierInvoice\_ProcessSupplierInvoice.
* Una vez que haya importado todos los archivos de asignaciones, asegúrese de aprobar cada uno de ellos haciendo clic en el ícono de marca dentro de cada uno de sus cuadrados en el panel de asignaciones.

## De DocBits a LN

El siguiente paso es configurar el flujo de datos en ION Desk, navegar hasta la aplicación ION Desk y seleccionar Flujo de datos → + ADD → Flujo de documentos como se muestra a continuación.

![Menú de ION Desk con Data Flow seleccionado, el botón + ADD y la opción Document Flow](https://lh7-us.googleusercontent.com/rjPVR1EFKw\_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a\_Fn3s1HSYDRmQVvgZtX\_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I)

Luego verá esta página, aquí es donde creará el flujo de información desde DocBits hasta M3

![Página vacía del creador de documentos Data Flow en ION Desk donde se construye el flujo desde DocBits](https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x\_-lVRbK6tpTxvbRYKvwyWO\_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8)

Un flujo de datos LN será similar al que se muestra a continuación (hay múltiples rutas debido a que cada ruta individual está destinada a un tipo de documento específico; para esta explicación nos centraremos en el flujo de datos de la factura).

![Diagrama de flujo de datos de LN en ION Desk con varias rutas desde DocBits a través de asignaciones hasta LN](https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn\_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD\_3myQY4Qcd9motySYh9U)

Todas las partes de la cadena se arrastran y sueltan desde la sección superior.

En la cadena, DocBits y LN son aplicaciones, mientras que entre ellas hay asignaciones que convierten los datos en un formato que pueda ser entendido por la siguiente sección del flujo de datos y “map” la información para que vaya a donde se necesita o también se desea.

![Lienzo vacío de flujo de datos en ION Desk con la paleta de componentes para Application, Database, Network y File encima](https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0\_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC\_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM)

### Aplicación DocBits

Asígnele el nombre apropiado, como “DocBits”, luego seleccione el signo más y busque el punto de conexión que creó anteriormente, como DocBits\_Export o similar y haga clic en él.

Para crear este punto de conexión, vaya a ION Desk → Conectar → Puntos de conexión

![Sección Connect de ION Desk que muestra la página Connection Points con la lista de puntos de conexión](https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l\_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530)

Click “+ Add”

![Página Connection Points en ION Desk con el botón + Add resaltado en la barra de herramientas](https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc\_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ\_vj\_-XPdegP1P0ySdos)

Seleccione “IMS via API Gateway” y complete la siguiente información

![Configuración del punto de conexión con IMS via API Gateway seleccionado y los campos de ION API rellenados](https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I)

El cliente ION API ID está en el archivo ION API que creó en Cómo crear un archivo ION API bajo el valor “ci”.

Cambie a la pestaña del documento y agregue Sync.CaptureDocument BOD al punto de conexión DocBits como se muestra a continuación.

![Pestaña Documents del punto de conexión con el BOD Sync.CaptureDocument añadido al punto de conexión de DocBits](https://lh7-us.googleusercontent.com/Wy2BIr1z\_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE\_333uCWuKvKiVoo99FrXVg)

Luego guarde el punto de conexión presionando el ícono del disco en la esquina superior izquierda.

Vuelva a la sección Flujo de datos de ION Desk para acceder a su flujo de datos. Su aplicación DocBits debería verse similar a lo que se muestra a continuación.

![Flujo de datos en ION Desk que muestra el nodo de la aplicación DocBits con su punto de conexión](https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa\_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw)

### Asignación 1

El primer nodo de mapeo debería tener el siguiente aspecto

![Panel Mapping Properties en ION Desk con la asignación SyncCaptDoc_SyncSuppInv seleccionada para el primer nodo de asignación](https://lh7-us.googleusercontent.com/9tlIun\_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw\_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY)

### Asignación 2

El segundo nodo de mapeo debería tener el siguiente aspecto

![Panel Mapping Properties en ION Desk para el segundo nodo de mapeo entre los BOD de facturas de proveedor](https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao)

### Aplicación LN

Ya debería haber un punto de conexión LN o un punto de conexión con un nombre similar (para la empresa LN apropiada) creado en INFOR, así que, al igual que la aplicación DocBits, selecciónela haciendo clic en el signo “+” y debería verse de la siguiente manera

![Panel Application Activity Properties en ION Desk con el nombre LN-200 y la empresa LN ln01_0200](https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O\_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE)

### BODs

![Flujo de datos que muestra los documentos BOD transportados entre los nodos de aplicación DocBits y LN](https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk)

Las siguientes configuraciones deberían verse así:

#### Primero

![Configuración de flujo de datos en ION Desk con el documento Sync.CaptureDocument seleccionado en el nodo de aplicación](https://lh7-us.googleusercontent.com/rj\_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn\_lmxtqUDVTm\_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY)

#### Segundo

![Configuración del flujo de datos en ION Desk con el documento Load.SupplierInvoice seleccionado en el nodo LN](https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y\_MF\_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc\_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8)

#### Tercero

![Configuración de flujo de datos en ION Desk con el documento Process.SupplierInvoice seleccionado en el nodo final](https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q\_epAj9\_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ\_rbCCixhWcaJg2kHyyYw)

El último icono debe estar vacío ya que no contiene ningún documento o información.

Una vez que haya agregado todos los nodos necesarios al flujo de datos, presione este botón para activar el flujo de datos.

![Barra de herramientas del flujo de datos en ION Desk para el flujo DocBits-Export-M3 con el botón REMOVE CONNECTION POINTS](https://lh7-us.googleusercontent.com/WjQeGz\_effl\_RlkWC4CdJS9Dg\_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o)
