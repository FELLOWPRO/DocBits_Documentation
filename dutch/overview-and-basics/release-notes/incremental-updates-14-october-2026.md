# Hotfixes 14 oktober 2026

_Wat er verandert met de DocBits-productiehotfix van 14 oktober 2026 (release R1.0.15), inclusief alles sinds de_ [_hotfix van 15 september_](incremental-updates-15-september-2026.md)_. Elke service vermeldt de versie die wordt uitgerold, gevolgd door wat er nieuw of opgelost is — in gewone taal. Services die niet zijn vermeld, hadden geen wijzigingen die zichtbaar zijn voor klanten._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/nl.mp4" %}

***

## Hoogtepunten

* **De Settings Assistant.** Een chatbalk op elke instellingenpagina beantwoordt vragen over de inrichting van uw organisatie, in uw taal en op basis van de DocBits-documentatie. De assistent leest de actuele stand van uw instellingen en legt die uit (groepsrechten, importkanalen, purchase order schakelaars, boekhouding). Als u vraagt om iets in of uit te schakelen, toont hij eerst een voorbeeld, wacht op uw bevestiging en biedt een ongedaanmaking aan. "Open setting" springt rechtstreeks naar de instelling, ook binnen een ingeklapte sectie, en markeert die. Organisatiebeheerders schakelen de assistent in of uit bij Bedrijfsgegevens. Hij beantwoordt alleen DocBits-vragen en wijzigt nooit iets zonder bevestiging.
* **Nieuwe AI-niveaus.** De niveaus Fast en Full draaien op nieuwe modellen. Een nieuw niveau Auto kiest per document Fast of Full, en Nexus Flash komt naast Nexus. Een visionmodus (hybrid of auto) bepaalt wanneer de pagina-afbeelding wordt meegestuurd. Opgeslagen voorkeuren voor AI-modellen schuiven vanzelf door naar de nieuwe niveaus, en schermen tonen alleen niveaunamen. "Use AI" is een keuzelijst (Standard, Yes, No) met een voorbeeld van wat de gestructureerde extractie zal opvragen.
* **Controle van kopvelden.** Het validatiescherm heeft een knop "Header field check" naast Opslaan. Het rapport toont voor elk kopveld waar de waarde vandaan kwam (AI, regel, script of stamgegevens), in een compacte tabel met bronfilter, zoekfunctie en sortering, en met dezelfde veldlabels als het validatiescherm. De herkomstpopup toont de bron van elke waarde in één strook.
* **Beveiliging bij aanmelden en voor organisaties.** Een MFA-uitdaging kan op elk aanmeldpad slechts één keer worden gebruikt, en voor het registreren van een authenticator is de e-mailcode nodig. Organisaties beheren een lijst met geverifieerde e-maildomeinen; een social login (bijvoorbeeld Microsoft) sluit aan bij de organisatie die het domein vermeldt en maakt nooit zelf een organisatie, gebruiker of abonnement aan. Alleen organisatiebeheerders wijzigen organisatievoorkeuren en schrijven of keuren purchase order matchregels goed. Gecachte antwoorden kunnen niet langer tussen organisaties lekken.
* **Purchase order matching en toeslagen.** Toeslagen die de purchase order als nul verwacht, krijgen een absolute ondergrens, de toeslagtolerantie geldt ook voor toeslagen die de order niet begroot, en één veld kan meerdere kostenelementen vermelden waarvan de bedragen naar verhouding met de purchase order worden verdeeld. Een matchkolom kan een vlag "allow mismatch" dragen. Workflowkaarten vergelijken toeslagen per lijst, en de uitvoeringslimiet van workflows stijgt van 30 naar 50.
* **Minder verkeerde getallen.** Bedragen worden getoond in het persoonlijke formaat van elke gebruiker (inclusief Zwitserland en Slovenië), waarden met alleen een datum behouden hun kalenderdag in elke tijdzone, de US-totaalvergelijking houdt rekening met extra bedragen en facturen met meerdere btw-tarieven, en documenten met kopbedragen van 0,00 vallen niet meer in de verkeerde kandidaatronde.

***

## Ook opgelost in deze release

