# Gegevenstransformatie Patroon

**Patroontype:** Gegevensverwerking & Manipulatie
**Complexiteit:** Gemiddeld
**Geschatte Insteltijd:** 30-45 minuten
**Veelvoorkomende Gebruiksscenario's:** Veldberekeningen, gegevensopmaak, valutaconversie, eenheidsconversie, gegevensverrijking

---

U bouwt dit patroon in de **Workflow Builder** (Workflow Dashboard → Workflowlijst → Workflow Toevoegen). Klik op **Add Card** en open de categorie **Document Field** — deze bevat de lees-, schrijf-, bereken- en opmaakkaarten die dit patroon aan elkaar koppelt:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-bibliotheek in de Workflow Builder, gegroepeerd per categorie"><figcaption><p>De <strong>Add Card</strong>-bibliotheek — kaarten voor het lezen/schrijven van velden, berekeningen en opmaak bevinden zich onder de categorie <strong>Document Field</strong>.</p></figcaption></figure>

---

## Patroonoverzicht

Dit patroon demonstreert hoe u documentgegevens kunt transformeren, berekenen, formatteren en verrijken in DocBits workflows. Gegevenstransformatie is essentieel voor het voorbereiden van gegevens voor export, het uitvoeren van berekeningen, het standaardiseren van formaten en het verrijken van documenten met aanvullende informatie.

**Wat Dit Patroon Doet:**
1. Extraheert gegevens uit documentvelden
2. Voert berekeningen en transformaties uit
3. Formatteert gegevens naar vereiste standaarden
4. Converteert tussen eenheden, valuta's, datums
5. Verrijkt documenten met afgeleide of opzoekgegevens
6. Valideert en schoont gegevens op

---

## Wanneer Dit Patroon Te Gebruiken

Gebruik dit patroon wanneer u het volgende moet doen:
- ✅ Totalen, subtotalen, belastingen berekenen
- ✅ Valuta's of eenheden converteren
- ✅ Datums, getallen, tekst formatteren
- ✅ Waarden afleiden uit bestaande velden
- ✅ Gegevens verrijken uit externe bronnen
- ✅ Gegevensformaten standaardiseren
- ✅ Gegevens opschonen en valideren
- ✅ Gegevens voorbereiden voor export

**Gebruik dit patroon niet wanneer:**
- ❌ Geen transformatie nodig is
- ❌ Gegevens al in het juiste formaat zijn
- ❌ Eenvoudige veldkopie voldoende is

---

## Typen Gegevenstransformatie

### 1. Berekeningen

**Wiskundige Operaties:**
```
- Optellen: Quantity + Bonus_Quantity = Total_Quantity
- Aftrekken: Invoice_Total - Tax_Amount = Net_Amount
- Vermenigvuldigen: Quantity × Unit_Price = Line_Total
- Delen: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. String Operaties

**Tekstmanipulatie:**
```
- Samenvoegen: First_Name + " " + Last_Name = Full_Name
- Hoofdletters: "invoice" → "INVOICE"
- Kleine letters: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (jaar extraheren)
- Vervangen: "01/23/2025" → "2025-01-23"
- Trimmen: "  ABC Corp  " → "ABC Corp"
```

### 3. Gegevenstypeconversie

**Type Transformaties:**
```
- String naar Nummer: "123.45" → 123.45
- Nummer naar String: 123.45 → "123.45"
- Datum naar String: 2025-10-23 → "23 oktober 2025"
- String naar Datum: "23.10.2025" → 2025-10-23
- Booleaans naar String: true → "Ja"
```

### 4. Eenheidsconversies

**Metingconversies:**
```
- Gewicht: kg → lbs, ton → kg
- Lengte: cm → inches, m → ft
- Volume: liters → gallons
- Temperatuur: Celsius → Fahrenheit
- Hoeveelheid: stuks → dozijnen, eenheden → pallets
```

### 5. Valutaconversies

**Toepassingen van Wisselkoersen:**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-valuta: Converteer alles naar basisvaluta
- Historische koersen: Gebruik koers van factuurdatum
```

### 6. Datumtransformaties

**Datumoperaties:**
```
- Formaatwijziging: 10/23/2025 → 2025-10-23
- Dagen toevoegen: Invoice_Date + 30 = Due_Date
- Leeftijd berekenen: Vandaag - Invoice_Date = Age_Days
- Delen extraheren: "2025-10-23" → Jaar: 2025, Maand: 10, Dag: 23
```

