# Tarjetas de manipulación de campos y tablas

## Tarjetas de manipulación de campo y tabla: guía completa

**Cubiertas:** 9 tarjetas para modificar campos y tablas del documento

***

Las tarjetas de campo y tabla en esta página van en el grupo **Entonces** del Generador de flujo de trabajo: las acciones que se ejecutan una vez que coinciden las condiciones Cuándo/Y:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-es.png" alt="Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos."><figcaption><p>Ejemplo sin guardar con tarjetas Cuando, Y y Entonces. Configure todos los campos antes de ejecutarlo. Algunas etiquetas de esta versión de la tarjeta todavía tienen una traducción incompleta o incorrecta en la interfaz. Las explicaciones de esta página utilizan los términos correctos.</p></figcaption></figure>

***

### 📌 Información de versión

**Tarjetas multiversión:** CALC\_COLUMNS (v2), CALC\_COLUMNS\_REGEX (v2), EDIT\_COLUMN (v2), AI\_CALC\_MTZ\_ETZ (v2)

**Patrón de versión:** Todas las tarjetas de manipulación de campo siguen el patrón v1 → v2 **Cambio de clave:** v2 agrega soporte de internacionalización (i18n) con claves de traducción

📖 [Historial de versiones completo](../../release.md) | [Versiones de tarjetas y comportamiento](../../cards-overview/card-versions-guide.md)

***

## Manipulación del campo del documento

### Tarjeta: ACTION\_SET\_FIELD\_TO\_TEXT / Establecer campo en valor de texto

#### Propósito

Rellena automáticamente un campo de documento con texto específico

#### Cuando usar

* Rellenar el campo a partir de la decisión
* Establecer valores predeterminados
* Complete la información estandarizada
* Actualizar campo según las condiciones

#### Cómo funciona

```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

#### Escenarios de ejemplo

**Escenario 1: Establecer categoría de aprobación**

```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Escenario 2: Establecer categoría de proveedor**

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

#### Parámetros

**Nombre de campo** Qué campo actualizar

```
Examples: Category, Type, Status, Comment, Notes
```

**Valor de texto** Qué poner en el campo

```
Examples: "Approved", "Pending Review", "High Priority"
```

#### Pasos de configuración

1. Elige el campo a llenar
2. Introduzca el valor del texto
3. Establecer condiciones (cuándo llenar)
4. Guardar

***

### Tarjeta: ACTION\_SET\_BOOLEAN\_FIELD / Establecer campo de casilla de verificación

#### Propósito

Marca o desmarca automáticamente un campo de casilla de verificación

#### Cuando usar

* Marcar como procesado
* Establecer indicadores de aprobación
* Activar/desactivar opciones
* Marcar para exportar

#### Cómo funciona

```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

#### Verdadero = marcado, falso = sin marcar

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

**Ejemplo 3: Desmarque la casilla Precompletada**

```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

#### Parámetros

```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

***

### Tarjeta: ACTION\_INVERT\_BOOLEAN\_FIELD / Alternar casilla de verificación

#### Propósito

Invierte el estado de la casilla de verificación (marcado → desmarcado, viceversa)

#### Cuando usar

* Alternar estado de aprobación
* Cambiar modo de procesamiento
* Invertir estado anterior
* Actualizar indicadores booleanos

#### Cómo funciona

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

#### Ejemplo

```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

***

### Tarjeta: ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD / Copiar valor de campo

#### Propósito

Copia el valor de un campo a otro campo

#### Cuando usar

* Copiar la información del proveedor a la información de facturación
* Duplicar datos en todos los campos
* Estandarizar el formato de datos
* Crear respaldo de valor

#### Cómo funciona

```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

#### Ejemplos reales

**Ejemplo 1: Copiar dirección de entrega**

```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Ejemplo 2: Copiar código de proveedor**

```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Ejemplo 3: Copiar monto para validación**

```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

#### Parámetros

