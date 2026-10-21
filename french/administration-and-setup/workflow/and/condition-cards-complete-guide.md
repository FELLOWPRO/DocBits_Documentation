# Cartes de condition - Guide complet

## Cartes de condition - Guide complet

Les cartes de condition de cette page se placent dans les groupes **Quand** et **Et** du Concepteur de workflow — elles déterminent si les actions Then s'exécutent. Pour le fonctionnement du canevas — **Ajouter une carte**, **Enregistrer le flux de travail**, **Enregistrer le modèle** — consultez le [guide du Standard Workflow](../standard-workflow-builder) :

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-fr.png" alt="Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution."><figcaption><p>Exemple non enregistré avec les cartes Quand, Et et Alors. Renseignez tous les champs avant exécution.</p></figcaption></figure>

**Couvertures :** 31 cartes de condition restantes

***

### 📌 Informations sur la version

**Statut :** La plupart des cartes de condition sont stables avec des structures à version unique ou double **Modèle de version :** La plupart suivent le modèle v1 → v2 (en ajoutant le support i18n) **Exemple de versions multiples :** CONDITION\_DECISION\_TREE\_DATA (v2-v3)

**Remarque :** Certaines cartes de condition de comparaison de PO ont plusieurs versions. Utilisez ce guide pour le comportement actuel et les notes de version ci-dessous pour les modifications publiées.

📖 [Notes de version du produit](../../../overview-and-basics/release-notes) | [Guide du rapprochement de PO](compare-with-purchase-order/po-matching-complete-guide.md)

***

## Conditions d'état et de statut du document

### Carte : CONDITION\_DOC\_STATUS\_IS\_ISNOT / Vérification de l'état du document

#### Objectif

Vérifie si le document a un statut spécifique

#### Quand utiliser

* Avant d'approuver
* À une étape spécifique du flux de travail
* Routage basé sur l'état

#### Types de statut de document

```
- Upload: Being uploaded
- OCR: Being scanned
- Classification: Type detection
- Ready for Validation: Waiting for review
- Workflow: In process
- Pending Approval: Needs approval
- Pending Second Approval: Needs secondary approval
- Auto Accounting: Auto-booking
- Export: Being exported
- Error: Problem occurred
```

#### Comment ça marche

```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

#### Exemple

```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

#### Paramètres

```
Operator: IS / IS NOT
Status: [Select status]
```

***

### Carte : CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST

#### Objectif

Vérifie si le statut correspond à celui d'une liste

#### Quand utiliser

* Plusieurs statuts valides
* OU logique pour le statut

#### Exemple

```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

***

### Carte : CONDITION\_DOC\_TYPE\_IS\_ISNOT / Vérification du type de document

#### Objectif

Vérifie si le document est d'un type spécifique

#### Types de documents

```
- Invoice
- Credit Note
- Purchase Order
- Delivery Note
- ASN (Advanced Ship Notice)
- Receipt
- Return
- Custom Types
```

#### Comment ça marche

```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

#### Exemple

```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

***

### Carte : CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST

#### Objectif

Vérifie si le type correspond à l'un des éléments de la liste

#### Exemple

```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

***

### Carte : CONDITION\_SUB\_ORG\_IS\_ISNOT / Chèque de sous-organisation

#### Objectif

Vérifie quelle organisation/département possède le document

#### Organisations

```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

#### Exemple

```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

***

### Carte : CONDITION\_PURCHASE\_ORDER\_IMPORT / PO Import Check

#### Objectif

Vérifie si le bon de commande est nouvellement importé ou existant

#### Comment ça marche

```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

#### Quand utiliser

* Traitement différent pour les nouveaux bons de commande
* Ignorer la validation pour les bons de commande connus
* Suivre la première fois que vous voyez un fournisseur

***

## Conditions du responsable

### Carte : CONDITION\_USER\_IS\_ISNOT / Contrôle utilisateur

#### Objectif

Vérifie si le document est attribué à un utilisateur spécifique

#### Comment ça marche

```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

