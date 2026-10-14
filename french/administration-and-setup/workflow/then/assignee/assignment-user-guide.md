# Cartes d'assignation de documents et d'utilisateurs - Guide complet

Ces cartes se placent dans le groupe **Then** du Concepteur de workflow — les actions exécutées une fois les conditions When/And remplies :

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Les cartes sont ajoutées au groupe <strong>Then</strong> via <strong>Add Card</strong>.</p></figcaption></figure>

**Couvre :** 13 cartes liées à l'assignation et aux utilisateurs

---

## 📌 Informations sur les versions

**Cartes multi-versions :** DOC_USER_ASSIGN (v2 la plus récente, v3 obsolète), DOC_GROUP_ASSIGN (v2 la plus récente, v3 obsolète), OC_ASSIGN_DOC (v2)

**Important :** Les versions v3 ont ajouté la prise en charge de l'arbre de décision mais sont désormais obsolètes
**Recommandation :** Utilisez v2 pour DOC_USER_ASSIGN et DOC_GROUP_ASSIGN

📖 [Historique complet des versions](../../../changelog/release.md#-assignment--routing-cards) | [Base de données des versions de cartes](../../../../DocFlow/docs/card_version.md)

---

# Assignation de document basique

## Carte : DOC_USER_ASSIGN / Assign Document to User

### Objectif
Assigne un document à une personne spécifique pour son action

### Quand l'utiliser
- Le document nécessite l'examen d'une personne spécifique
- Transfert à un membre individuel de l'équipe
- Suivi de la responsabilité
- Assigner du travail à une personne nommée

### Comment ça fonctionne
```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

### Exemple
```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

### Paramètres
```
User: [Select which person]
```

### Remarque
Assigner signifie :
- Le document apparaît comme « assigned to me » pour cette personne
- Cette personne est responsable
- Les autres peuvent toujours voir le document (mais pas comme assigné à eux)
- Une seule assignation à la fois par document

---

## Carte : DOC_GROUP_ASSIGN / Assign Document to Group

### Objectif
Assigne un document à un groupe (tous les membres le voient comme assigné à eux)

### Quand l'utiliser
- Document pour une équipe, pas pour un individu
- Plusieurs personnes peuvent s'en charger
- Responsabilité partagée
- Distribution de la charge de travail de l'équipe

### Comment ça fonctionne
```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

### Exemple
```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

### Paramètres
```
Group: [Select which group]
```

### Différence
```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

---

## Carte : ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE

### Objectif
Assigne un document en fonction de la logique d'une table de décision

### Quand l'utiliser
- Différents fournisseurs nécessitent différents gestionnaires
- Assignation basée sur le montant
- Logique de routage complexe
- Plusieurs conditions pour l'assignation

### Comment ça fonctionne
```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

### Exemple : Assignation basée sur le montant
```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

### Exemple : Assignation basée sur le fournisseur
```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

### Paramètres
```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

---

## Carte : ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL

### Objectif
Assigne un document séquentiellement en fonction d'une table de décision avec priorités

### Quand l'utiliser
- Plusieurs approbations séquentielles
- Différentes personnes à différents niveaux
- Chaîne d'approbation basée sur le montant
- Chemin d'escalade

### Comment ça fonctionne
```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

### Système de priorité
```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

### Exemple : Approbation à plusieurs niveaux
```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

### Paramètres
```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

---

## Carte : ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL

### Objectif
Assigne un document à un utilisateur avec une priorité séquentielle

### Quand l'utiliser
- Le document nécessite une personne spécifique
- Traitement séquentiel clair
- Assignation unique avec ordre

### Comment ça fonctionne
```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

### Exemple
```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

---

## Carte : ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL

### Objectif
Assigne un document séquentiellement à des groupes

### Quand l'utiliser
- Plusieurs approbations de groupe
- Différents départements à chaque étape
- Traitement séquentiel basé sur les équipes

### Comment ça fonctionne
```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

### Exemple
```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

---

## Carte : ACTION_ASSIGN_DOC_TO_FACILITY_GROUP

### Objectif
Assigne un document à un groupe d'établissement spécifique

### Quand l'utiliser
- Document pour un entrepôt/établissement spécifique
- Opérations basées sur l'établissement
- Traitement spécifique à un emplacement

### Exemple
```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

---

## Carte : ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL

### Objectif
Assigne séquentiellement entre établissements

### Quand l'utiliser
- Traitement multi-emplacements
- L'expédition passe par les établissements
- Flux de travail basé sur l'emplacement

### Exemple
```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

---

## Carte : ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP

### Objectif
Assigne un document au département des achats

### Quand l'utiliser
- Prise en charge par l'équipe des achats
- Travail lié aux fournisseurs
- Lié aux commandes d'achat

### Exemple
```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

---

## Carte : ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL

### Objectif
Assignation séquentielle au sein des achats

### Quand l'utiliser
- Processus d'achat en plusieurs étapes
- Chaîne d'approbation dans les achats

### Exemple
```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

---

## Carte : ACTION_CHANGE_DOC_SUBORG / Change Document Sub-Organization

### Objectif
Assigne un document à une sous-organisation différente

### Quand l'utiliser
- Mauvaise organisation sélectionnée
- Besoin de déplacer vers le bon département
- Restructuration organisationnelle

### Comment ça fonctionne
```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

### Exemple
```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

---

## Carte : ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT

### Objectif
Change la sous-organisation en fonction de la valeur d'un champ de document

### Quand l'utiliser
- Sous-organisation stockée dans un champ
- Faire correspondre l'emplacement du document avec le champ
- Assignation automatique d'organisation

### Comment ça fonctionne
```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

### Exemple
```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

---

## Carte : ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK

### Objectif
Assigne un document à un utilisateur à partir d'un champ, avec repli si l'utilisateur est introuvable

### Quand l'utiliser
- Nom d'utilisateur stocké dans un champ de document
- Peut ne pas exister dans le système
- Besoin d'une solution de secours si l'utilisateur n'est pas disponible

### Comment ça fonctionne
```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

### Paramètres
```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

### Exemple
```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

---

## Carte : ACTION_ASSIGN_USER_TO_SUPPLIER

### Objectif
Assigne un document à l'utilisateur qui gère ce fournisseur

### Quand l'utiliser
- Utilisateur lié à un fournisseur
- Gestionnaire de compte fournisseur
- Responsable de la relation fournisseur

### Comment ça fonctionne
```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

---

# Arbres de décision d'assignation

## Exemple de table de décision 1 : Basée sur le montant
```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

## Exemple de table de décision 2 : Basée sur le fournisseur
```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

## Exemple de table de décision 3 : Basée sur le type de document
```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

---

# Exemples de flux de travail d'assignation

## Exemple 1 : Routage simple
```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

## Exemple 2 : Approbation séquentielle
```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

## Exemple 3 : Routage basé sur le montant
```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

## Exemple 4 : Basé sur l'établissement
```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

---

# Bonnes pratiques d'assignation

✅ **À faire :**
- Garder les tables de décision simples
- Tester la logique de routage avec des échantillons
- S'assurer que tous les chemins mènent quelque part
- Disposer d'un repli pour les utilisateurs manquants
- Documenter les décisions de routage

❌ **À ne pas faire :**
- Créer des assignations circulaires (A→B→A)
- Assigner à des utilisateurs inexistants (sans repli)
- Rendre le routage trop complexe
- Oublier de tester le routage
- Assigner à des personnes non disponibles

---

# Dépannage de l'assignation

## « Document non assigné »
**Cause :** Condition non remplie ou l'utilisateur n'existe pas

**Solution :**
- Vérifiez que la condition est vraie
- Vérifiez que l'utilisateur existe dans le système
- Vérifiez les paramètres de repli
- Examinez la logique de la table de décision

## « Mauvaise personne assignée »
**Cause :** Table de décision ou logique de routage incorrecte

**Solution :**
- Testez la table de décision
- Vérifiez les conditions
- Vérifiez le mappage des utilisateurs
- Examinez les valeurs des champs

## « L'assignation semble ignorer quelqu'un »
**Cause :** Ordre séquentiel incorrect

**Solution :**
- Vérifiez les numéros de priorité
- Vérifiez que la séquence est correcte
- Testez avec un échantillon
- Examinez l'ordre de la table de décision

---

# Comparaison des cartes d'assignation

| Carte | Assigne à | Type de routage | Cas d'usage |
|------|-----------|-----------|----------|
| DOC_USER_ASSIGN | Individu | Direct | Assignation simple |
| DOC_GROUP_ASSIGN | Groupe | Direct | Assignation à une équipe |
| ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE | Résultat de décision | Conditionnel | Routage complexe |
| ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL | Multiple (séquentiel) | Conditionnel | Chaîne d'approbation |
| ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL | Utilisateur (séquentiel) | Ordonné | Étapes utilisateur séquentielles |
| ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL | Groupes (séquentiel) | Ordonné | Étapes de groupe séquentielles |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP | Groupe d'établissement | Direct | Spécifique à un établissement |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL | Établissements (séquentiel) | Ordonné | Multi-établissements |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP | Achats | Direct | Flux de travail des achats |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL | Achats (séquentiel) | Ordonné | Chaîne d'approbation des achats |
| ACTION_CHANGE_DOC_SUBORG | Sous-organisation | Direct | Changement de département |
| ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT | Sous-org par champ | Conditionnel | Assignation basée sur un champ |
| ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK | Champ/Repli | Conditionnel | Assignation dynamique d'utilisateur |

---

# Cartes associées

- **ACTION_CREATE_TASK_FOR_USER** - Assigner une tâche à la même personne
- **ACTION_SEND_EMAIL** - Notifier la personne assignée
- **CONDITION_USER_IS_ISNOT** - Vérifier si la bonne personne est assignée
- **CONDITION_GROUP_IS_ISNOT** - Vérifier si le bon groupe est assigné
