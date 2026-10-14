# Cartes d'assignation et de création de tâches - Guide complet

Ces cartes se placent dans le groupe **Then** du Concepteur de workflow — les actions exécutées une fois les conditions When/And remplies :

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Les cartes sont ajoutées au groupe <strong>Then</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

**Couvre :** 12 cartes liées aux tâches

---

## Aperçu

Les cartes de tâches créent des assignations de travail pour les membres de l'équipe. Lorsqu'une facture nécessite une approbation, vous pouvez automatiquement créer une tâche et l'assigner à la bonne personne.

---

# Création de tâche basique

## Carte : tasks_create / Create Task and Assign to User

### Objectif
Crée une tâche et l'assigne à une personne spécifique

### Quand l'utiliser
- La facture nécessite l'examen d'une personne spécifique
- Approbation requise d'une personne nommée
- Transfert à un membre spécifique de l'équipe

### Paramètres

**Title**
Le nom/objet de la tâche
```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Description**
Détails sur la tâche
```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priority**
- 🔴 **High** : Urgent, à faire immédiatement
- 🟡 **Medium** : Priorité normale
- 🟢 **Low** : Peut être fait plus tard

**Assigned User**
Qui reçoit la tâche
```
Example: John Smith (Finance Manager)
```

**Email Notification**
Envoyer une alerte par e-mail à la personne assignée ?
```
✅ Yes: Person gets email
❌ No: Task only in system
```

### Exemple
```
Condition: "Invoice amount > €10,000"
    ↓
Create Task:
- Title: "High-Value Invoice Review Required"
- Description: "Invoice #INV-2025-789 for €15,000 needs approval"
- Priority: High
- Assigned to: Sarah Johnson (Finance Approver)
- Send Email: Yes
    ↓
Sarah receives task and email notification
```

---

## Carte : ACTION_TASK_FOR_GROUP / Create Task for Group

### Objectif
Crée une tâche et l'assigne à un groupe (tous les membres peuvent la voir)

### Quand l'utiliser
- Plusieurs personnes peuvent effectuer la tâche
- Tâche pour une équipe, pas pour un individu
- La première personne disponible doit s'en charger

### Différence avec une tâche individuelle
```
Individual Task:
- Only John sees it
- John must do it
- Others can't see it

Group Task:
- Everyone in group sees it
- Any group member can claim it
- Distributed workload
```

### Exemple de flux de travail
```
Document arrives
    ↓
Condition: "Is supplier new?"
    ↓
Create Task for Procurement Team:
- Title: "Verify New Supplier Details"
- Description: "Please validate supplier information"
- Priority: Medium
- Group: Procurement Team (10 members)
- Notify: Yes
    ↓
All 10 procurement team members see task
First person available takes it
```

---

## Carte : ACTION_DECISION_TREE_CREATE_TASKS

### Objectif
Crée des tâches en fonction de la logique d'une table de décision

### Comment ça fonctionne
```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

### Quand l'utiliser
- Différents fournisseurs nécessitent une approbation différente
- Routage complexe basé sur plusieurs facteurs
- Équipe différente en fonction du type de document

### Exemple
```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

---

## Carte : ACTION_DECISION_TREE_TASKS_SEQUENTIAL

### Objectif
Crée des tâches séquentiellement en fonction d'une table de décision
Les tâches sont assignées une à la fois selon un ordre de priorité

### Quand l'utiliser
- Plusieurs approbations nécessaires en séquence
- Chaîne d'approbation d'un flux de travail
- Chaque personne examine puis transmet à la suivante

### Comment ça fonctionne
```
Step 1: Create Task for Procurement Manager
        (Priority 1)
    ↓
Step 2: Procurement Manager approves
    ↓
Step 3: Create Task for Finance Manager
        (Priority 2)
    ↓
Step 4: Finance Manager approves
    ↓
Step 5: Export
```

### Système de priorité
```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

### Exemple de configuration
```
Decision Table Returns:
  Level 1: Sarah Johnson (Finance)
  Level 2: Mike Smith (Manager)
  Level 3: Director (for approval)

