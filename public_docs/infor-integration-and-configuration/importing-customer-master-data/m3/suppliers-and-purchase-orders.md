# Proveedores y órdenes de compra de Infor M3

Este ejemplo conecta los BOD de proveedor y de orden de compra de M3 con DocBits a través de Infor ION. Las quince imágenes de Infor que aparecen a continuación son ejemplos históricos de un tenant y no una validación actual de su configuración de M3. Antes de ejecutar un trabajo, pida al administrador de Infor que confirme los nombres de los BOD, las tablas de origen, la empresa, la división, los nombres de las llamadas API y el entorno de destino. Para esta actualización no se ejecutó ninguna carga inicial de M3 ni ninguna importación en DocBits.

La [guía de carga inicial](https://docs.infor.com/m3udi/16.x/en-us/m3beud/appfoundhs/spl1567531742751.html) de Infor explica las definiciones de EVS006, el verbo y la selección de EVS007, el envío y el historial. Empiece con una selección limitada; una ejecución sin restricciones puede generar muchos eventos.

## **Punto de conexión**

Deberá crear el punto de conexión DocBits API para poder crear el flujo de datos más adelante.

En InforOS, navegue hasta ION Desk → Conectar → Puntos de conexión

<figure><img src="https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH_r3RAGOvJE6Ok67ST_272zFfhB_TTFYg3b-NwFq0CAv2o" alt="Navegación histórica de ION Desk con Conectar desplegado y Puntos de conexión resaltado."><figcaption><p>Navegación histórica: ION Desk → Conectar → Puntos de conexión.</p></figcaption></figure>

Una vez aquí, deberá crear un nuevo punto de conexión.

<figure><img src="https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE_WQj-0ONoE7McRl-f6_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI" alt="Página histórica de Puntos de conexión con una flecha verde que señala Agregar."><figcaption><p>Acción Agregar histórica para crear un punto de conexión.</p></figcaption></figure>

**Select API**

Asigne al punto de conexión un nombre y una descripción que describa su naturaleza y su entorno. En la pestaña Conexión, importe la cuenta de servicio que creó para el entorno con el que está trabajando.

<figure><img src="https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0" alt="Punto de conexión API histórico DocBits-DEV-Demo-Import con la pestaña Conexión seleccionada y un control para importar la cuenta de servicio."><figcaption><p>Pestaña Conexión histórica. Los nombres mostrados se refieren al entorno de ejemplo; utilice su propia cuenta de servicio.</p></figcaption></figure>

A continuación, cambie a la pestaña Documentos. Deberá agregar los siguientes BOD al punto de conexión; no todos son necesarios para los datos maestros del proveedor y de la orden de compra, pero serán útiles cuando sea necesario implementar otras funciones, como la contabilidad automática.

<figure><img src="https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8" alt="Pestaña Documentos histórica con Acknowledge.SupplierInvoice, Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster y Sync.SupplierPartyMaster."><figcaption><p>Lista histórica de documentos recibidos. El BOD de proveedor que se muestra es Sync.RemitToPartyMaster, sin el sufijo Data.</p></figcaption></figure>

Esta configuración histórica utiliza Sync.RemitToPartyMaster, Sync.SupplierPartyMaster y Sync.PurchaseOrder. Confirme los BOD necesarios para su mapeo de DocBits; la configuración puede variar según el tenant y la función.

* Sync.RemitToPartyMaster y Sync.SupplierPartyMaster

La siguiente imagen histórica muestra Sync.SupplierPartyMaster. Configure cada BOD de proveedor necesario con el nombre de la llamada API y la operación de recepción confirmados para su entorno; la segunda ruta de proveedor no aparece en la imagen.

<figure><img src="https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk" alt="Pestaña ION API histórica con Send to API seleccionado, el nombre de llamada API Sync.SupplierPartyMaster y una operación POST."><figcaption><p>Ruta histórica de SupplierPartyMaster. La imagen muestra una ruta de proveedor; confirme por separado la operación de recepción de cada BOD necesario.</p></figcaption></figure>

* Sync.PurchaseOrder

La siguiente imagen histórica muestra una operación de recepción de órdenes de compra. Confirme su endpoint actual y el formato de la solicitud para su entorno.

<figure><img src="https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4" alt="Pestaña ION API histórica con Send to API seleccionado para Sync.PurchaseOrder y una operación POST."><figcaption><p>Ruta histórica de PurchaseOrder. La antigua ruta de proxy de API Gateway es un ejemplo, no una dirección universal de DocBits.</p></figcaption></figure>

Una vez configurados estos BOD, puede guardar el punto de conexión presionando el ícono ubicado justo a la derecha del botón Atrás.

## **Flujo de datos**

Este flujo de datos histórico es un diseño posible; compruebe sus rutas y la organización de recepción en su propio tenant.

<figure><img src="https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8" alt="Flujo histórico desde M3 a través de un filtro Sí o No y después una división paralela hacia cuatro nodos DocBits API, con nodos de unión y de fin."><figcaption><p>Flujo histórico. La rama No termina antes de los nodos API; la rama Sí llega a los cuatro entornos de ejemplo.</p></figcaption></figure>

Los múltiples nodos DocBits API representan entornos separados en este ejemplo. Su diseño puede ser distinto; compruebe que los mensajes de prueba no puedan llegar a producción.

Los cuatro entornos se muestran solo como ejemplo.

### **M3**

El inicio del flujo de datos consiste en su aplicación M3

### **Filtro**

La configuración del filtro es la siguiente

<figure><img src="https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374_T2V0q__QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY" alt="Panel histórico Filter Properties con la pestaña Properties seleccionada y los campos Name y Description con el valor Division."><figcaption><p>Nombre y descripción históricos del filtro. El nombre Division por sí solo no establece qué registros se filtran.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA" alt="Pestaña Attributes histórica del panel Filter Properties con los atributos AccountingEntityID de ChartOfAccounts, PurchaseOrder, RemitToPartyMaster y SupplierPartyMaster."><figcaption><p>Atributos históricos: cada BOD tiene una ruta AccountingEntityID. Revise la ruta de cada documento en su tenant.</p></figcaption></figure>

<figure><img src="https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3_2DPj96aV0vLdZk2tzw" alt="Pestaña Conditions histórica del panel Filter Properties con ChartOfAccounts, Used Condition en Not Filtered y una expresión de ejemplo para AccountingEntityID_3."><figcaption><p>Ejemplo histórico de Conditions. Used Condition indica Not Filtered aunque aparece una expresión; compruebe la condición seleccionada y su efecto en lugar de suponer que la expresión está activa.</p></figcaption></figure>

(La entidad contable ID, por supuesto, es exclusiva de su organización)

### **API de DocBits**

Aquí agregará una aplicación y seleccionará los DocBits API que creó anteriormente

### **Documentos**

Seleccione los documentos asignados a los nodos de origen de M3 y de recepción. Confirme que los atributos del filtro y las rutas de recepción cubren todos los documentos necesarios.

<figure><img src="https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY" alt="Flujo histórico de M3 con su ícono de documento resaltado y un panel Documents con Sync.ChartOfAccounts, Sync.PurchaseOrder, Sync.RemitToPartyMaster y Sync.SupplierPartyMaster."><figcaption><p>Selección histórica de documentos para el flujo de M3. Es una lista de documentos BOD, no la configuración de un nodo de archivo.</p></figcaption></figure>

## **Activación de BOD de M3**

Navegue hasta la aplicación Infor M3

Abra el control **Search and Start** de M3, escriba **EVS006** y confirme el programa. Utilice la navegación que admita su cliente de M3.

<figure><img src="https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr_o" alt="Diálogo histórico Search and Start de M3 con evs006 y un botón OK."><figcaption><p>Búsqueda histórica de programas: escriba EVS006 en Search and Start.</p></figcaption></figure>

En EVS006, defina los sustantivos BOD necesarios para su mapeo aprobado. El ejemplo histórico utiliza SupplierPartyMaster, RemitToPartyMaster y PurchaseOrder. Confirme sus nombres de tabla de M3 en su versión antes de crear una definición de carga inicial.

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

Utilice la acción de agregar para cada definición aprobada. Compruebe la empresa y la división antes de continuar.

<figure><img src="https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN_ZlPk3W_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k_94_pYjt6Uw" alt="Barra de herramientas histórica de EVS006 recortada, con Agregar resaltado sobre los campos vacíos BOD noun, BOD variant, BOD y Table."><figcaption><p>Acción Agregar histórica en EVS006. Este recorte no muestra definiciones de carga inicial completadas.</p></figcaption></figure>

Después de haber agregado cada uno de los BOD, haga clic derecho en el sustantivo BOD del BOD y seleccione Relacionado → Ejecutar

<figure><img src="https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH_eIYzFj22XgFHZccEM9g2nVQ_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo" alt="Menú contextual histórico con Related desplegado y Run resaltado; History aparece debajo."><figcaption><p>Acción histórica Related → Run. Utilice History más adelante para revisar el resultado de la carga inicial.</p></figcaption></figure>

La acción **Run** relacionada abre EVS007. Elija **Sync** solo cuando el flujo de recepción de ION lo espere. Revise la selección y los filtros antes del envío final; pasar a la pantalla siguiente no demuestra que los datos se hayan entregado.

<figure><img src="https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD_ka--G1SFdzIhBAp7dq63_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA" alt="Pantalla histórica EVS007 Initial Load Job para CIDMAS y SupplierPartyMaster, con el estado Pending, el menú del verbo BOD abierto y Sync anotado mientras Show todavía aparece."><figcaption><p>Selección histórica del verbo en EVS007 antes de la ejecución. La imagen muestra un trabajo pendiente y una opción Sync anotada; no demuestra que se haya seleccionado Sync ni que se hayan importado datos.</p></figcaption></figure>

Una notificación de envío confirma que se solicitó el trabajo. En **History** de EVS006, revise el número de registros procesados y los errores. Después, compruebe el mensaje y el destino en Infor ION.

## Verificación en DocBits

Abra **Ajustes → Procesamiento de documentos → Búsqueda de datos maestros → BOD Datos de entrada → Proveedor** en la organización de DocBits prevista. Elija el campo identificador en el selector de columna, escriba un número o un nombre de proveedor conocido en **Buscar Cadena** y utilice la lupa para buscar. Después abra **Orden de compra** y busque un número de orden de compra conocido; consulte **Cabecera De Pedido** si su mapeo separa los datos de cabecera y de línea. Compare los identificadores y la empresa con el origen en M3. Una solicitud EVS007 correcta por sí sola no demuestra que hayan llegado todos los registros.

<figure><img src="../../../.gitbook/assets/suppliers-and-purchase-orders-supplier-bod-es-20261112.png" alt="Vista en español de Proveedor en Búsqueda de datos maestros de DocBits, con el selector de columna, el campo Buscar Cadena, el botón Acciones y filas de ejemplo inventadas."><figcaption><p>Vista de verificación Proveedor en la Sandbox. Las filas de la tabla son datos de ejemplo inventados; busque un identificador de prueba conocido y compárelo con M3 e ION.</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/suppliers-and-purchase-orders-purchase-order-bod-es-20261112.png" alt="Vista en español de Orden de compra en Búsqueda de datos maestros de DocBits, con la pestaña Orden de compra abierta, los controles de búsqueda, la entrada Cabecera De Pedido en el panel y filas de ejemplo inventadas."><figcaption><p>Vista de verificación Orden de compra en la Sandbox. Las filas de la tabla son datos de ejemplo inventados; no son prueba de una importación desde M3.</p></figcaption></figure>

Estas vistas en español se capturaron en la Sandbox, con la versión 11.27.7 en la esquina inferior izquierda de cada imagen, sin ejecutar ningún trabajo de M3, importar ningún archivo ni modificar datos maestros. Las filas de la tabla son datos de ejemplo inventados; las imágenes muestran dónde comprobar, no una transferencia completada. Si falta un registro esperado, revise el historial de EVS006, el enrutamiento de ION, el mapeo de BOD y la organización de DocBits antes de volver a ejecutar.
