# Modèle logique de décision

**Type de modèle :** Routage & logique conditionnels **Complexité :** Moyenne **Mise en place estimée :** 30-45 minutes **Cas d'usage courants :** Routage multi-chemins, traitement conditionnel, arbres de décision, mise en œuvre de règles métier

***

Dans le concepteur Standard, ouvrez **Ajouter une carte** dans le groupe **Et....**, puis la catégorie **Logique**. La vue partielle ci-dessous présente une carte de condition fondée sur une table de décision, affichée dans la bibliothèque avant sa sélection et sa configuration. La table à utiliser et le stockage des résultats pour les cartes suivantes restent à configurer. Les autres conditions, actions et connexions du modèle restent à définir et à vérifier. La condition porte sur les résultats renvoyés par la table pour le document ou l’organisation du fournisseur.

<figure><img src="../../../.gitbook/assets/workflow-decision-condition-library-current-fr.png" alt="Carte de condition de la catégorie « Logique » dans la bibliothèque, avant sa sélection et sa configuration. La table de décision et le stockage des résultats restent à configurer."><figcaption><p>Carte de condition de la catégorie « Logique » dans la bibliothèque, avant sa sélection et sa configuration. La table de décision et le stockage des résultats restent à configurer.</p></figcaption></figure>

***

## Vue d'ensemble du modèle

Ces quatre schémas présentent les règles métier à configurer. Ils complètent la carte de bibliothèque ci-dessus, affichée avant sélection et configuration. Dans Advanced, reliez explicitement chaque chemin. Dans une séquence Standard linéaire, définissez les conditions qui autorisent ses actions.

<figure><img src="../../../.gitbook/assets/decision-flow-overview-fr.png" alt="Vue d’ensemble de l’exemple complet : contrôler les exceptions critiques, le type de document et l’urgence avant de choisir le circuit d’approbation. Chaque traitement et chaque connexion doivent être configurés ; le schéma ne représente pas un comportement automatique du produit."><figcaption><p>Vue d’ensemble de l’exemple complet : contrôler les exceptions critiques, le type de document et l’urgence avant de choisir le circuit d’approbation. Chaque traitement et chaque connexion doivent être configurés ; le schéma ne représente pas un comportement automatique du produit.</p></figcaption></figure>

Ce modèle montre comment mettre en place une logique de décision complexe dans les workflows DocBits à l'aide de cartes de condition pour acheminer les documents par différents chemins de traitement en fonction des attributs des documents, des valeurs de champs et des règles métier.

**Ce que fait ce modèle :**

1. Évalue plusieurs conditions de façon séquentielle ou parallèle
2. Route les documents vers différents chemins en fonction des conditions
3. Met en œuvre des règles et des politiques métier
4. Traite des arbres de décision complexes
5. Combine plusieurs critères pour les décisions de routage

***

## Quand utiliser ce modèle

Utilisez ce modèle lorsque vous devez :

* ✅ Router les documents par seuils de montant
* ✅ Appliquer des règles différentes selon les types de documents
* ✅ Mettre en œuvre une logique d'approbation à plusieurs niveaux
* ✅ Gérer des politiques métier complexes
* ✅ Créer un routage dynamique basé sur plusieurs critères
* ✅ Mettre en œuvre une logique de gestion des exceptions
* ✅ Créer des matrices d'approbation

**N'utilisez pas ce modèle lorsque :**

* ❌ un workflow linéaire simple suffit
* ❌ tous les documents suivent le même chemin
* ❌ aucun traitement conditionnel n'est nécessaire

***

## Types de logique de décision

Les exemples IF-THEN, ET, OU et imbriqués ci-dessous sont indépendants. Leurs seuils illustrent chaque principe ; ils ne constituent pas une seule matrice d’approbation. La matrice complète plus loin utilise quatre tranches sans chevauchement. Une donnée inconnue ou une erreur d’évaluation n’est pas automatiquement Faux : définissez et testez son traitement séparément.

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

<figure><img src="../../../.gitbook/assets/decision-conditions-and-or-fr.png" alt="Deux exemples indépendants : ET exige les trois critères ; OU en exige au moins un. Leurs seuils illustratifs ne remplacent pas les tranches de la matrice complète. Les sorties et le traitement des données inconnues ou des erreurs doivent être configurés."><figcaption><p>Deux exemples indépendants : ET exige les trois critères ; OU en exige au moins un. Leurs seuils illustratifs ne remplacent pas les tranches de la matrice complète. Les sorties et le traitement des données inconnues ou des erreurs doivent être configurés.</p></figcaption></figure>

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

***

## Exemple complet de workflow

### Scénario : Matrice d'approbation des factures

**Règles métier :**

