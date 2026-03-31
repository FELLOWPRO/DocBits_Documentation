# Release Notes

## **Release Spring Spark 13 mei 2026**

Sandbox-beschikbaarheid: 27–29 april 2026

### DocBits Verbeteringen:

*   **Advanced Workflow Designer:**\
    DocBits presenteert een geheel nieuwe Advanced Workflow Designer — een visuele, op knooppunten gebaseerde automatiseringsbouwer die volledige workflow-orkestratie binnen handbereik brengt. Via een intuïtief drag-and-drop canvas kunnen beheerders DocBits workflow-kaarten verbinden tot complexe, meervoudige verwerkingspipelines. Elk knooppunt op het canvas vertegenwoordigt een actie of beslispunt, en de verbindingen tussen knooppunten definiëren de documentenstroom door de pipeline. De designer ondersteunt wachtstappen voor getimede vertragingen, parallelle paden waarbij alle of sommige vertakkingen moeten worden voltooid voordat wordt verdergegaan, en de mogelijkheid om elke combinatie van ingebouwde of door partners gemaakte kaarten te koppelen. Workflows kunnen worden opgeslagen als herbruikbare sjablonen, geïmporteerd en geëxporteerd tussen omgevingen, en direct vanuit de designer worden getest voordat ze live gaan. De editor biedt een canvas met snap-to-grid en mini-map navigatie voor grote workflows, sneltoetsen voor kopiëren en plakken, realtime validatie met foutmarkering tijdens het bouwen, en bescherming tegen gelijktijdig bewerken om het overschrijven van wijzigingen door andere gebruikers te voorkomen. Gedetailleerde uitvoeringslogboeken bieden monitoring per knooppunt, waardoor beheerders precies kunnen traceren hoe elke stap in een workflow is uitgevoerd en waar problemen zijn opgetreden.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_advanced_workflow_designer.png)

*   **Workflow Designer Verbeteringen:**\
    De bestaande workflow designer is verbeterd met if/else vertakkingslogica, waardoor meer geavanceerde op beslissingen gebaseerde workflows mogelijk zijn. Verschillende nieuwe conditiekaarten zijn toegevoegd, wat het bereik van beschikbare automatiseringslogica verder uitbreidt. Een nieuwe Workflow Test Manager stelt beheerders in staat geautomatiseerde tests voor workflows individueel of allemaal tegelijk te maken en uit te voeren, zodat wijzigingen zich gedragen zoals verwacht vóór implementatie. De Workflow-sectie bevat nu ook een KPI-dashboard met belangrijke statistieken over workflow-uitvoeringsprestaties.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_workflow_branching.png)

*   **DocNet AI Agents:**\
    DocBits bevat nu DocNet AI Agents — intelligente, autonome agenten die op de achtergrond draaien om documentverwerkingstaken af te handelen zoals inkooporder-matching en factuurvalidatie. Agenten werken onafhankelijk, werken toegewezen taken af en escaleren alleen naar gebruikers wanneer menselijk oordeel nodig is. Wanneer een agent een uitzondering tegenkomt of bevestiging nodig heeft, maakt deze een goedkeuringsverzoek aan dat direct in de inbox van de gebruiker verschijnt, zodat niets wordt gemist zonder constante supervisie. Agenten kunnen met elkaar coördineren, subtaken delegeren en werk organiseren in missies en projecten voor complexe meerstapsprocessen. Een speciaal agenten-dashboard biedt volledig inzicht in agentenactiviteit, prestatiestatistieken en auditlogboeken, zodat beheerders kunnen monitoren wat agenten doen en hoe efficiënt ze werken. Realtime notificaties houden gebruikers op de hoogte wanneer agenten taken voltooien of items markeren voor beoordeling.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_docnet_ai_agents.png)

*   **Partner Card SDK:**\
    Een nieuw Partner Card SDK stelt externe ontwikkelaars en partners in staat aangepaste workflow-kaarten voor DocBits te bouwen. Partners kunnen kaartpakketten uploaden voor validatie en beoordeling, kaarten importeren vanuit GitHub repositories, en inzendingen beheren via een speciale Card SDK instellingenpagina. Een AI-gestuurd beoordelingssysteem evalueert automatisch ingediende kaarten op kwaliteit en naleving. Het SDK bevat op voorbeelden gebaseerde downloads met kaartselectiedialogen, gedragsvalidatie in een sandbox-omgeving, en uitgebreide startdocumentatie. Het Card SDK is beveiligd met licentiecontroles en is nu zichtbaar voor alle gebruikers, niet alleen beheerders.

*   **Full-Text Search / DocSearch:**\
    Een nieuwe full-text zoekmogelijkheid is toegevoegd aan DocBits, aangedreven door AI-gestuurde vectorzoeking. Gebruikers kunnen zoeken over alle geïndexeerde documenten met realtime leveranciersfiltering en een "Find Similar" functie om documenten te vinden die lijken op een geselecteerd document. Een speciale instellingenpagina stelt beheerders in staat AI-gegevensindexering, vectoropslagvoorkeuren te configureren en indexeringsvoortgang in realtime te monitoren. DocSearch-toegang wordt beheerd via abonnementsplannen.

*   **E-Invoice Format Uitbreiding:**\
    DocBits heeft de ondersteuning voor elektronische factuurformaten aanzienlijk uitgebreid met meer dan 80 nieuwe wereldwijde e-invoice types en meer dan 40 nieuwe formaten. Nieuw ondersteunde formaten omvatten onder andere Taiwan EGUI, Thailand E-Tax, India GST Credit Note, SPS Commerce RSX 7.7.4, XRechnung 3.0.2, ZUGFeRD 2.2 en 2.3.2, Factur-X varianten, Uruguay CFE, Ecuador SRI Retención, SVEFAKTURA 1.0, EHF 3.0, OIOUBL, Finvoice en Asia-Pacific PINT Credit Notes. DocBits bereikt nu 100% classificatie- en extractiedekking voor alle ondersteunde elektronische documentformaten.

*   **Login Analytics:**\
    Een nieuw Login Analytics dashboard geeft beheerders volledig inzicht in loginactiviteit binnen de organisatie. Het dashboard bevat vergelijkingsgrafieken die logintrends in de tijd tonen, dagelijkse en wekelijkse aggregatieweergaven, en GeoLite2-gebaseerde geolocatie om te zien waar logins vandaan komen. Dit biedt een snelle manier om ongebruikelijke loginpatronen te herkennen en accountbeveiliging te monitoren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_login_analytics.png)

*   **Analytics Dashboard:**\
    Een uitgebreide documentverwerkingsanalysemodule is geïntroduceerd met meerdere dashboardweergaven waaronder Executive Overview, API Metrics, Quality Metrics en Processing Performance. Document Flow Analytics biedt statistieken op organisatieniveau over documentverwerkingstijden en statusovergangen. Een compleet Activity Log en Event Log systeem stelt beheerders in staat gebeurtenisgegevens te doorzoeken, filteren en exporteren met grafiekvisualisaties en JSON-syntaxmarkering. Een Audit Trail functie biedt gedetailleerde wijzigingsgeschiedenisregistratie met popup-details voor elke wijziging.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_analytics_dashboard.png)

*   **Verbeteringen Toegangscontrole:**\
    Toegangscontrole is toegepast op de gehele applicatie, inclusief het veldvalidatiescherm, AI-geëxtraheerde tabellen en meerdere andere weergaven. Beheerders hebben nu de optie om toegangscontrole globaal uit te schakelen indien nodig. Het ontwerp van de toegangscontrole is vernieuwd voor een consistentere en intuïtievere ervaring op alle schermen.

*   **Layout Builder Verbeteringen:**\
    De Layout Builder ondersteunt nu verborgen en alleen-lezen velden met visuele indicatoren, waardoor beheerders gemakkelijker kunnen zien welke velden zichtbaar en bewerkbaar zijn voor gebruikers. Een aanpasbaar scheidingselement tussen panelen verbetert de werkruimteflexibiliteit, en veldlengte-instellingen bieden meer precieze controle over gegevensinvoervelden.

*   **Exportgeschiedenis in Dashboard Acties:**\
    Gebruikers kunnen nu de exportgeschiedenis van een document direct openen vanuit het dashboard actiemenu, waardoor het sneller is om eerdere exportpogingen te bekijken zonder de hoofdweergave te verlaten.

*   **Export Verbeteringen:**\
    Exportconfiguraties ondersteunen nu uitvoeringsvolgorde, waardoor beheerders de volgorde kunnen definiëren waarin meerdere exportmethoden worden verwerkt. Een nieuwe herexport-knop op foutschermen stelt gebruikers in staat opnieuw te proberen vanaf de mislukte stap in plaats van het hele proces opnieuw te starten. DocBits ondersteunt nu ook het GLS840MI API exportdoel, met een bijgewerkte interface voor het beheren van meerdere actieve exportconfiguraties per documenttype.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_export_improvements.png)

*   **Script Versioning & AI Chat:**\
    Documentscripts ondersteunen nu volledige versiegeschiedenis, waardoor beheerders wijzigingen kunnen traceren, versies vergelijken en eerdere scriptversies kunnen herstellen. Standaardscripts zijn beschermd tegen onbedoelde bewerkingen, en scriptnamen kunnen inline worden bewerkt met breadcrumb-navigatie. Velden kunnen nu programmatisch als alleen-lezen worden ingesteld via de nieuwe set\_is\_readonly functie. Een nieuwe AI-gestuurde chatassistent helpt bij scriptontwikkeling met realtime streaming-antwoorden.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_script_versioning.png)

*   **API Key Management:**\
    Een nieuwe API Key Management pagina in de integratie-instellingen stelt beheerders in staat meerdere API-sleutels aan te maken, te bekijken en te beheren met Redis-gebaseerde caching voor prestaties.

*   **Idea Board:**\
    Een nieuwe Idea Board functie stelt gebruikers in staat functie-ideeën en suggesties in te dienen, te bespreken en erop te stemmen. Het bord bevat een rich text editor met ondersteuning voor het uploaden van afbeeldingen, reacties en stemfunctionaliteit.

*   **Leveranciersstatistieken:**\
    Nieuwe leveranciersstatistieken-weergaven bieden inzicht in leverancier-gerelateerde documentverwerkingsstatistieken.

*   **Taaluitbreiding:**\
    DocBits ondersteunt nu 22 talen, uitgebreid ten opzichte van de vorige selectie. De taalkiezer is bijgewerkt met een 4-koloms rasterindeling, en gebruikers kunnen nu hun voorkeurstaal direct in hun gebruikersinstellingen instellen.

*   **Abonnementplan Herontwerp:**\
    De abonnementplankiezer is herontworpen met verbeterde tokeninformatie-weergave en een nieuwe DocNet-gebruiksrij in de abonnementstabel.

*   **Dual Monitor Mode:**\
    Dual Monitor Mode is verplaatst naar een globale gebruikersinstelling, waardoor het toegankelijk en persistent is tussen sessies voor gebruikers die met meerdere schermen werken.

*   **Fuzzy Zoeken voor Duitse Tekens:**\
    De zoekfunctionaliteit ondersteunt nu correct Duitse speciale tekens (umlauten), waardoor zoekopdrachten naar woorden zoals "Rechnungsnummer" ook overeenkomen met alternatieve tekenrepresentaties.

