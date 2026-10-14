# Modèle de logique de décision

**Type de modèle :** Routage & logique conditionnels
**Complexité :** Moyenne
**Mise en place estimée :** 30-45 minutes
**Cas d'usage courants :** Routage multi-chemins, traitement conditionnel, arbres de décision, mise en œuvre de règles métier

---

Vous construisez ce modèle dans le **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Cliquez sur **Add Card** et ouvrez la catégorie **Logic** — elle contient les cartes de condition et de branchement qui pilotent l'arbre de décision, et que vous combinez avec le groupe **And** pour évaluer plusieurs conditions :

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Bibliothèque Add Card dans le Workflow Builder, regroupée par catégorie"><figcaption><p>La bibliothèque <strong>Add Card</strong> — les cartes de condition et de branchement se trouvent sous la catégorie <strong>Logic</strong>.</p></figcaption></figure>

---

## Vue d'ensemble du modèle

Ce modèle montre comment mettre en place une logique de décision complexe dans les workflows DocBits à l'aide de cartes de condition pour acheminer les documents par différents chemins de traitement en fonction des attributs des documents, des valeurs de champs et des règles métier.

**Ce que fait ce modèle :**
1. Évalue plusieurs conditions de façon séquentielle ou parallèle
2. Route les documents vers différents chemins en fonction des conditions
3. Met en œuvre des règles et des politiques métier
4. Traite des arbres de décision complexes
5. Combine plusieurs critères pour les décisions de routage

---

## Quand utiliser ce modèle

Utilisez ce modèle lorsque vous devez :
- ✅ Router les documents par seuils de montant
- ✅ Appliquer des règles différentes selon les types de documents
- ✅ Mettre en œuvre une logique d'approbation à plusieurs niveaux
- ✅ Gérer des politiques métier complexes
- ✅ Créer un routage dynamique basé sur plusieurs critères
- ✅ Mettre en œuvre une logique de gestion des exceptions
- ✅ Créer des matrices d'approbation

**N'utilisez pas ce modèle lorsque :**
- ❌ un workflow linéaire simple suffit
- ❌ tous les documents suivent le même chemin
- ❌ aucun traitement conditionnel n'est nécessaire

---

## Types de logique de décision

### 1. Logique IF-THEN simple

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Exemple :**
```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Plusieurs critères (logique ET)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Exemple :**
```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Critères alternatifs (logique OU)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Exemple :**
```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. Arbre de décision imbriqué

```
IF condition1:
  IF condition2:
    → Action A
  ELSE:
    → Action B
ELSE:
  IF condition3:
    → Action C
  ELSE:
    → Action D
```

**Exemple :**
```
IF Document_Type = "Invoice":
  IF Amount > €10,000:
    → High-value invoice workflow
  ELSE:
    → Standard invoice workflow
ELSE IF Document_Type = "Credit Note":
  IF Amount > €5,000:
    → High-value credit workflow
  ELSE:
    → Standard credit workflow
```

---

## Exemple complet de workflow

### Scénario : Matrice d'approbation des factures

**Règles métier :**
1. Montant < 1 000 € : Approbation automatique
2. Montant 1 000-10 000 € : Approbation par la responsable
3. Montant > 10 000 € ET nouveau fournisseur : Approbation par le directeur + CFO
4. Montant > 10 000 € ET fournisseur existant : Approbation par le directeur uniquement
5. Tout montant avec écart de commande : Approbation par les achats d'abord
6. Factures urgentes (marquées) : Workflow accéléré

**Mise en œuvre :**

```
STEP 1: Check for PO Mismatch
  IF PO_Match_Status = "FAIL":
    → Route to Procurement for PO resolution
    → After resolution, continue below

STEP 2: Check Urgent Flag
  IF Urgent_Flag = TRUE:
    → Skip amount checks
    → Direct to highest approver
    → Set priority = HIGH
    → 1-day deadline

STEP 3: Amount-Based Routing (if not urgent)
  IF Amount < €1,000:
    → Auto-approve
    → Export immediately

  ELSE IF Amount < €10,000:
    → Create task for Manager
    → Priority: Medium
    → Deadline: 3 days

  ELSE IF Amount ≥ €10,000:
    CHECK Supplier Status:
      IF Supplier_Age < 180 days (New):
        → Create task for Director (Task 1)
        → After approval, create task for CFO (Task 2)
        → Priority: High
        → Deadline: 2 days each

      ELSE (Existing Supplier):
        → Create task for Director only
        → Priority: High
        → Deadline: 2 days
