# Purchase Order (PO) Matching Cards - Complete Guide

Karty dopasowania zamówień na tej stronie trafiają do grupy **And** w Kreatorze przepływów — porównują dane faktury z dopasowanym zamówieniem przed wykonaniem akcji Then:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty dopasowania zamówień dodaje się do grupy <strong>And</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
Samouczek DocBits PO Matching: automatyczne/ręczne dopasowanie pozycji, tolerancje i wskaźniki niezgodności
{% endembed %}

**Status:** Obejmuje 15 kart porównania PO ze szczegółowymi obliczeniami

---

## 📌 Informacje o wersji

**Najbardziej ewoluowana karta:** CONDITION_DOC_TO_PO_UNIT_PRICE (5 wersji, v5 najnowsza)
**Inne złożone karty:** CONDITION_OC_TO_PO_ITEMS (v4), CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v4)

**Kluczowe wzorce:**
- **v2 → v3+:** Dodanie parametrów tolerancji dla elastycznego dopasowania
- **v3 → v4:** Dodanie parametrów trybu porównania
- **v4 → v5:** Wzbogacona tolerancja z wieloma jednostkami (%, EUR, $ itp.)

📖 [Pełna historia wersji](../../../changelog/release.md#-po-comparison--validation-cards) | [Baza danych wersji kart](../../../../DocFlow/docs/card_version.md)

---

## Zrozumienie dopasowania PO

Gdy otrzymujesz fakturę, powinna ona odpowiadać złożonemu wcześniej zamówieniu zakupu (PO). Karty dopasowania PO automatycznie sprawdzają, czy dane faktury są zgodne z danymi PO.

**Ogólny obraz:**
```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

---

# 1. Purchase Order Full Match

## Cel
Sprawdza, czy cała faktura odpowiada PO idealnie lub w granicach tolerancji

## Kiedy używać
- Przed zatwierdzeniem faktury
- Jako wstępna kontrola jakości
- Aby wcześnie zidentyfikować problemy

## Jak to działa
System porównuje:
- Ilości na fakturze a ilości w PO
- Ceny na fakturze a ceny w PO
- Pozycje na fakturze a pozycje w PO
- Sumę faktury a sumę PO

## Wynik
- **TRUE** (Full Match): Wszystko się zgadza, kontynuuj
- **FALSE** (Mismatch): Coś się nie zgadza, wymaga przeglądu

## Przykład
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

# 2. Unit Price Comparison (Document vs PO)

## Cel
Porównuje cenę jednostkową na fakturze z ceną jednostkową w PO

## Parametry
- **Unit Price Tolerance**: Dopuszcza odchylenie do tej wartości
- **Tolerance Type**: Procentowe (%) lub bezwzględne (€/$)
- **Operator**: Is Equal to, Is Greater than, Is Less than itp.

## Jak to działa (tolerancja procentowa)

**Formuła:**
```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Przykład krok po kroku:**
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

## Rzeczywiste przykłady

### Przykład 1: Niewielki wzrost (zaakceptowany)
```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

### Przykład 2: Duży wzrost (odrzucony)
```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

### Przykład 3: Rabat (również sprawdzany)
```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

### Przykład 4: Tolerancja wartości bezwzględnej
```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

## Co zrobić z wynikami

**Jeśli PASS ✅:**
- Kontynuuj do następnej kontroli
- Lub zatwierdź fakturę
- Lub przejdź do eksportu

**Jeśli FAIL ❌:**
- Oznacz do przeglądu ręcznego
- Poproś dostawcę o wyjaśnienie
- Skontaktuj się z zespołem zakupowym
- Zatwierdź z adnotacją, jeśli akceptowalne

---

# 3. Quantity Comparison

## Cel
Sprawdza, czy zamówiona ilość odpowiada ilości na fakturze

## Parametry
- **Tolerance**: Dopuszczalna kwota lub % różnicy
- **Operator**: Equals, Greater than, Less than
- **Quantity Type**: Ordered, Received, Open

## Przykład obliczenia

**Tolerancja procentowa:**
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

**Tolerancja bezwzględna:**
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

## Rzeczywiste scenariusze

### Nadmierna dostawa (więcej niż zamówiono)
```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

### Niedostateczna dostawa (mniej niż zamówiono)
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

# 4. Combined Price of Quantity Difference

## Cel
Gdy ilość się różni, oblicza, czy łączna różnica ceny jest akceptowalna

## Dlaczego to ważne
```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

## Obliczenie

**Formuła:**
```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Przykład:**
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

# 5. Item ID / Supplier Item Number Comparison

## Cel
Sprawdza, czy pozycje na fakturze odpowiadają pozycjom w PO

## Jak to działa

**Dokładne dopasowanie (najprostsze):**
```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Numer pozycji dostawcy (częstszy):**
```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

## Scenariusz: Co jeśli się nie zgadza?

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

# 6. Order Type Verification

## Cel
Weryfikuje, czy typ zamówienia zakupu jest poprawny

## Typy zamówień
- **Standard Order**: Zwykły zakup
- **Rush Order**: Pilny, może mieć dopłatę
- **Frame Agreement**: Umowa długoterminowa
- **Blanket Order**: Umowa otwarta
- **Consignment**: Płacisz dopiero po wykorzystaniu

## Przykład sprawdzenia
```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

---

# 7. Delivery Date Verification

## Cel
Sprawdza, czy data dostawy odpowiada obiecanej dacie w PO

## Obliczenie

**Opóźniona dostawa:**
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

**Wcześniejsza dostawa:**
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

## Ustawienia tolerancji
```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

---

# 8. Charge Verification (Taxes, Shipping, Etc.)

## Cel
Sprawdza, czy dodatkowe opłaty (podatki, wysyłka, obsługa) odpowiadają PO

## Typowe opłaty
```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

## Obliczenie

**Przykład: Sprawdzenie opłaty za wysyłkę**
```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Przykład: Wiele opłat**
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

# 9. Tax Verification

## Cel
Weryfikuje, czy kwoty podatku są poprawnie obliczone

## Obliczenie

**Formuła:**
```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Typowe problemy:**
```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Przykład: Opodatkowanie wielostawkowe**
```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

---

# 10. Facility/Cost Center Matching

## Cel
Zapewnia, że faktura dotyczy właściwego obiektu/centrum kosztów

## Przykład
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

# 11. Supplier Status Validation

## Cel
Sprawdza, czy dostawca jest nadal zatwierdzony/aktywny

## Typy statusu
```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

## Przykład sprawdzenia
```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

---

# Której tolerancji powinienem użyć?

## Ścisłe tolerancje (niższe ryzyko, więcej pracy ręcznej)
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

## Umiarkowane tolerancje (zrównoważone)
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

## Luźne tolerancje (wyższe ryzyko, mniej pracy ręcznej)
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

# Przykład przepływu pracy dopasowania PO

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

# Rozwiązywanie problemów z dopasowaniem PO

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

# Tabela podsumowująca

| Karta | Co sprawdza | Główne obliczenie | Typowa tolerancja |
|------|----------------|------------------|-----------------|
| Full Match | Wszystko | Wszystkie kontrole | Różnie |
| Unit Price | Cena za jednostkę | Różnica % lub € | ±3-5% |
| Quantity | Zamówiona ilość | Różnica % lub jednostek | ±3-5% |
| Combined Price | Suma ze zmianą ilości | Qty × Price | ±5-10% |
| Item ID | Właściwe pozycje | Dopasowanie ciągu | Dokładne |
| Order Type | Typ zakupu | Dopasowanie ciągu | Dokładne |
| Delivery Date | Kiedy przybyło | Różnica dni | ±3 dni |
| Charges | Dodatkowe opłaty | Różnica % lub € | ±5% |
| Tax | Kwota podatku | Obliczenie % podatku | ±1% |
| Facility | Centrum kosztów | Dopasowanie ciągu | Dokładne |
| Supplier | Zatwierdzony? | Sprawdzenie statusu | Tylko aktywny |

---

# Powiązana dokumentacja

- Zobacz przewodnik "Invoice Validation", aby poznać pełny przepływ pracy
- Zobacz "Tolerance Settings", aby uzyskać zalecane wartości według branży
- Zobacz "Exception Handling", aby dowiedzieć się, co zrobić w przypadku niepowodzeń
- Skontaktuj się ze swoim zespołem zakupowym, aby uzyskać konkretne zasady tolerancji
