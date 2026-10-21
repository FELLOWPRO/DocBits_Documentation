# Enviar solicitud HTTPS

***

Agregue esta tarjeta al grupo **Entonces** del Generador de flujo de trabajo: las acciones que se ejecutan una vez que coinciden las condiciones Cuándo/Y:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-es.png" alt="Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos."><figcaption><p>Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

***

## 📌 Información de versión

**Versión actual:** v2 (Último y recomendado) **Estado:** ✅ Activo

**Historial de versiones:**

* v1 → Solicitud HTTP simple (ya no se recomienda)
* **v2 → CURRENT** (se agregó soporte para varios idiomas)

**Qué cambió:** v2 agregó soporte de internacionalización (i18n). La funcionalidad principal de webhook/solicitud permanece sin cambios.

📖 [Historial de versiones y cambios](../../release.md) | [Base de datos de tarjetas completa](../../cards-overview/export-cards-guide.md)

***

## Propósito

Esta tarjeta envía un mensaje seguro a un sitio web o servicio y puede recibir una respuesta. Es más simple que la tarjeta "Call API" y es útil para integraciones rápidas.

**Ejemplo del mundo real:** Envíe los datos de la factura a su sistema de contabilidad o pregunte a un sistema externo si un empleado está aprobado para procesar esta compra.

***

## Cuándo utilizar esta tarjeta

Utilice esta tarjeta cuando necesite:

* Enviar notificaciones de webhooks a servicios externos
* Desencadenar acciones en otros sistemas
* Consultar un servicio web simple
* Enviar actualizaciones de estado a otras aplicaciones
* Realice integraciones simples sin requisitos de API complejos

***

## Cómo funciona

1. **Verificación de activación**: el sistema verifica si se cumplen las condiciones "Dónde" y "Y"
2. **Solicitud de compilación**: el sistema prepara la solicitud HTTPS con sus parámetros
3. **Enviar de forma segura**: los datos se envían mediante una conexión HTTPS segura
4. **Recibir respuesta**: El servicio externo responde
5. **Continuar**: el flujo de trabajo continúa con los datos de respuesta

***

## Parámetros

### URL

La dirección del sitio web al que enviar la solicitud

**Ejemplo:** `https://webhook.company.com/process`

### Encabezados

Instrucciones especiales para el destinatario.

**Ejemplo:**

```
Content-Type: application/json
Authorization: Bearer token123
```

### Método

* **GET**: Solicitar información
* **POST**: Enviar datos
* **PUT**: Actualizar datos

### Parámetros (cadena de consulta)

Datos agregados a la URL

**Ejemplo:** `?action=approve&user_id=123`

### Solicitar datos

La información real que se envía (en formato JSON)

**Ejemplo:**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## Ejemplo paso a paso

### Escenario: enviar factura al sistema de contabilidad

**Configuración de la tarjeta:**

* **URL:** `https://accounting.company.com/invoices/create`
* **Método:** POST
* **Encabezados:** `Authorization: Bearer YOUR-TOKEN`
* **Datos de solicitud:**

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

***

## Casos de uso comunes

### 1. Notificaciones de webhooks

Envíe notificaciones en tiempo real a otros sistemas cada vez que suceda algo en DocFlow

**Ejemplo:**

* Documento aprobado → Enviar notificación al sistema de cumplimiento
* Proveedor cambiado → Notificar al equipo de compras a través del webhook de Slack/Teams

### 2. Integración del sistema externo

Conecte DocFlow con otros sistemas empresariales para el intercambio automático de datos

**Ejemplo:**

* Después de procesar el documento → Sincronizar con el sistema ERP
* Nuevo proveedor agregado → Crear registro de proveedor en el sistema de datos maestros

### 3. Flujos de trabajo de aprobación

Enviar documento al sistema de aprobación externo y recibir decisión.

**Ejemplo:**

* Factura de alto valor → Enviar a Finanzas para su aprobación
* Devolver documento al sistema externo con decisión

***

## Guía de configuración

### Paso 1: obtener información del terminal

Solicite al sistema receptor:

* [] URL HTTPS
* [] Encabezados requeridos
* [] Método de autenticación
* [] Formato de solicitud esperado
* [] Formato de respuesta esperado

### Paso 2: configurar la tarjeta

1. Ingrese la URL HTTPS
2. Establecer el método HTTP (normalmente POST)
3. Agregue autenticación si es necesario
4. Formatear los datos de la solicitud como JSON
5. Agregue encabezados personalizados

### Paso 3: prueba

Enviar una solicitud de prueba y verificar la respuesta

***

## Manejo de respuestas

Su solicitud HTTPS recibirá una respuesta. Respuestas comunes:

### Éxito (200, 201)

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

### No autorizado (401)

```json
{
  "error": "Invalid authentication token"
}
```

### Error del servidor (500)

El sistema receptor tiene un problema interno.

***

## Solución de problemas

### "Error de certificado"

**Causa:** Problema con el certificado de seguridad HTTPS

**Solución:**

* Verifique que la URL sea correcta
* Compruebe si el certificado del sitio web es válido
* Asegúrate de estar usando HTTPS (no HTTP)

### "Conexión rechazada"

**Causa:** No se puede conectar al servidor

**Solución:**

* Verifique que la dirección URL/IP sea correcta
* Compruebe si el servicio se está ejecutando
* Verifique las reglas del firewall
* Verificar la conectividad a Internet

### "Sin respuesta/tiempo de espera"

**Causa:** El servidor no responde dentro del límite de tiempo

**Solución:**

* Comprueba si el servicio está disponible.
* Verificar la URL del punto final
* Comprueba si hay límites de tarifas
* Contactar al administrador del sistema

### "JSON no válido"

**Causa:** Los datos de la solicitud están mal formados

**Solución:**

* Compruebe si faltan comas en JSON
* Verifique que todas las cotizaciones sean correctas
* Validar el formato JSON (use el validador JSON en línea)
* Comprobar caracteres especiales

***

## Ejemplos

### Ejemplo 1: Enviar al servicio Webhook

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

### Ejemplo 2: actualizar el sistema externo

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

### Ejemplo 3: Consultar servicio externo

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## Diferencia con la tarjeta "Call API"

| Característica        | Solicitud HTTPS      | Llamar API          |
| -------------- | ------------------ | ----------------- |
| Simplicidad     | Sencillo             | Más complejo      |
| Parámetros     | Básico              | Avanzado          |
| Manejo de errores | Básico              | Detallado          |
| Usar para        | Integraciones rápidas | API complejas      |
| Lo mejor para       | Ganchos web           | API profesionales |

***

## Consideraciones de seguridad

✅ **Usa siempre HTTPS** (conexión segura)

⚠️ **Nunca:**

* Poner contraseñas en la URL
* Exponer claves API en registros
* Incluir datos personales en parámetros
* Utilice HTTP para datos confidenciales

***

## Mejores prácticas

✅ **Hacer:**

* Pruebe primero con pequeñas cantidades de datos
* Incluir manejo de errores
* Registrar solicitudes importantes
* Documentar la integración
* Monitorear fallas

❌ **No:**

* Llame al mismo punto final repetidamente si no es necesario
* Ignorar errores de respuesta
* Incluir datos confidenciales en texto sin formato
* Exceder los límites de la tarifa del servicio

***

## Tarjetas relacionadas

* **CALL\_API**: integración API más avanzada
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Verifique si la solicitud se realizó correctamente
* **ACTION\_SEND\_EMAIL** - Enviar por correo electrónico en su lugar
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** - Scripts automatizados