---

## Compleet Workflowvoorbeeld

### Scenario: Factuurtotaalberekening & Gegevensverrijking

**Bedrijfsvereiste:**
- Extraheer regelitems van factuur
- Bereken regeltotalen (Aantal × Prijs)
- Bereken subtotaal (som van regeltotalen)
- Bereken belastingbedrag (Subtotaal × Belastingtarief)
- Bereken eindtotaal (Subtotaal + Belasting)
- Converteer naar EUR als factuur in andere valuta is
- Formatteer bedragen naar 2 decimalen
- Voeg bedrijfs-GL-rekening toe op basis van productcategorie
- Valideer berekeningen tegen factuurtotaal
- Markeer als variantie > 1%

**Gebruikte Workflowkaarten:**
1. ACTION_CALCULATE_FIELD - Voer berekeningen uit
2. ACTION_SET_FIELD_TO_TEXT - Sla resultaten op
3. ACTION_COPY_FIELD_VALUE - Kopieer waarden
4. CALL_API - Haal wisselkoersen op (indien nodig)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Valideer berekeningen
6. ACTION_SET_FIELD_FROM_MASTER_DATA - Verrijk met GL-rekeningen

---

## Stap-voor-Stap Implementatie

### Stap 1: Regelitemberekeningen

**Bereken Regeltotalen:**

**Kaart:** ACTION_CALCULATE_FIELD

**Voor elk regelitem:**
```
Veld: Line_Total
Formule: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Resultaattype: Nummer
Decimalen: 2
```

**Voorbeeld:**
```
Regel 1:
  Aantal: 100
  Eenheidsprijs: €50,00
  Berekening: 100 × 50,00 = €5.000,00
  Opslaan in: Line_Total

Regel 2:
  Aantal: 50
  Eenheidsprijs: €20,00
  Berekening: 50 × 20,00 = €1.000,00
  Opslaan in: Line_Total

Regel 3:
  Aantal: 25
  Eenheidsprijs: €15,50
  Berekening: 25 × 15,50 = €387,50
  Opslaan in: Line_Total
```

