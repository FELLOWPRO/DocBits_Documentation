# PO-Matching-Karten – Vollständiger Leitfaden

## Passende Karten für Bestellungen (PO) – Vollständiger Leitfaden

**Status:** Deckt 15 PO-Vergleichskarten mit detaillierten Berechnungen ab

***

Die PO-Vergleichskarten auf dieser Seite gehen in die **Und** Gruppe des Workflow Builders – sie vergleichen Rechnungsdaten mit der abgeglichenen Bestellung, bevor die Then-Aktionen ausgeführt werden:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow-Builder"><figcaption><p>PO-Abgleichskarten werden über <strong>Add Card</strong> zur <strong>And</strong>-Gruppe hinzugefügt.</p></figcaption></figure>

***

### 📌 Versionsinformationen

**Am weitesten entwickelte Karte:** CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE (5 Versionen, neueste Version 5) **Andere komplexe Karten:** CONDITION\_OC\_TO\_PO\_ITEMS (Version 4), CONDITION\_LESS\_THAN\_TOLERANCE\_AS\_VALUE\_OF\_ORDERED\_QUANTITY (Version 4)

**Tastenmuster:**

* **v2 → v3+:** Hinzufügung von Toleranzparametern für eine flexible Anpassung
* **v3 → v4:** Hinzufügung von Vergleichsmodus-Parametern
* **v4 → v5:** Erweiterte Toleranz mit mehreren Einheiten (%, EUR, $ usw.)

📖 [Vollständiger Versionsverlauf](../../release.md) | [Kartenversionen und Verhalten](../../cards-overview/card-versions-guide.md)

***

### PO-Matching verstehen

Wenn Sie eine Rechnung erhalten, sollte diese mit der zuvor aufgegebenen Bestellung (PO) übereinstimmen. Bestellabgleichskarten prüfen automatisch, ob Rechnungsdaten mit Bestelldaten übereinstimmen.

**Das große Ganze:**

```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

***

## 1. Vollständige Übereinstimmung der Bestellung

### Zweck

Überprüft, ob die gesamte Rechnung perfekt oder innerhalb der Toleranz mit der Bestellung übereinstimmt

### Wann zu verwenden

* Bevor Sie eine Rechnung genehmigen
* Als vorläufige Qualitätskontrolle
* Um Probleme frühzeitig zu erkennen

### Wie es funktioniert

System vergleicht:

* Rechnungsmengen im Vergleich zu Bestellmengen
* Rechnungspreise vs. PO-Preise
* Rechnungspositionen vs. Bestellpositionen
* Gesamtsumme der Rechnung im Vergleich zur Gesamtsumme der Bestellung

### Ergebnis

* **TRUE** (Vollständige Übereinstimmung): Alles stimmt, fortfahren
* **FALSE** (Nichtübereinstimmung): Etwas stimmt nicht überein, muss überprüft werden

### Beispiel

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

***

## 2. Vergleich der Stückpreise (Dokument vs. Bestellung)

### Zweck

Vergleicht den Stückpreis auf der Rechnung mit dem Stückpreis auf der Bestellung

### Parameter

* **Stückpreistoleranz**: Abweichungen bis zu diesem Betrag zulassen
* **Toleranztyp**: Prozentsatz (%) oder Absolut (€/$)
* **Betreiber**: Ist gleich, ist größer als, ist kleiner als usw.

### So funktioniert es (prozentuale Toleranz)

**Formel:**

```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Schritt-für-Schritt-Beispiel:**

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

### Beispiele aus der Praxis

#### Beispiel 1: Kleine Erhöhung (akzeptiert)

```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

#### Beispiel 2: Große Erhöhung (abgelehnt)

```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

#### Beispiel 3: Rabatt (auch geprüft)

```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

#### Beispiel 4: Absolute Werttoleranz

```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

### Was tun mit Ergebnissen?

**Wenn PASS ✅:**

* Fahren Sie mit der nächsten Prüfung fort
* Oder Rechnung genehmigen
* Oder fahren Sie mit dem Export fort

**Wenn FAIL ❌:**

* Zur manuellen Überprüfung kennzeichnen
* Bitten Sie den Lieferanten um eine Erklärung
* Kontaktieren Sie das Beschaffungsteam
* Genehmigen Sie mit einer Notiz, wenn dies akzeptabel ist

***

## 3. Mengenvergleich

### Zweck

Prüft, ob die bestellte Menge mit der in Rechnung gestellten Menge übereinstimmt

### Parameter

* **Toleranz**: Betrag oder % dürfen abweichen
* **Betreiber**: Gleich, Größer als, Kleiner als
* **Mengentyp**: Bestellt, Erhalten, Offen

### Berechnungsbeispiel

**Prozent-Toleranz:**

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

**Absolute Toleranz:**

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

### Szenarien aus der realen Welt

#### Überlieferung (mehr als bestellt)

```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

#### Unterlieferung (weniger als bestellt)

```
Ordered: 100 units
Invoiced: 95 units
Tolerance: ±5%

Variance = |(95-100)|/100 × 100 = 5%

Is 5% ≤ 5%? YES ✅

Decision: Accept - within tolerance
Possible reason: Partial shipment, rest to follow
```

***

## 4. Kombinierter Preis der Mengendifferenz

### Zweck

Bei Mengenunterschieden wird berechnet, ob der Gesamtpreisunterschied akzeptabel ist

### Warum das wichtig ist

```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

