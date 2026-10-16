# NOVA — Grote release

**Versie-snapshot: 16 oktober 2026**

NOVA bevat alle functies die eerder als bèta in VESTA beschikbaar waren, nu als reguliere functies, naast begeleidende documentvalidatie, meer manieren om automatisering te verbeteren, duidelijkere e-factuurcontroles en betere controle over imports en documentverwerking. Deze notities beschrijven de klantgerichte toevoegingen in de hieronder vermelde serviceversies, vergeleken met de laatst gepubliceerde [VESTA hotfix, R1.0.15 van 14 oktober 2026](incremental-updates-14-october-2026.md), inclusief eerdere VESTA hotfixes.

De snapshot identificeert de builds die door deze notities worden gedekt. Voor beschikbaarheid in uw sandbox- of productieomgeving en het schakelen tussen kanalen, zie de [DocBits release lifecycle](../docbits-release-lifecycle-strategy.md). Functies met een schakelaar voor organisatie of documenttype moeten nog steeds door een beheerder worden ingeschakeld.

## Voormalige VESTA bètafuncties: opgenomen in NOVA <a href="#former-vesta-beta-features-included-in-nova" id="former-vesta-beta-features-included-in-nova"></a>

**Alle voormalige VESTA bètafuncties zijn nu onderdeel van de reguliere functieset van NOVA.** Voor klanten die de VESTA bèta niet hebben gebruikt, breidt dit de functies uit die beschikbaar zijn voor hun team, inclusief **Lay-outs beheren**, [**Aangepaste validatieregels**](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) en [**Transformatieregels**](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md). Organisatie-instellingen, schakelaars voor documenttypes en toegangsrechten blijven van toepassing.

Dezelfde voormalige bètafuncties worden reguliere VESTA-functies met de **volgende VESTA hotfix, gepland voor [11 november 2026](vesta-hotfix-11-november-2026.md)**. Deze aankondiging dekt de voormalige VESTA bètafuncties; de onderstaande secties beschrijven ook verdere NOVA-toevoegingen en verbeteringen.

## Wat NOVA toevoegt voor klanten <a href="#what-nova-adds-for-customers" id="what-nova-adds-for-customers"></a>

De onderstaande vergelijking dekt nieuw beschikbare voormalige bètafuncties, nieuwe mogelijkheden en uitbreidingen van bestaande functies. De VESTA-basislijn bevat functionaliteit die alleen in bèta beschikbaar was; de opname in de reguliere functieset van NOVA is een klantgerichte releasewijziging.

| Mogelijkheid | VESTA-basislijn (inclusief bèta) | Wat klanten krijgen met NOVA |
| --- | --- | --- |
| **Voormalige bètafuncties gebruiken** | Functies beschikbaar via VESTA bèta | **Reguliere NOVA-functies:** alle voormalige VESTA bètafuncties zijn opgenomen. De reguliere VESTA-introductie is gepland voor de hotfix van 11 november 2026. |
| **Hulp bij het valideren van een document** | Instellingenassistent en Header Field Check | **Nieuwe Validatieassistent:** identificeer blokkerende velden, spring naar de relevante waarde, bekijk voorgestelde correcties en houd de chat in een apart venster. |
| **Automatisering verbeteren vanuit dagelijkse correcties** | Touchless Intelligence dashboard, leveranciersdiagnose en wijzigingsvoorstellen | **Nieuw review- en meetproces:** dien verbeterverzoeken in, beoordeel geleerde regelvoorstellen, bekijk bewijs van beïnvloede documenten, rangschik kansen en meet resultaten na activering. |
| **E-factuurfouten begrijpen en oplossen** | E-documentcontroles, regencatalogus en XML-viewer | **Uitgebreide E-Invoice Validation:** rapporten gegroepeerd op validatieniveau, beleidscontroles en wijzigingsgeschiedenis, afwijzing vanuit het rapport en XML-inspectie binnen ondersteunde PDF-facturen. |
| **FTP/SFTP-imports beheren** | Importverbindingen en behoud of archivering van bronbestanden | **Nieuwe begeleidde setup en controles:** verbindingswizard, stapsgewijze logs, configureerbare retries en storingsmeldingen, en verwijdering van bronbestanden na succesvolle import. |
| **Werken met regels en lay-outs** | Regel-engines, uitvoerlogs en transformaties na masterdata-opzoeking; beheerpanelen vereisten een bètalink | **Bredere toegang en betere tools:** open beheerpanelen direct, zoek en bekijk doellay-outs, open de lay-outeditor van een document en leg de uitvoer van de lay-outselectie vast. |
| **Acties uitvoeren vanuit de Instellingenassistent** | Instellingenchat, voorbeeld/bevestig/ongedaan maken en proactieve waarschuwingen voor importgezondheid | **Aanvullende acties:** beheer mislukte verbindingen, bekijk de geschiedenis van deactiveringen, wijzig geselecteerde configuratie-items, maak een inactieve validatieregel vanuit een catalogus en bekijk pagina-uitleg. |
| **Documentverwerking beheren** | Limieten voor paginanummers per organisatie en documentherstart | **Nieuwe keuzes op documentniveau:** herstart met een gekozen aantal pagina's, bekijk verwerkte versus totale pagina's en kies of verborgen velden worden geëxtraheerd. |
| **Complexe leveringen matchen** | Matchen van inkooporders en handmatige koppeling van regels | **Flexibeler matchen:** selecteer regels in beide richtingen, behoud optioneel elke gematchte subregel van het document en groepeer exportverzoeken op geconfigureerde regelkolommen. |
| **Houd geëxporteerde en voltooide taken gescheiden** | Bestaande export- en Finished-workflows | **Nieuwe statuscontroles:** gebruik Exported voor opvolgbewerking, vergrendel optioneel Finished-documenten en vind documenten die door de workflow-uitvoeringslimiet zijn tegengehouden. |

