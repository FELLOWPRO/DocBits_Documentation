# Verificación del ajuste de la empresa logística ante discrepancias en la recepción de mercancías

En procesos de compras a gran escala, no es raro encontrarse con situaciones en las que determinados datos no coinciden como se espera. Por ejemplo, puede aparecer un mensaje de error como:

**“Delivery Note L1234, Order Type: Purchase, Order 100000211, Position 10, Subsequent Number 1, Logistic Company&#x20;**<mark style="color:red;">**XXXX**</mark>**, Goods Receipt WE0000293 and Entry Position 10 not found in direct debit.”**

Este tipo de mensaje suele indicar que existe una discrepancia o falta información relacionada con la configuración de su empresa logística. La empresa logística es un elemento fundamental en los sistemas de planificación de recursos empresariales (ERP), especialmente en cadenas de suministro complejas que abarcan varias entidades legales o logísticas.

**¿Por qué ocurre?**

En entornos con varias entidades, cada transacción (compra, recepción de mercancías o inicio de pagos) debe asignarse correctamente a la empresa logística adecuada. La “empresa logística” es más que un identificador: determina qué almacén, centro de distribución o nodo de la red de suministro es responsable de las tareas del pedido y de su cumplimiento. Si el número de empresa no coincide con la entidad esperada, los procesos posteriores, como la verificación de la recepción de mercancías o las liquidaciones por domiciliación bancaria, pueden fallar.

## **Comprobaciones clave que debe realizar:**

### 1. Verifique la empresa logística asignada:

Compruebe los registros de datos maestros para asegurarse de que la empresa logística referenciada (en este caso, <mark style="color:red;">XXXX</mark>) es la entidad correcta para el pedido en cuestión. ¿Es <mark style="color:red;">XXXX</mark> el código de empresa adecuado para gestionar las compras de este proveedor o de esta línea de producto concreta?

### 2. Revise la configuración de la orden de compra (PO):

Confirme que la empresa logística de la orden de compra coincide con el lugar de recepción previsto. A veces un pedido se crea bajo una empresa logística, pero las mercancías se reciben bajo otra si la configuración no es coherente.

### 3. Compare la recepción de mercancías con los registros del almacén:

Consulte la recepción de mercancías (WE0000293) y asegúrese de que se contabilizó en el almacén de la empresa correcta. Si el almacén pertenece a otra empresa logística, es posible que deba corregir la configuración o procesar un traspaso a la entidad correcta.

### 4. Compruebe la integración y la coherencia de los datos maestros:

Los puntos de integración entre los distintos módulos (Compras, Almacén, Finanzas) dependen de códigos coherentes. Asegúrese de que la empresa logística esté definida de manera uniforme en todos los módulos relevantes.

### 5. Consulte la documentación y el soporte:

Si las comprobaciones internas no resuelven el problema, consulte la documentación de su sistema o póngase en contacto con su equipo de soporte del ERP. Pueden ayudarle a verificar si el código de la empresa logística está configurado correctamente o si se necesitan pasos de configuración adicionales.
