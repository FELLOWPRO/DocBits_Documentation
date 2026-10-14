# Condition Cards - Complete Guide

Las tarjetas de condición de esta página van en los grupos **When** y **And** del Generador de flujos de trabajo: deciden si se ejecutan las acciones Then:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas de condición se añaden a los grupos <strong>When</strong> y <strong>And</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

**Cubre:** 31 tarjetas de condición restantes

---

## 📌 Información de versión

**Estado:** La mayoría de las tarjetas de condición son estables, con estructuras de una o dos versiones
**Patrón de versión:** La mayoría sigue el patrón v1 → v2 (añadiendo soporte de i18n)
**Ejemplo con varias versiones:** CONDITION_DECISION_TREE_DATA (v2-v3)

**Nota:** Algunas tarjetas de condición de comparación de PO tienen 4-5 versiones (consulte la PO Matching Guide para más detalles)

📖 [Complete Version History](../../../changelog/release.md) | [Card Version Database](../../../../DocFlow/docs/card_version.md) | [PO Matching Guide](../compare-with-purchase-order/po-matching-complete-guide.md)

---

# Condiciones de estado y situación del documento

## Tarjeta: CONDITION_DOC_STATUS_IS_ISNOT / Document Status Check

### Propósito
Comprueba si el documento tiene un estado específico

### Cuándo usar
- Antes de aprobar
- En una fase específica del flujo de trabajo
- Enrutamiento basado en el estado

### Tipos de estado del documento
```
- Upload: Being uploaded
- OCR: Being scanned
- Classification: Type detection
- Ready for Validation: Waiting for review
- Workflow: In process
- Pending Approval: Needs approval
- Pending Second Approval: Needs secondary approval
- Auto Accounting: Auto-booking
- Export: Being exported
- Error: Problem occurred
```

### Cómo funciona
```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

### Ejemplo
```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

### Parámetros
```
Operator: IS / IS NOT
Status: [Select status]
```

---

## Tarjeta: CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST

### Propósito
Comprueba si el estado coincide con alguno de una lista

### Cuándo usar
- Varios estados válidos
- Lógica OR para el estado

### Ejemplo
```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

---

## Tarjeta: CONDITION_DOC_TYPE_IS_ISNOT / Document Type Check

### Propósito
Comprueba si el documento es de un tipo específico

### Tipos de documento
```
- Invoice
- Credit Note
- Purchase Order
- Delivery Note
- ASN (Advanced Ship Notice)
- Receipt
- Return
- Custom Types
```

### Cómo funciona
```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

### Ejemplo
```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

---

## Tarjeta: CONDITION_DOC_TYPE_IS_ISNOT_LIST

### Propósito
Comprueba si el tipo coincide con alguno de una lista

### Ejemplo
```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

---

## Tarjeta: CONDITION_SUB_ORG_IS_ISNOT / Sub-Organization Check

### Propósito
Comprueba qué organización/departamento es propietario del documento

### Organizaciones
```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

### Ejemplo
```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

---

## Tarjeta: CONDITION_PURCHASE_ORDER_IMPORT / PO Import Check

### Propósito
Comprueba si el PO es de nueva importación o ya existente

### Cómo funciona
```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

### Cuándo usar
- Tratamiento diferente para los PO nuevos
- Omitir la validación para los PO conocidos
- Hacer un seguimiento de la primera vez que se ve a un proveedor

---

# Condiciones de persona asignada

## Tarjeta: CONDITION_USER_IS_ISNOT / User Check

### Propósito
Comprueba si el documento está asignado a un usuario específico

### Cómo funciona
```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

### Ejemplo
```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

---

## Tarjeta: CONDITION_USER_IS_ISNOT_IN_LIST

### Propósito
Comprueba si está asignado a algún usuario de una lista

### Ejemplo
```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

---

## Tarjeta: CONDITION_GROUP_IS_ISNOT / Group Check