```

---

## Mise en œuvre étape par étape

### Étape 1 : Définir les cartes de condition

**Condition 1 : Seuil de montant**
```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Condition 2 : Vérification du type de document**
```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Condition 3 : Statut du fournisseur**
```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Condition 4 : Vérification d'un nouveau fournisseur**
```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Référence du guide :** [Guide complet des cartes de condition](../and/condition-cards-complete-guide.md)

---

### Étape 2 : Construire l'arbre de décision

**Niveau 1 : Type de document**
```
Workflow: "Invoice Processing"

IF Document_Type = "Invoice":
  → Continue to Level 2

ELSE IF Document_Type = "Credit Note":
  → Branch to "Credit Note Processing"

ELSE IF Document_Type = "Receipt":
  → Branch to "Receipt Processing"

ELSE:
  → Route to "Unknown Document Type" handling
```

**Niveau 2 : Seuils de montant (pour les factures)**
```
IF Amount < €1,000:
  → Branch to "Auto-Approve Path"

ELSE IF Amount < €10,000:
  → Branch to "Manager Approval Path"

ELSE IF Amount < €50,000:
  → Branch to "Director Approval Path"
  → Check Level 3 conditions

ELSE (Amount ≥ €50,000):
  → Branch to "Executive Approval Path"
  → Dual or triple approval required
```

**Niveau 3 : Analyse du fournisseur (pour les factures de montant élevé)**
```
IF Supplier_Status = "BLOCKED":
  → STOP processing
  → Create urgent escalation task
  → Notify procurement and finance

ELSE IF Supplier_Age < 180 days (New):
  → Additional approval required
  → Add CFO to approval chain
  → Enhanced verification

ELSE IF Supplier_Risk_Rating = "HIGH":
  → Additional checks required
  → Fraud detection review
  → Manager pre-approval

ELSE:
  → Standard high-value workflow
```

---

### Étape 3 : Créer les actions de routage

**Chemin A : Approbation automatique (montant < 1 000 €)**
```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Chemin B : Approbation par la responsable (1 000-10 000 €)**
```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "1"
3. tasks_create:
   - Title: "Approve Invoice {{DOCUMENT_NUMBER}}"
   - Assign to: Department_Manager
   - Priority: Medium
   - Deadline: 3 days
4. Send email notification to manager
5. Wait for task completion
6. If approved: Export to ERP
7. If rejected: Return to supplier
```

**Chemin C : Approbation par le directeur (10 000-50 000 €)**
```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "2"
3. Check Supplier_Age:
   IF New (< 180 days):
     - Create Task 1: Director approval
     - After Task 1: Create Task 2: CFO approval
     - Dual approval required
   ELSE:
     - Create Task: Director approval only
4. Priority: High
5. Deadline: 2 days
6. Send email notifications
7. Wait for completion
8. If all approved: Export
9. If any rejected: Return to supplier
```

**Chemin D : Approbation par la direction générale (≥ 50 000 €)**
```
Actions:
1. Set field "Approval_Type" = "EXECUTIVE"
2. Set field "Approval_Level" = "3"
3. Sequential approvals:
   - Task 1: Finance Director
   - Task 2: CFO
   - Task 3: CEO (if > €100,000)
4. Priority: Urgent
5. Deadline: 1 day each
6. Send urgent notifications
7. Executive dashboard update
8. Wait for all approvals
9. If all approved: Export
10. If any rejected: Executive review meeting
```

---

## Modèles avancés de logique de décision

### Modèle 1 : Routage basé sur un score

**Calculer un score de risque et router en conséquence :**

```
Risk Score Calculation:
  Score = 0

  IF Amount > €50,000: Score += 30
  IF Supplier_Age < 180 days: Score += 25
  IF PO_Variance > 10%: Score += 20
  IF Supplier_Country = "High Risk Country": Score += 15
  IF Payment_Terms < 30 days: Score += 10

  Total Score Range: 0-100

Routing:
  IF Score < 20: Auto-approve
  IF Score 20-50: Manager approval
  IF Score 51-75: Director approval
  IF Score > 75: Executive approval + fraud check
```

**Mise en œuvre :**
```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

---

### Modèle 2 : Matrice basée sur le service

**Règles d'approbation différentes par service :**

```
Department Matrix:

  IT Department:
    Amount < €5,000: IT Manager
    Amount ≥ €5,000: IT Director + CIO

  Finance Department:
    Amount < €10,000: Finance Manager
    Amount ≥ €10,000: CFO

  Operations Department:
    Amount < €3,000: Operations Manager
    Amount ≥ €3,000: COO

  General:
    Amount < €2,000: Department Manager
    Amount ≥ €2,000: Department Director
```

**Mise en œuvre :**
```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

---

### Modèle 3 : Logique basée sur le temps

**Règles différentes selon le moment :**

