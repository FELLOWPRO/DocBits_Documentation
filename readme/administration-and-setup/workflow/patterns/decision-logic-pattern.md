# Beslissingslogica Patroon

**Patroontype:** Voorwaardelijke Routering & Logica
**Complexiteit:** Gemiddeld
**Geschatte Insteltijd:** 30-45 minuten
**Veelvoorkomende Gebruiksscenario's:** Routering met meerdere paden, voorwaardelijke verwerking, beslissingsbomen, implementatie van bedrijfsregels

---

U bouwt dit patroon in de **Workflow Builder** (Workflow Dashboard → Workflowlijst → Workflow Toevoegen). Klik op **Add Card** en open de categorie **Logic** — deze bevat de voorwaarde- en vertakkingskaarten die de beslissingsboom aansturen, die u combineert met de **And**-groep om meerdere voorwaarden te evalueren:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card-bibliotheek in de Workflow Builder, gegroepeerd per categorie"><figcaption><p>De <strong>Add Card</strong>-bibliotheek — voorwaarde- en vertakkingskaarten bevinden zich onder de categorie <strong>Logic</strong>.</p></figcaption></figure>

---

## Patroonoverzicht

Dit patroon demonstreert hoe u complexe beslissingslogica in DocBits workflows kunt implementeren met behulp van conditiekaarten om documenten via verschillende verwerkingspaden te routeren op basis van documentkenmerken, veldwaarden en bedrijfsregels.

**Wat Dit Patroon Doet:**
1. Evalueert meerdere condities in volgorde of parallel
2. Routeert documenten naar verschillende paden op basis van condities
3. Implementeert bedrijfsregels en beleid
4. Handelt complexe beslissingsbomen af
5. Combineert meerdere criteria voor routeringsbeslissingen

---

## Wanneer Dit Patroon Te Gebruiken

Gebruik dit patroon wanneer u het volgende moet doen:
- ✅ Documenten routeren op basis van bedragdrempels
- ✅ Verschillende regels toepassen voor verschillende documenttypen
- ✅ Goedkeuringslogica op meerdere niveaus implementeren
- ✅ Complexe bedrijfsbeleidsregels afhandelen
- ✅ Dynamische routering creëren op basis van meerdere criteria
- ✅ Logica voor uitzonderingsafhandeling implementeren
- ✅ Goedkeuringsmatrices implementeren

**Gebruik dit patroon niet wanneer:**
- ❌ Eenvoudige lineaire workflow voldoende is
- ❌ Alle documenten hetzelfde pad volgen
- ❌ Geen voorwaardelijke verwerking nodig is

---

## Typen Beslissingslogica

### 1. Eenvoudige ALS-DAN Logica

```
ALS conditie:
  → Actie A
ANDERS:
  → Actie B
```

**Voorbeeld:**
```
ALS Bedrag > €10.000:
  → Toewijzen aan Directeur
ANDERS:
  → Toewijzen aan Manager
```

### 2. Meerdere Criteria (EN Logica)

```
ALS conditie1 EN conditie2 EN conditie3:
  → Actie A
ANDERS:
  → Actie B
```

**Voorbeeld:**
```
ALS Bedrag > €10.000 EN Leverancier = "Nieuw" EN Afdeling = "IT":
  → Toewijzen aan IT-Directeur + CFO (dubbele goedkeuring)
ANDERS:
  → Standaard goedkeuringsworkflow
```

### 3. Alternatieve Criteria (OF Logica)

```
ALS conditie1 OF conditie2 OF conditie3:
  → Actie A
ANDERS:
  → Actie B
```

**Voorbeeld:**
```
ALS Bedrag > €50.000 OF Leverancier is "Geblokkeerd" OF Document heeft "Urgent" vlag:
  → Onmiddellijk escaleren
ANDERS:
  → Standaardverwerking
```

### 4. Geneste Beslissingsboom

```
ALS conditie1:
  ALS conditie2:
    → Actie A
  ANDERS:
    → Actie B
ANDERS:
  ALS conditie3:
    → Actie C
  ANDERS:
    → Actie D
```

**Voorbeeld:**
```
ALS Document_Type = "Factuur":
  ALS Bedrag > €10.000:
    → Factuurworkflow hoge waarde
  ANDERS:
    → Standaard factuurworkflow
ANDERS ALS Document_Type = "Creditnota":
  ALS Bedrag > €5.000:
    → Creditnotaworkflow hoge waarde
  ANDERS:
    → Standaard creditnotaworkflow
```

