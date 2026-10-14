# Proveedores y órdenes de compra

## **Punto de conexión**

Deberá crear el punto de conexión de la API de DocBits (Connection Point) para poder crear después el flujo de datos.

Primero, en InforOS, navegue a ION Desk → Connect → Connection Points

![](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

Una vez allí, deberá crear un nuevo punto de conexión.

![](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**Seleccione API**

Asigne al punto de conexión un nombre y una descripción que indiquen su naturaleza y su entorno. En la pestaña Connection, importe la cuenta de servicio (service account) que creó para el entorno con el que está trabajando.

![](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

A continuación, cambie a la pestaña Documents. Deberá añadir al punto de conexión los siguientes BOD.

![](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

Este BOD se utiliza para indicar a DocBits que se ha producido un error en Infor. La configuración de estos dos BOD debería ser similar a la siguiente (cambiando el API Call Name en cada uno)

![](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

La configuración de este BOD debería ser similar a la siguiente

![](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

La configuración de este BOD debería ser similar a la siguiente

![](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

Una vez configurados estos BOD, puede guardar el punto de conexión pulsando el icono situado a la derecha del botón de retroceso.

## **Flujo de datos (Data Flow)**

El flujo de datos tendrá un aspecto similar al siguiente

![](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

(El motivo de que haya varias API de DocBits es que cada conexión representa un entorno distinto; por tanto, según la cantidad de entornos que tenga, su flujo de datos podría diferir ligeramente)

Para esta explicación utilizaremos el ejemplo de cuatro entornos distintos.

### **Infor ERP / SAP**

El inicio del flujo de datos está formado por su aplicación Infor ERP / SAP

### **API de DocBits**

Aquí añadirá una aplicación y seleccionará las API de DocBits que creó anteriormente

### **Archivos**

La configuración debería ser la siguiente

![](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **Activación de BOD en Infor ERP / SAP**

Una vez completado todo lo anterior, deberá navegar a Infor ERP / SAP y activar los BOD para que los distintos datos maestros que necesita para proveedores y órdenes de compra lleguen a DocBits.

![](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

En el menú anterior, en la pestaña del menú izquierdo, seleccione Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

Seleccione la pestaña PurchaseOrder y marque la casilla.

![](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **Proveedores**

Desde la página de inicio de Infor ERP / SAP, en la pestaña del menú izquierdo, navegue a Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

Seleccione la pestaña PartyMaster y marque la casilla Supplier → Buy-from o SupplierPartyMaster.

![](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **Activación de BOD**

Una vez marcados todos los BOD correctos para su publicación, seleccione la pestaña Options.

Deberían seleccionarse las siguientes opciones.

![](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

Una vez hecho esto, pulse el botón PROCESS y se activarán los BOD. Aparecerá un mensaje en pantalla para notificarle que los BOD se han activado.

![](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

Si el proceso se ha completado correctamente, las tablas de proveedores (Supplier) y órdenes de compra (Purchase Order) deberían estar disponibles en Settings → Master Data Lookup.

\\