```
Month-End Processing (Last 3 days of month):
  IF Today in last 3 days of month:
    - Priority: URGENT
    - Deadline: 1 day
    - Approver: On-duty finance manager
    - Expedited workflow
  ELSE:
    - Standard priority
    - Standard deadline
    - Standard workflow

Business Hours vs After Hours:
  IF Time between 9 AM - 5 PM:
    - Assign to current shift
  ELSE:
    - Queue for next business day
    - OR route to on-call approver

Fiscal Period:
  IF Document_Date in Current_Fiscal_Period:
    - Standard processing
  ELSE:
    - Flag as "Prior Period"
    - Require accounting approval
    - Additional checks
```

---

### Modèle 4 : Routage basé sur les exceptions

**Acheminer les exceptions séparément :**

```
Exception Detection:

  No Exception:
    → Standard workflow

  Minor Exception (Auto-fixable):
    → Auto-correct
    → Log correction
    → Continue standard workflow

  Medium Exception (Needs review):
    → Create review task
    → Flag document
    → After fix: Continue workflow

  Major Exception (Requires escalation):
    → Stop processing
    → Create urgent task
    → Notify multiple levels
    → Manual intervention required

Exception Types:
  - Missing required field
  - Invalid field value
  - PO mismatch
  - Duplicate invoice
  - Supplier mismatch
  - Amount discrepancy
```

---

## Diagramme complet de logique de décision

```
INVOICE ARRIVES
│
├─ LEVEL 1: EXCEPTION CHECK
│  │
│  ├─ Has Critical Exception? (Missing PO, Duplicate, etc.)
│  │  │
│  │  ├─ YES → Stop & Escalate
│  │  │        Create urgent task
│  │  │        Notify admin
│  │  │        → END (Exception Handling)
│  │  │
│  │  └─ NO → Continue to Level 2
│
├─ LEVEL 2: DOCUMENT TYPE
│  │
│  ├─ Type = Invoice?
│  │  └─ YES → Continue to Level 3
│  │
│  ├─ Type = Credit Note?
│  │  └─ YES → Branch to Credit Note workflow
│  │           → END (Credit Note Path)
│  │
│  └─ Other Type?
│     └─ YES → Branch to appropriate workflow
│              → END (Other Type Path)
│
├─ LEVEL 3: URGENCY CHECK (for Invoices)
│  │
│  ├─ Urgent Flag = TRUE?
│  │  │
│  │  ├─ YES → Expedited Workflow
│  │  │        Priority: URGENT
│  │  │        Deadline: 1 day
│  │  │        Assign to: Senior Approver
│  │  │        → END (Expedited Path)
│  │  │
│  │  └─ NO → Continue to Level 4
│
├─ LEVEL 4: AMOUNT THRESHOLDS
│  │
│  ├─ Amount < €1,000?
│  │  │
│  │  ├─ YES → AUTO-APPROVE PATH
│  │  │        Set Approval_Type = "AUTO"
│  │  │        Approve immediately
│  │  │        Export to ERP
│  │  │        → END (Auto-Approved)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €10,000?
│  │  │
│  │  ├─ YES → MANAGER APPROVAL PATH
│  │  │        Create task for Manager
│  │  │        Priority: Medium
│  │  │        Deadline: 3 days
│  │  │        → WAIT for approval
│  │  │           → END (Manager Path)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €50,000?
│  │  │
│  │  ├─ YES → DIRECTOR APPROVAL PATH
│  │  │        Continue to Level 5 (Supplier Check)
│  │  │
│  │  └─ NO → Continue
│  │
│  └─ Amount ≥ €50,000?
│     │
│     └─ YES → EXECUTIVE APPROVAL PATH
│              Create sequential tasks:
│              - Finance Director
│              - CFO
│              - CEO (if > €100,000)
│              Priority: URGENT
│              Deadline: 1 day each
│              → WAIT for all approvals
│                 → END (Executive Path)
│
├─ LEVEL 5: SUPPLIER ANALYSIS (for €10k-€50k range)
│  │
│  ├─ Supplier Status = "BLOCKED"?
│  │  │
│  │  ├─ YES → BLOCK & ESCALATE
│  │  │        Stop processing
│  │  │        Create urgent task
│  │  │        Notify procurement & finance
│  │  │        → END (Blocked Supplier)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Age < 180 days (New)?
│  │  │
│  │  ├─ YES → DUAL APPROVAL REQUIRED
│  │  │        Task 1: Director (2 days)
│  │  │        → WAIT for Task 1
│  │  │           IF Task 1 Approved:
│  │  │             Task 2: CFO (2 days)
│  │  │             → WAIT for Task 2
│  │  │                → END (Dual Approved)
│  │  │           IF Task 1 Rejected:
│  │  │             → END (Rejected at Level 1)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Risk Rating = "HIGH"?
│  │  │
│  │  ├─ YES → ENHANCED APPROVAL
│  │  │        Additional fraud checks
│  │  │        Director approval required
│  │  │        Extended deadline
│  │  │        → END (Enhanced Path)
│  │  │
│  │  └─ NO → STANDARD DIRECTOR APPROVAL
│  │           Create task for Director
│  │           Priority: High
│  │           Deadline: 2 days
│  │           → WAIT for approval
│  │              → END (Standard High-Value)
│  │
│  └─ [Supplier analysis complete]
│
└─ [All decision levels processed]
```

