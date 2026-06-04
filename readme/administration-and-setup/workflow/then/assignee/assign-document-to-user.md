# Assign document to User

<figure><img src="../../../../.gitbook/assets/image (300).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Met de workflow-kaart **"Assign Document to User"** kunnen gebruikers een document aan een specifieke gebruiker toewijzen, wat zorgt voor soepel workflowbeheer door documenten naar de juiste persoon te routeren. Version 3 voegt de mogelijkheid toe om een beslisboom te gebruiken om de gebruikerstoewijzing dynamisch te bepalen op basis van beschikbare voorwaarden.

## **Onderdelen van de kaart:**

1. **User**
   * **Beschrijving:** Geeft de gebruiker op aan wie het document wordt toegewezen.
   * **Detail:** Er wordt een dropdownlijst van alle beschikbare gebruikers geboden om uit te selecteren. De geselecteerde gebruiker krijgt het document toegewezen voor verdere actie.

## **Aanvullende onderdelen in Version 3:**

1. **Use Decision Tree**
   * **Beschrijving:** Indien ingeschakeld, gebruikt de kaart een beslisboom om de gebruikerstoewijzing dynamisch te bepalen.
   * **Opties:**
     * **True:** Gebruikt de beslisboom voor dynamische gebruikerstoewijzing.
     * **False:** Wijst het document toe aan de geselecteerde gebruiker zonder de beslisboom te gebruiken.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**\
  De kaart voert de actie alleen uit als zowel de **"Where"**- als de **"And"**-secties als true worden geëvalueerd.
* **Documenttoewijzing:**\
  De kaart wijst het document toe aan de geselecteerde gebruiker, zodat de taak naar de juiste persoon wordt gerouteerd voor actie. Dit helpt bij verantwoording en effectief documentbeheer.
* **Beslisboom (Version 3):**\
  Als de beslisboom is ingeschakeld, evalueert de kaart de binnen de boom gedefinieerde voorwaarden om de gebruiker voor documenttoewijzing dynamisch te selecteren.

## **Opzet en configuratie:**

* **Gebruiker selecteren:**\
  Kies de **gebruiker** uit de dropdownlijst aan wie het document wordt toegewezen.
* **Beslisboom gebruiken (Version 3):**\
  Schakel het gebruik van de beslisboom in of uit om de gebruiker dynamisch te selecteren.

## **Conclusie:**

De workflow-kaart **"Assign Document to User"** faciliteert efficiënte documentroutering door deze aan de geselecteerde gebruiker toe te wijzen, met de toegevoegde flexibiliteit in Version 3 om de gebruiker dynamisch te bepalen met een beslisboom. Dit zorgt voor een aanpasbaarder en efficiënter workflowproces.
