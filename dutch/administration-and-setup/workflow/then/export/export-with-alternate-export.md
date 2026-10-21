# Exporteren met alternatieve export

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-379e4b3a5355-nl.png" alt="Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld." width="563"><figcaption><p>Kaartvelden in de getoonde versie. De velden zijn nog niet ingevuld.</p></figcaption></figure>

## Wanneer moet u deze kaart gebruiken?

Gebruik deze actie Dan voor de alternatieve export die is geconfigureerd voor het huidige documenttype. Configureer en valideer die route voordat u de actie toevoegt.

## Configuratie komt van het documenttype

De kaart heeft geen exportconfiguratiekiezer. Het leest of alternatieve export is ingeschakeld, de alternatieve exportconfiguratie en de status na export van de documenttype-instellingen. Intern zijn dit `DOC_ALTERNATE_EXPORT_SETTING`, `DOC_ALTERNATE_EXPORT_EXPORT_CONFIG` en `DOC_ALTERNATE_EXPORT_STATUS`.

Een expliciet uitgeschakelde alternatieve export levert een mislukte voorwaarde op. Ontbrekende activeringsgegevens, configuratie of resultaatstatus worden gerapporteerd in plaats van stilzwijgend de standaardroute te vervangen. Het exportverzoek controleert openstaande taken.

## Controleer het resultaat

Inspecteer het kaartlogboek, de exportgeschiedenis, de documentstatus en de geautoriseerde testbestemming. Een verzoek, time-out of statuswijziging alleen betekent niet dat de gegevens de bestemming hebben bereikt. Controleer de exportgeschiedenis voordat u een bewerking opnieuw probeert uit te voeren waarbij duplicaten kunnen ontstaan.

<!-- workflow-card-complete-example-20261021 action_alternate_export -->

### Alternatief exportvoorbeeld

**Configuratie:** Bereid synthetisch documenttype voor `DEMO_INVOICE` met alternatieve export ingeschakeld, een geautoriseerde testexportconfiguratie en de gewenste resultaatstatus in de documenttype-instellingen. Voeg deze toe Dan actie na de vereiste controles. Deze kaart leest die instellingen; het biedt geen selector voor exportconfiguratie.

**Verwacht resultaat en tegenvoorbeeld:** De actieverzoeken worden via die alternatieve configuratie geëxporteerd en controleren openstaande taken. Controleer het exportresultaat en de testbestemming afzonderlijk. Het uitschakelen van alternatieve export veroorzaakt een mislukte toestand; een ontbrekende activeringsinstelling of -configuratie is geen succesvolle export. Voer dit voorbeeld niet uit op een boekhoudbestemming.

Dit is een illustratieve testconfiguratie en verwachte uitkomst; het werd niet uitgevoerd. Gebruik gegevens en ontvangers die in uw testorganisatie zijn geconfigureerd.
