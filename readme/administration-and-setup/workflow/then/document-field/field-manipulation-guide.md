# Schede per la modifica di campi e tabelle

## Carte di manipolazione del campo e della tabella - Guida completa

**Copertine:** 9 schede per modificare campi e tabelle del documento

***

Le schede del campo e della tabella in questa pagina vanno nel gruppo **Allora** del Workflow Builder: le azioni che vengono eseguite una volta che le condizioni Quando/E corrispondono:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-it.png" alt="Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

***

### 📌 Informazioni sulla versione

**Carte multiversione:** CALC\_COLUMNS (v2), CALC\_COLUMNS\_REGEX (v2), EDIT\_COLUMN (v2), AI\_CALC\_MTZ\_ETZ (v2)

**Modello versione:** Tutte le schede di manipolazione dei campi seguono il modello v1 → v2 **Modifica chiave:** v2 aggiunge il supporto per l'internazionalizzazione (i18n) con chiavi di traduzione

📖 [Cronologia completa delle versioni](../../release.md) | [Versioni e comportamento delle carte](../../cards-overview/card-versions-guide.md)

***

## Manipolazione del campo del documento

### Scheda: ACTION\_SET\_FIELD\_TO\_TEXT / Imposta il campo sul valore del testo

#### Scopo

Riempie automaticamente un campo del documento con testo specifico

#### Quando usarlo

* Compilare il campo dalla decisione
* Imposta i valori predefiniti
* Compila le informazioni standardizzate
* Aggiorna il campo in base alle condizioni

#### Come funziona

```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

#### Scenari di esempio

**Scenario 1: imposta la categoria di approvazione**

```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scenario 2: Imposta categoria fornitore**

```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scenario 3: imposta le note di elaborazione**

```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

#### Parametri

**Nome campo** Quale campo aggiornare

```
Examples: Category, Type, Status, Comment, Notes
```

**Valore testo** Cosa mettere nel campo

```
Examples: "Approved", "Pending Review", "High Priority"
```

#### Passaggi di configurazione

1. Scegli il campo da compilare
2. Immettere il valore del testo
3. Imposta le condizioni (quando riempire)
4. Salva

***

### Scheda: ACTION\_SET\_BOOLEAN\_FIELD / Imposta campo casella di controllo

#### Scopo

Seleziona o deseleziona automaticamente un campo di casella di controllo

#### Quando usarlo

* Contrassegna come elaborato
* Imposta i flag di approvazione
* Abilita/disabilita le opzioni
* Contrassegna per l'esportazione

#### Come funziona

```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

#### Vero = Selezionato, Falso = Non selezionato

**Esempi:**

**Esempio 1: contrassegna come verificato**

```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Esempio 2: Flag per revisione manuale**

```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Esempio 3: deseleziona la casella precompilata**

```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

#### Parametri

```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

***

### Carta: ACTION\_INVERT\_BOOLEAN\_FIELD / Attiva/disattiva casella di controllo

#### Scopo

Inverte lo stato della casella di controllo (selezionato → deselezionato, viceversa)

#### Quando usarlo

* Attiva/disattiva lo stato di approvazione
* Cambia modalità di elaborazione
* Invertire lo stato precedente
* Aggiorna i flag booleani

#### Come funziona

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

#### Esempio

```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

***

### Carta: ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD / Copia valore del campo

#### Scopo

Copia il valore da un campo a un altro campo

#### Quando usarlo

* Copia le informazioni del fornitore nelle informazioni di fatturazione
* Duplicare i dati tra i campi
* Standardizzare il formato dei dati
* Creare backup di valore

#### Come funziona

```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

#### Esempi reali

**Esempio 1: Copia indirizzo di consegna**

```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Esempio 2: Copia Codice Fornitore**

```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Esempio 3: importo della copia per la convalida**

```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

#### Parametri

