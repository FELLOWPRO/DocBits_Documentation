# PWA Cache Status

De pagina **PWA Cache Status** is een diagnostisch hulpmiddel voor beheerders die een **leeg scherm** of een app die verouderde bestanden laadt, onderzoeken. DocBits kan Service Workers en browsercaches gebruiken om applicatiebestanden te laden. Deze pagina toont de actuele diagnostische momentopname van de browser en biedt onderhoudsacties voor cachegerelateerde problemen. De momentopname alleen bewijst niet wat de oorzaak van een leeg scherm is en bewijst ook niet dat een PWA-installatie gezond is.

Dit diagnosescherm is momenteel alleen in het Engels beschikbaar. De labels die hieronder worden genoemd, staan daarom precies zoals ze in de app verschijnen.

## Hoe u de pagina opent

De pagina is bedoeld voor beheerders en staat niet in de zijbalk. U opent hem op twee manieren:

* Open de URL rechtstreeks: `https://app.docbits.com/debug/pwa-cache-status`
* Druk vanuit de hoofdapplicatie (bijvoorbeeld het Dashboard) op <kbd>Ctrl</kbd> + <kbd>K</kbd> (of <kbd>Cmd</kbd> + <kbd>K</kbd> op macOS) om [Globale Snelzoek](../global-quick-search.md) te openen, typ "PWA Cache Status" en druk op <kbd>Enter</kbd> op dat resultaat.

<figure><img src="../../../.gitbook/assets/dbdc-993-pwa-cache-status-page-nl-20261111.png" alt="Diagnosepagina PWA Cache met de status van de Service Worker, versiegegevens, de lijst met gecachte items en de vier actieknoppen"><figcaption><p>De diagnosepagina PWA Cache in een Nederlandse sessie: statuspanelen, alle vier acties en de waarschuwing voor foutopsporing. De teksten van deze diagnosepagina blijven in het Engels, omdat de applicatie ze nog niet vertaalt. Versiewaarden en aantallen registraties en caches verschillen per browser en omgeving.</p></figcaption></figure>

## De statuspanelen lezen

* **Service Worker** — **Available: Yes/No** geeft aan of de browser de Service Worker-API ondersteunt. **Registrations** telt de registraties op de huidige origin in de browser. Deze waarden bewijzen niet dat DocBits als PWA is geïnstalleerd, dat een worker deze pagina beheert of dat de installatie gezond is.
* **Version** — **Current** is de app-versie van de geladen build. **Stored** is de basisversie die in de browser voor deze app-bundel is opgeslagen; het is geen overzicht van de versies van alle gecachte bestanden. **Mismatch: Yes** verschijnt alleen als beide waarden bekend zijn en van elkaar verschillen. Een lege huidige versie of **Stored: Not set** bewijst niet dat de caches actueel zijn, ook niet als **Mismatch** _No_ toont.
* **Cached Items** — toont de namen van alle CacheStorage-caches op de huidige origin, dus niet de afzonderlijke bestanden en niet alleen de caches van DocBits. Het aantal is het aantal cachenamen. _No caches found_ betekent dat deze momentopname geen CacheStorage-cachenamen bevat; over andere browseropslag of de gewone HTTP-cache van de browser zegt dat niets.

Lege waarden of een aantal van nul kunnen ook het gevolg zijn van niet-beschikbare API's of mislukte diagnostische uitlezingen; ze bewijzen niet dat de browser geen gecachte gegevens heeft.

Een origin is de combinatie van protocol, host en poort. Deze hulpmiddelen werken op alle caches en registraties van die origin, ook op die van andere applicatiepaden.

## De vier acties

| Actie | Wat de actie doet |
|---|---|
| **Reload Page** | Voert een normale herlaadactie van de pagina uit. De actie wist geen caches en omzeilt geen Service Worker. |
| **Clear All Caches** | Probeert alle CacheStorage-caches op deze origin te verwijderen en vernieuwt de diagnostische momentopname. Bij latere laadacties moeten bestanden mogelijk opnieuw worden opgehaald. |
| **Unregister Service Workers** | Probeert alle Service Worker-registraties op deze origin af te melden en vernieuwt de diagnostische momentopname. Controleer de resulterende status voordat u aanneemt dat het opschonen is gelukt. |
| **Emergency Cleanup** | Probeert caches te verwijderen en Service Workers af te melden in één stap en plant daarna een normale herlaadactie van de pagina. De actie probeert de huidige basisversie alleen op te slaan nadat beide opschoonstappen succes melden en er een huidige app-versie beschikbaar is. Een fout in de browseropslag kan het opslaan van de basisversie alsnog verhinderen. Als een van beide opschoonstappen mislukt, blijft de vorige basisversie behouden. |

⚠️ **Waarschuwing:** Deze hulpmiddelen zijn alleen voor foutopsporing. Gebruik **Emergency Cleanup** alleen bij een leeg scherm. Het verwijderen van caches kan gecachte gegevens en offlinebronnen van applicaties op dezelfde origin verwijderen; ga er niet van uit dat caches alleen wegwerpbare app-bestanden bevatten. De volgende laadactie kan langzamer zijn of een werkende netwerkverbinding vereisen. Een succesmelding of een geplande herlaadactie op zich bewijst niet dat elke opschoonactie is gelukt.

## Typische probleemoplossing

1. Open de pagina PWA Cache Status en noteer **Current**, **Stored**, **Mismatch**, het aantal registraties en de cachenamen. Een mismatch is een diagnostische aanwijzing, geen volledige diagnose.
2. Probeer, als dat bij uw onderzoek past, **Reload Page**. Dit is een gewone herlaadactie die nog steeds gecachte antwoorden kan gebruiken.
3. Als het scherm leeg blijft, controleer dan de origin en de waarschuwing hierboven voordat u **Clear All Caches** gebruikt, herlaad daarna de pagina en bekijk de status opnieuw.
4. Gebruik **Emergency Cleanup** alleen bij een aanhoudend leeg scherm. De actie probeert beide opschoonacties uit en plant een herlaadactie; de basisversie verandert alleen onder de hierboven beschreven succesvoorwaarden. Mislukt het opschonen, behoud dan de vorige basisversie als aanwijzing en neem contact op met de ondersteuning in plaats van aan te nemen dat het probleem is opgelost.
5. Helpt dit alles niet, verzamel dan diagnostische gegevens met de **Debugverzamelaar** (<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd>) en stuur ze naar de ondersteuning — zie [Zo gebruikt u de Debugverzamelaar](../debug-collector.md). Controleer de diagnostische gegevens op vertrouwelijke informatie voordat u ze deelt.
