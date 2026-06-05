# Workflow Documentatie

**Workflow Documentatie**

Om het overzicht te bewaren, kunt u de workflows verschillende koppen geven, zodat u meteen weet waarover deze workflow gaat.

Maak een nieuwe Workflow aan: Klik op + WORKFLOW TOEVOEGEN

![](<../../.gitbook/assets/workflow_add_button.png>)

U kunt deze workflows (Test 1, 2, 3) gebruiken om verschillende documenten automatisch toe te wijzen aan de juiste medewerker in het bedrijf.

![](<../../.gitbook/assets/workflow_list_overview.png>)

Als een factuur of ander document een bepaald totaalbedrag overschrijdt dat voorafgaande beoordeling en goedkeuring vereist, kunnen deze documenten onmiddellijk aan de juiste persoon worden toegewezen.

<figure><img src="../../.gitbook/assets/workflow_amount_check.png" alt="Workflow Amount Check"><figcaption></figcaption></figure>

**Test 1: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Invoice

Then: **Assign document to:** Stefan Reppermund

![](<../../.gitbook/assets/3 (1).png>)

**Test 2: Logic Card**

When: **Assignee is:** Amier Haider

And: **Document type is:** Delivery Note

Then: **Assign document to:** James Edwards

![](<../../.gitbook/assets/4 (1).png>)

**Test 3: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** **Document type is:** Order Confirmation

**Then:** **Assign document to:** Anian Sollinger

![](<../../.gitbook/assets/5 (1).png>)

Het is ook mogelijk om, als het document niet aan één enkele persoon is toegewezen, het vanaf het begin aan een specifieke medewerker toe te wijzen.

<figure><img src="../../.gitbook/assets/workflow_assign_to_employee_start.png" alt="Workflow Assign to Employee Start" width="375"><figcaption></figcaption></figure>

Voor een eenvoudiger overzicht van wat er met een document moet gebeuren, kunt u de status voor binnenkomende documenten in deze workflow instellen. Met deze workflow kunt u meteen zien of er bijvoorbeeld een goedkeuring in behandeling is.

**Test 4: Logic Card**

**When:** **Document type is:** Delivery Note

**And:** **Assignee is:** Amier Haider

**Then:** **Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test4_delivery_note_status.png" alt="Workflow Test 4 Delivery Note Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/8 (1).png>)

**Test 5: Logic Card**

When: **Document type is:** Invoice

And: **Assignee is:** Stefan Reppermund

Then: **Change Status to:** Pending Second Approval

<figure><img src="../../.gitbook/assets/workflow_test5_invoice_approval_status.png" alt="Workflow Test 5 Invoice Approval Status"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/10 (1).png>)

Als een factuur of ander document een bepaald totaalbedrag overschrijdt dat voorafgaande beoordeling en goedkeuring vereist, kunnen deze documenten onmiddellijk aan de juiste persoon worden toegewezen.

![](<../../.gitbook/assets/11 (1).png>)

**Test 6: Logic Card**

When: **Assignee is:** Amier Haider

And: Docfield **total\_amount** is **Greater than 500**

Then: **Assign document to:** Asad Usman Khan

<figure><img src="../../.gitbook/assets/workflow_test6_total_amount_assign.png" alt="Workflow Test 6 Total Amount Assign"><figcaption></figcaption></figure>

![](<../../.gitbook/assets/13 (1).png>)

Het is ook mogelijk om de status in de workflow in te voeren, zodat de toegewezen persoon meteen kan zien welke status dit document heeft en wat er vervolgens mee moet gebeuren.

**Test 7: Logic Card**

**When:** **Assignee is:** Amier Haider

**And:** Docfield **total\_amount** is **Greater then 500**

**Then:** **Assign document to:** Asad Usman Khan

**Change Status to:** Pending Approval

<figure><img src="../../.gitbook/assets/workflow_test7_status_update.png" alt="Workflow Test 7 Status Update"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/15 (1).png" alt=""><figcaption></figcaption></figure>

Als er bijvoorbeeld bepaalde of belangrijke informatie in een document ontbreekt die echter belangrijk is en voor verdere verwerking moet worden opgenomen, kunt u de workflow zo instellen dat deze documenten onmiddellijk worden doorgestuurd naar de inkoper en een vervanger.

<figure><img src="../../.gitbook/assets/workflow_test8_missing_info.png" alt="Workflow Test 8 Missing Info"><figcaption></figcaption></figure>

**Test 9:**

De Workflow met deze logic cards is ontworpen om automatisch te verifiëren dat de hoeveelheid, eenheidsprijs of korting die in een orderbevestiging is vermeld, overeenkomt met de bijbehorende cijfers in de inkooporder. Deze verificatie waarborgt consistentie en nauwkeurigheid tussen wat er is besteld en wat de leverancier bevestigt te leveren.

U kunt deze documenten een specifieke status geven of ze aan een specifieke medewerker toewijzen.