1. Avant tout routage par montant, arrêter et traiter les exceptions critiques, notamment un fournisseur bloqué. Un écart de commande n’est pas toujours critique : après sa résolution par les achats, le circuit peut continuer selon la configuration. Vérifier ensuite le type de document.
2. Pour une facture urgente, suivre le circuit accéléré décrit dans cet exemple plutôt que les tranches ordinaires.
3. Pour une facture non urgente avec un montant valide :
   * montant < 1 000 € : approbation automatique ;
   * 1 000 € ≤ montant < 10 000 € : approbation par la responsable ;
   * 10 000 € ≤ montant < 50 000 € : contrôle du fournisseur puis circuit du directeur ; un fournisseur non bloqué de moins de 180 jours nécessite l’accord du directeur, puis celui de la direction financière ; les autres fournisseurs passent aussi au contrôle du risque ;
   * montant ≥ 50 000 € : circuit de direction générale détaillé au chemin D.
4. Un montant absent ou invalide mène ici à un contrôle manuel explicitement configuré. C’est une politique de cet exemple, pas un comportement de repli automatique du produit.
5. Après création d’une tâche, attendre son résultat. Un refus arrête la chaîne et suit le traitement configuré ; un résultat en attente ne permet pas de poursuivre. La tâche de la direction financière n’est créée qu’après l’accord du directeur.

<figure><img src="../../../.gitbook/assets/decision-amount-routing-fr.png" alt="Seuils du niveau 2 : moins de 1 000 € ; de 1 000 € inclus à 10 000 € exclu ; de 10 000 € inclus à 50 000 € exclu ; 50 000 € ou plus. Chaque test suit le résultat négatif du précédent. Le contrôle manuel pour un montant absent ou invalide doit être configuré explicitement."><figcaption><p>Seuils du niveau 2 : moins de 1 000 € ; de 1 000 € inclus à 10 000 € exclu ; de 10 000 € inclus à 50 000 € exclu ; 50 000 € ou plus. Chaque test suit le résultat négatif du précédent. Le contrôle manuel pour un montant absent ou invalide doit être configuré explicitement.</p></figcaption></figure>

Les valeurs de 1 000 €, 10 000 € et 50 000 € appartiennent à la tranche supérieure. Les contrôles précédents, l’attente d’un résultat et les connexions entre chemins doivent être configurés et testés. Une tâche créée ne prouve ni son approbation ni l’export du document.

**Mise en œuvre illustrative :** adaptez les noms techniques et le pseudocode aux cartes réellement disponibles dans votre version. Ces blocs décrivent un exemple à configurer, plutôt qu’un fichier prêt à importer. Vérifiez les résultats d’exécution et les effets de votre configuration.

```
PRECHECK: Critical Exceptions
  IF Critical_Exception = TRUE OR Supplier_Status = "BLOCKED":
    → Stop & handle exception before routing

STEP 1: Check for PO Mismatch
  IF PO_Match_Status = "FAIL":
    → Route to Procurement for PO resolution
    → After resolution, continue below as configured

STEP 1b: Check Document Type
  IF Document_Type = "Credit Note":
    → Configured Credit Note workflow
  ELSE IF Document_Type is not "Invoice":
    → Configured workflow for this document type
  ELSE:
    → Continue below

STEP 2: Check Urgent Flag
  IF Urgent_Flag = TRUE:
    → Skip amount checks
    → Direct to highest approver
    → Set priority = URGENT
    → 1-day deadline

STEP 3: Amount-Based Routing (Invoice, if not urgent)
  IF Amount is missing or invalid:
    → Manual review (explicit example policy)
    → Do not enter amount bands

  ELSE IF Amount < €1,000:
    → Auto-approve
    → Export immediately

  ELSE IF Amount < €10,000:
    → Create task for Manager
    → Priority: Medium
    → Deadline: 3 days

  ELSE IF Amount < €50,000:
    CHECK Supplier Status and Risk:
      IF Supplier_Status = "BLOCKED":
        → Stop & handle exception
      ELSE IF Supplier_Age < 180 days (New):
        → Create task for Director (Task 1)
        → Wait for positive Director approval before creating CFO task (Task 2)
        → Wait for positive CFO approval before continuing
        → Any rejection: Stop chain & handle rejection as configured
        → Pending: Do not continue
        → Priority: High
        → Deadline: 2 days each
      ELSE IF Supplier_Risk_Rating = "HIGH":
        → Additional checks and Director approval
      ELSE (Existing Supplier):
        → Create task for Director only
        → Priority: High
        → Deadline: 2 days

  ELSE (Amount ≥ €50,000):
    → Executive approval path (see Path D)
```

***

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

***

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

**Niveau 2 : Seuils de montant (factures non urgentes, montant valide)**

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

***

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

**Chemin B : Approbation par la responsable (1 000 € ≤ montant < 10 000 €)**

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

**Chemin C : Approbation par le directeur (10 000 € ≤ montant < 50 000 €)**

