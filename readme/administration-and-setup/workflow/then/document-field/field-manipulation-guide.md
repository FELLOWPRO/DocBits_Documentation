# Cartes de manipulation de champs et de tables

## Cartes de manipulation de terrain et de table - Guide complet

**Couvertures :** 9 cartes pour modifier les champs et les tableaux du document

***

Les cartes de champ et de table de cette page vont dans le groupe **Alors** du Workflow Builder — les actions qui s'exécutent une fois que les conditions Quand/Et correspondent :

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-fr.png" alt="Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution."><figcaption><p>Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution.</p></figcaption></figure>

***

### 📌 Informations sur la version

**Cartes multi-versions :** CALC\_COLUMNS (v2), CALC\_COLUMNS\_REGEX (v2), EDIT\_COLUMN (v2), AI\_CALC\_MTZ\_ETZ (v2)

**Modèle de version :** Toutes les cartes de manipulation de champ suivent le modèle v1 → v2 **Changement de clé :** v2 ajoute la prise en charge de l'internationalisation (i18n) avec les clés de traduction

📖 [Historique complet des versions](../../release.md) | [Versions et comportement des cartes](../../cards-overview/card-versions-guide.md)

***

## Manipulation des champs de documents

### Carte : ACTION\_SET\_FIELD\_TO\_TEXT / Définir le champ sur la valeur du texte

#### Objectif

Remplit automatiquement un champ de document avec un texte spécifique

#### Quand utiliser

* Remplir le champ à partir de la décision
* Définir les valeurs par défaut
* Remplir des informations standardisées
* Mettre à jour le champ en fonction des conditions

#### Comment ça marche

```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

#### Exemples de scénarios

**Scénario 1 : Définir la catégorie d'approbation**

```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Scénario 2 : Définir la catégorie de fournisseur**

```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Scénario 3 : Définir les notes de traitement**

```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

#### Paramètres

**Nom du champ** Quel champ mettre à jour

```
Examples: Category, Type, Status, Comment, Notes
```

**Valeur du texte** Que mettre dans le champ

```
Examples: "Approved", "Pending Review", "High Priority"
```

#### Étapes de configuration

1. Choisissez le champ à remplir
2. Entrez la valeur du texte
3. Définir les conditions (quand remplir)
4. Enregistrer

***

### Carte : ACTION\_SET\_BOOLEAN\_FIELD / Définir le champ de la case à cocher

#### Objectif

Coche ou décoche automatiquement un champ de case à cocher

#### Quand utiliser

* Marquer comme traité
* Définir des indicateurs d'approbation
* Activer/désactiver les options
* Marquer pour l'exportation

#### Comment ça marche

```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

#### Vrai = Coché, Faux = Non coché

**Exemples :**

**Exemple 1 : Marquer comme vérifié**

```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Exemple 2 : indicateur pour révision manuelle**

```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Exemple 3 : Décochez la case pré-remplie**

```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

#### Paramètres

```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

***

### Carte : ACTION\_INVERT\_BOOLEAN\_FIELD / Basculer la case à cocher

#### Objectif

Inverse l'état de la case à cocher (cochée → décochée, vice versa)

#### Quand utiliser

* Changer le statut d'approbation
* Changer de mode de traitement
* Inverser l'état précédent
* Mettre à jour les indicateurs booléens

#### Comment ça marche

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

#### Exemple

```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

***

### Carte : ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD / Copier la valeur du champ

#### Objectif

Copie la valeur d'un champ vers un autre champ

#### Quand utiliser

* Copier les informations du fournisseur dans les informations de facturation
* Données en double dans les champs
* Standardiser le format des données
* Créer une sauvegarde de valeur

#### Comment ça marche

```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

#### Exemples réels

**Exemple 1 : Copier l'adresse de livraison**

```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Exemple 2 : Copier le code du fournisseur**

```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Exemple 3 : Copier le montant pour validation**

```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

#### Paramètres

```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

#### Remarques

* Champ d'origine inchangé
* Champ cible remplacé par la valeur source
* Idéal pour standardiser les données

***

## Manipulation des tableaux

### Carte : EDIT\_COLUMN / Modifier la colonne du tableau

#### Objectif

Modifie les valeurs dans une colonne de tableau en fonction des conditions

#### Quand utiliser

* Corriger les erreurs de tarification dans les lignes du document
* Mettre à jour les quantités
* Corriger les descriptions des articles
* Standardiser les valeurs

#### Comment ça marche

```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

