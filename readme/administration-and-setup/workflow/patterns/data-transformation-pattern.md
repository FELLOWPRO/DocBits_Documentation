# Patrón de transformación de datos

**Tipo de patrón:** Procesamiento y manipulación de datos
**Complejidad:** Media
**Configuración estimada:** 30-45 minutos
**Casos de uso habituales:** Cálculos de campos, formato de datos, conversión de divisas, conversión de unidades, enriquecimiento de datos

---

Este patrón se monta en el **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Haga clic en **Add Card** y abra la categoría **Document Field**: contiene las tarjetas de lectura, escritura, cálculo y formato que este patrón encadena:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card del Workflow Builder, agrupada por categoría"><figcaption><p>La biblioteca <strong>Add Card</strong>: las tarjetas de lectura/escritura de campos, cálculo y formato se encuentran en la categoría <strong>Document Field</strong>.</p></figcaption></figure>

---

## Resumen del patrón

Este patrón muestra cómo transformar, calcular, dar formato y enriquecer los datos de los documentos en los flujos de trabajo de DocBits. La transformación de datos es esencial para preparar los datos para la exportación, realizar cálculos, estandarizar formatos y enriquecer los documentos con información adicional.

**Qué hace este patrón:**
1. Extrae datos de los campos del documento
2. Realiza cálculos y transformaciones
3. Da formato a los datos según los estándares requeridos
4. Convierte entre unidades, divisas y fechas
5. Enriquece los documentos con datos derivados o de búsqueda
6. Valida y depura los datos

---

## Cuándo usar este patrón

Use este patrón cuando necesite:
- ✅ Calcular totales, subtotales e impuestos
- ✅ Convertir divisas o unidades
- ✅ Dar formato a fechas, números y texto
- ✅ Derivar valores a partir de campos existentes
- ✅ Enriquecer datos desde fuentes externas
- ✅ Estandarizar formatos de datos
- ✅ Limpiar y validar datos
- ✅ Preparar datos para la exportación

**No use este patrón cuando:**
- ❌ No se necesite ninguna transformación
- ❌ Los datos ya estén en el formato correcto
- ❌ Una simple copia de campo sea suficiente

---

## Tipos de transformación de datos

### 1. Cálculos

**Operaciones matemáticas:**
```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. Operaciones con cadenas

**Manipulación de texto:**
```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. Conversión de tipos de datos

**Transformaciones de tipo:**
```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. Conversiones de unidades

**Conversiones de medidas:**
```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. Conversiones de divisas

**Aplicación de tipos de cambio:**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. Transformaciones de fechas

**Operaciones con fechas:**
```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

---

## Ejemplo de flujo de trabajo completo

### Escenario: Cálculo del total de la factura y enriquecimiento de datos

**Requisito de negocio:**
- Extraer las líneas de la factura
- Calcular los totales de línea (cant. × precio)
- Calcular el subtotal (suma de los totales de línea)
- Calcular el importe de impuestos (subtotal × tipo impositivo)
- Calcular el total general (subtotal + impuestos)
- Convertir a EUR si la factura está en otra divisa
- Dar formato a los importes con 2 decimales
- Añadir la cuenta contable de la empresa según la categoría del producto
- Validar los cálculos contra el total de la factura
- Marcar si la desviación es > 1 %

**Tarjetas de flujo de trabajo utilizadas:**
1. ACTION_CALCULATE_FIELD - Realiza los cálculos
2. ACTION_SET_FIELD_TO_TEXT - Almacena los resultados
3. ACTION_COPY_FIELD_VALUE - Copia valores
4. CALL_API - Obtiene los tipos de cambio (si es necesario)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Valida los cálculos
6. ACTION_SET_FIELD_FROM_MASTER_DATA - Enriquece con las cuentas contables

---

## Implementación paso a paso

### Paso 1: Cálculos de las líneas

**Calcular los totales de línea:**

**Tarjeta:** ACTION_CALCULATE_FIELD

**Para cada línea:**
```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**Ejemplo:**
```
Line 1:
  Quantity: 100
  Unit Price: €50.00
  Calculation: 100 × 50.00 = €5,000.00
  Store in: Line_Total

Line 2:
  Quantity: 50
  Unit Price: €20.00
  Calculation: 50 × 20.00 = €1,000.00
  Store in: Line_Total

Line 3:
  Quantity: 25
  Unit Price: €15.50
  Calculation: 25 × 15.50 = €387.50
  Store in: Line_Total
```

