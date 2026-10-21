# Cartes d'affectation et de création de tâches

## Cartes d'affectation et de création de tâches - Guide complet

**Couvertures :** 12 cartes liées aux tâches

***

Les cartes de tâches de cette page vont dans le groupe **Alors** du Workflow Builder — les actions qui s'exécutent une fois que les conditions Quand/Et correspondent :

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-fr.png" alt="Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution."><figcaption><p>Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution.</p></figcaption></figure>

***

### 📌 Informations sur la version

**Carte la plus évoluée :** tasks\_create (4 versions, v4 la plus récente) **Autres cartes multi-versions :** ACTION\_TASK\_FOR\_GROUP (v4), ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP (v3), ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK (v3), ACTION\_DECISION\_TREE\_CREATE\_TASKS (v3)

**Modifications clés :**

* **v3 → v4 Evolution :** Suppression de l'approche d'arbre de décision, ajout de types d'éléments de travail génériques (tâche, ticket, problème)
* **v2 → v3 Migration :** Ajout de la prise en charge de l'arbre de décision (maintenant en grande partie obsolète)

📖 [Historique complet des versions](../../release.md) | [Versions et comportement des cartes](../../cards-overview/card-versions-guide.md)

***

### Aperçu

Les cartes de tâches créent des affectations de travail pour les membres de l'équipe. Lorsqu'une facture doit être approuvée, vous pouvez créer automatiquement une tâche et l'attribuer à la bonne personne.

***

## Création de tâches de base

### Carte : tasks\_create / Créer une tâche et attribuer à l'utilisateur

#### Objectif

Crée une tâche et l'attribue à une personne spécifique

#### Quand utiliser

* La facture nécessite l'examen d'une personne spécifique
* Approbation requise de la personne nommée
* Transfert à un membre spécifique de l'équipe

#### Paramètres

**Titre** Le nom/sujet de la tâche

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Descriptif** Détails sur la tâche

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priorité**

* 🔴 **High** : Urgent, à faire immédiatement
* 🟡 **Moyen** : Priorité normale
* 🟢 **Low** : Peut être fait plus tard

**Utilisateur attribué** Qui obtient la tâche

```
Example: John Smith (Finance Manager)
```

**Notification par e-mail** Envoyer une alerte par e-mail à la personne désignée ?

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### Exemple

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

***

### Carte : ACTION\_TASK\_FOR\_GROUP / Créer une tâche pour le groupe

#### Objectif

Crée une tâche et l'attribue à un groupe (tous les membres peuvent la voir)

#### Quand utiliser

* Plusieurs personnes peuvent effectuer la tâche
* Tâche pour l'équipe, pas pour l'individu
* La première personne disponible devrait s'en occuper

#### Différence par rapport à la tâche individuelle

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

#### Exemple de flux de travail

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

***

### Carte : ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### Objectif

Crée des tâches basées sur la logique de la table de décision

#### Comment ça marche

```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

#### Quand utiliser

* Différents fournisseurs nécessitent une approbation différente
* Routage complexe basé sur plusieurs facteurs
* Équipe différente en fonction du type de document

#### Exemple

```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

***

### Carte : ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### Objectif

Crée des tâches séquentiellement en fonction de la table de décision. Les tâches sont assignées une par une avec un ordre de priorité.

#### Quand utiliser

* Plusieurs approbations nécessaires en séquence
* Chaîne d'approbation du workflow
* Chaque personne examine puis passe au suivant

#### Comment ça marche

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

#### Système de priorité

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### Exemple de configuration

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

***

### Carte : ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### Objectif

Attribue un document à un utilisateur ET crée une tâche séquentielle

#### Quand utiliser

* Attribuer un document ET créer une tâche en même temps
* Le document doit être examiné par une personne spécifique
* Suivez à la fois l’affectation et la création de tâches

#### Comment ça marche

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### Exemple

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

***

### Carte : ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### Objectif

Attribue un document au groupe ET crée une tâche

#### Quand utiliser

* Le document nécessite l'attention du groupe
* Vous souhaitez suivre la création de tâches
* Créer une tâche initiale puis documenter l'affectation

#### Exemple

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

***

## Création de tâches avancées

### Carte : ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### Objectif

Crée une tâche pour un groupe d'installations spécifique

#### Quand utiliser

* Tâche pour l'équipe de l'entrepôt/installation
* Opérations spécifiques aux installations
* L’emplacement physique est important

#### Exemple

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

***

### Carte : ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### Objectif

Attribution séquentielle des tâches dans toutes les installations

#### Quand utiliser

* Opérations multi-installations
* Les tâches passent d’un établissement à l’autre
* Traitement séquentiel des installations

