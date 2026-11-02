# Frankrijk: erkende platforms en PEPPOL voor elektronische facturatie

## Erkend platform vereist voor binnenlandse B2B-facturen

Voor binnenlandse B2B-transacties tussen Franse btw-plichtige ondernemingen die onder de hervorming vallen, verloopt de uitwisseling van elektronische facturen via een erkend platform (plateforme agréée, **PA**, voorheen **PDP**). Het openbare portaal **PPF** is geen alternatief platform voor factuuruitwisseling; het vervult functies voor het centrale adresregister en de verzameling van gegevens. PEPPOL kan het transport en de interoperabiliteit ondersteunen, maar vervangt het vereiste erkende platform niet. Zie de [officiële informatie over erkende platforms](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees). De onderstaande oudere verwijzingen naar [vereisten](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform) en het [overheidsportaal](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html) beschrijven eerdere versies van de hervorming en zijn geen actuele implementatie-instructies.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt=""><figcaption></figcaption></figure>

### Historische technische context van het dienstenaanbod

De volgende beschrijving en de oorspronkelijke diagrammen documenteren een eerdere technische opzet rond het PPF. Ze blijven als historische context behouden. Verwijzingen naar factuuruitwisseling via het PPF beschrijven niet de huidige rolverdeling. In die eerdere opzet bood de API-modus toegang tot functies vanuit de bestaande IT-systemen van partners, met twee integratiemethoden:

### ·       Integratie in informatiesystemen (IS):

API's werden rechtstreeks geïntegreerd in informatiesystemen of beheersoftware van verzenders en ontvangers van facturen of hun digitaliseringsdienstverleners (OD's). Zo konden gebruikers vanuit hun gebruikelijke interne IT-tools of de tools van hun OD toegang krijgen tot de functies van de oplossing en de bijbehorende updates.

API's konden ook worden geïntegreerd in de informatiesystemen van PDP's om meer flexibiliteit te bieden dan de EDI-modus. Sommige API's waren specifiek voor deze platforms bedoeld.

### ·       Integratie in software van derden:

Softwareleveranciers konden software op basis van de API's aanbieden. Afhankelijk van de gekozen werkwijze werd de verbinding door de leverancier of door de klant tijdens de installatie of uitrol in het eigen informatiesysteem ingericht. Deze software voegde in de eerdere opzet een communicatielaag met het PPF toe aan het informatiesysteem van de klant.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt=""><figcaption></figcaption></figure>

## PEPPOL als transport- en interoperabiliteitslaag

PEPPOL kan erkende platforms ondersteunen bij transport en interoperabiliteit. Het vormt geen afzonderlijke route die het gebruik van een PA vervangt. Het PPF richt zich op het centrale adresregister en de verzameling van gegevens; het is geen alternatief voor factuuruitwisseling via een erkend platform. De oudere toelichtingen over de [onderlinge verbinding](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html) van platforms, de uitwisseling van [facturen](https://nymus.be/fr/facturation-electronique-en-france/) en het gebruik van [PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) voor die [uitwisseling](https://nymus.be/fr/facturation-electronique-en-france/) blijven achtergrondinformatie. Raadpleeg voor de huidige rolverdeling de [officiële uitleg over erkende platforms](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees).

\


<figure><img src="../../.gitbook/assets/Picture 2.png" alt=""><figcaption></figcaption></figure>

## Historische technische context: aansluiting van een hub

In de eerdere opzet bood de hub klanten een web- of applicatieoplossing om API-aanroepen uit te voeren. **De hub voerde daarbij de API-aanroepen namens al zijn klanten uit**. Elke partner had een technisch account nodig, terwijl alleen de hub een toepassing onder PISTE en een verbinding met het PPF nodig had. Dit beschrijft de historische technische context van het onderstaande diagram, geen actuele instructie om facturen via het PPF uit te wisselen.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt=""><figcaption></figcaption></figure>



Actueel tijdpad: ondernemingen binnen de reikwijdte van de hervorming moeten vanaf **1 september 2026** elektronische facturen kunnen ontvangen. Voor grote ondernemingen en ondernemingen van middelgrote omvang (GE/ETI) beginnen de uitgifteplicht en e-reporting op die datum; voor kleine en middelgrote ondernemingen en micro-ondernemingen (PME/micro) op **1 september 2027**. Zie het [officiële tijdpad](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) en de [toelichting van het ministerie](https://www.senat.fr/questions/base/2026/qSEQ260107185.html). De oorspronkelijke diagrammen hieronder blijven bewaard als historische technische context. Ze vormen geen actuele instructies of garantie dat een integratie aan alle wettelijke verplichtingen voldoet.

<div><figure><img src="../../.gitbook/assets/Picture 3.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Picture 4.png" alt=""><figcaption></figcaption></figure></div>
