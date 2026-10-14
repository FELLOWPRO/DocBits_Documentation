# Order Data in Order Confirmation

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel**

Deze workflow-kaart is ontworpen om specifieke velden — **Unit Price**, **Discount** of **Quantity** — te vergelijken tussen een orderbevestiging en een inkooporder. Hij zorgt voor consistentie en naleving van de afgesproken voorwaarden. Op basis van het vergelijkingsresultaat stelt de kaart gebruikers in staat om opgegeven tekst in een gekozen veld te schrijven wanneer de voorwaarde als **true** of **false** wordt geëvalueerd, wat de documentverwerking stroomlijnt en handmatige interventie vermindert.

## **Onderdelen van de kaart**

1. **Order Data**
   * **Beschrijving:** Geeft het veld op dat tussen de orderbevestiging en de inkooporder wordt vergeleken.
   * **Opties:**
     * **Unit Price**: Vergelijkt de eenheidsprijs in beide documenten.
     * **Discount**: Vergelijkt het kortingspercentage of de kortingswaarde.
     * **Quantity**: Vergelijkt de bestelde hoeveelheid.
2. **Operator**
   * **Beschrijving:** Definieert de voorwaarde die tijdens de vergelijking wordt toegepast.
   * **Opties:**
     * **Equals (=):** Controleert of de waarde in het geselecteerde veld overeenkomt tussen de orderbevestiging en de inkooporder.
     * **Not Equals (≠):** Zorgt ervoor dat de waarde in het geselecteerde veld verschilt tussen de twee documenten.
3. **Text**
   * **Beschrijving:** Geeft de tekst op die bij de evaluatie van de voorwaarde in het doelveld wordt geschreven.
   * **Detail:** Deze tekst kan aangepaste notities, statusupdates of vooraf gedefinieerde waarden bevatten.
4. **Field Name**
   * **Beschrijving:** Geeft het veld op waar de tekst wordt geschreven.
   * **Detail:** Het doelveld wordt geselecteerd uit de beschikbare bewerkbare velden binnen het systeem.
5. **Condition Result**
   * **Beschrijving:** Bepaalt wanneer de tekst moet worden geschreven, op basis van het vergelijkingsresultaat.
   * **Opties:**
     * **True:** Schrijft de tekst als aan de vergelijkingsvoorwaarde wordt voldaan.
     * **False:** Schrijft de tekst als niet aan de vergelijkingsvoorwaarde wordt voldaan.

## **Functionaliteit**

* **Vergelijkingsevaluatie:** Het systeem vergelijkt het geselecteerde veld tussen de orderbevestiging en de inkooporder met behulp van de opgegeven operator.
* **Actie-uitvoering:** Als de voorwaarde als **true** of **false** wordt geëvalueerd, wordt de opgegeven tekst in het aangewezen veld geschreven.

## **Opzet en configuratie**

* Om deze kaart op te zetten, selecteren gebruikers eerst het te vergelijken veld — **Unit Price**, **Discount** of **Quantity**. Vervolgens kiezen ze een operator om de vergelijkingsvoorwaarde te definiëren, zoals **equals** of **not equals**. Gebruikers geven de tekst op die in een doelveld moet worden geschreven en selecteren wanneer deze actie moet plaatsvinden, op basis van het voorwaarderesultaat (**true** of **false**).

## **Voorbeeldscenario**

* Een orderbevestiging vermeldt een eenheidsprijs van $50 voor een product, terwijl de inkooporder een prijs van $45 opgeeft. Met de operator **Not Equals (≠)** identificeert de kaart de afwijking en schrijft hij de tekst "Price Mismatch" in een aangewezen veld wanneer de voorwaarde als **true** wordt geëvalueerd.

## **Conclusie**

De workflow-kaart "\[Unit Price/Discount/Quantity] in Order Confirmation" biedt een praktische oplossing om documentconsistentie te waarborgen. Door automatisch afwijkingen te markeren en relevante tekst in opgegeven velden te schrijven, verhoogt hij de efficiëntie en vermindert hij fouten in orderbeheerprocessen.
