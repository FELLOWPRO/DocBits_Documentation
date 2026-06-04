# Cartes de manipulation des champs et des tableaux - Guide complet

Ces cartes se placent dans le groupe **Then** du Concepteur de workflow — les actions exécutées une fois les conditions When/And remplies :

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Les cartes sont ajoutées au groupe <strong>Then</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

**Couvre :** 9 cartes pour modifier les champs et les tableaux des documents

---

# Manipulation des champs de document

## Carte : ACTION_SET_FIELD_TO_TEXT / Set Field to Text Value

### Objectif
Remplit automatiquement un champ de document avec un texte spécifique

### Quand l'utiliser
- Renseigner un champ à partir d'une décision
- Définir des valeurs par défaut
- Remplir des informations standardisées
- Mettre à jour un champ en fonction de conditions

### Comment ça fonctionne
```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

### Exemples de scénarios

**Scénario 1 : Définir la catégorie d'approbation**
```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scénario 2 : Définir la catégorie du fournisseur**
```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scénario 3 : Définir les notes de traitement**
```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

### Paramètres

**Field Name**
Quel champ mettre à jour
```
Examples: Category, Type, Status, Comment, Notes
```

**Text Value**
Quoi mettre dans le champ
```
Examples: "Approved", "Pending Review", "High Priority"
```

### Étapes de configuration
1. Choisissez le champ à remplir
2. Saisissez la valeur textuelle
3. Définissez les conditions (quand remplir)
4. Enregistrez

---

## Carte : ACTION_SET_BOOLEAN_FIELD / Set Checkbox Field

### Objectif
Coche ou décoche automatiquement un champ case à cocher

### Quand l'utiliser
- Marquer comme traité
- Définir des indicateurs d'approbation
- Activer/désactiver des options
- Marquer pour l'exportation

### Comment ça fonctionne
```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

### True = Coché, False = Décoché

**Exemples :**

**Exemple 1 : Marquer comme vérifié**
```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Exemple 2 : Signaler pour révision manuelle**
```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Exemple 3 : Décocher une case pré-remplie**
```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

### Paramètres
```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

---

## Carte : ACTION_INVERT_BOOLEAN_FIELD / Toggle Checkbox

### Objectif
Inverse l'état de la case à cocher (cochée → décochée, et vice versa)

### Quand l'utiliser
- Inverser le statut d'approbation
- Changer de mode de traitement
- Inverser l'état précédent
- Mettre à jour des indicateurs booléens

### Comment ça fonctionne
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

### Exemple
```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

---

## Carte : ACTION_COPY_DOCFIELD_TO_DOCFIELD / Copy Field Value

### Objectif
Copie la valeur d'un champ vers un autre champ

### Quand l'utiliser
- Copier les infos du fournisseur vers les infos de facturation
- Dupliquer des données entre champs
- Standardiser le format des données
- Créer une sauvegarde d'une valeur

### Comment ça fonctionne
```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

### Exemples concrets

**Exemple 1 : Copier l'adresse de livraison**
```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Exemple 2 : Copier le code fournisseur**
```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Exemple 3 : Copier le montant pour validation**
```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

### Paramètres
```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

### Remarques
- Le champ d'origine reste inchangé
- Le champ cible est écrasé par la valeur source
- Idéal pour standardiser les données

---

# Manipulation des tableaux

## Carte : EDIT_COLUMN / Edit Table Column

### Objectif
Modifie les valeurs d'une colonne de tableau en fonction de conditions

### Quand l'utiliser
- Corriger des erreurs de tarification dans les lignes d'articles
- Mettre à jour des quantités
- Corriger les descriptions d'articles
- Standardiser des valeurs

### Comment ça fonctionne
```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

### Exemple : Corriger la tarification

**Scénario : Prix dans la mauvaise devise**
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

### Paramètres
```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

### Utilisations courantes
- Corriger les prix unitaires
- Standardiser les descriptions
- Corriger les quantités
- Mettre à jour les numéros de SKU

---

## Carte : CALC_COLUMNS / Calculate Column Values

### Objectif
Effectue un calcul sur les colonnes d'un tableau et stocke le résultat

### Quand l'utiliser
- Calculer les totaux de ligne (Qté × Prix unitaire)
- Additionner des colonnes
- Calculer des remises
- Calculer des pourcentages

### Comment ça fonctionne
```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

### Types de calcul

**Type 1 : Multiplication simple**
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

**Type 2 : Addition**
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

**Type 3 : Calcul de pourcentage**
```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Type 4 : Soustraction**
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

### Exemple concret

**Calcul des lignes d'articles de facture :**
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

### Paramètres
```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

---

## Carte : CALC_COLUMNS_REGEX / Calculate with Regex Pattern

### Objectif
Calcule les valeurs de colonne en fonction de la correspondance de motifs

### Quand l'utiliser
- Extraire des valeurs d'un texte à l'aide de motifs
- Formater des données selon des règles
- Convertir des valeurs selon des motifs
- Analyser du texte structuré

### Comment ça fonctionne

**Correspondance de motifs regex :**
```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

### Exemple : Extraire le code fournisseur

**Scénario : Les numéros d'article contiennent des infos sur le fournisseur**
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

### Exemple : Formater les numéros de téléphone

**Scénario : Numéros de téléphone non formatés**
```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

### Exemple : Extraire les prix d'un texte

**Scénario : Prix au format texte**
```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

### Paramètres
```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

### Motifs regex courants
```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

---

# Exemples de calcul

## Exemple 1 : Calcul du total de la facture
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

## Exemple 2 : Calcul de l'écart
```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

## Exemple 3 : Application d'une remise
```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

---

# Exemple de flux de travail de manipulation des champs

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

# Bonnes pratiques

✅ **À faire :**
- Garder les formules simples
- Tester les calculs avec des données d'exemple
- Vérifier que les résultats ont du sens
- Documenter pourquoi vous modifiez les champs
- Utiliser la copie de champ lorsque les données sont identiques

❌ **À ne pas faire :**
- Créer des références circulaires (A=B, B=A)
- Écraser des données importantes sans raison
- Créer des motifs regex trop complexes
- Oublier de vérifier les résultats de calcul
- Calculer sur le mauvais tableau/les mauvaises colonnes

---

# Dépannage

## « Le champ ne se met pas à jour »
**Cause :** Condition non remplie ou carte non déclenchée

**Solution :**
- Vérifiez que la condition est vraie
- Vérifiez que la carte est dans le flux de travail
- Testez avec des données d'exemple
- Vérifiez les fautes de frappe dans le nom du champ

## « Résultat de calcul incorrect »
**Cause :** Mauvaises colonnes sélectionnées ou formule incorrecte

**Solution :**
- Vérifiez les colonnes source
- Vérifiez que la formule est correcte
- Testez manuellement
- Vérifiez le nombre de décimales/l'arrondi

## « Le tableau affiche une erreur »
**Cause :** La colonne référencée n'existe pas

**Solution :**
- Vérifiez l'orthographe du nom de la colonne
- Vérifiez que la colonne contient des données
- Assurez-vous que le type de données de la colonne correspond au calcul
- Ajoutez les colonnes manquantes si nécessaire

---

# Cartes associées

- **ACTION_COPY_DOCFIELD_TO_DOCFIELD** - Copier des valeurs
- **EDIT_COLUMN** - Modifier les valeurs d'un tableau
- **CALC_COLUMNS** - Calculer des formules
- **ACTION_SET_FIELD_TO_TEXT** - Définir des valeurs textuelles
- **ACTION_SET_BOOLEAN_FIELD** - Cocher des cases
