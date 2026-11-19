# Configuración de LN

Esta guía combina ejemplos históricos de Infor ION con el formulario actual de exportación a LN de DocBits. Las imágenes de Infor ilustran los pasos individuales; los nombres de sus entornos, de sus mapeos y su disposición son ejemplos. Antes de activar un flujo, verifica los puntos de conexión, el paquete de mapeo y los permisos de BOD con tu administrador de Infor para tu empresa LN. Para esta actualización de la documentación no se probó ninguna conexión a un entorno de Infor ni ninguna exportación de facturas.

## Requisitos previos

Has creado:

* Un punto de conexión de ION API
* Un archivo de ION API
* Un archivo de mapeo BOD
* Un archivo de mapeo IDM

## Importar archivos de mapeo

Antes de configurar el flujo de datos, importa los archivos de mapeo en InforOS

En ION Desk → Connect, abre Mappings

<figure><img src="https://lh7-us.googleusercontent.com/fAUUcBUSxIWqLjYEHH78O2Mfq0P4d4D42OgCNFPdpUQTM5ZHu_BcKz9DmWe0AlHe3--ff7z9mfYTrt7oAkf2uknBwkV2VWayEpiJ_aAIxcJil5LNiep4U6KZr3_tBfs1RRwXoW749q3FUxurXy_pT_k" alt="Ejemplo histórico: navegación de ION Desk con el grupo Connect desplegado y las entradas Data Flows, API Flows, Connection Points, File Templates y Enterprise Locations."><figcaption><p>Ejemplo histórico: navegación de ION Desk con el grupo Connect desplegado y las entradas Data Flows, API Flows, Connection Points, File Templates y Enterprise Locations. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

Haz clic en el icono de importación

<figure><img src="https://lh7-us.googleusercontent.com/d_KYA9LgiiW1A95CH9hwU1AC1u5x25T4ET-4sAqpZkVOexHc4WcbwPXUaKt3O9fR3Btvv-NEGbCWwnnb8SfomnnO22M8YTIqWdvan-SkbG0cu1MWkjwOn_Vd_b6rJaQng8A92JTa5YKBms4RuIvwmb0" alt="Ejemplo histórico: barra de herramientas de la página Mappings en ION Desk con el control de importación marcado."><figcaption><p>Ejemplo histórico: barra de herramientas de la página Mappings en ION Desk con el control de importación marcado. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

* Aquí debes seleccionar los distintos archivos de mapeo que necesitas, entre ellos: SyncCaptDoc\_SyncSuppInv, SyncSupplierInvoice\_LoadSupplierInvoice y LoadSupplierInvoice\_ProcessSupplierInvoice.
* Cuando hayas importado todos los archivos de mapeo, aprueba cada uno de ellos haciendo clic en el icono de marca dentro de su cuadro en el panel de mapeos.

## De DocBits a LN

El siguiente paso es configurar el flujo de datos en ION Desk. Abre la aplicación ION Desk y selecciona Data Flow → + ADD → Document Flow, como se muestra a continuación

<figure><img src="https://lh7-us.googleusercontent.com/rjPVR1EFKw_gZI1Ztg9Aqt4pFw10rii7WU-yddLIz22a_Fn3s1HSYDRmQVvgZtX_85nb2ipNqJ1JU49NIE8a57TIur7jqoMuKFKlb-RrfnRFxiA1TefzofKPJ32fzIdDWI8PmnD-aDw4qhQj4e0dd9I" alt="Ejemplo histórico: página Data Flows de ION Desk con la navegación a la izquierda, el flujo DF_SLTStAPI en la lista y las entradas de menú Document Flow y Data Lake Flow."><figcaption><p>Ejemplo histórico: página Data Flows de ION Desk con la navegación a la izquierda, el flujo DF_SLTStAPI en la lista y las entradas de menú Document Flow y Data Lake Flow. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

Usa este lienzo para construir el flujo de información de DocBits a LN.