#### Exemple : Fixer le prix

**Scénario : Prix dans une mauvaise devise**

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

#### Paramètres

```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

#### Utilisations courantes

* Fixer les prix unitaires
* Standardiser les descriptions
* Quantités correctes
* Mettre à jour les numéros SKU

***

### Carte : CALC\_COLUMNS / Calculer les valeurs des colonnes

#### Objectif

Effectue le calcul sur les colonnes du tableau et stocke le résultat

#### Quand utiliser

* Calculer les totaux de ligne (Qté × Prix unitaire)
* Colonnes de somme
* Calculer les remises
* Calculer des pourcentages

#### Comment ça marche

```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

#### Types de calcul

**Type 1 : Multiplication simple**

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

**Type 2 : Ajout**

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

**Type 3 : Calcul du pourcentage**

```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Type 4 : Soustraction**

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

#### Exemple concret

**Calcul des éléments de ligne de facture :**

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

#### Paramètres

```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

***

### Carte : CALC\_COLUMNS\_REGEX / Calculer avec le modèle Regex

#### Objectif

Calcule les valeurs des colonnes en fonction de la correspondance de modèles

#### Quand utiliser

* Extraire des valeurs du texte à l'aide de modèles
* Formater les données en fonction de règles
* Convertir les valeurs en fonction de modèles
* Analyser du texte structuré

#### Comment ça marche

**Correspondance de modèles Regex :**

```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

#### Exemple : Extraire le code du fournisseur

**Scénario : les numéros d'article contiennent des informations sur le fournisseur**

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

#### Exemple : formater les numéros de téléphone

**Scénario : Numéros de téléphone non formatés**

```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

#### Exemple : Extraire les prix du texte

**Scénario : Prix au format texte**

```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

#### Paramètres

```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

#### Modèles d'expression régulière courants

```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

***

## Exemples de calcul

### Exemple 1 : calcul du total de la facture

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

### Exemple 2 : calcul de l'écart

```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

### Exemple 3 : Application de réduction

```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

***

## Exemple de workflow de manipulation de champs

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

## Meilleures pratiques

✅ **Faire :**

* Gardez les formules simples
* Tester les calculs avec des exemples de données
* Vérifier que les résultats ont du sens
* Documentez pourquoi vous modifiez les champs
* Utiliser le champ de copie lorsque les données sont identiques

❌ **À ne pas faire :**

* Créer des références circulaires (A=B, B=A)
* Écraser les données importantes sans raison
* Créer des modèles d'expressions régulières trop complexes
* Oublier de vérifier les résultats des calculs
* Calculer sur une mauvaise table/colonne

***

## Dépannage

### "Le champ ne se met pas à jour"

**Cause :** Condition non remplie ou carte non déclenchée

**Solution :**

* Vérifier que la condition est vraie
* Vérifier que la carte est en cours de travail
* Test avec des exemples de données
* Vérifiez les fautes de frappe dans le nom du champ

### "Résultat du calcul erroné"

**Cause :** Mauvaises colonnes sélectionnées ou formule incorrecte

**Solution :**

* Vérifier les colonnes source
* Vérifier que la formule est correcte
* Tester manuellement
* Vérifier les décimales/arrondis

### "Le tableau affiche une erreur"

**Cause :** La colonne référencée n'existe pas

**Solution :**

* Vérifier l'orthographe du nom de la colonne
* Vérifier que la colonne contient des données
* Assurez-vous que le type de données de la colonne correspond au calcul
* Ajoutez les colonnes manquantes si nécessaire

***

## Cartes associées

* **ACTION\_COPY\_DOCFIELD\_TO\_DOCFIELD** - Copier les valeurs
* **EDIT\_COLUMN** - Modifier les valeurs du tableau
* **CALC\_COLUMNS** - Calculer des formules
* **ACTION\_SET\_FIELD\_TO\_TEXT** - Définir les valeurs du texte
* **ACTION\_SET\_BOOLEAN\_FIELD** - Cases à cocher
