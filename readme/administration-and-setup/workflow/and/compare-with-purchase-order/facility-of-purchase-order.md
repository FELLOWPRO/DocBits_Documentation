# Faciliteit van inkooporder

<figure><img src="../../../../.gitbook/assets/workflow_card_condition_check_facility_in_po_v2-nl-nl.png" alt="Faciliteit van inkooporder, Versie 2" width="634"><figcaption><p>Versie 2</p></figcaption></figure>

## Doel:

Deze workflowkaart controleert de faciliteit van de aan een document gematchte inkooporders tegen een lijst met faciliteitscodes. De kaart kan worden gebruikt om documenten verschillend te behandelen afhankelijk van de faciliteit (locatie) waarvoor de bestelling is geplaatst, bijvoorbeeld om ze door te sturen naar het team dat voor die faciliteit verantwoordelijk is.

De inkoopordermatching hoort vóór deze kaart te lopen. Zonder gematchte inkooporder meldt de kaart ontbrekende gegevens.

## Onderdelen van de kaart:

1. **Elk/Alle**
   * **Beschrijving:** Hoe de faciliteitscodes van de gematchte inkooporders tegen de lijst worden geëvalueerd.
   * **Opties:**
     * **Elk:** Minstens één item van de lijst komt voor in de faciliteitscodes van de gematchte inkooporders.
     * **Alle:** Elke faciliteitscode van de gematchte inkooporders staat in de lijst. Is er geen waarde ingesteld, dan gebruikt de kaart **Alle**.
2. **Operator**
   * **Beschrijving:** Of de faciliteit wel of niet in de lijst hoort te staan.
   * **Opties:**
     * **Is**
     * **Is niet**
3. **Faciliteitsnaamcodes**
   * **Beschrijving:** De faciliteitscodes waarmee de faciliteit van de inkooporder wordt vergeleken.
   * **Detail:** Er kunnen meerdere codes worden ingevoerd, gescheiden door komma's.

## Functionaliteit:

* **Voorwaarde-evaluatie:** De kaart leest de aan het document gematchte inkoopordernummers, laadt deze inkooporders en verzamelt van elk daarvan de faciliteit (locatie). Inkooporders zonder faciliteit worden overgeslagen. De verzamelde faciliteitscodes worden vervolgens vergeleken met de **Faciliteitsnaamcodes** op de kaart.
  * Met **Elk** en **Is** wordt bij de vergelijking geen onderscheid gemaakt tussen hoofd- en kleine letters, en een item van de lijst telt ook mee wanneer het deel uitmaakt van een langere faciliteitscode (zo wordt het item `WH` gevonden in `WH01`).
  * Met **Alle** en **Is** hoort elke faciliteitscode van de inkooporders in precies dezelfde schrijfwijze in de lijst voor te komen, inclusief hoofd- en kleine letters.
  * Heeft geen van de gematchte inkooporders een faciliteit, dan is aan **Alle** voldaan en aan **Elk** niet.
  * Met **Is niet** is het resultaat niet eenvoudigweg het omgekeerde van **Is**. Het kaartlogboek toont welke codes zijn gevonden en welke niet zijn gematcht, wat helpt om het gedrag bij een bepaalde instelling te controleren.
* **Actie-uitvoering:**
  * **True-voorwaarde:**\
    Wordt aan de voorwaarde voldaan, dan gaat de workflow verder, bijvoorbeeld met een stap die specifiek is voor de vermelde faciliteiten.
  * **False-voorwaarde:**\
    Wordt niet aan de voorwaarde voldaan, dan stopt de workflow met een niet voldane voorwaarde.
* **Ontbrekende gegevens:** Zijn er op de kaart geen faciliteitscodes ingevoerd of heeft het document geen gematchte inkooporder, dan evalueert de kaart de voorwaarde niet en meldt ze de ontbrekende gegevens in het workflowlogboek.

## Opzet en configuratie:

* De kaart kan als And-voorwaarde na de inkoopordermatching worden toegevoegd vanuit de categorie **Vergelijk met inkooporder**. Daarna kunnen **Elk** of **Alle**, de operator en de faciliteitscodes, gescheiden door komma's, worden ingesteld. De codes in dezelfde schrijfwijze invoeren als op de inkooporder is de veiligste keuze, omdat **Alle** ze exact vergelijkt.
* Met **Testkaart** in het kaartmenu van de Workflow Builder kan de configuratie op een bestaand document worden uitgeprobeerd. Het kaartlogboek somt de gematchte inkooporders op, de daarop gevonden faciliteitscodes en de codes die niet zijn gematcht.

## Conclusie:

De workflowkaart "Facility of Purchase Order" maakt de faciliteit van de bestelde goederen beschikbaar als workflowvoorwaarde. Zo kan één workflow documenten voor verschillende faciliteiten verschillend behandelen, op basis van de inkoopordergegevens in plaats van wat er op het document staat.
