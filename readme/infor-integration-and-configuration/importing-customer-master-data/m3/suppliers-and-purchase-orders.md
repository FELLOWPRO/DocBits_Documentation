# Proveedores y órdenes de compra

## **Punto de conexión**

Deberá crear el punto de conexión DocBits API para poder crear el flujo de datos más adelante.

En InforOS, navegue hasta ION Desk → Conectar → Puntos de conexión

![Menú de navegación de Infor ION Desk con las entradas Home, Data Flows, API Flows y Mappings](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Una vez aquí, deberás crear un nuevo punto de conexión.

![Página Connection Points en ION Desk con los iconos de la barra de herramientas y una lista vacía de puntos de conexión](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Select API**

Asigne al punto de conexión un nombre y una descripción que describa su naturaleza y su entorno. En la pestaña Conexión, importe la cuenta de servicio que creó para el entorno con el que está trabajando.

![Configuración del punto de conexión de DocBits-DEV-Demo-Import en ION Desk que muestra Name, Description y cuenta de servicio bajo la pestaña Connection](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

A continuación, cambie a la pestaña Documentos. Deberá agregar los siguientes BOD al punto de conexión; no todos son necesarios para los datos maestros del proveedor y de la orden de compra, pero serán útiles cuando sea necesario implementar otras funciones como la contabilidad automática.

![Pestaña Documents del punto de conexión de ION Desk que lista Connection Documents incluyendo Acknowledge.SupplierInvoice, Sync.PurchaseOrder, Sync.RemitToPartyMaster y Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Por ahora solo nos centraremos en los BOD necesarios, siendo estos: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster y Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData and Sync.SupplierPartyMaster

La configuración para estos dos BOD debería ser similar a la siguiente (el nombre de la llamada API cambia para cada uno)

![Configuración Send to API para Sync.SupplierPartyMaster con el producto DocBits-DEV y la operación post CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

La configuración para este BOD debería ser similar a la siguiente

![Configuración de Send to API para Sync.PurchaseOrder con Product DocBits-DEV y la operación post CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Una vez configurados estos BOD, puede guardar el punto de conexión presionando el ícono ubicado justo al botón Atrás.

## **Flujo de datos**

El flujo de datos será similar al siguiente

![Diagrama de flujo de datos de ION que enlaza M3, un Filter y varias aplicaciones de la API de DocBits con un elemento End](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(El motivo de la existencia de múltiples API DocBits se debe a que cada conexión representa un entorno diferente, lo que significa que, dependiendo de la cantidad de entornos que tenga, su flujo de datos podría diferir ligeramente)

A los efectos de esta explicación, utilizaremos el ejemplo de tener cuatro entornos separados.

### **M3**

El inicio del flujo de datos consiste en su aplicación M3

### **Filtro**

La configuración del filtro es la siguiente

![Diálogo Filter Properties en ION Desk con las pestañas Properties, Attributes y Conditions y los campos Name y Description](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Pestaña Filter Attributes que enumera filas de Document Path Filtered Data Type para ChartOfAccounts, PurchaseOrder, RemitToPartyMaster y SupplierPartyMaster por AccountingEntityID](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Pestaña Filter Conditions con Document ChartOfAccounts, la condición Not Filtered y la expresión AccountingEntityID_3 equals 780_AAA](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(La entidad contable ID, por supuesto, es exclusiva de su organización)

### **API de DocBits**

Aquí agregará una aplicación y seleccionará los DocBits API que creó anteriormente

### **Archivos**

La configuración debería verse de la siguiente manera.

![Flujo de datos de ION desde M3 a través de un filtro hacia las aplicaciones DocBits-DEV-P, DocBits-DEV-S y DocBits-DEV-D con los documentos ChartOfAccounts, PurchaseOrder, RemitToPartyMaster y SupplierPartyMaster](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Activación de BOD de M3**

Navegue hasta la aplicación Infor M3

Una vez en el menú principal, escriba Comando + R para abrir el cuadro de búsqueda de comandos. Luego escriba evs006 y busque.

![Panel de Search and Start en Infor M3 abierto sobre el menú principal](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Una vez en esta página, deberá agregar SupplierPartyMaster, RemitToPartyMaster y PurchaseOrder a la lista.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Para cada caso, deberá presionar el ícono más para agregarlos a la lista.

![Lista de activación de BOD por eventos EVS006 en Infor M3 con una barra de herramientas Actions y el botón Apply](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Después de haber agregado cada uno de los BOD, haga clic derecho en el sustantivo BOD de BOD y seleccione Relacionado → Ejecutar

![Menú contextual del clic derecho en Infor M3 con las opciones Drill down, Select, Change, History, Copy, Delete y Display](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Se le dirigirá al siguiente menú, donde deberá cambiar el verbo BOD a Sincronizar y luego presionar NEXT para activar los BOD.

![Panel de activación de BOD en Infor M3 para la tabla CIDMAS con el nombre BOD SupplierPartyMaster y estado del trabajo Pending](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Una vez que active los BOD, recibirá una notificación que lo confirmará.

Si se hace correctamente, las tablas Proveedor y Orden de compra ahora deberían estar disponibles en Configuración → Búsqueda de datos maestros.
