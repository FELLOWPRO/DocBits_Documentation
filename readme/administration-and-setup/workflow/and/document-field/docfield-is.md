# Docfield is

<figure><img src="../../../../.gitbook/assets/image (9) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om acties te automatiseren door de waarde van een opgegeven documentveld te vergelijken met een referentiewaarde of -voorwaarde. Hij zorgt voor dynamische en nauwkeurige besluitvorming in workflows op basis van validatie van documentgegevens.

## **Onderdelen van de kaart:**

1. **Field Name**
   * **Beschrijving:** Geeft de naam op van het te evalueren documentveld.
   * **Detail:** Dit moet exact overeenkomen met de identifier van het veld binnen het document.
2. **Operators**
   * **Beschrijving:** Definieert het type vergelijking dat tussen de veldwaarde en de referentiewaarde wordt uitgevoerd.
   * **Opties:**
     * **Equals (=):** Controleert of de veldwaarde overeenkomt met de referentiewaarde.
     * **Not Equals (≠):** Zorgt ervoor dat de veldwaarde verschilt van de referentiewaarde.
     * **Greater Than (>):** Bevestigt dat de veldwaarde groter is dan de referentiewaarde.
     * **Greater or Equals (≥):** Valideert dat de veldwaarde gelijk is aan of groter is dan de referentiewaarde.
     * **Lesser Than (<):** Controleert of de veldwaarde kleiner is dan de referentiewaarde.
     * **Less or Equals (≤):** Zorgt ervoor dat de veldwaarde kleiner dan of gelijk is aan de referentiewaarde.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem controleert of de waarde van het documentveld, in relatie tot de bijbehorende kolom, aan de door de operator en referentiewaarde opgegeven vergelijkingsvoorwaarde voldoet.
* **Actie-uitvoering:**
  * **True-voorwaarde:**\
    Als de waarde van het documentveld aan de opgegeven voorwaarde voldoet (bijv. gelijk aan de referentiewaarde), triggert het systeem de bijbehorende acties. Deze kunnen het bijwerken van records, het voortzetten van de workflow of het genereren van meldingen omvatten.
  * **False-voorwaarde:**\
    Als de waarde van het documentveld niet aan de opgegeven voorwaarde voldoet, worden alternatieve acties of geen acties uitgevoerd, op basis van de workflow-configuratie.

## **Opzet en configuratie:**&#x20;

* De gebruiker selecteert de veldnaam van het relevante document en kiest de operator uit het dropdownmenu. Vervolgens geeft de gebruiker de referentieveldwaarde op om de configuratie te voltooien.

## **Conclusie:**

De workflow-kaart "DocField Comparison Validation" is een robuust hulpmiddel voor dynamische documentverwerking. Door acties te automatiseren op basis van veldvergelijkingen stroomlijnt deze kaart workflows, verbetert hij de nauwkeurigheid en ondersteunt hij datagedreven besluitvorming.