*   **Verbeteringen E-mailnotificaties:**\
    De parametervervanging in e-mailsjablonen is verbeterd met betere ontvangersvalidatie en afhandeling van gebruikersvoorkeuren.

*   **Kredietgebruik Tracking:**\
    Organisaties kunnen nu hun AI-kredietgebruik in de tijd bekijken en volgen met filteropties, wat betere zichtbaarheid biedt in verbruikspatronen.

### Algemene Verbeteringen:

*   Het instellingengebied is herontworpen met een inklapbare zijbalk, georganiseerde subcategorieën en ankergebaseerde navigatie voor snellere toegang. Een contextueel hulppaneel biedt inline begeleiding, en statusvolgbadges tonen configuratievolledigheid in één oogopslag.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_may_2026_settings_redesign.png)

* Documenten met barcodes worden nu betrouwbaarder gesplitst, met betere afhandeling van randgevallen en foutherstel.
* PO-matching detecteert en converteert nu automatisch eenheidsprijzen bij het splitsen van gematchte regels, waardoor handmatige correcties worden verminderd.
* Documenten blijven niet meer vastzitten tijdens extractie — een nieuw statusvolgsysteem zorgt ervoor dat elk document door de pipeline gaat.
* Bij extractiefouten biedt DocBits nu duidelijkere foutmeldingen met stapsgewijze details om het probleem sneller op te lossen.
* De algehele applicatieprestaties zijn verbeterd met snellere responstijden op alle schermen.
* Auto Accounting regels ondersteunen nu nummergebaseerde filtering voor nauwkeurigere matchingcondities.

### Bugfixes:

* Een probleem opgelost waarbij de aangepaste dashboardnaam niet was uitgelijnd met het dashboardpictogram.
* Een probleem opgelost waarbij het dashboard kolommen toonde die niet in de zichtbare kolommenconfiguratie waren opgenomen.
* Een probleem opgelost waarbij de geselecteerde tabnaam niet op het dashboard werd weergegeven.
* Een probleem opgelost waarbij de "Nieuwe versie beschikbaar" popup verscheen bij elke suborganisatiewijziging.
* Een probleem opgelost waarbij de documenten-per-pagina instelling niet werd bewaard na paginaverversing.
* Een probleem opgelost waarbij het documentenaantal op het dashboard niet correct werd bijgewerkt.
* Een probleem opgelost waarbij gebruikers onterecht het foutbericht "Dashboard bestaat al" ontvingen.
* Een probleem opgelost waarbij de bevestigingspopup voor bulkverwijdering niet werd weergegeven.
* Meerdere problemen opgelost met de weergave en het opslaggedrag van gedeelde dashboards.
* Een probleem opgelost waarbij documenttabellen niet werden weergegeven op het validatiescherm.
* Een probleem opgelost waarbij een onjuist foutbericht werd getoond voor ongeldige PDF-bestanden.
* Een probleem opgelost waarbij de kolomverkleiner achter rijactieknoppen verscheen.
* Een probleem opgelost waarbij onjuiste waarden werden geëxtraheerd voor nettobedrag, belastingbedrag en belastingtarief.
* Een probleem opgelost waarbij exportconfiguraties niet konden worden aangemaakt zonder een documenttype op te geven wanneer dit als optioneel was gemarkeerd.
* Een probleem opgelost waarbij een duplicaatconfiguratiefout optrad bij het toevoegen van nieuwe exportconfiguraties.
* Een probleem opgelost waarbij fouten optraden bij het aanmaken van meerdere exportconfiguraties.
* Een probleem opgelost waarbij de configuratietitel werd gewist na het selecteren van Watchdog als exporttype.
* Een interne serverfout opgelost bij het aanmaken van Infor exportconfiguraties.
* Een probleem opgelost dat het opnieuw starten van meerdere geëxporteerde documenten verhinderde.
* Een probleem opgelost waarbij sommige instellingenpagina's niet konden worden gevonden.
* Een probleem opgelost waarbij de Watchdog downloadlink een fout retourneerde.
* Een probleem opgelost waarbij de List of Values aanmaakknop geen actie triggerde.
* Een probleem opgelost waarbij groepsbeschrijvingen niet werden weergegeven.
* Een probleem opgelost waarbij de wachtwoordvalidatiestatus bleef bestaan na het annuleren van een gebruikersbewerking.
* Een probleem opgelost waarbij documenten in de status "Pending Watcher Export" niet klikbaar waren.
* Een probleem opgelost waarbij duplicaat lookup-configuraties konden worden aangemaakt.
* Een probleem opgelost waarbij gebruikerssortering niet correct werkte.
* Een weergaveprobleem opgelost waarbij alle applicatietekst in blauw verscheen.
* Een probleem opgelost waarbij de taalformaatweergave inconsistent was.
* Een probleem opgelost waarbij de taalinstelling leeg verscheen wanneer geen voorkeur was geselecteerd.
* Een probleem opgelost waarbij de hoofdletters van de bedrijfsnaam werden genegeerd.
* Een probleem opgelost waarbij zoeken niet werkte voor groepen en rechten.
* Een probleem opgelost waarbij de verwijder-gebruiker actie de gebruiker niet correct verwijderde.
* Een probleem opgelost waarbij documentstroom-iconen niet zichtbaar waren.
* Een interne serverfout opgelost bij het opslaan van e-mailsjablonen.
* Een probleem opgelost waarbij dubbele variabelen werden ingevoegd in e-mailsjabloon-onderwerpen.
* Een fout opgelost bij het opslaan van inkomende e-mailaccountgegevens.
* Een probleem opgelost waarbij documenten vastzaten op "nieuw" status na uploaden.
* Een probleem opgelost waarbij tabelkolommen niet beschikbaar waren na deactivering en heractivering.
* Een probleem opgelost waarbij het aanmaken van beslisbomen mislukte voor aangepaste documenttypen.
* Een probleem opgelost waarbij tabelextractie geen resultaten retourneerde.
* Een probleem opgelost waarbij het documenttype CREDIT\_NOTE niet correct werd herkend.
* Een probleem opgelost waarbij gebruikers zonder beheerdersrechten alle aangemaakte taken konden bekijken.
* Een probleem opgelost waarbij de suborganisatie-popup niet sloot na drag-and-drop bestandsuploaden.
* Een probleem opgelost waarbij tijdsperiodefilters niet correct werden toegepast.
* Een probleem opgelost met datum- en tijdconversie naar US-formaat.
* Een probleem opgelost waarbij workflows in de verkeerde volgorde werden getriggerd — workflow-uitvoering gebruikt nu correcte documentvergrendeling en wachtrijprioriteiten.

## **Release HotFix 2 31 maart 2026**

### DocBits-verbeteringen:

* **Hybride PDF-verwerking — Door de gebruiker gestuurde XML-extractie:**\
  Wanneer een PDF ingebedde XML-gegevens bevat, kunnen gebruikers nu kiezen of DocBits de ingebedde XML moet gebruiken voor extractie of het document als een standaard PDF moet verwerken. Dit geeft organisaties volledige controle over hoe hybride documenten worden verwerkt, zodat de extractiemethode die het beste past bij hun workflow wordt toegepast.

* **AP Assignment Code op het Approval-scherm:**\
  De AP Manager Approval-pagina bevat nu een AP Assignment Code-veld, geïntegreerd met Infor M3 CRS620. Dit stelt goedkeurders in staat om toewijzingscodes direct tijdens het goedkeuringsproces te controleren en te bevestigen zonder naar externe systemen te hoeven schakelen.

* **PO-totaal afstemming met documenttotaal:**\
  DocBits ondersteunt nu het vergelijken van het inkoopordertotaal met het totaal op het document, wat een extra validatielaag biedt tijdens PO Matching om afwijkingen eerder in het proces te detecteren.

* **Update van leveranciersartikelnummer en VPE:**\
  DocBits ondersteunt nu het bijwerken van de velden leveranciersartikelnummer en VPE (Verpackungseinheit / verpakkingseenheid) tijdens documentverwerking, waarbij de waarden bij export worden teruggesynchroniseerd naar M3.

* **Verbeterde documentlayout-classificatie:**\
  Het documentlayout-ID (tfidf_id) wordt nu alleen gegenereerd op basis van koptekst, met uitsluiting van voettekst. Dit verbetert de classificatienauwkeurigheid door te voorkomen dat voettekstinhoud de documenttypedetectie beïnvloedt.

* **Export & Next-knop:**\
  Er is een nieuwe "Export & Next"-knop toegevoegd, waarmee gebruikers het huidige document kunnen exporteren en onmiddellijk naar het volgende in de wachtrij kunnen gaan, wat de beoordelings- en exportworkflow stroomlijnt.

* **Goedkeuringsproces voor kostenfacturen:**\
  Het goedkeuringsproces voor kostenfacturen is verbeterd met geoptimaliseerde routering- en validatielogica.

### Bugfixes:

* Een probleem opgelost waarbij de Infor SFTP-export mislukte met een fout door een onjuist bibliotheekcommando.
* Een probleem opgelost waarbij booleaanse selectievakjes niet konden worden weergegeven op het goedkeuringsscherm.
* Een probleem opgelost waarbij UNMU-berichten werden verzonden, zelfs wanneer er geen afwijkingen in de inkoopeenheid waren.
* Een probleem opgelost waarbij omzetbelasting onjuist werd geclassificeerd als toeslag op het PO Matching-scherm, wat resulteerde in een negatief onverrekend bedrag.
* Een probleem opgelost waarbij de export mislukte wanneer de inkoopeenheid niet was ingesteld in de orderbevestiging maar wel aanwezig was in de inkooporder.
* Een probleem opgelost waarbij de e-mailtekst ontbrak bij meerdere documenten.
* Een probleem opgelost waarbij het artikelnummer van de leverancier niet zichtbaar was op het goedkeuringsscherm en updates niet naar M3 werden verzonden.
* Een probleem opgelost waarbij de leveranciersexport naar Infor een fout retourneerde.
* Een probleem opgelost waarbij PO Matching fouten produceerde tijdens de verwerking.
* Een probleem opgelost waarbij de `findAll`-functie niet correct werkte in documentscripts.
* Een probleem opgelost waarbij de Watchdog-kolom "Updated By" onjuist de Fellow Admin-gebruiker toonde in plaats van de werkelijke gebruiker.
* Een probleem opgelost waarbij BOD-Mapping niet kon worden geconfigureerd in de Watchdog-interface.
* Een probleem opgelost waarbij toeslagen onjuist werden weergegeven als onverrekende bedragen in plaats van als toeslagen.
* Een probleem opgelost waarbij automatische matching niet werkte voor facturen met meerdere regels ondanks een bestaande matchingconfiguratie.
* Een probleem opgelost waarbij een koppelteken ("-") in het artikelnummer werd meegenomen bij PO Matching voor de inkooporder maar werd genegeerd op de factuur, wat een valse afwijking veroorzaakte.
* Een probleem opgelost waarbij zowel PDF- als XML-bestanden naar de exportmap werden geüpload, zelfs wanneer de "Export PDF"-schakelaar was uitgeschakeld.
* Een probleem opgelost waarbij een ontbrekende status op de workflow-kaart verhinderde dat documenten door de workflow voortgingen.
* Een probleem opgelost waarbij de documentkwaliteit aanzienlijk was verslechterd na import.
* Een probleem opgelost waarbij het PO Match-scherm een fout gaf ("Cannot read properties of null").
* Een probleem opgelost waarbij de standaard waardelijst niet kon worden bewerkt.
* Een probleem opgelost waarbij de workflow de veldstatus niet correct kon lezen, wat onjuiste routering veroorzaakte.
* Een probleem opgelost waarbij inkomende e-mailimports mislukten met een fout.
* Een probleem opgelost waarbij ontbrekende regels niet correct in M3 aankwamen tijdens de export.
* Een probleem opgelost waarbij gecodeerde en goedgekeurde facturen af en toe niet werden bijgewerkt naar de status "goedgekeurd" in M3 via de APS110-API.
* Een probleem opgelost met de Multi Banking-configuratie die niet correct werkte.
* Meerdere problemen opgelost met de weergave en het opslaggedrag van gedeelde dashboards.
* Een probleem opgelost waarbij het veld leveranciersartikelnummer was beperkt tot 30 tekens, waardoor langere waarden niet konden worden opgeslagen.
* Een probleem opgelost waarbij eenheidsprijs- en eenheidsprijs-per-waarden een fout veroorzaakten tijdens de export.
* Een probleem opgelost waarbij PO-regels met een uitgesloten status (bijv. "Closed") nog steeds konden worden gesleept en gematcht op het PO Matching-scherm ondanks uitsluiting door matchingregels.

