# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

De workflow-kaart **"Create Task with Fallback"** zorgt voor efficiënte taakdelegatie door taken toe te wijzen aan specifieke rollen — disponent of purchaser — terwijl een terugvalmechanisme wordt geïntegreerd om mislukte taaktoewijzingen te voorkomen. Deze kaart verbetert de betrouwbaarheid en aanpasbaarheid van de workflow in dynamische scenario's.

## **Onderdelen van de kaart:**

1. **Title**
   * **Beschrijving**: Geeft de titel van de taak die wordt aangemaakt op.
   * **Detail**: Biedt een beknopte identifier voor de taak.
2. **Description**
   * **Beschrijving**: Beschrijft het doel of de context van de taak.
   * **Detail**: Verduidelijkt de details van de taak.
3. **Priority**
   * **Beschrijving**: Stelt het urgentieniveau voor de taak in.
   * **Opties**:
     * **High**: Vereist onmiddellijke aandacht.
     * **Medium**: Belangrijk maar niet urgent.
     * **Low**: Kan later worden afgehandeld.
4. **Assigned Role**
   * **Beschrijving**: Geeft de primaire rol op aan wie de taak wordt toegewezen.
   * **Opties**:
     * **Disponent**: Wijst de taak toe aan de disponent.
     * **Purchaser**: Wijst de taak toe aan de purchaser.
5. **Email Notification**
   * **Beschrijving**: Maakt het mogelijk de toegewezen gebruiker via e-mail op de hoogte te stellen.
   * **Opties**:
     * **True**: Verzendt een e-mailmelding naar de gebruiker.
     * **False**: Er wordt geen e-mailmelding verzonden.
6. **Fallback User**
   * **Beschrijving**: Biedt een terugvaloptie voor taaktoewijzing als de ontvangerrol niet wordt gevonden.
   * **Detail**: Maakt het mogelijk een gebruiker uit een dropdownlijst te selecteren om de taakdelegatie te waarborgen.

## **Functionaliteit:**

* **Voorwaarde-evaluatie**:\
  De kaart wordt alleen uitgevoerd als aan de voorwaarden in de **"Where"**- en **"And"**-secties wordt voldaan.
* **Taaktoewijzing**:
  * De taak wordt toegewezen aan de geselecteerde rol (disponent of purchaser).
  * Als de opgegeven rol niet wordt gevonden, wordt de taak toegewezen aan een gebruiker uit de terugval-dropdownlijst.
* **E-mailmelding**:\
  Verzendt een e-mail naar de toegewezen gebruiker als e-mailmelding is ingeschakeld.

## **Opzet en configuratie:**

1. **Taakdetails opgeven**: Voer de titel, beschrijving en prioriteit van de taak in.
2. **Primaire rol selecteren**: Kies de rol aan wie de taak wordt toegewezen (disponent of purchaser).
3. **Terugvalgebruiker configureren**: Selecteer een terugvalgebruiker uit de dropdownlijst om de taaktoewijzing te waarborgen als de primaire rol niet wordt gevonden.
4. **E-mailmelding inschakelen**: Geef aan of de toegewezen gebruiker een e-mailmelding moet ontvangen.

## **Conclusie:**

De workflow-kaart **"Create Task with Fallback"** zorgt voor een naadloze taakdelegatie door een terugvalmechanisme te integreren. Door taken op basis van rollen toe te wijzen en een alternatieve gebruikersoptie te bieden, verbetert hij de betrouwbaarheid en flexibiliteit in taakbeheerprocessen.