---

## Compleet Workflowvoorbeeld

### Scenario: Factuurgoedkeuringsmatrix

**Bedrijfsregels:**
1. Bedrag < €1.000: Automatisch goedkeuren
2. Bedrag €1.000-€10.000: Goedkeuring manager
3. Bedrag > €10.000 EN Nieuwe Leverancier: Goedkeuring Directeur + CFO
4. Bedrag > €10.000 EN Bestaande Leverancier: Alleen goedkeuring Directeur
5. Elk bedrag met PO-mismatch: Eerst inkoopgoedkeuring
6. Urgente facturen (gevlagd): Versnelde workflow

**Implementatie:**

```
STAP 1: Controleer op PO-mismatch
  ALS PO_Match_Status = "FAIL":
    → Routeer naar Inkoop voor PO-resolutie
    → Na resolutie, ga hieronder verder

STAP 2: Controleer Urgente Vlag
  ALS Urgent_Flag = TRUE:
    → Sla bedragcontroles over
    → Direct naar hoogste goedkeurder
    → Stel prioriteit = HOOG
    → Deadline van 1 dag

STAP 3: Op Bedrag Gebaseerde Routering (indien niet urgent)
  ALS Bedrag < €1.000:
    → Automatisch goedkeuren
    → Onmiddellijk exporteren

  ANDERS ALS Bedrag < €10.000:
    → Maak taak voor Manager
    → Prioriteit: Gemiddeld
    → Deadline: 3 dagen

  ANDERS ALS Bedrag ≥ €10.000:
    CONTROLEER Leveranciersstatus:
      ALS Leveranciersleeftijd < 180 dagen (Nieuw):
        → Maak taak voor Directeur (Taak 1)
        → Na goedkeuring, maak taak voor CFO (Taak 2)
        → Prioriteit: Hoog
        → Deadline: 2 dagen elk

      ANDERS (Bestaande Leverancier):
        → Maak taak voor alleen Directeur
        → Prioriteit: Hoog
        → Deadline: 2 dagen
```

---

## Stap-voor-Stap Implementatie

### Stap 1: Definieer Conditiekaarten

**Conditie 1: Bedragdrempel**
```
Kaart: CONDITION_DOC_FIELD_AMOUNT
Veld: Total_Amount
Operator: IS LESS THAN
Waarde: 1000
Valuta: EUR
```

**Conditie 2: Documenttypecontrole**
```
Kaart: CONDITION_DOC_TYPE_IS_ISNOT
Documenttype: IS
Type: Invoice
```

**Conditie 3: Leveranciersstatus**
```
Kaart: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Leveranciersstatus: IS
Status: ACTIVE
```

**Conditie 4: Nieuwe Leverancier Controle**
```
Kaart: CONDITION_DOC_FIELD_DATE
Veld: Supplier_First_Transaction_Date
Operator: IS AFTER
Waarde: {{TODAY_MINUS_180_DAYS}}
```

**Gidsreferentie:** [Conditiekaarten Complete Gids](../and/condition-cards-complete-guide.md)

---

### Stap 2: Bouw Beslissingsboom

**Niveau 1: Documenttype**
```
Workflow: "Factuurverwerking"

ALS Document_Type = "Factuur":
  → Ga door naar Niveau 2

ANDERS ALS Document_Type = "Creditnota":
  → Vertakken naar "Creditnota Verwerking"

ANDERS ALS Document_Type = "Bon":
  → Vertakken naar "Bon Verwerking"

ANDERS:
  → Routeer naar "Onbekend Documenttype" afhandeling
```

**Niveau 2: Bedragdrempels (voor Facturen)**
```
ALS Bedrag < €1.000:
  → Vertakken naar "Auto-Goedkeuring Pad"

ANDERS ALS Bedrag < €10.000:
  → Vertakken naar "Manager Goedkeuring Pad"

ANDERS ALS Bedrag < €50.000:
  → Vertakken naar "Directeur Goedkeuring Pad"
  → Controleer Niveau 3 condities

ANDERS (Bedrag ≥ €50.000):
  → Vertakken naar "Executive Goedkeuring Pad"
  → Dubbele of driedubbele goedkeuring vereist
```

