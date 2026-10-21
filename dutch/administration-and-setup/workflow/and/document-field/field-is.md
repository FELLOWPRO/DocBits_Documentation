# Aanwezigheid en inhoud van een documentveld controleren

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-db30554e1eb1-nl.png" alt="Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld." width="563"><figcaption><p>Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld.</p></figcaption></figure>

## **Doel:**

Deze workflow-kaart is ontworpen om acties te automatiseren op basis van de aanwezigheid of status van een opgegeven veld binnen een document. Door te evalueren of het veld leeg, ontbrekend of gevuld is, stelt hij workflows in staat documenten met precisie en nauwkeurigheid af te handelen.

## **Onderdelen van de kaart:**

1. **Veldnaam**
   * **Beschrijving:** Geeft de naam op van het te evalueren veld.
   * **Details:** Dit moet exact overeenkomen met de identifier die in het document wordt gebruikt om een nauwkeurige velddetectie te waarborgen.
2. **Exploitanten**
   * **Beschrijving**: Definieert de voorwaarde die de workflow triggert, op basis van de aanwezigheid of status van het veld.
   * **Opties**:
     * **Leeg/niet in document:** De workflow wordt getriggerd als het veld ofwel ontbreekt in het document, ofwel aanwezig maar leeg is.
     * **In document/niet leeg:** De workflow wordt getriggerd als het veld in het document bestaat en een waarde bevat.

## **Functionaliteit:**

* **Statusdetectie:** De kaart monitort het opgegeven veld om de aanwezigheid en status ervan te evalueren.
* **Voorwaarde-evaluatie:**
  * Het systeem evalueert of het opgegeven veld zich in de status (Empty/Not in Document of In Document/Not Empty) bevindt die door de geselecteerde operator is gedefinieerd.
*

**Actie-uitvoering:**
* **Empty/Not in Document-voorwaarde:** Als de status van het veld overeenkomt met deze voorwaarde (d.w.z. het veld ontbreekt in het document of is aanwezig maar leeg), start het systeem de bijbehorende acties. Deze kunnen het genereren van waarschuwingen, het markeren van het document voor beoordeling of het stoppen van de workflow omvatten.
* **In Document/Not Empty-voorwaarde:** Als de status van het veld overeenkomt met deze voorwaarde (d.w.z. het veld bestaat in het document en bevat een waarde), triggert het systeem de bijbehorende acties. Deze kunnen het inschakelen van vervolgstappen in de workflow, het bijwerken van records of het triggeren van meldingen omvatten.
## **Opzet en configuratie:**

* Gebruikers selecteren het veld uit een lijst van beschikbare documentvelden. De operator wordt gekozen via een dropdownmenu, met duidelijke opties voor "Empty/Not in Document" of "In Document/Not Empty".

## **Conclusie:**

De workflow-kaart "Field Presence and State Validation" is een essentieel hulpmiddel voor documentverwerkingsworkflows en zorgt voor een nauwkeurige afhandeling van ontbrekende of gevulde velden. Door acties te automatiseren op basis van veldstatussen verbetert deze kaart de data-integriteit, vermindert hij fouten en zorgt hij ervoor dat workflows soepel en efficiënt verlopen.

<!-- workflow-card-practical-example-20261021 -->

## Praktisch voorbeeld

**Wanneer gebruiken:** Detecteer facturen waarvan het factuurnummer nog moet worden gecontroleerd.

**Configuratie:** Selecteer veld `invoice_number` en Leeg/Niet in document.

**Verwacht resultaat en tegenvoorbeeld:** Er wordt een leeg of ontbrekend veld doorgegeven. Een ingevulde waarde zoals `DEMO-001` voldoet niet aan deze voorwaarde.

Dit is een illustratieve configuratie en een verwacht resultaat. Gebruik velden, gebruikers en groepen die in uw testorganisatie zijn geconfigureerd; het is geen bewering dat dit voorbeeld is uitgevoerd.
