# Modèle de rapprochement de commandes (PO Matching)

**Type de modèle :** Validation & comparaison
**Complexité :** Moyenne-Élevée
**Mise en place estimée :** 60-90 minutes
**Cas d'usage courants :** Rapprochement à trois voies, validation de factures, contrôle des écarts, gestion des tolérances

---

Vous construisez ce modèle dans le **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Cliquez sur **Add Card** et ouvrez la catégorie **Compare with Purchase Order** — elle contient toutes les cartes de rapprochement utilisées par ce modèle (cartes de comparaison de prix, de quantité, de tolérance et de position) :

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Bibliothèque Add Card affichant les cartes Compare with Purchase Order"><figcaption><p>La catégorie <strong>Compare with Purchase Order</strong> — cartes de rapprochement de prix, de quantité, de tolérance et de position utilisées tout au long de ce modèle.</p></figcaption></figure>

---

## Vue d'ensemble du modèle

Ce modèle montre comment mettre en place des workflows complets de rapprochement de commandes (PO Matching) dans DocBits. Le rapprochement de commandes est un processus de contrôle critique qui compare les données de facture aux données de commande afin de détecter les écarts avant l'approbation du paiement.

**Ce que fait ce modèle :**
1. Récupère les données de commande à partir du numéro de commande figurant sur la facture
2. Compare les positions de la facture aux positions de la commande
3. Calcule les écarts (prix, quantité, totaux)
4. Applique les règles de tolérance
5. Route vers l'approbation ou l'escalade en fonction des résultats du rapprochement
6. Suit l'historique des rapprochements et les exceptions

---

## Quand utiliser ce modèle

Utilisez ce modèle lorsque vous devez :
- ✅ Valider les factures par rapport aux commandes
- ✅ Détecter les erreurs de prix avant le paiement
- ✅ Identifier les écarts de quantité
- ✅ Faire respecter les contrôles d'approvisionnement
- ✅ Empêcher les paiements en double
- ✅ Automatiser le rapprochement à trois voies
- ✅ Réduire la charge de révision manuelle des factures

**N'utilisez pas ce modèle lorsque :**
- ❌ aucune commande n'existe pour la facture (factures sans commande)
- ❌ les données de commande ne sont pas disponibles dans DocBits
- ❌ une révision manuelle est préférée à l'automatisation
- ❌ le rapprochement de commandes n'est pas requis par la politique de l'entreprise

---

## Comprendre le rapprochement de commandes

### Le rapprochement à trois voies

**Contrôle d'approvisionnement classique :**
```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**Mise en œuvre dans DocBits (rapprochement à deux voies) :**
```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

---

## Formules de calcul des écarts

### Écart de prix unitaire

**Formule :**
```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**Exemple :**
```
PO Unit Price:       €100.00
Invoice Unit Price:  €103.00

Variance = |103 - 100| / 100 × 100
        = 3 / 100 × 100
        = 3%

Tolerance: 5%
Result: 3% ≤ 5% → PASS ✅
```

---

### Écart de quantité

**Formule :**
```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**Exemple :**
```
PO Quantity:        100 units
Invoice Quantity:   98 units

Variance = |98 - 100| / 100 × 100
        = 2 / 100 × 100
        = 2%

Tolerance: 10%
Result: 2% ≤ 10% → PASS ✅
```

---

### Écart de montant total

**Formule :**
```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**Exemple :**
```
PO Total:       €10,000.00
Invoice Total:  €10,450.00

Variance = |10450 - 10000| / 10000 × 100
        = 450 / 10000 × 100
        = 4.5%