**Niveau 3: Leveranciersanalyse (voor facturen met hoge waarde)**
```
ALS Leveranciersstatus = "GEBLOKKEERD":
  → STOP verwerking
  → Maak urgente escalatietaak
  → Meld inkoop en financiën

ANDERS ALS Leveranciersleeftijd < 180 dagen (Nieuw):
  → Extra goedkeuring vereist
  → Voeg CFO toe aan goedkeuringsketen
  → Verbeterde verificatie

ANDERS ALS Leveranciersrisicoscore = "HOOG":
  → Extra controles vereist
  → Fraudedetectiebeoordeling
  → Manager voorafgaande goedkeuring

ANDERS:
  → Standaard workflow hoge waarde
```

---

### Stap 3: Maak Routeringsacties

**Pad A: Auto-Goedkeuring (Bedrag < €1.000)**
```
Acties:
1. Stel veld "Approval_Type" = "AUTO"
2. Stel veld "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Exporteer naar ERP
5. Stuur bevestigingsmail (optioneel)
```

**Pad B: Manager Goedkeuring (€1.000-€10.000)**
```
Acties:
1. Stel veld "Approval_Type" = "MANUAL"
2. Stel veld "Approval_Level" = "1"
3. tasks_create:
   - Titel: "Keur Factuur {{DOCUMENT_NUMBER}} Goed"
   - Toewijzen aan: Afdelingsmanager
   - Prioriteit: Gemiddeld
   - Deadline: 3 dagen
4. Stuur e-mailmelding naar manager
5. Wacht op taakvoltooiing
6. Indien goedgekeurd: Exporteer naar ERP
7. Indien afgewezen: Retourneer naar leverancier
```

**Pad C: Directeur Goedkeuring (€10.000-€50.000)**
```
Acties:
1. Stel veld "Approval_Type" = "MANUAL"
2. Stel veld "Approval_Level" = "2"
3. Controleer Leveranciersleeftijd:
   ALS Nieuw (< 180 dagen):
     - Maak Taak 1: Goedkeuring Directeur
     - Na Taak 1: Maak Taak 2: Goedkeuring CFO
     - Dubbele goedkeuring vereist
   ANDERS:
     - Maak Taak: Alleen goedkeuring Directeur
4. Prioriteit: Hoog
5. Deadline: 2 dagen
6. Stuur e-mailmeldingen
7. Wacht op voltooiing
8. Als alles goedgekeurd: Exporteer
9. Als een afgewezen: Retourneer naar leverancier
```

**Pad D: Executive Goedkeuring (≥ €50.000)**
```
Acties:
1. Stel veld "Approval_Type" = "EXECUTIVE"
2. Stel veld "Approval_Level" = "3"
3. Sequentiële goedkeuringen:
   - Taak 1: Financieel Directeur
   - Taak 2: CFO
   - Taak 3: CEO (indien > €100.000)
4. Prioriteit: Urgent
5. Deadline: 1 dag elk
6. Stuur urgente meldingen
7. Update executive dashboard
8. Wacht op alle goedkeuringen
9. Als alles goedgekeurd: Exporteer
10. Als een afgewezen: Executive beoordelingsvergadering
```

---

## Geavanceerde Patronen voor Beslissingslogica

### Patroon 1: Op Score Gebaseerde Routering

**Bereken een risicoscore en routeer dienovereenkomstig:**

```
Risicoscoreberekening:
  Score = 0

  ALS Bedrag > €50.000: Score += 30
  ALS Leveranciersleeftijd < 180 dagen: Score += 25
  ALS PO_Variantie > 10%: Score += 20
  ALS Leveranciersland = "Hoog Risico Land": Score += 15
  ALS Betalingstermijnen < 30 dagen: Score += 10

  Totaal Scorebereik: 0-100

Routering:
  ALS Score < 20: Auto-goedkeuring
  ALS Score 20-50: Manager goedkeuring
  ALS Score 51-75: Directeur goedkeuring
  ALS Score > 75: Executive goedkeuring + fraudecontrole
```

**Implementatie:**
```
1. ACTION_CALCULATE_FIELD: Bereken risicoscore
2. ACTION_SET_FIELD_TO_NUMBER: Sla score op
3. CONDITION_DOC_FIELD_NUMBER: Controleer scoredrempels
4. Routeer op basis van score
```

---

### Patroon 2: Afdelingsmatrix

**Verschillende goedkeuringsregels per afdeling:**

