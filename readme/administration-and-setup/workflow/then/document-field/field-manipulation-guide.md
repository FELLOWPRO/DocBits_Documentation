# Kaarten voor veld- en tabelbewerkingen

## Veld- en tabelbewerkingkaarten - Complete gids

**Hoezen:** 9 kaarten voor het wijzigen van documentvelden en tabellen

***

De veld- en tabelkaarten op deze pagina bevinden zich in de groep **Dan** van de Workflow Builder – de acties die worden uitgevoerd zodra de When/And-voorwaarden overeenkomen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-nl.png" alt="Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface."><figcaption><p>Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

***

### 📌 Versie-informatie

**Multiversiekaarten:** CALC\_COLUMNS (v2), CALC\_COLUMNS\_REGEX (v2), EDIT\_COLUMN (v2), AI\_CALC\_MTZ\_ETZ (v2)

**Versiepatroon:** Alle veldmanipulatiekaarten volgen v1 → v2-patroon **Sleutelwijziging:** v2 voegt ondersteuning voor internationalisering (i18n) toe met vertaalsleutels

📖 [Volledige versiegeschiedenis](../../release.md) | [Kaartversies en gedrag](../../cards-overview/card-versions-guide.md)

***

## Manipulatie van documentvelden

### Kaart: ACTION\_SET\_FIELD\_TO\_TEXT / Veld instellen op tekstwaarde

#### Doel

Vult automatisch een documentveld met specifieke tekst

#### Wanneer te gebruiken

* Vul het veld in vanaf het besluit
* Stel standaardwaarden in
* Vul gestandaardiseerde informatie in
* Veld bijwerken op basis van voorwaarden

#### Hoe het werkt

```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

#### Voorbeeldscenario's

**Scenario 1: Goedkeuringscategorie instellen**

```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scenario 2: Leverancierscategorie instellen**

```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scenario 3: Verwerkingsnotities instellen**

```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

#### Parameters

**Veldnaam** Welk veld moet worden bijgewerkt

```
Examples: Category, Type, Status, Comment, Notes
```

**Tekstwaarde** Wat u in het veld moet zetten

```
Examples: "Approved", "Pending Review", "High Priority"
```

#### Configuratiestappen

1. Kies het veld dat u wilt invullen
2. Voer de tekstwaarde in
3. Voorwaarden instellen (wanneer invullen)
4. Opslaan

***

### Kaart: ACTION\_SET\_BOOLEAN\_FIELD / Selectievakjeveld instellen

#### Doel

Schakelt automatisch een selectievakje in of uit

#### Wanneer te gebruiken

* Markeer als verwerkt
* Goedkeuringsvlaggen instellen
* Opties in-/uitschakelen
* Markeren voor export

#### Hoe het werkt

```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

#### Waar = aangevinkt, onwaar = niet aangevinkt

**Voorbeelden:**

**Voorbeeld 1: Markeren als geverifieerd**

```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Voorbeeld 2: Vlag voor handmatige beoordeling**

```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Voorbeeld 3: verwijder het vinkje voor vooraf ingevuld vakje**

```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

#### Parameters

```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

***

### Kaart: ACTION\_INVERT\_BOOLEAN\_FIELD / Schakel selectievakje in

#### Doel

Draait de status van het selectievakje om (aangevinkt → niet aangevinkt, vice versa)

#### Wanneer te gebruiken

* Goedkeuringsstatus schakelen
* Verwerkingsmodus wijzigen
* Vorige toestand omkeren
* Booleaanse vlaggen bijwerken

#### Hoe het werkt

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

#### Voorbeeld

```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

***

### Kaart: ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD / Veldwaarde kopiëren

#### Doel

Kopieert waarde van het ene veld naar het andere veld

#### Wanneer te gebruiken

* Kopieer leveranciersgegevens naar factuurgegevens
* Dupliceer gegevens over velden heen
* Standaardiseer het gegevensformaat
* Creëer een back-up van waarde

#### Hoe het werkt

```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

#### Echte voorbeelden

**Voorbeeld 1: Kopieer afleveradres**

```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Voorbeeld 2: Kopieer leverancierscode**

```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Voorbeeld 3: Kopieerbedrag voor validatie**

```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

#### Parameters