**Gidsreferentie:** [Gids Veldmanipulatie - Berekeningen](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Stap 2: Bereken Documentsubtotaal

**Som Alle Regeltotalen:**

**Kaart:** ACTION_CALCULATE_FIELD

**Configuratie:**
```
Veld: Calculated_Subtotal
Formule: SUM({{TABLE_COLUMN:Line_Total}})
Resultaattype: Nummer
Decimalen: 2
```

**Voorbeeld:**
```
Regel 1 Totaal: €5.000,00
Regel 2 Totaal: €1.000,00
Regel 3 Totaal: €387,50

Subtotaal = 5000 + 1000 + 387,50 = €6.387,50
Opslaan in: Calculated_Subtotal
```

---

### Stap 3: Bereken Belastingbedrag

**Pas Belastingtarief Toe op Subtotaal:**

**Kaart:** ACTION_CALCULATE_FIELD

**Configuratie:**
```
Veld: Calculated_Tax_Amount
Formule: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Resultaattype: Nummer
Decimalen: 2
```

**Voorbeeld:**
```
Calculated_Subtotal: €6.387,50
Tax_Rate: 19% (BTW)

Belastingbedrag = 6387,50 × (19 / 100)
          = 6387,50 × 0,19
          = €1.213,63

Opslaan in: Calculated_Tax_Amount
```

---

### Stap 4: Bereken Eindtotaal

**Tel Subtotaal en Belasting Op:**

**Kaart:** ACTION_CALCULATE_FIELD

**Configuratie:**
```
Veld: Calculated_Grand_Total
Formule: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Resultaattype: Nummer
Decimalen: 2
```

**Voorbeeld:**
```
Calculated_Subtotal: €6.387,50
Calculated_Tax_Amount: €1.213,63

Eindtotaal = 6387,50 + 1213,63 = €7.601,13

Opslaan in: Calculated_Grand_Total
```

---

### Stap 5: Valutaconversie (indien nodig)

**Controleer of conversie nodig is:**

**Kaart:** CONDITION_DOC_FIELD_IS

**Configuratie:**
```
Veld: Invoice_Currency
Operator: IS NOT EQUAL TO
Waarde: EUR
```

**Als conversie nodig is:**

**Stap 5a: Haal Wisselkoers Op**

**Kaart:** CALL_API

**Configuratie:**
```
Eindpunt: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Methode: GET
Responspad: rates.EUR
Opslaan in: Exchange_Rate_To_EUR
```

**Voorbeeld:**
```
Factuurvaluta: USD
API-respons: {
  "base": "USD",
  "rates": {
    "EUR": 0,92
  }
}

Exchange_Rate_To_EUR = 0,92
```

**Stap 5b: Converteer Bedragen**

**Kaart:** ACTION_CALCULATE_FIELD

**Configuratie:**
```
Veld: Grand_Total_EUR
Formule: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Resultaattype: Nummer
Decimalen: 2
```

**Voorbeeld:**
```
Eindtotaal (USD): $7.601,13
Wisselkoers: 0,92

Eindtotaal (EUR) = 7601,13 × 0,92 = €6.993,04

Opslaan in: Grand_Total_EUR
```

**Gidsreferentie:** [API Integratie Patroon - Valutaconversie](api-integration-pattern.md#currency-conversion-example)

---

### Stap 6: Gegevensverrijking - Voeg GL-rekeningen Toe

**Zoek GL-rekening op Productcategorie:**

**Kaart:** ACTION_SET_FIELD_FROM_MASTER_DATA

**Configuratie:**
```
Opzoektabel: GL_Account_Mapping
Opzoeksleutel: {{TABLE_FIELD:Product_Category}}
Retourveld: GL_Account_Number
Opslaan in: GL_Account
```

**Voorbeeld:**
```
Regel 1:
  Productcategorie: "Kantoorbenodigdheden"
  Opzoeken → GL_Account_Mapping tabel
  Resultaat: GL-rekening "4200-100" (Kantoorkosten)

Regel 2:
  Productcategorie: "IT-apparatuur"
  Opzoeken → GL_Account_Mapping tabel
  Resultaat: GL-rekening "6100-200" (IT-activa)

Regel 3:
  Productcategorie: "Diensten"
  Opzoeken → GL_Account_Mapping tabel
  Resultaat: GL-rekening "5000-300" (Dienstenkosten)
```

**Gidsreferentie:** [Gids Veldmanipulatie - Master Data](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Stap 7: Valideer Berekeningen

**Vergelijk Berekend Totaal met Factuurtotaal:**

**Kaart:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configuratie:**
```
Veld 1: Calculated_Grand_Total
Veld 2: Invoice_Total (uit OCR)
Operator: Bereken Variantiepercentage
Tolerantie: 1%
```

**Berekening:**
```
Variantie % = |Berekend - Factuur| / Factuur × 100

Voorbeeld:
  Berekend Totaal: €7.601,13
  Factuurtotaal: €7.600,00

  Variantie = |7601,13 - 7600,00| / 7600,00 × 100
          = 1,13 / 7600,00 × 100
          = 0,015%

  Is 0,015% ≤ 1% tolerantie? JA ✅
  Resultaat: PASS (berekeningen komen overeen met factuur)
```

**Logica:**
```
ALS Variantie ≤ 1%:
  Stel Validation_Status = "PASS"
  Ga door met verwerking
ANDERS:
  Stel Validation_Status = "FAIL"
  Maak beoordelingstaak
  Markeer voor handmatige verificatie
```

**Gidsreferentie:** [Gids Conditiekaarten - Veldvergelijking](../and/condition-cards-complete-guide.md#field-comparison)

---

### Stap 8: Formatteer Gegevens voor Export

**Standaardiseer Formaten:**

**Kaart:** ACTION_SET_FIELD_TO_TEXT

**Datumopmaak:**
```
Veld: Invoice_Date_Formatted
Waarde: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Voorbeeld: 10/23/2025 → 2025-10-23
```

**Nummeropmaak:**
```
Veld: Amount_Formatted
Waarde: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Voorbeeld: 7601.13 → 7.601,13 (Duits formaat)
```

**Tekstopmaak:**
```
Veld: Supplier_Name_Upper
Waarde: UPPERCASE({{Supplier_Name}})
Voorbeeld: "ABC Corporation" → "ABC CORPORATION"
```

---

## Geavanceerde Transformaties

### Transformatie 1: Belastingberekening op Meerdere Niveaus

**Scenario:** Verschillende belastingtarieven per regelitem

```
Regel 1: Product A (Belastingtarief 19%)
Regel 2: Product B (Belastingtarief 7% - verlaagd)
Regel 3: Product C (Belastingtarief 0% - vrijgesteld)

Berekening:
  Regel 1 Belasting = €5.000,00 × 0,19 = €950,00
  Regel 2 Belasting = €1.000,00 × 0,07 = €70,00
  Regel 3 Belasting = €387,50 × 0,00 = €0,00

  Totaal Belasting = €950,00 + €70,00 + €0,00 = €1.020,00
```

**Implementatie:**
```
Voor elke regel:
  1. Haal belastingcategorie van product op
  2. Zoek toepasselijk belastingtarief op
  3. Bereken: Line_Net × Tax_Rate = Line_Tax
  4. Som alle Line_Tax waarden = Total_Tax
```

---

### Transformatie 2: Kortingsberekeningen

**Scenario:** Pas volumekorting en korting voor vroege betaling toe

```
Oorspronkelijk Subtotaal: €10.000,00

Stap 1: Volumekorting (10% voor bestellingen > €5.000)
  Korting = €10.000,00 × 0,10 = €1.000,00
  Na Volumekorting = €10.000,00 - €1.000,00 = €9.000,00

Stap 2: Korting voor Vroege Betaling (2% indien betaald binnen 10 dagen)
  Korting = €9.000,00 × 0,02 = €180,00
  Na Betalingskorting = €9.000,00 - €180,00 = €8.820,00

Stap 3: Bereken Belasting (over bedrag na korting)
  Belasting = €8.820,00 × 0,19 = €1.675,80

Eindtotaal = €8.820,00 + €1.675,80 = €10.495,80
```

**Implementatie:**
```
1. Controleer bestelwaarde voor geschiktheid volumekorting
2. Bereken volumekorting
3. Pas volumekorting toe op subtotaal
4. Controleer betalingsvoorwaarden voor korting vroege betaling
5. Bereken korting vroege betaling
6. Pas korting vroege betaling toe
7. Bereken belasting over definitief bedrag na korting
8. Bereken eindtotaal
```

---

### Transformatie 3: Meeteenheidconversie

**Scenario:** Converteer factuur-UOM naar standaard-UOM

```
Factuur toont:
  Product: Stalen Staven
  Aantal: 50
  Eenheid: Meters
  Eenheidsprijs: €10,00/meter
  Regeltotaal: €500,00

Bedrijfsstandaard UOM: Voeten

Conversie:
  1 meter = 3,28084 voet

  Aantal (voet) = 50 meter × 3,28084 = 164,042 voet
  Eenheidsprijs (voet) = €10,00/meter ÷ 3,28084 = €3,05/voet

  Verificatie: 164,042 voet × €3,05/voet ≈ €500,00 ✅
```

**Implementatie:**
```
1. Identificeer factuur-UOM
2. Haal conversiefactor naar standaard-UOM op
3. Converteer aantal
4. Converteer eenheidsprijs
5. Verifieer dat regeltotaal hetzelfde blijft
6. Sla zowel originele als geconverteerde waarden op
```

---

### Transformatie 4: Datumberekeningen

**Scenario:** Bereken betalingsvoorwaarden en vervaldatums

```
Factuurdatum: 2025-10-23
Betalingsvoorwaarden: NET30

Berekeningen:
  Vervaldatum = Factuurdatum + 30 dagen = 2025-11-22

  Korting Vroege Betaling Beschikbaar Indien:
    Betalingsdatum ≤ Factuurdatum + 10 dagen
    Korting Einddatum = 2025-11-02

  Dagen Tot Vervaldatum = Vervaldatum - Vandaag
    Als Vandaag = 2025-10-23: Dagen = 30
    Als Vandaag = 2025-11-15: Dagen = 7
    Als Vandaag = 2025-11-23: Dagen = -1 (achterstallig)
```

**Implementatie:**
```
1. Extraheer Invoice_Date
2. Extraheer Payment_Terms (bijv. "NET30", "NET60", "2/10 NET30")
3. Parse betalingsvoorwaarden
4. Bereken Due_Date
5. Bereken Discount_End_Date (indien van toepassing)
6. Bereken Days_Until_Due
7. Stel Status in: "Current", "Due Soon", "Overdue"
```

---

### Transformatie 5: Tekst Parsing & Extractie

**Scenario:** Extraheer gestructureerde gegevens uit ongestructureerde tekst

```
Origineel Veld: "PO-2025-ABC-12345-REV2"

Extraheer:
  Jaar: "2025"
  Afdeling: "ABC"
  PO-nummer: "12345"
  Revisie: "2"

Methode:
  Splitsen op scheidingsteken "-"
  Array: ["PO", "2025", "ABC", "12345", "REV2"]

  Extraheer:
    Jaar = Array[1] = "2025"
    Afdeling = Array[2] = "ABC"
    PO_Nummer = Array[3] = "12345"
    Revisie = Extraheer cijfers uit Array[4] = "2"
```

---

## Compleet Transformatie Workflow Diagram

```
FACTUURGEGEVENS GEËXTRAHEERD
│
├─ STAP 1: REGELITEMBEREKENINGEN
│  Voor elke regel:
│    Aantal × Eenheidsprijs = Regeltotaal
│  Resultaat: Regeltotalen berekend
│
├─ STAP 2: SUBTOTAALBEREKENING
│  SOM(Alle Regeltotalen) = Subtotaal
│  Resultaat: €6.387,50
│
├─ STAP 3: BELASTINGBEREKENING
│  Subtotaal × Belastingtarief = Belastingbedrag
│  €6.387,50 × 19% = €1.213,63
│
├─ STAP 4: EINDTOTAALBEREKENING
│  Subtotaal + Belastingbedrag = Eindtotaal
│  €6.387,50 + €1.213,63 = €7.601,13
│
├─ STAP 5: VALUTACONTROLE
│  │
│  ├─ Valuta = EUR? JA
│  │  → Sla conversie over
│  │  → Gebruik Grand_Total zoals het is
│  │
│  └─ Valuta ≠ EUR? NEE (bijv. USD)
│     │
│     ├─ Roep Wisselkoers-API Aan
│     │  Haal op: USD → EUR koers (0,92)
│     │
│     ├─ Converteer Bedrag
│     │  $7.601,13 × 0,92 = €6.993,04
│     │
│     └─ Sla geconverteerd bedrag op
│        Grand_Total_EUR = €6.993,04
│
├─ STAP 6: GEGEVENSVERRIJKING
│  Voor elke regel:
│    Zoek Productcategorie → GL_Account
│    Sla GL_Account op in regelitem
│  Resultaat: Alle regels hebben GL-rekeningen
│
├─ STAP 7: VALIDATIE
│  │
│  ├─ Vergelijk Berekend vs Factuurtotaal
│  │  Variantie = |Berekend - Factuur| / Factuur × 100
│  │
│  ├─ Variantie ≤ 1%? ✅
│  │  Stel Validation_Status = "PASS"
│  │  Ga door met verwerking
│  │
│  └─ Variantie > 1%? ❌
│     Stel Validation_Status = "FAIL"
│     Maak beoordelingstaak
│     Markeer voor handmatige controle
│
├─ STAP 8: OPMAAK
│  │
│  ├─ Formatteer Datums
│  │  10/23/2025 → 2025-10-23
│  │
│  ├─ Formatteer Nummers
│  │  7601.13 → 7.601,13 (locale-specifiek)
│  │
│  ├─ Formatteer Tekst
│  │  "abc corp" → "ABC CORP"
│  │
│  └─ Formatteer voor Export
│     Alle velden in ERP-compatibel formaat
│
└─ TRANSFORMATIE VOLTOOID
   Document gereed voor volgende workflowstap
```

---

## Configuratiesjablonen

### Sjabloon 1: Standaard Factuurberekeningen

```json
{
  "transformations": [
    {
      "step": 1,
      "name": "Bereken Regeltotalen",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Quantity}} * {{Unit_Price}}",
      "result_field": "Line_Total"
    },
    {
      "step": 2,
      "name": "Bereken Subtotaal",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "SUM({{Line_Total}})",
      "result_field": "Calculated_Subtotal"
    },
    {
      "step": 3,
      "name": "Bereken Belasting",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} * {{Tax_Rate}} / 100",
      "result_field": "Calculated_Tax"
    },
    {
      "step": 4,
      "name": "Bereken Totaal",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} + {{Calculated_Tax}}",
      "result_field": "Calculated_Total"
    }
  ]
}
```

---

### Sjabloon 2: Valutaconversie Workflow

```json
{
  "currency_conversion": {
    "check_needed": {
      "card": "CONDITION_DOC_FIELD_IS",
      "field": "Invoice_Currency",
      "operator": "NOT EQUAL TO",
      "value": "EUR"
    },
    "get_rate": {
      "card": "CALL_API",
      "endpoint": "https://api.exchangerate.com/v1/rates/{{Invoice_Currency}}",
      "method": "GET",
      "response_path": "rates.EUR"
    },
    "convert": {
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Amount}} * {{Exchange_Rate}}",
      "result_field": "Amount_EUR"
    },
    "store_details": {
      "original_currency": "{{Invoice_Currency}}",
      "original_amount": "{{Amount}}",
      "exchange_rate": "{{Exchange_Rate}}",
      "converted_amount": "{{Amount_EUR}}",
      "conversion_date": "{{Today}}"
    }
  }
}
```

---

## Foutafhandeling

### Veelvoorkomende Transformatiefouten

**Fout 1: Delen door Nul**
```
Probleem: Unit_Price = Total / Quantity, maar Quantity = 0

Oplossing:
  ALS Quantity = 0 OF Quantity IS NULL:
    Stel Unit_Price = 0
    Markeer voor beoordeling
  ANDERS:
    Bereken normaal
```

**Fout 2: Ongeldig Nummerformaat**
```
Probleem: Veld bevat "€1.234,56" maar heb nummer 1234.56 nodig

Oplossing:
  1. Verwijder valutasymbolen
  2. Verwijder duizendtalscheidingstekens
  3. Converteer decimaalteken indien nodig
  4. Parse naar nummer
  5. Valideer resultaat
```

**Fout 3: Datum Parse Mislukt**
```
Probleem: Datum in onverwacht formaat

Oplossing:
  1. Probeer meerdere datumformaten
  2. Als alles mislukt: Stel in op null
  3. Markeer voor handmatige beoordeling
  4. Log originele waarde
```

**Fout 4: Ontbrekende Conversiefactor**
```
Probleem: Onbekende UOM-conversie

Oplossing:
  1. Controleer conversietabel
  2. Indien niet gevonden: Sla conversie over
  3. Markeer voor admin om conversie toe te voegen
  4. Gebruik originele waarden
```

---

## Testchecklist

- [ ] Alle berekeningen leveren correcte resultaten op
- [ ] Decimale precisie behouden
- [ ] Valutaconversies nauwkeurig
- [ ] Datumberekeningen correct
- [ ] Teksttransformaties werken
- [ ] Null/lege waarden afgehandeld
- [ ] Delen door nul voorkomen
- [ ] Nummerformaten gevalideerd
- [ ] Afrondingsregels correct toegepast
- [ ] Alle getransformeerde velden gevuld
- [ ] Validatie vangt fouten op
- [ ] Exportformaat correct

---

## Gerelateerde Patronen

### Patronen Die Goed Samenwerken:

- **[API Integratie Patroon](api-integration-pattern.md)** - Haal wisselkoersen, verrijkingsgegevens op
- **[PO Matching Patroon](po-matching-pattern.md)** - Variantieberekeningen
- **[Beslissingslogica Patroon](decision-logic-pattern.md)** - Routeer op basis van berekende waarden
- **[Taakbeheer Patroon](task-management-pattern.md)** - Maak taken voor validatiefouten

---

## Gerelateerde Gidsen

### Vereisten
- [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md) - Alle veldoperaties
- [Gids Conditiekaarten](../and/condition-cards-complete-guide.md) - Validatiecondities
- [Call API Gids](../then/action/call-api-guide.md) - Externe gegevens ophalen

### Gerelateerde Kaarten
- **ACTION_CALCULATE_FIELD** - [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** - [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** - [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** - [Call API Gids](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Gids Conditiekaarten](../and/condition-cards-complete-guide.md)

### Volgende Stappen
- Valideer resultaten: [Beslissingslogica Patroon](decision-logic-pattern.md)
- Maak taken voor fouten: [Taakbeheer Patroon](task-management-pattern.md)
- Gebruik in PO-matching: [PO Matching Patroon](po-matching-pattern.md)

---

**Patroonversie:** 1.0
**Laatst Bijgewerkt:** 23 oktober 2025
**Moeilijkheidsgraad:** Gemiddeld
**Geschatte Tijd:** 30-45 minuten
**Succespercentage:** Hoog
