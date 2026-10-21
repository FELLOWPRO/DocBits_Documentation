# Bestelgegevens in orderbevestiging

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-77711a53d4d0-nl.png" alt="Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld." width="563"><figcaption><p>Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld.</p></figcaption></figure>

## **Doel**

Deze workflow-kaart is ontworpen om specifieke velden — **Eenheidsprijs**, **Korting** of **Hoeveelheid** — te vergelijken tussen een orderbevestiging en een inkooporder. Hij zorgt voor consistentie en naleving van de afgesproken voorwaarden. Op basis van het vergelijkingsresultaat stelt de kaart gebruikers in staat om opgegeven tekst in een gekozen veld te schrijven wanneer de voorwaarde als **true** of **false** wordt geëvalueerd, wat de documentverwerking stroomlijnt en handmatige interventie vermindert.

## **Onderdelen van de kaart**

1. **Bestelgegevens**
   * **Beschrijving:** Geeft het veld op dat tussen de orderbevestiging en de inkooporder wordt vergeleken.
   * **Opties:**
     * **Eenheidsprijs**: Vergelijkt de eenheidsprijs in beide documenten.
     * **Korting**: Vergelijkt het kortingspercentage of de kortingswaarde.
     * **Hoeveelheid**: Vergelijkt de bestelde hoeveelheid.
2. **Exploitant**
   * **Beschrijving:** Definieert de voorwaarde die tijdens de vergelijking wordt toegepast.
   * **Opties:**
     * **Is gelijk aan (=):** Controleert of de waarde in het geselecteerde veld overeenkomt tussen de orderbevestiging en de inkooporder.
     * **Niet gelijk aan (≠):** Zorgt ervoor dat de waarde in het geselecteerde veld verschilt tussen de twee documenten.
3. **Tekst**
   * **Beschrijving:** Geeft de tekst op die bij de evaluatie van de voorwaarde in het doelveld wordt geschreven.
   * **Details:** Deze tekst kan aangepaste notities, statusupdates of vooraf gedefinieerde waarden bevatten.
4. **Veldnaam**
   * **Beschrijving:** Geeft het veld op waar de tekst wordt geschreven.
   * **Details:** Het doelveld wordt geselecteerd uit de beschikbare bewerkbare velden binnen het systeem.
5. **Conditieresultaat**
   * **Beschrijving:** Bepaalt wanneer de tekst moet worden geschreven, op basis van het vergelijkingsresultaat.
   * **Opties:**
     * **True:** Schrijft de tekst als aan de vergelijkingsvoorwaarde wordt voldaan.
     * **False:** Schrijft de tekst als niet aan de vergelijkingsvoorwaarde wordt voldaan.

## **Functionaliteit**

* **Vergelijkingsevaluatie:** Het systeem vergelijkt het geselecteerde veld tussen de orderbevestiging en de inkooporder met behulp van de opgegeven operator.
* **Actie-uitvoering:** Als de voorwaarde als **true** of **false** wordt geëvalueerd, wordt de opgegeven tekst in het aangewezen veld geschreven.

## **Opzet en configuratie**

* Om deze kaart op te zetten, selecteren gebruikers eerst het te vergelijken veld — **Eenheidsprijs**, **Korting** of **Hoeveelheid**. Vervolgens kiezen ze een operator om de vergelijkingsvoorwaarde te definiëren, zoals **equals** of **niet gelijk**. Gebruikers geven de tekst op die in een doelveld moet worden geschreven en selecteren wanneer deze actie moet plaatsvinden, op basis van het voorwaarderesultaat (**true** of **false**).

## **Voorbeeldscenario**

* Een orderbevestiging vermeldt een eenheidsprijs van $50 voor een product, terwijl de inkooporder een prijs van $45 opgeeft. Met de operator **Niet gelijk aan (≠)** identificeert de kaart de afwijking en schrijft hij de tekst "Price Mismatch" in een aangewezen veld wanneer de voorwaarde als **true** wordt geëvalueerd.

## **Conclusie**

De workflow-kaart "\[Unit Price/Discount/Quantity] in Order Confirmation" biedt een praktische oplossing om documentconsistentie te waarborgen. Door automatisch afwijkingen te markeren en relevante tekst in opgegeven velden te schrijven, verhoogt hij de efficiëntie en vermindert hij fouten in orderbeheerprocessen.
