# Assign user from field

<figure><img src="../../../../.gitbook/assets/image (299).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

De workflow-kaart **"Assign User from Field with Fallback"** wijst dynamisch een gebruiker toe op basis van de waarde die in een opgegeven documentveld wordt gevonden. Als het veld geen geldige gebruiker bevat, wordt een terugvalgebruiker geselecteerd uit een vooraf gedefinieerde lijst van beschikbare gebruikers om ervoor te zorgen dat de taak of actie op de juiste manier wordt toegewezen.

## **Onderdelen van de kaart:**

1. **Field Name**
   * **Beschrijving:** Geeft het **documentveld** op dat de toe te wijzen gebruikersinformatie bevat.
   * **Detail:** Dit veld wordt geëvalueerd om te bepalen welke gebruiker moet worden toegewezen. Als het veld een geldige gebruiker bevat, krijgt die gebruiker de taak toegewezen. Als het veld leeg of ongeldig is, wordt de terugvalgebruiker toegewezen.
2. **User (Fallback)**
   * **Beschrijving:** Geeft de **terugvalgebruiker** op die wordt toegewezen als het documentveld geen geldige gebruiker bevat.
   * **Detail:** Er wordt een dropdownlijst van alle beschikbare gebruikers geboden om uit te selecteren. Deze gebruiker wordt toegewezen als het documentveld leeg is of geen geldige gebruiker bevat.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**\
  De kaart voert de actie alleen uit als zowel de **"Where"**- als de **"And"**-secties als true worden geëvalueerd.
* **Veldgebaseerde gebruikerstoewijzing:**\
  De kaart probeert eerst de taak of actie toe te wijzen aan de gebruiker die in het **Field Name** is geïdentificeerd.
* **Terugvalgebruikertoewijzing:**\
  Als het veld geen geldige gebruiker bevat (of leeg is), wijst de kaart de taak toe aan de terugvalgebruiker die in de **User (Fallback)**-dropdownlijst is geselecteerd.

## **Opzet en configuratie:**

* **Field Name selecteren:**\
  Kies het **documentveld** dat de gebruiker voor toewijzing opgeeft.
* **Terugvalgebruiker selecteren:**\
  Kies de **terugvalgebruiker** uit de dropdownlijst. Deze gebruiker krijgt de taak toegewezen als het documentveld geen geldige gebruiker bevat.

## **Conclusie:**

De workflow-kaart **"Assign User from Field with Fallback"** zorgt ervoor dat een taak of actie altijd aan een geldige gebruiker wordt toegewezen. Als de gebruiker in het documentveld niet beschikbaar is, wordt automatisch de terugvalgebruiker toegewezen, wat flexibiliteit biedt en de voltooiing van de taak waarborgt.