### Configuratiewijzigingen:

* E-mailsjablonen bijgewerkt om de "Go to Task"-knop te verwijderen.
* Scripts en verplichte veldinstellingen voor kostenelementen aangepast.

## **Release HotFix 1 16 maart 2026**

### DocBits-verbeteringen:

* **Documentgeschiedenis in SFTP-export:**\
  DocBits ondersteunt nu het opnemen van de volledige documentgeschiedenis als onderdeel van de geëxporteerde XML-payload bij export naar SFTP. Deze functie is configureerbaar via de Export Settings en biedt downstream-systemen een compleet auditspoor van elke statuswijziging en actie die op een document in DocBits is uitgevoerd — inclusief wie de wijziging heeft aangebracht, wanneer deze plaatsvond en wat de vorige en huidige statussen waren. Dit is bijzonder waardevol voor compliance, traceerbaarheid en operationele analyse.
* **Toeslagupdate bij orderbevestiging voor Infor On Premise:**\
  Infor On Premise-klanten kunnen nu orderbevestigingen met toeslagen direct in DocBits verwerken. De toeslagen worden volledig bijgewerkt via de export, waardoor het end-to-end orderbevestigingsproces naadloos verloopt en handmatige aanpassingen downstream overbodig worden.
*   **Standaard Layout toepassen op alle Origins:**\
    Een nieuwe **Apply Default Layout to Origins**-knop is geïntroduceerd in het layout-configuratiescherm. Beheerders kunnen nu het standaard layout met één enkele actie naar alle origins binnen een organisatie pushen, waardoor het tijdrovende handmatige proces van het kopiëren en plakken van layout-JSON per origin vervalt. Dit is vooral nuttig bij het onboarden van nieuwe klanten waarbij meerdere origins consistent moeten worden geconfigureerd.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(5).png)
*   **Documenttype-selectie voor FTP-import:**\
    FTP-importconfiguraties ondersteunen nu documenttype-toewijzing per map. Bij het configureren van een FTP-import kunnen gebruikers specificeren welk documenttype — zoals Factuur of Orderbevestiging — moet worden toegepast op alle documenten die uit die map worden geïmporteerd. Documenten worden automatisch geclassificeerd bij import, waardoor handmatige documenttype-toewijzing na opname overbodig wordt. Dit ondersteunt organisaties die meerdere documenttypen beheren over verschillende suborganisaties en mappen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(4).png)
* **Export naar GLS840 voor Infor On Premise:**\
  DocBits ondersteunt nu de export van documenten naar het GLS840-programma voor Infor On Premise-klanten, waardoor het scala aan ondersteunde exportbestemmingen voor on-premise omgevingen wordt uitgebreid.
*   **UI-verbeteringen voor Watchdog en exportconfiguratie:**\
    De Watchdog-configuratie- en exportconfiguratieschermen zijn vernieuwd met een verbeterde gebruikersinterface, met een overzichtelijkere lay-out en een intuïtievere ervaring voor beheerders die deze instellingen beheren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1).png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(2).png)

### Bugfixes:

* Een probleem opgelost waarbij gebruikers met geldige weergaverechten geen documenten konden bekijken — de permissielogica is herschreven met een toegangsniveaucontrole ter vervanging van de eerdere groepsgebaseerde filterbenadering.
* Verbeterde uitzonderingsafhandeling in meerdere gebieden van de applicatie voor grotere stabiliteit.
* Een probleem opgelost waarbij booleaanse kolomtypen niet correct werden verwerkt tijdens veldextractie.
* Een asynchroon authenticatieprobleem in het bestandsupload-endpoint opgelost.
* UI-weergaveproblemen voor de PO-tabel op het validatiescherm opgelost.
* Het scriptsjabloon bijgewerkt met opmerkingen voor het bijhouden van wijzigingen voor betere controleerbaarheid.
* Een probleem opgelost met dropdownvelden die zich niet correct gedroegen op het validatiescherm.
* Een probleem opgelost waarbij het suborganisatieveld niet vooraf was ingevuld bij het bijwerken van documenttoewijzingen vanuit het dashboard.

## **Release Winter Summit 10 december 2025**

### DocBits Verbeteringen:

*   **Verbeterde aanpassing van PO-matchingregels:**\
    DocBits biedt nu meer gedetailleerde en aanpasbare controle over inkooporder-matchingregels. Beheerders kunnen precies configureren welke kolommen moeten worden geëvalueerd tijdens het matchingproces voor elk documenttype, waardoor ervoor wordt gezorgd dat alleen de meest relevante velden worden overwogen. Bovendien kunnen toleranties op kolomniveau worden gedefinieerd, wat meer flexibiliteit biedt bij het omgaan met kleine afwijkingen. Elke regel kan ook worden geconfigureerd om te worden toegepast op handmatige matching, automatische matching of beide, waardoor teams de mogelijkheid krijgen om de matchingworkflow af te stemmen op hun exacte operationele vereisten. Deze verbeteringen verbeteren de aanpasbaarheid en precisie van het inkooporder-matchingproces aanzienlijk.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_3.png)
*   **Ondersteuning voor meerdere financiële accounts van leveranciers:**\
    DocBits ondersteunt nu het beheren van meerdere financiële accounts voor leveranciers via de RemitToPartyMaster BOD die door Infor wordt geleverd. Deze verbetering stelt organisaties in staat om meerdere remit-to accountrecords voor een enkele leverancier bij te houden, wat de flexibiliteit en nauwkeurigheid bij betalingsverwerking verbetert. Er is een nieuwe configuratie-instelling geïntroduceerd om deze mogelijkheid in of uit te schakelen, waardoor beheerders de functie kunnen activeren op basis van hun operationele behoeften.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_1.png)
*   **Gebruikerstoegang toegevoegd aan OCR-extractieresultaten:**\
    De knop **OCR-weergave** op het veldvalidatiescherm is nu beschikbaar voor alle gebruikers die validatietoegang hebben, in plaats van beperkt te zijn tot beheerders. Met deze update kan elke geautoriseerde gebruiker OCR-extractieresultaten direct bekijken, waardoor het gemakkelijker wordt om de nauwkeurigheid van gegevens te valideren en de algehele OCR-prestaties te monitoren. Deze verbetering bevordert meer transparantie en verbetert de efficiëntie van de validatieworkflow.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/release_notes_12_2025_2.png)
* **Dynamische kolomweergave in goedkeuringsschermen:**\
  Verbeterde goedkeuringsweergaven om dynamisch alleen de kolommen weer te geven die zijn geconfigureerd voor vergelijking in de databasevoorkeuren van elke organisatie. Eerder verschenen sommige organisatie-specifieke kolommen leeg wanneer ze niet waren geconfigureerd voor vergelijking, wat verwarring veroorzaakte. Nu tonen goedkeuringsweergaven alleen velden die actief worden vergeleken. Dit biedt duidelijkere, organisatie-specifieke goedkeuringsschermen zonder lege of irrelevante kolommen.
* **Ordertypeveld toegevoegd aan masterdataopzoekfunctie**:\
  De inkooporderkoplijst bevat nu een kolom "Order Type" in de masterdataopzoekfunctie, wat extra categorisatiemogelijkheden biedt.
* **Verbeteringen aangepast filterdashboard:**\
  De dashboard-deelfunctionaliteit is verbeterd om meer flexibiliteit te bieden aan gedeelde gebruikers. Personen met wie dashboards worden gedeeld, kunnen nu de dashboardfilters aanpassen en bewerken, waardoor ze de weergegeven informatie kunnen afstemmen op hun specifieke behoeften. Deze verbetering ondersteunt een meer gepersonaliseerde en interactieve kijkervaring, zodat gebruikers gemakkelijk de data-inzichten kunnen verfijnen die het meest relevant zijn voor hun taken.
* **Aanpasbare voorvoegsels voor goedkeuringsschermkolommen:**\
  Er is een nieuwe configureerbare optie geïntroduceerd om voorvoegsels weer te geven vóór documentkolommen op goedkeuringsschermen. Deze functie kan rechtstreeks binnen de layout builder worden beheerd, waardoor beheerders volledige controle hebben over of voorvoegsels worden weergegeven en op welke documenttypen ze van toepassing zijn. Door deze optie in te schakelen, krijgen gebruikers duidelijker context en verbeterde leesbaarheid bij het beoordelen van documenten tijdens het goedkeuringsproces.

### Algemene verbeteringen

* Verbeterde foutlogging voor slecht getrainde tabellen in tabel extractie.
* Een deellimiet toegevoegd voor dashboards van maximaal 10 gebruikers of 5 groepen, samen met een duidelijke foutmelding wanneer de limiet is bereikt.
* Verbeterde foutafhandeling voor aangepaste dashboards wanneer een gebruiker probeert een dashboard aan te maken met een naam die al bestaat.

### Bugfixes:

* Een probleem opgelost waarbij e-mails succesvol leken te verzenden vanuit de Leveranciersdetails sectie maar niet werden afgeleverd bij ontvangers.
* Een probleem opgelost waarbij Dropdown velden toegevoegd aan goedkeurings-/afwijzingsschermen niet werden weergegeven.
* Een probleem opgelost waarbij alle geëxporteerde documenten werden gemarkeerd als laatst bijgewerkt door de verkeerde gebruiker.
* Een probleem opgelost waarbij documenten "Workflow in Uitvoering" status toonden maar geen workflows werden uitgevoerd en het log leeg bleef.
* Een probleem opgelost waarbij niet-gerelateerde gebruikers aan documenten werden toegewezen op het moment van export zonder enig werk aan hen te hebben verricht.
* Een probleem opgelost waarbij gebruikers met de juiste rechten niet in staat waren toegewezen documenten af te wijzen en fouten ontvingen.
* Een probleem opgelost waarbij documentflow iconen niet werden weergegeven voor sommige organisaties.
* Een probleem opgelost waarbij een popup verscheen bij het uploaden van documenten met drag and drop naar het dashboard.
* Een probleem opgelost waarbij E-TEXT vlaggen als ingeschakeld werden weergegeven in de UI ondanks dat de API response alle waarden als false toonde.
* Een probleem opgelost waarbij een fout optrad bij het uploaden van documenten met lege pagina's.
* Een probleem opgelost waarbij taak hyperlinks in e-mail notificaties gebruikers niet naar het juiste goedkeuringsscherm verwezen.
* Een probleem opgelost waarbij het selecteren van de cross sub-organisatie ertoe leidde dat Master Data Lookup geen leveranciers weergaf. Gebruikers kunnen nu correct cross-organisatorische leveranciersgegevens bekijken.