Tolerance: 5%
Result: 4.5% ≤ 5% → PASS ✅
```

---

## Exemple complet de workflow

### Scénario : Validation de facture avec routage basé sur la tolérance

**Exigence métier :**
- Toutes les factures avec référence de commande doivent être validées
- Tolérance pour l'écart de prix : 5 %
- Tolérance pour l'écart de quantité : 10 %
- Tolérance pour l'écart de montant total : 3 %
- Dans la tolérance : Approbation automatique
- Hors tolérance : Créer une tâche de révision
- Commande manquante : Escalader vers les achats

**Cartes de workflow utilisées :**
1. CONDITION_DOC_FIELD_EXISTS – Vérifier si le numéro de commande est présent
2. PURCHASE_ORDER_FULL_MATCH – Tenter un rapprochement complet
3. CONDITION_DOC_TO_PO_UNIT_PRICE – Vérifier l'écart de prix
4. CONDITION_DOC_TO_PO_QUANTITY – Vérifier l'écart de quantité
5. CONDITION_DOC_TO_PO_TAX_LINES – Vérifier le rapprochement des taxes
6. ACTION_SET_FIELD_TO_TEXT – Stocker les résultats du rapprochement
7. tasks_create – Créer des tâches de révision
8. ACTION_SEND_EMAIL_TO_GROUPS – Envoyer des notifications

---

## Mise en œuvre étape par étape

### Étape 1 : Vérifier la référence de commande

**Carte :** CONDITION_DOC_FIELD_EXISTS ou CONDITION_DOC_FIELD_CONTAINS

**Configuration :**
```
Field: PO_Number
Operator: IS NOT EMPTY
```

**Logique :**
```
IF PO_Number exists:
  → Continue to PO matching
ELSE:
  → Route to "Non-PO Invoice" workflow
  → Create manual review task
  → Skip PO matching
```

**Référence du guide :** [Guide des cartes de condition](../and/condition-cards-complete-guide.md)

---

### Étape 2 : Récupérer les données de commande

**Automatique dans DocBits :**
- Le système recherche la commande à partir du champ PO_Number
- Récupère les positions de la commande
- Met les données à disposition pour la comparaison

**Configuration manuelle (si nécessaire) :**
```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

---

### Étape 3 : Vérifier le rapprochement complet

**Carte :** PURCHASE_ORDER_FULL_MATCH

**Objectif :** Vérification rapide que tout correspond parfaitement

**Configuration :**
```
Match Level: Full Match
Include: All line items, prices, quantities, totals
Tolerance: None (exact match)
```

**Logique :**
```
IF Full Match = TRUE:
  → Set "PO_Match_Status" = "FULL MATCH"
  → Auto-approve document
  → Skip detailed checks
  → END ✅

IF Full Match = FALSE:
  → Continue to detailed variance checks
  → Identify specific variances
```

**Résultat :**
- **TRUE** : Correspondance parfaite, approbation automatique
- **FALSE** : Poursuivre avec les vérifications détaillées

---

### Étape 4 : Vérifier l'écart de prix unitaire

**Carte :** CONDITION_DOC_TO_PO_UNIT_PRICE (v5 recommandée)

**Configuration :**
```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**Étape par étape :**
```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**Exemple de calcul :**
```
Line Item 1:
  Product: ABC123
  Invoice Price: €52.00
  PO Price: €50.00
  Variance = |52-50|/50 × 100 = 4%
  Tolerance: 5%
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Price: €120.00
  PO Price: €100.00
  Variance = |120-100|/100 × 100 = 20%
  Tolerance: 5%
  Result: FAIL ❌

Overall Result: FAIL (one or more items failed)
```

