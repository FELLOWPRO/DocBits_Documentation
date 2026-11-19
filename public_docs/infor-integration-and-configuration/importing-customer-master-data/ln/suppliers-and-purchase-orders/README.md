# Proveedores y órdenes de compra de Infor LN

Este ejemplo describe la ruta de Infor ION para los BOD de proveedores y de órdenes de compra y dónde verificarlos en DocBits. Las catorce capturas de Infor que aparecen a continuación son ejemplos históricos de un inquilino. Confirme con su administrador de integración los puntos de conexión, los nombres de las llamadas a la API y las opciones de publicación de LN; no se verificaron en un inquilino de Infor para esta actualización. Durante esta actualización no se publicó ni se importó ningún BOD.

Infor documenta el [publicador de datos maestros logísticos de LN](https://docs.infor.com/ln/latest/en-us/lnolh/tcolh/help/tc/bod/tcbod0200m000.html) y el [publicador transaccional de gestión de pedidos](https://docs.infor.com/ln/2025.x/en-us/lnolh/tdolh/help/td/bod/tdbod0200m000.html). Sus modos tienen efectos distintos: **Count** informa del total de registros sin publicar; **Simulate** genera un resultado de prueba sin confirmar la publicación; **Publish** envía los datos seleccionados. La publicación puede llegar a todos los suscriptores, así que compruebe el rango de empresas y los suscriptores antes de ejecutarla.

## **Punto de conexión**

Deberá crear el punto de conexión de la API de DocBits para poder crear después el flujo de datos.

En primer lugar, en InforOS, navegue a ION Desk → Connect → Connection Points

<figure><img src="https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE" alt="Navegación histórica de Infor ION Desk con el grupo Connect desplegado y Connection Points resaltado."><figcaption><p>Ejemplo de navegación histórico: ION Desk → Connect → Connection Points.</p></figcaption></figure>

Una vez allí, deberá crear un nuevo punto de conexión.

<figure><img src="https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU" alt="Pantalla histórica de Connection Points con una flecha verde que apunta a Add."><figcaption><p>Elija Add para crear un punto de conexión; la anotación verde marca la acción en esta interfaz histórica.</p></figcaption></figure>

**Seleccione API**

Asigne al punto de conexión un nombre y una descripción que indiquen su naturaleza y su entorno. En la pestaña Connection, importe la cuenta de servicio que haya creado para el entorno con el que trabaja.

<figure><img src="https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0" alt="Punto de conexión de API DocBits-DEV-Demo-Import histórico con Connection seleccionado y un control Import para la cuenta de servicio."><figcaption><p>Pestaña Connection histórica. Los nombres de cuenta de servicio y de conexión mostrados pertenecen al entorno de ejemplo.</p></figcaption></figure>

A continuación, cambie a la pestaña Documents. Deberá añadir los siguientes BOD al punto de conexión.

<figure><img src="https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg" alt="Pestaña Documents histórica en alemán con las llamadas a la API Ack-SupplierInvoice, Sync.PurchaseOrder y Sync.ReceiveDelivery y los BOD recibidos."><figcaption><p>Pestaña Dokumente (Documents) histórica. Este recorte muestra tres rutas; no muestra la configuración completa de proveedores.</p></figcaption></figure>

* Ack-SupplierInvoice

Este BOD sirve para indicar en DocBits que se ha producido un error en Infor. La ruta Acknowledge.SupplierInvoice que se muestra a continuación es un ejemplo de acuse de facturas. Confirme el nombre de su llamada a la API y si esta ruta es necesaria para su flujo de proveedores y órdenes de compra.

<figure><img src="https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y" alt="Pestaña ION API histórica en alemán para Ack-SupplierInvoice con una operación POST seleccionada."><figcaption><p>Ruta de acuse histórica. Ack-SupplierInvoice es un nombre de llamada a la API de ejemplo; Acknowledge.SupplierInvoice es el BOD recibido.</p></figcaption></figure>

* Sync.PurchaseOrder

El ejemplo histórico siguiente muestra una operación de recepción; confirme la operación actual y el formato de la solicitud para su entorno.

<figure><img src="https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0" alt="Pestaña ION API histórica con Send to API seleccionado para Sync.PurchaseOrder y una operación POST configurada."><figcaption><p>Ruta de órdenes de compra histórica. Revise la operación de recepción de su entorno de DocBits en lugar de copiar la antigua ruta del proxy.</p></figcaption></figure>

* Sync.ReceiveDelivery

El ejemplo histórico siguiente muestra una operación de recepción; confirme la operación actual y el formato de la solicitud para su entorno.

<figure><img src="https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc" alt="Pestaña ION API histórica en alemán para Sync.ReceiveDelivery con una operación POST configurada."><figcaption><p>Ruta histórica de datos de recepción. Confirme si ReceiveDelivery es necesario para su integración y qué operación lo recibe.</p></figcaption></figure>

Una vez configurados estos BOD, puede guardar el punto de conexión pulsando el icono situado a la derecha del botón de retroceso.

## **Flujo de datos**

El flujo de datos tendrá un aspecto similar al siguiente

<figure><img src="https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU" alt="Flujo de documentos histórico desde un nodo LN a través de una división paralela hacia cuatro nodos de API de DocBits, seguido de una unión y un final."><figcaption><p>Flujo histórico con cuatro entornos. La división y la unión son visibles; el número y el destino de los nodos dependen del diseño de su integración.</p></figcaption></figure>

Los múltiples nodos de API de DocBits de este ejemplo histórico representan entornos separados. Su diseño de producción puede usar un número distinto de nodos; nunca dirija datos de prueba a una organización de producción.

La siguiente ilustración utiliza cuatro entornos únicamente como ejemplo.

### **LN**

El inicio del flujo de datos lo forman sus aplicaciones de LN

### **DocBits API**

Aquí añadirá una aplicación y seleccionará las API de DocBits que creó anteriormente

### **Documentos**

Revise la lista de documentos asignada al flujo. Los mensajes de proveedor que se muestran aquí también necesitan sus correspondientes rutas de recepción en el punto de conexión de la API. Su configuración de llamadas a la API no aparece en el recorte anterior de tres rutas; confirme las operaciones necesarias con su administrador de integración.

<figure><img src="https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU" alt="Lienzo de flujo histórico con el panel alemán Dokumente debajo, que lista Sync.PurchaseOrder, Sync.ReceiveDelivery, Sync.RemitToPartyMaster y Sync.SupplierPartyMaster."><figcaption><p>Lista de documentos histórica del flujo. Aquí aparecen tanto los mensajes de proveedor como los de órdenes de compra y de recepción.</p></figcaption></figure>

## **Activación de BOD en LN**

Una vez que el administrador de integración haya comprobado el punto de conexión, las rutas de documentos y el flujo de datos activo, utilice la sesión de publicación de LN adecuada. Siga cada identificador de prueba por LN, ION y DocBits; activar un BOD por sí solo no demuestra que un registro haya llegado.

<figure><img src="https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y" alt="Página de inicio histórica en alemán de Infor LN con una lista de favoritos; el menú Publish BODs no está abierto."><figcaption><p>Página inicial histórica de LN. Utilice la navegación descrita a continuación para encontrar la sesión de publicación adecuada.</p></figcaption></figure>

### **PurchaseOrder**

En el menú anterior, en la pestaña del menú izquierdo, seleccione Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Seleccione la pestaña PurchaseOrder y marque la casilla.

<figure><img src="https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco" alt="Sesión histórica Publish Order Management Transactional Data con la pestaña PurchaseOrder y la casilla marcadas y campos de rango de pedidos visibles."><figcaption><p>Selección histórica de PurchaseOrder. Revise el rango de pedidos y los estados antes de publicar.</p></figcaption></figure>

### **Proveedores**

Desde la página de inicio de LN, en la pestaña del menú izquierdo, navegue a Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Seleccione la pestaña PartyMaster y marque la casilla Supplier → Buy-from o SupplierPartyMaster.

<figure><img src="https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0" alt="Sesión histórica Publish Logistic Master Data con PartyMaster seleccionado y la casilla Supplier Buy-from marcada."><figcaption><p>Selección histórica de proveedores en PartyMaster. Elija los roles de socio que necesite su integración y compruebe el rango de la selección.</p></figcaption></figure>

### **Activación de BOD**

Una vez marcados todos los BOD correctos para su publicación, seleccione la pestaña Options.

Revise las opciones de su inquilino. El ejemplo histórico resalta Publish y Use Process/Sync Verb; no son ajustes universales para todas las integraciones.

<figure><img src="https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U" alt="Pestaña Options histórica de LN con Publish y Use Process/Sync Verb resaltados y un rango de empresas visible."><figcaption><p>Ejemplo histórico de Options. Aquí están seleccionados Publish y Use Process/Sync Verb; verifique el modo, el rango de empresas y los suscriptores para su propia ejecución.</p></figcaption></figure>

Antes de **Process**, utilice **Count** o **Simulate** y revise el número de registros y el rango de empresas en los casos en que su versión de LN ofrezca esos modos. Publique solo con la aprobación del administrador de integración. Una confirmación de que se activaron los BOD no demuestra la entrega a DocBits.

<figure><img src="https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM" alt="Pestaña Options histórica de LN con el botón Process resaltado antes de la ejecución."><figcaption><p>Acción Process histórica antes de la ejecución. Esta captura no contiene ningún resultado de publicación ni confirmación de que DocBits recibiera datos.</p></figcaption></figure>

## Verificar en DocBits

Compruebe en Infor ION que la entrega a la organización de DocBits prevista se ha realizado correctamente. Después abra **Ajustes → Procesamiento de Documentos → Búsqueda de datos maestros**. En **BOD Datos de entrada**, abra **Proveedor**. Elija el campo identificador en **Búsqueda por columna**, introduzca un número o un nombre de proveedor conocido en **Buscar Cadena** y utilice la lupa para buscar. Abra **Orden de compra** y busque un número de pedido conocido. Compruebe también **Cabecera de pedido** si su mapeo separa cabecera y líneas. Compare los identificadores y la empresa con LN; no deduzca que todos los registros han llegado solo porque el mensaje de publicación se haya enviado correctamente.

<figure><img src="../../../../.gitbook/assets/dbdc-1144-supplier-es-20261112.png" alt="Vista Proveedor de Búsqueda de datos maestros de DocBits en español con los campos de búsqueda Búsqueda por columna y Buscar Cadena y diez filas de proveedores de ejemplo inventadas de SUP-1001 a SUP-1010."><figcaption><p>Vista de verificación de proveedores en la versión 11.27.7 del sandbox con filas de ejemplo inventadas. Busque un identificador de prueba conocido y compárelo con LN e ION.</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/dbdc-1144-purchase-order-es-20261112.png" alt="Vista Orden de compra de Búsqueda de datos maestros de DocBits en español con las pestañas Proveedor y Orden de compra, los mismos campos de búsqueda y diez filas de órdenes de compra de ejemplo inventadas de PO-4500 a PO-4509."><figcaption><p>Vista de verificación de órdenes de compra en la versión 11.27.7 del sandbox con filas de ejemplo inventadas. Las filas no demuestran ninguna importación desde LN.</p></figcaption></figure>

Las vistas en inglés de Dev se revisaron el 29 de octubre de 2026 sin publicar ningún BOD, importar ningún archivo ni modificar datos maestros; en esas imágenes se excluyeron las filas de registros. Las dos capturas en español proceden de la versión 11.27.7 del sandbox y muestran filas de ejemplo inventadas en lugar de datos maestros reales; ilustran dónde comprobar, no una transferencia desde LN completada. Si falta un registro esperado, revise los registros de publicación de LN, el enrutamiento en ION, la organización y el mapeo de BOD antes de volver a ejecutar.
