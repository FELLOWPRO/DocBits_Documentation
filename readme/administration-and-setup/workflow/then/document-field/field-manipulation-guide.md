# Kartice za manipulaciju poljima i tabelama - Kompletan vodič

**Pokriva:** 9 kartica za izmenu polja i tabela dokumenta

---

Kartice za polja i tabele na ovoj stranici idu u grupu **Then** u Workflow Builder-u — akcije koje se pokreću kada se When/And uslovi poklope:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Kartice za manipulaciju poljima i tabelama se dodaju u grupu <strong>Then</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Kartice sa više verzija:** CALC_COLUMNS (v2), CALC_COLUMNS_REGEX (v2), EDIT_COLUMN (v2), AI_CALC_MTZ_ETZ (v2)

**Obrazac verzija:** Sve kartice za manipulaciju poljima prate obrazac v1 → v2
**Ključna promena:** v2 dodaje podršku za internacionalizaciju (i18n) sa ključevima za prevod

📖 [Kompletna istorija verzija](../../../changelog/release.md#-data-manipulation-cards) | [Baza podataka verzija kartica](../../../../DocFlow/docs/card_version.md)

---

# Manipulacija poljima dokumenta

## Kartica: ACTION_SET_FIELD_TO_TEXT / Postavi polje na tekstualnu vrednost

### Svrha
Automatski popunjava polje dokumenta određenim tekstom

### Kada koristiti
- Popunjavanje polja na osnovu odluke
- Postavljanje podrazumevanih vrednosti
- Popunjavanje standardizovanih informacija
- Ažuriranje polja na osnovu uslova

### Kako funkcioniše
```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

### Primeri scenarija

**Scenario 1: Postavi kategoriju odobravanja**
```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scenario 2: Postavi kategoriju dobavljača**
```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scenario 3: Postavi napomene o obradi**
```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

### Parametri

**Field Name**
Koje polje ažurirati
```
Examples: Category, Type, Status, Comment, Notes
```

**Text Value**
Šta staviti u polje
```
Examples: "Approved", "Pending Review", "High Priority"
```

### Koraci konfiguracije
1. Izaberite polje za popunjavanje
2. Unesite tekstualnu vrednost
3. Postavite uslove (kada popuniti)
4. Sačuvajte

---

## Kartica: ACTION_SET_BOOLEAN_FIELD / Postavi polje za potvrdu

### Svrha
Automatski označava ili poništava polje za potvrdu

### Kada koristiti
- Označavanje kao obrađeno
- Postavljanje oznaka odobravanja
- Omogućavanje/onemogućavanje opcija
- Označavanje za izvoz

### Kako funkcioniše
```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

### True = Označeno, False = Neoznačeno

**Primeri:**

**Primer 1: Označi kao verifikovano**
```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Primer 2: Označi za ručni pregled**
```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Primer 3: Poništi unapred popunjeno polje**
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

## Kartica: ACTION_INVERT_BOOLEAN_FIELD / Prebaci polje za potvrdu

### Svrha
Menja stanje polja za potvrdu (označeno → neoznačeno, i obrnuto)

### Kada koristiti
- Prebacivanje statusa odobravanja
- Promena režima obrade
- Vraćanje prethodnog stanja
- Ažuriranje logičkih oznaka

### Kako funkcioniše
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

### Primer
```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

---

## Kartica: ACTION_COPY_DOCFIELD_TO_DOCFIELD / Kopiraj vrednost polja

### Svrha
Kopira vrednost iz jednog polja u drugo polje

### Kada koristiti
- Kopiranje informacija o dobavljaču u informacije o naplati
- Dupliranje podataka kroz polja
- Standardizacija formata podataka
- Kreiranje rezervne kopije vrednosti

### Kako funkcioniše
```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

### Stvarni primeri

**Primer 1: Kopiraj adresu isporuke**
```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Primer 2: Kopiraj kod dobavljača**
```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Primer 3: Kopiraj iznos za validaciju**
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

### Napomene
- Originalno polje ostaje nepromenjeno
- Ciljno polje se prepisuje vrednošću izvora
- Dobro za standardizaciju podataka

---

# Manipulacija tabelama

## Kartica: EDIT_COLUMN / Uredi kolonu tabele

### Svrha
Menja vrednosti u koloni tabele na osnovu uslova

### Kada koristiti
- Ispravljanje grešaka u cenama u stavkama
- Ažuriranje količina
- Ispravljanje opisa stavki
- Standardizacija vrednosti

### Kako funkcioniše
```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

### Primer: Ispravi cene

**Scenario: Cene u pogrešnoj valuti**
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

### Uobičajene upotrebe
- Ispravljanje jediničnih cena
- Standardizacija opisa
- Ispravljanje količina
- Ažuriranje SKU brojeva

---

## Kartica: CALC_COLUMNS / Izračunaj vrednosti kolona

### Svrha
Izvodi izračunavanje nad kolonama tabele i čuva rezultat

### Kada koristiti
- Izračunavanje ukupnih iznosa stavki (Količina × Jedinična cena)
- Sabiranje kolona
- Izračunavanje popusta
- Računanje procenata

### Kako funkcioniše
```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

### Tipovi izračunavanja

**Tip 1: Jednostavno množenje**
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

**Tip 2: Sabiranje**
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

**Tip 3: Procentualno izračunavanje**
```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Tip 4: Oduzimanje**
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

### Primer iz stvarnog sveta

**Izračunavanje stavki fakture:**
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

## Kartica: CALC_COLUMNS_REGEX / Izračunaj sa regex obrascem

### Svrha
Izračunava vrednosti kolone na osnovu poklapanja obrasca

### Kada koristiti
- Izvlačenje vrednosti iz teksta pomoću obrazaca
- Formatiranje podataka na osnovu pravila
- Konverzija vrednosti na osnovu obrazaca
- Parsiranje strukturiranog teksta

### Kako funkcioniše

**Poklapanje regex obrasca:**
```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

### Primer: Izvuci kod dobavljača

**Scenario: Brojevi artikala sadrže informacije o dobavljaču**
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

### Primer: Formatiraj brojeve telefona

**Scenario: Neformatirani brojevi telefona**
```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

### Primer: Izvuci cene iz teksta

**Scenario: Cene u tekstualnom formatu**
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

### Uobičajeni regex obrasci
```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

---

# Primeri izračunavanja

## Primer 1: Izračunavanje ukupnog iznosa fakture
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

## Primer 2: Izračunavanje odstupanja
```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

## Primer 3: Primena popusta
```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

---

# Primer toka rada za manipulaciju poljima

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

# Najbolje prakse

✅ **Radite:**
- Održavajte formule jednostavnim
- Testirajte izračunavanja sa uzorcima podataka
- Verifikujte da rezultati imaju smisla
- Dokumentujte zašto menjate polja
- Koristite kopiranje polja kada su podaci isti

❌ **Ne radite:**
- Ne kreirajte kružne reference (A=B, B=A)
- Ne prepisujte važne podatke bez razloga
- Ne kreirajte previše složene regex obrasce
- Ne zaboravljajte da verifikujete rezultate izračunavanja
- Ne izračunavajte na pogrešnoj tabeli/kolonama

---

# Rešavanje problema

## „Field not updating"
**Uzrok:** Uslov nije ispunjen ili kartica nije okinuta

**Rešenje:**
- Proverite da li je uslov istinit
- Verifikujte da je kartica u toku rada
- Testirajte sa uzorcima podataka
- Proverite greške u kucanju naziva polja

## „Calculation result wrong"
**Uzrok:** Izabrane pogrešne kolone ili formula nije ispravna

**Rešenje:**
- Verifikujte izvorne kolone
- Proverite da je formula ispravna
- Testirajte ručno
- Pregledajte decimalna mesta/zaokruživanje

## „Table shows error"
**Uzrok:** Referencirana kolona ne postoji

**Rešenje:**
- Verifikujte ispravnost naziva kolone
- Proverite da kolona ima podatke
- Obezbedite da tip podataka kolone odgovara izračunavanju
- Dodajte nedostajuće kolone ako je potrebno

---

# Povezane kartice

- **ACTION_COPY_DOCFIELD_TO_DOCFIELD** - Kopiraj vrednosti
- **EDIT_COLUMN** - Promeni vrednosti tabele
- **CALC_COLUMNS** - Izračunaj formule
- **ACTION_SET_FIELD_TO_TEXT** - Postavi tekstualne vrednosti
- **ACTION_SET_BOOLEAN_FIELD** - Označi polja za potvrdu
