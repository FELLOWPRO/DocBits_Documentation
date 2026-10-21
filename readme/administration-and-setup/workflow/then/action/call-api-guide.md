# Llamar API externa

***

Agregue esta tarjeta al grupo **Entonces** del Generador de flujo de trabajo: las acciones que se ejecutan una vez que coinciden las condiciones Cuándo/Y:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-es.png" alt="Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos."><figcaption><p>Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

***

## 📌 Información de versión

**Versión actual:** v2 (Último y recomendado) **Estado:** ✅ Activo

**Historial de versiones:**

* v1 → Llamada API básica (ya no se recomienda)
* **v2 → CURRENT** (se agregó soporte para varios idiomas)

**Qué cambió:** v2 agregó soporte de internacionalización (i18n) con claves de traducción. La funcionalidad sigue siendo idéntica.

📖 [Historial de versiones y cambios](../../release.md) | [Base de datos de tarjetas completa](../../cards-overview/export-cards-guide.md)

***

## Propósito

Esta tarjeta le permite enviar datos a un sitio web o servicio externo y recibir información. Piense en ello como enviar una pregunta a un servicio externo y obtener una respuesta que pueda utilizar en su flujo de trabajo.

**Ejemplo del mundo real:** Su empresa utiliza un sistema de precios en otro sitio web. Esta tarjeta puede solicitar automáticamente a ese sistema de precios el precio actual de un artículo e incluir ese precio en su documento.

***

## Cuándo utilizar esta tarjeta

Utilice esta tarjeta cuando necesite:

* Obtener información de un servicio externo (como precios, validación o datos de búsqueda)
* Enviar información del documento a otro sistema para su procesamiento.
* Integrar con servicios de terceros
* Obtener datos automáticamente sin búsquedas manuales
* Conecte varios sistemas empresariales juntos

**Escenarios comunes:**

* Buscar información de proveedores en una base de datos.
* Obtenga precios en tiempo real de un servicio de precios
* Validar datos contra un sistema externo
* Obtener información de envío de un proveedor de logística

***

## Cómo funciona

1. **Verificación de condición**: el flujo de trabajo primero verifica si se cumplen las condiciones en las secciones "Dónde" y "Y".
2. **Preparar Datos**: La tarjeta recoge los parámetros que has configurado
3. **Enviar Solicitud**: Envía tus datos a la API/servicio externo
4. **Recibir respuesta**: El servicio externo responde con datos
5. **Continuar**: el flujo de trabajo utiliza estos datos en tarjetas posteriores

***

## Parámetros explicados

### URL del punto final de API

**Qué es:** La dirección del servicio externo con el que desea comunicarse

**Ejemplo:** `https://api.supplier-system.com/product/pricing`

**Cómo encontrarlo:** Pregunte a su equipo de TI o al proveedor de servicios por su punto final API

***

### Método HTTP

**Qué es:** El tipo de solicitud a enviar

**Opciones:**

* **GET**: Solicitar información (como hacer una pregunta)
* **POST**: Enviar nuevos datos
* **PUT**: Actualizar datos existentes
* **DELETE**: Eliminar datos

**Más común:** GET (para buscar información)

***

### Encabezados

**Qué es:** Instrucciones adicionales para el servicio al que llamas

**Ejemplo:**

```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Por qué es necesario:** Los servicios a menudo requieren autenticación o instrucciones de formato específicas

***

### Parámetros (parámetros de consulta)

**Qué es:** Información adicional pasada en la URL

**Ejemplo:**

```
?supplier_id=12345&currency=USD
```

**Ejemplo real:** Si solicita precios, los parámetros pueden incluir el ID del proveedor y la moneda.

***

### Solicitar datos (cuerpo)

**Qué es:** La información que estás enviando al servicio

**Ejemplo:**

```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Cuando se usa:** Cuando se usan métodos POST o PUT

***

## Ejemplo paso a paso

### Escenario: obtener precios de proveedores en tiempo real

**Configuración:**

1. **Tipo de tarjeta:** Llamada API
2. **Punto final API:** `https://api.suppliers.com/v1/prices`
3. **Método:** POST
4. **Encabezados:** `Authorization: Bearer YOUR-API-KEY`
5.  **Datos de solicitud:**

    ```json
    {
      "product_id": "ABC123",
      "quantity": 100
    }
    ```

**Qué pasa:**

1. El documento llega con ID de producto: ABC123, Cantidad: 100
2. La tarjeta envía la solicitud a la API del proveedor
3. La API del proveedor responde con: `{"unit_price": 25.50, "total_price": 2550}`
4. El flujo de trabajo continúa con esta información de precios.
5. La tarjeta Next puede utilizar estos datos para validar el precio de la factura.

***

## Pasos de configuración

### 1. Obtenga información de la API

Póngase en contacto con el proveedor de servicios externo y solicite:

* [] URL del punto final de API
* [] Método de autenticación (clave API, nombre de usuario/contraseña, OAuth)
* [ ] Parámetros requeridos
* [] Formato de respuesta esperado
* [ ] Límites de tarifas o cuotas

### 2. Configurar la Tarjeta

1. Ingrese la URL del punto final de la API
2. Seleccione el método HTTP (generalmente GET o POST)
3. Agregue encabezados de autenticación si es necesario
4. Agregue los parámetros requeridos
5. Formatee los datos de la solicitud como JSON si es necesario

### 3. Pruebe la tarjeta