---

## Bonnes pratiques de configuration

### 1. Garder la logique claire et maintenable

✅ **Bon :**
```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Mauvais (trop complexe) :**
```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Mieux : Décomposer en étapes :**
```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

---

### 2. Documenter la logique de décision

**Toujours inclure :**
- L'objectif de chaque point de décision
- La règle métier mise en œuvre
- Les résultats attendus
- La gestion des exceptions

**Exemple de documentation :**
```
Decision Point: Amount Threshold Check
Business Rule: BR-INV-001 (Invoice Approval Matrix)
Purpose: Route invoices based on amount thresholds per company policy
Thresholds:
  < €1,000: Auto-approve (CFO approved threshold)
  €1,000-€10,000: Manager approval (Delegation matrix)
  > €10,000: Director approval (Signature authority)
Exceptions: Urgent invoices skip to highest level
Updated: 2025-10-23
Owner: Finance Department
```

---

### 3. Tester tous les chemins

**Matrice de test :**

| Cas de test | Montant | Type | Fournisseur | Chemin attendu | Statut |
|-----------|--------|------|----------|---------------|--------|
| TC1 | €500 | Invoice | Existing | Auto-approve | ✅ |
| TC2 | €5,000 | Invoice | Existing | Manager | ✅ |
| TC3 | €15,000 | Invoice | New | Director+CFO | ✅ |
| TC4 | €60,000 | Invoice | Existing | Executive | ✅ |
| TC5 | €2,000 | Credit Note | Existing | Credit workflow | ✅ |
| TC6 | €100,000 | Invoice | Blocked | Stop & Escalate | ✅ |

---

### 4. Surveiller les indicateurs de décision

**Suivre :**
- La répartition sur les chemins de décision
- Le taux d'approbation automatique
- Le taux de révision manuelle
- Le temps de traitement moyen par chemin
- Les taux d'exception
- L'utilisation des chemins

**Exemple d'indicateurs :**
```
Month: October 2025
Total Invoices: 1,250

Decision Path Distribution:
- Auto-approved (< €1k): 680 (54%)
- Manager path (€1k-€10k): 420 (34%)
- Director path (€10k-€50k): 120 (10%)
- Executive path (> €50k): 30 (2%)

Processing Time:
- Auto-approve: < 1 minute
- Manager path: 2.5 days average
- Director path: 1.8 days average
- Executive path: 3.2 days average

Exceptions: 15 (1.2%)
```

---

## Modèles connexes

### Modèles qui fonctionnent bien ensemble :

- **[Modèle de gestion des tâches](task-management-pattern.md)** – Créer des tâches en fonction des décisions
- **[Modèle d'intégration d'API](api-integration-pattern.md)** – Récupérer des données pour la prise de décision
- **[Modèle de rapprochement de commandes (PO Matching)](po-matching-pattern.md)** – Utiliser les résultats de commande dans les décisions
- **[Modèle de transformation des données](data-transformation-pattern.md)** – Transformer les données avant les décisions

---

## Guides connexes

### Prérequis
- [Guide complet des cartes de condition](../and/condition-cards-complete-guide.md) – Toutes les cartes de condition
- [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md) – Opérations sur les champs
- [Guide d'affectation](../then/assignee/assignment-user-guide.md) – Logique de routage

### Cartes connexes
- **CONDITION_DOC_FIELD_AMOUNT** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** – [Guide d'affectation](../then/assignee/assignment-user-guide.md)
- **tasks_create** – [Guide d'affectation des tâches](../then/task/task-assignment-guide.md)

### Prochaines étapes
- Créer des tâches : [Modèle de gestion des tâches](task-management-pattern.md)
- Ajouter un rapprochement complexe : [Modèle de rapprochement de commandes (PO Matching)](po-matching-pattern.md)
- Intégrer des API : [Modèle d'intégration d'API](api-integration-pattern.md)

---

**Version du modèle :** 1.0
**Dernière mise à jour :** 23 octobre 2025
**Difficulté :** Moyenne
**Temps estimé :** 30-45 minutes
**Taux de réussite :** Élevé
