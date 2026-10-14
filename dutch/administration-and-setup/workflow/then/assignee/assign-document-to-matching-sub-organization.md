# Assign document to matching sub organization

<figure><img src="../../../../.gitbook/assets/image (303).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

De workflow-kaart **"Assign Document to Matching Sub-Organization Based on Field"** wijst een document dynamisch toe aan een suborganisatie, op basis van een opgegeven veld in het document. Als er geen overeenkomende suborganisatie wordt gevonden, gebruikt de kaart een vooraf gedefinieerde terugval-suborganisatie.

## **Onderdelen van de kaart:**

1. **Field Name**
   * **Beschrijving:** Geeft het documentveld op dat wordt gebruikt om de overeenkomende suborganisatie te bepalen.
   * **Detail:** De kaart zoekt naar een waarde in het opgegeven veld om deze te matchen met een beschikbare suborganisatie.
2. **Sub-Organization (Fallback)**
   * **Beschrijving:** Definieert de terugval-suborganisatie die wordt gebruikt als er geen match in het opgegeven veld wordt gevonden.
   * **Detail:** Als de veldwaarde met geen enkele suborganisatie overeenkomt, wordt het document toegewezen aan de geselecteerde terugval-suborganisatie.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:**\
  De kaart voert de actie alleen uit als zowel de **"Where"**- als de **"And"**-secties als true worden geëvalueerd.
* **Dynamische toewijzing:**\
  De kaart controleert de waarde van het opgegeven veld en wijst het document toe aan de suborganisatie die met deze waarde overeenkomt.
* **Terugvalmechanisme:**\
  Als er geen overeenkomende suborganisatie wordt gevonden, wordt het document toegewezen aan de terugval-suborganisatie.

## **Opzet en configuratie:**

* **Field Name selecteren:**\
  Kies het veld uit het document dat de waarde bevat om te matchen met een suborganisatie.
* **Terugval-suborganisatie selecteren:**\
  Kies de suborganisatie die wordt gebruikt als er geen match in het documentveld wordt gevonden.

## **Conclusie:**

De workflow-kaart **"Assign Document to Matching Sub-Organization Based on Field"** biedt flexibiliteit door documenten dynamisch naar de juiste suborganisatie te routeren, met een toegevoegde terugvaloptie om ervoor te zorgen dat geen enkel document niet-toegewezen blijft.
