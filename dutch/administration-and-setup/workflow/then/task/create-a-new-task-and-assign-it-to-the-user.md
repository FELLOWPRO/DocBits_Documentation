# Create a New Task and assign it to the User

<figure><img src="../../../../.gitbook/assets/image (287).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel**

De workflow-kaart **"Create Task or Notification"** stroomlijnt taakbeheer en meldingen binnen workflows. Afhankelijk van de versie kan de kaart taken aanmaken, meldingen verzenden en aanvullende functionaliteit benutten, zoals beslisbomen voor dynamische verwerking.

## **Onderdelen van de kaart**

1. **Title**
   * **Beschrijving**: Definieert de titel van de taak of melding die wordt aangemaakt.
   * **Detail**: De titel biedt een duidelijke en beknopte identifier voor de taak of melding.
2. **Description**
   * **Beschrijving**: Biedt details over de taak of melding.
   * **Detail**: Helpt het doel of de context van de taak of melding voor de toegewezen gebruiker te verduidelijken.
3. **Priority**
   * **Beschrijving**: Stelt het urgentieniveau voor de taak in.
   * **Opties**:
     * **High**: Vereist onmiddellijke aandacht.
     * **Medium**: Belangrijk maar niet urgent.
     * **Low**: Kan later worden afgehandeld.
4. **Assigned User**
   1. **Beschrijving**: Geeft de gebruiker op aan wie de taak wordt toegewezen.
   2. **Detail**: Gebruikers worden geselecteerd uit een dropdownlijst van beschikbaar personeel.
5. **Email Notification**
   * **Beschrijving**: Bepaalt of de toegewezen gebruiker een e-mailmelding ontvangt.
   * **Opties**:
     * **True**: Verzendt een e-mailmelding naar de gebruiker.
     * **False**: Er wordt geen e-mailmelding verzonden.

## Aanvullende onderdelen **in Version 3 en Version 4**

1. **Decision Tree (alleen Version 3)**
   * **Beschrijving**: Maakt het gebruik van een beslisboom voor dynamische taakaanmaak mogelijk.
   * **Opties**:
     * **True**: Activeert verwerking via de beslisboom.
     * **False**: Schakelt verwerking via de beslisboom uit.
2. **Task or Notification (alleen Version 4)**
   * **Beschrijving**: Maakt de selectie mogelijk tussen het aanmaken van een taak of een melding.
   * **Opties**:
     * **Task**: Maakt een taak aan.
     * **Notification**: Maakt een melding aan in plaats van een taak.

## **Functionaliteit:**

* **Voorwaarde-evaluatie**:\
  Deze kaart wordt alleen getriggerd als aan de voorwaarden in de **"Where"**- en **"And"**-secties wordt voldaan.
* **Aanmaak van taak of melding**:
  * Versions 2 en 3: Er wordt een taak aangemaakt met de opgegeven titel, beschrijving, prioriteit en toegewezen gebruiker.
  * Version 4: Maakt het aanmaken van ofwel een taak ofwel een melding mogelijk.
* **Dynamische toewijzing**:
  * In Version 3 bepaalt de beslisboom dynamisch de gebruiker aan wie de taak wordt toegewezen op basis van workflow-parameters.
* **E-mailmelding**:\
  Verzendt een e-mail naar de toegewezen gebruiker als de meldingsoptie is ingeschakeld.

## **Opzet en configuratie:**

1. **Versie selecteren**: Kies de versie van de kaart op basis van de vereiste functionaliteit:
   * Version 2: Basistaakaanmaak met handmatige gebruikerstoewijzing en e-mailmeldingen.
   * Version 3: Bevat beslisboomfunctionaliteit voor dynamische gebruikerstoewijzing.
   * Version 4: Voegt de mogelijkheid toe om een melding aan te maken in plaats van een taak.
2. **Taakdetails invoeren**: Geef de titel, beschrijving en prioriteit van de taak of melding op.
3. **Gebruiker toewijzen**:
   * Voor Versions 2 en 4: selecteer handmatig een gebruiker uit de dropdownlijst.
   * Voor Version 3: schakel de beslisboom in om de toegewezen gebruiker dynamisch te bepalen.
4. **E-mailmelding inschakelen**: Geef op of de toegewezen gebruiker een e-mailmelding moet ontvangen.
5. (Voor Version 4) **Taak of melding kiezen**: Geef aan of er een taak of melding moet worden aangemaakt.

## **Conclusie:**

De workflow-kaart **"Create Task or Notification"** is een veelzijdig hulpmiddel voor het beheren van taken en meldingen. Door dynamische gebruikerstoewijzing via beslisbomen te ondersteunen en opties voor het aanmaken van taken of meldingen te bieden, verbetert hij de aanpasbaarheid van de workflow en de efficiëntie van de samenwerking.