## Release Autumn Summit 22 oktober 2025

### DocBits verbeteringen:

*   **E-mail Template Ontwerp Verbeteringen:**

    De e-mail template editor is opnieuw ontworpen om een duidelijkere structuur en soepelere ervaring te bieden. Het selecteren van documentvelden is nu intuïtiever en bijlagen kunnen direct binnen templates worden toegevoegd. Deze verbeteringen maken het sneller en gemakkelijker om professionele, op maat gemaakte e-mails te creëren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(310).png)
*   **Dashboard Verbeteringen:**

    Het dashboard is uitgebreid om navigatie en aanpassing te verbeteren. Met nieuwe tabbladen kunnen gebruikers sneller schakelen tussen verschillende documenttypen, waardoor de tijd die wordt besteed aan het zoeken naar de juiste weergave wordt verminderd.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(474)%20(1).png)
*   **Aangepaste FilterDashboards:**\
    Daarnaast kunnen dashboards nu worden aangepast en gefilterd volgens individuele voorkeuren. Deze aangepaste dashboards kunnen ook worden gedeeld met collega's, waardoor het\
    gemakkelijker wordt om consistente teamrapportageweergaven te creëren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(477).png)
*   **E-mail Notificatie Logs:**

    Een nieuwe logging functie is beschikbaar voor alle e-mail notificaties. Gebruikers kunnen nu een geschiedenis van verzonden notificaties bekijken, wat het gemakkelijker maakt om afleveringen te verifiëren en problemen op te lossen als e-mails niet worden ontvangen.
*   **E-Factuur Ondersteuning: e-SLOG 1.6 & 2.0:**

    Ondersteuning voor extra e-factuur formaten is geïntroduceerd. Het systeem kan nu e-SLOG versies 1.6 en 2.0 verwerken en genereren, wat compatibiliteit met partners en regelgevingsvereisten uitbreidt.
*   **Duplicaat Detectie Verbeteringen:**

    Duplicaat detectie is geüpgraded met twee krachtige configuratieopties. Het **Duplicaat Detectie Interval** stelt u in staat een tijdsbereik te definiëren om nauwkeuriger op duplicaten te controleren, terwijl de **Sta Export van Duplicaten Niet Toe** instelling automatisch voorkomt dat documenten die als duplicaat zijn gedetecteerd worden geëxporteerd. Samen bieden deze verbeteringen meer controle en zorgen voor hogere gegevensnauwkeurigheid.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(478).png)
*   **Beslisboom Verbeteringen:**

    Beslisbomen zijn nu veelzijdiger, met de mogelijkheid om documentveldwaarden te retourneren. Dit maakt geavanceerdere automatiseringslogica mogelijk, waardoor workflows beslissingen kunnen nemen op basis van daadwerkelijke documentgegevens.
*   **Nieuwe Workflow Kaarten:**

    Twee nieuwe workflow kaarten breiden automatiseringsmogelijkheden uit. De eerste stelt u in staat te controleren of een document tot een specifieke suborganisatie behoort, wat het gemakkelijker maakt om multi-entiteit setups te beheren. De tweede introduceert een leverdatum tolerantie controle, die leverdatums vergelijkt met de huidige datum in werkdagen om leververeisten effectiever te beheren en af te dwingen.
*   **CSV Export Verbeteringen:**

    De CSV export functie is aanzienlijk verbeterd. In plaats van alleen de documenten te exporteren die op de huidige pagina worden weergegeven, exporteert het systeem nu alle documenten in een dataset. Elke export creëert een logvermelding en de resulterende CSV wordt automatisch per e-mail verzonden, wat een completer en betrouwbaarder exportproces biedt.
*   **Inkooporder Verwijdering Tijdsbestek:**

    Een nieuwe configuratieoptie stelt beheerders in staat een tijdsbestek te definiëren voor het verwijderen van inkooporders. Deze verbetering voegt flexibiliteit en controle toe over gegevensretentiebeleid, zodat inkooporders alleen worden verwijderd wanneer dat gepast is.

### Bugfixes

* Een probleem opgelost waarbij oude gegevens werden opgenomen bij het exporteren van documenten.
* Het filter voor Export Fouten gecorrigeerd, dat eerder ook andere statussen toonde.
* Een tabelvalidatie mismatch opgelost waarbij "Unit Price" fouten triggerde maar "Unit Price Per" niet, ondanks dat de waarden correct waren.
* Een probleem opgelost waarbij het toevoegen van een nieuwe kolom aan het dashboard mislukte.
* Een probleem gecorrigeerd waarbij taken niet zichtbaar waren in de dashboard taak kolom.
* Willekeurig sorteergedrag opgelost zodat lijsten nu een consistente volgorde volgen.
* Een probleem opgelost waarbij het wijzigen van de kolomgrootte niet kon worden gestopt.
* Een bug opgelost die handmatige regelmatching in het PO-Matching scherm verhinderde.
* Een probleem gecorrigeerd waarbij de e-mail bijlage optie werd gereset na opslaan.
* Een probleem opgelost waarbij auto accounting aanvankelijk database ID's weergaf wanneer voor de eerste keer geopend.
* Fuzzy veldgedrag gecorrigeerd zodat waarden niet langer onjuist worden overschreven.
* Een probleem opgelost waarbij velden in auto account verdwenen na het verwijderen van inhoud.
* Een bug gecorrigeerd waarbij de gebruiker "Voornaam" en "Achternaam" niet kon hernoemen in de instellingen popup.
* Een probleem opgelost waarbij documenten vast konden komen te zitten in "workflow in uitvoering."
* Een menu icoon kleur probleem opgelost waarbij geselecteerde organisatiekleuren niet correct werden toegepast.
* Een probleem gecorrigeerd waarbij QR codes soms niet werden herkend.
* Een probleem opgelost waarbij accounts niet konden worden verwijderd met backspace om een andere in te voeren.
* Een taalmix-up opgelost na inloggen na de productie push.

## Release **Summer Bloom** Juli 2025

### DocBits verbeteringen:

* **Filteroptie voor E-mail Import Log:**\
  Gebruikers hebben nu de mogelijkheid om de importlogboeken te filteren en de tabel te sorteren voor een duidelijker, efficiënter overzicht. Deze verbetering stroomlijnt het proces van het identificeren en beheren van e-mailgegevens, wat troubleshooting en algemeen logbeheer verbetert.
*   **Meertalige Ondersteuning voor Lijsten van Waarden:**\
    We hebben de meertalige mogelijkheden uitgebreid naar de functie Lijsten van Waarden. Beheerders kunnen nu labels in meerdere talen definiëren, zodat het juiste label automatisch wordt weergegeven op basis van de systeemtaalinstellingen van de gebruiker. Deze verbetering bevordert grotere toegankelijkheid en lokalisatie, waardoor het voor gebruikers wereldwijd gemakkelijker wordt om met het platform in hun eigen taal te werken.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(1)%20(1)%20(1).png)
* **Verbeteringen voor Gebruikersdetails in Instellingen:**\
  De instellingeninterface toont nu uitgebreide gebruikersinformatie. Beheerders kunnen eenvoudig groepsaffiliaties, suborganisatiedetails en aanvullende belangrijke gegevens bekijken, wat beter beheer van gebruikersrollen mogelijk maakt en een duidelijker begrip van teamstructuren biedt.
* **Auto Accounting Informatie op het Goedkeuringsscherm:**\
  Het goedkeuringsscherm presenteert nu automatische boekhouddetails naast factuurinformatie. Deze verbetering biedt dieper inzicht in transactiegegevens, wat soepelere beoordelingsprocessen en beter geïnformeerde besluitvorming over facturen mogelijk maakt.
* **Taakteller voor Documenten op het Dashboardweergave:**\
  Documenten op het dashboard kunnen nu openstaande taken aangeven die ermee geassocieerd zijn en het totale aantal openstaande taken weergeven. Deze functie biedt gebruikers een snel overzicht van uitstaande acties, wat taakbeheer en workflowefficiëntie verbetert.
* **Leverancier-gebaseerde AI Model Selectie:**\
  Gebruikers kunnen nu het AI-model selecteren dat wordt gebruikt voor gegevensextractie op leveranciersbasis. Deze verbetering maakt fijnafgestemde optimalisatie mogelijk, wat zorgt voor betere extractienauwkeurigheid voor verschillende leveranciers en verbeterde algemene gegevensverwerkingsresultaten. [Leer meer](https://docs.docbits.com/end-user-and-partner-section/end-user-section/validation-screen#supplier-based-ai-model)
* **Verbeterde Workflow Logs voor Beslisboomkaarten:**\
  De logboeken tonen nu de output van de beslisboom, wat het gemakkelijker maakt om te volgen en begrijpen hoe beslissingen werden genomen binnen workflows.
*   **Introductie van Nieuwe Auto-Testing Setup voor Verbeterde Systeemfunctionaliteit en Stabiliteit:**

    We zijn verheugd de implementatie aan te kondigen van een nieuw geautomatiseerd testsysteem dat is ontworpen om de algehele functionaliteit en betrouwbaarheid van ons platform te verbeteren. Deze nieuwe setup voert consistente, grondige controles uit op ons systeem om problemen te identificeren voordat ze uw ervaring beïnvloeden. Door deze tests te automatiseren, kunnen we snellere reacties op potentiële problemen garanderen en de hoogste kwaliteitsnormen voor ons systeem handhaven.
* **Implementatie van Microservices Architectuur:**\
  We hebben het platform geherstructureerd door kerncomponenten op te splitsen in specifieke microservices. Deze architectuurverschuiving verbetert schaalbaarheid, verbetert systeemprestaties en maakt snellere, meer modulaire ontwikkelings- en implementatiecycli mogelijk.
*   **Walkthrough:**\
    Een begeleide walkthrough is nu beschikbaar om gebruikers te helpen verschillende delen van de applicatie gemakkelijker te navigeren en begrijpen. Dit is vooral nuttig voor het inwerken van nieuwe gebruikers of het verkennen van onbekende functies.\


    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(431).png)
* **Verbeteringen aan Beslisboom:**\
  Er zijn verbeteringen aangebracht aan de beslisboominterface, inclusief een intuïtievere functie voor het toevoegen van rijen — nu bovenaan de boom geplaatst — om onderhoud en bewerking te vereenvoudigen.
* **DocOperator, DocNet en Extension Tools:**\
  Nieuwe AI-aangedreven tools zoals DocOperator en DocNet helpen bij het automatiseren van repetitieve taken, wat de efficiëntie verbetert en handmatige inspanning bij documentworkflows vermindert.
*   **Elektronische Document Voorbeeld Optie:**\
    Een voorbeeldfunctie is toegevoegd voor elektronische documenten (eDocs), waardoor gebruikers wijzigingen direct binnen de instellingen kunnen testen en bekijken voordat ze worden geïmplementeerd.\


    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(3)%20(1)%20(1).png)
