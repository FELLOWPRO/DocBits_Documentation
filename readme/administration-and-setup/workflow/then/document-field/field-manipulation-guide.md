# Field & Table Manipulation Cards - Complete Guide

Estas tarjetas van en el grupo **Then** del Generador de flujos de trabajo: las acciones que se ejecutan cuando se cumplen las condiciones When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Las tarjetas se añaden al grupo <strong>Then</strong> mediante <strong>Add Card</strong>.</p></figcaption></figure>

**Cubre:** 9 tarjetas para modificar campos y tablas de documentos

---

## 📌 Información de versión

**Tarjetas con varias versiones:** CALC_COLUMNS (v2), CALC_COLUMNS_REGEX (v2), EDIT_COLUMN (v2), AI_CALC_MTZ_ETZ (v2)

**Patrón de versión:** Todas las tarjetas de manipulación de campos siguen el patrón v1 → v2
**Cambio clave:** v2 añade soporte de internacionalización (i18n) con claves de traducción

📖 [Complete Version History](../../../changelog/release.md#-data-manipulation-cards) | [Card Version Database](../../../../DocFlow/docs/card_version.md)

---

# Manipulación de campos de documento

## Tarjeta: ACTION_SET_FIELD_TO_TEXT / Set Field to Text Value

### Propósito
Rellena automáticamente un campo del documento con un texto específico

### Cuándo usar
- Rellenar un campo a partir de una decisión
- Establecer valores predeterminados
- Rellenar información estandarizada
- Actualizar un campo según condiciones

### Cómo funciona
```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

### Escenarios de ejemplo

**Escenario 1: Establecer la categoría de aprobación**
```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Escenario 2: Establecer la categoría del proveedor**
```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Escenario 3: Establecer notas de procesamiento**
```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

### Parámetros

**Field Name**
Qué campo actualizar
```
Examples: Category, Type, Status, Comment, Notes
```

**Text Value**
Qué poner en el campo
```
Examples: "Approved", "Pending Review", "High Priority"
```

### Pasos de configuración
1. Elija el campo que se va a rellenar
2. Introduzca el valor de texto
3. Establezca las condiciones (cuándo rellenarlo)
4. Guarde

---

## Tarjeta: ACTION_SET_BOOLEAN_FIELD / Set Checkbox Field

### Propósito
Marca o desmarca automáticamente un campo de casilla de verificación

### Cuándo usar
- Marcar como procesado
- Establecer indicadores de aprobación
- Habilitar/deshabilitar opciones
- Marcar para exportación

### Cómo funciona
```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

### True = Marcada, False = Sin marcar

**Ejemplos:**

**Ejemplo 1: Marcar como verificado**
```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Ejemplo 2: Marcar para revisión manual**
```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Ejemplo 3: Desmarcar una casilla pre-marcada**
```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

### Parámetros
```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

---

## Tarjeta: ACTION_INVERT_BOOLEAN_FIELD / Toggle Checkbox

### Propósito
Invierte el estado de la casilla (marcada → sin marcar, y viceversa)

### Cuándo usar
- Alternar el estado de aprobación
- Cambiar el modo de procesamiento
- Invertir el estado anterior
- Actualizar indicadores booleanos

### Cómo funciona
```
Current state: ✅ (Checked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ☐ (Unchecked)

OR

Current state: ☐ (Unchecked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ✅ (Checked)
```

### Ejemplo
```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

---

## Tarjeta: ACTION_COPY_DOCFIELD_TO_DOCFIELD / Copy Field Value

### Propósito
Copia el valor de un campo a otro campo

### Cuándo usar
- Copiar la información del proveedor a la información de facturación
- Duplicar datos entre campos
- Estandarizar el formato de los datos
- Crear una copia de seguridad de un valor

### Cómo funciona
```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

### Ejemplos reales

**Ejemplo 1: Copiar la dirección de entrega**
```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Ejemplo 2: Copiar el código del proveedor**
```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Ejemplo 3: Copiar el importe para validación**
```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

### Parámetros
```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

### Notas
- El campo original permanece sin cambios
- El campo de destino se sobrescribe con el valor de origen
- Útil para estandarizar datos

---

# Manipulación de tablas

## Tarjeta: EDIT_COLUMN / Edit Table Column

### Propósito
Cambia los valores de una columna de tabla según condiciones

### Cuándo usar
- Corregir errores de precios en las líneas
- Actualizar cantidades
- Corregir descripciones de artículos
- Estandarizar valores

### Cómo funciona
```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

### Ejemplo: Corregir precios

**Escenario: Precios en moneda incorrecta**
```
Table "Line_Items" with column "Price"

Current prices: [100, 100, 100] (in wrong currency)
    ↓
Condition: "If Price column equals 100"
    ↓
Action: Replace with 95 (corrected price)
    ↓
Result: [95, 95, 95] (prices corrected)
```

### Parámetros
```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

### Usos comunes
- Corregir precios unitarios
- Estandarizar descripciones
- Corregir cantidades
- Actualizar números de SKU

---

## Tarjeta: CALC_COLUMNS / Calculate Column Values

### Propósito
Realiza un cálculo sobre las columnas de la tabla y almacena el resultado

### Cuándo usar
- Calcular los totales de línea (Qty × Unit Price)
- Sumar columnas
- Calcular descuentos
- Calcular porcentajes

### Cómo funciona
```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

### Tipos de cálculo

**Tipo 1: Multiplicación simple**
```
Formula: Qty × Unit Price = Line Total

Example:
100 units × €50/unit = €5000

Config:
  Column 1: Quantity
  Operator: ×
  Column 2: Unit Price
  Result Column: Line Total
```

**Tipo 2: Suma**
```
Formula: Base Price + Shipping + Tax = Total

Example:
€5000 + €100 + €950 = €6050

Config:
  Column 1: Base Price
  Operator: +
  Column 2: Shipping
  Operator: +
  Column 3: Tax
  Result Column: Total
```

**Tipo 3: Cálculo de porcentaje**
```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Tipo 4: Resta**
```
Formula: Original Price - Discount = Final Price

Example:
€100 - €10 = €90

Config:
  Column 1: Original Price
  Operator: -
  Column 2: Discount
  Result Column: Final Price
```

### Ejemplo real

**Cálculo de las líneas de una factura:**
```
Table: Invoice_Lines

Row 1:
  Quantity: 100
  Unit Price: €25.00
  Calculate: 100 × €25.00 = €2500.00 (Line Total)

Row 2:
  Quantity: 50
  Unit Price: €40.00
  Calculate: 50 × €40.00 = €2000.00 (Line Total)

Row 3:
  Quantity: 200
  Unit Price: €10.00
  Calculate: 200 × €10.00 = €2000.00 (Line Total)

Subtotal: €6500.00 (sum of line totals)
Tax (19%): €1235.00
Shipping: €100.00
TOTAL: €7835.00
```

### Parámetros
```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

---

## Tarjeta: CALC_COLUMNS_REGEX / Calculate with Regex Pattern

### Propósito
Calcula los valores de columna según la coincidencia de patrones

### Cuándo usar
- Extraer valores de texto mediante patrones
- Dar formato a los datos según reglas
- Convertir valores según patrones
- Analizar texto estructurado

### Cómo funciona

**Coincidencia de patrones regex:**
```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

### Ejemplo: Extraer el código del proveedor

**Escenario: Los números de artículo contienen información del proveedor**
```
Table Column: "Article_Code"
Values: ["SUPP001-2025-A", "SUPP002-2025-B"]

Pattern: Extract supplier code (first 7 characters)
    ↓
Calculate: SUPP001, SUPP002
    ↓
Store in: "Supplier_Code" column

Result:
Article_Code: SUPP001-2025-A  →  Supplier_Code: SUPP001
Article_Code: SUPP002-2025-B  →  Supplier_Code: SUPP002
```

### Ejemplo: Dar formato a números de teléfono

**Escenario: Números de teléfono sin formato**
```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

### Ejemplo: Extraer precios de un texto

**Escenario: Precios en formato de texto**
```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

### Parámetros
```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

### Patrones regex comunes
```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

---

# Ejemplos de cálculo

## Ejemplo 1: Cálculo del total de una factura
```
Step 1: Calculate line totals
  Each row: Qty × Unit Price

Step 2: Sum all line totals
  Sum: €2500 + €2000 + €2000 = €6500

Step 3: Calculate tax
  Tax: €6500 × 0.19 = €1235

Step 4: Add shipping
  Final: €6500 + €1235 + €100 = €7835
```

## Ejemplo 2: Cálculo de variación
```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

## Ejemplo 3: Aplicación de descuento
```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

---

# Ejemplo de flujo de trabajo de manipulación de campos

```
Document arrives
    ↓
Check condition: "Amount > €5000?"
    ↓
YES → Set field "Category" = "High Value"
    ↓
Check condition: "Supplier is preferred?"
    ↓
YES → Check "FastTrack" checkbox
    ↓
Copy "Delivery_Address" to "Invoice_Address"
    ↓
In table: Calculate line totals (Qty × Price)
    ↓
In table: Calculate total with tax
    ↓
Document now has all calculated and populated fields
```

---

# Buenas prácticas

✅ **Haga:**
- Mantenga las fórmulas simples
- Pruebe los cálculos con datos de muestra
- Verifique que los resultados tengan sentido
- Documente por qué cambia los campos
- Use la copia de campo cuando los datos sean los mismos

❌ **No haga:**
- Crear referencias circulares (A=B, B=A)
- Sobrescribir datos importantes sin motivo
- Crear patrones regex demasiado complejos
- Olvidar verificar los resultados de los cálculos
- Calcular sobre la tabla/columnas incorrectas

---

# Resolución de problemas

## "Field not updating"
**Causa:** No se cumple la condición o la tarjeta no se activa

**Solución:**
- Compruebe que la condición es verdadera
- Verifique que la tarjeta está en el flujo de trabajo
- Pruebe con datos de muestra
- Compruebe si hay errores tipográficos en el nombre del campo

## "Calculation result wrong"
**Causa:** Columnas incorrectas seleccionadas o fórmula incorrecta

**Solución:**
- Verifique las columnas de origen
- Compruebe que la fórmula es correcta
- Pruebe manualmente
- Revise los decimales/el redondeo

## "Table shows error"
**Causa:** La columna referenciada no existe

**Solución:**
- Verifique la ortografía del nombre de la columna
- Compruebe que la columna tiene datos
- Asegúrese de que el tipo de datos de la columna coincide con el cálculo
- Añada las columnas que falten si es necesario

---

# Tarjetas relacionadas

- **ACTION_COPY_DOCFIELD_TO_DOCFIELD** - Copiar valores
- **EDIT_COLUMN** - Cambiar valores de tabla
- **CALC_COLUMNS** - Calcular fórmulas
- **ACTION_SET_FIELD_TO_TEXT** - Establecer valores de texto
- **ACTION_SET_BOOLEAN_FIELD** - Marcar casillas