```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

#### Opmerkingen

* Oorspronkelijk veld ongewijzigd
* Doelveld overschreven met bronwaarde
* Goed voor het standaardiseren van gegevens

***

## Tabelmanipulatie

### Kaart: EDIT\_COLUMN / Tabelkolom bewerken

#### Doel

Wijzigt waarden in een tabelkolom op basis van voorwaarden

#### Wanneer te gebruiken

* Los prijsfouten in regelitems op
* Hoeveelheden bijwerken
* Correcte artikelbeschrijvingen
* Standaardiseer waarden

#### Hoe het werkt

```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

#### Voorbeeld: vaste prijzen

**Scenario: Prijzen in verkeerde valuta**

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

#### Parameters

```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

#### Gemeenschappelijk gebruik

* Vaste eenheidsprijzen
* Standaardiseer beschrijvingen
* Juiste hoeveelheden
* Update SKU-nummers

***

### Kaart: CALC\_COLUMNS / Kolomwaarden berekenen

#### Doel

Voert berekeningen uit op tabelkolommen en slaat het resultaat op

#### Wanneer te gebruiken

* Regeltotalen berekenen (aantal x eenheidsprijs)
* Som kolommen
* Bereken kortingen
* Bereken percentages

#### Hoe het werkt

```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

#### Berekeningstypen

**Type 1: eenvoudige vermenigvuldiging**

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

**Type 2: Toevoeging**

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

**Type 3: Percentageberekening**

```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Type 4: Aftrekken**

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

#### Voorbeeld uit de echte wereld

**Berekening factuurregelitems:**

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

#### Parameters

```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

***

### Kaart: CALC\_COLUMNS\_REGEX / Bereken met Regex-patroon

#### Doel

Berekent kolomwaarden op basis van patroonovereenkomst

#### Wanneer te gebruiken

* Haal waarden uit tekst met behulp van patronen
* Formatteer gegevens op basis van regels
* Converteer waarden op basis van patronen
* Gestructureerde tekst analyseren

#### Hoe het werkt

**Regex-patroonaanpassing:**

```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

#### Voorbeeld: Leverancierscode extraheren

**Scenario: Artikelnummers bevatten leveranciersinformatie**

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

#### Voorbeeld: Telefoonnummers opmaken

**Scenario: niet-geformatteerde telefoonnummers**

```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

#### Voorbeeld: Haal prijzen uit tekst

**Scenario: Prijzen in tekstformaat**

```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

#### Parameters

```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

#### Algemene Regex-patronen

```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

***

## Rekenvoorbeelden

### Voorbeeld 1: Berekening van het factuurtotaal

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

### Voorbeeld 2: Variantieberekening

```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

### Voorbeeld 3: Kortingstoepassing

```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

***

## Voorbeeld van een workflow voor veldmanipulatie

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

## Beste praktijken

✅ **Doe:**

* Houd formules eenvoudig
* Testberekeningen met voorbeeldgegevens
* Controleer of de resultaten zinvol zijn
* Documenteer waarom u velden wijzigt
* Gebruik het kopieerveld als de gegevens hetzelfde zijn

❌ **Niet doen:**

* Cirkelreferenties aanmaken (A=B, B=A)
* Overschrijf belangrijke gegevens zonder reden
* Maak te complexe regex-patronen
* Vergeet de berekeningsresultaten te verifiëren
* Bereken op verkeerde tabel/kolommen

***

## Problemen oplossen

### "Veld wordt niet bijgewerkt"

**Oorzaak:** Aan voorwaarde is niet voldaan of kaart is niet geactiveerd

**Oplossing:**

* Controleer of de voorwaarde waar is
* Controleer of de kaart zich in de workflow bevindt
* Test met voorbeeldgegevens
* Controleer op typefouten in de veldnaam

### "Berekeningsresultaat verkeerd"

**Oorzaak:** Verkeerde kolommen geselecteerd of formule onjuist

**Oplossing:**

* Bronkolommen verifiëren
* Controleer de formule is correct
* Handmatig testen
* Controleer decimalen/afrondingen

### "Tabel toont fout"

**Oorzaak:** De kolom waarnaar wordt verwezen bestaat niet

**Oplossing:**

* Controleer de spelling van de kolomnaam
* Controleer kolom bevat gegevens
* Zorg ervoor dat het kolomgegevenstype overeenkomt met de berekening
* Voeg indien nodig ontbrekende kolommen toe

***

## Gerelateerde kaarten

* **ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD** - Waarden kopiëren
* **EDIT\_COLUMN** - Tabelwaarden wijzigen
* **CALC\_COLUMNS** - Formules berekenen
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Tekstwaarden instellen
* **ACTION\_SET\_BOOLEAN\_FIELD** - Selectievakjes
