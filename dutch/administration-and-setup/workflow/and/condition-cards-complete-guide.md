# Conditiekaarten - Volledige gids

## Conditiekaarten - Volledige gids

De voorwaardekaarten op deze pagina horen in de **Wanneer**- en **En**-groep van de Workflow Builder — ze bepalen of de Then-acties worden uitgevoerd. Voor het gebruik van het canvas — **Kaart toevoegen**, **Workflow opslaan**, **Sjabloon opslaan** — zie de [gids Standaard workflow](../README.md):

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-nl.png" alt="Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface."><figcaption><p>Niet-opgeslagen voorbeeld met Wanneer-, En- en Dan-kaarten. Vul alle velden in vóór uitvoering. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

**Omslagen:** 31 resterende conditiekaarten

***

### 📌 Versie-informatie

**Status:** De meeste voorwaardekaarten zijn stabiel met structuren in één of dubbele versie **Versiepatroon:** De meeste volgen v1 → v2-patroon (met toevoeging van i18n-ondersteuning) **Voorbeeld van meerdere versies:** CONDITION\_DECISION\_TREE\_DATA (v2-v3)

**Opmerking:** Sommige voorwaardekaarten voor PO-vergelijking hebben meerdere versies. Gebruik deze gids voor het huidige gedrag en de release-opmerkingen hieronder voor gepubliceerde wijzigingen.

📖 [Release-opmerkingen van het product](../../../overview-and-basics/release-notes) | [PO Matching Gids](compare-with-purchase-order/po-matching-complete-guide.md)

***

## Documentstatus- en statusvoorwaarden

### Kaart: CONDITION\_DOC\_STATUS\_IS\_ISNOT / Documentstatuscontrole

#### Doel

Controleert of het document een specifieke status heeft

#### Wanneer te gebruiken

* Voordat u het goedkeurt
* In een specifieke workflowfase
* Statusgebaseerde routering

#### Documentstatustypen

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

#### Hoe het werkt

```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

#### Voorbeeld

```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

#### Parameters

```
Operator: IS / IS NOT
Status: [Select status]
```

***

### Kaart: CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST

#### Doel

Controleert of de status overeenkomt met een status in een lijst

#### Wanneer te gebruiken

* Meerdere geldige statussen
* OF-logica voor status

#### Voorbeeld

```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

***

### Kaart: CONDITION\_DOC\_TYPE\_IS\_ISNOT / Documenttypecontrole

#### Doel

Controleert of het document van een specifiek type is

#### Documenttypen

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

#### Hoe het werkt

```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

#### Voorbeeld

```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

***

### Kaart: CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST

#### Doel

Controleert of het type overeenkomt met een van de typen in de lijst

#### Voorbeeld

```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

***

### Kaart: CONDITION\_SUB\_ORG\_IS\_ISNOT / Suborganisatiecontrole

#### Doel

Controleert welke organisatie/afdeling eigenaar is van het document

#### Organisaties

```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

#### Voorbeeld

```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

***

### Kaart: CONDITION\_PURCHASE\_ORDER\_IMPORT / PO-importcontrole

#### Doel

Controleert of de inkooporder nieuw geïmporteerd of bestaand is

#### Hoe het werkt

```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

#### Wanneer te gebruiken

* Verschillende afhandeling voor nieuwe inkooporders
* Sla validatie voor bekende inkooporders over
* Volg de eerste keer dat u de leverancier ziet

***

## Voorwaarden voor de verantwoordelijke

### Kaart: CONDITION\_USER\_IS\_ISNOT / Gebruikerscontrole

#### Doel

Controleert of het document aan een specifieke gebruiker is toegewezen

#### Hoe het werkt

```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

#### Voorbeeld

```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

***

### Kaart: CONDITION\_USER\_IS\_ISNOT\_IN\_LIST

#### Doel

Controleert of deze is toegewezen aan een gebruiker in de lijst

#### Voorbeeld

```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

***

### Kaart: CONDITION\_GROUP\_IS\_ISNOT / Groepscontrole

#### Doel

Controleert of toegewezen is aan een specifieke groep

#### Voorbeeld

```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

***

### Kaart: CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST

#### Doel

Controleert of toegewezen is aan een groep in de lijst

#### Voorbeeld

```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