### Propósito
Comprueba si está asignado a un grupo específico

### Ejemplo
```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

---

## Tarjeta: CONDITION_GROUP_IS_ISNOT_IN_LIST

### Propósito
Comprueba si está asignado a algún grupo de una lista

### Ejemplo
```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

---

# Condiciones de fecha y hora

## Tarjeta: CONDITION_TIME_IS_ISNOT_BETWEEN / Date Range Check

### Propósito
Comprueba si una fecha se encuentra entre dos fechas

### Cómo funciona
```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

### Cálculo
```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

### Cuándo usar
- Comprobar si está dentro de un período fiscal
- Comprobar si está dentro del plazo
- Comprobar si está dentro de un período promocional

### Ejemplo
```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

### Parámetros
```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

---

## Tarjeta: CONDITION_TODAY_IS_ISNOT / Today Check

### Propósito
Comprueba si la fecha de hoy cumple los criterios

### Cómo funciona
```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

### Casos de uso
```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

### Ejemplo
```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

---

## Tarjeta: CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA

### Propósito
Comprueba si la fecha de entrega coincide con las fechas de entrega aprobadas en el calendario

### Cómo funciona
```
Delivery Date from Invoice: 2025-10-25
    ↓
Check Master Calendar: Is 2025-10-25 acceptable?
    ↓
(Master calendar has list of acceptable dates)
    ↓
YES: Date is acceptable
NO: Date not in approved list
```

### Cuándo usar
- Verificar que la entrega coincide con las fechas acordadas
- Cotejar con el calendario de festivos
- Validar frente a las fechas contratadas

### Ejemplo
```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

---

# Condiciones de lógica

## Tarjeta: CONDITION_DECISION_TREE_DATA / Decision Table Returns

### Propósito
Comprueba si la tabla de decisión tiene valores de retorno

### Cómo funciona
```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

### Cuándo usar
- Antes de usar los resultados de la tabla de decisión
- Como condición de control (gate)
- Para comprobar si hay enrutamiento disponible

### Ejemplo
```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

---

## Tarjeta: CONDITION_CONTINUE_CHANCE / Random Probability

### Propósito
Continúa con la probabilidad especificada

### Cómo funciona
```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

### Cuándo usar
- Flujos de trabajo de pruebas A/B
- Muestreo de documentos
- Controles de calidad aleatorios

### Ejemplo
```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

### Cálculo
```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

---

## Tarjeta: CONDITION_MODULE_IS_ISNOT_ACTIVE / Feature Check

### Propósito
Comprueba si un módulo/función específico está habilitado

### Módulos
```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

### Cómo funciona
```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

### Cuándo usar
- Flujos de trabajo que dependen de funciones
- Procesamiento opcional
- Comprobar si una función con licencia está activa

---

## Tarjeta: CONDITION_HTTPS_REQUEST_STATUS / Request Result Check

### Propósito
Comprueba si la solicitud HTTPS fue correcta

### Códigos de estado
```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

### Cómo funciona
```
Send HTTPS request
    ↓
Receive response code
    ↓
Check: Was request successful (200)?
    ↓
YES: Continue with response data
NO: Error handling
```

### Ejemplo
```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

---

## Tarjeta: CONDITION_SUPPLIER_STATUS_IS_ISNOT / Supplier Status Check

### Propósito
Comprueba el estado del proveedor en el sistema

### Estados del proveedor
```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### Cómo funciona
```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

### Ejemplo
```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

---

## Tarjeta: CONDITION_SPECIFY_SUPPLIER_TYPE

### Propósito
Especifica/comprueba el tipo de proveedor

### Tipos de proveedor
```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

### Cómo funciona
```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

---

# Ejemplos de flujos de decisión

