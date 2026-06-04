# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Doel:

Deze DocBits-kaart is ontworpen om een specifiek orderdataveld — zoals hoeveelheid, korting of eenheidsprijs — te vergelijken tussen een orderbevestiging en een inkooporder. Door een gerichte vergelijking van één veld tegelijk toe te staan, zorgt hij voor precisie bij het valideren van belangrijke datapunten en het handhaven van de ordernauwkeurigheid. **Version 4** breidt deze functionaliteit uit door vergelijkingen mogelijk te maken tussen verschillende entiteiten zoals de inkooporder, de ontvangen hoeveelheden en het document zelf, wat meer flexibiliteit en controle aan de workflow toevoegt.

## Onderdelen van de kaart:

1. **Any/All**&#x20;
   * **Beschrijving:** Bepaalt of de voorwaarde van toepassing is op elke of alle regels in de orderbevestiging.\
     **Opties:**
     * **Any**: De vergelijking wordt getriggerd als de geselecteerde veldwaarde in een willekeurige regel van de orderbevestiging overeenkomt met de bijbehorende waarde in de inkooporder.
     * **All**: De vergelijking wordt alleen getriggerd als de geselecteerde veldwaarde in alle regels van de orderbevestiging overeenkomt met de bijbehorende waarde in de inkooporder.
2. **Order Data Field**
   * **Beschrijving**: Geeft het dataveld op dat tussen de orderbevestiging en de inkooporder wordt vergeleken.
   * **Detail**: Gebruikers kunnen een van de volgende velden voor vergelijking selecteren:
     * **Quantity**: Vergelijkt de bestelde hoeveelheid met de bevestigde hoeveelheid.
     * **Discount**: Valideert dat de korting in de bevestiging overeenkomt met de inkooporder.
     * **Unit Price**: Zorgt ervoor dat de eenheidsprijs in de bevestiging overeenkomt met de inkooporder.
3. **Operator**
   * **Beschrijving**: Definieert de voorwaarde die op de vergelijking van het geselecteerde dataveld wordt toegepast.
   * **Opties**:
     * **Equals (=)**: Bevestigt dat de waarde overeenkomt met de inkooporder.
     * **Not Equals (≠)**: Zorgt ervoor dat de waarde verschilt van de inkooporder.
     * **Greater Than (>)**: Verifieert dat de waarde de waarde van de inkooporder overschrijdt.
     * **Greater or Equals (≥)**: Bevestigt dat de waarde gelijk is aan of groter is dan de waarde van de inkooporder.
     * **Less Than (<)**: Controleert dat de waarde onder de waarde van de inkooporder ligt.
     * **Less or Equals (≤)**: Bevestigt dat de waarde lager dan of gelijk is aan de waarde van de inkooporder.

## **Aanvullende onderdelen in Version 4**:

* **Comparison Type**: Selecteert de te vergelijken entiteiten. De opties zijn:
  * **Purchase Order to Document**: Vergelijkt de inkooporderdata met het gerelateerde document.
  * **Received to Document**: Vergelijkt de ontvangen data (bijv. ontvangen hoeveelheden) met het document.
  * **Purchase Order to Received**: Vergelijkt de inkooporderdata met de ontvangen hoeveelheden.

## Functionaliteit:

* **Veldvergelijking**: Het systeem vergelijkt het geselecteerde orderdataveld (Unit Price, Discount of Quantity) uit de orderbevestiging met de bijbehorende waarde in de inkooporder.
* **Actie-uitvoering**: Op basis van het vergelijkingsresultaat en de operatorvoorwaarde kan de kaart vervolgacties triggeren, zoals meldingen of waarschuwingen.

## Voorbeeldscenario:

* Een orderbevestiging geeft een **eenheidsprijs** van $50 op, terwijl de inkooporder $45 vermeldt. Met de operator "Greater Than" markeert de kaart de afwijking, zodat het inkoopteam deze kan aanpakken voordat de verwerking plaatsvindt.

## Conclusie:

Deze kaart vereenvoudigt de validatie van afzonderlijke orderdatavelden en zorgt voor naleving van de inkoorder-voorwaarden. Door één veld tegelijk voor vergelijking te isoleren, ondersteunt hij gerichte beoordelingen en foutpreventie in de orderverwerking.
