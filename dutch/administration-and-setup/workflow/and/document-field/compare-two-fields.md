# Compare two Fields

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om acties te automatiseren door de waarden van twee opgegeven documentvelden te vergelijken. Hij maakt dynamische besluitvorming op basis van veldgegevens mogelijk en zorgt ervoor dat workflows worden uitgevoerd op basis van vergelijkingen tussen verschillende documentwaarden.

## **Onderdelen van de kaart:**

1. **Field Name (1)**
   * **Beschrijving:** Geeft het eerste te vergelijken documentveld op.
   * **Detail:** Dit moet exact overeenkomen met de identifier van het eerste veld binnen het document.
2. **Operator**
   * **Beschrijving:** Definieert het type vergelijking dat tussen de twee velden wordt uitgevoerd.
   * **Opties:**
     * **Equals (=):** Controleert of de waarden van de twee velden gelijk zijn.
     * **Not Equals (≠):** Zorgt ervoor dat de waarden van de twee velden verschillend zijn.
     * **Greater Than (>):** Bevestigt dat de waarde van het eerste veld groter is dan het tweede veld.
     * **Greater or Equals (≥):** Valideert dat de waarde van het eerste veld gelijk is aan of groter is dan het tweede veld.
     * **Lesser Than (<):** Controleert of de waarde van het eerste veld kleiner is dan het tweede veld.
     * **Less or Equals (≤):** Zorgt ervoor dat de waarde van het eerste veld kleiner dan of gelijk is aan het tweede veld.
3. **Field Name (2)**
   * **Beschrijving:** Geeft het tweede documentveld op dat met het eerste veld wordt vergeleken.
   * **Detail:** Dit moet exact overeenkomen met de identifier van het tweede veld binnen het document.

## **Functionaliteit:**

**Voorwaarde-evaluatie:** Het systeem evalueert of de waarden in de twee opgegeven velden aan de door de operator gedefinieerde vergelijkingsvoorwaarde voldoen.

**Actie-uitvoering:**

* **True-voorwaarde:**\
  Als de waarden van de twee velden overeenkomen met de vergelijkingsvoorwaarde, triggert het systeem de bijbehorende acties. Deze acties kunnen het bijwerken van records of het triggeren van waarschuwingen omvatten.
* **False-voorwaarde:**\
  Als de waarden van de twee velden niet overeenkomen met de opgegeven voorwaarde, kunnen alternatieve acties of geen acties worden uitgevoerd, afhankelijk van de configuratie van de workflows.

## **Opzet en configuratie:**&#x20;

* Gebruikers configureren de kaart door de twee te vergelijken velden uit een lijst van beschikbare velden in het systeem te selecteren. De operator wordt geselecteerd uit een dropdownlijst van beschikbare vergelijkingsopties.

## **Conclusie:**

De workflow-kaart "Compare Two Fields" is een essentieel hulpmiddel voor het vergelijken van gegevens tussen velden binnen documenten. Door acties te automatiseren op basis van veldvergelijkingen helpt deze kaart de besluitvorming te optimaliseren, ondersteunt hij gegevensvalidatie en verbetert hij de workflow-automatisering.
