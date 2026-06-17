# Beheerdersrechten

De rol van een beheerder is van cruciaal belang voor het beheren van IT-systemen, netwerken en digitale platforms binnen een organisatie. Een beheerder heeft uitgebreide rechten en verantwoordelijkheden waarmee hij verschillende aspecten van de technische infrastructuur kan aansturen en ervoor kan zorgen dat deze efficiënt en veilig functioneert. Hier zijn enkele van de belangrijkste verantwoordelijkheden van een beheerder:

* **Gebruikersbeheer:** Beheerders beheren gebruikersaccounts, toegangsrechten en machtigingen. Ze maken nieuwe gebruikersaccounts aan, kennen daaraan de benodigde machtigingen toe en beheren de toegangscontrole, zodat alleen geautoriseerde gebruikers toegang hebben tot bepaalde bronnen.
* **Beveiliging:** Beheerders zijn verantwoordelijk voor de beveiliging van IT-systemen om bescherming te bieden tegen gegevensverlies en ongeautoriseerde toegang.
* **Probleemoplossing en ondersteuning:** De beheerder is vaak het eerste aanspreekpunt voor technische problemen. Hij helpt gebruikers bij het opsporen en oplossen van problemen en zorgt ervoor dat het systeem soepel blijft draaien.

Naast deze verantwoordelijkheden hebben beheerders ook de taak om gevoelige instellingen te beheren en ervoor te zorgen dat systemen voldoen aan de nalevingsvereisten en aan de best practices voor informatiebeveiliging. Dit omvat het beheren van gevoelige gegevens, het configureren van toegangscontroles en machtigingen, en het monitoren en analyseren van systeemlogboeken om mogelijke beveiligingsrisico's te herkennen en aan te pakken.

## Admin vs System Admin

DocBits kent twee beheerdersrollen: **Admin** en **System Admin**. Ze klinken hetzelfde, maar doen verschillend werk. Hier is de eenvoudige uitleg.

### Admin — een persoon die uw organisatie beheert

Een **Admin** is een echte persoon in uw team die DocBits mag beheren. Admins kunnen:

* Alle onderdelen van **Instellingen** openen en aanpassen hoe uw organisatie werkt.
* Nieuwe gebruikers toevoegen, bewerken, in- of uitschakelen en bepalen wie er nog meer Admin wordt.
* Groepen, machtigingen, integraties en workflows instellen.

U kunt **zoveel Admins hebben als u nodig heeft**, en u kunt de Admin-rol op elk moment aan een gebruiker toekennen of ontnemen. De meeste beheerders in uw team zijn van dit type.

### System Admin — het account dat DocBits gebruikt om zelfstandig te werken

Een **System Admin** is **één speciaal account per organisatie** dat DocBits gebruikt voor acties die **automatisch gebeuren, zonder dat iemand op een knop klikt** — bijvoorbeeld wanneer documenten worden geïmporteerd vanuit e-mail, geëxporteerd naar een ander systeem of op de achtergrond worden doorgegeven door een gekoppelde dienst.

Zie het als het "robot"-account van de organisatie. Wanneer het systeem zelf iets doet, doet het dat **als de System Admin**, zodat deze automatische activiteit gemakkelijk te herkennen is en niet wordt verward met het werk van uw echte teamleden.

Een System Admin is op drie manieren bijzonder:

* **Het is altijd ook een Admin.** Door System Admin te kiezen krijgt dat account automatisch ook volledige Admin-rechten.
* **Er is er maar één per organisatie.** Zodra er een System Admin bestaat, kunt u geen andere gebruiker als System Admin aanmerken.
* **Het wordt alleen bij het aanmaken van de gebruiker ingesteld.** U bepaalt dit op het moment dat u de gebruiker toevoegt. Het **kan later niet meer worden in- of uitgeschakeld**.

> **Aanbeveling:** Maak hiervoor een speciaal account aan — bijvoorbeeld `system@your-company.com` — en merk dit aan als de System Admin. Op die manier verschijnt alles wat DocBits automatisch doet duidelijk als de **System Admin** in uw logboeken en documentgeschiedenis, gescheiden van uw echte gebruikers.

### In één oogopslag

| | Admin | System Admin |
|---|---|---|
| Volledige toegang om de organisatie te beheren | Ja | Ja |
| Hoeveel u er kunt hebben | Zoveel als u nodig heeft | Slechts één |
| Kan worden gewijzigd nadat de gebruiker is aangemaakt | Ja, op elk moment | Nee, alleen bij het aanmaken ingesteld |
| Gebruikt voor automatische acties op de achtergrond | Nee | Ja |
| Heeft altijd Admin-rechten | — | Ja |

## Best practices voor beveiliging

Beveiliging is een essentieel onderdeel van elke organisatie, vooral als het gaat om het beheren van gebruikersaccounts en toegangsrechten. Hier zijn enkele best practices om een veilig gebruikersbeheerproces te behouden:

* **Wachtwoorden regelmatig bijwerken:** Moedig gebruikers aan om hun wachtwoorden regelmatig bij te werken om hun accounts veilig te houden. Stel beleidsregels op voor wachtwoordcomplexiteit en vereis het gebruik van sterke wachtwoorden met een combinatie van letters, cijfers en speciale tekens.
* **Beheerdersacties monitoren:** Zet mechanismen in om beheerdersactiviteiten te monitoren en verdachte of ongebruikelijke activiteit te herkennen. Leg alle beheerdersacties vast, waaronder toegang tot gevoelige gegevens of instellingen, om verantwoording te waarborgen en mogelijke beveiligingslekken op te sporen.
* **Beperk het aantal beheerders:** Houd het aantal beheerders zo klein mogelijk en ken beheerdersrechten alleen toe aan wie ze echt nodig heeft. Door het aantal beheerders te beperken, verkleint u het risico op beveiligingslekken en wordt het eenvoudiger om gebruikersaccounts te beheren en te bewaken.
* **Tweefactorauthenticatie (2FA):** Implementeer tweefactorauthenticatie voor beheerdersaccounts om de beveiliging verder te verhogen. Hiermee wordt een extra beveiligingsstap toegevoegd die ervoor zorgt dat een aanvaller, zelfs als een wachtwoord wordt gecompromitteerd, geen ongeautoriseerde toegang tot het account krijgt.
* **Regelmatige beveiligingscontroles:** Voer regelmatig beveiligingscontroles en audits uit om mogelijke beveiligingslekken of zwakke plekken te herkennen en te verhelpen. Controleer de toegangsrechten en machtigingen van gebruikersaccounts om te waarborgen dat deze voldoen aan de actuele vereisten en best practices.
* **Training en bewustwording:** Train medewerkers en beheerders regelmatig in best practices voor beveiliging en bewustwording rond phishingaanvallen en andere cyberdreigingen. Maak ze bewust van het belang van beveiliging en moedig ze aan om verdachte activiteit te melden.

Door deze best practices toe te passen, kunnen organisaties de beveiliging van hun gebruikersbeheerproces verbeteren en het risico op beveiligingslekken en gegevensverlies minimaliseren. Het is belangrijk om beveiliging te zien als een doorlopend proces en regelmatig updates en aanpassingen door te voeren om bij te blijven met de steeds veranderende dreigingen en beveiligingsvereisten.
