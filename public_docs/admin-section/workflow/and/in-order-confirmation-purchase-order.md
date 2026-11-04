# Confirmación de Orden de Compra

### Comparar con Orden de Compra:&#x20;

**Confirmación de Orden de Compra**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Tarjeta Lógica: Coincidencia de Cantidad, Precio Unitario o Descuento

Esta tarjeta lógica está diseñada para verificar automáticamente que la cantidad, precio unitario o descuento detallados en una confirmación de orden coincidan con las cifras correspondientes en la orden de compra. Esta verificación garantiza la consistencia y precisión entre lo solicitado y lo que el proveedor confirma entregar.

#### Condición de Disparo

La lógica se activa cuando se cumplen cualquiera de las siguientes condiciones en una confirmación de orden en relación con la orden de compra original:

* **Cantidad**: La cantidad de artículos solicitados coincide con la cantidad confirmada por el proveedor.
* **Precio Unitario**: El precio por artículo acordado coincide con la confirmación del proveedor.
* **Descuento**: Cualquier descuento aplicado es consistente entre la orden de compra y la confirmación de la orden.

#### Resultados

* **Igual**: Si la cantidad, precio unitario o descuento de la confirmación de la orden coincide exactamente con la orden de compra, el sistema considera la confirmación como válida y continúa con los siguientes pasos en el proceso de adquisición.
* **No Igual**: Si hay una discrepancia en la cantidad, precio unitario o descuento, el sistema marca la confirmación de la orden para revisión manual. Esto garantiza que se resuelvan las discrepancias antes de avanzar.

#### Beneficios

* **Precisión y Consistencia**: Mantiene la precisión en el proceso de adquisición, asegurando que los pagos y entregas se realicen en base a cifras correctas.
* **Eficiencia**: Automatiza el proceso de verificación, reduciendo la necesidad de verificaciones manuales y acelerando el procesamiento de pedidos.
* **Control de Costos**: Ayuda a prevenir pagos excesivos o entregas incorrectas al detectar discrepancias temprano en el proceso.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Definir Parámetros de Comparación**: Configurar los campos específicos (cantidad, precio unitario, descuento) que la tarjeta lógica verificará para una coincidencia.
2. **Automatizar Verificación**: Configurar el sistema para comparar automáticamente estos detalles al recibir una confirmación de orden.
3. **Personalizar Alertas**: Decidir sobre el flujo de trabajo para manejar discrepancias, incluida la personalización de alertas para revisión manual.

Esta tarjeta lógica es vital para garantizar que los detalles de una confirmación de orden se alineen con la orden de compra original, salvaguardando la integridad del ciclo de adquisiciones. \`\`