Task Flow:
1. Sarah reviews → Comments
2. Passes to Mike → He reviews
3. Passes to Director → Final approval
4. All complete → Export
```

---

## Carte : ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL

### Objectif
Assigne le document à un utilisateur ET crée une tâche séquentielle

### Quand l'utiliser
- Assigner le document ET créer une tâche en même temps
- Le document doit être examiné par une personne spécifique
- Suivre à la fois l'assignation et la création de tâche

### Comment ça fonctionne
```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

### Exemple
```
High-value invoice arrives
    ↓
ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL:
- Assign Document to: Finance Manager
- Create Task: "Review & Approve High Value Invoice"
- Priority: High
    ↓
Document AND task both go to Finance Manager
```

---

## Carte : ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL

### Objectif
Assigne le document à un groupe ET crée une tâche

### Quand l'utiliser
- Le document nécessite l'attention d'un groupe
- Vous souhaitez suivre la création de la tâche
- Créer une tâche initiale puis assigner le document

### Exemple
```
New supplier evaluation
    ↓
ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL:
- Document assigned to: Supplier Management Group
- Create Task: "Evaluate New Supplier Credentials"
- Assign Task to: Same group
- Priority: Medium
    ↓
Group members see document and task
```

---

# Création de tâche avancée

## Carte : ACTION_ASSIGN_TASK_TO_FACILITY_GROUP

### Objectif
Crée une tâche pour un groupe d'établissement spécifique

### Quand l'utiliser
- Tâche pour l'équipe d'entrepôt/d'établissement
- Opérations spécifiques à un établissement
- L'emplacement physique est important

### Exemple
```
Document: Shipment notification
    ↓
Create Task for Facility Group:
- Group: Berlin Warehouse Team
- Task: "Prepare items for shipment"
- Items: From document
    ↓
Berlin warehouse team gets task
```

---

## Carte : ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL

### Objectif
Assignation séquentielle de tâches entre établissements

### Quand l'utiliser
- Opérations multi-établissements
- Les tâches passent d'établissement en établissement
- Traitement séquentiel par établissement

### Comment ça fonctionne
```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

### Exemple
```
Manufacturing Document
    ↓
Create Sequential Tasks:
- Task 1: Factory A (Manufacturing) - Priority 1
- Task 2: Quality Team (Testing) - Priority 2
- Task 3: Warehouse (Packing) - Priority 3
- Task 4: Shipping (Dispatch) - Priority 4
    ↓
Each team completes → Passes to next
```

---

## Carte : ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP

### Objectif
Crée une tâche pour le département des achats

### Quand l'utiliser
- Tâche pour l'équipe des achats
- Tâches de gestion des fournisseurs
- Travail lié aux achats

### Exemple
```
Supplier status change notification
    ↓
Create Task for Procurement Group:
- Task: "Update supplier records"
- Supplier: ABC Corp
- Action: Change status to 'On Hold'
- Priority: High
    ↓
Procurement team is notified
```

---

## Carte : ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL

### Objectif
Routage séquentiel de tâches au sein des achats

### Quand l'utiliser
- Processus d'achat en plusieurs étapes
- Chaîne d'approbation dans les achats
- Chemin d'escalade

### Exemple
```
Purchase Requisition received
    ↓
Step 1: Buyer verifies (Priority 1)
    ↓
Step 2: Approver approves (Priority 2)
    ↓
Step 3: Director signs off (Priority 3)
    ↓
All sign-offs complete → Release to supplier
```

---

## Carte : ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK

### Objectif
Obtient l'utilisateur à partir d'un champ de document, assigne la tâche
Si l'utilisateur est introuvable, utilise l'utilisateur de repli

### Quand l'utiliser
- Utilisateur stocké dans un champ de document
- Le document spécifie qui doit l'examiner
- Disposer d'une personne de secours si l'utilisateur spécifié n'est pas disponible

### Comment ça fonctionne
```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

### Exemple
```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

### Paramètres
```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

---

# Paramètres de tâche courants

Toutes les cartes de tâches utilisent ces paramètres :

### Title
```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

### Description
```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

### Niveaux de priorité
```
🔴 HIGH
   - Action needed within hours
   - Blocks other processes
   - Example: Supply missing, urgent approval

🟡 MEDIUM
   - Standard processing
   - Normal timeline
   - Example: Regular invoice review

🟢 LOW
   - Can wait days/weeks
   - Non-urgent
   - Example: Archive old documents
```