* **Nieuwe Taalondersteuning – Chinees:**\
  DocBits ondersteunt nu Chinees, wat toegankelijkheid en lokalisatieopties voor gebruikers over wereldwijde markten uitbreidt.
* **Verbeterd Taakdashboard:**\
  Het taakdashboard is verbeterd om een groter aantal taken tegelijk weer te geven, wat gebruikers een duidelijker overzicht geeft en taakopvolging verbetert.
*   **PO Matching Verbeteringen:**

    Visuele indicatoren toegevoegd voor verschillende matchingstatussen

    Nieuwe instelling om reeds gematcht PO-regels per documenttype te negeren

    Verbeterde auto-controle voor PO-updates om consistentie te garanderen
* **Layout Builder Verbeteringen:**\
  U kunt nu zoeken naar zowel veldnamen als veldtitels, wat het sneller en gemakkelijker maakt om lay-outcomponenten te configureren en te vinden.
* **Export en Volgende Knop in Goedkeuringsscherm:**\
  Een nieuwe knop is toegevoegd aan het goedkeuringsscherm waarmee gebruikers een document kunnen exporteren en automatisch naar het volgende document in de "Klaar voor Validatie" wachtrij kunnen gaan.
* **Nieuwe Workflow Kaarten:**\
  Nieuwe workflow kaarten zijn geïntroduceerd, inclusief kaarten voor het uitvoeren van workflows op nieuwe inkooporders en offertes-gerelateerde gebeurtenissen. Deze bieden meer automatiseringsopties.
*   **Watchdog Verbeteringen:**\
    Watchdog-configuratie is verplaatst naar de hoofdapplicatie-UI, wat het gemakkelijker maakt om te beheren. Extra functionaliteiten zijn ook geïntroduceerd voor betere monitoring en controle.\


    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(4)%20(1)%20(1).png)
* **Verbeteringen voor Regelafwijzing:**\
  Het afwijzen van een regelitem vereist nu dat gebruikers een reden opgeven, wat betere traceerbaarheid en verantwoordelijkheid in beoordelingsworkflows garandeert.
* **Leverancier AI Model Lijst in Instellingen:**\
  Een nieuwe instellingenweergave toont de AI-modellen die zijn toegewezen aan specifieke leveranciers, samen met een optie om ze te resetten. Dit verbetert transparantie en beheerbaarheid van leverancier-gebaseerde AI-configuraties.
*   **Verbeteringen aan Document Log:**\
    De documentlogboeken bevatten nu meer gedetailleerde informatie om betere auditing en troubleshooting te ondersteunen.\


    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/image%20(5)%20(1)%20(1).png)
* **PNG en JPG Ondersteuning:**\
  U kunt nu PNG- en JPG-bestanden uploaden, die automatisch worden geconverteerd naar PDF-formaat voor verwerking.
* **IDM Export Documentformaat Configuratie:**\
  Het exportformaat voor PDF's in IDM kan nu worden geconfigureerd, wat gebruikers meer controle geeft over hoe documenten worden gegenereerd.
* **Nieuw eDoc Type – EDIFACT INVOIC02:**\
  We ondersteunen nu het EDIFACT INVOIC02 elektronische documenttype, wat compatibiliteit met gestandaardiseerde factuurformaten uitbreidt.

### Bugfixes

* Een probleem opgelost waarbij taken niet verschenen op het validatie-/goedkeuringsscherm.
* De positionering van de Volgende/Vorige knop gefixeerd zodat deze statisch blijft.
* Scrollproblemen in de script- en beslisboomweergaven opgelost, zodat actieknoppen stationair blijven tijdens scrollen.
* Het land van oorsprong veld verwijderd van e-facturen.
* Een probleem opgelost met de taakteller die een onjuist aantal taken weergaf.
* Ontbrekende vertalingen toegevoegd.
* Aangepaste velden gecorrigeerd om beschrijvende namen weer te geven in plaats van ID's.
* Een probleem opgelost waarbij documenten werden gedownload met een onjuiste bestandsnaam.
* Sorteerinconsistenties in de factuurregel-tabel binnen PO-matching opgelost.
* Een probleem opgelost dat de functionaliteit voor het aanmaken van taken beïnvloedde.
* Een probleem opgelost in PO-matching waarbij de factuur-tabelsortering werd gereset bij het matchen van een regel.
* Auto accounting problemen opgelost door ervoor te zorgen dat boekingsreferenties correct worden gesplitst wanneer een bedrag wordt verdeeld.
* De ClickHouse host-informatie bijgewerkt.
* Een probleem opgelost waarbij dubbele documenten niet als duplicaten werden herkend.
* Exportproblemen opgelost veroorzaakt door boekingsreferenties die te lang waren.
* Een probleem opgelost waarbij alleen-lezen checkboxen niet alleen-lezen waren
* Een probleem opgelost waarbij gebruikers twee keer aan een suborganisatie konden worden toegevoegd
* Een probleem opgelost waarbij het wijzigen van de suborganisatie voor een document de toegewezen gebruiker of groep resettte
* Enkele problemen met het auto accounting scherm opgelost
* Een probleem opgelost waarbij gebruikers geen FTP-configuratie konden toevoegen
* Een probleem met de SSO-login opgelost
* Enkele problemen met betrekking tot inkomende e-mails opgelost
* Een probleem opgelost waarbij documenten een verkeerde naam kregen bij het downloaden
* Een probleem opgelost waarbij de beslisboom een onjuist resultaat retourneerde

## Release Hot Fix Winter Frost 10 april 2025

### DocBits verbeteringen:

* **Verbeterde `set_column_date_value` Scriptfunctie:**\
  De `set_column_date_value` functie bevat nu ondersteuning voor de `skip_weekend` optie, waardoor datumwaarden automatisch weekends kunnen overslaan wanneer toegepast.
* **Verbeterde Bestandsupload Ondersteuning:**\
  PNG- en JPEG-bestanden kunnen nu direct worden geüpload en worden automatisch geconverteerd naar PDF-formaat voor gestroomlijnde documentverwerking.
* **Watchdog Functionaliteit Upgrades:**
  * Ondersteunt nu export naar **Enaio** voor betere systeemintegratie.
  * Verbeterde parseermogelijkheden om informatie uit `Sync.ContentDocument` XML-structuren te extraheren, wat efficiëntere gegevensverwerking mogelijk maakt.

### Bugfixes

* Een probleem met een scriptfunctie opgelost.
* Een probleem opgelost waarbij inkooporders een verkeerde status hadden nadat ze werden bijgewerkt

## Release Hot Fix Winter Frost 17 maart 2025

### Bugfixes

* De sneltoetsen verbeterd.

## Release Hot Fix Winter Frost 11 maart 2025

### DocBits verbeteringen:

* **Verbeterde Data Extractie:** Een optie toegevoegd om het **Inkoopordernummer** of **Artikelnummer** uit een regel erboven of eronder te extraheren.
* **Uitgebreide Cross Sub-Organisaties Toegang:** Niet-admin gebruikers hebben nu ook toegang tot de **Cross Sub-Organisaties** functie. [Leer meer](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/sub-organizations#cross-sub-organisations-access)

### **Bugfixes:**

* Een probleem opgelost waarbij gebruikers niet aan een groep konden worden toegevoegd.
* Een probleem met e-mail import fouten opgelost.
* Een probleem opgelost met veldtraining op documenten met meer dan één pagina
* Een probleem opgelost waarbij scripts niet goed werkten.
* Een probleem opgelost waarbij documentgegevens niet correct werden weergegeven
* Een probleem opgelost met de automatische inkooporder update instelling
* Een probleem opgelost waarbij de abonnementstokens verkeerd werden weergegeven
* Een probleem opgelost waarbij het taakscherm een verouderde documentversie toonde
* Een probleem opgelost dat ervoor zorgde dat documenten hun status niet veranderden

## Release Hot Fix Winter Frost 3 februari 2025

### **DocBits Verbeteringen:**

* **Ondersteuning voor ISO-8859-1 voor ZUGFeRD:** Verbeterde compatibiliteit voor facturen met ISO-8859-1 karaktercodering.
* **Geoptimaliseerd Logging Systeem:** Verbeterde tracking en diagnostiek voor snellere probleemidentificatie en oplossing.

## Release Winter Frost 22 januari 2025

#### Nieuwe Functies

### Ondersteuning voor ZUGFeRD 2.1 en Nieuwer

DocBits bevat nu volledige ondersteuning voor ZUGFeRD versies 2.1 en hoger, wat naadloze verwerking van ZUGFeRD-compatibele elektronische facturen mogelijk maakt. De integratie garandeert:

* **Compatibiliteit**: DocBits kan ZUGFeRD-facturen beheren in zowel hun gestructureerde (XML) als ongestructureerde (PDF) formaten, met behoud van naleving van EU-normen zoals EN 16931 voor e-facturering.
* **Efficiëntie**: Gebruikers kunnen moeiteloos ZUGFeRD e-facturen importeren, valideren en gegevens extraheren, wat handmatige gegevensinvoer minimaliseert en verwerkingstijd vermindert.
* **Flexibiliteit**: Of u nu werkt met basis-, comfort- of uitgebreide profielen binnen de ZUGFeRD-standaard, DocBits biedt tools om elk niveau van factuurcomplexiteit te beheren.
* **Toekomstbestendig**: Met ondersteuning voor nieuwere versies zorgt DocBits ervoor dat bedrijven voldoen aan evoluerende e-factureringsregels in EU-lidstaten en daarbuiten.

Door ZUGFeRD 2.1 en nieuwere standaarden op te nemen, vereenvoudigt DocBits grensoverschrijdende transacties en sluit het aan bij moderne bedrijfsbehoeften, wat het een essentieel hulpmiddel maakt voor organisaties die prioriteit geven aan digitale transformatie en naleving van regelgeving. [Leer meer](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/zugferd-1.0-2.1-and-2.3)

### Externe API Integratie voor Verbeterde Documentverwerking

DocBits introduceert een geavanceerde mogelijkheid om externe API's te gebruiken tijdens documentverwerking, wat de volledigheid en nauwkeurigheid van geëxtraheerde gegevens verbetert. Deze functie vermindert handmatige invoer aanzienlijk door ontbrekende velden te vullen met nauwkeurige, actuele informatie die in real-time wordt opgehaald uit vertrouwde bronnen. Het zorgt ervoor dat documenten sneller en met grotere consistentie worden verwerkt.

### Cross Sub-Organisaties Toegang

Voor organisaties met meerdere suborganisaties ingeschakeld, introduceert DocBits nu de Cross Sub-Organisaties functie. Deze verbetering stelt administratieve gebruikers in staat hun documentbeheer te stroomlijnen over alle suborganisaties onder één paraplu. Admin-gebruikers hebben nu toegang tot en kunnen alle documenten van elke suborganisatie bekijken zonder van suborganisatie te hoeven wisselen. Deze gecentraliseerde zichtbaarheid stelt admins in staat om alle documenten voor alle suborganisaties te zien, waardoor het gemakkelijk wordt om specifieke bestanden te vinden terwijl ze toch een vogelvluchtperspectief behouden. [Leer meer](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/sub-organizations#cross-sub-organisations-access)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/CrossSubOrganisations.png)

### Documentzichtbaarheid op Basis van Groepsrechten

DocBits introduceert verbeterde documentzichtbaarheidscontroles, die preciezer toegangsbeheer mogelijk maken voor niet-admin gebruikers via groep-gebaseerde rechten. Deze functie stelt beheerders in staat te definiëren welke documenten zichtbaar zijn voor specifieke gebruikers of groepen, wat gestroomlijnde workflows en verbeterde gegevensbeveiliging garandeert. Admin-gebruikers kunnen documenten toewijzen aan specifieke groepen, waarbij zichtbaarheid alleen wordt verleend aan gebruikers binnen die groepen. Dit zorgt ervoor dat gebruikers alleen de documenten zien die relevant zijn voor hun rol of team, wat rommel vermindert en focus verbetert. [Leer meer](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/groups-and-permissions)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Group%20Based%20Permission.png)

### Sequentiële Workflow en Goedkeuringsgeschiedenis

DocBits introduceert een krachtige Sequentiële Workflow en Goedkeuringsgeschiedenis functie, ontworpen om de efficiëntie en verantwoordelijkheid van documentverwerking te verbeteren. Door documenten een vooraf gedefinieerde beslisboom te laten volgen, zorgt deze functie voor ordelijke beoordeling en goedkeuring terwijl een volledig overzicht van genomen acties wordt bijgehouden. Sequentieel Workflow Beheer:

* Documenten kunnen worden toegewezen aan meerdere gebruikers in een vooraf gedefinieerde volgorde, zodat elke fase van beoordeling of validatie in de juiste volgorde plaatsvindt.
* Elke gebruiker in de workflow wordt op de hoogte gesteld wanneer het hun beurt is om actie te ondernemen op het document, wat verwarring en vertragingen vermindert.
* Workflows kunnen worden aangepast om specifieke bedrijfsprocessen te matchen

**Goedkeuringsgeschiedenis:**

* Een volledig logboek van alle acties die op het document zijn ondernomen is beschikbaar in de Validatie- en Goedkeuringsweergaven. Dit omvat:
  * Gebruikersacties (bijv. "goedgekeurd", "afgewezen")
  * Tijdstempels voor elke actie
  * Opmerkingen of notities toegevoegd door gebruikers tijdens beoordeling
* De geschiedenis zorgt voor transparantie en biedt een auditspoor voor naleving en troubleshooting. [Leer meer](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/more-settings/approval-history)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Approval%20History.png)

