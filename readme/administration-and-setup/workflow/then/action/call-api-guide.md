# Call External API

Estas tarjetas van en el grupo **Then** del Generador de flujos de trabajo: las acciones que se ejecutan cuando se cumplen las condiciones When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas se añaden al grupo <strong>Then</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Información de versión

**Versión actual:** v2 (la más reciente y recomendada)
**Estado:** ✅ Activa

**Historial de versiones:**
- v1 → Llamada API básica (ya no se recomienda)
- **v2 → ACTUAL** (se añadió soporte multilingüe)

**Qué cambió:** v2 añadió soporte de internacionalización (i18n) con claves de traducción. La funcionalidad permanece idéntica.

📖 [Version History & Changes](../../../changelog/release.md#1-call_api) | [Complete Card Database](../../../../DocFlow/docs/card_version.md#call_api)

---

## Propósito
Esta tarjeta le permite enviar datos a un sitio web o servicio externo y recibir información de vuelta. Considérelo como enviar una pregunta a un servicio externo y obtener una respuesta que puede utilizar en su flujo de trabajo.

**Ejemplo real:** Su empresa utiliza un sistema de precios en otro sitio web. Esta tarjeta puede preguntar automáticamente a ese sistema de precios cuál es el precio actual de un artículo e incorporar ese precio a su documento.

---

## Cuándo usar esta tarjeta

Use esta tarjeta cuando necesite:
- Obtener información de un servicio externo (como precios, validación o datos de búsqueda)
- Enviar información de documentos a otro sistema para su procesamiento
- Integrarse con servicios de terceros
- Obtener datos automáticamente sin búsquedas manuales
- Conectar varios sistemas empresariales entre sí

**Escenarios comunes:**
- Buscar información de proveedores en una base de datos
- Obtener precios en tiempo real de un servicio de precios
- Validar datos frente a un sistema externo
- Obtener información de envío de un proveedor logístico

---

## Cómo funciona

1. **Comprobación de condiciones**: El flujo de trabajo primero comprueba si se cumplen las condiciones de las secciones "Where" y "And"
2. **Preparar datos**: La tarjeta recopila los parámetros que ha configurado
3. **Enviar solicitud**: Envía sus datos a la API/servicio externo
4. **Recibir respuesta**: El servicio externo responde con datos
5. **Continuar**: El flujo de trabajo utiliza estos datos en las tarjetas posteriores

---

## Explicación de los parámetros

### API Endpoint URL
**Qué es:** La dirección del servicio externo con el que desea comunicarse

**Ejemplo:** `https://api.supplier-system.com/product/pricing`

**Cómo encontrarla:** Solicite a su equipo de TI o al proveedor del servicio su endpoint de API

---

### HTTP Method
**Qué es:** El tipo de solicitud que se va a enviar

**Opciones:**
- **GET**: Solicitar información (como hacer una pregunta)
- **POST**: Enviar datos nuevos
- **PUT**: Actualizar datos existentes
- **DELETE**: Eliminar datos

**Más común:** GET (para obtener información)

---

### Headers
**Qué es:** Instrucciones adicionales para el servicio al que está llamando

**Ejemplo:**
```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Por qué es necesario:** Los servicios a menudo requieren autenticación o instrucciones de formato específicas

---

### Parameters (Query Parameters)
**Qué es:** Información adicional que se pasa en la URL

**Ejemplo:**
```
?supplier_id=12345&currency=USD
```

**Ejemplo real:** Si está solicitando precios, los parámetros podrían incluir el ID del proveedor y la moneda

---

### Request Data (Body)
**Qué es:** La información que está enviando al servicio

**Ejemplo:**
```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Cuándo se usa:** Al utilizar los métodos POST o PUT

---

## Ejemplo paso a paso

### Escenario: Obtener precios de proveedor en tiempo real

**Configuración:**
1. **Tipo de tarjeta:** Call API
2. **API Endpoint:** `https://api.suppliers.com/v1/prices`
3. **Method:** POST
4. **Headers:** `Authorization: Bearer YOUR-API-KEY`
5. **Request Data:**
   ```json
   {
     "product_id": "ABC123",
     "quantity": 100
   }
   ```

**Qué ocurre:**
1. Llega un documento con Product ID: ABC123, Quantity: 100
2. La tarjeta envía una solicitud a la API del proveedor
3. La API del proveedor responde con: `{"unit_price": 25.50, "total_price": 2550}`
4. El flujo de trabajo continúa con esta información de precios
5. La siguiente tarjeta puede usar estos datos para validar el precio de la factura

---

## Pasos de configuración

### 1. Obtener información de la API
Contacte con el proveedor del servicio externo y solicite:
- [ ] La URL del endpoint de API
- [ ] El método de autenticación (clave de API, usuario/contraseña, OAuth)
- [ ] Los parámetros requeridos
- [ ] El formato de respuesta esperado
- [ ] Los límites de tasa o cuotas

### 2. Configurar la tarjeta
1. Introduzca la URL del endpoint de API
2. Seleccione el método HTTP (normalmente GET o POST)
3. Añada encabezados de autenticación si es necesario
4. Añada los parámetros requeridos
5. Dé formato a los datos de la solicitud como JSON si es necesario

### 3. Probar la tarjeta
1. Use un documento de prueba
2. Ejecute el flujo de trabajo
3. Compruebe si la respuesta se recibe correctamente
4. Verifique que el formato de los datos coincide con lo esperado

---

## Escenarios de respuesta comunes

### Respuesta correcta (Status Code 200)
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
✅ Los datos están disponibles para que los usen las siguientes tarjetas

### Respuesta de error (Status Code 404)
```json
{
  "error": "Product not found"
}
```
⚠️ La API no pudo encontrar lo que está buscando

### Tiempo de espera agotado
El servicio externo no respondió dentro del límite de tiempo
⚠️ Compruebe si el servicio está disponible o si la URL del endpoint es correcta

---

## Flujos de trabajo de ejemplo

### Ejemplo 1: Validación automática de precios
**Escenario:** Validar los precios de las facturas frente a los precios actuales del proveedor

**Flujo:**
1. Llega un documento con una línea de factura (Product: A123, Price: €50)
2. **Call API Card** → Pregunta a la API del proveedor: "¿Cuál es el precio actual de A123?"
3. El proveedor responde: "€48"
4. **Condition Card** → Comprueba si el precio de la factura (€50) está dentro del 5 % del precio actual (€48)
5. **Approval Card** → Aprueba si está dentro de la tolerancia

### Ejemplo 2: Búsqueda automática de proveedor
**Escenario:** Obtener los datos maestros del proveedor desde una base de datos central

**Flujo:**
1. Llega una factura con el código de proveedor: SUPP-789
2. **Call API Card** → Pregunta al sistema: "Dame los detalles del proveedor SUPP-789"
3. El sistema responde con: nombre, contacto, condiciones, etc.
4. **Set Field Cards** → Rellenan los campos del documento con estos datos
5. **Export Card** → Exporta con la información completa

### Ejemplo 3: Costes de envío en tiempo real
**Escenario:** Obtener el coste de envío automático según el destino

**Flujo:**
1. El documento tiene una dirección de entrega
2. **Call API Card** → Pregunta al proveedor de envíos: "¿Cuál es el coste hasta [address]?"
3. El proveedor responde con el coste de envío
4. **Calculate Card** → Añade el envío al importe total de la factura
5. **Export Card** → Envía con el total actualizado

---

## Resolución de problemas

### Error "Connection Timeout"
**Causa:** El servicio de API no responde

**Soluciones:**
- [ ] Compruebe si el servicio está disponible (visite el sitio web)
- [ ] Verifique que la URL del endpoint es correcta (sin errores tipográficos)
- [ ] Compruebe la conexión a internet
- [ ] Contacte con el proveedor del servicio
- [ ] Compruebe si el servicio tiene límites de tasa (está enviando demasiadas solicitudes)

### Error "Unauthorized" o "403 Forbidden"
**Causa:** Fallo de autenticación

**Soluciones:**
- [ ] Verifique que su clave de API es correcta
- [ ] Compruebe si su clave de API ha caducado
- [ ] Asegúrese de que el encabezado de autenticación tenga el formato correcto
- [ ] Verifique que tiene permisos para este endpoint

### Error "Bad Request" o "400 Error"
**Causa:** El formato de los datos de la solicitud es incorrecto

**Soluciones:**
- [ ] Compruebe la sintaxis JSON (comas, comillas, etc. que falten)
- [ ] Verifique que se incluyen todos los campos requeridos
- [ ] Compruebe que los nombres de los parámetros coinciden con lo que espera el servicio
- [ ] Consulte la documentación de la API

### "La respuesta no funciona como se esperaba"
**Soluciones:**
- [ ] Pruebe la API con una herramienta como Postman
- [ ] Compare el formato de respuesta real con el formato esperado
- [ ] Compruebe si la documentación de la API ha cambiado
- [ ] Verifique que los datos que está enviando son correctos

---

## Uso de los datos de respuesta

Una vez que obtenga datos de la API, las siguientes tarjetas pueden usarlos:

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

---

## Notas de seguridad

⚠️ **Importante:** Nunca incluya información confidencial en la configuración de la tarjeta que pueda ser visible para otros usuarios

- No codifique contraseñas de forma fija
- Use las claves de API de forma segura
- No incluya datos personales en los registros
- Use endpoints HTTPS (no HTTP)

---

## Consejos y buenas prácticas

✅ **Haga:**
- Pruebe primero con una pequeña muestra de documentos
- Mantenga las llamadas a la API simples y enfocadas
- Añada gestión de errores con tarjetas Condition
- Supervise el uso/coste de la API
- Documente los requisitos de la API para su equipo

❌ **No haga:**
- Llamar a las API en cada solicitud si puede almacenar los datos en caché
- Ignorar los códigos de error de respuesta
- Usar API de prueba en producción
- Olvidar añadir los encabezados de autenticación
- Asumir que la API siempre estará disponible

---

## Tarjetas relacionadas

- **ACTION_HTTPS_REQUEST** - Solicitudes HTTPS similares pero más simples
- **CONDITION_HTTPS_REQUEST_STATUS** - Comprobar si la llamada a la API fue correcta
- **ACTION_SEND_EMAIL** - Enviar datos por correo electrónico en lugar de por API
- **CALL_API** (versión diferente) - Método alternativo de llamada a la API

---

## ¿Necesita ayuda?

- Solicite a su equipo de TI/integración la documentación de la API
- Use la herramienta Postman para probar primero los endpoints de la API
- Consulte el portal de soporte del proveedor del servicio
- Revise la documentación de la API para conocer los formatos requeridos
