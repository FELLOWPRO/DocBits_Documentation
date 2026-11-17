# Documentveld vergelijken met een referentiewaarde

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_operator_value_v1-nl-nl.png" alt="Documentveld vergelijken met een referentiewaarde, Versie 1" width="634"><figcaption><p>Versie 1</p></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_docfield_operator_value_v2-nl-nl.png" alt="Documentveld vergelijken met een referentiewaarde, Versie 2" width="634"><figcaption><p>Versie 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.mp4" %}

**Video:** Kaart: Documentveld vergeleken met een waarde · 0:46 · [Ondertitels (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.vtt)

<details>

<summary>Transcriptie</summary>

**Documentveld vergeleken met een waarde** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.mp4#t=0.25)

De kaart Documentveld vergelijkt één veld van het document met een waarde die u invoert. Kies het veld, bijvoorbeeld Totaalbedrag, dan de operator, hier Groter dan, en de waarde, tienduizend.

**Tekst, getallen, datums** · [0:19](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.mp4#t=19.05)

Tekstvelden kunnen alleen gelijk of niet gelijk zijn, en hoofdletters maken niet uit. Getallen en datums kunnen ook groter of kleiner dan de waarde zijn. Staat het veld niet op het document, dan neemt de kaart het foutpad.

**Voorbeeld: grote facturen hebben een tweede goedkeuring nodig** · [0:33](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-doc-field-value/v1/nl.mp4#t=33.183)

Bijvoorbeeld een tweede goedkeuring voor grote facturen: Totaalbedrag groter dan tienduizend, dan de toewijzingskaart voor financiën. Kleinere facturen bereiken deze stap niet.

</details>

## **Doel:**

Deze workflow-kaart is ontworpen om acties te automatiseren door de waarde van een opgegeven documentveld te vergelijken met een referentiewaarde of -voorwaarde. Hij zorgt voor dynamische en nauwkeurige besluitvorming in workflows op basis van validatie van documentgegevens.

## **Onderdelen van de kaart:**

1. **Veldnaam**
   * **Beschrijving:** Geeft de naam op van het te evalueren documentveld.
   * **Details:** Dit moet exact overeenkomen met de identifier van het veld binnen het document.
2. **Exploitanten**
   * **Beschrijving:** Definieert het type vergelijking dat tussen de veldwaarde en de referentiewaarde wordt uitgevoerd.
   * **Opties:**
     * **Is gelijk aan (=):** Controleert of de veldwaarde overeenkomt met de referentiewaarde.
     * **Niet gelijk aan (≠):** Zorgt ervoor dat de veldwaarde verschilt van de referentiewaarde.
     * **Groter dan (>):** Bevestigt dat de veldwaarde groter is dan de referentiewaarde.
     * **Groter of gelijk aan (≥):** Valideert dat de veldwaarde gelijk is aan of groter is dan de referentiewaarde.
     * **Kleiner dan (<):** Controleert of de veldwaarde kleiner is dan de referentiewaarde.
     * **Minder of gelijk aan (≤):** Zorgt ervoor dat de veldwaarde kleiner dan of gelijk is aan de referentiewaarde.

## **Functionaliteit:**

* **Voorwaarde-evaluatie:** Het systeem controleert of de waarde van het documentveld, in relatie tot de bijbehorende kolom, aan de door de operator en referentiewaarde opgegeven vergelijkingsvoorwaarde voldoet.
* **Actie-uitvoering:**
  * **True-voorwaarde:**\
    Als de waarde van het documentveld aan de opgegeven voorwaarde voldoet (bijv. gelijk aan de referentiewaarde), triggert het systeem de bijbehorende acties. Deze kunnen het bijwerken van records, het voortzetten van de workflow of het genereren van meldingen omvatten.
  * **False-voorwaarde:**\
    Als de waarde van het documentveld niet aan de opgegeven voorwaarde voldoet, worden alternatieve acties of geen acties uitgevoerd, op basis van de workflow-configuratie.

## **Opzet en configuratie:**

* De gebruiker de veldnaam van het relevante document selecteert en de operator uit het dropdownmenu kiest. Vervolgens geeft de gebruiker de referentieveldwaarde op om de configuratie te voltooien.

## **Conclusie:**

De workflow-kaart "DocField Comparison Validation" is een robuust hulpmiddel voor dynamische documentverwerking. Door acties te automatiseren op basis van veldvergelijkingen stroomlijnt deze kaart workflows, verbetert hij de nauwkeurigheid en ondersteunt hij datagedreven besluitvorming.

<!-- workflow-card-practical-example-20261021 -->

## Praktisch voorbeeld

**Wanneer gebruiken:** Facturen boven een bepaald bedrag bekijken.

**Configuratie:** Selecteer numeriek veld `total_amount`, operator `>` en referentiewaarde `1000`.

**Verwacht resultaat en tegenvoorbeeld:** Een waarde van `1200` voldoet aan de voorwaarde. `1000` en `900` voldoen niet: de operator `>` vereist een waarde groter dan `1000`.

Dit is een illustratieve configuratie en een verwacht resultaat. Gebruik velden, gebruikers en groepen die in uw testorganisatie zijn geconfigureerd; het is geen bewering dat dit voorbeeld is uitgevoerd.