**Référence du guide :** [Guide complet du PO Matching – Prix unitaire](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---

### Étape 5 : Vérifier l'écart de quantité

**Carte :** CONDITION_DOC_TO_PO_QUANTITY

**Configuration :**
```
Comparison Mode: Percentage Variance
Tolerance: 10%
Operator: Variance is Less Than or Equal To
Apply To: All line items
Allow Under-Delivery: Yes (within tolerance)
Allow Over-Delivery: No (strict)
```

**Logique :**
```
For each line item:
  1. Get Invoice Quantity
  2. Get PO Quantity
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 10%?
  5. Special rules:
     - Under-delivery: Allow within tolerance
     - Over-delivery: Reject (or apply stricter tolerance)
```

**Exemple :**
```
Line Item 1:
  Product: ABC123
  Invoice Qty: 98 units
  PO Qty: 100 units
  Variance = |98-100|/100 × 100 = 2%
  Under-delivery: 2% (within 10% tolerance)
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Qty: 115 units
  PO Qty: 100 units
  Variance = |115-100|/100 × 100 = 15%
  Over-delivery: 15% (exceeds 10% tolerance)
  Result: FAIL ❌ (Escalate)
```

**Référence du guide :** [Guide complet du PO Matching – Quantité](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---

### Étape 6 : Vérifier le rapprochement des lignes de taxe

**Carte :** CONDITION_DOC_TO_PO_TAX_LINES

**Configuration :**
```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**Validation :**
```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**Exemple :**
```
Invoice:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

PO:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

Result: Tax alignment PASS ✅
```

---

### Étape 7 : Stocker les résultats du rapprochement

**Carte :** ACTION_SET_FIELD_TO_TEXT (plusieurs instances)

**Configuration :**

**Champ 1 : PO_Match_Status**
```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Champ 2 : Price_Variance_Percent**
```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**Champ 3 : Quantity_Variance_Percent**
```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**Champ 4 : Match_Details**
```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**Référence du guide :** [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md)

---

### Étape 8 : Router en fonction des résultats du rapprochement

**Scénario A : Correspondance parfaite (rapprochement complet)**
```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**Scénario B : Dans la tolérance**
```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**Scénario C : Hors tolérance (mineur)**
```
IF Variance < 15% (minor exceptions):
  1. Set Match_Status = "REVIEW REQUIRED"
  2. Create Task: "Review PO Variance"
     - Assign to: Accounts Payable Officer
     - Priority: Medium
     - Deadline: 3 days
  3. Send email with variance details
  4. Wait for task completion
  5. IF Approved: Continue processing
     IF Rejected: Return to supplier
```

**Scénario D : Hors tolérance (majeur)**
```
IF Variance ≥ 15% (major exceptions):
  1. Set Match_Status = "ESCALATION REQUIRED"
  2. Create Task: "URGENT: Major PO Variance"
     - Assign to: Procurement Manager
     - Priority: High
     - Deadline: 1 day
  3. Send urgent email to:
     - Procurement Manager
     - Finance Manager
     - Supplier contact
  4. Block document from processing
  5. Wait for resolution
```

**Scénario E : Commande manquante ou aucune correspondance**
```
IF PO not found OR no items match:
  1. Set Match_Status = "NO MATCH"
  2. Create Task: "PO Not Found"
     - Assign to: Procurement Team
     - Priority: High
  3. Send email to procurement
  4. Block document
  5. Request PO creation or correction
```

---

## Diagramme de workflow complet

```
INVOICE ARRIVES
│
├─ CHECK: Does invoice have PO number?
│  │
│  ├─ NO PO NUMBER ❌
│  │  │
│  │  ├─ Set Match_Status = "NO PO"
│  │  ├─ Route to Non-PO workflow
│  │  └─ Create manual review task
│  │     → END (Non-PO Invoice)
│  │
│  └─ PO NUMBER EXISTS ✅
│     │
│     ├─ RETRIEVE PO DATA
│     │  - Lookup PO by PO_Number
│     │  - Get PO line items
│     │  - Get PO totals
│     │  │
│     │  ├─ PO FOUND ✅
│     │  │  │
│     │  │  ├─ STEP 1: Check Full Match
│     │  │  │  Card: PURCHASE_ORDER_FULL_MATCH
│     │  │  │  │
│     │  │  │  ├─ FULL MATCH ✅✅✅
│     │  │  │  │  │
│     │  │  │  │  ├─ Set Match_Status = "FULL MATCH"
│     │  │  │  │  ├─ Auto-Approve
│     │  │  │  │  └─ Export to ERP
│     │  │  │  │     → END (Perfect Match)
│     │  │  │  │
│     │  │  │  └─ NO FULL MATCH ⚠️
│     │  │  │     │
│     │  │  │     ├─ STEP 2: Check Unit Price Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_UNIT_PRICE
│     │  │  │     │  Tolerance: 5%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Invoice-PO|/PO × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ PRICE VARIANCE ≤ 5% ✅
│     │  │  │     │  │  Store variance: 3.2% (example)
│     │  │  │     │  │  Price Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ PRICE VARIANCE > 5% ❌
│     │  │  │     │     Store variance: 12.5% (example)
│     │  │  │     │     Price Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 3: Check Quantity Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_QUANTITY
│     │  │  │     │  Tolerance: 10%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Inv Qty-PO Qty|/PO Qty × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ QUANTITY VARIANCE ≤ 10% ✅
│     │  │  │     │  │  Store variance: 2.0% (example)
│     │  │  │     │  │  Quantity Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ QUANTITY VARIANCE > 10% ❌
│     │  │  │     │     Store variance: 15.0% (example)
│     │  │  │     │     Quantity Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 4: Check Tax Lines
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_TAX_LINES
│     │  │  │     │  │
│     │  │  │     │  ├─ TAX ALIGNED ✅
│     │  │  │     │  │  Tax Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ TAX MISMATCH ❌
│     │  │  │     │     Tax Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ EVALUATE RESULTS
│     │  │  │     │  │
│     │  │  │     │  ├─ ALL CHECKS PASS ✅
│     │  │  │     │  │  (Within tolerance)
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "WITHIN TOLERANCE"
│     │  │  │     │  │  ├─ Log variance details
│     │  │  │     │  │  ├─ Auto-Approve
│     │  │  │     │  │  └─ Export to ERP
│     │  │  │     │  │     → END (Approved with Variance)
│     │  │  │     │  │
│     │  │  │     │  ├─ MINOR FAILURES (Variance < 15%) ⚠️
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "REVIEW REQUIRED"
│     │  │  │     │  │  ├─ Create Review Task
│     │  │  │     │  │  │  - Assign to: AP Officer
│     │  │  │     │  │  │  - Priority: Medium
│     │  │  │     │  │  │  - Deadline: 3 days
│     │  │  │     │  │  ├─ Send email with details
│     │  │  │     │  │  │
│     │  │  │     │  │  └─ WAIT FOR TASK COMPLETION
│     │  │  │     │  │     │
│     │  │  │     │  │     ├─ TASK APPROVED ✅
│     │  │  │     │  │     │  Approve & Export
│     │  │  │     │  │     │  → END (Manual Approval)
│     │  │  │     │  │     │
│     │  │  │     │  │     └─ TASK REJECTED ❌
│     │  │  │     │  │        Reject & Return to Supplier
│     │  │  │     │  │        → END (Rejected)
│     │  │  │     │  │
│     │  │  │     │  └─ MAJOR FAILURES (Variance ≥ 15%) 🚨
│     │  │  │     │     │
│     │  │  │     │     ├─ Set Match_Status = "ESCALATION"
│     │  │  │     │     ├─ Create Urgent Task
│     │  │  │     │     │  - Assign to: Procurement Manager
│     │  │  │     │     │  - Priority: High
│     │  │  │     │     │  - Deadline: 1 day
│     │  │  │     │     ├─ Send urgent emails to:
│     │  │  │     │     │  * Procurement Manager
│     │  │  │     │     │  * Finance Manager
│     │  │  │     │     │  * Supplier
│     │  │  │     │     ├─ Block document processing
│     │  │  │     │     │
│     │  │  │     │     └─ WAIT FOR RESOLUTION
│     │  │  │     │        → END (Pending Escalation)
│     │  │  │     │
│     │  │  │     └─ [Variance checks complete]
│     │  │  │
│     │  │  └─ [Full match check complete]
│     │  │
│     │  └─ PO NOT FOUND ❌
│     │     │
│     │     ├─ Set Match_Status = "PO NOT FOUND"
│     │     ├─ Create Task: "Missing PO"
│     │     │  - Assign to: Procurement Team
│     │     │  - Priority: High
│     │     ├─ Send email to procurement
│     │     └─ Block document
│     │        → END (Missing PO)
│     │
│     └─ [PO retrieval complete]
│
└─ [PO check complete]
```

---

## Gabarits de configuration

### Gabarit 1 : Rapprochement de commandes standard (conservateur)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 3,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": false
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": true,
    "match_tax_rates": true,
    "tax_amount_tolerance": 0.5
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 10,
    "assign_to": "procurement_manager"
  }
}
```

**Utilisation :** Environnement strictement contrôlé, faible tolérance aux écarts

---

### Gabarit 2 : Rapprochement de commandes flexible (souple)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 10,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 15,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": true
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": false,
    "match_tax_rates": true,
    "tax_amount_tolerance": 2
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 20,
    "assign_to": "accounts_payable"
  }
}
```