```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

#### Note

* Campo originale invariato
* Campo di destinazione sovrascritto con il valore di origine
* Utile per standardizzare i dati

***

## Manipolazione della tabella

### Scheda: EDIT\_COLUMN / Modifica colonna tabella

#### Scopo

Modifica i valori in una colonna della tabella in base alle condizioni

#### Quando usarlo

* Correggi gli errori di prezzo nele righe del documento
* Aggiorna quantità
* Descrizioni degli articoli corrette
* Standardizzare i valori

#### Come funziona

```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

#### Esempio: fissare i prezzi

**Scenario: prezzi nella valuta sbagliata**

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

#### Parametri

```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

#### Usi comuni

* Fissare i prezzi unitari
* Standardizzare le descrizioni
* Quantità corrette
* Aggiorna i numeri SKU

***

### Scheda: CALC\_COLUMNS / Calcola i valori delle colonne

#### Scopo

Esegue il calcolo sulle colonne della tabella e memorizza il risultato

#### Quando usarlo

* Calcola i totali delle righe (Qtà × Prezzo unitario)
* Colonne di somma
* Calcola sconti
* Calcolare le percentuali

#### Come funziona

```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

#### Tipi di calcolo

**Tipo 1: Moltiplicazione semplice**

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

**Tipo 2: addizione**

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

**Tipo 3: Calcolo percentuale**

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

#### Esempio del mondo reale

**Calcolo delle voci della fattura:**

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

#### Parametri

```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

***

### Scheda: CALC\_COLUMNS\_REGEX / Calcola con Regex Pattern

#### Scopo

Calcola i valori delle colonne in base alla corrispondenza dei modelli

#### Quando usarlo

* Estrai valori dal testo utilizzando modelli
* Formattare i dati in base alle regole
* Converti valori in base a modelli
* Analizzare il testo strutturato

#### Come funziona

**Corrispondenza modello Regex:**

```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

#### Esempio: Estrai Codice Fornitore

**Scenario: i numeri degli articoli contengono informazioni sul fornitore**

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

#### Esempio: formattare i numeri di telefono

**Scenario: numeri di telefono non formattati**

```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

#### Esempio: estrai i prezzi dal testo

**Scenario: prezzi in formato testo**

```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

#### Parametri

```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

#### Modelli Regex comuni

```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

***

## Esempi di calcolo

### Esempio 1: calcolo del totale della fattura

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

### Esempio 2: calcolo della varianza

```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

### Esempio 3: Applicazione dello sconto

```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

***

## Esempio di flusso di lavoro di manipolazione dei campi

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

## Migliori pratiche

✅ **Fai:**

* Mantieni le formule semplici
* Testare i calcoli con dati campione
* Verificare che i risultati abbiano senso
* Documenta il motivo per cui stai modificando i campi
* Utilizza il campo copia quando i dati sono gli stessi

❌ **Non farlo:**

* Crea riferimenti circolari (A=B, B=A)
* Sovrascrivi dati importanti senza motivo
* Creare modelli regex eccessivamente complessi
* Dimentica di verificare i risultati del calcolo
* Calcola su tabella/colonne sbagliate

***

## Risoluzione dei problemi

### "Campo non aggiornato"

**Causa:** Condizione non soddisfatta o carta non attivata

**Soluzione:**

* La condizione di controllo è vera
* Verifica che la carta sia nel flusso di lavoro
* Testare con dati campione
* Verificare la presenza di errori di battitura nel nome del campo

### "Risultato del calcolo errato"

**Causa:** Colonne selezionate errate o formula errata

**Soluzione:**

* Verifica le colonne di origine
* La formula di controllo è corretta
* Prova manualmente
* Revisione delle cifre decimali/arrotondamenti

### "La tabella mostra un errore"

**Causa:** La colonna referenziata non esiste

**Soluzione:**

* Verificare l'ortografia del nome della colonna
* Controlla che la colonna contenga dati
* Assicurarsi che il tipo di dati della colonna corrisponda al calcolo
* Aggiungi le colonne mancanti se necessario

***

## Carte correlate

* **ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD** - Copia valori
* **EDIT\_COLUMN** - Modifica i valori della tabella
* **CALC\_COLUMNS** - Calcola le formule
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Imposta valori di testo
* **ACTION\_SET\_BOOLEAN\_FIELD** - Caselle di controllo