#### Exemple

```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

***

### Carte : CONDITION\_USER\_IS\_ISNOT\_IN\_LIST

#### Objectif

Vérifie s'il est attribué à un utilisateur de la liste

#### Exemple

```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

***

### Carte : CONDITION\_GROUP\_IS\_ISNOT / Chèque Groupe

#### Objectif

Vérifie si attribué à un groupe spécifique

#### Exemple

```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

***

### Carte : CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST

#### Objectif

Vérifie s'il est affecté à un groupe de la liste

#### Exemple

```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

***

## Conditions de date et d'heure

### Carte : CONDITION\_TIME\_IS\_ISNOT\_BETWEEN / Vérification de la plage de dates

#### Objectif

Vérifie si la date se situe entre deux dates

#### Comment ça marche

```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

#### Calcul

```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

#### Quand utiliser

* Vérifiez si c'est en période fiscale
* Vérifiez si dans les délais
* Vérifiez si vous êtes en période promotionnelle

#### Exemple

```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

#### Paramètres

```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

***

### Carte : CONDITION\_TODAY\_IS\_ISNOT / Chèque du jour

#### Objectif

Vérifie si la date du jour correspond aux critères

#### Comment ça marche

```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

#### Cas d'utilisation

```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

#### Exemple

```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

***

### Carte : CONDITION\_CONFIRMED\_DELIVERY\_ACCEPTED\_DATE\_IN\_CALENDAR\_MASTER\_DATA

#### Objectif

Vérifie si la date de livraison correspond aux dates de livraison approuvées dans le calendrier

#### Comment ça marche

```
Delivery Date from Invoice: 2025-10-25
    ↓
Check Master Calendar: Is 2025-10-25 acceptable?
    ↓
(Master calendar has list of acceptable dates)
    ↓
YES: Date is acceptable
NO: Date not in approved list
```

#### Quand utiliser

* Vérifier que la livraison correspond aux dates convenues
* Vérifiez par rapport au calendrier des jours fériés
* Valider par rapport aux dates contractuelles

#### Exemple

```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

***

## Conditions logiques

### Carte : CONDITION\_DECISION\_TREE\_DATA / Retours de la table de décision

#### Objectif

Vérifie si la table de décision a des valeurs de retour

#### Comment ça marche

```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

#### Quand utiliser

* Avant d'utiliser les résultats de la table de décision
* Comme état du portail
* Pour vérifier si le routage est disponible

#### Exemple

```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

***

### Carte : CONDITION\_CONTINUE\_CHANCE / Probabilité aléatoire

#### Objectif

Continue avec une probabilité spécifiée

#### Comment ça marche

```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

#### Quand utiliser

* Flux de travail de test A/B
* Documents d'échantillonnage
* Contrôles de qualité aléatoires

#### Exemple

```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

#### Calcul

```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

***

### Carte : CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE / Vérification des fonctionnalités

#### Objectif

Vérifie si un module/une fonctionnalité spécifique est activé

#### Modules

```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

#### Comment ça marche

```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

#### Quand utiliser

* Flux de travail dépendant des fonctionnalités
* Traitement facultatif
* Vérifiez si la fonctionnalité sous licence est active

***

### Carte : CONDITION\_HTTPS\_REQUEST\_STATUS / Demande de vérification des résultats

#### Objectif

Vérifie si la requête HTTPS a réussi

#### Codes d'état

```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

#### Comment ça marche

```
Send HTTPS request
    ↓
Receive response code
    ↓
Check: Was request successful (200)?
    ↓
YES: Continue with response data
NO: Error handling
```

#### Exemple

```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

***

### Carte : CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT / Vérification du statut du fournisseur

#### Objectif

Vérifie le statut du fournisseur dans le système

#### Statuts des fournisseurs

```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

#### Comment ça marche

```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

#### Exemple

```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

***

### Carte : CONDITION\_SPECIFY\_SUPPLIER\_TYPE

#### Objectif

Spécifie/vérifie le type de fournisseur

