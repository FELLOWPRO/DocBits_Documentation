# Assign a Task with Title

<figure><img src="../../../../.gitbook/assets/image (291).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

De workflow-kaart "Assign Task / Notification from Decision Table" is ontworpen om taken of meldingen dynamisch toe te wijzen op basis van de resultaten van een decision table. Deze kaart zorgt ervoor dat taken of meldingen aan de juiste gebruiker of groep worden toegewezen volgens de logica die in de decision table is gedefinieerd, met een optionele e-mailmelding die naar de ontvanger wordt verzonden.

## **Onderdelen van de kaart:**

1. **Title**
   * **Beschrijving**: Geeft de titel op van de taak of melding die wordt aangemaakt.
   * **Detail**: De titel moet context bieden en het doel van de taak of melding beschrijven.
2. **Description**
   * **Beschrijving**: Definieert de inhoud of het doel van de taak of melding.
   * **Detail**: Biedt aanvullende informatie over de taak of melding en legt de context of de vereiste actie uit.
3. **Priority**
   * **Beschrijving**: Definieert het urgentieniveau van de taak of melding.
   * **Opties**:
     * **High**: Taken of meldingen die onmiddellijke aandacht vereisen.
     * **Medium**: Belangrijke taken die snel moeten worden afgehandeld.
     * **Low**: Taken die op een later tijdstip kunnen worden afgehandeld.
4. **Assignee Type**
   * **Beschrijving**: Geeft de gebruiker of groep op die op basis van de uitvoer van de decision table aan de taak of melding wordt toegewezen.
   * **Detail**: De decision table evalueert dynamisch de voorwaarden en retourneert de juiste gebruiker of groep voor toewijzing.
5. **Email Notification**
   * **Beschrijving**: Configureert of er een e-mailmelding naar de toegewezen gebruiker of groep wordt verzonden.
   * **Opties**:
     * **True**: Verzendt een e-mailmelding naar de ontvanger.
     * **False**: Er wordt geen e-mailmelding verzonden.

#### **Aanvullende onderdelen in Version 3**

1. **Notification Type**
   * **Beschrijving**: Geeft op of de kaart een taak of een melding aanmaakt.
   * **Opties**:
     * **Task**: Maakt een taak aan die wordt toegewezen aan de gebruiker of groep uit de decision table.
     * **Notification**: Verzendt een melding naar de gebruiker of groep uit de decision table.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**\
  De kaart voert de actie alleen uit als zowel de **"Where"**- als de **"And"**-secties als true worden geëvalueerd.
* **Taak-/meldingstoewijzing**\
  De kaart wijst de taak of melding toe aan de gebruiker of groep die door de decision table wordt geïdentificeerd. De decision table evalueert dynamisch vooraf gedefinieerde voorwaarden en retourneert de bijbehorende ontvanger.
* **E-mailmelding**\
  Indien zo geconfigureerd, wordt er een e-mailmelding naar de toegewezen gebruiker of groep verzonden.
* **Version 3-functionaliteit**\
  In Version 3 maakt de kaart het aanmaken van ofwel een Task ofwel een Notification mogelijk, wat meer flexibiliteit biedt voor taakbeheer en communicatie.

## **Opzet en configuratie:**

1. **Taak- of meldingsdetails definiëren**:\
   Voer de titel, beschrijving en prioriteit voor de taak of melding in.
2. **Decision table configureren**:\
   Stel de decision table in om dynamisch te bepalen welke gebruiker of groep de taak of melding krijgt toegewezen.
3. **E-mailmelding inschakelen**:\
   Geef op of er een e-mailmelding naar de toegewezen gebruiker of groep moet worden verzonden.
4. **Notification Type opgeven (Version 3)**:\
   Kies of de kaart een taak aanmaakt of een melding verzendt.

## **Conclusie:**

De workflow-kaart **"Assign Task / Notification from Decision Table"** automatiseert de toewijzing van taken of meldingen op basis van dynamische voorwaarden die in een decision table zijn gedefinieerd. Version 3 verbetert de functionaliteit door gebruikers te laten kiezen tussen het aanmaken van een taak of een melding, en zorgt ervoor dat altijd de juiste ontvanger wordt toegewezen. De e-mailmeldingsfunctie houdt gebruikers op de hoogte, wat de communicatie en het taakbeheer stroomlijnt.
