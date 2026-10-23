# Proveedores y órdenes de compra

## **Punto de conexión**

Deberá crear el punto de conexión de la API de DocBits (Connection Point) para poder crear después el flujo de datos.

Primero, en InforOS, navega a ION Desk → Conectar → Puntos de conexión

![Navegación de ION Desk en InforOS con las entradas de menú Home, Data Flows, API Flows y Mappings](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Una vez allí, deberá crear un nuevo punto de conexión.

![Página Connection Points en ION Desk con los iconos de la barra de herramientas y una lista vacía de puntos de conexión](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Seleccione API**

Asigne al punto de conexión un nombre y una descripción que indiquen su naturaleza y su entorno. En la pestaña Connection, importe la cuenta de servicio (service account) que creó para el entorno con el que está trabajando.

![Configuración del punto de conexión de DocBits-DEV-Demo-Import en ION Desk que muestra Name, Description y cuenta de servicio bajo la pestaña Connection](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

A continuación, cambie a la pestaña Documents. Deberá añadir al punto de conexión los siguientes BOD.

![Pestaña Documents del punto de conexión de ION Desk que enumera los documentos de conexión Ack SupplierInvoice, Sync.PurchaseOrder y Sync.ReceiveDelivery](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Este BOD se utiliza para indicar a DocBits que se ha producido un error en Infor. La configuración de estos dos BOD debería ser similar a la siguiente (cambiando el API Call Name en cada uno)

![Configuración de Send to API para Ack-SupplierInvoice con las pestañas en alemán Eingabedokument, Anforderungsparameter, Anforderungstext y Einstellungen](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

La configuración de este BOD debería ser similar a la siguiente

![Configuración de Send to API para Sync.PurchaseOrder con Product DocBits-DEV y la operación post CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

La configuración de este BOD debería ser similar a la siguiente

![Configuración Send to API para Sync.ReceiveDelivery en ION Desk con los campos API call name, Product y Operation](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Una vez configurados estos BOD, puede guardar el punto de conexión pulsando el icono situado a la derecha del botón de retroceso.

## **Flujo de datos (Data Flow)**

El flujo de datos tendrá un aspecto similar al siguiente

![Diagrama de flujo de datos de ION que enlaza la aplicación LN a través de un filtro con una aplicación DocBits API y un elemento End](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(El motivo de que haya varias API de DocBits es que cada conexión representa un entorno distinto; por tanto, según la cantidad de entornos que tenga, su flujo de datos podría diferir ligeramente)

Para esta explicación utilizaremos el ejemplo de cuatro entornos distintos.

### **Infor ERP / SAP**

El inicio del flujo de datos está formado por su aplicación Infor ERP / SAP

### **API de DocBits**

Aquí añadirá una aplicación y seleccionará las API de DocBits que creó anteriormente

### **Archivos**

La configuración debería ser la siguiente

![Configuración de Files en ION Desk que muestra una lista de documentos que incluye Sync.PurchaseOrder y Sync.ReceiveDelivery para la aplicación DocBits API](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **Activación de BOD en Infor ERP / SAP**

Una vez completado todo lo anterior, deberá navegar a Infor ERP / SAP y activar los BOD para que los distintos datos maestros que necesita para proveedores y órdenes de compra lleguen a DocBits.

![Menú Publish BODs en Infor LN con la ruta de navegación Common, BOD-Messaging, Publish BODs, Publish Order Management Transactional Data](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

En el menú anterior, en la pestaña del menú izquierdo, seleccione Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Seleccione la pestaña PurchaseOrder y marque la casilla.

![Página Publish Order Management Transactional Data en Infor LN con la pestaña PurchaseOrder marcada y los botones PROCESS, CLONE, SELECT ALL y CLEAR ALL](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Proveedores**

Desde la página de inicio de Infor ERP / SAP, en la pestaña del menú izquierdo, navegue a Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Seleccione la pestaña PartyMaster y marque la casilla Supplier → Buy-from o SupplierPartyMaster.

![Página Publish Logistics Master Data en Infor LN con la pestaña PartyMaster y la opción Supplier Buy-from SupplierPartyMaster marcada](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Activación de BOD**

Una vez marcados todos los BOD correctos para su publicación, seleccione la pestaña Options.

Deberían seleccionarse las siguientes opciones.

![Pestaña Options de la página Publish Logistics Master Data en Infor LN que muestra la selección y los ajustes del documento con los botones PROCESS y CLEAR ALL](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Una vez hecho esto, pulse el botón PROCESS y se activarán los BOD. Aparecerá un mensaje en pantalla para notificarle que los BOD se han activado.

![Página Publish Logistics Master Data en Infor LN tras el procesamiento, mostrando la pestaña Factory Track, el panel Selection y las opciones de Settings](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Si el proceso se ha completado correctamente, las tablas de proveedores (Supplier) y órdenes de compra (Purchase Order) deberían estar disponibles en Settings → Master Data Lookup.

\\