***

## Datum- en tijdvoorwaarden

### Kaart: CONDITION\_TIME\_IS\_ISNOT\_BETWEEN / Datumbereikcontrole

#### Doel

Controleert of de datum tussen twee datums valt

#### Hoe het werkt

```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

#### Berekening

```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

#### Wanneer te gebruiken

* Controleer of het in de fiscale periode is
* Controleer of het binnen de deadline is
* Controleer of het in de promotieperiode is

#### Voorbeeld

```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

#### Parameters

```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

***

### Kaart: CONDITION\_TODAY\_IS\_ISNOT / Vandaagcontrole

#### Doel

Controleert of de datum van vandaag overeenkomt met de criteria

#### Hoe het werkt

```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

#### Gebruiksscenario's

```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

#### Voorbeeld

```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

***

### Kaart: CONDITION\_CONFIRMED\_DELIVERY\_ACCEPTED\_DATE\_IN\_CALENDAR\_MASTER\_DATA

#### Doel

Controleert of de leverdatum overeenkomt met de goedgekeurde leverdata in de kalender

#### Hoe het werkt

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

#### Wanneer te gebruiken

* Controleer of de levering overeenkomt met de afgesproken data
* Controleer met de vakantiekalender
* Valideer op gecontracteerde datums

#### Voorbeeld

```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

***

## Logische omstandigheden

### Kaart: CONDITION\_DECISION\_TREE\_DATA / Beslissingstabelresultaten

#### Doel

Controleert of de beslissingstabel retourwaarden bevat

#### Hoe het werkt

```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

#### Wanneer te gebruiken

* Voordat u de resultaten van de beslissingstabel gebruikt
* Als poortvoorwaarde
* Om te controleren of routing beschikbaar is

#### Voorbeeld

```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

***

### Kaart: CONDITION\_CONTINUE\_CHANCE / Willekeurige waarschijnlijkheid

#### Doel

Gaat verder met gespecificeerde waarschijnlijkheid

#### Hoe het werkt

```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

#### Wanneer te gebruiken

* A/B-testworkflows
* Bemonsteringsdocumenten
* Willekeurige kwaliteitscontroles

#### Voorbeeld

```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

#### Berekening

```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

***

### Kaart: CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE / Functiecontrole

#### Doel

Controleert of een specifieke module/functie is ingeschakeld

#### Modules

```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

#### Hoe het werkt

```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

#### Wanneer te gebruiken

* Functie-afhankelijke workflows
* Optionele verwerking
* Controleer of de gelicentieerde functie actief is

***

### Kaart: CONDITION\_HTTPS\_REQUEST\_STATUS / Resultaatcontrole aanvragen

#### Doel

Controleert of het HTTPS-verzoek succesvol was

#### Statuscodes

```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

#### Hoe het werkt

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

#### Voorbeeld

```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

***

### Kaart: CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT / Controle leveranciersstatus

#### Doel

Controleert de status van de leverancier in het systeem

#### Leveranciersstatussen

```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

#### Hoe het werkt

```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

#### Voorbeeld

```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

***

### Kaart: CONDITION\_SPECIFY\_SUPPLIER\_TYPE

#### Doel

Specificeert/controleert het leverancierstype

#### Soorten leveranciers

```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

#### Hoe het werkt

```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

***

## Voorbeeld van beslissingsstromen

### Stroom 1: Op status gebaseerde verwerking

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

### Stroom 2: Op leveranciers gebaseerde verwerking

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

### Stroom 3: Op bedrag gebaseerd met datumcontrole

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

## Conditiekaartvergelijking

