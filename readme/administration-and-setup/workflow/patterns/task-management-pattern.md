# Modèle de gestion des tâches

**Type de modèle :** Gestion de workflow
**Complexité :** Faible-Moyenne
**Mise en place estimée :** 30-45 minutes
**Cas d'usage courants :** Workflows d'approbation, tâches de révision, gestion des exceptions, escalade

---

Vous construisez ce modèle dans le **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Cliquez sur **Add Card** pour ouvrir la bibliothèque de cartes et sélectionnez les cartes utilisées par ce modèle — `tasks_create`, `ACTION_ASSIGN_TO_USER`, `ACTION_SEND_EMAIL_TO_GROUPS` et `CONDITION_TASK_STATUS` (la catégorie **Assignee** contient les cartes de tâche et d'affectation) :

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Bibliothèque Add Card dans le Workflow Builder, regroupée par catégorie"><figcaption><p>La bibliothèque <strong>Add Card</strong> — les cartes de tâche, d'affectation et de notification se trouvent sous les catégories <strong>Assignee</strong> et <strong>Status</strong>.</p></figcaption></figure>

---

## Vue d'ensemble du modèle

Ce modèle montre comment créer, affecter, suivre et gérer des tâches dans les workflows DocBits. Les tâches sont des éléments de travail concrets affectés à des utilisateurs ou des groupes qui doivent être terminés avant que le workflow du document puisse se poursuivre.

**Ce que fait ce modèle :**
1. Crée des tâches en fonction des conditions du workflow
2. Affecte les tâches aux utilisateurs ou groupes appropriés
3. Définit les propriétés des tâches (priorité, échéance, description)
4. Envoie des notifications lors de la création des tâches
5. Suit le statut et l'achèvement des tâches
6. Route les documents en fonction des résultats des tâches

---

## Quand utiliser ce modèle

Utilisez ce modèle lorsque vous devez :
- ✅ Créer des workflows d'approbation
- ✅ Affecter des tâches de révision aux utilisateurs
- ✅ Traiter les exceptions nécessitant une intervention humaine
- ✅ Escalader les problèmes vers les responsables
- ✅ Créer des chaînes d'approbation à plusieurs niveaux
- ✅ Suivre qui doit faire quoi
- ✅ Fixer des échéances pour les actions

**N'utilisez pas ce modèle lorsque :**
- ❌ aucune action humaine n'est requise (utilisez plutôt le traitement automatique)
- ❌ il s'agit seulement de notifier (utilisez plutôt l'e-mail)
- ❌ un simple routage de document suffit (utilisez plutôt l'affectation)

---

## Exemple complet de workflow

### Scénario : Approbation de factures avec routage basé sur le montant

**Exigence métier :**
- Factures < 1 000 € : Approbation automatique (aucune tâche nécessaire)
- Factures 1 000-10 000 € : Tâche d'approbation au responsable
- Factures > 10 000 € : Double approbation (responsable + directeur)
- Tous les approbateurs reçoivent une notification par e-mail
- Les tâches ont une échéance de 3 jours

**Cartes de workflow utilisées :**
1. CONDITION_DOC_FIELD_AMOUNT – Vérifier le montant de la facture
2. tasks_create – Créer une tâche d'approbation
3. ACTION_ASSIGN_TO_USER – Affecter la tâche à l'approbateur
4. ACTION_SEND_EMAIL_TO_GROUPS – Envoyer une notification
5. CONDITION_TASK_STATUS – Vérifier si la tâche est terminée
6. ACTION_APPROVE_DOCUMENT – Approuver après l'achèvement de la tâche

---

## Mise en œuvre étape par étape

### Étape 1 : Vérifier le seuil de montant

**Carte :** CONDITION_DOC_FIELD_AMOUNT ou une condition de champ similaire

**Configuration pour le chemin 1 (< 1 000 €) :**
```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Configuration pour le chemin 2 (1 000-10 000 €) :**
```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Configuration pour le chemin 3 (> 10 000 €) :**
```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Référence du guide :** [Guide des cartes de condition](../and/condition-cards-complete-guide.md)

---

### Étape 2A : Approuver automatiquement les petites factures (< 1 000 €)

**Aucune tâche nécessaire pour les petits montants**

**Cartes :**
- ACTION_SET_FIELD_TO_TEXT
  - Définir « Approval_Type » = « AUTO »
  - Définir « Approval_Reason » = « Amount below threshold »
- ACTION_APPROVE_DOCUMENT

**Résultat :** Document approuvé automatiquement, aucune tâche créée

---

### Étape 2B : Créer une tâche d'approbation pour le responsable (1 000-10 000 €)

**Carte :** tasks_create (v4 recommandée)

**Configuration :**
```json
{
  "task_type": "Approval",
  "task_title": "Approve Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "Please approve invoice from {{Supplier_Name}}\n\nAmount: €{{Total_Amount}}\nInvoice Number: {{Invoice_Number}}\nInvoice Date: {{Invoice_Date}}\n\nReview and approve within 3 business days.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "{{DOCUMENT_FIELD:Approving_Manager}}",
  "task_category": "Invoice Approval",
  "required_action": "Approve or Reject"
}
```

**Mappage des champs :**
- `{{DOCUMENT_NUMBER}}` – ID de document automatique
- `{{Total_Amount}}` – Champ : Total_Amount
- `{{Supplier_Name}}` – Champ : Supplier_Name
- `{{Invoice_Number}}` – Champ : Invoice_Number
- `{{Invoice_Date}}` – Champ : Invoice_Date
- `{{Approving_Manager}}` – Champ ou utilisateur fixe

**Référence du guide :** [Guide d'affectation des tâches](../then/task/task-assignment-guide.md)

---

### Étape 2C : Créer des tâches de double approbation (> 10 000 €)

**Deux tâches successives pour les factures de montant élevé**

**Tâche 1 : Approbation par le responsable**
```json
{
  "task_type": "First Approval",
  "task_title": "URGENT: Approve High-Value Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "HIGH VALUE INVOICE REQUIRES APPROVAL\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nThis invoice exceeds €10,000 and requires dual approval.\nYour approval is required before Director review.",
  "priority": "High",
  "deadline_days": 2,
  "assign_to": "Finance_Manager",
  "task_category": "High-Value Approval",
  "next_task": "Director_Approval"
}
```

**Tâche 2 : Approbation par le directeur (créée après l'achèvement de la tâche 1)**
```json
{
  "task_type": "Second Approval",
  "task_title": "Final Approval: Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "FINAL APPROVAL REQUIRED\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nFirst approval: Completed by {{Task1_Approver}} on {{Task1_Date}}\n\nYour final approval required.",
  "priority": "High",
  "deadline_days": 1,
  "assign_to": "Finance_Director",
  "task_category": "Final Approval",
  "prerequisite_task": "Manager_Approval"
}
```

---

### Étape 3 : Affecter la tâche à un utilisateur/un groupe

**Carte :** ACTION_ASSIGN_TO_USER ou ACTION_ASSIGN_TO_GROUP

**Option 1 : Affecter à un utilisateur spécifique**
```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Option 2 : Affecter à un groupe**
```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Option 3 : Affectation séquentielle**
```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Référence du guide :** [Guide d'affectation](../then/assignee/assignment-user-guide.md)

---

### Étape 4 : Envoyer une notification par e-mail

**Carte :** ACTION_SEND_EMAIL_TO_GROUPS

**Configuration :**
```json
{
  "recipients": [
    "{{TASK_ASSIGNEE_EMAIL}}",
    "finance-notifications@company.com"
  ],
  "subject": "New Task Assigned: Approve Invoice {{DOCUMENT_NUMBER}}",
  "body": "Dear {{TASK_ASSIGNEE_NAME}},\n\nA new approval task has been assigned to you:\n\nTask: Approve Invoice {{DOCUMENT_NUMBER}}\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\nDeadline: {{TASK_DEADLINE}}\nPriority: {{TASK_PRIORITY}}\n\nPlease log in to DocBits to review and approve:\n{{DOCUMENT_LINK}}\n\nBest regards,\nDocBits Automation"
}
```

**Variables d'e-mail :**
- `{{TASK_ASSIGNEE_EMAIL}}` – E-mail du destinataire de la tâche
- `{{TASK_ASSIGNEE_NAME}}` – Nom du destinataire de la tâche
- `{{DOCUMENT_NUMBER}}` – ID du document
- `{{TASK_DEADLINE}}` – Date d'échéance de la tâche
- `{{TASK_PRIORITY}}` – Niveau de priorité de la tâche
- `{{DOCUMENT_LINK}}` – Lien direct vers le document

**Référence du guide :** [Guide d'envoi d'e-mails à des groupes](../then/action/send-email-groups-guide.md)

---

### Étape 5 : Suivre le statut de la tâche

**Carte :** CONDITION_TASK_STATUS ou un vérificateur de statut de tâche similaire

**Configuration :**
```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Options de statut :**
- CREATED – Tâche tout juste créée
- ASSIGNED – Tâche affectée à un utilisateur
- IN_PROGRESS – L'utilisateur a commencé à travailler sur la tâche
- COMPLETED – Tâche terminée
- APPROVED – Tâche approuvée
- REJECTED – Tâche rejetée
- CANCELLED – Tâche annulée
- OVERDUE – Tâche en retard

**Logique :**
```
IF TASK_STATUS = COMPLETED AND TASK_RESULT = APPROVED:
  → Continue to next step (or next approval level)
  → Update document status
  → Log approval

IF TASK_STATUS = COMPLETED AND TASK_RESULT = REJECTED:
  → Stop workflow
  → Send rejection notification
  → Create review task for corrections

IF TASK_STATUS = OVERDUE:
  → Escalate to manager
  → Send reminder email
  → Create escalation task
```

---

### Étape 6 : Terminer le workflow en fonction du résultat de la tâche

**Après l'achèvement de la tâche :**

**Scénario A : Tâche approuvée**
```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Scénario B : Tâche rejetée**
```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Scénario C : Tâche en retard**
```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

---

## Diagramme de workflow complet

```
INVOICE ARRIVES
│
├─ CHECK AMOUNT
│  │
│  ├─ Amount < €1,000 ✅
│  │  │
│  │  ├─ Set Approval_Type = "AUTO"
│  │  └─ Auto-Approve Document
│  │     → END (Approved)
│  │
│  ├─ Amount €1,000-€10,000 ⚠️
│  │  │
│  │  ├─ CREATE TASK: Manager Approval
│  │  │  - Title: "Approve Invoice"
│  │  │  - Priority: Medium
│  │  │  - Deadline: 3 days
│  │  │  │
│  │  │  ├─ ASSIGN TO: Finance Manager
│  │  │  │
│  │  │  ├─ SEND EMAIL: Notification
│  │  │  │
│  │  │  ├─ WAIT FOR TASK COMPLETION
│  │  │  │  │
│  │  │  │  ├─ TASK APPROVED ✅
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "APPROVED"
│  │  │  │  │  └─ Approve Document
│  │  │  │  │     → END (Approved)
│  │  │  │  │
│  │  │  │  ├─ TASK REJECTED ❌
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "REJECTED"
│  │  │  │  │  ├─ Reject Document
│  │  │  │  │  └─ Create Correction Task
│  │  │  │  │     → END (Rejected)
│  │  │  │  │
│  │  │  │  └─ TASK OVERDUE ⏰
│  │  │  │     │
│  │  │  │     ├─ Send Reminder Email
│  │  │  │     ├─ Escalate to Director
│  │  │  │     └─ Create Escalation Task
│  │  │  │        → WAIT (Escalated)
│  │  │  │
│  │  │  └─ [Task tracking active]
│  │  │
│  │  └─ [Manager approval path]
│  │
│  └─ Amount > €10,000 🚨
│     │
│     ├─ CREATE TASK 1: Manager First Approval
│     │  - Title: "URGENT: First Approval"
│     │  - Priority: High
│     │  - Deadline: 2 days
│     │  │
│     │  ├─ ASSIGN TO: Finance Manager
│     │  ├─ SEND EMAIL: High Priority Notification
│     │  │
│     │  ├─ WAIT FOR TASK 1 COMPLETION
│     │  │  │
│     │  │  ├─ TASK 1 APPROVED ✅
│     │  │  │  │
│     │  │  │  ├─ CREATE TASK 2: Director Final Approval
│     │  │  │  │  - Title: "Final Approval Required"
│     │  │  │  │  - Priority: High
│     │  │  │  │  - Deadline: 1 day
│     │  │  │  │  │
│     │  │  │  │  ├─ ASSIGN TO: Finance Director
│     │  │  │  │  ├─ SEND EMAIL: Final Approval Notification
│     │  │  │  │  │
│     │  │  │  │  ├─ WAIT FOR TASK 2 COMPLETION
│     │  │  │  │  │  │
│     │  │  │  │  │  ├─ TASK 2 APPROVED ✅
│     │  │  │  │  │  │  │
│     │  │  │  │  │  │  ├─ Set Dual_Approval = "COMPLETE"
│     │  │  │  │  │  │  └─ Approve Document
│     │  │  │  │  │  │     → END (Dual Approved)
│     │  │  │  │  │  │
│     │  │  │  │  │  └─ TASK 2 REJECTED ❌
│     │  │  │  │  │     │
│     │  │  │  │  │     ├─ Reject Document
│     │  │  │  │  │     └─ Notify All Parties
│     │  │  │  │  │        → END (Final Rejected)
│     │  │  │  │  │
│     │  │  │  │  └─ [Task 2 tracking]
│     │  │  │  │
│     │  │  │  └─ [Task 2 created]
│     │  │  │
│     │  │  └─ TASK 1 REJECTED ❌
│     │  │     │
│     │  │     ├─ Reject Document (No Task 2 created)
│     │  │     └─ Notify Supplier
│     │  │        → END (First Rejected)
│     │  │
│     │  └─ [Task 1 tracking]
│     │
│     └─ [Dual approval path]
│
└─ [Amount check complete]
```

---

## Gabarits de configuration

### Gabarit 1 : Tâche d'approbation simple

```json
{
  "card": "tasks_create",
  "task_title": "Approve {{DOCUMENT_TYPE}} {{DOCUMENT_NUMBER}}",
  "task_description": "Please review and approve this document.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "approver@company.com",
  "category": "Approval"
}
```

---

### Gabarit 2 : Tâche de révision avec détails

```json
{
  "card": "tasks_create",
  "task_title": "Review Exception: {{EXCEPTION_TYPE}}",
  "task_description": "Document: {{DOCUMENT_NUMBER}}\nException: {{EXCEPTION_REASON}}\n\nDetails:\n- Supplier: {{Supplier_Name}}\n- Amount: €{{Total_Amount}}\n- Date: {{Document_Date}}\n\nAction Required: Review and resolve exception",
  "priority": "High",
  "deadline_days": 1,
  "assign_to_group": "Exceptions Team",
  "category": "Exception Handling"
}
```

---

### Gabarit 3 : Tâche d'escalade

```json
{
  "card": "tasks_create",
  "task_title": "ESCALATION: {{ORIGINAL_TASK_TITLE}}",
  "task_description": "ESCALATED TASK\n\nOriginal Task: {{ORIGINAL_TASK_ID}}\nOriginal Assignee: {{ORIGINAL_ASSIGNEE}}\nDeadline Passed: {{ORIGINAL_DEADLINE}}\nDays Overdue: {{DAYS_OVERDUE}}\n\nPlease review and take immediate action.",
  "priority": "Urgent",
  "deadline_days": 1,
  "assign_to": "manager@company.com",
  "category": "Escalation",
  "parent_task": "{{ORIGINAL_TASK_ID}}"
}
```

---

## Modèles avancés

### Modèle 1 : Approbation séquentielle à plusieurs niveaux

**Utilisation :** Les factures doivent passer par plusieurs approbateurs successivement

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Mise en œuvre :**
```
1. Create Task 1 for Clerk
2. Wait for Task 1 completion
3. IF Task 1 = APPROVED:
     Create Task 2 for Manager
4. Wait for Task 2 completion
5. IF Task 2 = APPROVED:
     Create Task 3 for Director
6. Wait for Task 3 completion
7. IF Task 3 = APPROVED:
     Approve Document
```

---

### Modèle 2 : Approbation parallèle par plusieurs personnes

**Utilisation :** Plusieurs personnes doivent approuver simultanément

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Mise en œuvre :**
```
1. Create 3 tasks simultaneously
2. Track all 3 task statuses
3. WAIT until ALL tasks completed
4. IF ALL = APPROVED:
     Approve Document
   ELSE:
     Reject Document
```

---

### Modèle 3 : Création conditionnelle de tâches

**Utilisation :** Créer différentes tâches en fonction de conditions

```
IF Supplier = "New":
  → Create "New Supplier Review" task
ELSE IF Amount > €50,000:
  → Create "High Value Approval" task
ELSE IF Document has errors:
  → Create "Error Correction" task
ELSE:
  → Create "Standard Approval" task
```

---

### Modèle 4 : Escalade basée sur l'échéance

**Utilisation :** Escalader automatiquement si la tâche n'est pas terminée à temps

```
Day 0: Create task for User A (3-day deadline)
Day 3: IF not completed:
         → Send reminder to User A
Day 4: IF still not completed:
         → Create escalation task for Manager B
         → Notify both User A and Manager B
Day 5: IF still not completed:
         → Create urgent task for Director C
         → High priority notification
```

---

## Gestion des erreurs

### Scénario 1 : Destinataire introuvable

**Problème :** L'utilisateur n'existe pas ou est inactif

**Solution :**
```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

---

### Scénario 2 : Échec de la création de tâche

**Problème :** Erreur système lors de la création de la tâche

**Solution :**
```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

---

### Scénario 3 : Aucune réaction à la tâche

**Problème :** L'utilisateur ne termine pas la tâche dans les délais

**Solution :**
```
1. Monitor task deadline
2. Day before deadline:
     → Send reminder email
3. On deadline day:
     → Send urgent reminder
4. After deadline:
     → Create escalation task
     → Notify manager
     → Log overdue event
```

---

## Liste de vérification de test

- [ ] Tâche créée avec succès
- [ ] Tâche affectée au bon utilisateur/au bon groupe
- [ ] Notification par e-mail envoyée
- [ ] La tâche apparaît dans la liste des tâches de l'utilisateur
- [ ] Propriétés de la tâche correctes (titre, description, priorité, échéance)
- [ ] L'utilisateur peut terminer la tâche
- [ ] Le workflow se poursuit après l'achèvement de la tâche
- [ ] Le workflow d'approbation fonctionne correctement
- [ ] Le workflow de rejet fonctionne correctement
- [ ] L'escalade se déclenche au bon moment
- [ ] La gestion des retards fonctionne
- [ ] Toutes les notifications par e-mail envoyées
- [ ] Les mises à jour de champs fonctionnent correctement

---

## Exemples concrets

### Exemple 1 : Exception lors du rapprochement de commande à trois voies

**Scénario :** La facture ne correspond pas à la commande, une révision est nécessaire

```
1. PO Matching fails (price variance > 5%)
2. Create Task: "Review PO Mismatch"
   - Assign to: Procurement Officer
   - Priority: High
   - Description: Include variance details
3. Send email with comparison table
4. Wait for task completion
5. IF Approved: Continue processing
   IF Rejected: Return to supplier
```

---

### Exemple 2 : Approbation d'une facture fournisseur

**Scénario :** La facture d'un nouveau fournisseur nécessite une approbation particulière

```
1. Check if supplier is new (< 6 months old)
2. IF New:
     Create Task: "New Supplier Invoice Review"
     - Assign to: Procurement Manager
     - Include supplier details
     - Require supplier verification
3. After approval:
     Add to approved supplier list
     Continue normal workflow
```

---

### Exemple 3 : Traitement de fin de mois

**Scénario :** Les factures de fin de mois nécessitent un traitement urgent

```
1. Check if document date in last 3 days of month
2. IF Yes:
     Create Task: "URGENT: Month-End Invoice"
     - Priority: Urgent
     - Deadline: 1 day
     - Assign to: Finance Team (all members)
     - Flag for expedited processing
3. Send urgent email notification
4. Track completion
```

---

## Conseils de performance

✅ **Bonnes pratiques :**
- Fixer des échéances réalistes
- Utiliser des titres et descriptions de tâches clairs
- Inclure toutes les informations nécessaires dans la tâche
- Notifier en temps utile
- Surveiller les taux d'achèvement des tâches
- Escalader automatiquement les tâches en retard
- Journaliser toutes les activités liées aux tâches
- Réviser les schémas de tâches mensuellement

❌ **À éviter :**
- Créer des tâches pour tout
- Descriptions de tâches vagues
- Échéances irréalistes
- Trop d'e-mails de notification
- Aucun chemin d'escalade
- Ignorer les tâches en retard
- Ne pas suivre les indicateurs de tâches

---

## Modèles connexes

### Modèles qui fonctionnent bien ensemble :

- **[Modèle d'intégration d'API](api-integration-pattern.md)** – Créer des tâches pour les erreurs d'API
- **[Modèle de rapprochement de commandes (PO Matching)](po-matching-pattern.md)** – Créer des tâches en cas d'écarts de commande
- **[Modèle de logique de décision](decision-logic-pattern.md)** – Router vers le type de tâche approprié
- **[Modèle de transformation des données](data-transformation-pattern.md)** – Transformer les données avant la création de la tâche

---

## Guides connexes

### Prérequis
- [Guide d'affectation des tâches](../then/task/task-assignment-guide.md) – Documentation de la carte de tâche
- [Guide d'affectation](../then/assignee/assignment-user-guide.md) – Affectation aux utilisateurs
- [Guide d'envoi d'e-mails à des groupes](../then/action/send-email-groups-guide.md) – Notifications par e-mail

### Cartes connexes
- **tasks_create** – [Guide d'affectation des tâches](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** – [Guide d'affectation](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** – [Guide e-mail](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** – [Guide des cartes de condition](../and/condition-cards-complete-guide.md)

### Prochaines étapes
- Ajouter des notifications par e-mail : [Guide e-mail](../then/action/send-email-groups-guide.md)
- Mettre en place un routage complexe : [Modèle de logique de décision](decision-logic-pattern.md)

---

**Version du modèle :** 1.0
**Dernière mise à jour :** 23 octobre 2025
**Difficulté :** Faible-Moyenne
**Temps estimé :** 30-45 minutes
**Taux de réussite :** Très élevé
