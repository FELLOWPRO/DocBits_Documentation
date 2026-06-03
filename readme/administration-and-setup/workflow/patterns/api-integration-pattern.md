# Patrón de integración de API

**Tipo de patrón:** Integración
**Complejidad:** Media
**Configuración estimada:** 45-60 minutos
**Casos de uso habituales:** Obtención de datos externos, validación de precios, búsqueda de datos maestros

---

Este patrón se monta en el **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Haga clic en **Add Card** para abrir la biblioteca de tarjetas y elija las tarjetas que usa este patrón: `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` y `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card del Workflow Builder, agrupada por categoría"><figcaption><p>La biblioteca <strong>Add Card</strong>: elija de estas categorías las tarjetas de API, condición y campo que usa este patrón.</p></figcaption></figure>

---

## Resumen del patrón

Este patrón muestra cómo integrar DocBits con API externas para obtener, validar y almacenar datos de sistemas externos. Es uno de los patrones de flujo de trabajo más habituales para conectar DocBits con sistemas de precios, servicios de validación, sistemas ERP y otras fuentes de datos externas.

**Qué hace este patrón:**
1. Llama a una API externa para obtener datos
2. Valida la respuesta de la API
3. Almacena los datos de la respuesta en campos del documento
4. Toma decisiones según los datos obtenidos
5. Enruta los documentos en consecuencia

---

## Cuándo usar este patrón

Use este patrón cuando necesite:
- ✅ Obtener precios en tiempo real de sistemas externos
- ✅ Validar información de proveedores con la base de datos maestra
- ✅ Buscar detalles de productos en sistemas de catálogo
- ✅ Obtener tipos de cambio de servicios de divisas
- ✅ Verificar direcciones con servicios de geocodificación
- ✅ Comprobar niveles de inventario en sistemas de almacén
- ✅ Validar tipos impositivos en servicios fiscales

**No use este patrón cuando:**
- ❌ Los datos ya están en los datos maestros de DocBits (use la búsqueda de datos maestros)
- ❌ El sistema externo no tiene API (use el patrón de script de DocOperator)
- ❌ Los datos cambian poco (considere la importación manual)

---

## Ejemplo completo de flujo de trabajo

### Escenario: Validar el precio de la factura frente a una API de precios actual

**Requisito de negocio:**
- El proveedor envía una factura
- La factura muestra un precio unitario de 52,00 €
- Debemos verificar que coincide con el precio actual del proveedor
- Si el precio varía más de un 5 %, escalar para revisión

**Tarjetas de flujo de trabajo utilizadas:**
1. CALL_API: obtener el precio actual de la API del proveedor
2. CONDITION_HTTPS_REQUEST_STATUS: comprobar si la llamada a la API tuvo éxito
3. ACTION_SET_FIELD_TO_TEXT: almacenar el precio de la API en un campo del documento
4. CONDITION_COMPARE_TWO_DOCFIELD_VALUES: comparar el precio de la factura con el de la API
5. ACTION_ASSIGN_TO_USER: enrutar según el resultado de la comparación
6. tasks_create: crear una tarea de revisión si es necesario

---

## Implementación paso a paso

### Paso 1: Llamar a la API externa

**Tarjeta:** CALL_API o ACTION_CALL_EXTERNAL_API

**Configuración:**
```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**Respuesta esperada:**
```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**Referencia de guía:** [Guía de Call API](../then/action/call-api-guide.md)

---

### Paso 2: Validar la respuesta de la API

**Tarjeta:** CONDITION_HTTPS_REQUEST_STATUS

**Configuración:**
```
Operator: IS EQUAL TO
Status Code: 200
```

**Lógica:**
```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**Referencia de guía:** [Guía de tarjetas de condición – Estado HTTP](../and/condition-cards-complete-guide.md#condition-https-request-status)

---

### Paso 3: Almacenar la respuesta de la API en campos del documento

**Tarjeta:** ACTION_SET_FIELD_TO_TEXT (o un asignador de campos equivalente)

**Configuración:**

**Campo 1: Current_API_Price**
```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**Campo 2: API_Price_Valid_Until**
```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**Campo 3: API_Discount_Available**
```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**Resultado:** Los datos de la API quedan almacenados en campos del documento para su uso posterior

**Referencia de guía:** [Guía de manipulación de campos – Almacenamiento de datos de API](../then/document-field/field-manipulation-guide.md#storing-api-data)

---

### Paso 4: Comparar el precio de la factura con el de la API

**Tarjeta:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configuración:**
```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**Cálculo:**
```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**Referencia de guía:** [Guía de tarjetas de condición – Comparación de campos](../and/condition-cards-complete-guide.md#field-comparison)

---

### Paso 5: Enrutar según el resultado de la validación

**Escenario A: Precio dentro de la tolerancia (Pass)**

**Tarjetas:**
- ACTION_SET_FIELD_TO_TEXT
  - Establecer «Price_Validation_Status» = «PASS»
  - Establecer «Price_Variance_Percent» = «4%»
- ACTION_APPROVE_DOCUMENT
  - Aprobar el documento automáticamente

**Escenario B: Precio fuera de la tolerancia (Fail)**

**Tarjetas:**
- ACTION_SET_FIELD_TO_TEXT
  - Establecer «Price_Validation_Status» = «FAIL»
  - Establecer «Price_Variance_Percent» = «12%» (ejemplo)
- tasks_create
  - Título de la tarea: «Review Price Variance - {{DOCUMENT_NUMBER}}»
  - Descripción: «Invoice price (€{{Invoice_Unit_Price}}) exceeds API price (€{{Current_API_Price}}) by {{Price_Variance_Percent}}»
  - Prioridad: Alta
- ACTION_ASSIGN_TO_USER
  - Asignar a: Responsable de compras
- ACTION_SEND_EMAIL_TO_GROUPS
  - Enviar notificación al equipo de compras

**Referencias de guía:**
- [Guía de asignación](../then/assignee/assignment-user-guide.md)
- [Guía de asignación de tareas](../then/task/task-assignment-guide.md)
- [Guía de envío de correo](../then/action/send-email-groups-guide.md)

---

## Diagrama completo del flujo de trabajo

```
DOCUMENT ARRIVES (Invoice with Product ABC123, Price €52)
│
├─ STEP 1: Call Pricing API
│  Card: CALL_API
│  Request: Get current price for ABC123
│  │
│  ├─ SUCCESS (200) ✅
│  │  Response: {"unit_price": 50.00}
│  │  │
│  │  ├─ STEP 2: Check API Status
│  │  │  Card: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Result: 200 = Success
│  │  │  │
│  │  │  ├─ STEP 3: Store API Data
│  │  │  │  Card: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Action: Store €50 in "Current_API_Price" field
│  │  │  │  │
│  │  │  │  ├─ STEP 4: Compare Prices
│  │  │  │  │  Card: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Calculate: Variance = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF Variance ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Set Status Field: "PASS"
│  │  │  │  │  │  └─ Auto-Approve Document
│  │  │  │  │  │     → END (Document Approved)
│  │  │  │  │  │
│  │  │  │  │  └─ IF Variance > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Set Status Field: "FAIL"
│  │  │  │  │     ├─ Create Review Task
│  │  │  │  │     ├─ Assign to Procurement Manager
│  │  │  │  │     └─ Send Email Notification
│  │  │  │  │        → END (Pending Review)
│  │  │  │  │
│  │  │  │  └─ [Field storage complete]
│  │  │  │
│  │  │  └─ [Status check complete]
│  │  │
│  │  └─ [API data retrieved]
│  │
│  └─ ERROR (Non-200) ❌
│     │
│     ├─ Set Error Status
│     ├─ Create "API Error" Task
│     ├─ Assign to IT Support
│     └─ Send Email to Admin
│        → END (API Error - Manual Review)
```

---

## Plantillas de configuración

### Plantilla 1: Petición GET sencilla (búsqueda)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

**Uso:** Búsqueda simple de datos por ID

---

### Plantilla 2: Petición POST con cuerpo (validación)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**Uso:** Enviar datos del documento para su validación

---

### Plantilla 3: Petición compleja con datos anidados

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**Uso:** Procesamiento complejo de documentos con datos de tabla

---

## Gestión de errores

### Errores habituales y soluciones

#### Error 1: Tiempo de conexión agotado

**Síntomas:**
- La API no responde
- El flujo de trabajo se queda esperando

**Solución:**
```
1. Check API endpoint URL (typo?)
2. Verify network connectivity
3. Check API service status
4. Implement timeout handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Create "API Timeout" task
     → Assign to IT Support
     → Send email notification
     → Use fallback value (if available)
```

#### Error 2: 401 No autorizado

**Síntomas:**
- La API devuelve el estado 401
- La autenticación falló

**Solución:**
```
1. Verify API key is correct
2. Check if API key expired
3. Ensure Authorization header formatted correctly
4. Implement auth error handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Create "API Auth Failed" task
     → Assign to Admin
     → Log error details
     → Stop workflow execution
```

#### Error 3: Formato de respuesta no válido

**Síntomas:**
- Se recibe la respuesta pero no se puede analizar
- Faltan campos esperados

**Solución:**
```
1. Verify API documentation
2. Check response structure matches expectations
3. Implement response validation:

   IF API_RESPONSE:data.unit_price IS NULL:
     → Set default value
     → Create "Invalid Response" task
     → Log response for debugging
```

**Referencia de guía:** [Resolución de problemas de Call API](../then/action/call-api-guide.md#troubleshooting)

---

## Variantes avanzadas

### Variante 1: Encadenamiento de varias API

**Escenario:** Se necesitan datos de varias API

```
Step 1: Call Supplier API → Get Supplier Details
Step 2: Call Product API → Get Product Info (using Supplier ID from Step 1)
Step 3: Call Pricing API → Get Price (using Product ID from Step 2)
Step 4: Validate & Store all data
```

---

### Variante 2: Llamadas a la API condicionales

**Escenario:** Llamar a la API solo bajo ciertas condiciones

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

---

### Variante 3: Almacenamiento en caché de respuestas de API

**Escenario:** Reducir las llamadas a la API almacenando las respuestas en caché

```
1. Check if "API_Last_Called" date is today
2. IF Yes:
     → Use cached value from "Cached_API_Price" field
3. IF No:
     → Call API
     → Store response in "Cached_API_Price"
     → Set "API_Last_Called" to today
```

---

## Consideraciones de rendimiento

### Buenas prácticas

✅ **Recomendado:**
- Almacenar en caché las respuestas de la API cuando sea posible
- Usar ajustes de tiempo de espera (30-60 segundos)
- Implementar lógica de reintentos para fallos temporales
- Registrar las llamadas a la API para depuración
- Supervisar el uso y los costes de la API
- Probar primero con documentos de muestra

❌ **No recomendado:**
- Llamar a las API de forma síncrona para cada documento (considere el procesamiento por lotes)
- Ignorar los errores de respuesta
- Codificar credenciales de forma fija en el flujo de trabajo
- Realizar llamadas innecesarias a la API
- Olvidar gestionar los tiempos de espera

---

## Lista de pruebas

Antes de desplegar este patrón:

- [ ] Probar la llamada a la API con datos válidos
- [ ] Probar la llamada a la API con datos no válidos
- [ ] Probar el escenario de tiempo de espera (¿qué pasa si la API es lenta?)
- [ ] Probar el fallo de autenticación
- [ ] Probar un formato de respuesta no válido
- [ ] Probar el almacenamiento de campos (¿se guardan bien los datos?)
- [ ] Probar la lógica de comparación (¿cálculo correcto?)
- [ ] Probar el enrutamiento (¿los documentos van al lugar correcto?)
- [ ] Probar la gestión de errores (¿se gestionan con elegancia?)
- [ ] Probar con un gran volumen (¿rendimiento aceptable?)

---

## Ejemplos reales

### Ejemplo 1: Búsqueda de tipo de cambio

**API:** https://api.exchangerate-api.com/v4/latest/USD

**Flujo de trabajo:**
1. Extraer la moneda de la factura: «GBP»
2. Llamar a la API de tipos de cambio
3. Obtener el tipo GBP→EUR
4. Calcular el equivalente en EUR
5. Almacenar en el campo «Amount_EUR»
6. Continuar el procesamiento con el importe en EUR

---

### Ejemplo 2: Comprobación de crédito del proveedor

**API:** Servicio interno de comprobación de crédito

**Flujo de trabajo:**
1. Extraer el código del proveedor
2. Llamar a la API de comprobación de crédito
3. Obtener el estado de crédito: «APPROVED» o «BLOCKED»
4. IF BLOCKED:
   - Detener el procesamiento
   - Crear una tarea urgente
   - Notificar al equipo de finanzas
5. IF APPROVED:
   - Continuar el flujo de trabajo normal

---

### Ejemplo 3: Enriquecimiento de datos maestros de producto

**API:** Servicio de catálogo de productos

**Flujo de trabajo:**
1. Extraer el código de producto de la factura
2. Llamar a la API de productos
3. Obtener: nombre del producto, categoría, cuenta contable
4. Almacenar en campos del documento
5. Usar para la contabilización automática

---

## Patrones relacionados

### Este patrón funciona bien con:

- **[Patrón de transformación de datos](data-transformation-pattern.md)**: transformar los datos de respuesta de la API
- **[Patrón de lógica de decisión](decision-logic-pattern.md)**: enrutar según los datos de la API
- **[Patrón de gestión de tareas](task-management-pattern.md)**: crear tareas para errores de API
- **[Patrón de PO Matching](po-matching-pattern.md)**: combinar precios de API con validación de pedidos

---

## Guías relacionadas

### Requisitos previos
- [Guía de Call API](../then/action/call-api-guide.md): documentación de la tarjeta de API
- [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md): lógica de condiciones
- [Guía de manipulación de campos](../then/document-field/field-manipulation-guide.md): operaciones con campos

### Tarjetas relacionadas
- **CALL_API**: [Guía de Call API](../then/action/call-api-guide.md)
- **ACTION_HTTPS_REQUEST**: [Guía de petición HTTPS](../then/action/https-request-guide.md)
- **CONDITION_HTTPS_REQUEST_STATUS**: [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md#condition-https-request-status)
- **ACTION_SET_FIELD_TO_TEXT**: [Guía de manipulación de campos](../then/document-field/field-manipulation-guide.md#set-field)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES**: [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md#field-comparison)

---

## Soporte y recursos

**¿Necesita ayuda?**
- Consulte la [resolución de problemas de Call API](../then/action/call-api-guide.md#troubleshooting)
- Revise los [códigos de respuesta de la API](../then/action/call-api-guide.md#response-scenarios)
- Pruebe primero la API con Postman
- Contacte con el soporte del proveedor de la API

**Comentarios:**
- Informe de problemas del patrón a: docs@docbits.com
- Sugiera mejoras
- Comparta sus casos de uso

---

**Versión del patrón:** 1.0
**Última actualización:** 23 de octubre de 2025
**Dificultad:** Media
**Tiempo estimado:** 45-60 minutos
**Tasa de éxito:** Alta (cuando la API es estable)