#### Types de fournisseurs

```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

#### Comment ça marche

```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

***

## Exemples de flux de décision

### Flux 1 : Traitement basé sur le statut

```
Document Arrives
    ↓
Check: Status = "Ready for Validation"?
    ↓
YES: Validate document
    ↓
Check: Status = "Pending Approval"?
    ↓
YES: Create approval task
    ↓
Check: Status = "Error"?
    ↓
YES: Escalate to manager
```

### Flux 2 : Traitement basé sur le fournisseur

```
Invoice Arrives
    ↓
Check: Supplier status ACTIVE?
    ↓
NO: Block and escalate
    ↓
YES: Check: Supplier is preferred?
    ↓
YES: Fast track approval
NO: Standard approval
```

### Flux 3 : Basé sur le montant avec vérification de la date

```
Invoice Arrives
    ↓
Check: Amount > €10,000?
    ↓
YES: Check: Date within Oct (fiscal period)?
    ↓
YES: Assign to Finance Director
NO: Assign to Finance Manager
```

***

## Comparaison des cartes d'état

| Carte                                        | Checks          | Opérateur      | Use               |
| ------------------------------------------- | --------------- | ------------- | ----------------- |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT           | Document status | EST / N'EST PAS   | Stage check       |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST | Status in list  | DANS / PAS DANS   | Plusieurs statuts |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT             | Document type   | EST / N'EST PAS   | Type filtering    |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST       | Type in list    | DANS / PAS DANS   | Multiple types    |
| CONDITION\_SUB\_ORG\_IS\_ISNOT              | Organisation    | EST / N'EST PAS   | Chèque du département  |
| CONDITION\_USER\_IS\_ISNOT                  | Utilisateur attribué   | EST / N'EST PAS   | User check        |
| CONDITION\_USER\_IS\_ISNOT\_IN\_LIST        | User in list    | DANS / PAS DANS   | Plusieurs utilisateurs    |
| CONDITION\_GROUP\_IS\_ISNOT                 | Groupe assigné  | EST / N'EST PAS   | Group check       |
| CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST       | Group in list   | DANS / PAS DANS   | Plusieurs groupes   |
| CONDITION\_TIME\_IS\_ISNOT\_BETWEEN         | Date range      | ENTRE       | Fenêtre de dates       |
| CONDITION\_TODAY\_IS\_ISNOT                 | La date d'aujourd'hui    | EST / N'EST PAS   | Vérifiez aujourd'hui       |
| CONDITION\_DECISION\_TREE\_DATA             | DT revient      | A / N'A PAS | DT result check   |
| CONDITION\_CONTINUE\_CHANCE                 | Probabilité     | CHANCE        | Random gate       |
| CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE        | Fonctionnalité activée | EST / N'EST PAS   | Vérification des fonctionnalités     |
| CONDITION\_HTTPS\_REQUEST\_STATUS           | Request result  | STATUS        | Response check    |
| CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT      | Supplier status | EST / N'EST PAS   | Supplier check    |

***

## Meilleures pratiques pour les conditions

✅ **Faire :**

* Utiliser des conditions spécifiques
* Tester la logique avec des échantillons
* Conditions de commande logiquement
* Avoir une solution de repli pour tous les chemins
* Documenter la logique complexe

❌ **À ne pas faire :**

* Créer des conditions circulaires (A si B, B si A)
* Rendre les conditions trop complexes
* Oubliez les cas extrêmes
* Supposons que le champ a toujours une valeur
* Créer des conditions impossibles

***

## Combinaison de plusieurs conditions

```
Condition 1: Type = Invoice?
    AND
Condition 2: Amount > €5000?
    AND
Condition 3: Supplier status = Active?
    ↓
ALL TRUE → Process
SOME FALSE → Stop
```

***

## Cartes associées

* **CONDITION\_DOC\_FIELD\_CONTAINS** - Vérification du contenu du champ
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - Comparaison de champs
* **CONDITION\_CHECKBOX\_IS** - Case à cocher