<figure><img src="https://lh7-us.googleusercontent.com/9C7BaoiHWRaav0ytCbYkxEYG12f-64qyagsl8H2eq5TXUySRE1s3x_-lVRbK6tpTxvbRYKvwyWO_6ASSQ6Rn62LQR9ZvMRpRXq9UymZLS0I8IZ-hOzX58iYtTruqSo5WdgIXwEPjMlb1dnuFuhN8IS8" alt="Ejemplo histórico: Document Flow nuevo con el panel de propiedades vacío y los mensajes Document flow name must be specified y The document flow has no activities."><figcaption><p>Ejemplo histórico: Document Flow nuevo con el panel de propiedades vacío y los mensajes Document flow name must be specified y The document flow has no activities. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

Un flujo de datos de LN se parecerá a lo que se muestra a continuación (hay varias rutas porque cada ruta individual está pensada para un tipo de documento concreto; en esta explicación nos centramos en el flujo de datos de la factura).

<figure><img src="https://lh7-us.googleusercontent.com/gltDE9JxeGb7Ufg9Ldl-JIJ95zfWHnQtyOqys2QKCiTlIn_PdAyBLFYmTVCh9c-TxF5xNQR3G8Hmn4EXK94t6MJ-1WzlZg1Zl7HNoxfR56zC8dT1skmxLTj7rtnSl0JTQJD_3myQY4Qcd9motySYh9U" alt="Ejemplo histórico: lienzo de flujo de datos con varias rutas para distintos tipos de documento; cada ruta se compone de un punto de conexión DocBits, un mapeo y un punto de conexión LN."><figcaption><p>Ejemplo histórico: lienzo de flujo de datos con varias rutas para distintos tipos de documento; cada ruta se compone de un punto de conexión DocBits, un mapeo y un punto de conexión LN. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

Todas las partes de la cadena se arrastran y sueltan desde la sección superior

En la cadena, DocBits y LN son aplicaciones, mientras que entre ellas hay mapeos que convierten los datos a un formato que la siguiente sección del flujo de datos puede entender y “asignan” la información para que llegue adonde se necesita.

<figure><img src="https://lh7-us.googleusercontent.com/Gwk0C0gsnMSlgEwRx0_1GDMJEu8Z1TAhKo8gxHN8GxFFKGgb257a684Hj0eNSLTIK5v8F7yzJ1hIHrC_3I9RLY0S-u3ZDhmkD6iJbYAvtCAeFPWHBVLOqyCH7FKsl2SKAfXL-AdtNowqdol9PzS4qJM" alt="Ejemplo histórico de la paleta de actividades de ION y del flujo: las actividades de aplicación representan DocBits y LN, con actividades de mapeo entre ellas."><figcaption><p>Ejemplo histórico de la paleta de actividades de ION y del flujo: las actividades de aplicación representan DocBits y LN, con actividades de mapeo entre ellas. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

### Aplicación DocBits

Dale un nombre apropiado, como “DocBits”; después selecciona el signo más, busca el punto de conexión que creaste antes (por ejemplo, DocBits\_Export o similar) y haz clic en él.

Para crear este punto de conexión, ve a ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/1SZJN-GW7BP-fvUHZ-tCJ4xNXx0ABRP3J9eMzF3BTKIY54J-pK4bYy4fOVHCaI6A2sdrYekWJsY9ky8dXz36l_FwwzzEnO1IjxNkMqlV-Y4UvyFIei73Z9C19m9bzTr3gCL3IpTUqiV280id1vJE530" alt="Ejemplo histórico: navegación de ION Desk con el grupo Connect desplegado y las entradas Data Flows, API Flows, Mappings y Connection Points."><figcaption><p>Ejemplo histórico: navegación de ION Desk con el grupo Connect desplegado y las entradas Data Flows, API Flows, Mappings y Connection Points. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

Haz clic en “+ Add”

<figure><img src="https://lh7-us.googleusercontent.com/ZJ1212Gwdk-b2-LVbEd2ZDzc_AqaEEYtIN0fC6d6P4EaWdTKj6nOzGDbA5sxdBtMcTrWopfDmd7GTahbwkDpj3uvmMYgvEUQa6qmi58NFGvtcgAtIwYr952Yu7Lcj802iHtQ_vj_-XPdegP1P0ySdos" alt="Ejemplo histórico: página Connection Points de ION Desk con el grupo Connect abierto en la navegación."><figcaption><p>Ejemplo histórico: página Connection Points de ION Desk con el grupo Connect abierto en la navegación. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

