# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Doel:

De workflow-kaart **"AI Calculation for Cost Increase Surcharges"** gebruikt AI om automatisch toeslagbedragen te berekenen op basis van kostenstijgingen. Hij zorgt voor consistente en nauwkeurige toeslagberekeningen, stroomlijnt workflows en vermindert handmatige inspanning.

## Onderdelen van de kaart:

* **Cost Increase Factor**
  * **Beschrijving:** De vermenigvuldigingsfactor of het percentage dat op de basiskosten wordt toegepast om de toeslag te berekenen.
  * **Detail:** Bepaalt het toeslagbedrag op basis van de kostenstijging (bijv. een factor van 1,10 voor een stijging van 10%).
* **Base Cost Field**
  * **Beschrijving:** Het veld dat de oorspronkelijke kostenwaarde bevat die als basis voor de toeslagberekening wordt gebruikt.
  * **Detail:** Wordt automatisch geselecteerd of binnen de workflow gedefinieerd ter referentie tijdens de berekening.
* **Surcharge Field**
  * **Beschrijving:** Het veld waarin de door AI berekende toeslagwaarde wordt opgeslagen.
  * **Detail:** Dit veld geeft de berekende toeslag weer en maakt deze beschikbaar voor verdere verwerking of rapportage.

## Functionaliteit:

**Voorwaarde-evaluatie:**

* De kaart wordt alleen geactiveerd als zowel de **"Where"**- als de **"And"**-voorwaarden als true worden geëvalueerd.
* Als een van beide voorwaarden als false wordt geëvalueerd, wordt er geen toeslagberekening uitgevoerd.

**AI-gestuurde berekening:**

* Het systeem past de **Cost Increase Factor** toe op het **Base Cost Field** om de toeslag te berekenen.
* Het resultaat wordt opgeslagen in het **Surcharge Field**, zodat het toegankelijk is voor volgende workflow-stappen.

## Conclusie:

De workflow-kaart **"AI Calculation for Cost Increase Surcharges"** automatiseert het toepassen van toeslagen op basis van kostenstijgingen. Door AI te benutten voor precisie en consistentie elimineert deze kaart handmatige berekeningen, verbetert hij de efficiëntie en ondersteunt hij nauwkeurig kostenbeheer in geautomatiseerde workflows.
