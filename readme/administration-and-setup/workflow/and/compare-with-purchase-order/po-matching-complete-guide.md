# Cartes de rapprochement de commande d'achat (PO) - Guide complet

Les cartes de rapprochement de commande de cette page se placent dans le groupe **And** du Concepteur de workflow — elles comparent les données de la facture à la commande associée avant l'exécution des actions Then :

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Les cartes de rapprochement de commande sont ajoutées au groupe <strong>And</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

{% embed url="https://youtu.be/qR-lrSaj4Ug" %}
DocBits PO Matching Tutorial: Auto/Manual Line Matching, Tolerances & Mismatch Indicators
{% endembed %}

**Statut :** Couvre 15 cartes de comparaison de PO avec des calculs détaillés

---

## 📌 Informations sur les versions

**Carte la plus évoluée :** CONDITION_DOC_TO_PO_UNIT_PRICE (5 versions, v5 la plus récente)
**Autres cartes complexes :** CONDITION_OC_TO_PO_ITEMS (v4), CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v4)

**Modèles clés :**
- **v2 → v3+ :** Ajout de paramètres de tolérance pour un rapprochement flexible
- **v3 → v4 :** Ajout de paramètres de mode de comparaison
- **v4 → v5 :** Tolérance améliorée avec plusieurs unités (%, EUR, $, etc.)

