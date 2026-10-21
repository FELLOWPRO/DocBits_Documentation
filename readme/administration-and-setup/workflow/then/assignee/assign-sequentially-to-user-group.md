# Opeenvolgend toewijzen aan gebruiker/groep

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-61e424b9ad8c-nl.png" alt="Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface." width="563"><figcaption><p>Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

## **Doel**

De workflow-kaart "**Wijs het document opeenvolgend toe aan de gebruiker/groep op basis van de beslissingstabel**" wijst documenten dynamisch toe aan een gebruiker of een groep, afhankelijk van de evaluatie van de decision table. Dit zorgt ervoor dat documenten op de juiste manier worden gerouteerd op basis van vooraf gedefinieerde regels.

## **Onderdelen van de kaart**

1. **Prioriteit (waarde)**
   * **Beschrijving**: Geeft het prioriteitsniveau voor toewijzingen op, waarbij lagere getallen een hogere prioriteit vertegenwoordigen.
   * **Details**: Een numeriek invoerveld waarin de prioriteitswaarde kan worden ingesteld om de toewijzingsvolgorde te bepalen.

## **Functionaliteit**

* **Besluittabel-evaluatie**:\
  De decision table evalueert vooraf gedefinieerde voorwaarden om te beslissen of het document aan een gebruiker of een groep wordt toegewezen.
* **Documenttoewijzing**:
  * Als de decision table een gebruiker retourneert, wordt het document rechtstreeks aan die gebruiker toegewezen.
  * Als de decision table een groep retourneert, wordt het document sequentieel aan de groep toegewezen, met inachtneming van de opgegeven prioriteitswaarde.

## **Opzet en configuratie**

1. Voeg de kaart **Wijs het document opeenvolgend toe** toe aan uw workflow.
2. Configureer het veld **Prioriteit (waarde)**:
   * Voer een numerieke waarde in om de toewijzingsprioriteit in te stellen.
3. Sla op en activeer de workflow om de configuratie toe te passen.

## **Conclusie**

De workflow-kaart "**Wijs het document opeenvolgend toe aan de gebruiker/groep op basis van de beslissingstabel**" zorgt voor efficiënte en dynamische documentroutering. Door beslislogica en prioriteitswaarden te benutten, faciliteert de kaart een nauwkeurige toewijzing aan een gebruiker of een groep, wat documentworkflows stroomlijnt.

<!-- workflow-card-practical-example-20261021 -->

## Praktisch voorbeeld

**Wanneer gebruiken:** Gebruik een beslissingstabel om een documentontvanger met prioriteit te selecteren.

**Configuratie:** Configureer een overeenkomende demo-beslissingstabelregel die de beoogde gebruiker of groep retourneert en selecteer vervolgens die tabel op de kaart.

**Verwacht resultaat en tegenvoorbeeld:** De geretourneerde verantwoordelijke wordt gebruikt voor opeenvolgende documenttoewijzing. Als er geen passende retourwaarde is, mag u niet uitgaan van een standaard verantwoordelijke; inspecteer het resultaat en het geconfigureerde fallback-gedrag van deze versie.

Dit is een illustratieve configuratie en een verwacht resultaat. Gebruik velden, gebruikers en groepen die in uw testorganisatie zijn geconfigureerd; het is geen bewering dat dit voorbeeld is uitgevoerd.
