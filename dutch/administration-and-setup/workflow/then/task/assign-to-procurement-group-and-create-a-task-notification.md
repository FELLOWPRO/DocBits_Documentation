# Assign to Procurement Group and Create a Task/Notification

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel**

De workflow-kaart "**Assign Document to Procurement Group and Create Task/Notification**" wijst een document toe aan een opgegeven inkoopgroep, maakt een taak of melding aan met gedefinieerde details en stelt de groep optioneel via e-mail op de hoogte. Hij prioriteert de taakuitvoering op basis van een configureerbare numerieke prioriteitswaarde.

## **Onderdelen van de kaart**

1. **Group Name**
   * **Beschrijving:** Geeft de inkoopgroep op die verantwoordelijk is voor het afhandelen van het document.
   * **Detail:** Een veld waarin de gebruiker handmatig de naam van de inkoopgroep kan invoeren.
2. **Task/Notification**
   * **Beschrijving:** Definieert of er een taak of melding voor de groep wordt aangemaakt.
   * **Detail:** Een veld waarin de gebruiker kan kiezen tussen het aanmaken van een taak of een melding
3. **Title**
   * **Beschrijving:** De titel van de taak of melding die voor de groep wordt aangemaakt.
   * **Detail:** Een veld om een beknopte en herkenbare titel voor de taak of melding te bieden.
4. **Description**
   * **Beschrijving:** Verdere details over de taak of melding.
   * **Detail:** Een veld om het doel van de taak te beschrijven en context of instructies te bieden.
5. **Priority**
   * **Beschrijving:** Definieert het urgentieniveau van de taak of melding.
   * **Opties:**
     * **High:** Taak vereist onmiddellijke aandacht.
     * **Medium:** Taak is belangrijk maar niet urgent.
     * **Low:** Taak kan op een later tijdstip worden afgehandeld.
6. **Send Mail**
   * **Beschrijving:** Configureert of er een e-mailmelding naar de groep moet worden verzonden.
   * **Opties:**
     * **True:** Verzendt een e-mailmelding naar de inkoopgroep.
     * **False:** Er wordt geen e-mailmelding verzonden.
7. **Value**
   * **Beschrijving:** Stelt de numerieke prioriteit voor de taakuitvoering in.
   * **Detail:** Een veld om een numerieke waarde in te voeren, waarbij een lager getal een hogere prioriteit vertegenwoordigt.

## **Functionaliteit**

* **Voorwaarde-evaluatie:**\
  De kaart voert de acties alleen uit als aan de gedefinieerde workflow-voorwaarden wordt voldaan.
* **Groepstoewijzing en aanmaak van taak/melding:**\
  Het document wordt toegewezen aan de opgegeven inkoopgroep. Er wordt een taak of melding aangemaakt met de opgegeven titel, beschrijving en prioriteit.
* **E-mailmelding:**\
  Als "Send Mail" op True is ingesteld, ontvangt de groep een e-mail over de taak of melding.

## **Opzet en configuratie**

1. **Group Name definiëren:**
   * Voer de naam van de inkoopgroep in het veld Group Name in.
2. **Taak-/meldingsdetails configureren:**
   * Geef de Title en Description voor de taak of melding op.
   * Selecteer de Priority in het dropdownmenu (High, Medium of Low).
3. **E-mailmelding inschakelen:**
   * Stel "Send Mail" in op True of False, afhankelijk van of de groep een e-mail moet ontvangen.
4. **Numerieke prioriteit instellen:**
   * Voer een numerieke waarde in het veld Value in om de prioriteit van de taak te bepalen, waarbij lagere waarden het eerst worden verwerkt.
5. Sla de kaartconfiguratie op en activeer de workflow.

## **Conclusie**

De workflow-kaart "Assign Document to Procurement Group and Create Task/Notification" zorgt ervoor dat documenten naar de juiste groep worden geleid met duidelijke taakinstructies en prioriteitsniveaus. Door optionele e-mailmeldingen mogelijk te maken, verbetert deze kaart de zichtbaarheid van taken en zorgt hij voor een soepele workflow-uitvoering.