* Het dashboard blijft niet langer leeg wanneer een race het filter voor de suborganisatie op de organisatie-id zet en daarmee elk document uitsluit.
* Dimensiewaarden kunnen weer door elke gebruiker worden geselecteerd.
* Een door een klant gemelde uploadfout is opgelost.
* "Match on total" werkt voor leveranciers van wie de factuur één regel heeft, en voor de leveranciersinrichtingen die dit hebben gemeld.
* SPS e-documents: de 810-toeslagen zijn aangepast, de lay-out van de 855-toeslagen is bijgewerkt en het klantlogo in de e-documentvoorbeeldweergave is gecorrigeerd.

***

## Web App — `10.78.9.4`

**Settings Assistant**

* Een chatpaneel aan de rechterkant met een schakelaar staat op alle instellingenpagina's. Het gesprek blijft behouden bij paginawissels, is beperkt tot 20 berichten en toont de toegepaste wijzigingen met een ongedaanmaking.
* Begroet u met vragen die passen bij de huidige instellingenpagina en toont instellingskaarten met een aan/uit-schakelaar. Esc sluit eerst menu's, Stop breekt een lopend antwoord af en schermafbeeldingen in antwoorden openen in een lightbox.
* Het toepassen van een wijziging opent een dialoogvenster met voorbeeld, bevestiging en ongedaanmaking.
* Elke instelling is doorzoekbaar vanuit de zijbalk, en de gevonden instelling wordt in een andere kleur gemarkeerd. "Open setting" scrolt naar het doel binnen een ingeklapte accordeon.
* Een schakelaar voor organisatiebeheerders voor de assistent staat bij Bedrijfsgegevens.
* AI-adviezen worden toegeschreven aan Nova, en alleen niveaunamen verschijnen, nooit model-id's.

**Validatiescherm en documentafhandeling**

* Nieuwe knop "Header field check" met rapport, herkomst per veld en helppagina (zie Hoogtepunten). Bronlabels en statuschips blijven binnen hun cellen.
* De tekstbadges "from master data" naast veldlabels zijn verdwenen; de herkomstpopup bevat die informatie.
* Eén gedeelde veldvalidatie draait overal, waardoor de algemene fout "One or more fields need validation" na Auto Accounting verdwijnt.
* Tooltips op de knoppen van de veldpopup (Verwijderen, Wissen, Bevestigen) leggen uit wat elke knop doet voordat u klikt.
* Een optimistische rij toont nu wat is opgeslagen, niet wat is getypt. Een kolomhermapping vraagt alleen om bevestiging wanneer een zichtbare kolom zijn mapping verliest.
* Pagina's voorbij de OCR-paginalimiet zijn alleen-lezen en gemarkeerd, ook in de Auto Accounting-viewer. Het oude importpaneel voor paginabeperking is verwijderd.
* Er verschijnt een PO-tabel voor elk purchase order nummer in een multi-PO-kopveld, en de Layout Builder benoemt PO-tabbladen naar de PO-tabelsleutel en meldt de module niet langer als uitgeschakeld wanneer de PO-tabel aan staat.
* De voorstelkaart toont de tolerantie in plaats van `[object Object]`, en het Approval-vergelijkingsscherm rondt geconfigureerde vergelijkingskolommen (artikelnummers) niet meer af.

**Accounts, instellingen en fouten**

* Elke foutmelding en aanmeldfout toont de trace-id van het mislukte verzoek, zodat support het kan terugvinden. WebSocket-fouten van het dashboard wijzen precies het verzoek af dat ze noemen.
* Bedrijfsgegevens vermeldt de e-maildomeinen van de organisatie.
* Beheerders kunnen de e-mail "Set your password" opnieuw verzenden vanaf de gebruikerspagina.
* Globale beheerders stellen de contractstart in de abonnementstabel in.
* Organisatiebeheerders zien het tabblad Executive Dashboard en de knoppen voor het toevoegen en verwijderen van XSLT. Leden slaan layouts op als hun eigen voorkeur.
* Een sessie zonder organisatie krijgt een duidelijke foutmelding en de organisatiekiezer in plaats van een leeg dashboard.
* Bedragen volgen het persoonlijke getalformaat van de gebruiker, en waarden met alleen een datum behouden hun dag in elke tijdzone.
* Stamgegevens sturen suborganisatie-id's alleen mee wanneer ze afwijken van de organisatie-id, en aangepaste stamgegevensheaders worden als headers verzonden.
* Het Tabellen-scherm knipt de keuzelijst "Use AI" niet meer af, de AI-hinttekst bedekt de trainingsregel niet meer, en de AI-tabel behoudt zijn directe knop Toepassen, met een headercontrole met alleen een icoon en een licentiemelding.
* Pictogrammen voor tabelextractie worden weer weergegeven nadat het oude pictogramlettertype is verwijderd.

