# Probleemoplossing

## Ik kan Testing niet vinden in Instellingen

De pagina wordt alleen aan organisatiebeheerders getoond. Vraag het aan een organisatiebeheerder van uw organisatie.

## De pagina meldt dat Testing is uitgeschakeld

Een organisatiebeheerder moet bovenaan de pagina **Schakel Testing in voor de organisatie** inschakelen.
Totdat dat is gebeurd, wordt er niets uitgevoerd, ook niet vanuit een AI-assistent of van buitenaf.

## Mijn run is mislukt

Open het logboek in het tabblad **Logboek** en kijk naar de eerste mislukte stap en de foutcode ervan:

| U ziet | Betekent meestal | Wat te doen |
|---|---|---|
| Een element is niet gevonden of niet zichtbaar | De pagina ziet er in uw organisatie anders uit, of laadt traag | Open de pagina zelf en controleer hem; pas uw eigen sjabloon aan, of controleer de invoerwaarden |
| Een veld of status komt niet overeen | Het document heeft een andere waarde dan de invoer verwacht | Controleer het document; corrigeer de verwachte waarde in de invoer |
| De pagina kon niet worden geopend | Verkeerde document-ID, of geen toestemming | Controleer de ID in de invoer en de rechten van de gebruiker die het tabblad heeft gestart |
| Time-out | De stap of de hele test duurde te lang | Voer de test opnieuw uit; als het zich herhaalt, controleer dan de prestaties van de pagina |
| Geblokkeerd door de omgeving | De test schrijft gegevens in een klantomgeving | Bevestig de start, of voer de test uit in een testomgeving |

## Mijn run is "Geblokkeerd"

De run kon niet worden beoordeeld: sommige stappen zijn overgeslagen (bijvoorbeeld een screenshotstap, die de browser niet kan maken)
of er ontbreekt een bevestiging. Een geblokkeerde run wordt nooit als geslaagd geteld. Verwijder de stap uit uw eigen sjabloon, of
start de run opnieuw met de bevestiging.

## "Registreer een browsersessie om te starten" / geen enkel tabblad accepteert starts

Starts vanuit een AI-assistent of van buitenaf vereisen een browsertabblad waarop **Starten op afstand toestaan** is ingeschakeld. Open
de pagina Invoer in een browsertabblad dat open blijft, schakel de optie in en gebruik het sessie-ID ervan. Een herlading beëindigt de registratie.

## De run is gestopt of toont Geannuleerd / Niet afleverbaar

Het tabblad dat de test uitvoerde, is opnieuw geladen, gesloten of heeft de verbinding verloren, of er heeft geen tabblad op tijd gereageerd. Houd het tabblad open
en op de voorgrond totdat de run eindigt en start daarna opnieuw. Een test met een stap **Laad pagina opnieuw** eindigt ook zo als de pagina niet binnen ongeveer twee minuten terugkomt
(zie [Opnieuw laden en hervatten](reload-and-resume.md)).

## "Playwright-sjablonen kunnen hier nog niet worden gestart"

Sjablonen waarvan **Uitgevoerd door** **Playwright** is, worden door uw testautomatisering uitgevoerd. U kunt er invoer voor opslaan, maar u
kunt ze niet vanaf deze pagina starten.

## Ik kan een sjabloon niet verwijderen

Alleen de eigen sjablonen van uw organisatie (**aangepast**) kunnen worden verwijderd. Ingebouwde sjablonen en standaardsjablonen niet; gebruik
**Een kopie bewerken** om uw eigen versie te krijgen.
