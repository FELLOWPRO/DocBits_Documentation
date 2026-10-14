# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze DocBits-kaart is ontworpen om de interactie met externe systemen te faciliteren door HTTPS-verzoeken naar opgegeven URL's te verzenden. Hij maakt het mogelijk dat workflows acties uitvoeren zoals het ophalen, bijwerken of verwijderen van gegevens door API-aanroepen te doen, wat zorgt voor naadloze integratie met externe diensten.

## **Functionaliteit:**

* **HTTPS-verzoekuitvoering:** De kaart verzendt een verzoek naar een opgegeven URL met behulp van de geconfigureerde HTTP-methode (bijv. GET, POST, PUT, DELETE).
* **Headers en parameters:** Gebruikers kunnen aangepaste headers en queryparameters opnemen om ervoor te zorgen dat het verzoek voldoet aan de vereisten van de externe API.
* **Verzoekgegevens:** Maakt het mogelijk dat gebruikers de gegevens-payload (indien van toepassing) definiëren die met het verzoek wordt verzonden, zoals JSON of formuliergecodeerde gegevens.
* **Responsevaluatie:** De workflow controleert of de ontvangen statuscode overeenkomt met de verwachte waarde, wat zorgt voor succesvolle communicatie voordat er wordt verdergegaan.
* **Ondersteunde HTTP-methoden:**
  * GET: Haalt gegevens op van de opgegeven URL.
  * POST: Verzendt gegevens naar de opgegeven URL om resources te maken.
  * PUT: Werkt bestaande resources op de opgegeven URL bij.
  * DELETE: Verwijdert resources van de opgegeven URL.

## **Gebruik:**

Deze kaart is met name nuttig in scenario's waarin workflows moeten communiceren met externe API's voor gegevensuitwisseling, zoals het verzenden van updates naar een CRM, het ophalen van orderstatussen of het plaatsen van nieuwe vermeldingen in een database.

## **Voorbeeldscenario:**

* Een gebruiker configureert de kaart om een POST-verzoek te verzenden naar een extern orderbeheersysteem met een payload die nieuwe orderdetails bevat. Aangepaste headers worden toegevoegd om API-authenticatietokens op te nemen. De kaart is ingesteld om alleen verder te gaan als de responsstatuscode 201 (Created) is. Als de statuscode anders is, triggert de workflow een foutmelding voor handmatige interventie.

Door de kaart "Send HTTPS Request" te gebruiken, kunnen organisaties externe integraties automatiseren, de communicatie tussen systemen verbeteren en complexe workflows stroomlijnen.