**Referencia de guía:** [Guía de manipulación de campos - Cálculos](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Paso 2: Calcular el subtotal del documento

**Sumar todos los totales de línea:**

**Tarjeta:** ACTION_CALCULATE_FIELD

**Configuración:**
```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**Ejemplo:**
```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

---

### Paso 3: Calcular el importe de los impuestos

**Aplicar el tipo impositivo al subtotal:**

**Tarjeta:** ACTION_CALCULATE_FIELD

**Configuración:**
```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**Ejemplo:**
```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

---

### Paso 4: Calcular el total general

**Sumar el subtotal y los impuestos:**

**Tarjeta:** ACTION_CALCULATE_FIELD

**Configuración:**
```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**Ejemplo:**
```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

---

### Paso 5: Conversión de divisas (si es necesario)

**Comprobar si se necesita la conversión:**

**Tarjeta:** CONDITION_DOC_FIELD_IS

**Configuración:**
```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**Si se necesita la conversión:**

**Paso 5a: Obtener el tipo de cambio**

**Tarjeta:** CALL_API

**Configuración:**
```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**Ejemplo:**
```
Invoice Currency: USD
API Response: {
  "base": "USD",
  "rates": {
    "EUR": 0.92
  }
}

Exchange_Rate_To_EUR = 0.92
```

**Paso 5b: Convertir los importes**

**Tarjeta:** ACTION_CALCULATE_FIELD

**Configuración:**
```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**Ejemplo:**
```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**Referencia de guía:** [Patrón de integración de API - Conversión de divisas](api-integration-pattern.md#currency-conversion-example)

---

### Paso 6: Enriquecimiento de datos - Añadir cuentas contables

**Buscar la cuenta contable por categoría de producto:**

**Tarjeta:** ACTION_SET_FIELD_FROM_MASTER_DATA

**Configuración:**
```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**Ejemplo:**
```
Line 1:
  Product Category: "Office Supplies"
  Lookup → GL_Account_Mapping table
  Result: GL Account "4200-100" (Office Expense)

Line 2:
  Product Category: "IT Equipment"
  Lookup → GL_Account_Mapping table
  Result: GL Account "6100-200" (IT Assets)

Line 3:
  Product Category: "Services"
  Lookup → GL_Account_Mapping table
  Result: GL Account "5000-300" (Services Expense)
```

**Referencia de guía:** [Guía de manipulación de campos - Datos maestros](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Paso 7: Validar los cálculos

**Comparar el total calculado con el total de la factura:**

**Tarjeta:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configuración:**
```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**Cálculo:**
```
Variance % = |Calculated - Invoice| / Invoice × 100

Example:
  Calculated Total: €7,601.13
  Invoice Total: €7,600.00

  Variance = |7601.13 - 7600.00| / 7600.00 × 100
          = 1.13 / 7600.00 × 100
          = 0.015%

  Is 0.015% ≤ 1% tolerance? YES ✅
  Result: PASS (calculations match invoice)
```

**Lógica:**
```
IF Variance ≤ 1%:
  Set Validation_Status = "PASS"
  Continue processing
ELSE:
  Set Validation_Status = "FAIL"
  Create review task
  Flag for manual verification
```

**Referencia de guía:** [Guía de tarjetas de condición - Comparación de campos](../and/condition-cards-complete-guide.md#field-comparison)

---

### Paso 8: Dar formato a los datos para la exportación

**Estandarizar formatos:**

**Tarjeta:** ACTION_SET_FIELD_TO_TEXT

**Formato de fecha:**
```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**Formato de número:**
```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**Formato de texto:**
```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

---

## Transformaciones avanzadas

### Transformación 1: Cálculo de impuestos multinivel

**Escenario:** Distintos tipos impositivos por línea

```
Line 1: Product A (Tax Rate 19%)
Line 2: Product B (Tax Rate 7% - reduced)
Line 3: Product C (Tax Rate 0% - exempt)

Calculation:
  Line 1 Tax = €5,000.00 × 0.19 = €950.00
  Line 2 Tax = €1,000.00 × 0.07 = €70.00
  Line 3 Tax = €387.50 × 0.00 = €0.00

  Total Tax = €950.00 + €70.00 + €0.00 = €1,020.00
```

**Implementación:**
```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

---

### Transformación 2: Cálculo de descuentos

**Escenario:** Aplicar descuento por volumen y descuento por pronto pago

```
Original Subtotal: €10,000.00

Step 1: Volume Discount (10% for orders > €5,000)
  Discount = €10,000.00 × 0.10 = €1,000.00
  After Volume Discount = €10,000.00 - €1,000.00 = €9,000.00

Step 2: Early Payment Discount (2% if paid within 10 days)
  Discount = €9,000.00 × 0.02 = €180.00
  After Payment Discount = €9,000.00 - €180.00 = €8,820.00

Step 3: Calculate Tax (on discounted amount)
  Tax = €8,820.00 × 0.19 = €1,675.80

Final Total = €8,820.00 + €1,675.80 = €10,495.80
```

**Implementación:**
```
1. Check order value for volume discount eligibility
2. Calculate volume discount
3. Apply volume discount to subtotal
4. Check payment terms for early payment discount
5. Calculate early payment discount
6. Apply early payment discount
7. Calculate tax on final discounted amount
8. Calculate grand total
```

---

### Transformación 3: Conversión de unidad de medida

**Escenario:** Convertir la UM de la factura a la UM estándar

```
Invoice shows:
  Product: Steel Rods
  Quantity: 50
  Unit: Meters
  Unit Price: €10.00/meter
  Line Total: €500.00

Company standard UOM: Feet

Conversion:
  1 meter = 3.28084 feet

  Quantity (feet) = 50 meters × 3.28084 = 164.042 feet
  Unit Price (feet) = €10.00/meter ÷ 3.28084 = €3.05/foot

  Verification: 164.042 feet × €3.05/foot ≈ €500.00 ✅
```

**Implementación:**
```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

---

### Transformación 4: Cálculos de fechas

**Escenario:** Calcular las condiciones de pago y las fechas de vencimiento

```
Invoice Date: 2025-10-23
Payment Terms: NET30

Calculations:
  Due Date = Invoice Date + 30 days = 2025-11-22

  Early Payment Discount Available If:
    Payment Date ≤ Invoice Date + 10 days
    Discount End Date = 2025-11-02

  Days Until Due = Due Date - Today
    If Today = 2025-10-23: Days = 30
    If Today = 2025-11-15: Days = 7
    If Today = 2025-11-23: Days = -1 (overdue)
```

**Implementación:**
```
1. Extract Invoice_Date
2. Extract Payment_Terms (e.g., "NET30", "NET60", "2/10 NET30")
3. Parse payment terms
4. Calculate Due_Date
5. Calculate Discount_End_Date (if applicable)
6. Calculate Days_Until_Due
7. Set Status: "Current", "Due Soon", "Overdue"
```

---

### Transformación 5: Análisis y extracción de texto

**Escenario:** Extraer datos estructurados de texto no estructurado

```
Original Field: "PO-2025-ABC-12345-REV2"

Extract:
  Year: "2025"
  Department: "ABC"
  PO Number: "12345"
  Revision: "2"

Method:
  Split by delimiter "-"
  Array: ["PO", "2025", "ABC", "12345", "REV2"]

  Extract:
    Year = Array[1] = "2025"
    Department = Array[2] = "ABC"
    PO_Number = Array[3] = "12345"
    Revision = Extract digits from Array[4] = "2"
```

---

## Diagrama completo del flujo de trabajo de transformación

```
INVOICE DATA EXTRACTED
│
├─ STEP 1: LINE ITEM CALCULATIONS
│  For each line:
│    Quantity × Unit_Price = Line_Total
│  Result: Line totals calculated
│
├─ STEP 2: SUBTOTAL CALCULATION
│  SUM(All Line_Totals) = Subtotal
│  Result: €6,387.50
│
├─ STEP 3: TAX CALCULATION
│  Subtotal × Tax_Rate = Tax_Amount
│  €6,387.50 × 19% = €1,213.63
│
├─ STEP 4: GRAND TOTAL CALCULATION
│  Subtotal + Tax_Amount = Grand_Total
│  €6,387.50 + €1,213.63 = €7,601.13
│
├─ STEP 5: CURRENCY CHECK
│  │
│  ├─ Currency = EUR? YES
│  │  → Skip conversion
│  │  → Use Grand_Total as is
│  │
│  └─ Currency ≠ EUR? NO (e.g., USD)
│     │
│     ├─ Call Exchange Rate API
│     │  Get: USD → EUR rate (0.92)
│     │
│     ├─ Convert Amount
│     │  $7,601.13 × 0.92 = €6,993.04
│     │
│     └─ Store converted amount
│        Grand_Total_EUR = €6,993.04
│
├─ STEP 6: DATA ENRICHMENT
│  For each line:
│    Lookup Product_Category → GL_Account
│    Store GL_Account in line item
│  Result: All lines have GL accounts
│
├─ STEP 7: VALIDATION
│  │
│  ├─ Compare Calculated vs Invoice Total
│  │  Variance = |Calculated - Invoice| / Invoice × 100
│  │
│  ├─ Variance ≤ 1%? ✅
│  │  Set Validation_Status = "PASS"
│  │  Continue processing
│  │
│  └─ Variance > 1%? ❌
│     Set Validation_Status = "FAIL"
│     Create review task
│     Flag for manual check
│
├─ STEP 8: FORMATTING
│  │
│  ├─ Format Dates
│  │  10/23/2025 → 2025-10-23
│  │
│  ├─ Format Numbers
│  │  7601.13 → 7.601,13 (locale-specific)
│  │
│  ├─ Format Text
│  │  "abc corp" → "ABC CORP"
│  │
│  └─ Format for Export
│     All fields in ERP-compatible format
│
└─ TRANSFORMATION COMPLETE
   Document ready for next workflow step
```

---

## Plantillas de configuración

### Plantilla 1: Cálculos de factura estándar

```json
{
  "transformations": [
    {
      "step": 1,
      "name": "Calculate Line Totals",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Quantity}} * {{Unit_Price}}",
      "result_field": "Line_Total"
    },
    {
      "step": 2,
      "name": "Calculate Subtotal",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "SUM({{Line_Total}})",
      "result_field": "Calculated_Subtotal"
    },
    {
      "step": 3,
      "name": "Calculate Tax",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} * {{Tax_Rate}} / 100",
      "result_field": "Calculated_Tax"
    },
    {
      "step": 4,
      "name": "Calculate Total",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} + {{Calculated_Tax}}",
      "result_field": "Calculated_Total"
    }
  ]
}
```

---

### Plantilla 2: Flujo de trabajo de conversión de divisas

```json
{
  "currency_conversion": {
    "check_needed": {
      "card": "CONDITION_DOC_FIELD_IS",
      "field": "Invoice_Currency",
      "operator": "NOT EQUAL TO",
      "value": "EUR"
    },
    "get_rate": {
      "card": "CALL_API",
      "endpoint": "https://api.exchangerate.com/v1/rates/{{Invoice_Currency}}",
      "method": "GET",
      "response_path": "rates.EUR"
    },
    "convert": {
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Amount}} * {{Exchange_Rate}}",
      "result_field": "Amount_EUR"
    },
    "store_details": {
      "original_currency": "{{Invoice_Currency}}",
      "original_amount": "{{Amount}}",
      "exchange_rate": "{{Exchange_Rate}}",
      "converted_amount": "{{Amount_EUR}}",
      "conversion_date": "{{Today}}"
    }
  }
}
```

---

## Gestión de errores

### Errores comunes de transformación

**Error 1: División por cero**
```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**Error 2: Formato de número no válido**
```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**Error 3: Fallo al analizar la fecha**
```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**Error 4: Falta el factor de conversión**
```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

---

## Lista de comprobación para pruebas

- [ ] Todos los cálculos producen resultados correctos
- [ ] Se mantiene la precisión decimal
- [ ] Las conversiones de divisas son precisas
- [ ] Los cálculos de fechas son correctos
- [ ] Las transformaciones de texto funcionan
- [ ] Los valores nulos/vacíos se gestionan
- [ ] Se evita la división por cero
- [ ] Los formatos de número se validan
- [ ] Las reglas de redondeo se aplican correctamente
- [ ] Todos los campos transformados se rellenan
- [ ] La validación detecta los errores
- [ ] El formato de exportación es correcto

---

## Patrones relacionados

### Patrones que funcionan bien juntos:

- **[Patrón de integración de API](api-integration-pattern.md)** - Obtiene tipos de cambio y datos de enriquecimiento
- **[Patrón de cotejo de PO](po-matching-pattern.md)** - Cálculos de desviación
- **[Patrón de lógica de decisión](decision-logic-pattern.md)** - Enruta según los valores calculados
- **[Patrón de gestión de tareas](task-management-pattern.md)** - Crea tareas para los fallos de validación

---

## Guías relacionadas

### Requisitos previos
- [Guía de manipulación de campos](../then/document-field/field-manipulation-guide.md) - Todas las operaciones con campos
- [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md) - Condiciones de validación
- [Guía de Call API](../then/action/call-api-guide.md) - Obtención de datos externos

### Tarjetas relacionadas
- **ACTION_CALCULATE_FIELD** - [Guía de manipulación de campos](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** - [Guía de manipulación de campos](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** - [Guía de manipulación de campos](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** - [Guía de Call API](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Guía de tarjetas de condición](../and/condition-cards-complete-guide.md)

### Próximos pasos
- Validar los resultados: [Patrón de lógica de decisión](decision-logic-pattern.md)
- Crear tareas para errores: [Patrón de gestión de tareas](task-management-pattern.md)
- Usar en el cotejo de PO: [Patrón de cotejo de PO](po-matching-pattern.md)

---

**Versión del patrón:** 1.0
**Última actualización:** 23 de octubre de 2025
**Dificultad:** Media
**Tiempo estimado:** 30-45 minutos
**Tasa de éxito:** Alta
