# Workflow exportkaarten en documentstatus

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-11f244132c25-nl.png" alt="Beschikbare kaarten in de geselecteerde categorie. Vul de velden vóór gebruik in. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface."><figcaption><p>Beschikbare kaarten in de geselecteerde categorie. Vul de velden vóór gebruik in. Sommige labels van deze versie zijn in de interface nog niet of onjuist vertaald. De uitleg op deze pagina gebruikt de juiste termen; de afbeelding toont de werkelijke interface.</p></figcaption></figure>

Kies of u onmiddellijk wilt exporteren of een configuratie in de wachtrij wilt zetten voor de definitieve export aan het einde van de run. Deze keuzes staan ​​los van de status die het document moet hebben na een succesvolle export.

| Kaart | Wanneer de export wordt uitgevoerd | Belangrijke instellingen |
| --- | --- | --- |
| Exporteren met validatie starten (`EXPORT`) | Start de export met behulp van de geconfigureerde exportinstellingen van het document. | Validatie en vanaf v4 Status na export. |
| Exporteren met exportconfiguratie (`ACTION_EXPORT_WITH`) | Exporteert met behulp van de geselecteerde configuratie tijdens kaartuitvoering. | Configuratie exporteren, taken in behandeling negeren en, vanaf v3, Status na export. |
| Wachtrijexport met configuratie (`ACTION_EXPORT_WITH_CONFIG_DEFERRED`) | Verzamelt de configuratie voor de uiteindelijke export aan het einde van de run. Het toevoegen van een exportverzoek aan de wachtrij bewijst niet dat de uiteindelijke export is geslaagd. | Configuratie exporteren, taken in behandeling negeren en, vanaf v3, Status na export. |
| Alternatieve export (`ACTION_ALTERNATE_EXPORT`) | Gebruikt de alternatieve exportroute die op de kaart staat gedocumenteerd. | Ga er niet vanuit dat deze dezelfde versie- of statusopties heeft als de drie bovenstaande kaarten. |

## Status na export

| Waarde | Dat betekent na een succesvolle export | Typisch gebruik |
| --- | --- | --- |
| `finished` | Geëxporteerd en gesloten. | De verwerking is voltooid. |
| `exported` | Geëxporteerd maar blijft open voor verdere verwerking. | Goedkeuring of een andere workflow moet nog volgen. |

Start Export v4, Exporteren met exportconfiguratie v3 en export in wachtrij v3 bieden deze selectie. Eerdere versies behouden `finished`. Een ontbrekende selectie valt terug naar `finished` en wordt geregistreerd; een ongeldige waarde wordt vóór de export afgewezen. Een opgeslagen oude kaart krijgt het nieuwe gedrag niet louter omdat er een nieuwe sjabloonversie bestaat. Inspecteer de kaartversie en test eventuele expliciete upgrades opnieuw.

De documentstatusvoorwaarden en Change Status bieden ook `exported` in releases die de bijbehorende statusupdate bevatten. Alleen het wijzigen van de status voert geen export uit. Gebruik het exportresultaat en de logboeken om vast te stellen dat de gegevens daadwerkelijk hun bestemming hebben bereikt.

## Onmiddellijke export met configuratie

1. Voeg de kaart toe onder Dan en selecteer een geldige exportconfiguratie.
2. Kies of u openstaande taken wilt negeren. Houd dit uitgeschakeld als taken de export moeten blokkeren.
3. Selecteer op v3 bewust `finished` of `exported`.
4. Test met een document in een toegestane verwerkingsstatus en inspecteer vervolgens het kaartresultaat en de bestemming.

Als lopende taken de export verhinderen, registreert de kaart een geweigerde export. Los de taken op en regel de beoogde workflow-trigger of probeer het opnieuw. Deze kaart belooft niet te wachten en automatisch te hervatten. Een time-out bewijst ook niet dat het externe systeem niets heeft gedaan; inspecteer de exportgeschiedenis voordat u een bewerking herhaalt die duplicaten kan veroorzaken.

## Wachtrijexport met configuratie

Voeg deze kaart toe wanneer de export moet worden verzameld voor de laatste stap van de run. Selecteer de configuratie, het beleid voor openstaande taken en de resultaatstatus. De kaart registreert de gevraagde configuratie; bekijk het uiteindelijke exportresultaat afzonderlijk. Het bericht dat de aanvraag in de wachtrij bevestigt, is geen bevestiging van een boekhoudkundige boeking.

Selecteer bijvoorbeeld `exported` wanneer een succesvolle export het document beschikbaar moet laten voor latere goedkeuring. Selecteer `finished` als er geen verdere verwerking vereist is. Controleer opnieuw de eindstatus en de exportbestemming.

## Vereiste controles

Test een geldige configuratie, een ontbrekende configuratie, openstaande taken met beide instellingen en beide resultaatstatussen. Test de versie die al in een bestaande workflow wordt gebruikt voordat u deze wijzigt. Controleer voor een export in de wachtrij de uiteindelijke uitvoering; voor een onmiddellijke export verifieert u het eigen resultaat. Bekijk [Workflowlogboeken](../workflow-logs.md) en verwar een overgeslagen kaart niet met succes.

<!-- workflow-card-complete-example-20261021 action_export_with_config_deferred -->

### Voorbeeld van uitgestelde export

**Configuratie:** Kies op v3 testconfiguratie `DEMO_EXPORT`, laat 'In behandeling zijnde taken negeren' uitgeschakeld en selecteer `exported` als de status na het exporteren. Plaats de kaart in de beoogde gevalideerde route.

**Verwacht resultaat en tegenvoorbeeld:** De kaart verzamelt een exportverzoek voor het einde van de uitvoering van de werkstroom. Alleen bij een succesvolle definitieve uitvoering wordt vastgesteld dat de bestemming de gegevens heeft ontvangen en dat het document open blijft als `exported`. Het succes van een in de wachtrij geplaatste kaart alleen is geen bewijs van export; een onopgeloste blokkeringstaak mag niet als levering worden beschouwd.

Dit is een illustratieve testconfiguratie en verwachte uitkomst; het werd niet uitgevoerd. Gebruik gegevens en ontvangers die in uw testorganisatie zijn geconfigureerd.
