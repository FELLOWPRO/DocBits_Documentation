# Conciliación con órdenes de compra

Cuando se trata de probar su configuración de conciliación con órdenes de compra, deberá crear una orden de compra en LN/M3 para verificar si INFOR está sincronizado con DocBits.

## Crear una orden de compra en INFOR

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}


* LN: https://docs.infor.com/ln/10.4/en-us/lnolh/docs/ln\_10.4\_procpoug\_\_en-us.pdf&#x20;
* M3: https://docs.infor.com/m3udi/16.x/en-us/m3beud/default.html?helpcontent=ois610.html&#x20;

Una vez que haya creado su orden de compra, vaya a Configuración → Búsqueda de datos maestros y busque el número de orden de compra del PO que acaba de crear, como debería aparecer ahora en los datos maestros de su orden de compra en DocBits.

![](https://lh7-us.googleusercontent.com/JKGJdww6uF6U5mc1s1X\_uCcEMPYeqcikfrFOFjxpxpuaNjw-XmzNmIV2G2x6R-ZpwN2KlZACQe5Hs\_UB26klGU5XZyu6srVVLPVkS9AgEDZ1SO75YF-4ZTIt-aAuxoyyoW5sNPLsl0UxXwk193QNrFs)

Deberías ver tu número PO único aquí, esto significa que DocBits y INFOR están sincronizados correctamente.

Ahora cargue su factura que coincida con la cantidad y los precios unitarios de la orden de compra que creó. Valide el documento y seleccione Conciliación con la orden de compra en la pantalla de validación.

Las líneas de pedido PO y la factura deben coincidir automáticamente, luego simplemente seleccione la opción de exportación y verifique si el documento se exporta sin errores. Si encuentra un error de exportación, cree un ticket para que el equipo de soporte de DocBits lo ayude. Si no está seguro de cómo crear un ticket dentro de DocBits, consulte nuestra documentación de descripción general de DocBits para obtener ayuda.

\
