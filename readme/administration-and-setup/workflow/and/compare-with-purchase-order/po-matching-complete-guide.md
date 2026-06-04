# Purchase Order (PO) Matching Cards - Complete Guide

Las tarjetas de cotejo de pedidos de esta página van en el grupo **And** del Generador de flujos de trabajo: comparan los datos de la factura con el pedido asociado antes de ejecutar las acciones Then:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas de cotejo de pedidos se añaden al grupo <strong>And</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
DocBits PO Matching Tutorial: Auto/Manual Line Matching, Tolerances & Mismatch Indicators
{% endembed %}

**Estado:** Cubre 15 tarjetas de comparación de PO con cálculos detallados

---

## 📌 Información de versión

**Tarjeta más evolucionada:** CONDITION_DOC_TO_PO_UNIT_PRICE (5 versiones, v5 la más reciente)
**Otras tarjetas complejas:** CONDITION_OC_TO_PO_ITEMS (v4), CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v4)

**Patrones clave:**
- **v2 → v3+:** Adición de parámetros de tolerancia para un cotejo flexible
- **v3 → v4:** Adición de parámetros de modo de comparación
- **v4 → v5:** Tolerancia mejorada con varias unidades (%, EUR, $, etc.)

📖 [Complete Version History](../../../changelog/release.md#-po-comparison--validation-cards) | [Card Version Database](../../../../DocFlow/docs/card_version.md)

---

## Comprensión del cotejo de PO

Cuando recibe una factura, esta debe coincidir con el pedido de compra (PO) realizado anteriormente. Las tarjetas de cotejo de PO comprueban automáticamente si los datos de la factura coinciden con los del PO.

**Visión general:**
```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

---

# 1. Coincidencia total del pedido de compra

## Propósito
Comprueba si toda la factura coincide con el PO perfectamente o dentro de la tolerancia

## Cuándo usar
- Antes de aprobar una factura
- Como comprobación de calidad preliminar
- Para identificar problemas a tiempo

## Cómo funciona
El sistema compara:
- Las cantidades de la factura frente a las cantidades del PO
- Los precios de la factura frente a los precios del PO
- Los artículos de la factura frente a los artículos del PO
- El total de la factura frente al total del PO

## Resultado
- **TRUE** (coincidencia total): Todo coincide, continuar
- **FALSE** (discrepancia): Algo no coincide, necesita revisión

## Ejemplo
```
PO:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Invoice:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Result: ✅ FULL MATCH
```

---

# 2. Comparación de precio unitario (Documento vs PO)

## Propósito
Compara el precio unitario de la factura con el precio unitario del PO

## Parámetros
- **Unit Price Tolerance**: Permitir una variación de hasta este importe
- **Tolerance Type**: Porcentaje (%) o Absoluto (€/$)
- **Operator**: Is Equal to, Is Greater than, Is Less than, etc.

## Cómo funciona (tolerancia porcentual)

**Fórmula:**
```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Ejemplo paso a paso:**
```
Step 1: Get prices
  PO Unit Price: €100.00
  Invoice Unit Price: €103.00

Step 2: Calculate difference
  Difference = |€103.00 - €100.00| = €3.00

Step 3: Calculate percentage
  Percentage = (€3.00 / €100.00) × 100 = 3%

Step 4: Check tolerance (5% allowed)
  Is 3% ≤ 5%? YES ✅

Result: PASS - Within tolerance
```

## Ejemplos reales

### Ejemplo 1: Pequeño aumento (aceptado)
```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

### Ejemplo 2: Gran aumento (rechazado)
```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

### Ejemplo 3: Descuento (también comprobado)
```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

### Ejemplo 4: Tolerancia de valor absoluto
```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

## Qué hacer con los resultados

**Si PASA ✅:**
- Continuar con la siguiente comprobación
- O aprobar la factura
- O proceder con la exportación

**Si FALLA ❌:**
- Marcar para revisión manual
- Pedir una explicación al proveedor
- Contactar con el equipo de compras
- Aprobar con una nota si es aceptable

---

# 3. Comparación de cantidad

## Propósito
Comprueba si la cantidad pedida coincide con la cantidad facturada

## Parámetros
- **Tolerance**: Importe o % permitido de diferencia
- **Operator**: Equals, Greater than, Less than
- **Quantity Type**: Ordered, Received, Open

## Ejemplo de cálculo

**Tolerancia porcentual:**
```
Formula:
  Quantity Variance % = |(Invoice Qty - PO Qty)| / PO Qty × 100

Example:
  PO Quantity: 100 units
  Invoice Quantity: 103 units
  Tolerance: ±5%

  Variance = |(103 - 100)| / 100 × 100
  Variance = 3 / 100 × 100 = 3%

  Is 3% ≤ 5%? YES ✅ ACCEPT
```

**Tolerancia absoluta:**
```
Formula:
  Quantity Variance = |Invoice Qty - PO Qty|

Example:
  PO Quantity: 100 units
  Invoice Quantity: 102 units
  Tolerance: ±5 units

  Variance = |102 - 100| = 2 units

  Is 2 units ≤ 5 units? YES ✅ ACCEPT
```

## Escenarios reales

### Entrega excesiva (más de lo pedido)
```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

### Entrega insuficiente (menos de lo pedido)
```
Ordered: 100 units
Invoiced: 95 units
Tolerance: ±5%

Variance = |(95-100)|/100 × 100 = 5%

Is 5% ≤ 5%? YES ✅

Decision: Accept - within tolerance
Possible reason: Partial shipment, rest to follow
```

---

# 4. Precio combinado de la diferencia de cantidad

## Propósito
Cuando la cantidad difiere, calcula si la diferencia de precio total es aceptable

## Por qué es importante
```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

## Cálculo

**Fórmula:**
```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Ejemplo:**
```
PO:
- Unit Price: €100
- Quantity: 100
- Total: €10,000

Invoice:
- Unit Price: €102 (2% higher)
- Quantity: 105 (5% higher)
- Total: €10,710

Analysis:
- Price variance: 2% ✅
- Quantity variance: 5% ✅
- Combined effect: 1.02 × 1.05 = 1.071 = 7.1% total increase

Is combined variance acceptable? Usually YES ✅
```

---

# 5. Comparación de ID de artículo / Número de artículo del proveedor

## Propósito
Comprueba si los artículos de la factura coinciden con los artículos del PO

## Cómo funciona

**Coincidencia exacta (la más simple):**
```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Número de artículo del proveedor (más común):**
```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

## Escenario: ¿Qué ocurre si no coincide?

```
PO Item: ABC-123 (Copper Wire, 2mm)
Invoice Item: ABC-124 (Steel Wire, 2mm)

Result: ❌ NO MATCH

Actions:
1. Is this a substitution? Check with procurement
2. Is this an error? Contact supplier
3. Is the description similar? Verify manually
```

---

# 6. Verificación del tipo de pedido

## Propósito
Verifica que el tipo de pedido de compra es correcto

## Tipos de pedido
- **Standard Order**: Compra habitual
- **Rush Order**: Urgente, puede tener un recargo
- **Frame Agreement**: Contrato a largo plazo
- **Blanket Order**: Contrato abierto
- **Consignment**: No paga hasta usarlo

## Ejemplo de comprobación
```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

---

# 7. Verificación de la fecha de entrega

## Propósito
Comprueba si la fecha de entrega coincide con la fecha prometida en el PO

## Cálculo

**Entrega tardía:**
```
Formula:
  Days Late = Invoice Delivery Date - PO Promised Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-22
  Days Late = 7 days

If tolerance is ±3 days:
  Is 7 ≤ 3? NO ❌ LATE
```

**Entrega anticipada:**
```
Formula:
  Days Early = PO Promised Date - Invoice Delivery Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-10
  Days Early = 5 days

Early delivery is usually OK ✅
Unless you need it at specific time
```

## Configuración de tolerancia
```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

---

# 8. Verificación de cargos (impuestos, envío, etc.)

## Propósito
Comprueba si los cargos adicionales (impuestos, envío, manipulación) coinciden con el PO

## Cargos comunes
```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

## Cálculo

**Ejemplo: Comprobación del cargo de envío**
```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Ejemplo: Varios cargos**
```
PO Total Charges:
  - Shipping: €50
  - Taxes: €300
  - Handling: €10
  Total: €360

Invoice Total Charges:
  - Shipping: €50
  - Taxes: €312 (11% tax)
  - Handling: €10
  Total: €372

Difference: €12
Check if within tolerance ✅ or ❌
```

---

# 9. Verificación de impuestos

## Propósito
Verifica que los importes de los impuestos se calculan correctamente

## Cálculo

**Fórmula:**
```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Problemas comunes:**
```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Ejemplo: Imposición con varias tasas**
```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

---

# 10. Cotejo de instalación/centro de coste

## Propósito
Garantiza que la factura corresponde a la instalación/centro de coste correcto

## Ejemplo
```
PO is for:
- Facility: Berlin Plant
- Cost Center: CC-2025

Invoice should have:
- Facility: Berlin Plant ✅
- Cost Center: CC-2025 ✅

If different facility: May need different approval
```

---

# 11. Validación del estado del proveedor

## Propósito
Comprueba si el proveedor sigue aprobado/activo

## Tipos de estado
```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

## Ejemplo de comprobación
```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

---

# ¿Qué tolerancia debo usar?

## Tolerancias estrictas (menor riesgo, más trabajo manual)
```
Use for:
- High-value items
- Items where exactness matters
- Regulated industries

Settings:
- Unit Price: ±1%
- Quantity: ±1%
- Delivery Date: ±1 day
- Charges: ±1%
```

## Tolerancias moderadas (equilibradas)
```
Use for:
- Most business transactions
- Standard items
- Normal purchasing

Settings:
- Unit Price: ±3-5%
- Quantity: ±3-5%
- Delivery Date: ±3 days
- Charges: ±5%
```

## Tolerancias amplias (mayor riesgo, menos trabajo manual)
```
Use for:
- Low-value items
- Bulk purchases
- Supplier agreements with flexibility

Settings:
- Unit Price: ±10%
- Quantity: ±10%
- Delivery Date: ±7 days
- Charges: ±10%
```

---

# Ejemplo de flujo de trabajo de cotejo de PO

```
Invoice Arrives
    ↓
Condition: "Is amount > €5000?" → YES
    ↓
Check: Full Match? → NO (10% price difference)
    ↓
Check: Unit Price within 5%? → NO (12% difference)
    ↓
Check: Quantity within 5%? → YES (2% difference)
    ↓
Decision: FAIL - Price variance too high
    ↓
Flag for: Manual review / Buyer approval
    ↓
Wait for: Buyer comment
    ↓
If Approved: Continue to Export
If Rejected: Return to Supplier
```

---

# Resolución de problemas de cotejo de PO

## "PO Not Found"
```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

## "Items Don't Match"
```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

## "Price Higher Than PO"
```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

## "Delivery Date Wrong"
```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

---

# Tabla resumen

| Tarjeta | Qué comprueba | Cálculo principal | Tolerancia común |
|------|----------------|------------------|-----------------|
| Full Match | Todo | Todas las comprobaciones | Variable |
| Unit Price | Precio por unidad | Diferencia en % o € | ±3-5% |
| Quantity | Cantidad pedida | Diferencia en % o unidades | ±3-5% |
| Combined Price | Total con cambio de cantidad | Qty × Price | ±5-10% |
| Item ID | Artículos correctos | Coincidencia de cadena | Exacta |
| Order Type | Tipo de compra | Coincidencia de cadena | Exacta |
| Delivery Date | Cuándo llegó | Diferencia de días | ±3 días |
| Charges | Cargos adicionales | Diferencia en % o € | ±5% |
| Tax | Importe del impuesto | Cálculo del % de impuesto | ±1% |
| Facility | Centro de coste | Coincidencia de cadena | Exacta |
| Supplier | ¿Aprobado? | Comprobación de estado | Solo activo |

---

# Documentación relacionada

- Consulte la guía "Invoice Validation" para ver el flujo de trabajo completo
- Consulte "Tolerance Settings" para conocer los valores recomendados por sector
- Consulte "Exception Handling" para saber qué hacer ante los fallos
- Contacte con su equipo de compras para conocer las políticas de tolerancia específicas