## Flujo 1: Procesamiento basado en el estado
```
Document Arrives
    ↓
Check: Status = "Ready for Validation"?
    ↓
YES: Validate document
    ↓
Check: Status = "Pending Approval"?
    ↓
YES: Create approval task
    ↓
Check: Status = "Error"?
    ↓
YES: Escalate to manager
```

## Flujo 2: Procesamiento basado en el proveedor
```
Invoice Arrives
    ↓
Check: Supplier status ACTIVE?
    ↓
NO: Block and escalate
    ↓
YES: Check: Supplier is preferred?
    ↓
YES: Fast track approval
NO: Standard approval
```

## Flujo 3: Basado en el importe con comprobación de fecha
```
Invoice Arrives
    ↓
Check: Amount > €10,000?
    ↓
YES: Check: Date within Oct (fiscal period)?
    ↓
YES: Assign to Finance Director
NO: Assign to Finance Manager
```

---

# Comparación de tarjetas de condición

| Tarjeta | Comprueba | Operador | Uso |
|------|--------|----------|-----|
| CONDITION_DOC_STATUS_IS_ISNOT | Estado del documento | IS / IS NOT | Comprobación de fase |
| CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST | Estado en lista | IN / NOT IN | Varios estados |
| CONDITION_DOC_TYPE_IS_ISNOT | Tipo de documento | IS / IS NOT | Filtrado por tipo |
| CONDITION_DOC_TYPE_IS_ISNOT_LIST | Tipo en lista | IN / NOT IN | Varios tipos |
| CONDITION_SUB_ORG_IS_ISNOT | Organización | IS / IS NOT | Comprobación de departamento |
| CONDITION_USER_IS_ISNOT | Usuario asignado | IS / IS NOT | Comprobación de usuario |
| CONDITION_USER_IS_ISNOT_IN_LIST | Usuario en lista | IN / NOT IN | Varios usuarios |
| CONDITION_GROUP_IS_ISNOT | Grupo asignado | IS / IS NOT | Comprobación de grupo |
| CONDITION_GROUP_IS_ISNOT_IN_LIST | Grupo en lista | IN / NOT IN | Varios grupos |
| CONDITION_TIME_IS_ISNOT_BETWEEN | Rango de fechas | BETWEEN | Ventana de fechas |
| CONDITION_TODAY_IS_ISNOT | Fecha de hoy | IS / IS NOT | Comprobación de hoy |
| CONDITION_DECISION_TREE_DATA | Retornos de DT | HAS / HAS NOT | Comprobación de resultado de DT |
| CONDITION_CONTINUE_CHANCE | Probabilidad | CHANCE | Control aleatorio |
| CONDITION_MODULE_IS_ISNOT_ACTIVE | Función habilitada | IS / IS NOT | Comprobación de función |
| CONDITION_HTTPS_REQUEST_STATUS | Resultado de solicitud | STATUS | Comprobación de respuesta |
| CONDITION_SUPPLIER_STATUS_IS_ISNOT | Estado del proveedor | IS / IS NOT | Comprobación de proveedor |

---

# Buenas prácticas para las condiciones

✅ **Haga:**
- Use condiciones específicas
- Pruebe la lógica con muestras
- Ordene las condiciones de forma lógica
- Tenga un respaldo para todas las rutas
- Documente la lógica compleja

❌ **No haga:**
- Crear condiciones circulares (A si B, B si A)
- Hacer las condiciones demasiado complejas
- Olvidar los casos límite
- Asumir que el campo siempre tiene un valor
- Crear condiciones imposibles

---

# Combinación de varias condiciones

```
Condition 1: Type = Invoice?
    AND
Condition 2: Amount > €5000?
    AND
Condition 3: Supplier status = Active?
    ↓
ALL TRUE → Process
SOME FALSE → Stop
```

---

# Tarjetas relacionadas

- **CONDITION_DOC_FIELD_CONTAINS** - Comprobación del contenido de un campo
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - Comparación de campos
- **CONDITION_CHECKBOX_IS** - Comprobación de casilla de verificación
