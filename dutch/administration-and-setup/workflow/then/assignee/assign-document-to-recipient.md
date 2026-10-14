# Assign document to recipient

<figure><img src="../../../../.gitbook/assets/image (301).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

De workflow-kaart **"Assign Document to Disponent / Purchaser"** wijst een document toe aan een **Disponent** of **Purchaser**. Als er geen geldige gebruiker wordt gevonden, wordt een terugvalgebruiker geselecteerd om ervoor te zorgen dat het document altijd aan iemand wordt toegewezen.

## **Onderdelen van de kaart:**

1. **Disponent / Purchaser**
   * **Beschrijving:** Geeft op of het document aan een Disponent of Purchaser wordt toegewezen.
   * **Opties:**
     * **Disponent:** Wijs het document toe aan de Disponent.
     * **Purchaser:** Wijs het document toe aan de Purchaser.
2. **Fallback User**
   * **Beschrijving:** Geeft een terugvalgebruiker op voor het geval het document niet aan de geselecteerde Disponent of Purchaser kan worden toegewezen.
   * **Detail:** Met de dropdownlijst van beschikbare gebruikers kunt u een terugvalgebruiker kiezen om ervoor te zorgen dat het document wordt toegewezen, zelfs als de primaire gebruiker niet kan worden bepaald.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**\
  De kaart voert de actie alleen uit als zowel de **"Where"**- als de **"And"**-secties als true worden geëvalueerd.
* **Documenttoewijzing:**\
  De kaart wijst het document toe aan de **Disponent** of **Purchaser** zoals geselecteerd. Als de geselecteerde persoon niet beschikbaar of niet geldig is, wordt het document aan de terugvalgebruiker toegewezen.

## **Opzet en configuratie:**

* **Disponent / Purchaser selecteren:**\
  Kies of het document aan de **Disponent** of **Purchaser** wordt toegewezen.
* **Terugvalgebruiker selecteren:**\
  Kies een terugvalgebruiker uit de dropdownlijst die het document ontvangt als de primaire toewijzing niet mogelijk is.

## **Conclusie:**

De workflow-kaart **"Assign Document to Disponent / Purchaser"** zorgt ervoor dat het document altijd wordt toegewezen, ofwel aan de geselecteerde Disponent/Purchaser, ofwel, indien nodig, aan de terugvalgebruiker. Dit minimaliseert verstoringen in de workflow en zorgt ervoor dat de documentverwerking soepel doorgaat.
