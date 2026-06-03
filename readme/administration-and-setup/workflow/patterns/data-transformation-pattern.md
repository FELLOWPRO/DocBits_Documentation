# Modèle de transformation des données

**Type de modèle :** Traitement & manipulation de données
**Complexité :** Moyenne
**Mise en place estimée :** 30-45 minutes
**Cas d'usage courants :** Calculs de champs, formatage de données, conversion de devises, conversion d'unités, enrichissement de données

---

Vous construisez ce modèle dans le **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Cliquez sur **Add Card** et ouvrez la catégorie **Document Field** — elle contient les cartes de lecture, d'écriture, de calcul et de formatage que ce modèle enchaîne :

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Bibliothèque Add Card dans le Workflow Builder, regroupée par catégorie"><figcaption><p>La bibliothèque <strong>Add Card</strong> — les cartes de lecture/écriture de champs, de calcul et de formatage se trouvent sous la catégorie <strong>Document Field</strong>.</p></figcaption></figure>

---

## Vue d'ensemble du modèle

Ce modèle montre comment transformer, calculer, formater et enrichir les données des documents dans les workflows DocBits. La transformation des données est essentielle pour préparer les données à l'export, effectuer des calculs, standardiser les formats et enrichir les documents avec des informations supplémentaires.

**Ce que fait ce modèle :**
1. Extrait des données des champs de document
2. Effectue des calculs et des transformations
3. Formate les données aux standards requis
4. Convertit entre unités, devises et dates
5. Enrichit les documents avec des données dérivées ou recherchées
6. Valide et nettoie les données

---

## Quand utiliser ce modèle

Utilisez ce modèle lorsque vous devez :
- ✅ Calculer des totaux, sous-totaux, taxes
- ✅ Convertir des devises ou des unités
- ✅ Formater des dates, des nombres, du texte
- ✅ Dériver des valeurs à partir de champs existants
- ✅ Enrichir les données à partir de sources externes
- ✅ Standardiser les formats de données
- ✅ Nettoyer et valider les données
- ✅ Préparer les données pour l'export

**N'utilisez pas ce modèle lorsque :**
- ❌ aucune transformation n'est nécessaire
- ❌ les données sont déjà au bon format
- ❌ une simple copie de champs suffit

---

## Types de transformation des données

### 1. Calculs

**Opérations mathématiques :**
```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. Opérations sur les chaînes de caractères

**Manipulation de texte :**
```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. Conversion de type de données

**Conversions de type :**
```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. Conversions d'unités

**Conversions d'unités de mesure :**
```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. Conversions de devises

**Application de taux de change :**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. Transformations de dates

**Opérations sur les dates :**
```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

---

## Exemple complet de workflow

### Scénario : Calcul de la somme d'une facture & enrichissement des données

**Exigence métier :**
- Extraire les positions de la facture
- Calculer les sommes des positions (quantité × prix)
- Calculer le sous-total (somme des sommes des positions)
- Calculer le montant de la taxe (sous-total × taux de taxe)
- Calculer la somme totale (sous-total + taxe)
- Convertir en EUR si la facture est dans une autre devise
- Formater les montants à 2 décimales
- Ajouter le compte général en fonction de la catégorie de produit
- Valider les calculs par rapport à la somme de la facture
- Marquer si l'écart est > 1 %

**Cartes de workflow utilisées :**
1. ACTION_CALCULATE_FIELD – Effectuer les calculs
2. ACTION_SET_FIELD_TO_TEXT – Stocker les résultats
3. ACTION_COPY_FIELD_VALUE – Copier les valeurs
4. CALL_API – Récupérer les taux de change (si nécessaire)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES – Valider les calculs
6. ACTION_SET_FIELD_FROM_MASTER_DATA – Enrichir avec les comptes généraux

---

## Mise en œuvre étape par étape

### Étape 1 : Calculs des positions

**Calculer les sommes des positions :**

**Carte :** ACTION_CALCULATE_FIELD

**Pour chaque position :**
```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**Exemple :**
```
Line 1:
  Quantity: 100
  Unit Price: €50.00
  Calculation: 100 × 50.00 = €5,000.00
  Store in: Line_Total

Line 2:
  Quantity: 50
  Unit Price: €20.00
  Calculation: 50 × 20.00 = €1,000.00
  Store in: Line_Total

Line 3:
  Quantity: 25
  Unit Price: €15.50
  Calculation: 25 × 15.50 = €387.50
  Store in: Line_Total
```