**Takenbord**

* Het bord laadt zijn eerste pagina met minder dubbele verzoeken, Enter voert de zoekopdracht direct uit, late antwoorden worden aan de juiste zoekopdracht gekoppeld, de voettekst toont het werkelijke aantal treffers in plaats van de paginacapaciteit, en een verwijdering die in de ene organisatie is gestart, wordt geannuleerd voordat deze wordt verzonden als u van organisatie wisselt.

***

## API Service — `12.83.293`

**Settings Assistant en MCP**

* Chat-endpoint met vangrails: alleen DocBits-vragen, geen wijziging zonder bevestiging, onduidelijke of metavragen krijgen hulp in plaats van een weigering, en antwoorden streamen eerst kaarten en daarna tekst.
* Alleen-lezen bouwstenen voor elk instellingsgebied (groepsrechten, importkanalen, PO matching, boekhouding, e-maildomeinen), een catalogus van deeplinks met een zoekhulpmiddel voor instellingen, en documentatiezoeker met afbeeldingen uit de DocBits-documentatie.
* Toepassingsflow wave 1: voorbeeld, bevestiging en ongedaanmaking voor ondersteunde instellingen, één scoperegel voor alle drie, beveiligd tegen dubbele bevestiging en verloop.
* MCP-tools lezen in remote-modus nooit bestanden van de server, en fixture- en lab-tools draaien alleen op dev.

**AI**

* Nieuwe modellen achter de niveaus Fast en Full, het niveau Auto, Nexus Flash en de voorkeur voor de visionmodus. Opgeslagen `AI_MODEL`-voorkeuren worden naar de nieuwe niveaus verplaatst.
* "Use AI" documenteert wat gestructureerde extractie opvraagt.

**Beveiliging en isolatie**

* Alleen organisatiebeheerders wijzigen organisatievoorkeuren.
* De aanroep `/accounting/rebuild` traint alleen de organisatie van de aanroeper, weigert bij een mislukte organisatieopzoeking en antwoordt met 400 bij een ongeldige id.
* XSLT-, XML- en PDF-rendering weigeren toegang tot bestanden en netwerk, lossen geen externe includes op, en factuurbytes worden gesaneerd voordat ze de transformer bereiken. Gerenderde PDF-voorbeelden staan alleen vertrouwde afbeeldingshosts toe.
* Cachesleutels bevatten de organisatie en dezelfde identifier geeft altijd dezelfde sleutel, zodat een vreemde organisatie-id geen gecachte gegevens meer kan lezen. Organisatiebrede dashboardcache-wissingen bij elke documentwijziging zijn verdwenen.
* De lijst met e-maildomeinen van de organisatie wordt doorgegeven aan Auth.

**Purchase order matching en export**

* Een veld kan meerdere kostenelementen vermelden waarvan de bedragen naar verhouding met de PO worden verdeeld.
* Goedkeuringsvervangers verwijzen naar het actieve goedkeuringsverzoek, opgeslagen hersteld-goedkeuringen blokkeren niet meer, en een document dat op goedkeuring wacht, wordt voor export geweigerd.
* PDF/A-annotatie behoudt catalogus en ingebed XML, zodat e-facturen hun XML behouden na annotatie. UBL-facturen met de kale EN 16931 CustomizationID worden geclassificeerd (e-invoicenetwerk).
* GRPR rondt af op de 6 decimalen die M3 accepteert. Conversiefactoren naar de basismeeteenheid worden aan de bevroren regel toegevoegd.
* Zacht verwijderde trainingen en opmaakregels worden gerespecteerd, en MCP `update_document_fields` bevestigt geen schrijfactie meer die verloren is gegaan. `get_table_rules` antwoordt met een getypeerde misser, en een lege vertalingenpayload gebruikt zijn terugvaloptie.
* Sloveense bedragen gebruiken `sl_SI` en opgeslagen voorkeuren worden gemigreerd. Aangepaste classificatielabels die als UUID-id's worden verzonden, worden opgelost. Gedeelde dashboards behouden `created_by` en de deellijst bij een update.
* Foutframes van het dashboard bevatten de `request_id` van het verzoek, en elk mislukt JSON-antwoord bevat een trace-id.
* Het systeem herstart alleen ongezonde workers in plaats van de hele API-vloot en controleert de geregistreerde takenlijst correct. De wachtrij van de hang-monitor wordt weer verwerkt.