#### Comment ça marche

```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

#### Exemple

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

***

### Carte : ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### Objectif

Crée une tâche pour le service des achats

#### Quand utiliser

* Tâche pour l'équipe d'approvisionnement
* Tâches de gestion des fournisseurs
* Travaux liés aux achats

#### Exemple

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

***

### Carte : ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### Objectif

Acheminement séquentiel des tâches au sein des achats

#### Quand utiliser

* Processus d'approvisionnement en plusieurs étapes
* Chaîne d'approbation dans les achats
* Chemin d'escalade

#### Exemple

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

***

### Carte : ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### Objectif

Récupérer l'utilisateur du champ du document, attribuer une tâche. Si l'utilisateur est introuvable, utiliser un utilisateur de secours.

#### Quand utiliser

* Utilisateur stocké dans le champ du document
* Le document précise qui doit examiner
* Avoir une personne de secours si l'utilisateur spécifié n'est pas disponible

#### Comment ça marche

```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

#### Exemple

```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

#### Paramètres

```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

***

## Paramètres de tâche courants

Toutes les fiches tâche utilisent ces paramètres :

#### Titre

```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

#### Descriptif

```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

#### Niveaux de priorité

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

#### Date d'échéance (si disponible)

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## Scénarios de flux de travail de tâches

### Scénario 1 : approbation simple

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### Scénario 2 : approbation à plusieurs niveaux

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

### Scénario 3 : tâches parallèles

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

### Scénario 4 : routage conditionnel

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

***

## Meilleures pratiques en matière d'attribution de tâches

✅ **Faire :**

* Inclure des détails spécifiques dans le titre de la tâche
* Définir des niveaux de priorité appropriés
* Fixez des délais réalistes
* Notifier les responsables
* Inclure un lien vers le document
* Utilisez des descriptions claires et exploitables

❌ **À ne pas faire :**

* Créez des titres de tâches vagues (« Revoir ceci »)
* Définir tout comme haute priorité
* Oublier d'avertir la personne désignée
* Créer plusieurs tâches pour le même travail
* Attribuer à des personnes indisponibles

***

## Tâches de dépannage

### "Tâche assignée à personne"

**Cause :** L'utilisateur n'existe pas ou le groupe est vide

**Solution :**

* Vérifier l'orthographe du nom d'utilisateur
* Vérifier que l'utilisateur est actif dans le système
* Vérifier que le groupe a des membres
* Utiliser une solution de secours si nécessaire

### "La personne dit qu'elle n'a pas reçu de notification"

**Cause :** Notification par e-mail désactivée ou e-mail erroné

**Solution :**

* Cochez la case "Envoyer un e-mail"
* Vérifier l'adresse e-mail du destinataire
* Vérifier le dossier spam
* Renvoyer la notification manuellement

### "La mauvaise personne a reçu la tâche"

**Cause :** Logique de routage incorrecte

**Solution :**

* Vérifier les conditions de la table de décision
* Vérifier les paramètres de secours
* Test avec un exemple de document
* Vérifiez les fautes de frappe dans les noms d'utilisateur

### "Trop de tâches créées"

**Cause :** La carte se déclenche plusieurs fois

**Solution :**

* Les conditions de vérification sont suffisamment précises
* Vérifier que la carte ne s'exécute qu'une seule fois par document
* Revoir les conditions "Et"
* Ajouter un filtrage supplémentaire

***

## Tableau de comparaison des cartes de tâches

| Carte                                                        | Crée une tâche | Attribue à            | When        |
| ----------------------------------------------------------- | ------------ | --------------------- | ----------- |
| tasks\_create                                               | Oui          | Individuel            | Toujours      |
| ACTION\_TASK\_FOR\_GROUP                                    | Oui          | Groupe                 | Toujours      |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | Oui          | Résultat du tableau de décision | Conditionnel |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | Oui          | Multiple (séquentiel) | Conditionnel |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | Oui          | Utilisateur + Document       | Conditionnel |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | Oui          | Groupe + Document      | Conditionnel |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | Oui          | Groupe d'installations        | Conditionnel |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | Oui          | Installations multiples   | Conditionnel |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | Oui          | Équipe d'approvisionnement      | Conditionnel |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | Oui          | Multiple (séquentiel) | Conditionnel |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | Oui          | Champ/Retour        | Conditionnel |

***

## Cartes associées

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** - Attribuer un document sans créer de tâche
* **ACTION\_SEND\_EMAIL** - Notifier les personnes directement
* **STAUS\_CHANGE** - Changer le statut au lieu de créer une tâche
* **RUN\_WORKFLOW** - Déclenchez plutôt un flux de travail différent
