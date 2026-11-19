# Frankrijk: erkende platforms en PEPPOL voor elektronische facturatie

## Huidige regels en tijdpad

Voor binnenlandse B2B-facturen in Frankrijk die binnen de reikwijdte van de hervorming vallen tussen btw-plichtige ondernemingen, moet de uitwisseling van facturen via een **erkend platform (plateforme agréée, PA; voorheen PDP)** verlopen. Het **openbare facturatieportaal (PPF, Portail public de facturation)** verzorgt het openbare register en het verzamelen van fiscale gegevens; het is voor deze transacties geen alternatief platform voor factuuruitwisseling.

* **1 september 2026:** Alle ondernemingen binnen de reikwijdte moeten elektronische facturen kunnen ontvangen. Grote ondernemingen (GE) en ondernemingen van middelgrote omvang (ETI) moeten vanaf die datum ook elektronische facturen uitgeven en aan hun e-reportingverplichtingen voldoen.
* **1 september 2027:** De verplichtingen voor uitgifte en e-reporting gelden voor kleine en middelgrote ondernemingen (PME) en micro-ondernemingen.

Welke verplichting geldt, hangt af van de reikwijdte van de transactie en van de categorie van de onderneming. Raadpleeg de officiële [informatie over erkende platforms](https://www.impots.gouv.fr/facturation-electronique-et-plateformes-agreees), het [tijdpad voor de invoering](https://www.impots.gouv.fr/professionnel/questions/partir-de-quand-suis-je-concerne-par-la-reforme-de-la-facturation) en de [toelichting van het ministerie](https://www.senat.fr/questions/base/2026/qSEQ260107185.html).

## PEPPOL en interoperabiliteit

PEPPOL kan zorgen voor transport en interoperabiliteit tussen aangesloten systemen en platforms. Het gebruik van PEPPOL vervangt niet de verplichting om voor factuuruitwisseling binnen het Franse mandaat een PA te gebruiken. Beschouw een PEPPOL-aansluiting op zichzelf niet als bewijs dat aan de Franse uitwisselings- en rapportageverplichtingen is voldaan.

Voor de formatcatalogus van DocBits zie [Overzicht van standaarden voor elektronische facturen](../../administration-and-setup/settings/global-settings/document-types/edi/currently-supported-e-invoice-standards/README.md).

## Historische technische context

De zes diagrammen en de onderstaande API-beschrijvingen zijn afkomstig uit eerder PPF-/PDP-materiaal en blijven bewaard als historische technische context. Ze gebruiken de terminologie en de architectuur van toen; ze beschrijven geen actuele mogelijkheid om voorgeschreven B2B-facturen via het PPF uit te wisselen. Controleer de actuele specificaties van de PA en van de openbare diensten voordat u een integratie implementeert.

<figure><img src="../../.gitbook/assets/Picture 1.png" alt="Diagram van de levenscyclus van Franse e-facturatie over voorbereiding, ontvangst, validatie en betaling met statussen voor leverancier en koper"><figcaption><p>Historisch levenscyclusdiagram: voorbereiding en uitgifte, ontvangst, validatie/retour en betaling, met de labels voor de status van leverancier en koper in elke fase.</p></figcaption></figure>

### Historisch API-servicemodel

Het eerdere API-model beschreef de toegang tot beschikbare functies vanuit de IT-hulpmiddelen die partnerorganisaties inzetten, via twee integratiemethoden:

* **Informatiesystemen (IS):** API's werden beschreven als onderdeel van de systemen van factuurverzenders, ontvangers of hun dematerialiseringsoperatoren (OD's). Sommige API's waren bedoeld voor PDP-systemen en boden een alternatief voor EDI-integratie.
* **Software van derden:** Softwareleveranciers konden een communicatielaag aan klantsystemen toevoegen. Eerdere verwijzingen naar een verbinding met het PPF horen bij dat historische model en zijn geen actuele route voor factuuruitwisseling.