<div align="center"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="Workflow Test 9 Match Check Overview"><figcaption></figcaption></figure></div>

<figure><img src="../../.gitbook/assets/workflow_test9_match_check_detail.png" alt="Workflow Test 9 Match Check Detail"><figcaption></figcaption></figure>

**Logic Card: Quantity or Unit Price or Discount Match**

Deze logic card is ontworpen om automatisch te verifiëren dat de hoeveelheid, eenheidsprijs of korting die in een orderbevestiging is vermeld, overeenkomt met de bijbehorende cijfers in de inkooporder. Deze verificatie waarborgt consistentie en nauwkeurigheid tussen wat er is besteld en wat de leverancier bevestigt te leveren.

**Trigger Condition**

De logica wordt geactiveerd wanneer aan een van de volgende voorwaarden wordt voldaan in een orderbevestiging ten opzichte van de oorspronkelijke inkooporder:

* **Quantity**: De bestelde hoeveelheid items komt overeen met de door de leverancier bevestigde hoeveelheid.
* **Unit Price**: De overeengekomen prijs per item komt overeen met de bevestiging van de leverancier.
* **Discount**: Eventuele toegepaste kortingen zijn consistent tussen de inkooporder en de orderbevestiging.
* **Define Comparison Parameters**: Stel de specifieke velden (hoeveelheid, eenheidsprijs, korting) in die de logic card op een overeenkomst zal controleren.
* **Automate Verification**: Configureer het systeem om deze gegevens automatisch te vergelijken bij ontvangst van een orderbevestiging.
* **Customize Alerts**: Bepaal de workflow voor het afhandelen van discrepanties, inclusief het aanpassen van waarschuwingen voor handmatige beoordeling.

Deze logic card is essentieel om ervoor te zorgen dat de gegevens van een orderbevestiging overeenkomen met de oorspronkelijke inkooporder, waardoor de integriteit van de inkoopcyclus wordt gewaarborgd.

**Test 10:**

Als u een andere berekening voor toeslagen heeft, of deze slechts op sommige items van toepassing zijn, kunt u de generieke tabelberekeningskaarten gebruiken; sommige daarvan staan ook toe om te filteren op reguliere expressies.

<figure><img src="../../.gitbook/assets/19 (1).png" alt=""><figcaption></figcaption></figure>

Hierboven staat een berekeningsvoorbeeld voor MTZ met een filter voor artikelnummers die beginnen met 01, 06, 9, 001 of 000.

Bij een handmatige opzet wordt geadviseerd om berekeningen die afhankelijk zijn van nieuwe kolommen in een aparte workflow te splitsen. Om met de berekening door te gaan, kunt u de Run Workflow-kaart gebruiken.

**Run Workflow**

<figure><img src="../../.gitbook/assets/20 (1).png" alt=""><figcaption></figcaption></figure>

Met deze kaart kunt u de naam opgeven van een workflow die na de huidige workflow moet worden uitgevoerd als aan de voorwaarden ervan is voldaan en na voorgaande then-kaarten van de huidige workflow. Hoewel uitvoerbare, actieve workflows worden geprioriteerd, kunt u er ook gedeactiveerde workflows mee uitvoeren als het document aan de voorwaarden van de workflows voldoet.

### **Adding calculated surcharges into an existing column** <a href="#pekg4i18rshn" id="pekg4i18rshn"></a>

<figure><img src="https://lh7-us.googleusercontent.com/XYY1xsFpp7_-Bi0WOSbotiVzspDLdaufx_xgoopMHmxdZnSDhroLpb0AE_si5PhwMq1jHfndc9FwOte9MOoCoTP5_JUYawO5cr4uIctIDHmwVjz3KacQrLJd8iBQy5KY4N-dMaWEi3IeTcc5OBRNJk4" alt=""><figcaption></figcaption></figure>

Als u alle toeslagen als een negatieve korting in de kortingskolom wilt opnemen, kunt u de berekeningskaart gebruiken. Mogelijk staan er al gegevens in deze kolom; u kunt deze instellen als een van de variabelen op de kaart, de MTZ ervan laten aftrekken en het resultaat weer aan deze kolom toevoegen. Mocht er sprake zijn van lege velden (toeslagen slechts voor sommige items), dan gaat het voor de berekening uit van een 0.

**Notify user to authorize the order confirmation in DocBits**

Nadat u de toeslagen heeft berekend, wilt u mogelijk een specifieke gebruiker informeren om de orderbevestiging te autoriseren. Hiervoor kunt u de meldingskaart gebruiken.

<figure><img src="../../.gitbook/assets/workflow_notification_card_overview.png" alt="Workflow Notification Card"><figcaption></figcaption></figure>

Afhankelijk van de instellingen krijgt de gebruiker een nieuwe taak in DocBits toegewezen en optioneel een e-mail om hen op de hoogte te stellen van hun nieuwe taak.