### SFTP/FTP Documenten Archief Verbetering

De SFTP/FTP Documenten Archief verbetering in DocBits bouwt voort op de bestaande importfunctionaliteit en introduceert een naadloze methode voor het archiveren van bestanden nadat ze zijn verwerkt. Een nieuwe instelling in de FTP-importconfiguratie stelt gebruikers in staat bestandsarchivering in of uit te schakelen. Zodra bestanden succesvol zijn ingested en verwerkt in DocBits, worden ze automatisch gearchiveerd naar een aangewezen map op de SFTP/FTP-server als de optie is ingeschakeld. Dit zorgt ervoor dat verwerkte bestanden worden bewaard voor administratie zonder de actieve importmappen te vervuilen. [Leer meer](https://docs.docbits.com/end-user-and-partner-section/end-user-section/how-to-import-documents/ftp)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/SFTPArchieve.png)

### Meerdere BTW Secties voor BTW Type en Export naar LN

Deze functie verbetert mogelijkheden voor BTW-verwerking door gedetailleerde classificatie en export van BTW-informatie naar Infor LN mogelijk te maken (Volledige BTW, Verlaagde BTW, BTW Vrij). Dit maakt betere afstemming met complexe BTW-structuren mogelijk en zorgt voor naadloze integratie met boekhoudsystemen.

**Meerdere BTW Secties per Type**:

* DocBits ondersteunt nu het toevoegen van meerdere BTW-secties onder elk BTW-type, zoals:
  * Volledige BTW: Standaard BTW- of omzetbelastingtarieven.
  * Verlaagde BTW: Lagere tarieven voor specifieke goederen of diensten (bijv. essentiële artikelen).
  * BTW-Vrij: Vrijstellingen voor in aanmerking komende transacties.
* Deze secties maken nauwkeurige categorisatie van BTW-bedragen mogelijk, wat naleving van BTW-regelgeving en boekhoudnormen garandeert.

**Dynamische Auto Accounting Integratie**:

* Op basis van de gegevens die tijdens documentverwerking zijn geëxtraheerd, worden de relevante BTW-secties automatisch weergegeven op het Auto Accounting Scherm.
* Dit zorgt ervoor dat gebruikers BTW-invoeren snel kunnen valideren en aanpassen zonder handmatige berekening of herinvoer, wat de workflow stroomlijnt.

**Export naar Infor LN**:

* De BTW-gegevens, inclusief alle relevante secties en classificaties, worden naadloos geëxporteerd naar Infor LN, wat consistentie garandeert tussen documentverwerking in DocBits en het ERP-systeem (Enterprise Resource Planning).
* Geëxporteerde gegevens zijn gekoppeld aan de respectievelijke kostenregels in Infor LN, wat duidelijke traceerbaarheid en nauwkeurige financiële rapportage handhaaft.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/MultipleTaxLInes.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/MultipleTaxLineAuto%20Accounting.png)

### Dashboard Verbeteringen

DocBits heeft aanzienlijke updates aan het dashboard geïntroduceerd, met focus op bruikbaarheid, efficiëntie en verbeterde gegevenszichtbaarheid. Deze verbeteringen omvatten een nieuw "Toegewezen aan Groep" filter en een geoptimaliseerde UI voor Document Logs, waardoor het gemakkelijker wordt voor gebruikers om met hun documenten te werken en ze te beheren.

### PO Matching Verbeteringen

DocBits introduceert verschillende bruikbaarheidsverbeteringen voor het PO Matching Scherm, ontworpen om het proces van het matchen van inkooporderregels (PO) met facturen te stroomlijnen. Deze verbeteringen bieden meer intuïtieve controles voor het selecteren van meerdere regels en bieden duidelijke visuele indicatoren voor het verwerken van verouderde PO-gegevens.

**Ctrl + Klik voor Individuele Regelselectie**:

* Gebruikers kunnen nu de Ctrl-toets ingedrukt houden en op specifieke regels klikken om meerdere, niet-aaneengesloten rijen op het PO-matchingscherm te selecteren.

**Shift + Klik voor Bereikselectie**:

* Gebruikers kunnen een reeks rijen selecteren door de Shift-toets ingedrukt te houden, op de eerste rij te klikken en vervolgens op de laatste rij. Alle rijen tussen de eerste en laatste selectie worden automatisch geselecteerd.

**Automatische Detectie van Verouderde Gegevens**:

* Als de PO-gegevens die aan een factuur zijn gekoppeld oud zijn (op basis van systeeminstellingen), wordt een pictogram weergegeven om de gebruiker te waarschuwen. Deze visuele indicator zorgt ervoor dat gebruikers zich bewust zijn van verouderde gegevens die mogelijk niet de laatste updates in de inkooporder weerspiegelen.

### Bugfixes

* Een probleem opgelost om ervoor te zorgen dat alle mogelijke waarden correct worden weergegeven tijdens auto-accountingprocessen
* De gebruikersinterface van Workflow Logs verbeterd om navigatie en bruikbaarheid intuïtiever te maken
* De documentvelden bijgewerkt om aanvullende informatie weer te geven, zoals vereiste en verborgen vlaggen, direct in de gebruikersinterface
* Zichtbaarheid van groepsbeschrijvingen toegevoegd in de groepsinstellingen
* Lengterestricties voor groepsnamen weergegeven tijdens het aanmaken om fouten te voorkomen
* Problemen in de testfunctionaliteit van de beslisboom aangepakt en vertaalinconsistenties opgelost
* De zoekfunctionaliteit in Workflow Logs verbeterd voor nauwkeurigere en effectievere zoekresultaten
* Een probleem opgelost om te voorkomen dat gebruikers per ongeluk e-document concepten verwijderen
* Bugs in het e-mail importproces opgelost om naadloze integratie en gegevensverwerking te garanderen
* Problemen opgelost met het opslaan van AI-gegenereerde tags, wat consistente gegevensretentie garandeert
* Een sorteerprobleem gecorrigeerd dat optrad bij het toepassen van sortering over verschillende pagina's van het dashboard
* De documentteller verbeterd om het aantal documenten dat door DocBits is verwerkt nauwkeurig weer te geven
* Vertalingen door de applicatie verbeterd om bruikbaarheid voor verschillende talen te verbeteren

## Release Hot Fix Feast 17 december 2024

### **DocBits Verbeteringen:**

#### E-mail Import Verbeteringen

* Gebruikers kunnen nu naadloos XML- en EDI-bestanden importeren via de E-mail Import functie.

## Release Hot Fix Feast 27 november 2024

### DocBits Verbeteringen:

#### Verbeterde PO Optimalisatie

* **Geoptimaliseerd Opslagmechanisme**: Het opslagproces is gestroomlijnd om alleen plaats te vinden nadat de gebruiker de matching voltooit, wat redundante opslagen vermindert en efficiëntie verbetert.
* **Verbeterde Asynchrone Export**: Exportfunctionaliteit draait nu asynchroon, wat soepelere bewerkingen en een verbeterde algehele gebruikerservaring garandeert.

#### Workflow Verbeteringen

De workflowfunctionaliteit is geüpgraded om een betere gebruikerservaring te bieden:

* **Verbeterde Logs**: Workflow logs hebben nu een schonere, intuïtievere interface, wat het gemakkelijker maakt om procesdetails te bekijken en begrijpen.
* **Verbeterde Responsiviteit**: Workflow executieprocessen zijn geoptimaliseerd voor snellere en betrouwbaardere prestaties, wat snellere taakvoltooiing en verminderde vertragingen mogelijk maakt.

#### Verbeterde Applicatie Caching

We hebben geavanceerde caching-strategieën over de applicatie geïmplementeerd om gegevensopvraging te optimaliseren en laadtijden te verminderen. Deze verbeteringen verbeteren de algehele bruikbaarheid door soepelere navigatie en een meer responsieve gebruikerservaring te garanderen, vooral voor vaak gebruikte functies.

#### Dashboard en UI Upgrades

* **Dashboard Verbeteringen**: Het dashboard is vernieuwd met een verbeterde lay-out en extra functies om navigatie te vereenvoudigen en zichtbaarheid van belangrijke metrieken te verbeteren.
* **UI Verbeteringen**: De gebruikersinterface over de applicatie is verfijnd voor een modernere, intuïtievere en gebruiksvriendelijkere ervaring, wat het voor gebruikers gemakkelijker maakt om hun taken met minimale inspanning te volbrengen.

### Bugfixes:

1. De fuzzy logica verbeterd om nauwkeurigere en betrouwbaardere gegevenspopulatie na extractie te garanderen.
2. Bekende bugs die groepen en rechten beïnvloedden opgelost, wat naadloos toegangsbeheer en rolfunctionaliteit garandeert.
3. Inconsistenties in vertalingen over de applicatie aangepakt, wat duidelijkheid en lokalisatie verbetert.
4. Lay-out-gerelateerde problemen opgelost, wat een consistente en geoptimaliseerde gebruikersinterface over alle configuraties garandeert.
5. Fouten in de master data lookup-functionaliteit gecorrigeerd, wat nauwkeurige en betrouwbare gegevensopvraging garandeert.
6. Problemen met e-mail importfunctionaliteit over alle beschikbare opties opgelost, wat soepele en foutloze bewerkingen garandeert.