**Utilisation :** Environnement flexible, fournisseurs de confiance, tolérance plus élevée

---

### Gabarit 3 : Rapprochement de prix uniquement

```json
{
  "full_match_check": false,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": false
  },
  "tax_validation": {
    "enabled": false
  },
  "auto_approve": {
    "full_match": false,
    "within_tolerance": true
  }
}
```

**Utilisation :** Lorsque seul le prix compte et que des écarts de quantité sont attendus

---

## Scénarios avancés

### Scénario 1 : Gestion des livraisons partielles

**Défi :** Facture pour une livraison partielle d'une commande

**Solution :**
```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**Mise en œuvre :**
```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

---

### Scénario 2 : Rapprochement de commandes multidevises

**Défi :** La devise de la facture diffère de la devise de la commande

**Solution :**
```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**Mise en œuvre :**
```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

---

### Scénario 3 : Commande cadre / accord-cadre

**Défi :** Plusieurs factures pour une seule commande

**Solution :**
```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**Mise en œuvre :**
```
IF PO_Type = "Blanket":
  Calculate: Total_Invoiced_To_Date
  Check: Total_Invoiced_To_Date + Current_Invoice ≤ PO_Total_Value
  IF Within limit:
    Approve invoice
    Update: Remaining_PO_Value
  ELSE:
    Escalate: "Blanket PO limit exceeded"