**Référence du guide :** [Guide de manipulation des champs – Calculs](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Étape 2 : Calculer le sous-total du document

**Additionner toutes les sommes des positions :**

**Carte :** ACTION_CALCULATE_FIELD

**Configuration :**
```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**Exemple :**
```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

---

### Étape 3 : Calculer le montant de la taxe

**Appliquer le taux de taxe au sous-total :**

**Carte :** ACTION_CALCULATE_FIELD

**Configuration :**
```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**Exemple :**
```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

---

### Étape 4 : Calculer la somme totale

**Additionner le sous-total et la taxe :**

**Carte :** ACTION_CALCULATE_FIELD

**Configuration :**
```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**Exemple :**
```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

---

### Étape 5 : Conversion de devise (si nécessaire)

**Vérifier si une conversion est nécessaire :**

**Carte :** CONDITION_DOC_FIELD_IS

**Configuration :**
```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**Si une conversion est nécessaire :**

**Étape 5a : Récupérer le taux de change**

**Carte :** CALL_API

**Configuration :**
```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**Exemple :**
```
Invoice Currency: USD
API Response: {
  "base": "USD",
  "rates": {
    "EUR": 0.92
  }
}

Exchange_Rate_To_EUR = 0.92
```

**Étape 5b : Convertir les montants**

**Carte :** ACTION_CALCULATE_FIELD

**Configuration :**
```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**Exemple :**
```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**Référence du guide :** [Modèle d'intégration d'API – Conversion de devise](api-integration-pattern.md#exemple-1-recherche-de-taux-de-change)

---

### Étape 6 : Enrichissement des données – Ajouter les comptes généraux

**Rechercher le compte général à partir de la catégorie de produit :**

**Carte :** ACTION_SET_FIELD_FROM_MASTER_DATA

**Configuration :**
```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**Exemple :**
```
Line 1:
  Product Category: "Office Supplies"
  Lookup → GL_Account_Mapping table
  Result: GL Account "4200-100" (Office Expense)

Line 2:
  Product Category: "IT Equipment"
  Lookup → GL_Account_Mapping table
  Result: GL Account "6100-200" (IT Assets)

Line 3:
  Product Category: "Services"
  Lookup → GL_Account_Mapping table
  Result: GL Account "5000-300" (Services Expense)
```

**Référence du guide :** [Guide de manipulation des champs – Données de référence](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Étape 7 : Valider les calculs

**Comparer la somme calculée à la somme de la facture :**

**Carte :** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configuration :**
```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**Calcul :**
```
Variance % = |Calculated - Invoice| / Invoice × 100

Example:
  Calculated Total: €7,601.13
  Invoice Total: €7,600.00

  Variance = |7601.13 - 7600.00| / 7600.00 × 100
          = 1.13 / 7600.00 × 100
          = 0.015%

  Is 0.015% ≤ 1% tolerance? YES ✅
  Result: PASS (calculations match invoice)
```

**Logique :**
```
IF Variance ≤ 1%:
  Set Validation_Status = "PASS"
  Continue processing
ELSE:
  Set Validation_Status = "FAIL"
  Create review task
  Flag for manual verification
```

**Référence du guide :** [Guide des cartes de condition – Comparaison de champs](../and/condition-cards-complete-guide.md#field-comparison)

---

### Étape 8 : Formater les données pour l'export

**Standardiser les formats :**

**Carte :** ACTION_SET_FIELD_TO_TEXT

**Formatage des dates :**
```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**Formatage des nombres :**
```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**Formatage du texte :**
```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

---

## Transformations avancées

### Transformation 1 : Calcul de taxe à plusieurs niveaux

**Scénario :** Taux de taxe différents par position

```
Line 1: Product A (Tax Rate 19%)
Line 2: Product B (Tax Rate 7% - reduced)
Line 3: Product C (Tax Rate 0% - exempt)

Calculation:
  Line 1 Tax = €5,000.00 × 0.19 = €950.00
  Line 2 Tax = €1,000.00 × 0.07 = €70.00
  Line 3 Tax = €387.50 × 0.00 = €0.00

  Total Tax = €950.00 + €70.00 + €0.00 = €1,020.00
```

**Mise en œuvre :**
```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

---

### Transformation 2 : Calculs de remises

**Scénario :** Appliquer une remise sur volume et un escompte

```
Original Subtotal: €10,000.00

Step 1: Volume Discount (10% for orders > €5,000)
  Discount = €10,000.00 × 0.10 = €1,000.00
  After Volume Discount = €10,000.00 - €1,000.00 = €9,000.00

Step 2: Early Payment Discount (2% if paid within 10 days)
  Discount = €9,000.00 × 0.02 = €180.00
  After Payment Discount = €9,000.00 - €180.00 = €8,820.00

Step 3: Calculate Tax (on discounted amount)
  Tax = €8,820.00 × 0.19 = €1,675.80

Final Total = €8,820.00 + €1,675.80 = €10,495.80
```

**Mise en œuvre :**
```
1. Check order value for volume discount eligibility
2. Calculate volume discount
3. Apply volume discount to subtotal
4. Check payment terms for early payment discount
5. Calculate early payment discount
6. Apply early payment discount
7. Calculate tax on final discounted amount
8. Calculate grand total
```

---

### Transformation 3 : Conversion de l'unité de mesure

**Scénario :** Convertir l'unité de mesure de la facture dans l'unité standard

```
Invoice shows:
  Product: Steel Rods
  Quantity: 50
  Unit: Meters
  Unit Price: €10.00/meter
  Line Total: €500.00

Company standard UOM: Feet

Conversion:
  1 meter = 3.28084 feet

  Quantity (feet) = 50 meters × 3.28084 = 164.042 feet
  Unit Price (feet) = €10.00/meter ÷ 3.28084 = €3.05/foot

  Verification: 164.042 feet × €3.05/foot ≈ €500.00 ✅
```

**Mise en œuvre :**
```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

---

### Transformation 4 : Calculs de dates

**Scénario :** Calculer les conditions de paiement et les dates d'échéance

```
Invoice Date: 2025-10-23
Payment Terms: NET30

Calculations:
  Due Date = Invoice Date + 30 days = 2025-11-22

  Early Payment Discount Available If:
    Payment Date ≤ Invoice Date + 10 days
    Discount End Date = 2025-11-02

  Days Until Due = Due Date - Today
    If Today = 2025-10-23: Days = 30
    If Today = 2025-11-15: Days = 7
    If Today = 2025-11-23: Days = -1 (overdue)
```

**Mise en œuvre :**
```
1. Extract Invoice_Date
2. Extract Payment_Terms (e.g., "NET30", "NET60", "2/10 NET30")
3. Parse payment terms
4. Calculate Due_Date
5. Calculate Discount_End_Date (if applicable)
6. Calculate Days_Until_Due
7. Set Status: "Current", "Due Soon", "Overdue"
```

---

### Transformation 5 : Analyse & extraction de texte

**Scénario :** Extraire des données structurées d'un texte non structuré

```
Original Field: "PO-2025-ABC-12345-REV2"

Extract:
  Year: "2025"
  Department: "ABC"
  PO Number: "12345"
  Revision: "2"

Method:
  Split by delimiter "-"
  Array: ["PO", "2025", "ABC", "12345", "REV2"]

  Extract:
    Year = Array[1] = "2025"
    Department = Array[2] = "ABC"
    PO_Number = Array[3] = "12345"
    Revision = Extract digits from Array[4] = "2"
```

---

## Diagramme complet du workflow de transformation

```
INVOICE DATA EXTRACTED
│
├─ STEP 1: LINE ITEM CALCULATIONS
│  For each line:
│    Quantity × Unit_Price = Line_Total
│  Result: Line totals calculated
│
├─ STEP 2: SUBTOTAL CALCULATION
│  SUM(All Line_Totals) = Subtotal
│  Result: €6,387.50
│
├─ STEP 3: TAX CALCULATION
│  Subtotal × Tax_Rate = Tax_Amount
│  €6,387.50 × 19% = €1,213.63
│
├─ STEP 4: GRAND TOTAL CALCULATION
│  Subtotal + Tax_Amount = Grand_Total
│  €6,387.50 + €1,213.63 = €7,601.13
│
├─ STEP 5: CURRENCY CHECK
│  │
│  ├─ Currency = EUR? YES
│  │  → Skip conversion
│  │  → Use Grand_Total as is
│  │
│  └─ Currency ≠ EUR? NO (e.g., USD)
│     │
│     ├─ Call Exchange Rate API
│     │  Get: USD → EUR rate (0.92)
│     │
│     ├─ Convert Amount
│     │  $7,601.13 × 0.92 = €6,993.04
│     │
│     └─ Store converted amount
│        Grand_Total_EUR = €6,993.04
│
├─ STEP 6: DATA ENRICHMENT
│  For each line:
│    Lookup Product_Category → GL_Account
│    Store GL_Account in line item
│  Result: All lines have GL accounts
│
├─ STEP 7: VALIDATION
│  │
│  ├─ Compare Calculated vs Invoice Total
│  │  Variance = |Calculated - Invoice| / Invoice × 100
│  │
│  ├─ Variance ≤ 1%? ✅
│  │  Set Validation_Status = "PASS"
│  │  Continue processing
│  │
│  └─ Variance > 1%? ❌
│     Set Validation_Status = "FAIL"
│     Create review task
│     Flag for manual check
│
├─ STEP 8: FORMATTING
│  │
│  ├─ Format Dates
│  │  10/23/2025 → 2025-10-23
│  │
│  ├─ Format Numbers
│  │  7601.13 → 7.601,13 (locale-specific)
│  │
│  ├─ Format Text
│  │  "abc corp" → "ABC CORP"
│  │
│  └─ Format for Export
│     All fields in ERP-compatible format
│
└─ TRANSFORMATION COMPLETE
   Document ready for next workflow step
```

---

## Gabarits de configuration

### Gabarit 1 : Calculs de facture standard

```json
{
  "transformations": [
    {
      "step": 1,
      "name": "Calculate Line Totals",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Quantity}} * {{Unit_Price}}",
      "result_field": "Line_Total"
    },
    {
      "step": 2,
      "name": "Calculate Subtotal",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "SUM({{Line_Total}})",
      "result_field": "Calculated_Subtotal"
    },
    {
      "step": 3,
      "name": "Calculate Tax",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} * {{Tax_Rate}} / 100",
      "result_field": "Calculated_Tax"
    },
    {
      "step": 4,
      "name": "Calculate Total",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} + {{Calculated_Tax}}",
      "result_field": "Calculated_Total"
    }
  ]
}
```

---

### Gabarit 2 : Workflow de conversion de devise

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

## Gestion des erreurs

### Erreurs de transformation courantes

**Erreur 1 : Division par zéro**
```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**Erreur 2 : Format de nombre invalide**
```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**Erreur 3 : Échec de l'analyse de date**
```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**Erreur 4 : Facteur de conversion manquant**
```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

---

## Liste de vérification de test

- [ ] Tous les calculs produisent des résultats corrects
- [ ] La précision décimale est conservée
- [ ] Les conversions de devises sont correctes
- [ ] Les calculs de dates sont corrects
- [ ] Les transformations de texte fonctionnent
- [ ] Les valeurs nulles/vides sont gérées
- [ ] La division par zéro est empêchée
- [ ] Les formats de nombres sont validés
- [ ] Les règles d'arrondi sont correctement appliquées
- [ ] Tous les champs transformés sont renseignés
- [ ] La validation détecte les erreurs
- [ ] Le format d'export est correct

---

## Modèles connexes

### Modèles qui fonctionnent bien ensemble :

- **[Modèle d'intégration d'API](api-integration-pattern.md)** – Récupérer les taux de change et les données d'enrichissement
- **[Modèle de rapprochement de commandes (PO Matching)](po-matching-pattern.md)** – Calculs d'écarts
- **[Modèle de logique de décision](decision-logic-pattern.md)** – Router en fonction des valeurs calculées
- **[Modèle de gestion des tâches](task-management-pattern.md)** – Créer des tâches en cas d'échec de validation

---

## Guides connexes

### Prérequis
- [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md) – Toutes les opérations sur les champs
- [Guide des cartes de condition](../and/condition-cards-complete-guide.md) – Conditions de validation
- [Guide Call API](../then/action/call-api-guide.md) – Récupération de données externes

### Cartes connexes
- **ACTION_CALCULATE_FIELD** – [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** – [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** – [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** – [Guide Call API](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md)

### Prochaines étapes
- Valider les résultats : [Modèle de logique de décision](decision-logic-pattern.md)
- Créer des tâches pour les erreurs : [Modèle de gestion des tâches](task-management-pattern.md)
- Utiliser dans le rapprochement de commandes : [Modèle de rapprochement de commandes (PO Matching)](po-matching-pattern.md)

---

**Version du modèle :** 1.0
**Dernière mise à jour :** 23 octobre 2025
**Difficulté :** Moyenne
**Temps estimé :** 30-45 minutes
**Taux de réussite :** Élevé
