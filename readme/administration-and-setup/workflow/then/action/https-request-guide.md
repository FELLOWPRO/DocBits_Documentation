# Send HTTPS Request

Estas tarjetas van en el grupo **Then** del Generador de flujos de trabajo: las acciones que se ejecutan cuando se cumplen las condiciones When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas se añaden al grupo <strong>Then</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Información de versión

**Versión actual:** v2 (la más reciente y recomendada)
**Estado:** ✅ Activa

**Historial de versiones:**
- v1 → Solicitud HTTP simple (ya no se recomienda)
- **v2 → ACTUAL** (se añadió soporte multilingüe)

**Qué cambió:** v2 añadió soporte de internacionalización (i18n). La funcionalidad principal de webhook/solicitud permanece sin cambios.

📖 [Version History & Changes](../../../changelog/release.md#2-https-request-https_request) | [Complete Card Database](../../../../DocFlow/docs/card_version.md)

---

## Propósito
Esta tarjeta envía un mensaje seguro a un sitio web o servicio y puede recibir una respuesta de vuelta. Es más simple que la tarjeta "Call API" y resulta útil para integraciones rápidas.

**Ejemplo real:** Envíe los datos de una factura a su sistema de contabilidad, o pregunte a un sistema externo si un empleado está autorizado a procesar esta compra.

---

## Cuándo usar esta tarjeta

Use esta tarjeta cuando necesite:
- Enviar notificaciones de webhook a servicios externos
- Activar acciones en otros sistemas
- Consultar un servicio web simple
- Enviar actualizaciones de estado a otras aplicaciones
- Realizar integraciones simples sin requisitos complejos de API

---

## Cómo funciona

1. **Comprobación del disparador**: El sistema comprueba si se cumplen las condiciones "Where" y "And"
2. **Construir la solicitud**: El sistema prepara la solicitud HTTPS con sus parámetros
3. **Enviar de forma segura**: Los datos se envían mediante una conexión HTTPS segura
4. **Recibir respuesta**: El servicio externo responde
5. **Continuar**: El flujo de trabajo continúa con los datos de la respuesta

---

## Parámetros

### URL
La dirección del sitio web al que enviar la solicitud

**Ejemplo:** `https://webhook.company.com/process`

### Headers
Instrucciones especiales para el destinatario

**Ejemplo:**
```
Content-Type: application/json
Authorization: Bearer token123
```

### Method
- **GET**: Solicitar información
- **POST**: Enviar datos
- **PUT**: Actualizar datos

### Parameters (Query String)
Datos añadidos a la URL

**Ejemplo:** `?action=approve&user_id=123`

### Request Data
La información real que se está enviando (en formato JSON)

**Ejemplo:**
```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

---

## Ejemplo paso a paso

### Escenario: Enviar una factura al sistema de contabilidad

**Configuración de la tarjeta:**
- **URL:** `https://accounting.company.com/invoices/create`
- **Method:** POST
- **Headers:** `Authorization: Bearer YOUR-TOKEN`
- **Request Data:**
```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Respuesta esperada:**
```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

---

## Casos de uso comunes

### 1. Notificaciones de webhook
Envíe notificaciones en tiempo real a otros sistemas cada vez que ocurra algo en DocFlow

**Ejemplo:**
- Documento aprobado → Enviar notificación al sistema de cumplimiento
- Proveedor modificado → Notificar al equipo de compras mediante un webhook de Slack/Teams

### 2. Integración con sistemas externos
Conecte DocFlow con otros sistemas empresariales para el intercambio automático de datos

**Ejemplo:**
- Después de procesar un documento → Sincronizar con el sistema ERP
- Nuevo proveedor añadido → Crear el registro del proveedor en el sistema de datos maestros

### 3. Flujos de trabajo de aprobación
Envíe el documento a un sistema de aprobación externo y reciba la decisión

**Ejemplo:**
- Factura de alto valor → Enviar a Finanzas para su aprobación
- Devolver el documento al sistema externo con la decisión

---

## Guía de configuración

### Paso 1: Obtener la información del endpoint
Solicite al sistema receptor:
- [ ] La URL HTTPS
- [ ] Los encabezados requeridos
- [ ] El método de autenticación
- [ ] El formato de solicitud esperado
- [ ] El formato de respuesta esperado

### Paso 2: Configurar la tarjeta
1. Introduzca la URL HTTPS
2. Establezca el método HTTP (normalmente POST)
3. Añada la autenticación si es necesario
4. Dé formato a los datos de la solicitud como JSON
5. Añada los encabezados personalizados

### Paso 3: Probar
Envíe una solicitud de prueba y verifique la respuesta

---

## Gestión de respuestas

Su solicitud HTTPS recibirá una respuesta. Respuestas comunes:

### Correcta (200, 201)
```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Solicitud incorrecta (400)
```json
{
  "error": "Missing required field: invoice_number"
}
```

### No autorizada (401)
```json
{
  "error": "Invalid authentication token"
}
```

### Error del servidor (500)
El sistema receptor tiene un problema interno

---

## Resolución de problemas

### "Certificate Error"
**Causa:** Problema con el certificado de seguridad HTTPS

**Solución:**
- Verifique que la URL es correcta
- Compruebe si el certificado del sitio web es válido
- Asegúrese de que está usando HTTPS (no HTTP)

### "Connection Refused"
**Causa:** No se puede conectar al servidor

**Solución:**
- Verifique que la dirección URL/IP es correcta
- Compruebe si el servicio está en ejecución
- Compruebe las reglas del firewall
- Verifique la conectividad a internet

### "No Response / Timeout"
**Causa:** El servidor no responde dentro del límite de tiempo

**Solución:**
- Compruebe si el servicio está disponible
- Verifique la URL del endpoint
- Compruebe si hay límites de tasa
- Contacte con el administrador del sistema

### "Invalid JSON"
**Causa:** Los datos de la solicitud tienen un formato incorrecto

**Solución:**
- Compruebe si faltan comas en el JSON
- Verifique que todas las comillas son correctas
- Valide el formato JSON (use un validador de JSON en línea)
- Compruebe si hay caracteres especiales

---

## Ejemplos

### Ejemplo 1: Enviar a un servicio de webhook
```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Ejemplo 2: Actualizar un sistema externo
```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Ejemplo 3: Consultar un servicio externo
```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

---

## Diferencia con la tarjeta "Call API"

| Característica | HTTPS Request | Call API |
|---------|---------------|----------|
| Simplicidad | Simple | Más compleja |
| Parámetros | Básicos | Avanzados |
| Gestión de errores | Básica | Detallada |
| Usar para | Integraciones rápidas | API complejas |
| Mejor para | Webhooks | API profesionales |

---

## Consideraciones de seguridad

✅ **Use siempre HTTPS** (conexión segura)

⚠️ **Nunca:**
- Ponga contraseñas en la URL
- Exponga las claves de API en los registros
- Incluya datos personales en los parámetros
- Use HTTP para datos confidenciales

---

## Buenas prácticas

✅ **Haga:**
- Pruebe primero con pequeñas cantidades de datos
- Incluya gestión de errores
- Registre las solicitudes importantes
- Documente la integración
- Supervise los fallos

❌ **No haga:**
- Llamar al mismo endpoint repetidamente si no es necesario
- Ignorar los errores de respuesta
- Incluir datos confidenciales en texto plano
- Superar los límites de tasa del servicio

---

## Tarjetas relacionadas

- **CALL_API** - Integración de API más avanzada
- **CONDITION_HTTPS_REQUEST_STATUS** - Comprobar si la solicitud fue correcta
- **ACTION_SEND_EMAIL** - Enviar por correo electrónico en su lugar
- **ACTION_RUN_DOCOPERATOR_SCRIPT** - Scripts automatizados
