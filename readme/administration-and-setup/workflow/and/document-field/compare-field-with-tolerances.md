# Compare Field with tolerances

<figure><img src="../../../../.gitbook/assets/image (15) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om de waarde van een veld te vergelijken met een opgegeven referentiewaarde, waarbij toleranties zijn toegestaan. Hij maakt nauwkeurige voorwaardelijke verwerking mogelijk in workflows waar kleine afwijkingen acceptabel zijn, waardoor hij ideaal is voor scenario's zoals kwaliteitsborging, financiële analyse of drempelgebaseerde acties.

## **Onderdelen van de kaart:**

1. **Field Name**
   * **Beschrijving:** Het veld dat in de vergelijking wordt geëvalueerd.
   * **Detail:** Dit moet exact overeenkomen met de identifier van het eerste veld binnen het document.
2. **Comparison Operator**
   * **Beschrijving:** Geeft op hoe de geselecteerde veldwaarde met de referentiewaarde wordt vergeleken.
   * **Opties:**
     * **Equals (=):** Verifieert of de veldwaarde exact overeenkomt met de referentiewaarde.
     * **Not Equals (≠):** Verifieert of de veldwaarde niet overeenkomt met de referentiewaarde.
     * **Greater Than (>):** Controleert of de veldwaarde groter is dan de referentiewaarde.
     * **Greater or Equals (≥):** Controleert of de veldwaarde groter dan of gelijk is aan de referentiewaarde.
     * **Lesser Than (<):** Controleert of de veldwaarde kleiner is dan de referentiewaarde.
     * **Lesser or Equals (≤):** Controleert of de veldwaarde kleiner dan of gelijk is aan de referentiewaarde.
3. **Reference Value**
   * **Beschrijving:** De waarde waarmee het veld wordt vergeleken.
   * **Detail:** Deze waarde kan numeriek, tekst- of datumgebaseerd zijn, afhankelijk van de context van de vergelijking.
4. **Tolerance Amount**
   * **Beschrijving:** Definieert de aanvaardbare foutmarge voor de vergelijking.
   * **Detail:** Het tolerantiebedrag is een numerieke waarde die het maximaal toegestane verschil tussen de twee veldwaarden aangeeft om de vergelijking als true te beschouwen.
5. **Tolerance Type**
   * **Beschrijving:** Geeft de meeteenheid voor het tolerantiebedrag op.
   * **Opties:**
     * **Value:** De tolerantie is een absolute waarde, wat betekent dat de twee velden met het opgegeven tolerantiebedrag kunnen verschillen.
     * **Percent:** De tolerantie wordt berekend als een percentage van de waarde van het tweede veld, wat een relatieve foutmarge mogelijk maakt.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem evalueert de waarde van het veld ten opzichte van de referentiewaarde met behulp van de geselecteerde vergelijkingsoperator. Als een tolerantie is geconfigureerd, beschouwt het systeem de vergelijking als geslaagd als de veldwaarde binnen het gedefinieerde tolerantiebereik valt.
* **Actie-uitvoering:**
  * **Binnen tolerantie:** Als de veldwaarde binnen de opgegeven tolerantie aan de voorwaarde voldoet, gaat de workflow verder en worden de bijbehorende acties getriggerd.
  * **Buiten tolerantie:** Als de veldwaarde niet aan de voorwaarde voldoet of buiten het tolerantiebereik valt, kunnen alternatieve acties worden uitgevoerd, zoals logging, het verzenden van waarschuwingen of het stoppen van de workflow.

## **Opzet en configuratie:**

* Gebruikers configureren de kaart door het te evalueren veld uit een lijst van beschikbare velden te selecteren en de vergelijkingsoperator (bijv. equals, greater than) uit een dropdownlijst te kiezen. Vervolgens geven ze de referentiewaarde op waarmee wordt vergeleken en definiëren ze het tolerantiebedrag, waarna ze het tolerantietype (bijv. percent of value) selecteren.&#x20;

## **Conclusie:**

De kaart "Field Comparison with Tolerances" is een veelzijdig hulpmiddel voor workflows die flexibele evaluaties vereisen. Door vergelijkingen met toleranties mogelijk te maken, zorgt hij ervoor dat workflows efficiënt en aanpasbaar blijven, en houdt hij rekening met variaties uit de praktijk zonder concessies te doen aan de nauwkeurigheid.