### Schakel de functies in die configuratie vereisen

* **Validatieassistent:** een organisatiebeheerder schakelt deze in onder **Instellingen → Bedrijfsgegevens → Assistenten**. Deze is gescheiden van de Instellingenassistent en staat uit totdat deze is ingeschakeld.
* **Beoordeling van verbeteringen en adviesrapporten:** vereisen rechten als organisatiebeheerder en toegang tot Analytics. Geleerde voorstellen hebben een correctiegeschiedenis nodig. Voor een gemeten resultaat zijn voldoende gegevens en een voltooide opvolgperiode vereist.
* **Regel- en lay-outcontroles:** hun schakelaars voor inschakelen per documenttype zijn nog steeds van toepassing. NOVA maakt de beheerpanelen toegankelijk zonder bètalink.
* **Optioneel verwerkingsgedrag:** configureer FTP-opruiming en pogingen per verbinding. Eén-op-veel subregeluitbreiding en de vergrendeling van voltooide documenten zijn opt-in-instellingen.

Raadpleeg de [releaselifecycle](../docbits-release-lifecycle-strategy.md) voor beschikbaarheid in uw omgeving en het wisselen van releasekanalen.

## Bekijk de featurevideo's <a href="#watch-the-feature-videos" id="watch-the-feature-videos"></a>

Gebruik deze handleidingen naast de releasenotes om de gerelateerde functies en hun configuratie te begrijpen. Video's die in het Nederlands beschikbaar zijn, zijn hieronder gelinkt; andere video's zijn duidelijk gelabeld als Engels.

| Onderwerp | Video |
| --- | --- |
| Kies de juiste automatisering — inclusief waar Inkoopordermatchingsregels passen | [Nederlandse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/nl.mp4) · [Engelse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/en.mp4) |
| Transformatieregels | [Nederlandse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/nl.mp4) · [Engelse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/en.mp4) |
| Aangepaste validatieregels | [Engelse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/en.mp4) |
| Lay-outs en selectieregels | [Engelse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/layouts/v1/en.mp4) |
| Touchless Intelligence | [Nederlandse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/nl.mp4) · [Engelse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/en.mp4) |
| Validatie van e-facturen | [Nederlandse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/nl.mp4) · [Engelse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/en.mp4) |
| Gebruikers en beheerderstoegang | [Nederlandse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/nl.mp4) · [Engelse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/en.mp4) |
| Suborganisaties | [Nederlandse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/nl.mp4) · [Engelse video](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/en.mp4) |

### AI Table: zes korte video's

Deze video's zijn in het Engels. Bekijk de volledige serie of kies het onderwerp dat u nodig heeft.

