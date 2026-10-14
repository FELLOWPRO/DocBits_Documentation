# Call Api

<figure><img src="../../../../.gitbook/assets/image (310).png" alt="" width="563"><figcaption></figcaption></figure>

## Doel:

Met de workflow-kaart **"Call API"** kunnen gebruikers rechtstreeks vanuit de workflow HTTP-verzoeken naar opgegeven API-eindpunten doen. Deze kaart ondersteunt diverse HTTP-methoden en maakt dynamische interactie met externe systemen mogelijk door parameters en gegevens te verzenden. Hij stroomlijnt de integratie met diensten van derden en aangepaste API's en zorgt voor naadloze communicatie.

## Onderdelen van de kaart:

1. **API Endpoint**
   * **Beschrijving:** De URL van de aan te roepen API.
   * **Detail:** Een tekstveld waarin gebruikers het eindpunt voor het API-verzoek opgeven.
2. **HTTP Method**
   * **Beschrijving:** Het type HTTP-verzoek dat wordt gedaan.
   * **Opties:**
     1. **GET:** Haalt gegevens op van het opgegeven eindpunt.
     2. **POST:** Verzendt gegevens naar het eindpunt.
     3. **PUT:** Werkt bestaande gegevens op het eindpunt bij.
     4. **DELETE:** Verwijdert gegevens op het eindpunt.
3. **Parameters**
   * **Beschrijving:** Queryparameters die in het API-verzoek worden opgenomen.
   * **Detail:** Een tekstveld of lijst voor het invoeren van sleutel-waardeparen voor de verzoek-URL.
4. **Data**
   1. **Beschrijving:** De payload die in de body van het API-verzoek wordt verzonden (van toepassing voor POST- en PUT-methoden).
   2. **Detail:** Een veld voor het invoeren van de gegevens in JSON of andere gestructureerde formaten.

## Functionaliteit:

**Voorwaarde-evaluatie:** Het systeem evalueert de voorwaarden die zijn gedefinieerd in de "Where"- en "And"-secties:

* Als beide voorwaarden **true** zijn, wordt het API-verzoek uitgevoerd zoals geconfigureerd.
* Als een van beide voorwaarden **false** is, wordt de kaart niet uitgevoerd en wordt er geen API-aanroep gedaan.

**API-verzoekuitvoering:**

* De kaart verzendt het HTTP-verzoek naar het opgegeven eindpunt met de geselecteerde methode.
* Eventueel opgegeven parameters worden aan de URL toegevoegd en de gegevens worden in de verzoekbody opgenomen (indien van toepassing).

## Opzet en configuratie:

1. **API-eindpunt definiëren:**\
   Voer de URL in van de API die u wilt aanroepen.
2. **HTTP-methode selecteren:**\
   Kies een van de ondersteunde methoden (GET, POST, PUT, DELETE) op basis van de vereisten van uw API.
3. **Parameters opgeven:**\
   Voeg eventueel vereiste queryparameters toe als sleutel-waardeparen.
4. **Gegevens opnemen (indien van toepassing):**\
   Geef voor POST- of PUT-methoden de gegevens op die in de verzoekbody worden verzonden.
5. **Voorwaardeconfiguratie:**\
   Configureer de "Where"- en "And"-secties om te definiëren wanneer de API-aanroep moet plaatsvinden.

## Conclusie:

De workflow-kaart **"Call API"** verbetert de workflow-automatisering door directe interactie met externe systemen mogelijk te maken. Door flexibele configuraties voor eindpunten, methoden en gegevens te bieden, zorgt hij ervoor dat workflows naadloos kunnen integreren met API's van derden of aangepaste backends. De mogelijkheid om API-aanroepen voorwaardelijk uit te voeren, zorgt voor precisie en efficiëntie bij het automatiseren van externe communicatie.

***