```
Afdelingsmatrix:

  IT-afdeling:
    Bedrag < €5.000: IT-manager
    Bedrag ≥ €5.000: IT-directeur + CIO

  Financiële afdeling:
    Bedrag < €10.000: Financieel manager
    Bedrag ≥ €10.000: CFO

  Operationele afdeling:
    Bedrag < €3.000: Operationeel manager
    Bedrag ≥ €3.000: COO

  Algemeen:
    Bedrag < €2.000: Afdelingsmanager
    Bedrag ≥ €2.000: Afdelingsdirecteur
```

**Implementatie:**
```
1. Controleer veld Afdeling
2. Controleer bedragdrempel op basis van afdeling
3. Routeer naar juiste goedkeurder
4. Verschillende drempels per afdeling
```

---

### Patroon 3: Op Tijd Gebaseerde Logica

**Verschillende regels op basis van timing:**

**Maandeindverwerking (Laatste 3 dagen van de maand):**
```
  ALS Vandaag in laatste 3 dagen van maand:
    - Prioriteit: URGENT
    - Deadline: 1 dag
    - Goedkeurder: Dienstdoende financieel manager
    - Versnelde workflow
  ANDERS:
    - Standaard prioriteit
    - Standaard deadline
    - Standaard workflow
```

**Kantooruren vs Na Kantooruren:**
```
  ALS Tijd tussen 9.00 - 17.00 uur:
    - Toewijzen aan huidige dienst
  ANDERS:
    - Wachtrij voor volgende werkdag
    - OF routeer naar oproepbare goedkeurder
```

**Fiscaal Tijdvak:**
```
  ALS Documentdatum in Huidig Fiscaal Tijdvak:
    - Standaard verwerking
  ANDERS:
    - Markeer als "Vorig Tijdvak"
    - Vereis boekhoudkundige goedkeuring
    - Extra controles
```

---

### Patroon 4: Op Uitzondering Gebaseerde Routering

**Routeer uitzonderingen apart:**

```
Uitzonderingsdetectie:

  Geen Uitzondering:
    → Standaard workflow

  Kleine Uitzondering (Automatisch herstelbaar):
    → Automatisch corrigeren
    → Log correctie
    → Ga door met standaard workflow

  Gemiddelde Uitzondering (Vereist beoordeling):
    → Maak beoordelingstaak
    → Markeer document
    → Na correctie: Ga door met workflow

  Grote Uitzondering (Vereist escalatie):
    → Stop verwerking
    → Maak urgente taak
    → Meld meerdere niveaus
    → Handmatige tussenkomst vereist

Uitzonderingstypen:
  - Ontbrekend verplicht veld
  - Ongeldige veldwaarde
  - PO-mismatch
  - Dubbele factuur
  - Leveranciersmismatch
  - Bedragdiscrepantie
```

---

## Compleet Diagram Beslissingslogica