Selecciona “IMS via API Gateway” y completa la siguiente información

<figure><img src="https://lh7-us.googleusercontent.com/H4YCH-324EzrxKkrbRs0SFTsHch5eK74gXleSpfI03uJ5frIEFjwofu7p6bsYO1lS7sVqamWDZMXrGfEgewdROyhTYLkn7MuCgwb7oQxOLJoH3NsnMsqTOgT3WxlihUkJdNy-WTai5kPz8ZjdtTDQ9I" alt="Punto de conexión histórico IMS via API Gateway con el nombre DocBits-Sandbox-Export, el tipo de ID lógico ims y el campo ION API Client Id oculto."><figcaption><p>Punto de conexión histórico IMS via API Gateway con el nombre DocBits-Sandbox-Export, el tipo de ID lógico ims y el campo ION API Client Id oculto. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

El ID de cliente de ION API es el valor `ci` de tu archivo `.ionapi`. Solicita el archivo específico de tu entorno a tu administrador autorizado de Infor. Contiene credenciales: mantenlo fuera de capturas de pantalla, tickets y Git. Consulta la [explicación de Infor sobre los campos de credenciales de ION API](https://docs.infor.com/crm/9.4.x/en-us/webclient/upi1639111995644.html).

Cambia a la pestaña de documentos y añade el BOD Sync.CaptureDocument al punto de conexión DocBits, como se muestra a continuación.

<figure><img src="https://lh7-us.googleusercontent.com/Wy2BIr1z_RqU-yMkXo6vOu64QC6c66OdHOxdI6PPy0yJv1jIAJF0OYITULxTFoPUK93SK3jvNm67tcxqjiEBIk0Wbu1Q1s-mSIUuPjJorcYyXY7vjsHOnoutn6tE8r6yE_333uCWuKvKiVoo99FrXVg" alt="Ejemplo histórico: punto de conexión DocBits-Sandbox-Export con la pestaña Documents abierta y el documento Sync.CaptureDocument asignado."><figcaption><p>Ejemplo histórico: punto de conexión DocBits-Sandbox-Export con la pestaña Documents abierta y el documento Sync.CaptureDocument asignado. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

Después guarda el punto de conexión pulsando el icono de disco de la esquina superior izquierda.

Vuelve a la sección Dataflow de ION Desk para acceder a tu flujo de datos. Tu aplicación DocBits debería parecerse a lo que se muestra a continuación.

<figure><img src="https://lh7-us.googleusercontent.com/cDWHmRP85YNLu7JRzq4CSezncTgP2ZOkEfZSqXK9JEq4bSwsddU7VKg8leoxaJ5zeFAbDzXrNkztmeWDIXbHwjxfUa_IpATDDwykv-OlZ2zaOVGHVqRZZpVLJ5Cq5Qla1pZk5sBV39I98lUfGao65Mw" alt="Propiedades históricas de la actividad de aplicación con el nombre DocBits-Sandbox y su punto de conexión seleccionado DocBits-Sandbox-Export."><figcaption><p>Propiedades históricas de la actividad de aplicación con el nombre DocBits-Sandbox y su punto de conexión seleccionado DocBits-Sandbox-Export. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

### Mapeo 1

El primer nodo de mapeo debería verse así

<figure><img src="https://lh7-us.googleusercontent.com/9tlIun_ipbTp15aMX3xN2DGlDjAZ1oI4AFWXwbP7yoFLeQNqcw_L3Z1djaqcbxP1tsp1R-nq6ZJqEzsoKe1-SmLrJNmYrJ4HJircLEwMxfmif-p2T8nqbuuxHLLLzQJ6E6tNG6MzghOpoEAt41ea2GY" alt="Propiedades históricas del primer mapeo: Capture2sync con el mapeo de ejemplo LN_CaptureDocumentToSupplierInvoice_1."><figcaption><p>Propiedades históricas del primer mapeo: Capture2sync con el mapeo de ejemplo LN_CaptureDocumentToSupplierInvoice_1. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

### Mapeo 2

El segundo nodo de mapeo debería verse así

<figure><img src="https://lh7-us.googleusercontent.com/ZDYzTAfm3MHnEIKHa2tDl7NPbjzxv8jH-KL8O0pRhi1JYtqiiVz0-GQv5N4roVWi1STopQkFV9YHbEXdyzwYxK2Oq6mUv6tuqKDp-2bc-aPVgEXdEBd2hmW-6j6JRhEympyw9yUTrCDQRKlDQ41C5Ao" alt="Propiedades históricas del segundo mapeo: Load2Process con el mapeo de ejemplo LoadSupplierToProcessSupplierInvoice."><figcaption><p>Propiedades históricas del segundo mapeo: Load2Process con el mapeo de ejemplo LoadSupplierToProcessSupplierInvoice. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

### Aplicación LN

Ya debería existir un punto de conexión LN o con un nombre similar (para la empresa LN adecuada) creado en INFOR; al igual que con la aplicación DocBits, lo seleccionas haciendo clic en el signo “+” y debería verse así

<figure><img src="https://lh7-us.googleusercontent.com/mRXL11f68EtQHHjl40QmCisy7S1aUezqCzufPTZWgYHhWLK2Yw0UY82O_dgbAhBChFHHYUMBDSWWb-PEKyohJWOp5gvufat431ezpA2cIHMtry7XEDxhnNzPB68uSMkFAXhX1x4GyiH6Cxp-USxDnHE" alt="Propiedades históricas de la actividad de aplicación LN con el nombre de ejemplo LN-200 y la conexión de aplicación seleccionada IMI_0200."><figcaption><p>Propiedades históricas de la actividad de aplicación LN con el nombre de ejemplo LN-200 y la conexión de aplicación seleccionada IMI_0200. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

### BOD

<figure><img src="https://lh7-us.googleusercontent.com/de8OyDF4yMoHaXsxM9weJdm8mKDzL97kFRr00fhoHAxxKXb2BgMcMM2shyxi1S7cBwzSAUy2u8bZV4sJOVqgXt8Mcge6L2CXxbfVGiqXUwKwF6A5mgt4zfGPYltaZuLazOJYu2u7arszJE6IonMOskk" alt="Ejemplo histórico: lienzo de flujo de datos con los nodos DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder y AdvancedShip sobre la entrada End."><figcaption><p>Ejemplo histórico: lienzo de flujo de datos con los nodos DocBits-DEV, MappingDeliver, Load Supplier, PurchaseOrder, SalesOrder y AdvancedShip sobre la entrada End. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

Las siguientes configuraciones deberían verse así:

#### Primero

<figure><img src="https://lh7-us.googleusercontent.com/rj_qpiML1a2dNxj6ItiRxescymVtD6LHIAum3UPrPERAavhkt81lpjcyAFmn_lmxtqUDVTm_kiZ9f02Lqh9w-SAWmcxvGuxWITVvhv9qg04HaJXGH7VfRiO4Iv1LtDxfKYFyUWPLzCE4L3yP4hcdGnY" alt="Lista histórica de Documents del primer paso con la entrada Sync.CaptureDocument."><figcaption><p>Lista histórica de Documents del primer paso con la entrada Sync.CaptureDocument. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

#### Segundo

<figure><img src="https://lh7-us.googleusercontent.com/TCxMS-RhoJcUyBko36Lfpa8D71qk-ZSN-lME7Oq8cfPACVV0Ci7Lnv6y_MF_53U763ZA74xq6icEfgDUwYYJ9UJK0kCiLHQZpJYmc_ywjB32UGrpDnh7AjoHpI5AtWd3yZR3RsMaki1AYenpdG4X9X8" alt="Lista histórica de Documents del segundo paso con la entrada Load.SupplierInvoice."><figcaption><p>Lista histórica de Documents del segundo paso con la entrada Load.SupplierInvoice. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

#### Tercero

<figure><img src="https://lh7-us.googleusercontent.com/VPYJyfpO0RZueW46s2Y8W2H-tQFlMfIdP1Sf8qMB8BfTxefgQ5dhsaAxL36R7cdvmKR26Q_epAj9_i6CzUO6C-PHjStEynBDkjtwId4BSuH6-zJklmsr25XcNH2AY7pSwOQ_rbCCixhWcaJg2kHyyYw" alt="Lista histórica de Documents del tercer paso con la entrada Process.SupplierInvoice."><figcaption><p>Lista histórica de Documents del tercer paso con la entrada Process.SupplierInvoice. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

El último icono debe estar vacío, ya que no contiene ningún documento ni información.

Cuando tu administrador de Infor haya verificado todos los nodos, mapeos y suscripciones de documentos, usa el control de activación del flujo previsto. La captura histórica siguiente marca ese control; su antiguo nombre de flujo contiene M3 y no debe usarse como nombre ni como destino de tu configuración de LN.

<figure><img src="https://lh7-us.googleusercontent.com/WjQeGz_effl_RlkWC4CdJS9Dg_9DpsIz3meKOsa7GbU9RFSrYMw3PpbXFat6cGsA4gvEGS-0D-YFrZj9K2wK3Irap-30mcQ5kr5k4Gy2gm7DLJdYpzJgeBRVInyAYfGmGXu2dCQvmX9ballRbSwyq3o" alt="Barra de herramientas histórica del Document Flow con el control de activación marcado en verde. El ejemplo antiguo se llama DocBits-Export-M3; elige el flujo LN correcto en tu entorno."><figcaption><p>Barra de herramientas histórica del Document Flow con el control de activación marcado en verde. El ejemplo antiguo se llama DocBits-Export-M3; elige el flujo LN correcto en tu entorno. Confirma la configuración correspondiente en tu entorno de Infor.</p></figcaption></figure>

## Configurar la exportación en DocBits

Abre **Ajustes → Exportar** en la organización de DocBits prevista. La lista muestra las configuraciones de exportación existentes; mientras no haya ninguna, aparece el aviso **Sin configuraciones**. Selecciona **Nuevo** para preparar una nueva configuración.

<figure><img src="../../../.gitbook/assets/dbdc-1109-export-list-es-20261112.png" alt="Lista de exportación actual de DocBits en español, vacía, con el botón Nuevo y los encabezados Tipo, Suborganizaciones, Título, Método De Exportación y Acciones."><figcaption><p>Nuevo abre un formulario de configuración. En esta organización de ejemplo todavía no hay ninguna configuración guardada y no se abrió ni se modificó ninguna.</p></figcaption></figure>

En **Información básica**, introduce un **Título de configuración**, selecciona el **Tipo de Documento** (una factura en el ejemplo) y elige una **Suborganización** solo si tu configuración la requiere. En **Exportar**, elige **Infor** y, en **Tipo de información**, elige **Infor IDM + LN**.

Aporta los tres archivos necesarios para una nueva configuración de LN: el **Archivo API de ION** (`.ionapi`), el **Archivo de asignación de IDM** (`.properties`) y el **Archivo de mapeo LN** (`.properties`). Solicita los archivos de este entorno y de esta empresa LN al administrador autorizado de Infor. La captura deja deliberadamente todas las cargas vacías y no contiene credenciales.

<figure><img src="../../../.gitbook/assets/dbdc-1109-export-ln-es-20261112.png" alt="Formulario actual de DocBits en español para una exportación a Infor LN: Exportar ajustado a Infor y Tipo de información ajustado a Infor IDM + LN; el título, el tipo de documento, la suborganización y los tres campos de archivo están vacíos."><figcaption><p>El formulario actual separa los tres campos de carga. Información básica identifica el destino y el tipo de documento; en este ejemplo no se eligieron tipo de documento ni archivos, y el formulario no se guardó. La captura se tomó en una organización de ejemplo con datos inventados.</p></figcaption></figure>

Cuando tu administrador haya confirmado el flujo de ION y los archivos, selecciona **Guardar** y prueba una factura autorizada que no sea de producción. Comprueba el resultado en DocBits, en Infor ION y en LN. Una configuración guardada por sí sola no demuestra que LN haya recibido una factura. Si solo estás revisando los campos disponibles, **Cancelar** cierra el formulario sin guardar nada.

Para conocer la función de los puntos de conexión y de los flujos de documentos, consulta la [explicación de Infor ION](https://docs.infor.com/ln/10.8/en-us/lnesolh/lnoshybridng/wxa1699288671147.html).
