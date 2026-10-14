# Purchase Order (PO) Matching Cards - Complete Guide

Le schede di abbinamento ordini di questa pagina vanno nel gruppo **And** del Generatore di workflow — confrontano i dati della fattura con l'ordine abbinato prima dell'esecuzione delle azioni Then:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede di abbinamento ordini vengono aggiunte al gruppo <strong>And</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
DocBits PO Matching Tutorial: Auto/Manual Line Matching, Tolerances & Mismatch Indicators
{% endembed %}

**Stato:** copre 15 card di confronto PO con calcoli dettagliati

---

## 📌 Informazioni sulla Versione

**Card Più Evoluta:** CONDITION_DOC_TO_PO_UNIT_PRICE (5 versioni, v5 la più recente)
**Altre Card Complesse:** CONDITION_OC_TO_PO_ITEMS (v4), CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v4)

**Schemi Principali:**
- **v2 → v3+:** aggiunta dei parametri di tolleranza per un abbinamento flessibile
- **v3 → v4:** aggiunta dei parametri di modalità di confronto
- **v4 → v5:** tolleranza potenziata con più unità (%, EUR, $, ecc.)

📖 [Cronologia Completa delle Versioni](../../../changelog/release.md#-po-comparison--validation-cards) | [Database delle Versioni delle Card](../../../../DocFlow/docs/card_version.md)

---

## Comprendere il PO Matching

Quando ricevi una fattura, questa dovrebbe corrispondere all'ordine di acquisto (PO) emesso in precedenza. Le card di PO matching verificano automaticamente se i dati della fattura corrispondono ai dati del PO.

**Il Quadro Generale:**
```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

---

# 1. Purchase Order Full Match

## Scopo
Verifica se l'intera fattura corrisponde perfettamente al PO o entro la tolleranza

## Quando Usarla
- Prima di approvare una fattura
- Come controllo qualità preliminare
- Per individuare i problemi in anticipo

## Come Funziona
Il sistema confronta:
- Quantità della fattura vs quantità del PO
- Prezzi della fattura vs prezzi del PO
- Articoli della fattura vs articoli del PO
- Totale della fattura vs totale del PO

## Risultato
- **TRUE** (Full Match): tutto corrisponde, procedi
- **FALSE** (Mismatch): qualcosa non corrisponde, richiede revisione

## Esempio
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

# 2. Confronto del Prezzo Unitario (Document vs PO)

## Scopo
Confronta il prezzo unitario sulla fattura con il prezzo unitario sul PO

## Parametri
- **Unit Price Tolerance**: consente una varianza fino a questo importo
- **Tolerance Type**: percentuale (%) o assoluta (€/$)
- **Operator**: Is Equal to, Is Greater than, Is Less than, ecc.

## Come Funziona (Tolleranza Percentuale)

**Formula:**
```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Esempio Passo dopo Passo:**
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

## Esempi Reali

### Esempio 1: Piccolo Aumento (Accettato)
```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

### Esempio 2: Grande Aumento (Rifiutato)
```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

### Esempio 3: Sconto (Anch'esso Verificato)
```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

### Esempio 4: Tolleranza con Valore Assoluto
```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

## Cosa Fare con i Risultati

**Se PASS ✅:**
- Prosegui al controllo successivo
- Oppure approva la fattura
- Oppure procedi con l'esportazione

**Se FAIL ❌:**
- Contrassegna per la revisione manuale
- Chiedi al fornitore una spiegazione
- Contatta il team di approvvigionamento
- Approva con una nota se accettabile

---

# 3. Confronto della Quantità

## Scopo
Verifica se la quantità ordinata corrisponde alla quantità fatturata

## Parametri
- **Tolerance**: importo o % di differenza consentita
- **Operator**: Equals, Greater than, Less than
- **Quantity Type**: Ordered, Received, Open

## Esempio di Calcolo

**Tolleranza Percentuale:**
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

**Tolleranza Assoluta:**
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

## Scenari Reali

### Consegna in Eccesso (Più del Quantitativo Ordinato)
```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

### Consegna in Difetto (Meno del Quantitativo Ordinato)
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

# 4. Prezzo Combinato della Differenza di Quantità

## Scopo
Quando la quantità differisce, calcola se la differenza di prezzo totale è accettabile

## Perché è Importante
```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

## Calcolo

**Formula:**
```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Esempio:**
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

# 5. Confronto Item ID / Numero Articolo del Fornitore

## Scopo
Verifica se gli articoli nella fattura corrispondono agli articoli nel PO

## Come Funziona

**Corrispondenza Esatta (Più Semplice):**
```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Numero Articolo del Fornitore (Più Comune):**
```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

## Scenario: Cosa Succede se Non Corrispondono?

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

# 6. Verifica del Tipo di Ordine

## Scopo
Verifica che il tipo di ordine di acquisto sia corretto

## Tipi di Ordine
- **Standard Order**: acquisto regolare
- **Rush Order**: urgente, può prevedere un sovrapprezzo
- **Frame Agreement**: contratto a lungo termine
- **Blanket Order**: contratto aperto
- **Consignment**: paghi solo quando viene utilizzato

## Esempio di Verifica
```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

---

# 7. Verifica della Data di Consegna

## Scopo
Verifica se la data di consegna corrisponde alla data promessa sul PO

## Calcolo

**Consegna in Ritardo:**
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

**Consegna Anticipata:**
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

## Impostazioni della Tolleranza
```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

---

# 8. Verifica degli Oneri (Imposte, Spedizione, Ecc.)

## Scopo
Verifica se gli oneri aggiuntivi (imposte, spedizione, gestione) corrispondono al PO

## Oneri Comuni
```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

## Calcolo

**Esempio: Verifica dell'Onere di Spedizione**
```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Esempio: Oneri Multipli**
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

# 9. Verifica delle Imposte

## Scopo
Verifica che gli importi delle imposte siano calcolati correttamente

## Calcolo

**Formula:**
```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Problemi Comuni:**
```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Esempio: Imposizione a Più Aliquote**
```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

---

# 10. Abbinamento Sede/Centro di Costo

## Scopo
Garantisce che la fattura sia per la sede/centro di costo corretti

## Esempio
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

# 11. Convalida dello Stato del Fornitore

## Scopo
Verifica se il fornitore è ancora approvato/attivo

## Tipi di Stato
```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

## Esempio di Verifica
```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

---

# Quale Tolleranza Dovrei Usare?

## Tolleranze Rigorose (Rischio Inferiore, Più Lavoro Manuale)
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

## Tolleranze Moderate (Bilanciate)
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

## Tolleranze Ampie (Rischio Superiore, Meno Lavoro Manuale)
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

# Esempio di Workflow di PO Matching

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

# Risoluzione dei Problemi del PO Matching

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

# Tabella di Riepilogo

| Card | Cosa Verifica | Calcolo Principale | Tolleranza Comune |
|------|----------------|------------------|-----------------|
| Full Match | Everything | All checks | Varies |
| Unit Price | Price per unit | % or € difference | ±3-5% |
| Quantity | Amount ordered | % or unit difference | ±3-5% |
| Combined Price | Total with qty change | Qty × Price | ±5-10% |
| Item ID | Right items | String match | Exact |
| Order Type | Type of purchase | String match | Exact |
| Delivery Date | When arrived | Day difference | ±3 days |
| Charges | Extra fees | % or € difference | ±5% |
| Tax | Tax amount | Tax % calculation | ±1% |
| Facility | Cost center | String match | Exact |
| Supplier | Approved? | Status check | Active only |

---

# Documentazione Correlata

- Consulta la guida "Invoice Validation" per il workflow completo
- Consulta "Tolerance Settings" per i valori consigliati per settore
- Consulta "Exception Handling" per cosa fare in caso di errori
- Contatta il tuo team di approvvigionamento per le politiche di tolleranza specifiche
