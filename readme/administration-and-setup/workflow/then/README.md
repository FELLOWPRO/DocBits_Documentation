# Then

## Overzicht van "Then..."-actiekaarten

### **1. Document Field-acties:**

* **Invert Checkbox:** Deze actie wisselt de status van een selectievakjeveld in een document om.
* **Set Checkbox:** Hiermee wordt de status van een selectievakjeveld op true (aangevinkt) of false (niet aangevinkt) gezet.
* **Set Field to Text:** Deze actie stelt een opgegeven documentveld in op een bepaalde tekstwaarde.

<figure><img src="../../../.gitbook/assets/then1.png" alt=""><figcaption></figcaption></figure>

### **2. Document-acties:**

* **Approve the Document:** Markeert een document als goedgekeurd binnen het systeem.
* **Reject the Document:** Markeert een document als afgekeurd.

<figure><img src="../../../.gitbook/assets/image (259).png" alt=""><figcaption></figcaption></figure>

### **3. Export-acties:**

* **Export document with export configuration:** Start het exportproces met een specifieke exportconfiguratie.
* **Start Export:** Start het exportproces.



<figure><img src="../../../.gitbook/assets/image (260).png" alt=""><figcaption></figcaption></figure>

### **4. Status-acties:**



* **Change Status:** Wijzigt de status van een document of taak naar een opgegeven nieuwe status.

<figure><img src="../../../.gitbook/assets/then3.png" alt=""><figcaption></figcaption></figure>

### **5. Task-acties:**

* Toewijzingen en meldingen:
  * **Assign Task:** Maakt een taak aan en wijst deze met specifieke details toe aan een persoon of groep, met de optie om hen via e-mail op de hoogte te stellen.
  * **Create a New Task:** Vergelijkbaar met toewijzen, maar gericht op het opzetten van een volledig nieuwe taak binnen het systeem.

<figure><img src="../../../.gitbook/assets/then4.png" alt=""><figcaption></figcaption></figure>

### **6. Table-acties:**

* **Calculate in Table:** Voert berekeningen uit op tabelgegevens op basis van opgegeven voorwaarden en slaat de resultaten op in een aangewezen kolom.
* **Change Entries:** Werkt vermeldingen in een tabel bij op basis van opgegeven voorwaarden.

<figure><img src="../../../.gitbook/assets/then5.png" alt=""><figcaption></figcaption></figure>

### **7. Assignee-acties:**

* **Assign User from Field:** Wijst een gebruiker toe aan een taak of document op basis van gebruikersgegevens die in een specifiek veld zijn opgeslagen, met een optie voor een terugvalgebruiker als de primaire gebruiker niet beschikbaar is.
* **Assign Document to User or Group:** Wijst een document rechtstreeks toe aan een gebruiker of groep, zodat de verantwoordelijkheid op de juiste manier wordt belegd.

<figure><img src="../../../.gitbook/assets/then6.png" alt=""><figcaption></figcaption></figure>

### **8. Externe-interactie-acties:**

* **Call API:** Verzendt een verzoek naar een externe API, dat kan worden aangepast met specifieke methoden, parameters en gegevens.
* **Send HTTPS Request:** Vergelijkbaar met API-aanroepen, maar specifiek opgemaakt voor HTTPS-protocollen.

<figure><img src="../../../.gitbook/assets/then7.png" alt=""><figcaption></figcaption></figure>

### **9. Geavanceerde verwerking:**

* **Run Workflow:** Triggert een andere workflow binnen het systeem, waardoor complexe procesketens mogelijk zijn.

#### Praktische toepassing

Deze actiekaarten worden gebruikt om reacties te automatiseren op basis van specifieke triggers die in de eerdere delen van de workflowconfiguratie zijn vastgesteld. Bijvoorbeeld:

* Als een document wordt geïdentificeerd als beoordeling vereisend, kan de actie "Approve the Document" automatisch worden getriggerd zodra het aan alle opgegeven voorwaarden voldoet.
* Voor gegevensbeheertaken zorgen de acties "Set Checkbox" of "Set Field to Text" ervoor dat documentvelden automatisch worden bijgewerkt, wat handmatige gegevensinvoer en de kans op fouten vermindert.
* Complexe taken zoals API-interacties of statuswijzigingen stroomlijnen interacties niet alleen binnen het ERP-systeem, maar ook met externe diensten en tools, wat de integratie en functionaliteit verbetert.

### Conclusie

Het "Then..."-gedeelte in uw workflowsysteem biedt krachtige hulpmiddelen om precieze acties te definiëren die moeten plaatsvinden wanneer aan voorwaarden in de workflow is voldaan. Door deze acties effectief te gebruiken, kunnen bedrijven routineprocessen automatiseren, de gegevensnauwkeurigheid waarborgen en dynamisch reageren op veranderende informatie en systeemtoestanden. Begrijpen hoe u deze acties configureert en gebruikt, is essentieel om de efficiëntie en effectiviteit van de workflowmogelijkheden van uw ERP-systeem te maximaliseren.
