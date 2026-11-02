# Taaktoewijzing en creatiekaarten

## Taaktoewijzing en creatiekaarten - Complete gids

**Omslagen:** 12 taakgerelateerde kaarten

***

De taakkaarten op deze pagina bevinden zich in de groep **Dan** van de Workflow Builder – de acties die worden uitgevoerd zodra de When/And-voorwaarden overeenkomen:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-nl.png" alt="Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface."><figcaption><p>Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

***

### 📌 Versie-informatie

**Meest ontwikkelde kaart:** tasks\_create (4 versies, laatste v4) **Andere kaarten met meerdere versies:** ACTION\_TASK\_FOR\_GROUP (v4), ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP (v3), ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK (v3), ACTION\_DECISION\_TREE\_CREATE\_TASKS (v3)

**Belangrijkste wijzigingen:**

* **v3 → v4 Evolutie:** Beslisboombenadering verwijderd, generieke werkitemtypen toegevoegd (taak, ticket, probleem)
* **v2 → v3 Migratie:** Ondersteuning voor beslissingsbomen toegevoegd (nu grotendeels verouderd)

📖 [Volledige versiegeschiedenis](../../release.md) | [Kaartversies en gedrag](../../cards-overview/card-versions-guide.md)

***

### Overzicht

Taakkaarten creëren werkopdrachten voor teamleden. Wanneer een factuur goedkeuring nodig heeft, kunt u automatisch een taak aanmaken en deze aan de juiste persoon toewijzen.

***

## Basistaakcreatie

### Kaart: tasks\_create / Taak maken en toewijzen aan gebruiker

#### Doel

Creëert een taak en wijst deze toe aan een specifieke persoon

#### Wanneer te gebruiken

* Factuur heeft beoordeling van een specifieke persoon nodig
* Goedkeuring vereist van genoemde persoon
* Overdracht aan een specifiek teamlid

#### Parameters

**Titel** De taaknaam/het onderwerp

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Beschrijving** Details over de taak

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Prioriteit**

* 🔴 **High**: Dringend, onmiddellijk doen
* 🟡 **Middelmatig**: Normale prioriteit
* 🟢 **Laag**: kan later worden gedaan

**Toegewezen gebruiker** Wie de taak krijgt

```
Example: John Smith (Finance Manager)
```

**E-mailmelding** E-mailwaarschuwing verzenden naar toegewezen persoon?

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### Voorbeeld

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

### Kaart: ACTION\_TASK\_FOR\_GROUP / Taak voor groep maken

#### Doel

Creëert een taak en wijst deze toe aan een groep (alle leden kunnen deze zien)

#### Wanneer te gebruiken

* Meerdere mensen kunnen de taak uitvoeren
* Taak voor team, niet individueel
* De eerste persoon die beschikbaar is, moet dit afhandelen

#### Verschil met individuele taak

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

#### Voorbeeld workflow

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

### Kaart: ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### Doel

Creëert taken op basis van de logica van de beslissingstabel

#### Hoe het werkt

```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

#### Wanneer te gebruiken

* Verschillende leveranciers hebben verschillende goedkeuringen nodig
* Complexe routing gebaseerd op meerdere factoren
* Ander team op basis van documenttype

#### Voorbeeld

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

### Kaart: ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### Doel

Creëert taken opeenvolgend op basis van de beslissingstabel. Taken worden één voor één toegewezen in volgorde van prioriteit

#### Wanneer te gebruiken

* Meerdere goedkeuringen achter elkaar nodig
* Goedkeuringsketen voor workflows
* Elke persoon beoordeelt en gaat vervolgens door naar de volgende

#### Hoe het werkt

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

#### Prioriteitssysteem

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### Voorbeeldconfiguratie

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

### Kaart: ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### Doel

Wijst een document toe aan één gebruiker EN maakt een opeenvolgende taak

#### Wanneer te gebruiken

* Wijs tegelijkertijd een document toe EN maak een taak
* Het document moet door een specifieke persoon worden beoordeeld
* Houd zowel de toewijzing als de taakcreatie bij

#### Hoe het werkt

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### Voorbeeld

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

### Kaart: ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### Doel

Wijst document toe aan groep EN creëert taak

#### Wanneer te gebruiken

* Document heeft groepsaandacht nodig
* Wilt u het maken van taken bijhouden
* Maak een initiële taak en documenteer vervolgens de toewijzing

#### Voorbeeld

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

## Geavanceerde taakcreatie

### Kaart: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### Doel

Creëert een taak voor een specifieke faciliteitsgroep

#### Wanneer te gebruiken

* Taak voor magazijn/facilitair team
* Faciliteitspecifieke activiteiten
* Fysieke locatie is belangrijk

#### Voorbeeld

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

### Kaart: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### Doel

Opeenvolgende taaktoewijzing over de faciliteiten heen

#### Wanneer te gebruiken

* Operaties met meerdere faciliteiten
* Taken gaan van faciliteit naar faciliteit
* Sequentiële faciliteitsverwerking

#### Hoe het werkt

```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