***

## Auth Service — `1.78.49`

* Een multifactor-uitdaging is op elk aanmeldpad eenmalig te gebruiken, niet alleen in de MCP-flow. Voor registratie is de e-mailcode nodig, na een login met gedeeld wachtwoord wordt geen registratietoken uitgegeven, en gebruikers worden op de hoogte gebracht wanneer een factor wordt geregistreerd.
* Organisaties beheren een lijst met e-maildomeinen, elk slechts één keer toewijsbaar. Een social login sluit aan bij de organisatie die het geverifieerde domein vermeldt, verzint nooit een organisatie, gebruiker of abonnement, en weigert zonder iemand te noemen, terwijl de beheerders worden geïnformeerd. De domeinen die Microsoft teruggeeft, worden afgehandeld.
* Elke geweigerde aanmelding bevat een trace-id. Beheerders kunnen de e-mail "Set your password" opnieuw verzenden. Het contractsaldo heeft een teken en de contractstart wordt geaudit.

## Auth Bridge — `0.5.7`

* De replicatie van EU- en US-accounts houdt de verbinding gevoed tijdens de afstemming, koppelt een weggevallen replicatieslot zelf opnieuw, gebruikt begrensd geheugen en behandelt een bestaande replicatieorigin als succes. Aanmelden tussen regio's is betrouwbaarder.

## Docflow Service — `2.10.22`

* De aparte eenheidsprijskaart leest de standaard velddefinities van de organisatie voor toeslagen en vergelijkt elk kostenelement dat een veld vermeldt.
* De uitvoeringslimiet van workflows stijgt van 30 naar 50, en het doorzoeken van workflowlogs weigert een id die geen UUID is.

## Docnet Service — `1.56.15`

* `list_document_fields` meldt elke geconfigureerde tabelkolom, ook de kolommen die leeg zijn.

## Extraction Service — `1.56.0.1`

* Niveaus: nieuwe modellen achter Fast en Full, Auto, Nexus Flash en een visionmodus. Visionverzoeken aan de inferentiehost blijven onder de groottelimiet.
* Tabelextractie met Nexus bundelt pagina's in batches (twee per batch), draait batches parallel met een gemeten time-out, probeert tijdelijke fouten opnieuw en splitst een batch die een time-out kreeg. Kopvelden worden uit alle batches gelezen.
* US-totalen: extra bedragen maken deel uit van de totaalvergelijking, paar 1 telt mee in de bewaking van paar 2, kandidaten met een lage score worden overgeslagen wanneer belastingen niet nul zijn, en "above" en "below" herkennen labels van meerdere woorden.
* Identificatievelden herstellen tekens die echt voorkomen, en onzichtbare tekens worden behandeld naar hun betekenis, zodat een "O" niet meer in een vreemd teken verandert.

## Fulltext Service — `1.42.41`

* Nieuwe index voor de DocBits-documentatie, met ingest- en zoek-endpoints, afbeeldingen in antwoorden en een deadline voor de hele zoekopdracht. Deze voedt de Settings Assistant.

## PO Match Service — `1.59.48`

* Absolute ondergrens voor toeslagen die de purchase order als nul verwacht, en toeslagtolerantie voor toeslagen die de order niet begroot.
* Een kolom kan een vlag "allow mismatch" dragen. Meerdere kostenelementen per veld worden naar verhouding verdeeld.
* Alleen organisatiebeheerders schrijven of keuren matchregels goed, en regelvoorwaarden accepteren alleen een expressiegrammatica op een whitelist.
* Regelwijzigingen kunnen worden gesimuleerd tegen een overschrijvende regelset zonder te schrijven, voor Touchless-wijzigingsvoorstellen. Extra PO-kolommen om op te matchen worden gelezen uit het attribuut van het documenttype, met een migratie van de oude voorkeur.

***

_Niet geraakt in deze release: Auto Accounting, Barcode, E-Mail, FTP, Ideas, OCR, Operator. FTP en Operator bevatten alleen intern onderhoud._