1. [Lees de AI-tabel](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part1/v1/en.mp4)
2. [Corrigeer een kolom en leer DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/en.mp4)
3. [Drie typische problemen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part3/v1/en.mp4)
4. [Kortings-, belasting- en nulhoeveelheidsregels](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part4/v1/en.mp4)
5. [Wat de AI al correct leest](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part5/v1/en.mp4)
6. [De Assistent en wie wat kan wijzigen](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part6/v2/en.mp4)

Raadpleeg de [AI Table-handleiding](../../end-user-and-partner-section/end-user-section/ai-table/README.md) voor screenshots en gedetailleerde instructies.

## Validatieassistent: hulp bij het document voor u

* **Vind wat voortgang blokkeert.** Vraag waarom een document niet kan doorgaan. De assistent identificeert de betreffende velden, legt het probleem uit en biedt een sprong naar het veld of de tabelcel. Deze gebruikt het huidige document en de toegangsrechten van de gebruiker.
* **Beoordeel voorgestelde correcties in context.** Waar ondersteund, kunnen reviewers een voorgestelde veld- of tabelwaarde toepassen, een masterdata-kandidaat gebruiken, een opzoeking herhalen of het relevante matchingscherm openen. Wijzigingen aan het formulier blijven onderworpen aan het normale review- en opslagproces van het document. Alleen-lezen documenten en gebruikers zonder bewerkingsrechten krijgen geen bewerkingsacties.
* **Vraag naar matching en boekhouding.** De assistent kan de context van inkooporders of boekhouding uitleggen wanneer deze op die schermen wordt geopend. Wijzigingen aan het validatieformulier worden op het validatiescherm doorgevoerd.
* **Begrijp een verbetering voordat u deze gebruikt.** Uitleggen koppelen een voorgestelde regel of instelling aan de daadwerkelijke waarden van het document. Ze kunnen een diagram en een vertelde uitleg in de taal van de gebruiker bevatten, indien beschikbaar. Suggesties blijven gericht op het huidige document.
* **Werk met de chat in een apart venster.** Pop out het gesprek tijdens het reviewen van het document. Acties die het formulier wijzigen, blijven in het documentvenster.
* **Bekijk meer details achter geëxtraheerde waarden.** De weergave van de waardeherkomst voegt details toe zoals OCR versus de PDF-tekstlaag, matching van extractieregels en de opzoeking die een waarde heeft geleverd. De uitleg van de AI-tabel voegt meer bruikbare instellingsadviezen en duidelijkere tellingen toe.

Een organisatiebeheerder schakelt de Validatieassistent apart in van de Instellingenassistent onder **Instellingen → Bedrijfsgegevens → Assistenten**.

## Herhaalde correcties omzetten in verbeteringen van de automatisering

Het bestaande [Touchless Intelligence](../../administration-and-setup/touchless-intelligence.md)-dashboard krijgt een review- en opvolgingsproces:

* **Voorgestelde geleerde regels.** Herhaalde handmatige correcties kunnen een [transformatieregel](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) voorstellen. Beheerders zien wat de regel zou schrijven, de ondersteunende voorbeelden en de documenten waarop deze een door het team geaccepteerde waarde zou vervangen. Een voorstel wordt beoordeeld voordat het een actieve regel wordt.
* **Verbeterverzoeken van reviewers.** Gebruikers kunnen een verbetering indienen vanuit de documentassistent voor beoordeling door een beheerder in Touchless Intelligence. Het verzoek houdt de uitleg en het besluit bij elkaar.
* **Meten wat er na activering is gebeurd.** Voor ondersteunde transformatieregels vergelijkt DocBits handmatige correcties voor en na activering en toont de touchless-rate ernaast. Meting gebruikt periodes van 14 dagen en identificeert ontoereikende gegevens in plaats van een verbetering te verzinnen. Een wijziging van een regel start een nieuwe meting voor die revisie.
* **Consultingrapport.** Beheerders kunnen een gerangschikt overzicht genereren van verbetermogelijkheden over extractie, masterdata, inkoopordermatching, boekhouding, instellingen en het verwerkingsproces. Geschatte impact wordt als schatting gelabeld totdat deze is gemeten.
* **Leveranciersspecifieke matchingadviezen.** Herhaalde problemen met leveranciers- en artikelmatching kunnen voorstellen voor toleranties of [inkoopordermatchingsregels](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) informeren. Advies onderscheidt een ontbrekende inkooporder van een regel- of tolerantieprobleem.
* **Samenvattingen voor opvolging.** Een wekelijkse beheerderssamenvatting brengt openstaande verbeterverzoeken, leidende mogelijkheden en voltooide metingen samen wanneer er iets te melden is. Aanvragers kunnen worden geïnformeerd wanneer een gemeten resultaat beschikbaar is.

