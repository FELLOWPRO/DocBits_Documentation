# Coincidencia de PO

Cuando se trata de probar la configuración de Coincidencia de PO, deberás crear una orden de compra en LN/M3 para verificar si INFOR está sincronizado con DocBits.

## Crear una Orden de Compra en INFOR

* LN: [Manual de LN](https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf)
* M3: [Manual de M3](https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html)

Una vez que hayas creado tu orden de compra, ve a Configuración → Búsqueda de Datos Maestros y busca el número de orden de compra de la PO que acabas de crear, ya que ahora debería aparecer en los datos maestros de orden de compra en DocBits.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Deberías ver tu número de PO único aquí, lo que significa que DocBits e INFOR están sincronizados correctamente.

Ahora sube tu factura que coincida con la cantidad y los precios unitarios de la orden de compra que creaste. Valida el documento y selecciona Coincidencia de PO en la pantalla de validación.

Los elementos de línea de la PO y la factura deberían coincidir automáticamente, luego simplemente selecciona la opción de exportación y verifica si el documento se exporta sin errores. Si te encuentras con un error de exportación, crea un ticket para que el equipo de soporte de DocBits te ayude. Si no estás seguro de cómo crear un ticket dentro de DocBits, consulta nuestra documentación general de DocBits para obtener ayuda.