```
FACTUUR KOMT AAN
│
├─ NIVEAU 1: UITZONDERINGCONTROLE
│  │
│  ├─ Heeft Kritieke Uitzondering? (Ontbrekende PO, Duplicaat, etc.)
│  │  │
│  │  ├─ JA → Stop & Escaleer
│  │  │        Maak urgente taak
│  │  │        Meld admin
│  │  │        → EINDE (Uitzonderingsafhandeling)
│  │  │
│  │  └─ NEE → Ga door naar Niveau 2
│
├─ NIVEAU 2: DOCUMENTTYPE
│  │
│  ├─ Type = Factuur?
│  │  └─ JA → Ga door naar Niveau 3
│  │
│  ├─ Type = Creditnota?
│  │  └─ JA → Vertakken naar Creditnotaworkflow
│  │           → EINDE (Creditnota Pad)
│  │
│  └─ Ander Type?
│     └─ JA → Vertakken naar toepasselijke workflow
│              → EINDE (Ander Type Pad)
│
├─ NIVEAU 3: URGENTIECONTROLE (voor Facturen)
│  │
│  ├─ Urgente Vlag = TRUE?
│  │  │
│  │  ├─ JA → Versnelde Workflow
│  │  │        Prioriteit: URGENT
│  │  │        Deadline: 1 dag
│  │  │        Toewijzen aan: Senior Goedkeurder
│  │  │        → EINDE (Versneld Pad)
│  │  │
│  │  └─ NEE → Ga door naar Niveau 4
│
├─ NIVEAU 4: BEDRAGDREMPELS
│  │
│  ├─ Bedrag < €1.000?
│  │  │
│  │  ├─ JA → AUTO-GOEDKEURING PAD
│  │  │        Stel Approval_Type = "AUTO"
│  │  │        Keur onmiddellijk goed
│  │  │        Exporteer naar ERP
│  │  │        → EINDE (Auto-Goedgekeurd)
│  │  │
│  │  └─ NEE → Ga door
│  │
│  ├─ Bedrag < €10.000?
│  │  │
│  │  ├─ JA → MANAGER GOEDKEURING PAD
│  │  │        Maak taak voor Manager
│  │  │        Prioriteit: Gemiddeld
│  │  │        Deadline: 3 dagen
│  │  │        → WACHT op goedkeuring
│  │  │           → EINDE (Manager Pad)
│  │  │
│  │  └─ NEE → Ga door
│  │
│  ├─ Bedrag < €50.000?
│  │  │
│  │  ├─ JA → DIRECTEUR GOEDKEURING PAD
│  │  │        Ga door naar Niveau 5 (Leverancierscontrole)
│  │  │
│  │  └─ NEE → Ga door
│  │
│  └─ Bedrag ≥ €50.000?
│     │
│     └─ JA → EXECUTIVE GOEDKEURING PAD
│              Maak sequentiële taken:
│              - Financieel Directeur
│              - CFO
│              - CEO (indien > €100.000)
│              Prioriteit: URGENT
│              Deadline: 1 dag elk
│              → WACHT op alle goedkeuringen
│                 → EINDE (Executive Pad)
│
├─ NIVEAU 5: LEVERANCIERSANALYSE (voor bereik €10k-€50k)
│  │
│  ├─ Leveranciersstatus = "GEBLOKKEERD"?
│  │  │
│  │  ├─ JA → BLOKKEER & ESCALEER
│  │  │        Stop verwerking
│  │  │        Maak urgente taak
│  │  │        Meld inkoop & financiën
│  │  │        → EINDE (Geblokkeerde Leverancier)
│  │  │
│  │  └─ NEE → Ga door
│  │
│  ├─ Leveranciersleeftijd < 180 dagen (Nieuw)?
│  │  │
│  │  ├─ JA → DUBBELE GOEDKEURING VEREIST
│  │  │        Taak 1: Directeur (2 dagen)
│  │  │        → WACHT op Taak 1
│  │  │           ALS Taak 1 Goedgekeurd:
│  │  │             Taak 2: CFO (2 dagen)
│  │  │             → WACHT op Taak 2
│  │  │                → EINDE (Dubbel Goedgekeurd)
│  │  │           ALS Taak 1 Afgewezen:
│  │  │             → EINDE (Afgewezen op Niveau 1)
│  │  │
│  │  └─ NEE → Ga door
│  │
│  ├─ Leveranciersrisicoscore = "HOOG"?
│  │  │
│  │  ├─ JA → VERBETERDE GOEDKEURING
│  │  │        Extra fraudecontroles
│  │  │        Directeur goedkeuring vereist
│  │  │        Verlengde deadline
│  │  │        → EINDE (Verbeterd Pad)
│  │  │
│  │  └─ NEE → STANDAARD DIRECTEUR GOEDKEURING
│  │           Maak taak voor Directeur
│  │           Prioriteit: Hoog
│  │           Deadline: 2 dagen
│  │           → WACHT op goedkeuring
│  │              → EINDE (Standaard Hoge Waarde)
│  │
│  └─ [Leveranciersanalyse voltooid]
│
└─ [Alle beslissingsniveaus verwerkt]
```

---

## Configuratie Beste Praktijken

### 1. Houd Logica Duidelijk en Onderhoudbaar

✅ **Goed:**
```
ALS Bedrag > 10000:
  → Hoge waarde pad
ANDERS:
  → Standaard pad
```

❌ **Slecht (Te Complex):**
```
ALS (Bedrag > 10000 EN (Leverancier = "A" OF Leverancier = "B") EN NIET (Status = "X" OF Status = "Y") EN Afdeling IN [1,2,3]):
  → Complex pad
```

**Beter: Opsplitsen in stappen:**
```
Stap 1: ALS Bedrag > 10000: Ga door, ANDERS: Standaard pad
Stap 2: ALS Leverancier in toegestane lijst: Ga door, ANDERS: Beoordeling
Stap 3: ALS Status geldig: Ga door, ANDERS: Afwijzen
Stap 4: ALS Afdeling geautoriseerd: Goedkeuren, ANDERS: Escaleren
```

---

### 2. Documenteer Beslissingslogica

