# Assign Document and Create Task/Notification for Group

<figure><img src="../../../../.gitbook/assets/image (12) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel**

De workflow-kaart "**Assign Document and Create Task/Notification for Group**" wijst een document toe aan een opgegeven groep, maakt een taak of melding aan met aanpasbare details en verzendt optioneel een e-mailmelding naar de groep. Deze kaart ondersteunt ook het toewijzen van een numerieke prioriteitswaarde om de uitvoeringsvolgorde te bepalen.

## **Onderdelen van de kaart**

1. **Group Name**
   * **Beschrijving:** Geeft de groep op die de taak of melding ontvangt.
   * **Detail:** Een dropdown om de naam te kiezen van de groep waaraan het document en de taak/melding worden toegewezen.
2. **Task/Notification**
   * **Beschrijving:** Geeft het type actie op dat voor de groep wordt aangemaakt.
   * **Detail:** Een dropdown om ofwel "Task" ofwel "Notification" te selecteren op basis van de gewenste actie.
3. **Title**
   * **Beschrijving:** Biedt de titel van de taak of melding.
   * **Detail:** Een veld om een beknopte, beschrijvende titel voor de taak of melding toe te voegen.
4. **Description**
   * **Beschrijving:** Beschrijft de taak of melding verder.
   * **Detail:** Een veld om aanvullende details over het doel van de taak of de inhoud van de melding te bieden.
5. **Priority**
   * **Beschrijving:** Definieert het urgentieniveau van de taak of melding.
   * **Opties:**
     * **High:** Vereist onmiddellijke aandacht.
     * **Medium:** Belangrijk maar niet urgent.
     * **Low:** Kan later worden afgehandeld.
6. **Send Mail**
   * **Beschrijving:** Configureert of er een e-mailmelding naar de groep wordt verzonden.
   * **Opties:**
     * **True:** Verzendt een e-mailmelding.
     * **False:** Verzendt geen e-mail.
7. **Value**
   * **Beschrijving:** Stelt de numerieke prioriteit voor de documenttoewijzing in.
   * **Detail:** Een veld om een numerieke waarde in te voeren, waarbij een lager getal een hogere prioriteit aangeeft.

## **Functionaliteit**

* **Voorwaarde-evaluatie:**\
  De kaart voert de acties alleen uit als aan de geconfigureerde workflow-voorwaarden wordt voldaan.
* **Documenttoewijzing en aanmaak van taak/melding:**\
  Het document wordt toegewezen aan de groep die in het veld "Group Name" is opgegeven. Er wordt een taak of melding aangemaakt met de geconfigureerde titel, beschrijving en prioriteitsniveau.
* **E-mailmelding:**\
  Als "Send Mail" op True is ingesteld, wordt er een e-mailmelding naar de groep verzonden om hen op de hoogte te stellen van de taak of melding.

## **Opzet en configuratie**

1. **Group Name definiëren:**
   * Voer de naam van de groep in het veld Group Name in.
2. **Task/Notification selecteren:**
   * Kies "Task" of "Notification" in de Task/Notification-dropdown.
3. **Taak-/meldingsdetails instellen:**
   * Voer de Title en Description voor de taak of melding in.
   * Selecteer de Priority in de dropdown (High, Medium of Low).
4. **E-mailmelding inschakelen:**
   * Configureer de optie Send Mail op True of False, afhankelijk van of er een e-mailmelding moet worden verzonden.
5. **Numerieke prioriteit toewijzen:**
   * Voer een numerieke waarde in het veld Value in om de prioriteit van de toewijzing te bepalen, waarbij lagere waarden voorrang krijgen.
6. Sla de kaartconfiguratie op en activeer de workflow.

## **Conclusie**

De workflow-kaart "Assign Document and Create Task/Notification for Group" zorgt ervoor dat documenten aan de juiste groep worden toegewezen, terwijl taken of meldingen worden aangemaakt met aanpasbare prioriteits- en e-mailmeldingsopties. Dit stroomlijnt het documentbeheer en verbetert de workflow-efficiëntie.