## Instellingenassistent: aanvullende acties en pagina-uitleg

De [Instellingenassistent](../../administration-and-setup/settings/global-settings/company-information/settings-assistant.md), inclusief proactieve waarschuwingen voor e-mail/FTP-gezondheid, is al uitgebracht in VESTA. NOVA voegt acties en context toe aan die bestaande ervaring:

* **Verbindingsacties vanuit een gezondheidswaarschuwing.** Open de betreffende verbinding, bekijk de beschikbare actie en bevestig deze vanuit de assistent. Gezondheidswaarschuwingen kunnen ook worden gesloten. De basis waarschuwingkaarten per kanaal en hun fout-/opnieuwprobeerinformatie bestaan al in VESTA.
* **Zichtbare geschiedenis van deactivering.** Waar vastgelegd, toont een uitgeschakelde import wanneer deze is uitgeschakeld en door wie.
* **Aanvullende beoordeelde acties.** Beheerders kunnen ondersteunde wijzigingen voorvertonen en bevestigen, zoals het activeren van documenttypes, het hernoemen van een groep, het wijzigen van de zoekmodus van een opzoekveld, het verwijderen van een veld of het aanmaken van een inactieve aangepaste validatieregel uit de catalogus.
* **Beheer van mislukte importverbindingen.** Ondersteunde kaarten kunnen een verbinding uitschakelen of verwijderen na bevestiging. Omkeerbare acties bieden een ongedaan maken; permanente verwijdering wordt als zodanig geïdentificeerd.
* **Pagina-uitleg.** Geselecteerde instellingenpagina's bieden video's met ondertiteling en transcripten, inclusief lay-outs, gebruikers, suborganisaties, transformatieregels en e-factuurvalidatie waar een taalversie beschikbaar is.

## Regels en lay-outs: directe toegang en betere diagnostiek

* **Voormalige bèta-besturingselementen worden reguliere functies.** Lay-outs beheren, [Aangepaste validatieregels](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) en [Transformatieregels](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) zijn zichtbaar in de geavanceerde instellingen voor documenttypes van NOVA zonder bètalink. Hun inschakelschakelaars blijven onder beheerderscontrole. Deze besturingselementen zijn opgenomen in de geplande VESTA-hotfix van 11 november 2026 samen met alle andere voormalige VESTA-bètafuncties.
* **Nuttigere regeldiagnostiek.** Regels voor lay-outselectie krijgen een optie **Uitvoering loggen**. Regelzoeken accepteert regel-ID's, en het openen van een editor laadt de huidige opgeslagen regel. Het bestaande logboek voor regeluitvoering blijft de plaats om te bekijken wat er is uitgevoerd.
* **Kies en open lay-outs met meer context.** Zoek doellay-outs, bekijk hun inhoud en open het doel rechtstreeks vanuit een selectieregel. Goedkeuringsselectieregels accepteren correct de ondersteunde lay-outtypes voor goedkeuring. Beheerders krijgen ook een snelkoppeling van documentvalidatie naar de lay-outeditor van dat documenttype.
* **Selecteer meerdere voorwaardewaarden.** Voorwaarden zoals **is een van** ondersteunen meerdere geselecteerde waarden.
* **Vind dubbele detectievelden sneller.** De veldselector in de dubbele instellingen van het documenttype is doorzoekbaar.

Transformaties na masterdata-opzoeking, het basisuitvoeringslogboek van regels, bredere regel-editors en de fixes voor het klonen van standaardregels hebben reeds implementaties in de VESTA-baseline. NOVA draagt die functionaliteit door en maakt de voormalige bèta-beheersfuncties beschikbaar als reguliere functies.

Zie [Aangepaste validatieregels](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) en [Transformatieregels](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) voor instelstappen, voorbeelden en testen. Zie [Lay-outselectieregels](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md) om te kiezen welke lay-out een document gebruikt.

## E-factuurvalidatie: duidelijkere bevindingen en beleidscontroles

