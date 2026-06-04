---
hidden: true
---

# In Order Confirmation Purchase Order

### Compare with Purchase Order:

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Tarjeta de lógica: coincidencia de cantidad, precio unitario o descuento

Esta tarjeta de lógica está diseñada para verificar automáticamente que la cantidad, el precio unitario o el descuento detallados en una confirmación de pedido coincidan con las cifras correspondientes de la orden de compra. Esta verificación garantiza la coherencia y la precisión entre lo que se pidió y lo que el proveedor confirma que entregará.

#### Condición de disparo

La lógica se activa cuando se cumple alguna de las siguientes condiciones en una confirmación de pedido en relación con la orden de compra original:

* **Quantity**: La cantidad de artículos pedidos coincide con la cantidad confirmada por el proveedor.
* **Unit Price**: El precio por artículo acordado coincide con la confirmación del proveedor.
* **Discount**: Cualquier descuento aplicado es coherente entre la orden de compra y la confirmación de pedido.

#### Resultados

* **Equals**: Si la cantidad, el precio unitario o el descuento de la confirmación de pedido coinciden exactamente con la orden de compra, el sistema considera la confirmación como válida y continúa con los siguientes pasos del proceso de compras.
* **Not Equal**: Si hay una discrepancia en la cantidad, el precio unitario o el descuento, el sistema señala la confirmación de pedido para revisión manual. Esto garantiza que cualquier desajuste se resuelva antes de avanzar.

#### Beneficios

* **Precisión y coherencia**: Mantiene la precisión en el proceso de compras, garantizando que los pagos y las entregas se realicen sobre la base de cifras correctas.
* **Eficiencia**: Automatiza el proceso de verificación, reduciendo la necesidad de comprobaciones manuales y acelerando el procesamiento de pedidos.
* **Control de costes**: Ayuda a evitar pagos excesivos o entregas incorrectas detectando discrepancias de forma temprana en el proceso.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Definir los parámetros de comparación**: Configure los campos específicos (cantidad, precio unitario, descuento) que la tarjeta de lógica comprobará para detectar una coincidencia.
2. **Automatizar la verificación**: Configure el sistema para comparar automáticamente estos detalles al recibir una confirmación de pedido.
3. **Personalizar las alertas**: Decida el flujo de trabajo para gestionar las discrepancias, incluida la personalización de alertas para la revisión manual.

Esta tarjeta de lógica es vital para garantizar que los detalles de una confirmación de pedido se ajusten a la orden de compra original, salvaguardando la integridad del ciclo de compras. \`\`