## Release Feast 4 november 2024

### Nieuwe Functies:

#### E-mail Import Verbeteringen

Geconfigureerde IMAP e-mailinstellingen om automatisch notificaties te verzenden voor importresultaten. Succesvolle importnotificaties bevestigen de verwerkte bestanden, terwijl foutmeldingen de bestandsnamen en specifieke foutdetails bevatten voor snelle troubleshooting.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/EmailImport.png)

#### Master Data Lookup Vernieuwing

De master data lookup-instellingen zijn vernieuwd met verfijnde categorisatie, wat snellere en preciezere opvraging van diverse master data-types mogelijk maakt. Deze verbetering stroomlijnt gegevenstoegang door master data in verschillende categorieën te organiseren, wat zoekefficiëntie en nauwkeurigheid aanzienlijk verhoogt. Gebruikers kunnen nu sneller de relevante gegevens vinden, wat productiviteit en besluitvorming over de applicatie verbetert.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/MasterDataLookup.png)

#### Prestatieverbeteringen

Een robuust caching-mechanisme geïmplementeerd om applicatieprestaties aanzienlijk te verhogen, vooral onder hoge verzoekdruk. Deze verbetering vermindert serververwerkingstijd door vaak geopende gegevens tijdelijk op te slaan, wat snellere responstijden en een soepelere gebruikerservaring mogelijk maakt. Het nieuwe caching-systeem beheert verhoogd verkeer efficiënt, wat betrouwbare en schaalbare prestaties garandeert, zelfs tijdens piekgebruiksperioden.

#### Verbetering van Document Vergrendeling Functie

De documentvergrendelingsfunctionaliteit is geüpgraded om gelijktijdige bewerkingen te voorkomen, wat gegevensintegriteit garandeert en conflicten minimaliseert. Nu worden documenten automatisch vergrendeld tijdens actieve bewerking, wat gebruikers duidelijke indicatoren biedt wanneer een document in gebruik is en voorkomt dat anderen wijzigingen aanbrengen totdat de bewerkingssessie is voltooid. Deze verbetering stroomlijnt samenwerkende workflows en vermindert het risico op gegevensoverschrijvingen.

#### Navigatie en Gebruikerservaring Verbeteringen

* **Breadcrumb Navigatie**: Breadcrumb trails toegevoegd over applicatiepagina's om navigatie te verbeteren, waardoor gebruikers eenvoudig eerdere secties kunnen volgen en naar teruggaan voor een intuïtievere browse-ervaring.
* **Gestroomlijnde Gebruikersinterface**: De "nieuwe versie" pop-up notificatie verwijderd om een soepelere, ononderbroken workflow te creëren, wat afleidingen vermindert en algehele bruikbaarheid verbetert.

### Bugfixes:

* Gebruikersspecifieke problemen opgelost, zoals bijlageproblemen bij versleutelde of ondertekende e-mails.
* Kaartweergave- en flowproblemen opgelost.
* Routeringsproblemen met Volgende/Vorige knoppen gecorrigeerd.
* Bugs met betrekking tot beslisboomtabellen aangepakt.
* UI voor het wachtwoordveld bijgewerkt om bruikbaarheid te verbeteren.
* Problemen met de taakteller die niet correct werd weergegeven opgelost.
* Een gebruikersinterfaceprobleem met de AI-tabel gecorrigeerd.
* Fouten met documentextractie tijdens tabeltraining opgelost.
* Een waarschuwing toegevoegd wanneer een PO wordt gematcht tijdens herformattering, en ervoor gezorgd dat gematchte rijen worden verwijderd.
* Datumformattering gecorrigeerd, zodat gegevens correct worden geladen per dag- en weekfilters, en ervoor gezorgd dat documenttypen correct worden weergegeven.
* De weergave van documenten op dubbele monitors gecorrigeerd.
* Een probleem opgelost waarbij het ontkoppelen van één PO-regel alle regels zou verwijderen.
* Onjuiste vertalingen over de applicatie opgelost.
* Het probleem opgelost waarbij lange beschrijvingen in regelbeheer scrollen op de lijst veroorzaakten.
* Ontbrekende "Toewijzen aan" functionaliteit voor niet-admin gebruikers hersteld.

## Release Harvest 9 september 2024

#### Nieuwe Functies

### Afhandeling van Dubbele Facturen

Deze functie stelt gebruikers in staat om te identificeren of documenten gedupliceerd zijn in hun systeem. Deze functie werkt door documentvelden te analyseren die door de gebruiker kunnen worden geconfigureerd. Door specifieke velden te selecteren, kunnen gebruikers de detectiecriteria aanpassen aan hun behoeften, zodat alleen relevante duplicaten worden gemarkeerd. Dit helpt gegevensintegriteit te behouden en vermindert de rommel van redundante documenten, wat documentbeheerprocessen stroomlijnt.

{% embed url="https://youtu.be/8CdBu7HN47I" %}

### Beslisboom

De beslisboom is een hulpmiddel dat wordt gebruikt om besluitvorming in een workflow te automatiseren door keuzes en hun uitkomsten in kaart te brengen. Door beslisbomen te integreren, kunt u consistente beslissingen garanderen op basis van specifieke criteria, processen stroomlijnen en fouten verminderen. Deze aanpak verbetert efficiëntie door complexe beslispunten binnen de workflow te automatiseren.

{% embed url="https://youtu.be/E7cx8BDGTI0" %}

### AI Modellen Kiezen

DocBits stelt gebruikers nu in staat om te wisselen tussen verschillende AI-modellen om beter aan hun behoeften te voldoen. U kunt het AI-model kiezen dat het beste past bij uw specifieke use case, of het nu gaat om documentanalyse, gegevensextractie of tekstclassificatie. Deze flexibiliteit stelt u in staat prestaties te optimaliseren en nauwkeurigere resultaten te bereiken, waarbij de mogelijkheden van de AI worden afgestemd op de unieke vereisten van uw organisatie.

{% embed url="https://youtu.be/YvgEVagPepY" %}

### OCR Versie Kiezen

DocBits biedt nu de mogelijkheid om de OCR (Optical Character Recognition) versie te wijzigen die binnen het platform wordt gebruikt. Gebruikers kunnen verschillende OCR-versies selecteren op basis van hun specifieke behoeften, wat betere nauwkeurigheid en compatibiliteit met verschillende documenttypen garandeert. Deze functie maakt preciezere tekstextractie uit afbeeldingen en gescande documenten mogelijk, wat de algehele gegevenskwaliteit en workflow-efficiëntie verbetert.

{% embed url="https://youtu.be/zkW8zj0H5Ko" %}

## Release Sunset 12 augustus 2024

### Nieuwe Functies:

## Rule Manager

[rule-manager](../../administration-and-setup/settings/document-processing/rule-manager/ "mention") biedt de flexibiliteit om conflictoplossingsregels te creëren en bewerken die zijn afgestemd op het DocBits factureringssysteem. Deze regels zijn ontworpen om automatisch discrepanties tussen factuurdetails en inkoopordergegevens (PO) af te handelen, wat nauwkeurige financiële reconciliatie garandeert. Het systeem past deze regels toe om factuurregels, kosten en belastingen te verwerken, en genereert waar nodig passende aanpassingen of notities.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/RuleManager.png)

### Gegevens Synchroniseren met Stream

BOD-synchronisatie van Infor maakt gebruik van AWS Stream voor real-time gegevensverwerking, wat efficiëntie verbetert en de synchronisatietijd van gegevens aanzienlijk vermindert.

### XRechnung

DocBits verwerkt nu XRechnung (elektronische facturen) naadloos door eerst een gebruiksvriendelijke PDF te creëren, wat de factuurverwerkingsworkflow stroomlijnt en vereenvoudigt.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/XRECHNUNG.png)

### Bugfixes:

1. PO Match Knop Zichtbaarheid\
   Probleem: PO Match knop is beschikbaar wanneer er geen tabel is of de tabel is verwijderd.\
   Status: Bij veldvalidatie wordt PO Match verborgen als er geen tabel is of de tabel is verwijderd
2. Tabel Drag & Drop Sorteren\
   Probleem: Tabel Drag & drop voor sorteren op alle Lijsten/Dashboards\
   Oplossing: Gebruiker kan nu slepen en neerzetten om de tabel te sorteren
3. Validatiescherm Toolbar\
   Probleem: Validatiescherm: toolbar rechterkant niet scrollbaar\
   Oplossing: Opgelost
4. Horizontaal Scrollen\
   Probleem: Horizontaal Scrollen op Goedkeuringsscherm\
   Oplossing: Opgelost
5. Goedkeuringsscherm Beslissing Wissen\
   Probleem: Mogelijkheid om de goedkeur/afwijs beslissing op goedkeuringsscherm te wissen\
   Oplossing: Opgelost
6. Taakweergave op Goedkeuringsscherm\
   Probleem: Taak getoond op het Goedkeuringsscherm\
   Oplossing: Toolbar is beschikbaar die de taken telt van open/in uitvoering
7. PO Match Tabel Grootte\
   Probleem: PO Match tabel wordt kleiner na het matchen van een regel\
   Oplossing: Opgelost
8. Taaktoewijzing op basis van Artikel Inkoop Groep\
   Probleem: Vertaling voor inkoop groep toewijzing\
   Oplossing: Opgelost
9. Leveranciersnaam en Id in Taak Aanmaken\
   Probleem: Leveranciersnaam en Id toevoegen in Taak aanmaken\
   Oplossing: Leveranciersnaam en Id worden uit het document gehaald
10. Document Subtype Kopiëren\
    Probleem: Klikken op Kopieer Document Subtype uit subdocument type instelling werkte niet\
    Oplossing: Opgelost
11. Nieuw Label Veld\
    Probleem: Nieuw Label veld in lijst van waarden om label toe te voegen samen met waarde en synoniem\
    Oplossing: Opgelost
12. Land van Oorsprong Kaart in Workflow\
    Probleem: Nieuwe Kaart in workflow die land van oorsprong van een leverancier controleert en een taak aanmaakt of doorgaat met het verwerken van document dienovereenkomstig\
    Oplossing: Opgelost
13. Dark Mode Fix op instellingen zoekbalk\
    Probleem: Dit probleem was eerder geïdentificeerd\
    Oplossing: Opgelost
14. Geëxtraheerde Tabel Kolom Zichtbaarheid Indicator\
    Probleem: Indicator als Kolommen zijn verborgen in geëxtraheerde tabel op Veldvalidatie\
    Oplossing: Opgelost
15. Dashboard Toewijzing voor Admins\
    Probleem: Toewijzen aan op het dashboard alleen voor admins maken\
    Oplossing: Opgelost
16. Document Splitsen Zichtbaarheid\
    Probleem: Document splitsen alleen tonen wanneer er meer pagina's zijn\
    Oplossing: Opgelost
17. Factuur Dashboard Kolommen\
    Probleem: Extra kolommen op factuur dashboard\
    Oplossing: Opgelost
18. Veldvalidatie Script Deactivering\
    Probleem: Veldvalidatie- Deactiveer script werkte niet correct\
    Oplossing: Opgelost