<figure><img src="../../.gitbook/assets/Picture 6.png" alt="Diagram van verzender en ontvanger die facturen uitwisselen via OD-PDP-serviceportalen en het PPF met gegevenscontrole en herstel"><figcaption><p>Historisch interconnectiediagram: verzender en ontvanger zijn verbonden via software van derden, serviceportalen en OD-/PDP-blokken rond het PPF-blok voor gegevenscontrole en herstel.</p></figcaption></figure>

### Historisch interconnectiediagram

Dit diagram illustreert de eerdere context van de koppeling tussen platforms. De actuele implementatie moet de vereisten van de PA volgen; hier wordt niet gesteld dat elke uitwisseling via één enkel transportnetwerk moet verlopen.

<figure><img src="../../.gitbook/assets/Picture 2.png" alt="Diagram van flow-, factuur- en factuurgegevenscontroles: inzendingen van leveranciers doorlopen technische, applicatie- en functionele controles met afwijzingen"><figcaption><p>Historisch controlediagram: technische, applicatie- en functionele dan wel bedrijfsmatige controles voor handmatige, API- en EDI-inzendingen, naast de uitkomsten ontoelaatbaar, afgewezen en geweigerd.</p></figcaption></figure>

### Historische hub-aansluiting

Het eerdere hub-model beschreef een web- of applicatieoplossing waarbij **de hub API-aanroepen uitvoerde namens zijn klanten**. Het noemde een technisch account voor elke partner en één toepassing onder PISTE plus een PPF-verbinding voor de hub. Dit zijn historische architectuurdetails, geen geverifieerde actuele integratieprocedure.

<figure><img src="../../.gitbook/assets/Picture 5.png" alt="Diagram van partners met technische accounts die via één hub zijn verbonden met één toepassing onder PISTE en één verbinding"><figcaption><p>Historisch hubdiagram: partners met technische accounts zijn via één hub verbonden met één toepassing onder PISTE en één verbinding.</p></figcaption></figure>

### Historische bronnen

Het eerdere materiaal verwees naar [het toenmalige tijdpad en het juridische overzicht](https://www.ey.com/en_gl/technical/tax-alerts/france-revises-schedule-for-adopting-e-invoicing-reform), [de specificaties van 2022](https://www.avalara.com/blog/en/europe/2022/09/france-publishes-updated-specifications-for-e-invoicing-and-e-reporting.html), [een overzicht van de hervorming uit 2025](https://www.avalara.com/blog/en/europe/2025/01/e-invoicing-reform-france.html), [achtergrond over de koppeling tussen platforms](https://nymus.be/fr/facturation-electronique-en-france/), [achtergrond over PEPPOL](https://edicomgroup.com/blog/status-of-b2b-electronic-invoicing-in-france) en [achtergrond over de uitwisseling](https://nymus.be/fr/facturation-electronique-en-france/). Deze links en de overige diagrammen blijven bewaard als historische context. Gebruik voor actuele verplichtingen de hierboven genoemde officiële bronnen, inclusief het onderscheid tussen factuuruitwisseling via een PA en de openbare functies van het PPF. De eerdere verwijzing naar artikel 91 van de Financieringswet 2024 vormt geen grondslag voor een actuele mogelijkheid tot uitwisseling via het PPF.

<figure><img src="../../.gitbook/assets/Picture 3.png" alt="Stroomschema van het uitgifteproces van EDI-flow en API-ontvangst via flow-, applicatie- en functionele controles tot de uitgegeven factuur"><figcaption><p>Historisch stroomschema voor uitgifte: inkomende EDI- en API-flows doorlopen controles van de flow, de applicatie en de functie voordat factuurgegevens worden opgenomen; ook afwijzingspaden, de uitgaande flows 1 en 2 en levenscyclusmeldingen zijn weergegeven.</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/Picture 4.png" alt="Stroomschema van het ontvangstproces van EDI-flow en API-ontvangst via controles met afwijzing of weigering tot de beschikbaar gestelde factuur"><figcaption><p>Historisch stroomschema voor ontvangst: technische, applicatie- en functionele controles omvatten eigen bedrijfsregels met paden voor afwijzing of weigering; geaccepteerde gegevens leiden tot een ontvangen en beschikbaar gestelde factuur, naast ontvangerflow 2 en levenscyclusmeldingen.</p></figcaption></figure>