📖 [Historique complet des versions](../../../changelog/release.md#-po-comparison--validation-cards) | [Base de données des versions de cartes](../../../../DocFlow/docs/card_version.md)

---

## Comprendre le rapprochement de PO

Lorsque vous recevez une facture, elle doit correspondre à la commande d'achat (PO) passée précédemment. Les cartes de rapprochement de PO vérifient automatiquement si les données de la facture correspondent aux données du PO.

**Vue d'ensemble :**
```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

---

# 1. Correspondance complète de la commande d'achat

## Objectif
Vérifie si l'ensemble de la facture correspond parfaitement au PO ou dans la tolérance

## Quand l'utiliser
- Avant d'approuver une facture
- Comme contrôle qualité préliminaire
- Pour identifier les problèmes tôt

## Comment ça fonctionne
Le système compare :
- Les quantités de la facture vs les quantités du PO
- Les prix de la facture vs les prix du PO
- Les articles de la facture vs les articles du PO
- Le total de la facture vs le total du PO

## Résultat
- **TRUE** (correspondance complète) : Tout correspond, continuer
- **FALSE** (non-correspondance) : Quelque chose ne correspond pas, nécessite un examen

## Exemple
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

# 2. Comparaison du prix unitaire (Document vs PO)

## Objectif
Compare le prix unitaire de la facture avec le prix unitaire du PO

## Paramètres
- **Unit Price Tolerance** : Autorise un écart jusqu'à ce montant
- **Tolerance Type** : Pourcentage (%) ou Absolu (€/$)
- **Operator** : Is Equal to, Is Greater than, Is Less than, etc.

## Comment ça fonctionne (tolérance en pourcentage)

**Formule :**
```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Exemple étape par étape :**
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

## Exemples concrets

### Exemple 1 : Petite augmentation (acceptée)
```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

### Exemple 2 : Grande augmentation (rejetée)
```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

### Exemple 3 : Remise (également vérifiée)
```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

### Exemple 4 : Tolérance en valeur absolue
```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

## Que faire avec les résultats

**Si PASS ✅ :**
- Passer à la vérification suivante
- Ou approuver la facture
- Ou procéder à l'exportation

**Si FAIL ❌ :**
- Signaler pour révision manuelle
- Demander une explication au fournisseur
- Contacter l'équipe des achats
- Approuver avec une note si acceptable

---

# 3. Comparaison de la quantité

## Objectif
Vérifie si la quantité commandée correspond à la quantité facturée

## Paramètres
- **Tolerance** : Montant ou % d'écart autorisé
- **Operator** : Equals, Greater than, Less than
- **Quantity Type** : Ordered, Received, Open

## Exemple de calcul

**Tolérance en pourcentage :**
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

**Tolérance absolue :**
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

## Scénarios concrets

### Sur-livraison (plus que commandé)
```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

### Sous-livraison (moins que commandé)
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

# 4. Prix combiné de la différence de quantité

## Objectif
Lorsque la quantité diffère, calcule si la différence de prix totale est acceptable

## Pourquoi c'est important
```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

## Calcul

**Formule :**
```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Exemple :**
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

# 5. Comparaison de l'ID d'article / numéro d'article fournisseur

## Objectif
Vérifie si les articles de la facture correspondent aux articles du PO

## Comment ça fonctionne

**Correspondance exacte (la plus simple) :**
```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Numéro d'article fournisseur (plus courant) :**
```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

## Scénario : Que se passe-t-il s'il n'y a pas de correspondance ?

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

# 6. Vérification du type de commande

## Objectif
Vérifie que le type de commande d'achat est correct

## Types de commande
- **Standard Order** : Achat régulier
- **Rush Order** : Urgent, peut avoir une majoration
- **Frame Agreement** : Contrat à long terme
- **Blanket Order** : Contrat ouvert
- **Consignment** : Vous ne payez qu'à l'utilisation

## Exemple de vérification
```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

---

# 7. Vérification de la date de livraison

## Objectif
Vérifie si la date de livraison correspond à la date promise sur le PO

## Calcul

**Livraison tardive :**
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

**Livraison anticipée :**
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

## Paramètres de tolérance
```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

---

# 8. Vérification des frais (taxes, expédition, etc.)

## Objectif
Vérifie si les frais supplémentaires (taxes, expédition, manutention) correspondent au PO

## Frais courants
```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

## Calcul

**Exemple : Vérification des frais d'expédition**
```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Exemple : Frais multiples**
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

# 9. Vérification de la taxe

## Objectif
Vérifie que les montants de taxe sont calculés correctement

## Calcul

**Formule :**
```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Problèmes courants :**
```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Exemple : Taxation à plusieurs taux**
```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

---

# 10. Rapprochement de l'établissement/centre de coûts

## Objectif
Garantit que la facture concerne le bon établissement/centre de coûts

## Exemple
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

# 11. Validation du statut du fournisseur

## Objectif
Vérifie si le fournisseur est toujours approuvé/actif

## Types de statut
```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

## Exemple de vérification
```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

---

# Quelle tolérance dois-je utiliser ?

## Tolérances strictes (risque plus faible, plus de travail manuel)
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

## Tolérances modérées (équilibrées)
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

## Tolérances larges (risque plus élevé, moins de travail manuel)
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

# Exemple de flux de travail de rapprochement de PO

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

# Dépannage du rapprochement de PO

## « PO Not Found »
```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

## « Items Don't Match »
```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

## « Price Higher Than PO »
```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

## « Delivery Date Wrong »
```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

---

# Tableau récapitulatif

| Carte | Ce qu'elle vérifie | Calcul principal | Tolérance courante |
|------|----------------|------------------|-----------------|
| Full Match | Tout | Toutes les vérifications | Variable |
| Unit Price | Prix par unité | Différence en % ou € | ±3-5% |
| Quantity | Quantité commandée | Différence en % ou unité | ±3-5% |
| Combined Price | Total avec variation de qté | Qté × Prix | ±5-10% |
| Item ID | Bons articles | Correspondance de chaîne | Exacte |
| Order Type | Type d'achat | Correspondance de chaîne | Exacte |
| Delivery Date | Date d'arrivée | Différence en jours | ±3 jours |
| Charges | Frais supplémentaires | Différence en % ou € | ±5% |
| Tax | Montant de la taxe | Calcul du % de taxe | ±1% |
| Facility | Centre de coûts | Correspondance de chaîne | Exacte |
| Supplier | Approuvé ? | Vérification du statut | Actif uniquement |

---

# Documentation associée

- Voir le guide « Invoice Validation » pour le flux de travail complet
- Voir « Tolerance Settings » pour les valeurs recommandées par secteur
- Voir « Exception Handling » pour savoir quoi faire en cas d'échec
- Contactez votre équipe des achats pour les politiques de tolérance spécifiques
