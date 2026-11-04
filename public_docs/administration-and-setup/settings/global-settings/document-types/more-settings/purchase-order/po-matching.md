# Matching de OC

Cuando se trata de probar su configuración de Matching de OC, necesitará crear una Orden de Compra en LN/M3 para verificar si INFOR está sincronizado con DocBits.

## Creación de una Orden de Compra en INFOR

* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln_10.4_procpoug__en-us.pdf
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html

Una vez que haya creado su orden de compra, vaya a Configuración → Búsqueda de Datos Maestros y busque el número de orden de compra de la OC que acaba de crear, ya que ahora debería aparecer en sus datos maestros de orden de compra en DocBits.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Debería ver su número de OC único aquí; esto significa que DocBits e INFOR están correctamente sincronizados.

Ahora cargue su factura que coincida con la cantidad y los precios unitarios de la orden de compra que creó. Valide el documento y seleccione Matching de OC en la pantalla de validación.

Las partidas de la OC y de la factura deberían coincidir automáticamente, luego simplemente seleccione la opción de exportación y verifique si el documento se exporta o no sin ningún error. Si encuentra un error de exportación, cree un ticket para que el equipo de soporte de DocBits le asista. Si no está seguro de cómo crear un ticket dentro de DocBits, consulte nuestra documentación de Descripción General de DocBits para obtener ayuda.