```

---

## Gestion des erreurs & cas particuliers

### Cas particulier 1 : Position manquante sur la facture

**Problème :** La facture contient une position qui ne figure pas sur la commande

**Solution :**
```
1. Identify unmatched line items
2. Calculate: Unmatched_Amount
3. IF Unmatched_Amount < €100 (threshold):
     Create review task (minor issue)
   ELSE:
     Escalate immediately (major issue)
4. Store unmatched item details
5. Flag: "Additional_Items_Present"
```

---

### Cas particulier 2 : Commande clôturée, mais une facture arrive

**Problème :** Commande déjà clôturée, facture tardive reçue

**Solution :**
```
1. Check: PO_Status = "CLOSED"
2. Check: Invoice_Date vs PO_Close_Date
3. IF Invoice within 30 days of close:
     Reopen PO temporarily
     Process invoice
     Close PO again
   ELSE:
     Create task: "Late Invoice for Closed PO"
     Assign to procurement
     Manual decision required
```

---

### Cas particulier 3 : Plusieurs commandes sur une seule facture

**Problème :** La facture fait référence à plusieurs commandes

**Solution :**
```
1. Parse invoice for multiple PO numbers
2. For each PO:
     Retrieve PO data
     Match respective line items
3. Aggregate match results
4. Overall match = ALL individual POs must match
5. Report on each PO separately
```

---

## Conseils de performance

✅ **Bonnes pratiques :**
- Mettre en cache les données de commande pour réduire les recherches
- Définir des tolérances appropriées (ni trop strictes, ni trop souples)
- Vérifier d'abord le rapprochement complet (plus rapide)
- Journaliser tous les calculs d'écart
- Réviser les réglages de tolérance trimestriellement
- Surveiller les taux d'approbation automatique
- Suivre les motifs d'écart fréquents

❌ **À éviter :**
- Tolérance zéro (trop stricte, trop de révisions manuelles)
- Tolérance extrêmement élevée (détourne l'objectif)
- Ignorer les écarts systématiques
- Ne pas suivre les tendances d'écart
- Traiter sans commande (lorsqu'elle est requise)

---

## Surveillance & reporting

### Indicateurs clés à suivre

1. **Taux de rapprochement :**
   - Rapprochement complet : X %
   - Dans la tolérance : Y %
   - Hors tolérance : Z %

2. **Analyse des écarts :**
   - Écart de prix moyen
   - Écart de quantité moyen
   - Motifs d'écart fréquents

3. **Efficacité de traitement :**
   - Taux d'approbation automatique
   - Taux de révision manuelle
   - Temps de révision moyen

4. **Performance des fournisseurs :**
   - Écarts par fournisseur
   - Taux de rapprochement par fournisseur
   - Fournisseurs problématiques

---

## Liste de vérification de test

- [ ] Scénario de correspondance parfaite (rapprochement complet)
- [ ] Scénario dans la tolérance (écart faible)
- [ ] Scénario hors tolérance (écart important)
- [ ] Scénario de commande manquante
- [ ] Scénario de numéro de commande erroné
- [ ] Scénario de livraison partielle
- [ ] Scénario de surlivraison
- [ ] Scénario d'écart de devise
- [ ] Scénario de plusieurs commandes
- [ ] Scénario de commande clôturée
- [ ] Scénario d'écart de taxe
- [ ] Workflow d'escalade
- [ ] Création de tâche
- [ ] Notifications par e-mail
- [ ] Mises à jour de champs
- [ ] Export après approbation

---

## Modèles connexes

### Modèles qui fonctionnent bien ensemble :

- **[Modèle de gestion des tâches](task-management-pattern.md)** – Créer des tâches de révision pour les écarts
- **[Modèle de logique de décision](decision-logic-pattern.md)** – Routage complexe selon le niveau d'écart
- **[Modèle d'intégration d'API](api-integration-pattern.md)** – Récupérer les tarifs actuels pour comparaison
- **[Modèle de transformation des données](data-transformation-pattern.md)** – Conversion de devises et d'unités

---

## Guides connexes

### Prérequis
- [Guide complet du PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md) – Toutes les cartes de rapprochement de commandes
- [Guide des cartes de condition](../and/condition-cards-complete-guide.md) – Logique de condition
- [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md) – Opérations sur les champs

### Cartes connexes
- **PURCHASE_ORDER_FULL_MATCH** – [Guide du PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** – [Guide du PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** – [Guide du PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** – [Guide du PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** – [Guide d'affectation des tâches](../then/task/task-assignment-guide.md)

### Prochaines étapes
- Créer des tâches de révision : [Modèle de gestion des tâches](task-management-pattern.md)
- Ajouter des notifications par e-mail : [Guide e-mail](../then/action/send-email-groups-guide.md)
- Mettre en place un routage complexe : [Modèle de logique de décision](decision-logic-pattern.md)

---

**Version du modèle :** 1.0
**Dernière mise à jour :** 23 octobre 2025
**Difficulté :** Moyenne-Élevée
**Temps estimé :** 60-90 minutes
**Taux de réussite :** Élevé (lorsqu'il est correctement configuré)
