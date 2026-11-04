# Proveedores y Órdenes de Compra

## **Punto de Conexión**

Necesitarás crear el punto de conexión de la API de DocBits para poder crear el flujo de datos más adelante.

En InforOS, ve a ION Desk → Conectar → Puntos de Conexión

![](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

Una vez aquí, necesitarás crear un nuevo punto de conexión.

![](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**Selecciona la API**

Asigna un nombre y una descripción al punto de conexión que describa su naturaleza y su entorno. En la pestaña de Conexión, importa la cuenta de servicio que creaste para el entorno con el que estás trabajando.

![](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

A continuación, cambia a la pestaña de Documentos. Necesitarás agregar los siguientes BODs al punto de conexión, no todos son necesarios para los datos maestros de proveedores y órdenes de compra, pero serán útiles cuando se implementen otras funciones como la Contabilidad Automática.

![](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

Por ahora nos enfocaremos solo en los BODs necesarios, que son: Sync.RemitToPartyMasterData, Sync.SupplierPartyMaster y Sync.PurchaseOrder.

* Sync.RemitToPartyMasterData y Sync.SupplierPartyMaster

La configuración para estos dos BODs debería verse similar a lo siguiente (cambiando el nombre de la llamada de la API para cada uno)

![](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

La configuración para este BOD debería verse similar a lo siguiente

![](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

Una vez configurados estos BODs, puedes guardar el punto de conexión presionando el ícono ubicado a la derecha del botón de retroceso.

## **Flujo de Datos**

El flujo de datos se verá similar a lo siguiente

![](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

(La razón de tener múltiples APIs de DocBits se debe a que cada conexión representa un entorno diferente, lo que significa que, dependiendo de la cantidad de entornos que tengas, tu flujo de datos podría diferir ligeramente)

Para este ejemplo, usaremos la configuración de tener cuatro entornos separados.

### **M3**

El inicio del flujo de datos consiste en tu aplicación M3

### **Filtro**

La configuración del filtro se ve así

![](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

(El ID de entidad contable, por supuesto, es único para tu organización)

### **API de DocBits**

Aquí agregarás una aplicación y seleccionarás la(s) API(s) de DocBits que creaste anteriormente
### **Archivos**

La configuración debería lucir de la siguiente manera

![](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **Desencadenamiento de M3 BOD**

Navega hasta la aplicación Infor M3

Una vez en el menú principal, escribe Command + R para abrir el cuadro de búsqueda del símbolo del sistema. Luego escribe evs006 y busca.

![](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

Una vez en esta página, necesitarás agregar el SupplierPartyMaster, RemitToPartyMaster y PurchaseOrder a la lista.

Sustantivo BOD: SupplierPartyMaster

Tabla: CIDMAS

Sustantivo BOD: RemitToPartyMaster

Tabla: CIDMAS

Sustantivo BOD: PurchaseOrder

Tabla: MPHEAD

Para cada caso necesitarás presionar el ícono de suma para agregarlos a la lista.

![](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

Después de haber agregado cada uno de los BODs, haz clic derecho en el sustantivo BOD del BOD y selecciona Relacionado → Ejecutar

![](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

Serás llevado al siguiente menú, donde necesitarás cambiar el verbo BOD a Sincronizar y luego presionar SIGUIENTE para desencadenar los BODs.

![](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

Una vez que desencadenes los BODs, recibirás una notificación confirmando esto.

Si se realiza con éxito, las tablas de Proveedor y Orden de Compra ahora deberían estar disponibles en Configuración → Búsqueda de Datos Maestros.