### Date d'échéance (si disponible)
```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

---

# Scénarios de flux de travail de tâches

## Scénario 1 : Approbation simple
```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

## Scénario 2 : Approbation à plusieurs niveaux
```
Invoice Arrives (€50,000 - High Value)
    ↓
Create Sequential Tasks:
1. Finance Team (Initial review)
2. Finance Manager (Approval)
3. Director (Final sign-off)
    ↓
Each level completes → Next begins
```

## Scénario 3 : Tâches parallèles
```
Invoice Arrives (From New Supplier)
    ↓
Create Task 1: Quality Team (verify supplier)
Create Task 2: Finance Team (check prices)
Create Task 3: Procurement (check contract)
    ↓
All teams work simultaneously
All must complete before proceeding
```

## Scénario 4 : Routage conditionnel
```
Invoice Arrives
    ↓
Decision Table:
  If amount > €10k → Assign to Director
  If amount €1k-€10k → Assign to Manager
  If amount < €1k → Assign to Team Lead
    ↓
Task created for correct person
```

---

# Bonnes pratiques d'assignation de tâches

✅ **À faire :**
- Inclure des détails spécifiques dans le titre de la tâche
- Définir des niveaux de priorité appropriés
- Fixer des échéances réalistes
- Notifier les personnes assignées
- Inclure un lien vers le document
- Utiliser des descriptions claires et exploitables

❌ **À ne pas faire :**
- Créer des titres de tâche vagues (« Examiner ceci »)
- Tout définir comme priorité High
- Oublier de notifier la personne assignée
- Créer plusieurs tâches pour le même travail
- Assigner à des personnes non disponibles

---

# Dépannage des tâches

## « La tâche n'est assignée à personne »
**Cause :** L'utilisateur n'existe pas ou le groupe est vide

**Solution :**
- Vérifiez l'orthographe du nom de l'utilisateur
- Vérifiez que l'utilisateur est actif dans le système
- Vérifiez que le groupe a des membres
- Utilisez un repli si nécessaire

## « La personne dit ne pas avoir reçu de notification »
**Cause :** Notification par e-mail désactivée ou e-mail incorrect

**Solution :**
- Vérifiez que la case « Send Email » est activée
- Vérifiez l'adresse e-mail du destinataire
- Vérifiez le dossier spam
- Renvoyez la notification manuellement

## « La mauvaise personne a reçu la tâche »
**Cause :** Logique de routage incorrecte

**Solution :**
- Vérifiez les conditions de la table de décision
- Vérifiez les paramètres de repli
- Testez avec un document d'exemple
- Vérifiez les fautes de frappe dans les noms d'utilisateur

## « Trop de tâches créées »
**Cause :** La carte se déclenche plusieurs fois

**Solution :**
- Vérifiez que les conditions sont suffisamment spécifiques
- Vérifiez que la carte ne s'exécute qu'une fois par document
- Examinez les conditions « And »
- Ajoutez un filtrage supplémentaire

---

# Tableau comparatif des cartes de tâches

| Carte | Crée une tâche | Assigne à | Quand |
|------|-------------|-----------|------|
| tasks_create | Oui | Individu | Toujours |
| ACTION_TASK_FOR_GROUP | Oui | Groupe | Toujours |
| ACTION_DECISION_TREE_CREATE_TASKS | Oui | Résultat de la table de décision | Conditionnel |
| ACTION_DECISION_TREE_TASKS_SEQUENTIAL | Oui | Multiple (séquentiel) | Conditionnel |
| ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL | Oui | Utilisateur + Document | Conditionnel |
| ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL | Oui | Groupe + Document | Conditionnel |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP | Oui | Groupe d'établissement | Conditionnel |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL | Oui | Plusieurs établissements | Conditionnel |
| ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP | Oui | Équipe des achats | Conditionnel |
| ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL | Oui | Multiple (séquentiel) | Conditionnel |
| ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK | Oui | Champ/Repli | Conditionnel |

---

# Cartes associées

- **ACTION_ASSIGN_DOCUMENT_TO_USER** - Assigner un document sans créer de tâche
- **ACTION_SEND_EMAIL** - Notifier les personnes directement
- **STAUS_CHANGE** - Changer le statut au lieu de créer une tâche
- **RUN_WORKFLOW** - Déclencher un autre flux de travail à la place
