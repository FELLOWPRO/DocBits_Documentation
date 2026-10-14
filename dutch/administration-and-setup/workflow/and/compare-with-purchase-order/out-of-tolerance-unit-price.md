# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om te evalueren of de gecombineerde waarde van eenheidsprijzen en een opgegeven veld een gedefinieerde drempel overschrijdt of daaronder blijft. Hij helpt afwijkingen te identificeren waarbij de eenheidsprijzen, gecombineerd met andere velden, buiten de tolerantie vallen, en zorgt ervoor dat prijsvoorwaarden aan de verwachtingen voldoen en eventuele problemen voor beoordeling of verdere actie worden gemarkeerd.

## **Onderdelen van de kaart:**

1. **Field Name:**
   * **Beschrijving**: Geeft het documentveld op dat de waarde bevat die met de eenheidsprijs wordt gecombineerd.
   * **Detail**: De waarde in dit veld wordt gecombineerd met de eenheidsprijs om de totale gecombineerde waarde voor vergelijking te creëren.
2. **Operator:**
   * **Beschrijving**: Definieert de voorwaarde voor het vergelijken van de gecombineerde waarde van de eenheidsprijs en de veldwaarde met de opgegeven waarde.
   * **Opties**:
     * **Equals (=)**: Verifieert of de gecombineerde waarde van de eenheidsprijs en het veld overeenkomt met de opgegeven waarde.
     * **Not Equals (≠)**: Zorgt ervoor dat de gecombineerde waarde van de eenheidsprijs en het veld verschilt van de opgegeven waarde.
     * **Greater Than (>)**: Verifieert of de gecombineerde waarde van de eenheidsprijs en het veld de opgegeven waarde overschrijdt.
     * **Greater or Equals (≥)**: Verifieert of de gecombineerde waarde van de eenheidsprijs en het veld groter dan of gelijk is aan de opgegeven waarde.
     * **Lesser Than (<)**: Verifieert of de gecombineerde waarde van de eenheidsprijs en het veld kleiner is dan de opgegeven waarde.
     * **Lesser or Equals (≤)**: Verifieert of de gecombineerde waarde van de eenheidsprijs en het veld kleiner dan of gelijk is aan de opgegeven waarde.
3. **Value:**
   * **Beschrijving**: Geeft de waarde op waarmee de gecombineerde eenheidsprijs en veldwaarde worden vergeleken.
   * **Detail**: Deze numerieke waarde vertegenwoordigt de drempel voor vergelijking. Als de gecombineerde waarde van de eenheidsprijs en het veld deze waarde overschrijdt of daaronder blijft (op basis van de geselecteerde operator), triggert de voorwaarde de opgegeven acties.

## **Functionaliteit:**

* &#x20;**Voorwaarde-evaluatie:** Het systeem berekent de gecombineerde waarde door de eenheidsprijs met de veldwaarde te vermenigvuldigen of op te tellen, afhankelijk van de configuratie. Het resultaat wordt vervolgens met de opgegeven waarde vergeleken met behulp van de geselecteerde operator. Als aan de voorwaarde wordt voldaan (d.w.z. de gecombineerde waarde valt buiten de tolerantie), gaat de workflow verder met de volgende stap, of dat nu goedkeuring, afkeuring of verdere beoordeling is.
* **Actie-uitvoering:**
  * **True-voorwaarde**: Als de vergelijking true oplevert (d.w.z. de gecombineerde waarde voldoet aan de voorwaarde), triggert de workflow de actie die aan de true-voorwaarde is gekoppeld (bijv. goedkeuring of melding).
  * **False-voorwaarde**: Als de vergelijking false oplevert (d.w.z. de gecombineerde waarde voldoet niet aan de voorwaarde), gaat de workflow niet verder.

## **Opzet en configuratie:**

* Gebruikers selecteren het veld dat de waarde bevat die met de eenheidsprijs wordt gecombineerd. Vervolgens kiezen ze de juiste operator om te bepalen hoe de gecombineerde waarde met de opgegeven waarde wordt vergeleken. Ten slotte stelt de gebruiker de waarde in waarmee de gecombineerde prijs wordt vergeleken.

## **Voorbeeldscenario:**

* Een factuur vermeldt 50 eenheden van een product à $30 per stuk, in totaal $1500. Het gerelateerde document heeft een hoeveelheidsveld met de waarde 10. De gecombineerde prijs wordt berekend door de eenheidsprijs ($30) en de hoeveelheid (10) te vermenigvuldigen, wat resulteert in $300. De kaart vergelijkt deze gecombineerde waarde vervolgens met een drempel van $250. Met de operator "Greater Than" stelt de kaart vast dat $300 groter is dan $250, waardoor een goedkeuringsproces voor het document wordt getriggerd.

## **Conclusie:**

De workflow-kaart "Out of Tolerance Unit Prices Combined with Fields" helpt ervoor te zorgen dat prijs- en veldwaarden overeenkomen met bedrijfsregels. Door deze controle te automatiseren, kunnen organisaties afwijkingen vroeg in het proces identificeren en ervoor zorgen dat eventuele eenheidsprijzen buiten de tolerantie worden gemarkeerd voor beoordeling of noodzakelijke actie.