* **Een rapport georganiseerd op validatieniveau.** Bevindingen worden gegroepeerd in syntaxis-, schema-, bedrijfsregels, kruiscontrole-regels en landspecifieke regels, met aanvullende groepen voor andere standaardcontroles en waardecontroles. Berichten en samenvattingen gebruiken de taal van de gebruiker waar vertalingen beschikbaar zijn.
* **Volledigere controles en duidelijkere resultaten.** De bijgewerkte validator en het rapport onderscheiden fouten, waarschuwingen en de effectieve ernst na organisatie-specifieke configuratie. De pagina heet **E-factuurvalidatie**.
* **Beleidsregels per documenttype.** Beheerders kunnen controleren of e-factuurvalidatie is ingeschakeld en of fouten de verwerking blokkeren. De beleidsweergave identificeert overschrijvingen voor subtypes, en beleidswijzigingen worden vastgelegd in een wijzigingsgeschiedenis.
* **Inspecteer de XML binnen een PDF-factuur.** De XML-viewer kan de ingebedde XML in ondersteunde ZUGFeRD/Factur-X PDF's lezen, de positie openen waarnaar een bevinding verwijst en terugkeren naar het document.
* **Weiger met een vastgelegde reden.** Een bevoegde reviewer kan een geschikt document weigeren vanuit het validatierapport. Het rapport stelt een reden op uit de fouten voor de reviewer om te controleren voordat deze wordt bevestigd.
* **Verdere formaatcorrecties.** EDNA utility CII-facturen worden herkend, en correcties aan de XRechnung-btw-mapping verbeteren hoe relevante factuurwaarden DocBits-velden bereiken.

Zie [E-documentvalidatieregels](../../administration-and-setup/settings/document-processing/e-documents/validation-rules.md).

## FTP/SFTP- en e-mailimports

* **Begeleide FTP/SFTP-instelling.** De verbindingswizard scheidt servergegevens, importopties en configuratie. Verbindingscontroles en duidelijkere fouten helpen beheerders een onjuiste verbinding of een ontbrekende bronmap te identificeren.
* **Importlogboeken per stap.** Controleer de voortgang van een bestand door de FTP-import, inclusief upload en de geconfigureerde actie op het bronbestand.
* **Configureerbaar herhalings- en meldingsgedrag.** Stel het interval tussen latere herhalingen in, hoe lang er herhaald moet worden en de meldingsontvangers. Wanneer het herhalingsvenster is verstreken, kan de verbinding automatisch worden uitgeschakeld en kunnen ontvangers worden geïnformeerd; de wizard toont de uitschakelingsmelding.
* **Verwijderen na succesvolle import.** Naast het bewaren of archiveren van bronbestanden kunnen beheerders ervoor kiezen om ze na een succesvolle import van de FTP/SFTP-server te verwijderen. Archiveren en verwijderen zijn afzonderlijke alternatieven.
* **Betrouwbaarder herstel bij importproblemen.** Overlappende FTP-runs kunnen niet meer hetzelfde bronbestand twee keer uploaden. Bij het bewerken van een verbinding blijft het opgeslagen wachtwoord behouden, tenzij het wordt vervangen. De e-mailverwerking markeert een bericht niet voor verwijdering als het kopiëren is mislukt.
* **Onderssteuning voor ondertekende e-mail.** Opaque-ondertekende S/MIME-berichten met facturen kunnen worden uitgepakt in plaats van overgeslagen.
* **Geschiedenis en status van e-mailconfiguratie.** Importinstellingen tonen wie de configuratie als laatste heeft opgeslagen of geactiveerd. De schakelaar voor inkomende e-mail weerspiegelt de opgeslagen actieve status, inclusief een nieuw opgeslagen configuratie.

Zie [FTP-import](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) en [Een FTP-importverbinding testen](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md).

## Documentverwerking en extractie

* **Herstart met een gekozen aantal pagina's.** Het dashboard voegt een herstartactie toe waarmee reviewers kunnen opgeven hoeveel pagina's voor dat document moeten worden verwerkt, binnen het werkelijke aantal pagina's.
* **Bekijk de verwerkingslimiet.** Het dashboard kan verwerkte versus totale pagina's voor een beperkt document weergeven. De instelling **Aantal te verwerken pagina's** van de organisatie is gegroepeerd onder Documentverwerking in **Classificeren & extraheren**.
* **Beheer de extractie van verborgen velden.** Beheerders kunnen via de instelling **Verborgen velden extraheren** kiezen of verborgen velden deelnemen aan de extractie.
* **Sneller werken met grotere batches.** Prestatieverbeteringen zijn doorgevoerd voor het in bulk herstarten van documenten, het importeren van masterdata via CSV, PDF-verwerking en regelgebaseerde veldextractie.
* **Betrouwbare AI-extractie.** Time-outs worden gerapporteerd als time-outs, en fouten bij ondersteunde modellen kunnen terugvallen op een ander beschikbaar model. Aanvullende fixes lossen problemen op met herhaalde sleutels in AI-uitvoer, geconfigureerde veldsynoniemen en lege opgeslagen tabeldefinities.
* **Behoud het net ingevoerde waarde.** Als u een tabelcel opslaat zonder eerst ergens anders te klikken, blijft de ingetypte waarde behouden. Datums met OCR-verwarde maandnamen worden betrouwbaarder verwerkt.