19. Goedkeuringslayout Knop Aanpassing\
    Probleem: Kan het knoptype en stijl niet wijzigen op goedkeurings layout builder\
    Oplossing: Opgelost
20. Data Sync Tabel\
    Probleem: Data Sync Tabel in instellingen\
    Oplossing: Opgelost
21. Dashboard Analytics Totaal Weergave\
    Probleem: Dashboard Analytics- tonen verkeerd totaal nummer\
    Oplossing: Opgelost

## Release Firework 8 juli 2024

### Nieuwe Functies

**Regelkosten Export naar M3**

• Exporteer regelkosten naar M3 met passende kostenlementen volgens uw bedrijfsbehoeften.

**PO & Factuur Discrepantie Afhandeling**

• Slimme afhandeling van discrepanties in hoeveelheid, prijzen, kosten en belasting.

### Belangrijkste Bugoplossingen

#### 1. PO Zoekfunctionaliteit

• Probleem: PO-zoeken werkte niet.

• Status: Dit probleem is geïdentificeerd en zal niet worden aangepakt in deze release.

#### 2. PO Matching Connectie

• Probleem: PO matching connectie werd niet verwijderd zoals verwacht.

• Oplossing: Opgelost om naadloze PO matching bewerkingen te garanderen.

#### 3. Geëxporteerde Document Waarschuwingen

• Probleem: Geëxporteerde documenten hadden waarschuwingen voor kostenlementen zelfs wanneer het systeem er niet voor was ingesteld.

• Oplossing: Gecorrigeerd om onnodige waarschuwingen te voorkomen, wat nauwkeurige documentexporten garandeert.

#### 4. Advance Shipment EDI Weergave

• Probleem: Advance shipment EDI-weergave toonde ID's in de titel.

• Oplossing: Titels worden nu correct weergegeven, wat de leesbaarheid van gegevens verbetert.

#### 5. Berekeningsfouten in Splitsen op Totaal Probleem

• Probleem: Berekeningsfouten traden op wanneer regels verder werden gesplitst.

• Oplossing: Opgelost om nauwkeurige berekeningen in alle scenario's te garanderen.

#### 6. PO Scherm Tabel Weergave

• Probleem: Geen tabel werd getoond op het PO-scherm.

• Oplossing: Weergaveprobleem opgelost om ervoor te zorgen dat tabellen correct verschijnen.

#### 7. Auto Export op Orderbevestiging

• Probleem: Auto export werkte niet.

• Oplossing: Functionaliteit hersteld om ervoor te zorgen dat automatische exports soepel werken.

#### 8. Mismatch Probleem op PO

• Probleem: Mismatch probleem op PO toonde ondanks dat alles identiek was op de Leveringsbon.

• Oplossing: Opgelost om nauwkeurige mismatch detectie te garanderen.

#### 9. Rapport Download Problemen

• Probleem: Rapporten werden niet gedownload.

• Oplossing: Opgelost om naadloze rapport downloads mogelijk te maken.

#### 10. Onjuiste Totaal en Netto Bedragen

• Probleem: Totaal en Netto bedragen toonden onjuiste waarden.

• Oplossing: Waarden gecorrigeerd om financiële nauwkeurigheid te garanderen.

#### 11. Factuurdatum Formaat op Dashboard

• Probleem: Factuurdatum kolom had verkeerde formaatwaarden.

• Oplossing: Data worden nu in het juiste formaat weergegeven, wat bruikbaarheid verbetert.

#### 12. Workflow Vertragingen bij "Klaar voor Validatie"

• Probleem: Workflow vertragingen traden op bij "Klaar voor Validatie" tot feedback van Doc2flow.

• Oplossing: Workflow timing verbeterd voor snellere validatieprocessen.

## Volgende Release Firework 8 juli 2024

### Probleem:

Het bestaande systeem mist geautomatiseerde regels voor het nauwkeurig matchen en verwerken van factuurkosten tegen inkooporders (PO's). Dit handmatige proces kan tot discrepanties leiden, zoals geïllustreerd in de screenshots, waar factuurkosten en PO's reconciliatie nodig hebben voor correcte facturering.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Bildschirmfoto%202024-06-07%20um%2017.11.37.png)

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Bildschirmfoto%202024-06-07%20um%2017.11.46.png)

### Oplossing:

Met de nieuwe Rule Manager in DocBits, die in juli wordt gelanceerd, kunt u dit proces automatiseren:

#### 1. Regels Aanmaken:

Definieer criteria (bijv. Hoeveelheid > PO Hoeveelheid) voor factuurregel items.

#### 2. Acties Instellen:

Breng velden en acties in kaart om gegevens naadloos te exporteren naar Infor.

#### 3. Regels Testen:

Valideer regels met voorbeeldgegevens om nauwkeurigheid te garanderen.

## Junebug Release Notes - 10 juni 2024

Deze update brengt spannende nieuwe functies en bugfixes naar Junebug:

**Nieuwe Functies:**

* **Geautomatiseerde Kosten Extractie:** Junebug extraheert en brengt nu automatisch kosten in kaart binnen uw Docbit-documenten. Dit elimineert handmatige gegevensinvoer en stroomlijnt uw workflow.
* **Portal Export naar Infor IDM:** De nieuwe Portal stelt u in staat om leveranciersdocumenten moeiteloos direct naar Infor IDM te exporteren. Dit vereenvoudigt zendingsverwerking en vermindert handmatige interventie.
* **Oorsprong Identificatie (AI):** Junebug introduceert een krachtige AI-functie die automatisch de oorsprong van documenten leert. Dit bespaart u tijd en moeite bij documentclassificatie.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/POShipmentTable.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ApprovalScreen2.png)

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/ApprovalScreen1.png)

**Bugfixes:**

* **QR Code Fix:** Een probleem dat eerder problemen veroorzaakte met QR-codeverwerking is opgelost.
* **Niet-EDI Document Afhandeling:** Junebug verwerkt niet-EDI documenten nu effectiever.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/EDI810-Invoice.png)

Hotfix - 5 Juni [**Priority System**](../../end-user-and-partner-section/end-user-section/our-document-priority-system.md)

## Volgende Release - Junebug Release 10 juni 2024

Sandbox Freeze - 3 juni 2024

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/Bildschirmfoto%202024-05-08%20um%2020.37.35.png)

In de komende release zal een belangrijke verbetering aan de classificatie- en extractiemogelijkheden worden geïntroduceerd, specifiek gericht op tabelregels binnen documenten. Deze nieuwe functie stelt gebruikers in staat om te definiëren of een regel in een tabel een kost vertegenwoordigt. Deze functionaliteit is bijzonder nuttig in gedetailleerde financiële documenten, zoals facturen, waar het onderscheid maken tussen verschillende soorten transacties—zoals kosten, belastingen of vergoedingen—cruciaal is voor nauwkeurige verwerking en administratie.

**Belangrijke Punten voor Release Notes:**

* **Verbeterde Tabel Regel Classificatie**: Gebruikers kunnen nu specificeren of een bepaalde regel in een documenttabel een kost is, wat de nauwkeurigheid en granulariteit van gegevensextractie verbetert.

## Maypole Release 5.55.8.10 - (17 mei)

### Release Notes - Web App

#### Nieuwe Functies:

▪ Workflow Kaart Vertaling: Verbeteringen in de workflow, inclusief kaartvertaling voor betere lokalisatieondersteuning.

▪ E-mail Import Logging: Gedetailleerde logging toegevoegd voor e-mail imports om troubleshooting en monitoring te verbeteren.

▪ Broken Fuzzy Screen Fix: Een probleem opgelost met broken fuzzy screen weergave over verschillende interfaces.

▪ Accounting Updates: Het accountingproces verbeterd door verouderde accountingmethoden te verwijderen en kosten efficiënter te integreren.

#### Verbeteringen:

▪ Ruiz Workflow Verbeteringen: Bugs opgelost met betrekking tot workflownavigatie, vooral met betrekking tot verborgen stappen.

▪ Gebruikersinterface Aanpassingen: Gebruikersinterface-elementen verbeterd zoals contante kortingstermijnen onder betalingstermijnen voor betere duidelijkheid en gebruikerservaring.

▪ Prestatieverbeteringen: Verschillende backend verbeteringen om systeemprestaties en stabiliteit te verbeteren.

#### Bugfixes:

▪ Approval Stamp Issue: Kritieke problemen opgelost rondom het goedkeuringsstempelproces om naleving en correcte functionaliteit te garanderen.

▪ Key Addition: Noodzakelijke sleutels terug aan het systeem toegevoegd om gegevensintegriteit en systeemfunctionaliteit te garanderen.

▪ Master Data Field Adjustment: Een probleem in het master data veld aangepakt om af te stemmen op gebruikersvereisten.

#### Technisch:

▪ Versie Updates: Routineupdates aan verschillende systeemcomponenten om af te stemmen op huidige normen en technologieën.

▪ Merge Activiteiten: Talrijke merges om functies, fixes en verbeteringen van meerdere ontwikkelingsbranches te integreren in de hoofdbranch.

### What's New - API

▪ Cache Management Verbeteringen: De get\_receive\_delivery\_cache bijgewerkt om prestaties en betrouwbaarheid te verbeteren.

▪ Nieuwe Functies voor Verkooporders: Een voorbeeldfunctie geïntroduceerd voor verkooporders, wat visualisatie en beheer van ordergegevens verbetert.

▪ Document Afhandeling Verbeteringen: Geautomatiseerde testjobs toegevoegd voor demotesting en sandbox-omgevingen om robuustheid te garanderen.

▪ Verbeterde Cache Functionaliteit: field\_id toegevoegd om cachingmechanismen verder te verbeteren.

#### Fixes en Verbeteringen

▪ Office E-mail Import Aanpassingen: Noodzakelijke aanpassingen gemaakt aan de Office E-mail Import functie om functionaliteit te verbeteren.

▪ Ontwikkelingsverbeteringen: Meerdere merges van dev naar hoofdbranches om synchronisatie en stabiliteit over omgevingen te garanderen.

#### Diversen

▪ Configuratie Updates: Verschillende updates aan de configuratiebestanden om systeemsetup en parameters te verbeteren.

### Release Notes - Workflow

#### Verbeteringen:

▪ Een nieuwe workflow test geïmplementeerd die nu kan worden ingeschakeld tijdens import, wat flexibelere testscenario's mogelijk maakt.

▪ De loggingfunctionaliteit voor actiekaarten verbeterd, wat debugging en monitoring efficiënter maakt.

▪ Verbeterde compatibiliteit voor veldvergelijkingskaarten met datum- en enum-types, wat soepelere vergelijkingen en validaties garandeert.

▪ De belastingkaart bijgewerkt en de retourprocessen voor actiekaarten aangepast om bewerkingen te stroomlijnen.

#### Fixes:

▪ Problemen aangepakt met documentstatusupdates, zodat ze nauwkeurig worden weerspiegeld in het systeem.

▪ De berekening voor de vergelijkingskaart met betrekking tot eenheidsprijs en hoeveelheid gefixeerd om discrepanties correct af te handelen.

▪ Meerdere kleine bugs opgelost en stabiliteitsverbeteringen aangebracht.

#### Operationele Wijzigingen:

▪ Meerdere ontwikkelingsfasen samengevoegd in de sandbox en stage branches, wat een aanzienlijke integratie van nieuwe functies en fixes weerspiegelt.