**Neem altijd op:**
- Doel van elk beslissingspunt
- Bedrijfsregel die wordt geïmplementeerd
- Verwachte uitkomsten
- Uitzonderingsafhandeling

**Voorbeeld Documentatie:**
```
Beslissingspunt: Bedragdrempelcontrole
Bedrijfsregel: BR-INV-001 (Factuurgoedkeuringsmatrix)
Doel: Routeer facturen op basis van bedragdrempels volgens bedrijfsbeleid
Drempels:
  < €1.000: Auto-goedkeuring (CFO goedgekeurde drempel)
  €1.000-€10.000: Manager goedkeuring (Delegatiematrix)
  > €10.000: Directeur goedkeuring (Handtekeningbevoegdheid)
Uitzonderingen: Urgente facturen slaan over naar hoogste niveau
Bijgewerkt: 23-10-2025
Eigenaar: Financiële Afdeling
```

---

### 3. Test Alle Paden

**Testmatrix:**

| Testgeval | Bedrag | Type | Leverancier | Verwacht Pad | Status |
|-----------|--------|------|----------|---------------|--------|
| TC1 | €500 | Factuur | Bestaand | Auto-goedkeuring | ✅ |
| TC2 | €5.000 | Factuur | Bestaand | Manager | ✅ |
| TC3 | €15.000 | Factuur | Nieuw | Directeur+CFO | ✅ |
| TC4 | €60.000 | Factuur | Bestaand | Executive | ✅ |
| TC5 | €2.000 | Creditnota | Bestaand | Creditworkflow | ✅ |
| TC6 | €100.000 | Factuur | Geblokkeerd | Stop & Escaleer | ✅ |

---

### 4. Monitor Beslissingsstatistieken

**Volgen:**
- Verdeling over beslissingspaden
- Auto-goedkeuringspercentage
- Handmatig beoordelingspercentage
- Gemiddelde verwerkingstijd per pad
- Uitzonderingspercentages
- Padgebruik

**Voorbeeld Statistieken:**
```
Maand: Oktober 2025
Totaal Facturen: 1.250

Verdeling Beslissingspaden:
- Auto-goedgekeurd (< €1k): 680 (54%)
- Manager pad (€1k-€10k): 420 (34%)
- Directeur pad (€10k-€50k): 120 (10%)
- Executive pad (> €50k): 30 (2%)

Verwerkingstijd:
- Auto-goedkeuring: < 1 minuut
- Manager pad: 2,5 dagen gemiddeld
- Directeur pad: 1,8 dagen gemiddeld
- Executive pad: 3,2 dagen gemiddeld

Uitzonderingen: 15 (1,2%)
```

---

## Gerelateerde Patronen

### Patronen Die Goed Samenwerken:

- **[Taakbeheer Patroon](task-management-pattern.md)** - Maak taken op basis van beslissingen
- **[API Integratie Patroon](api-integration-pattern.md)** - Haal gegevens op voor besluitvorming
- **[PO Matching Patroon](po-matching-pattern.md)** - Gebruik PO-resultaten in beslissingen
- **[Gegevenstransformatie Patroon](data-transformation-pattern.md)** - Transformeer gegevens vóór beslissingen

---

## Gerelateerde Gidsen

### Vereisten
- [Conditiekaarten Complete Gids](../and/condition-cards-complete-guide.md) - Alle conditiekaarten
- [Gids Veldmanipulatie](../then/document-field/field-manipulation-guide.md) - Veldoperaties
- [Toewijzingsgebruikersgids](../then/assignee/assignment-user-guide.md) - Routeringslogica

### Gerelateerde Kaarten
- **CONDITION_DOC_FIELD_AMOUNT** - [Gids Conditiekaarten](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** - [Gids Conditiekaarten](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** - [Gids Conditiekaarten](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** - [Toewijzingsgids](../then/assignee/assignment-user-guide.md)
- **tasks_create** - [Taaktoewijzingsgids](../then/task/task-assignment-guide.md)

### Volgende Stappen
- Maak taken: [Taakbeheer Patroon](task-management-pattern.md)
- Voeg complexe matching toe: [PO Matching Patroon](po-matching-pattern.md)
- Integreer API's: [API Integratie Patroon](api-integration-pattern.md)

---

**Patroonversie:** 1.0
**Laatst Bijgewerkt:** 23 oktober 2025
**Moeilijkheidsgraad:** Gemiddeld
**Geschatte Tijd:** 30-45 minuten
**Succespercentage:** Hoog
