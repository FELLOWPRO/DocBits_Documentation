# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om de hoeveelheid in een document te vergelijken met de tolerantie die in de inkooporder is gedefinieerd. Hij stelt gebruikers in staat te evalueren of de hoeveelheid aan bepaalde voorwaarden voldoet, zoals gelijkheid of het overschrijden van de opgegeven tolerantie. In Version 4 breidt de kaart de functionaliteit uit met de mogelijkheid om meerdere entiteiten te vergelijken, waaronder de inkooporder, de ontvangen hoeveelheden en de documenthoeveelheden, wat meer flexibiliteit biedt bij het afhandelen van verschillende scenario's.

## **Onderdelen van de kaart:**

1. **Any / All:**
   * **Beschrijving**: Geeft op hoe de vergelijking over meerdere items of voorwaarden moet worden toegepast.
   * **Opties**:
     * **Any**: Ten minste een van de voorwaarden moet waar zijn om de actie te triggeren.
     * **All**: Alle voorwaarden moeten waar zijn om de actie te laten doorgaan.
2. **Operator:**
   * **Beschrijving**: Definieert de voorwaarde die wordt toegepast om de documenthoeveelheid te vergelijken met de opgegeven tolerantie.
   * **Opties**:
     * **Equals (=)**: Controleert of de hoeveelheid overeenkomt met de opgegeven tolerantiewaarde.
     * **Not Equals (≠)**: Zorgt ervoor dat de hoeveelheid verschilt van de opgegeven tolerantiewaarde.
     * **Greater Than (>)**: Verifieert of de hoeveelheid groter is dan de opgegeven tolerantie.
     * **Greater or Equals (≥)**: Controleert of de hoeveelheid groter dan of gelijk is aan de opgegeven tolerantie.
     * **Lesser Than (<)**: Verifieert of de hoeveelheid kleiner is dan de opgegeven tolerantie.
     * **Lesser or Equals (≤)**: Controleert of de hoeveelheid kleiner dan of gelijk is aan de opgegeven tolerantie.
3. **Tolerance Amount:**
   * **Beschrijving**: Geeft de tolerantiewaarde op waarmee de documenthoeveelheid wordt vergeleken.
   * **Detail**: Deze waarde is numeriek en vertegenwoordigt de drempel van de toegestane afwijking in de hoeveelheid
4. **Tolerance Type:**
   * **Beschrijving**: Definieert het type tolerantie dat wordt toegepast.
   * **Opties**:
     * **Percentage**: De tolerantie wordt berekend als een percentage van de inkooporderhoeveelheid.
     * **Value**: De tolerantie wordt opgegeven als een vaste numerieke waarde.

## **Aanvullende onderdelen in Version 4:**

* **Comparison Type**: Selecteert de te vergelijken entiteiten, wat in Version 4 meer flexibiliteit biedt in de manier waarop de hoeveelheden worden geëvalueerd.
  * **Purchase Order to Document**: Vergelijkt de hoeveelheid in de inkooporder met de hoeveelheid in het gerelateerde document.
  * **Received to Document**: Vergelijkt de ontvangen hoeveelheid met de hoeveelheid in het document.
  * **Purchase Order to Received**: Vergelijkt de inkooporderhoeveelheid met de ontvangen hoeveelheid.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem vergelijkt de hoeveelheid in het document met de tolerantie in de inkooporder op basis van de geselecteerde operator en het tolerantiebedrag/-type. In Version 4 maakt de **Comparison Type** het mogelijk om verschillende hoeveelheden te vergelijken, zoals inkooporder tot ontvangen, of inkooporder tot document, wat een dynamischere vergelijking biedt.
* **Actie-uitvoering:**
  * **True-voorwaarde**: Als de vergelijking true oplevert (bijv. de documenthoeveelheid valt binnen het acceptabele tolerantiebereik), gaat de workflow verder.
  * **False-voorwaarde**: Als de vergelijking false oplevert (bijv. de hoeveelheid voldoet niet aan de tolerantie), gaat de workflow niet verder.

## **Opzet en configuratie:**

**Version 3:**

* Gebruikers configureren de kaart door de documenthoeveelheid te selecteren, het tolerantiebedrag en tolerantietype te definiëren en de juiste operator te kiezen om de hoeveelheid met de tolerantie te vergelijken. De kaart evalueert of de hoeveelheid binnen de tolerantiedrempel valt en gaat door met de "True"- of "False"-actie op basis van het resultaat.

**Version 4:**

* Naast de configuratie in Version 3 kunnen gebruikers de **Comparison Type** selecteren, waardoor vergelijkingen tussen verschillende entiteiten mogelijk zijn, zoals:
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Voorbeeldscenario:**

Een factuur toont dat 100 eenheden werden geleverd, maar de inkooporder autoriseerde slechts 90 eenheden. Het tolerantiebedrag is ingesteld op 10 eenheden en het tolerantietype is absoluut.

* **Version 3**: De kaart vergelijkt de 100 eenheden in het document met de tolerantie van 90 eenheden van de inkooporder. Als de hoeveelheid de tolerantie overschrijdt, markeert de kaart de afwijking voor verdere beoordeling.
* **Version 4**: De kaart kan de **inkooporderhoeveelheid** (90 eenheden) vergelijken met de **ontvangen hoeveelheid** (100 eenheden) of de **documenthoeveelheid** (100 eenheden). Afhankelijk van de geselecteerde **Comparison Type** controleert hij of het verschil tussen de twee entiteiten de tolerantie overschrijdt en triggert hij de bijbehorende actie.

## **Conclusie:**

* **Version 3**: Deze workflow-kaart vergelijkt de documenthoeveelheid met de inkoopordertolerantie, wat helpt om ervoor te zorgen dat afwijkingen in hoeveelheid worden gemarkeerd en op de juiste manier worden afgehandeld.
* **Version 4**: Breidt deze functionaliteit uit door gebruikers verschillende entiteiten te laten vergelijken, zoals inkooporder tot ontvangen of inkooporder tot document, wat meer flexibiliteit biedt bij het afhandelen van complexere scenario's. Version 4 zorgt voor strakkere controle over inkoop- en ontvangstworkflows en biedt dynamischere vergelijkingen en acties op basis van het gekozen vergelijkingstype.
