# PO-vergelijkingen: richting, tolerantie en kaartversies

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-72e8f3204ac8-nl.png" alt="Beschikbare kaarten in de geselecteerde categorie. Vul de velden vóór gebruik in. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface."><figcaption><p>Beschikbare kaarten in de geselecteerde categorie. Vul de velden vóór gebruik in. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

PO-vergelijkingskaarten vergelijken een gekozen kant met een referentiekant. De referentie bepaalt de basis voor een procentuele tolerantie. Voltooi eerst de matching van inkooporders en selecteer vervolgens de vergelijking, operator, Any/All en tolerantie die door de specifieke kaart wordt gevraagd.

## Vergelijkingsrichtingen

| Opgeslagen optie | Vergeleken kant | Referentiezijde |
| --- | --- | --- |
| `po_document` | Aankooporder | Documenteren |
| `received_document` | Ontvangen gegevens | Documenteren |
| `po_received` | Aankooporder | Ontvangen gegevens |
| `document_po` | Documenteren | Aankooporder |
| `document_received` | Documenteren | Ontvangen gegevens |
| `received_po` | Ontvangen gegevens | Aankooporder |

De ontvangen zijde wordt afgeleid van de gekoppelde inkoopordergegevens. Een ontvangen vergelijking op de eenheidsprijskaart kan hoeveelheden gebruiken om een ​​vergelijkbaar bedrag af te leiden; het is geen directe vergelijking van een hoeveelheid met een valutaprijs. Gebruik de waarden die op die kaart in het logboek zijn geregistreerd bij het controleren van de berekening.

## Waarom richting belangrijk is

Voor een referentie van `100` en een vergeleken waarde van `110` komt een procentuele tolerantie van `5` overeen met `5` rond de referentie. Als het document de referentie is en de waarde ervan bewerkbaar is, verandert het wijzigen van het document ook de tolerantiebasis. Kies de referentie bewust, vooral voor automatische goedkeuring.

Door de zijden om te keren, worden de volgorde-operatoren omgedraaid: `>` wordt `<`, `>=` wordt `<=`, en omgekeerd. Gelijkheid en ongelijkheid behouden hun betekenis. Rijd een operator niet achteruit zonder ook de gekozen zijden te inspecteren.

Releases die de vergelijkingsmigratie bevatten, verplaatsen de getroffen opgeslagen kaarten van `po_document` naar `document_po` en van `received_document` naar `document_received`, terwijl de volgorde-operator wordt omgekeerd. De betrokken versies zijn hoeveelheidstolerantie v4, orderbevestiging-naar-PO v4 en eenheidsprijs v4/v5. Het gecombineerde verschil in prijs en hoeveelheid is uitgesloten van die migratie van opgeslagen kaarten. Inspecteer de opgeslagen configuratie en test het bedrijfsresultaat na een release; draai het niet nog een tweede keer handmatig om.

## Kaartversies met eenheidsprijs

| Versie | Configuratie |
| --- | --- |
| v3 | Maakt gebruik van het eerdere vergelijkingsgedrag. Ga er niet van uit dat hierdoor de nieuwere richtings- en tolerantievelden zichtbaar worden. |
| v4 | Voegt de selectie aan de vergelijkingskant toe. |
| v5 | Omvat Alle/Alles, operator, tolerantiebedrag, tolerantietype en selectie aan de vergelijkingskant. |

Kies een absolute tolerantie voor een vast bedrag en een procentuele tolerantie voor een afwijking ten opzichte van de geselecteerde referentie. Gebruik de operator die door de kaart wordt aangeboden; exacte gelijkheid en binnen tolerantie blijven, zijn verschillende beslissingen. Er bestaat geen universele zakelijke tolerantie die geschikt is voor iedere leverancier of elk documenttype.

## Verificatie voorbeeld

1. Gebruik een overeenkomende inkooporderreferentie van `100` en documentwaarde `110`.
2. Selecteer Document naar inkooporder, een vergelijking binnen de toleranties indien aangeboden, en `5` procent. Verwacht een out-of-band vergelijking.
3. Test de exacte tolerantiegrens, waarden aan beide kanten en een ontbrekende overeenkomende PO.
4. Als er meerdere regels zijn, verifieer dan Any versus All met behulp van één passerende en één falende regel.
5. Inspecteer de vergeleken waarden, geselecteerde zijden, operator en tolerantie van het logboek en verifieer vervolgens de resulterende workflowtak.

Een ongeëvenaarde inkooporder, een niet-numerieke waarde en een valse bedrijfsvoorwaarde zijn verschillende resultaten. Beschouw ontbrekende gegevens niet als een succesvolle match. Voor kosten gebruikt u [Alle / Alle kosten](../and/compare-with-purchase-order/any-all-charges.md), waarin het gedrag van ontbrekende kosten en v2/v3 afzonderlijk wordt uitgelegd.

Ga verder met de [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md) en de individuele kaartreferentie voor de resterende velden.
