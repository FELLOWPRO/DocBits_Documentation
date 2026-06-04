# Kartice za uparivanje narudžbenica (PO) - Kompletan vodič

**Status:** Pokriva 15 kartica za poređenje PO sa detaljnim izračunavanjima

---

Kartice za poređenje PO na ovoj stranici idu u grupu **And** u Workflow Builder-u — one porede podatke fakture sa uparenom narudžbenicom pre nego što se Then akcije pokrenu:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Kartice za poređenje PO se dodaju u grupu <strong>And</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Najrazvijenija kartica:** CONDITION_DOC_TO_PO_UNIT_PRICE (5 verzija, v5 najnovija)
**Druge složene kartice:** CONDITION_OC_TO_PO_ITEMS (v4), CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v4)

**Ključni obrasci:**
- **v2 → v3+:** Dodavanje parametara tolerancije za fleksibilno uparivanje
- **v3 → v4:** Dodavanje parametara režima poređenja
- **v4 → v5:** Poboljšana tolerancija sa više jedinica (%, EUR, $, itd.)

📖 [Kompletna istorija verzija](../../../changelog/release.md#-po-comparison--validation-cards) | [Baza podataka verzija kartica](../../../../DocFlow/docs/card_version.md)

---

## Razumevanje uparivanja PO

Kada primite fakturu, ona treba da se poklapa sa narudžbenicom (PO) koja je ranije postavljena. Kartice za uparivanje PO automatski proveravaju da li se podaci fakture poklapaju sa podacima PO.

**Šira slika:**
```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

---

# 1. Potpuno uparivanje narudžbenice

## Svrha
Proverava da li se cela faktura savršeno poklapa sa PO ili unutar tolerancije

## Kada koristiti
- Pre odobravanja fakture
- Kao preliminarna provera kvaliteta
- Za rano identifikovanje problema

## Kako funkcioniše
Sistem poredi:
- Količine na fakturi vs količine na PO
- Cene na fakturi vs cene na PO
- Stavke fakture vs stavke PO
- Ukupan iznos fakture vs ukupan iznos PO

## Rezultat
- **TRUE** (Potpuno uparivanje): Sve se poklapa, nastavite
- **FALSE** (Neslaganje): Nešto se ne poklapa, potreban je pregled

## Primer
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

# 2. Poređenje jedinične cene (Dokument vs PO)

## Svrha
Poredi jediničnu cenu na fakturi sa jediničnom cenom na PO

## Parametri
- **Tolerancija jedinične cene**: Dozvolite odstupanje do ovog iznosa
- **Tip tolerancije**: Procenat (%) ili apsolutno (€/$)
- **Operator**: Is Equal to, Is Greater than, Is Less than, itd.

## Kako funkcioniše (Procentualna tolerancija)

**Formula:**
```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Primer korak po korak:**
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

## Primeri iz stvarnog sveta

### Primer 1: Malo povećanje (Prihvaćeno)
```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

### Primer 2: Veliko povećanje (Odbijeno)
```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

### Primer 3: Popust (Takođe proveren)
```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

### Primer 4: Tolerancija apsolutne vrednosti
```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

## Šta raditi sa rezultatima

**Ako PROLAZI ✅:**
- Nastavite na sledeću proveru
- Ili odobrite fakturu
- Ili nastavite sa izvozom

**Ako NE USPE ❌:**
- Označite za ručni pregled
- Pitajte dobavljača za objašnjenje
- Kontaktirajte tim za nabavku
- Odobrite uz napomenu ako je prihvatljivo

---

# 3. Poređenje količine

## Svrha
Proverava da li se naručena količina poklapa sa fakturisanom količinom

## Parametri
- **Tolerancija**: Iznos ili % dozvoljeno za odstupanje
- **Operator**: Equals, Greater than, Less than
- **Tip količine**: Ordered, Received, Open

## Primer izračunavanja

**Procentualna tolerancija:**
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

**Apsolutna tolerancija:**
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

## Scenariji iz stvarnog sveta

### Prekomerna isporuka (Više od naručenog)
```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

### Manjkava isporuka (Manje od naručenog)
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

# 4. Kombinovana cena razlike u količini

## Svrha
Kada se količina razlikuje, izračunava da li je ukupna razlika u ceni prihvatljiva

## Zašto je ovo važno
```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

## Izračunavanje

**Formula:**
```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Primer:**
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

# 5. Poređenje ID-a stavke / Broja stavke dobavljača

## Svrha
Proverava da li se stavke na fakturi poklapaju sa stavkama na PO

## Kako funkcioniše

**Tačno poklapanje (Najjednostavnije):**
```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Broj stavke dobavljača (Češće):**
```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

## Scenario: Šta ako se ne poklapa?

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

# 6. Verifikacija tipa narudžbine

## Svrha
Verifikuje da je tip narudžbenice ispravan

## Tipovi narudžbine
- **Standard Order**: Redovna kupovina
- **Rush Order**: Hitno, može imati premiju
- **Frame Agreement**: Dugoročni ugovor
- **Blanket Order**: Otvoreni ugovor
- **Consignment**: Ne plaćate dok ne iskoristite

## Primer provere
```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

---

# 7. Verifikacija datuma isporuke

## Svrha
Proverava da li se datum isporuke poklapa sa obećanim datumom na PO

## Izračunavanje

**Zakasnela isporuka:**
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

**Rana isporuka:**
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

## Podešavanja tolerancije
```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

---

# 8. Verifikacija troškova (Porezi, dostava, itd.)

## Svrha
Proverava da li se dodatni troškovi (porezi, dostava, manipulacija) poklapaju sa PO

## Uobičajeni troškovi
```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

## Izračunavanje

**Primer: Provera troška dostave**
```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Primer: Više troškova**
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

# 9. Verifikacija poreza

## Svrha
Verifikuje da su iznosi poreza ispravno izračunati

## Izračunavanje

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

**Uobičajeni problemi:**
```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Primer: Oporezivanje sa više stopa**
```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

---

# 10. Uparivanje objekta/troškovnog centra

## Svrha
Obezbeđuje da je faktura za ispravan objekat/troškovni centar

## Primer
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

# 11. Validacija statusa dobavljača

## Svrha
Proverava da li je dobavljač i dalje odobren/aktivan

## Tipovi statusa
```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

## Primer provere
```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

---

# Koju toleranciju da koristim?

## Stroge tolerancije (Niži rizik, više ručnog rada)
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

## Umerene tolerancije (Izbalansirano)
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

## Labave tolerancije (Viši rizik, manje ručnog rada)
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

# Primer toka rada za uparivanje PO

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

# Rešavanje problema sa uparivanjem PO

## „PO Not Found"
```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

## „Items Don't Match"
```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

## „Price Higher Than PO"
```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

## „Delivery Date Wrong"
```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

---

# Zbirna tabela

| Kartica | Šta proverava | Glavno izračunavanje | Uobičajena tolerancija |
|------|----------------|------------------|-----------------|
| Full Match | Sve | Sve provere | Varira |
| Unit Price | Cena po jedinici | Razlika u % ili € | ±3-5% |
| Quantity | Naručeni iznos | Razlika u % ili jedinici | ±3-5% |
| Combined Price | Ukupno sa promenom količine | Količina × Cena | ±5-10% |
| Item ID | Ispravne stavke | Poklapanje stringa | Tačno |
| Order Type | Tip kupovine | Poklapanje stringa | Tačno |
| Delivery Date | Kada je stiglo | Razlika u danima | ±3 dana |
| Charges | Dodatne naknade | Razlika u % ili € | ±5% |
| Tax | Iznos poreza | Izračunavanje % poreza | ±1% |
| Facility | Troškovni centar | Poklapanje stringa | Tačno |
| Supplier | Odobren? | Provera statusa | Samo aktivni |

---

# Povezana dokumentacija

- Pogledajte vodič „Invoice Validation" za kompletan tok rada
- Pogledajte „Tolerance Settings" za preporučene vrednosti po industriji
- Pogledajte „Exception Handling" za to šta raditi sa neuspesima
- Kontaktirajte svoj tim za nabavku za specifične politike tolerancije