## Inkoopordermatching, goedkeuring en export

De [gids voor Inkoopordermatchingsregels](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) (Engels) legt uit hoe u regelgebaseerde matching inschakelt, matchingtypes en toleranties configureert, de uitvoervolgorde instelt en regelversies beheert.

* **Match in beide richtingen.** Selecteer documentregels en koppel ze aan inkooporderregels, of begin bij de inkooporderregels. Dit is handig wanneer veel leveringsbonregels betrekking hebben op één inkooporderregel.
* **Behoud detail van één-op-veel-regels.** Een matchingconfiguratie kan nu een individuele subregel voor elke documentregel behouden wanneer meerdere regels overeenkomen met één inkooporderregel. Deze optie is standaard uitgeschakeld. Generieke API-export kan verzoeken groeperen op geconfigureerde kolomwaarden van regels, wat ondersteuning biedt voor leveringen of containers die aparte doelrecords vereisen.
* **Configureer fallback voor de laatste regel.** Organisaties kunnen bepalen of de resterende document- en inkooporderregel mag worden gematcht door de fallback voor één regel.
* **Nauwere matching en weergave.** Fixes zorgen ervoor dat de juiste prijsbasis voor pakketgeconverteerde matches behouden blijft, de status van de inkooporderregel wordt overgenomen op planningrijen en ontvangen hoeveelheden uit ontvangstregels worden weergegeven.
* **Voorkom voortijdige goedkeuring en dubbel werk.** De definitieve goedkeuring wordt geblokkeerd zolang relevante afwijkingen in de inkooporder niet zijn goedgekeurd. Herhaalde workflowuitvoering maakt geen nieuwe openstaande taak voor dezelfde groep aan, en controles op dubbele export worden vóór goedkeuring uitgevoerd.
* **Scheid Exported van Finished.** Exportacties kunnen de status na een succesvolle export selecteren. **Exported** heeft een eigen dashboardbadge. Organisaties die de vergrendeling van voltooide documenten inschakelen, voorkomen dat gewone workflows of herstarts voltooide documenten opnieuw openen; bevoegde overschrijvingen worden vastgelegd.
* **Duidelijkere workflowprobleemoplossing.** Een dashboardfilter vindt documenten die worden tegengehouden door de limiet voor workflowuitvoering. Workflowruns kunnen worden geïnspecteerd in een pop-up, en een geweigerde statuswijziging noemt de status van het document.
* **Aanvullende exportfixes.** M3-validatie en goedkeuringspogingen worden aangepast, en voorwaardelijke leveranciersexportconfiguraties worden correct verwerkt.

## Dagelijkse bruikbaarheid en toegang