1. Utilice un documento de prueba
2. Ejecute el flujo de trabajo
3. Compruebe si la respuesta se recibe correctamente
4. Verificar que el formato de los datos coincida con las expectativas

***

## Escenarios de respuesta comunes

### Respuesta exitosa (Código de estado 200)

```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```

✅ Los datos están disponibles para usar en las próximas tarjetas

### Respuesta de error (código de estado 404)

```json
{
  "error": "Product not found"
}
```

⚠️ La API no pudo encontrar lo que buscas

### Tiempo de espera

El servicio externo no respondió dentro del límite de tiempo ⚠️ Verifique si el servicio está disponible o si la URL del punto final es correcta

***

## Flujos de trabajo de ejemplo

### Ejemplo 1: Validación automática de precios

**Escenario:** Validar los precios de factura con los precios actuales del proveedor

**Flujo:**

1. El documento llega con la partida de factura (Producto: A123, Precio: 50 €)
2. **Llame a la tarjeta API** → Pregunta al proveedor API: "¿Cuál es el precio actual del A123?"
3. El proveedor responde: "48€"
4. **Tarjeta de condición** → Comprueba si el precio de la factura (50€) está dentro del 5% del precio actual (48€)
5. **Tarjeta de aprobación** → Aprueba si está dentro de la tolerancia

### Ejemplo 2: búsqueda automática de proveedores

**Escenario:** Obtener datos maestros de proveedores de la base de datos central

**Flujo:**

1. La factura llega con el código de proveedor: SUPP-789
2. **Llamar tarjeta API** → Pregunta al sistema: "Dame detalles del proveedor SUPP-789"
3. El sistema responde con: Nombre, Contacto, Términos, etc.
4. **Establecer tarjetas de campo** → Complete los campos del documento con estos datos
5. **Exportar Tarjeta** → Exportar con información completa

### Ejemplo 3: Costos de envío en tiempo real

**Escenario:** Obtener costo de envío automático según el destino

**Flujo:**

1. El documento tiene dirección de entrega.
2. **Llame a la tarjeta API** → Pregunte al proveedor de envío: "¿Cuál es el costo para \[dirección]?"
3. El proveedor responde con el costo de envío.
4. **Calcular Tarjeta** → Agregar envío al monto total de la factura
5. **Exportar Tarjeta** → Enviar con total actualizado

***

## Solución de problemas

### Error de "tiempo de espera de conexión"

**Causa:** El servicio API no responde

**Soluciones:**

* [ ] Compruebe si el servicio está disponible (visite el sitio web)
* [] Verifique que la URL del punto final sea correcta (sin errores tipográficos)
* [] Verifique la conexión a Internet
* [ ] Póngase en contacto con el proveedor de servicios
* [ ] Comprueba si el servicio tiene límites de tarifas (estás enviando demasiadas solicitudes)

### Error "no autorizado" o "403 prohibido"

**Causa:** Error de autenticación

**Soluciones:**

* [] Verifique que su clave API sea correcta
* [] Compruebe si su clave API ha caducado
* [] Asegúrese de que el encabezado de autenticación tenga el formato correcto
* [] Verifique que tiene permisos para este punto final

### "Solicitud incorrecta" o "Error 400"

**Causa:** El formato de datos de la solicitud es incorrecto

**Soluciones:**

* [] Verifique la sintaxis JSON (faltan comas, comillas, etc.)
* [] Verifique que todos los campos obligatorios estén incluidos
* [] Verifique que los nombres de los parámetros coincidan con lo que espera el servicio
* [ ] Consultar la documentación API

### "La respuesta no funciona como se esperaba"

**Soluciones:**

* [] Pruebe la API usando una herramienta como Postman
* [] Compare el formato de respuesta real con el formato esperado
* [] Compruebe si la documentación de la API cambió
* [ ] Verifica que los datos que estás enviando sean correctos

***

## Uso de datos de respuesta

Una vez que recupere los datos de la API, las siguientes tarjetas pueden usarlos:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

***

## Notas de seguridad

⚠️ **Importante:** Nunca coloques información confidencial en la configuración de la tarjeta que pueda ser visible para otros usuarios

* No codifiques contraseñas
* Utilice claves API de forma segura
* No incluya datos personales en los registros
* Utilice puntos finales HTTPS (no HTTP)

***

## Consejos y mejores prácticas

✅ **Hacer:**

* Pruebe primero con una pequeña muestra de documentos
* Mantenga las llamadas API simples y enfocadas
* Agregar manejo de errores con tarjetas de condición
* Monitorear el uso/costos de API
* Documente los requisitos de API para su equipo

❌ **No:**

* Llame a las API para cada solicitud si puede almacenar datos en caché
* Ignorar códigos de error de respuesta
* Utilice API de prueba en producción
* Olvídese de agregar encabezados de autenticación
* Supongamos que la API siempre estará disponible

***

## Tarjetas relacionadas

* **ACTION\_HTTPS\_REQUEST**: solicitudes HTTPS similares pero más simples
* **CONDITION\_HTTPS\_REQUEST\_STATUS**: compruebe si la llamada API se realizó correctamente
* **ACTION\_SEND\_EMAIL**: envía datos por correo electrónico en lugar de API
* **CALL\_API** (versión diferente): método de llamada API alternativo

***

## ¿Necesita ayuda?

* Solicite documentación de API a su equipo de TI/Integración
* Utilice la herramienta Postman para probar primero los puntos finales de API
* Consulte el portal de soporte del proveedor de servicios
* Revise la documentación de la API para conocer los formatos requeridos