```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "2"
3. Check Supplier_Age and Supplier_Risk_Rating:
   IF New (< 180 days):
     - Create Task 1: Director approval
     - Wait for positive Task 1 approval before creating Task 2: CFO approval
     - Wait for positive Task 2 approval before continuing
     - Pending: Do not continue
     - Any rejection: Stop chain & handle rejection as configured
     - Both positive approvals required
   ELSE IF Supplier_Risk_Rating = "HIGH":
     - Additional risk checks and Director approval
   ELSE:
     - Create Task: Director approval only
4. Priority: High
5. Deadline: 2 days
6. Send email notifications
7. Wait for completion
8. If all approved: Export
9. If any rejected: Return to supplier
```

<figure><img src="../../../.gitbook/assets/decision-approvals-sequence-fr.png" alt="Exemple d’approbations successives : créer la tâche de la direction financière seulement après l’accord du directeur, puis attendre son résultat. Poursuivre uniquement après les deux accords. Un refus arrête la chaîne et suit le traitement configuré ; un résultat en attente ne permet pas de continuer."><figcaption><p>Exemple d’approbations successives : créer la tâche de la direction financière seulement après l’accord du directeur, puis attendre son résultat. Poursuivre uniquement après les deux accords. Un refus arrête la chaîne et suit le traitement configuré ; un résultat en attente ne permet pas de continuer.</p></figcaption></figure>

Le traitement d’un refus peut, selon votre configuration, renvoyer le document au fournisseur ou suivre un autre circuit. Ce schéma impose seulement l’arrêt de la chaîne d’approbation concernée ; il ne prescrit pas un contrôle manuel dans tous les cas.

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

***

## Modèles avancés de logique de décision

Les modèles suivants sont des variantes indépendantes. Le score, les seuils par service et les règles temporelles ne s’ajoutent pas automatiquement à la matrice complète précédente ; choisissez et configurez les règles applicables à votre cas.

### Modèle 1 : Routage basé sur un score

**Calculer un score de risque entier et router en conséquence dans cet exemple :**

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

***

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

***

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

***

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

***

## Diagramme complet de logique de décision

Les quatre graphiques présentent les étapes essentielles. L’arbre textuel ci-dessous conserve le détail technique de l’exemple ; ses destinations restent à configurer.

<details>
<summary>Consulter l’arbre textuel détaillé de l’exemple complet</summary>

```
INVOICE ARRIVES
│
├─ LEVEL 1: EXCEPTION CHECK
│  │
│  ├─ Critical exception or BLOCKED supplier?
│  │  (Criticality must be configured; not every PO mismatch is critical.)
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
│  ├─ Amount missing or invalid?
│  │  ├─ YES → Manual review (explicit example policy)
│  │  └─ NO → Continue to amount thresholds below
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
│  │  │        → WAIT for result; pending must not continue
│  │  │           → Approved: Continue configured processing
│  │  │           → Rejected: Stop chain & handle rejection as configured
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
│              → WAIT for all required results
│                 → All approved: Continue configured processing
│                 → Pending: Do not continue
│                 → Any rejection: Stop chain & handle rejection as configured
│
├─ LEVEL 5: SUPPLIER ANALYSIS (€10,000 ≤ Amount < €50,000)
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
│  │  │                → Pending: Do not continue
│  │  │                → Approved: Continue only after both positive approvals
│  │  │                → Rejected: Stop chain & handle rejection as configured
│  │  │           IF Task 1 Rejected:
│  │  │             → Stop chain & handle rejection as configured
│  │  │           IF Task 1 Pending:
│  │  │             → Do not create Task 2 or continue
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
│  │           → WAIT for result; pending must not continue
│  │              → Approved: Continue configured processing
│  │              → Rejected: Stop chain & handle rejection as configured
│  │
│  └─ [Supplier analysis complete]
│
└─ [All decision levels processed]
```

</details>

***

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

***

### 2. Documenter la logique de décision

**Toujours inclure :**

* L'objectif de chaque point de décision
* La règle métier mise en œuvre
* Les résultats attendus
* La gestion des exceptions

**Exemple de documentation :**

```
Decision Point: Amount Threshold Check
Business Rule: BR-INV-001 (Invoice Approval Matrix)
Purpose: Route invoices based on amount thresholds per company policy
Thresholds:
  < €1,000: Auto-approve (CFO approved threshold)
  €1,000 ≤ Amount < €10,000: Manager approval (Delegation matrix)
  €10,000 ≤ Amount < €50,000: Director approval with supplier checks
  Amount ≥ €50,000: Executive approval
Exceptions: Urgent invoices skip to highest level
Updated: 2025-10-23
Owner: Finance Department
```

***

### 3. Tester tous les chemins

**Matrice de tests proposés — résultats attendus, pas des tests exécutés :**