* **Betrouwbare navigatie.** Bijgewerkte documentadressen hebben omleidingen voor oudere links. NOVA-deeplinks behouden het beoogde kanaal tijdens het aanmelden, en de laadvoortgang toont welk deel van de pagina wordt voorbereid.
* **Persoonlijke werkvoorkeuren.** De kolomvolgorde van inkooporders wordt per gebruiker opgeslagen, en het goedkeuringsscherm onthoudt het geopende zijbalkpaneel van de gebruiker.
* **Betrouwbere taak- en dashboardweergaven.** Taken zonder toegewezen persoon kunnen worden weergegeven, geopend en toegewezen. Het takenbord wordt opnieuw geladen wanneer de geselecteerde organisatie gereed is, aangepaste datumbereiken op het dashboard worden correct toegepast, en dubbele documentrijen worden vermeden.
* **Betere labels en logs.** Beheerders kunnen vertaalsleutels voor velden en tabelkolommen bewerken. Kolommen in het documentlogboek kunnen worden aangepast, aangepaste dashboardkolommen verwerken veldidentificatiecodes met gemengde hoofdletters, en lange labels en bestandsnamen passen consistenter.
* **Bereik van meldingen.** E-mailregels voor documentstatus kunnen worden beperkt tot een suborganisatie.
* **Leveranciersonboarding.** Magische links voor registratie in het Leveranciersportaal blijven **21 dagen geldig in plaats van 7 dagen**. Beheerders kunnen ook de kop voor uploadfouten voor een bestandsveld in een leverancierslay-out configureren.
* **Betrouwbaarheid van aanmelden.** SAML-aanmelden gebruikt geen verlopen of ingetrokken sessies meer. Beheerdersaanmelden ondersteunt de vereiste MFA-stap, en inactieve lidmaatschappen kunnen geen nieuwe uitnodiging voor het instellen van een wachtwoord meer ontvangen.
* **Afbeeldingen op het Idea Board.** Geüploade afbeeldingen worden apart van de ideeomschrijving opgeslagen en aangeboden, wat de verwerking van afbeeldingen verbetert.
* **Beheerde kanaalwisseling.** De instelling voor het releasekanaal kan alleen-lezen worden gemaakt als wisselen niet is ingeschakeld voor de omgeving. Volg de releaseaankondiging voor de beschikbaarheid.

## Aangesloten assistenten en integratietools

Voor organisaties en partners die de DocBits MCP-integratie gebruiken, voegt NOVA tools toe om de effectieve validatieregels op te vragen, één regel op een document te testen zonder wijzigingen op te slaan en de opgeslagen gegevens over de regeluitvoering toe te lichten. Aangesloten assistenten kunnen ook verbeterverzoeken opvragen en een door een beheerder geautoriseerde goedkeuring indienen via hetzelfde beoordelingsproces als de webapp. De bestaande rechten voor organisaties en documenten blijven van toepassing.

## Functies die al aanwezig zijn in VESTA

NOVA brengt ook de hieronder vermelde functionaliteit over. Waar de toegang eerder beperkt was tot de VESTA-bèta, maakt de reguliere beschikbaarheid deel uit van deze NOVA-release en is deze gepland voor de VESTA-hotfix op 11 november 2026. De lijst beschrijft de eerdere functionaliteit, naast de hierboven uitgelegde wijzigingen in de beschikbaarheid en verbeteringen:

* De oorspronkelijke Instellingenassistent, de documentatiezoekfunctie, de basisstroom van voorbeeld/bevestigen/ongedaan maken en proactieve waarschuwingen voor de importgezondheid via e-mail/FTP.
* De AI-tiers Fast, Full, Nexus en Auto en de instelling voor de visuele modus.
* De Header Field Check en het oorspronkelijke rapport voor de waardeherkomst.
* De eerste release van Touchless Intelligence, leveranciersdiagnose, bulkanalyse en het beslisdiagram voor inkooporders.
* De onderliggende engines voor validatie-, transformatie- en lay-outselectieregels, transformaties na masterdata-opzoeking en het basislogboek voor de regeluitvoering.
* Eerdere verbeteringen van het dashboardzoeken, MFA, geverifieerde e-maildomeinen van organisaties, afwijkingstolerantie voor kosten en de verhoging van de limiet voor workflowuitvoering naar 50.

Zie de [VESTA-hotfix van 14 oktober](incremental-updates-14-october-2026.md), de [hotfix van 15 september](incremental-updates-15-september-2026.md) en de [eerdere release-opmerkingen](README.md#vesta-hotfix-releases) voor de VESTA-releasegeschiedenis.

## NOVA-serviceversies

Dit zijn de versies en implementatietijdstempels in de **momentopname van 16 oktober 2026**. De tijdstempels beschrijven individuele service-implementaties, niet een aparte releasedatum voor elke functie.

| Service | Versie | Implementatietijdstempel |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

Versienummers lopen onafhankelijk op de twee kanalen op. Een hoger nummer betekent niet per se dat een service een nieuwe klantfunctie heeft. De beoordeelde wijzigingen voor Auto Accounting, Barcode, Docnet, Fulltext, OCR en Operator zijn onderhouds- of verwerkingsbetrouwbaarheidswijzigingen; ze introduceren geen aparte klantworkflow in deze vergelijking. Updates van Auth Bridge verbeteren de betrouwbaarheid van de cross-regionale accountsynchronisatie.
