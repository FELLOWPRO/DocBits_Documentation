# Set to

<figure><img src="../../../../.gitbook/assets/image (278).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om een opgegeven veld in het document automatisch op een vooraf gedefinieerde tekstwaarde in te stellen op basis van de voorwaarden die zijn gedefinieerd in de **"Where"**- en **"And"**-secties. Hiermee kunnen gebruikers de gegevensinvoer stroomlijnen door ervoor te zorgen dat velden met consistente waarden worden gevuld wanneer aan bepaalde criteria wordt voldaan.

## **Onderdelen van de kaart:**

1. **Field Name**
   * **Beschrijving**: Geeft het veld op dat met de tekstwaarde wordt bijgewerkt.&#x20;
   * **Detail**: Het geselecteerde veld wordt bijgewerkt met de opgegeven tekstwaarde als aan de voorwaarden in de **"Where"**- en **"And"**-secties wordt voldaan.
2. **Text**
   * **Beschrijving**: Definieert de tekstwaarde die in het doelveld wordt ingesteld wanneer de voorwaarden als true worden geëvalueerd.
   * **Detail**: Dit kan een aangepast bericht, een status of een vooraf gedefinieerde waarde zijn die de gebruiker in het veld wil schrijven. De tekst moet overeenkomen met het verwachte invoerformaat van het veld (bijv. alfanumeriek, datum of andere soorten tekstuele informatie).

## **Functionaliteit:**

* **Voorwaarde-evaluatie**: Het systeem evalueert de voorwaarden in de **"Where"**- en **"And"**-secties:
  * Als **beide voorwaarden true zijn**, worden de in de **"Then"**-sectie gedefinieerde acties uitgevoerd. Specifiek wordt het doelveld (Field Name) gevuld met de opgegeven tekst.
  * Als **de "Where"- of de "And"-sectie false is**, wordt er geen actie ondernomen en blijft het veld ongewijzigd. De acties van de **Then**-sectie worden volledig overgeslagen als een van beide voorwaarden false is.
* **Actie-uitvoering**: Als aan beide voorwaarden in de **"Where"**- en **"And"**-secties wordt voldaan, vult het systeem automatisch het opgegeven veld met de gekozen tekstwaarde. Als niet aan de voorwaarden wordt voldaan, worden er geen wijzigingen aan het veld aangebracht.

## **Opzet en configuratie:**

Om deze kaart op te zetten:

1. **Selecteer het veld** (Field Name) dat met de tekstwaarde wordt bijgewerkt. De beschikbare velden in het document worden weergegeven om uit te selecteren.
2. **Geef de tekstwaarde op** die in het doelveld wordt geschreven wanneer de voorwaarden true zijn.
3. De actie wordt alleen uitgevoerd als zowel de **"Where"**- als de **"And"**-voorwaarden als true worden geëvalueerd.

## **Conclusie:**

De workflow-kaart **"Set Field to Text"** biedt een eenvoudige manier om het vullen van tekstwaarden in specifieke documentvelden te automatiseren op basis van vooraf gedefinieerde voorwaarden. Dit vermindert handmatige gegevensinvoer en zorgt voor consistentie in de documentverwerking, waardoor het een nuttig hulpmiddel is voor het automatiseren van workflows en het verbeteren van de efficiëntie.