### Berechnung

**Formel:**

```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Beispiel:**

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

***

## 5. Vergleich zwischen Artikel-ID und Lieferantenartikelnummer

### Zweck

Prüft, ob die Artikel in der Rechnung mit den Artikeln in der Bestellung übereinstimmen

### Wie es funktioniert

**Genaue Übereinstimmung (am einfachsten):**

```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Lieferantenartikelnummer (häufiger):**

```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

### Szenario: Was passiert, wenn es nicht übereinstimmt?

```
PO Item: ABC-123 (Copper Wire, 2mm)
Invoice Item: ABC-124 (Steel Wire, 2mm)

Result: ❌ NO MATCH

Actions:
1. Is this a substitution? Check with procurement
2. Is this an error? Contact supplier
3. Is the description similar? Verify manually
```

***

## 6. Überprüfung des Auftragstyps

### Zweck

Überprüft, ob der Bestelltyp korrekt ist

### Auftragsarten

* **Standardbestellung**: Regulärer Kauf
* **Eilauftrag**: Dringend, möglicherweise mit Aufpreis
* **Rahmenvereinbarung**: Langfristiger Vertrag
* **Pauschalauftrag**: Unbefristeter Vertrag
* **Einlieferung**: Sie zahlen erst bei Nutzung

### Überprüfen Sie das Beispiel

```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

***

## 7. Überprüfung des Lieferdatums

### Zweck

Überprüft, ob das Lieferdatum mit dem versprochenen Datum auf der Bestellung übereinstimmt

### Berechnung

**Verspätete Lieferung:**

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

**Frühe Lieferung:**

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

### Toleranzeinstellungen

```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

***

## 8. Gebührenüberprüfung (Steuern, Versand usw.)

### Zweck

Prüft, ob zusätzliche Kosten (Steuern, Versand, Bearbeitung) mit der Bestellung übereinstimmen

### Gemeinsame Gebühren

```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

### Berechnung

**Beispiel: Versandkostenprüfung**

```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Beispiel: Mehrfachladungen**

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

***

## 9. Steuerprüfung

### Zweck

Überprüft, ob die Steuerbeträge korrekt berechnet werden

### Berechnung

**Formel:**

```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Häufige Probleme:**

```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Beispiel: Mehrfachbesteuerung**

```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

***

## 10. Zuordnung von Einrichtung und Kostenstelle

### Zweck

Stellt sicher, dass die Rechnung für die richtige Einrichtung/Kostenstelle ausgestellt ist

### Beispiel

```
PO is for:
- Facility: Berlin Plant
- Cost Center: CC-2025

Invoice should have:
- Facility: Berlin Plant ✅
- Cost Center: CC-2025 ✅

If different facility: May need different approval
```

***

## 11. Validierung des Lieferantenstatus

### Zweck

Prüft, ob der Lieferant noch zugelassen/aktiv ist

### Statustypen

```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### Überprüfen Sie das Beispiel

```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

***

## Welche Toleranz sollte ich verwenden?

### Strenge Toleranzen (geringeres Risiko, mehr manuelle Arbeit)

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

### Moderate Toleranzen (ausgewogen)

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

### Lockere Toleranzen (höheres Risiko, weniger manuelle Arbeit)

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

***

## Beispiel für einen PO-Matching-Workflow

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

***

## Fehlerbehebung beim Bestellabgleich

### „Bestellung nicht gefunden“

```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

### „Artikel stimmen nicht überein“

```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

### „Preis höher als Bestellwert“

```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

### „Lieferdatum falsch“

```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

***

## Übersichtstabelle

| Karte           | Was es überprüft        | Hauptberechnung     | Gemeinsame Toleranz |
| -------------- | --------------------- | -------------------- | ---------------- |
| Vollständige Übereinstimmung     | Alles            | Alle Schecks           | Variiert           |
| Stückpreis     | Preis pro Einheit        | % oder € Differenz    | ±3-5%            |
| Menge       | Bestellte Menge        | % oder Einheitsdifferenz | ±3-5%            |
| Kombipreis | Gesamt mit Mengenänderung | Menge × Preis          | ±5-10%           |
| Artikel-ID        | Richtige Artikel           | Zeichenfolgenübereinstimmung         | Genau            |
| Auftragsart     | Art des Kaufs      | Zeichenfolgenübereinstimmung         | Genau            |
| Liefertermin  | Als angekommen          | Tagesunterschied       | ±3 Tage          |
| Gebühren        | Zusätzliche Gebühren            | % oder € Differenz    | ±5%              |
| Steuer            | Steuerbetrag            | Berechnung des Steuerprozentsatzes    | ±1%              |
| Einrichtung       | Kostenstelle           | Zeichenfolgenübereinstimmung         | Genau            |
| Lieferant       | Genehmigt?             | Statusprüfung         | Nur aktiv      |

***

## Verwandte Dokumentation

* Den vollständigen Arbeitsablauf finden Sie im Leitfaden „Rechnungsvalidierung“.
* Empfohlene Werte nach Branche finden Sie unter „Toleranzeinstellungen“.
* Informationen zum Umgang mit Fehlern finden Sie unter „Ausnahmebehandlung“.
* Kontaktieren Sie Ihr Beschaffungsteam für spezifische Toleranzrichtlinien
