# Field & Table Manipulation Cards - Complete Guide

Queste schede vanno nel gruppo **Then** del Generatore di workflow — le azioni eseguite una volta soddisfatte le condizioni When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede vengono aggiunte al gruppo <strong>Then</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

**Copre:** 9 card per modificare campi e tabelle del documento

---

# Manipolazione dei Campi del Documento

## Card: ACTION_SET_FIELD_TO_TEXT / Set Field to Text Value

### Scopo
Compila automaticamente un campo del documento con un testo specifico

### Quando Usarla
- Popolare un campo a partire da una decisione
- Impostare valori predefiniti
- Inserire informazioni standardizzate
- Aggiornare un campo in base alle condizioni

### Come Funziona
```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

### Scenari di Esempio

**Scenario 1: Impostare la Categoria di Approvazione**
```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scenario 2: Impostare la Categoria del Fornitore**
```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scenario 3: Impostare le Note di Elaborazione**
```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

### Parametri

**Field Name**
Quale campo aggiornare
```
Examples: Category, Type, Status, Comment, Notes
```

**Text Value**
Cosa inserire nel campo
```
Examples: "Approved", "Pending Review", "High Priority"
```

### Passaggi di Configurazione
1. Scegli il campo da compilare
2. Inserisci il valore di testo
3. Imposta le condizioni (quando compilare)
4. Salva

---

## Card: ACTION_SET_BOOLEAN_FIELD / Set Checkbox Field

### Scopo
Seleziona o deseleziona automaticamente un campo checkbox

### Quando Usarla
- Contrassegnare come elaborato
- Impostare flag di approvazione
- Abilitare/disabilitare opzioni
- Contrassegnare per l'esportazione

### Come Funziona
```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

### True = Selezionata, False = Deselezionata

**Esempi:**

**Esempio 1: Contrassegnare come Verificato**
```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Esempio 2: Contrassegnare per la Revisione Manuale**
```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Esempio 3: Deselezionare una Casella Precompilata**
```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

### Parametri
```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

---

## Card: ACTION_INVERT_BOOLEAN_FIELD / Toggle Checkbox

### Scopo
Inverte lo stato della checkbox (selezionata → deselezionata e viceversa)

### Quando Usarla
- Invertire lo stato di approvazione
- Cambiare modalità di elaborazione
- Invertire lo stato precedente
- Aggiornare flag booleani

### Come Funziona
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

### Esempio
```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

---

## Card: ACTION_COPY_DOCFIELD_TO_DOCFIELD / Copy Field Value

### Scopo
Copia il valore da un campo a un altro campo

### Quando Usarla
- Copiare le informazioni del fornitore nelle informazioni di fatturazione
- Duplicare i dati tra i campi
- Standardizzare il formato dei dati
- Creare un backup del valore

### Come Funziona
```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

### Esempi Reali

**Esempio 1: Copiare l'Indirizzo di Consegna**
```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Esempio 2: Copiare il Codice Fornitore**
```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Esempio 3: Copiare l'Importo per la Convalida**
```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

### Parametri
```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

### Note
- Il campo di origine rimane invariato
- Il campo di destinazione viene sovrascritto con il valore di origine
- Utile per standardizzare i dati

---

# Manipolazione delle Tabelle

## Card: EDIT_COLUMN / Edit Table Column

### Scopo
Modifica i valori in una colonna della tabella in base alle condizioni

### Quando Usarla
- Correggere errori di prezzo nelle voci
- Aggiornare le quantità
- Correggere le descrizioni degli articoli
- Standardizzare i valori

### Come Funziona
```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

### Esempio: Correggere i Prezzi

**Scenario: Prezzi nella valuta errata**
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

### Parametri
```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

### Usi Comuni
- Correggere i prezzi unitari
- Standardizzare le descrizioni
- Correggere le quantità
- Aggiornare i numeri SKU

---

## Card: CALC_COLUMNS / Calculate Column Values

### Scopo
Esegue un calcolo sulle colonne della tabella e ne memorizza il risultato

### Quando Usarla
- Calcolare i totali di riga (Qty × Unit Price)
- Sommare le colonne
- Calcolare gli sconti
- Calcolare le percentuali

### Come Funziona
```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

### Tipi di Calcolo

**Tipo 1: Moltiplicazione Semplice**
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

**Tipo 2: Addizione**
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

**Tipo 3: Calcolo Percentuale**
```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Tipo 4: Sottrazione**
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

### Esempio Reale

**Calcolo delle Voci della Fattura:**
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

### Parametri
```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

---

## Card: CALC_COLUMNS_REGEX / Calculate with Regex Pattern

### Scopo
Calcola i valori delle colonne in base alla corrispondenza di pattern

### Quando Usarla
- Estrarre valori dal testo usando pattern
- Formattare i dati in base a regole
- Convertire i valori in base ai pattern
- Analizzare testo strutturato

### Come Funziona

**Corrispondenza di Pattern Regex:**
```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

### Esempio: Estrarre il Codice Fornitore

**Scenario: I numeri di articolo contengono informazioni sul fornitore**
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

### Esempio: Formattare i Numeri di Telefono

**Scenario: Numeri di telefono non formattati**
```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

### Esempio: Estrarre i Prezzi dal Testo

**Scenario: Prezzi in formato testo**
```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

### Parametri
```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

### Pattern Regex Comuni
```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

---

# Esempi di Calcolo

## Esempio 1: Calcolo del Totale della Fattura
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

## Esempio 2: Calcolo della Varianza
```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

## Esempio 3: Applicazione dello Sconto
```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

---

# Esempio di Workflow di Manipolazione dei Campi

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

# Best Practice

✅ **Fai:**
- Mantieni le formule semplici
- Testa i calcoli con dati di esempio
- Verifica che i risultati abbiano senso
- Documenta perché stai modificando i campi
- Usa la copia del campo quando i dati sono identici

❌ **Non Fare:**
- Creare riferimenti circolari (A=B, B=A)
- Sovrascrivere dati importanti senza motivo
- Creare pattern regex eccessivamente complessi
- Dimenticare di verificare i risultati del calcolo
- Calcolare su tabelle/colonne errate

---

# Risoluzione dei Problemi

## "Field not updating"
**Causa:** condizione non soddisfatta o card non attivata

**Soluzione:**
- Verifica che la condizione sia vera
- Verifica che la card sia nel workflow
- Testa con dati di esempio
- Controlla eventuali errori di battitura nel nome del campo

## "Calculation result wrong"
**Causa:** colonne errate selezionate o formula errata

**Soluzione:**
- Verifica le colonne di origine
- Controlla che la formula sia corretta
- Testa manualmente
- Rivedi i decimali/l'arrotondamento

## "Table shows error"
**Causa:** la colonna a cui si fa riferimento non esiste

**Soluzione:**
- Verifica l'ortografia del nome della colonna
- Controlla che la colonna contenga dati
- Assicurati che il tipo di dati della colonna corrisponda al calcolo
- Aggiungi le colonne mancanti se necessario

---

# Card Correlate

- **ACTION_COPY_DOCFIELD_TO_DOCFIELD** - Copia i valori
- **EDIT_COLUMN** - Modifica i valori della tabella
- **CALC_COLUMNS** - Calcola le formule
- **ACTION_SET_FIELD_TO_TEXT** - Imposta valori di testo
- **ACTION_SET_BOOLEAN_FIELD** - Seleziona le caselle