#### Voorbeeld

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

### Kaart: ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### Doel

Creëert een taak voor de inkoopafdeling

#### Wanneer te gebruiken

* Taak voor het inkoopteam
* Taken voor leveranciersbeheer
* Aankoopgerelateerde werkzaamheden

#### Voorbeeld

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

### Kaart: ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### Doel

Sequentiële taakroutering binnen inkoop

#### Wanneer te gebruiken

* Inkoopprocessen in meerdere stappen
* Goedkeuringsketen bij inkoop
* Escalatie pad

#### Voorbeeld

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

### Kaart: ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### Doel

Gebruiker uit documentveld halen, taak toewijzen Als gebruiker niet gevonden wordt, gebruik dan reservegebruiker

#### Wanneer te gebruiken

* Gebruiker opgeslagen in documentveld
* Document specificeert wie moet beoordelen
* Zorg dat er een back-uppersoon is als de opgegeven gebruiker niet beschikbaar is

#### Hoe het werkt

```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

#### Voorbeeld

```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

#### Parameters

```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

***

## Algemene taakparameters

Alle taakkaarten gebruiken deze parameters:

#### Titel

```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

#### Beschrijving

```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

#### Prioriteitsniveaus

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

#### Vervaldatum (indien beschikbaar)

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## Taakworkflowscenario's

### Scenario 1: Eenvoudige goedkeuring

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### Scenario 2: Goedkeuring op meerdere niveaus

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

### Scenario 3: Parallelle taken

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

### Scenario 4: Voorwaardelijke routering

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

## Beste praktijken voor taaktoewijzing

✅ **Doe:**

* Neem specifieke details op in de taaktitel
* Stel de juiste prioriteitsniveaus in
* Stel realistische deadlines
* Informeer de verantwoordelijkesen
* Voeg een link naar het document toe
* Gebruik duidelijke, bruikbare beschrijvingen

❌ **Niet doen:**

* Maak vage taaktitels ("Bekijk dit")
* Zet alles op Hoge prioriteit
* Vergeten de toegewezen persoon op de hoogte te stellen
* Maak meerdere taken voor hetzelfde werk
* Toewijzen aan niet-beschikbare personen

***

## Problemen oplossen

### "Taak aan niemand toegewezen"

**Oorzaak:** Gebruiker bestaat niet of groep is leeg

**Oplossing:**

* Controleer de spelling van de gebruikersnaam
* Controleer of de gebruiker actief is in het systeem
* Controleer of de groep leden heeft
* Maak indien nodig gebruik van fallback

### 'Persoon zegt dat hij geen melding heeft gekregen'

**Oorzaak:** E-mailmelding uitgeschakeld of e-mail verkeerd

**Oplossing:**

* Controleer of het selectievakje 'E-mail verzenden' is ingeschakeld
* Controleer het e-mailadres van de ontvanger
* Controleer de spammap
* Melding handmatig opnieuw verzenden

### "Verkeerde persoon kreeg taak"

**Oorzaak:** Routeringslogica onjuist

**Oplossing:**

* Controleer de beslissingstabelvoorwaarden
* Controleer de fallback-instellingen
* Test met voorbeelddocument
* Controleer op typefouten in gebruikersnamen

### "Te veel taken aangemaakt"

**Oorzaak:** Kaart meerdere keren geactiveerd

**Oplossing:**

* Controleer of de voorwaarden specifiek genoeg zijn
* Verifieerkaart wordt slechts één keer per document uitgevoerd
* Bekijk de 'En'-voorwaarden
* Voeg extra filtering toe

***

## Vergelijkingstabel taakkaarten

| Kaart                                                        | Creëert een taak | Wijst toe aan            | When        |
| ----------------------------------------------------------- | ------------ | --------------------- | ----------- |
| tasks\_create                                               | Ja          | Individueel            | Altijd      |
| ACTION\_TASK\_FOR\_GROUP                                    | Ja          | Groep                 | Altijd      |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | Ja          | Resultaat van de beslissingstabel | Voorwaardelijk |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | Ja          | Meerdere (sequentieel) | Voorwaardelijk |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | Ja          | Gebruiker + document       | Voorwaardelijk |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | Ja          | Groep + document      | Voorwaardelijk |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | Ja          | Facilitaire Groep        | Voorwaardelijk |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | Ja          | Meerdere faciliteiten   | Voorwaardelijk |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | Ja          | Inkoopteam      | Voorwaardelijk |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | Ja          | Meerdere (sequentieel) | Voorwaardelijk |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | Ja          | Veld/terugval        | Voorwaardelijk |

***

## Gerelateerde kaarten

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** - Document toewijzen zonder taak te maken
* **ACTION\_SEND\_EMAIL** - Breng mensen rechtstreeks op de hoogte
* **STAUS\_CHANGE** - Wijzig de status in plaats van een taak aan te maken
* **RUN\_WORKFLOW** - Activeer in plaats daarvan een andere workflow