| Kaart                                        | Checks          | Exploitant      | Use               |
| ------------------------------------------- | --------------- | ------------- | ----------------- |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT           | Document status | IS / IS NIET   | Stage check       |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST | Status in list  | IN / NIET IN   | Meerdere statussen |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT             | Document type   | IS / IS NIET   | Type filtering    |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST       | Type in list    | IN / NIET IN   | Multiple types    |
| CONDITION\_SUB\_ORG\_IS\_ISNOT              | Organisatie    | IS / IS NIET   | Afdelingscontrole  |
| CONDITION\_USER\_IS\_ISNOT                  | Toegewezen gebruiker   | IS / IS NIET   | User check        |
| CONDITION\_USER\_IS\_ISNOT\_IN\_LIST        | User in list    | IN / NIET IN   | Meerdere gebruikers    |
| CONDITION\_GROUP\_IS\_ISNOT                 | Toegewezen groep  | IS / IS NIET   | Group check       |
| CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST       | Group in list   | IN / NIET IN   | Meerdere groepen   |
| CONDITION\_TIME\_IS\_ISNOT\_BETWEEN         | Date range      | TUSSEN       | Datumvenster       |
| CONDITION\_TODAY\_IS\_ISNOT                 | De datum van vandaag    | IS / IS NIET   | Vandaag controle       |
| CONDITION\_DECISION\_TREE\_DATA             | DT keert terug      | HEEFT / HEEFT NIET | DT result check   |
| CONDITION\_CONTINUE\_CHANCE                 | Waarschijnlijkheid     | CHANCE        | Random gate       |
| CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE        | Functie ingeschakeld | IS / IS NIET   | Functiecontrole     |
| CONDITION\_HTTPS\_REQUEST\_STATUS           | Request result  | STATUS        | Response check    |
| CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT      | Supplier status | IS / IS NIET   | Supplier check    |

***

## Beste praktijken voor omstandigheden

✅ **Doe:**

* Gebruik specifieke voorwaarden
* Testlogica met voorbeelden
* Bestel voorwaarden logisch
* Zorg voor terugval voor alle paden
* Documenteer complexe logica

❌ **Niet doen:**

* Creëer circulaire voorwaarden (A als B, B als A)
* Maak de omstandigheden te complex
* Vergeet randgevallen
* Stel dat veld altijd waarde heeft
* Creëer onmogelijke omstandigheden

***

## Meerdere voorwaarden combineren

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

## Gerelateerde kaarten

* **CONDITION\_DOC\_FIELD\_CONTAINS** - Controle van veldinhoud
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - Veldvergelijking
* **CONDITION\_CHECKBOX\_IS** - Selectievakje controleren

<!-- workflow-card-complete-example-20261021 condition_purchase_order_import -->

### Voorbeeld van importtrigger voor inkooporders

**Configuratie:** Selecteer onder Wanneer de importgebeurtenis voor nieuwe inkooporders (`wf_new_purchase_order`) en laat de updategebeurtenis (`wf_updated_purchase_order`) ongeselecteerd. Configureer vervolgacties voor deze documentonafhankelijke workflowcontext.

**Verwacht resultaat en tegenvoorbeeld:** Een run die wordt geactiveerd door een nieuw geïmporteerde inkooporder, voldoet aan deze voorwaarde. Een run die alleen door een update wordt geactiveerd, doet dat niet. Als u beide gebeurtenissen selecteert, zijn beide gebeurtenissen mogelijk. Hiermee wordt de triggerinformatie van de workflow gecontroleerd, niet of een factuur momenteel een inkoopordernummer bevat.

Dit is een illustratieve testconfiguratie en verwachte uitkomst; het werd niet uitgevoerd. Gebruik gegevens en ontvangers die in uw testorganisatie zijn geconfigureerd.

<!-- workflow-card-complete-example-20261021 condition_supplier_status_is_isnot -->

### Voorbeeld van een trigger voor een statuswijziging van een leverancier

**Configuratie:** Kies onder Wanneer operator `is` en één doelstatus die daadwerkelijk in uw organisatie wordt aangeboden. Noem die geselecteerde status in dit voorbeeld A. Laat een andere beschikbare status B ongeselecteerd.

**Verwacht resultaat en tegenvoorbeeld:** De voorwaarde is waar voor een statusveranderingsgebeurtenis van een leverancier waarvan de nieuwe status A is; het is onwaar voor een gebeurtenis waarvan de nieuwe status B is. Met operator `is not` zijn deze resultaten omgekeerd. Dit is een gebeurtenistrigger op basis van informatie over de workflowrun, en niet een algemene controle van de leveranciersstatus op een factuur. Bevestig de feitelijke gebeurtenis en de geselecteerde status in het logboek.

Dit is een illustratieve testconfiguratie en verwachte uitkomst; het werd niet uitgevoerd. Gebruik gegevens en ontvangers die in uw testorganisatie zijn geconfigureerd.