Ces résultats sont attendus et restent à vérifier dans votre configuration. Renseignez les résultats observés après vos tests.

| Cas de test | Montant  | Type        | Fournisseur | Chemin attendu  | Vérification |
| ----------- | -------- | ----------- | ----------- | --------------- | ------ |
| TC1         | €500     | Facture     | Existant    | Approbation automatique    | À tester      |
| TC2         | €5,000   | Facture     | Existant    | Responsable         | À tester      |
| TC3         | €15,000  | Facture     | Nouveau     | Directeur puis direction financière    | À tester      |
| TC4         | €60,000  | Facture     | Existant    | Direction générale       | À tester      |
| TC5         | €2,000   | Note de crédit | Existant    | Flux de travail de crédit | À tester      |
| TC6         | €100,000 | Facture     | Bloqué     | Arrêter et escalader | À tester      |
| TC7 | 999,99 € | Facture | Existant | Approbation automatique | À tester |
| TC8 | 1 000 € | Facture | Existant | Responsable | À tester |
| TC9 | 9 999,99 € | Facture | Existant | Responsable | À tester |
| TC10 | 10 000 € | Facture | Existant | Directeur + contrôle fournisseur | À tester |
| TC11 | 49 999,99 € | Facture | Existant | Directeur + contrôle fournisseur | À tester |
| TC12 | 50 000 € | Facture | Existant | Direction générale | À tester |
| TC13 | Absent ou invalide | Facture | Existant | Contrôle manuel choisi pour cet exemple | À tester |
| TC14 | 15 000 € | Facture | Nouveau | Directeur en attente : ne pas créer la tâche suivante | À tester |
| TC15 | 15 000 € | Facture | Nouveau | Refus du directeur ou de la direction financière : arrêter la chaîne et traiter le refus | À tester |
| TC16 | 15 000 € | Facture | Nouveau | Deux accords positifs : poursuivre le traitement prévu | À tester |

***

### 4. Surveiller les indicateurs de décision

**Suivre :**

* La répartition sur les chemins de décision
* Le taux d'approbation automatique
* Le taux de révision manuelle
* Le temps de traitement moyen par chemin
* Les taux d'exception
* L'utilisation des chemins

**Exemple fictif d’indicateurs :** les valeurs ci-dessous illustrent un rapport ; elles ne prouvent ni les performances actuelles ni l’exécution de ce workflow.

```
Month: October 2025
Total Invoices: 1,250

Decision Path Distribution:
- Auto-approved (< €1k): 680 (54%)
- Manager path (€1k ≤ Amount < €10k): 420 (34%)
- Director path (€10k ≤ Amount < €50k): 120 (10%)
- Executive path (Amount ≥ €50k): 30 (2%)

Processing Time:
- Auto-approve: < 1 minute
- Manager path: 2.5 days average
- Director path: 1.8 days average
- Executive path: 3.2 days average

Exceptions: 15 (1.2%)
```

***

## Modèles connexes

### Modèles qui fonctionnent bien ensemble :

* [**Modèle de gestion des tâches**](task-management-pattern.md) – Créer des tâches en fonction des décisions
* [**Modèle d'intégration d'API**](api-integration-pattern.md) – Récupérer des données pour la prise de décision
* [**Modèle de rapprochement de commandes (PO Matching)**](po-matching-pattern.md) – Utiliser les résultats de commande dans les décisions
* [**Modèle de transformation des données**](data-transformation-pattern.md) – Transformer les données avant les décisions

***

## Guides connexes

### Prérequis

* [Guide complet des cartes de condition](../and/condition-cards-complete-guide.md) – Toutes les cartes de condition
* [Guide de manipulation des champs](../then/document-field/field-manipulation-guide.md) – Opérations sur les champs
* [Guide d'affectation](../then/assignee/assignment-user-guide.md) – Logique de routage

### Cartes connexes

* **CONDITION\_DOC\_FIELD\_AMOUNT** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md)
* **CONDITION\_DOC\_TYPE\_IS\_ISNOT** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md)
* **CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md)
* **ACTION\_ASSIGN\_TO\_USER** – [Guide d'affectation](../then/assignee/assignment-user-guide.md)
* **tasks\_create** – [Guide d'affectation des tâches](../then/task/task-assignment-guide.md)

### Prochaines étapes

* Créer des tâches : [Modèle de gestion des tâches](task-management-pattern.md)
* Ajouter un rapprochement complexe : [Modèle de rapprochement de commandes (PO Matching)](po-matching-pattern.md)
* Intégrer des API : [Modèle d'intégration d'API](api-integration-pattern.md)

***

**Métadonnées historiques de l’exemple :**

**Version du modèle :** 1.0 **Dernière mise à jour :** 23 octobre 2025 **Difficulté :** Moyenne **Temps estimé :** 30-45 minutes
