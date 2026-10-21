# Vergelijk Veld met toleranties

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-4ee291b0848d-nl.png" alt="Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld." width="563"><figcaption><p>Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld.</p></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om de waarde van een veld te vergelijken met een opgegeven referentiewaarde, waarbij toleranties zijn toegestaan. Hij maakt nauwkeurige voorwaardelijke verwerking mogelijk in workflows waar kleine afwijkingen acceptabel zijn, waardoor hij ideaal is voor scenario's zoals kwaliteitsborging, financiële analyse of drempelgebaseerde acties.

## **Onderdelen van de kaart:**

1. **Veldnaam**
   * **Beschrijving:** Het veld dat in de vergelijking wordt geëvalueerd.
   * **Details:** Dit moet exact overeenkomen met de identifier van het eerste veld binnen het document.
2. **Vergelijkingsoperator**
   * **Beschrijving:** Geeft op hoe de geselecteerde veldwaarde met de referentiewaarde wordt vergeleken.
   * **Opties:**
     * **Is gelijk aan (=):** Verifieert of de veldwaarde exact overeenkomt met de referentiewaarde.
     * **Niet gelijk aan (≠):** Verifieert of de veldwaarde niet overeenkomt met de referentiewaarde.
     * **Groter dan (>):** Controleert of de veldwaarde groter is dan de referentiewaarde.
     * **Groter of gelijk aan (≥):** Controleert of de veldwaarde groter dan of gelijk is aan de referentiewaarde.
     * **Kleiner dan (<):** Controleert of de veldwaarde kleiner is dan de referentiewaarde.
     * **Kleiner of gelijk aan (≤):** Controleert of de veldwaarde kleiner dan of gelijk is aan de referentiewaarde.
3. **Referentiewaarde**
   * **Beschrijving:** De waarde waarmee het veld wordt vergeleken.
   * **Details:** Deze waarde kan numeriek, tekst- of datumgebaseerd zijn, afhankelijk van de context van de vergelijking.
4. **Tolerantiebedrag**
   * **Beschrijving:** Definieert de aanvaardbare foutmarge voor de vergelijking.
   * **Details:** Het tolerantiebedrag is een numerieke waarde die het maximaal toegestane verschil tussen de twee veldwaarden aangeeft om de vergelijking als true te beschouwen.
5. **Tolerantietype**
   * **Beschrijving:** Geeft de meeteenheid voor het tolerantiebedrag op.
   * **Opties:**
     * **Waarde:** De tolerantie is een absolute waarde, wat betekent dat de twee velden met het opgegeven tolerantiebedrag kunnen verschillen.
     * **Percent:** De tolerantie wordt berekend als een percentage van de waarde van het tweede veld, wat een relatieve foutmarge mogelijk maakt.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem evalueert de waarde van het veld ten opzichte van de referentiewaarde met behulp van de geselecteerde vergelijkingsoperator. Als een tolerantie is geconfigureerd, beschouwt het systeem de vergelijking als geslaagd als de veldwaarde binnen het gedefinieerde tolerantiebereik valt.
* **Actie-uitvoering:**
  * **Binnen tolerantie:** Als de veldwaarde binnen de opgegeven tolerantie aan de voorwaarde voldoet, gaat de workflow verder en worden de bijbehorende acties getriggerd.
  * **Buiten tolerantie:** Als de veldwaarde niet aan de voorwaarde voldoet of buiten het tolerantiebereik valt, kunnen alternatieve acties worden uitgevoerd, zoals logging, het verzenden van waarschuwingen of het stoppen van de workflow.

## **Opzet en configuratie:**

* Gebruikers configureren de kaart door het te evalueren veld uit een lijst van beschikbare velden te selecteren en de vergelijkingsoperator (bijv. equals, greater than) uit een dropdownlijst te kiezen. Vervolgens geven ze de referentiewaarde op waarmee wordt vergeleken en definiëren ze het tolerantiebedrag, waarna ze het tolerantietype (bijv. percent of value) selecteren.

## **Conclusie:**

De kaart "Field Comparison with Tolerances" is een veelzijdig hulpmiddel voor workflows die flexibele evaluaties vereisen. Door vergelijkingen met toleranties mogelijk te maken, zorgt hij ervoor dat workflows efficiënt en aanpasbaar blijven, en houdt hij rekening met variaties uit de praktijk zonder concessies te doen aan de nauwkeurigheid.

<!-- workflow-card-complete-example-20261021 condition_docfield_operator_value_tolerances -->

### Voorbeeld tolerantie referentiewaarde

**Configuratie:** Kies numeriek documentveld `total_amount`, gelijkheid, referentiewaarde `100`, absolute tolerantie `5` en tolerantietype Waarde.

**Verwacht resultaat en tegenvoorbeeld:** Met de waarde `103` is de voorwaarde waar omdat het verschil binnen de toegestane tolerantie ligt. Met de waarde `110` is de voorwaarde onwaar omdat het verschil die tolerantie overschrijdt. Deze kaart vergelijkt één veld met een geconfigureerde referentiewaarde. Gebruik de aparte kaart met twee velden als beide zijden uit documentvelden moeten komen. Ontbrekende of niet-numerieke gegevens vereisen onderzoek, geen veronderstelde overeenkomst.

Dit is een illustratieve testconfiguratie en verwachte uitkomst; het werd niet uitgevoerd. Gebruik gegevens en ontvangers die in uw testorganisatie zijn geconfigureerd.