```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

#### Notas

* Campo original sin cambios
* Campo de destino sobrescrito con valor de origen
* Bueno para estandarizar datos

***

## Manipulación de tablas

### Tarjeta: EDIT\_COLUMN / Editar columna de tabla

#### Propósito

Cambia los valores en una columna de la tabla según las condiciones.

#### Cuando usar

* Corregir errores de precios en líneas de pedido
* Actualizar cantidades
* Descripciones correctas de los artículos.
* Estandarizar valores

#### Cómo funciona

```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

#### Ejemplo: fijar precios

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

#### Parámetros

```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

#### Usos comunes

* Fijar precios unitarios
* Estandarizar descripciones
* Cantidades correctas
* Actualizar números SKU

***

### Tarjeta: CALC\_COLUMNS / Calcular valores de columna

#### Propósito

Realiza cálculos en las columnas de la tabla y almacena el resultado.

#### Cuando usar

* Calcular totales de línea (Cantidad × Precio unitario)
* Columnas de suma
* Calcular descuentos
* Calcular porcentajes

#### Cómo funciona

```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

#### Tipos de cálculo

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

#### Ejemplo del mundo real

**Cálculo de partidas individuales de factura:**

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

#### Parámetros

```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

***

### Tarjeta: CALC\_COLUMNS\_REGEX / Calcular con patrón Regex

#### Propósito

Calcula los valores de las columnas basándose en la coincidencia de patrones.

#### Cuando usar

* Extraer valores del texto usando patrones
* Formatear datos según reglas
* Convertir valores basados en patrones
* Analizar texto estructurado

#### Cómo funciona

**Coincidencia de patrones Regex:**

```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

#### Ejemplo: extraer código de proveedor

**Escenario: los números de artículo contienen información del proveedor**

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

#### Ejemplo: formatear números de teléfono

**Escenario: Números de teléfono sin formato**

```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

#### Ejemplo: extraer precios del texto

**Escenario: Precios en formato texto**

```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

#### Parámetros

```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

#### Patrones de expresiones regulares comunes

```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

***

## Ejemplos de cálculo

### Ejemplo 1: Cálculo del total de la factura

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

### Ejemplo 2: Cálculo de la varianza

```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

### Ejemplo 3: Solicitud de descuento

```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

***

## Ejemplo de flujo de trabajo de manipulación de campo

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

***

## Mejores prácticas

✅ **Hacer:**

* Mantenga las fórmulas simples
* Cálculos de prueba con datos de muestra.
* Verificar que los resultados tengan sentido
* Documente por qué está cambiando los campos
* Utilice el campo de copia cuando los datos sean los mismos

❌ **No:**

* Crear referencias circulares (A=B, B=A)
* Sobrescribir datos importantes sin motivo
* Crear patrones de expresiones regulares demasiado complejos
* Olvídese de verificar los resultados del cálculo
* Calcular en tablas/columnas incorrectas

***

## Solución de problemas

### "El campo no se actualiza"

**Causa:** Condición no cumplida o tarjeta no activada

**Solución:**

* La condición de verificación es verdadera
* Verificar que la tarjeta esté en el flujo de trabajo
* Prueba con datos de muestra
* Compruebe si hay errores tipográficos en el nombre del campo

### "Resultado del cálculo incorrecto"

**Causa:** Se seleccionaron columnas incorrectas o fórmula incorrecta

**Solución:**

* Verificar columnas de origen
* Compruebe que la fórmula sea correcta
* Probar manualmente
* Revisar decimales/redondeo

### "La tabla muestra un error"

**Causa:** La columna referenciada no existe

**Solución:**

* Verificar la ortografía del nombre de la columna
* Verificar que la columna tenga datos
* Asegúrese de que el tipo de datos de la columna coincida con el cálculo
* Agregue las columnas que faltan si es necesario

***

## Tarjetas relacionadas

* **ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD** - Copiar valores
* **EDIT\_COLUMN** - Cambiar valores de tabla
* **CALC\_COLUMNS** - Calcular fórmulas
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Establecer valores de texto
* **ACTION\_SET\_BOOLEAN\_FIELD** - Casillas de verificación
