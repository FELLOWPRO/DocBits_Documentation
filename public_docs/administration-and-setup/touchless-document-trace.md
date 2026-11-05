# Touchless Intelligence: Documentspoor

<!-- touchless-admin-video-v2-20261104:start -->
**Videohoofdstuk (controleversie):** [Uitvoeringen vergelijken](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/nl.html#chapter=08).
<!-- touchless-admin-video-v2-20261104:end -->

Voer een document-ID in bij **Document ID**, of open een voorbeelddocument uit een cluster, om te zien **wat er met dit ene document is gebeurd**.

De kop toont het bestand, de status ervan (bijvoorbeeld **In uitvoering**), de uitvoering die u bekijkt en de eerste blokkeerder daarvan, en een knop **Document** met het document-ID.

<figure><img src="../.gitbook/assets/touchless-nova-trace-overview-nl.png" alt="Dev NOVA: procespad en vastgelegde waarden van de eerste testuitvoering"><figcaption><p>Nieuwe opname op Dev NOVA 11.0.3, 4 november 2026. De fictieve factuur stopt bij veldvalidatie. Classificatie, leverancierszoekactie en extractie van kopgegevens en tabel bevatten echt vastgelegde waarden. De kaarten tonen het document en de uitvoeringsgeschiedenis. Dit is de werkende productinterface. In deze versie blijven de stapnamen in het procespad Engels. EA op de documentkaart verwijst hier naar het inkoopordernummer.</p></figcaption></figure>

Het **Pijplijnpad** toont 14 stappen: Intake, Classification, E-Document Validation, Supplier Identification, Text Recognition, Header Extraction, Table Extraction, Field Validation, PO Lookup, PO Line Match, Approval, Workflow Routing, Export, ERP Acknowledgement. Elke stap draagt één status:

| Status | Betekenis |
| --- | --- |
| **Geslaagd** (groen) | De stap is goed verlopen |
| **Hier gestopt** (oranje) | De stap heeft het document geblokkeerd |
| **Niet bereikt** | Stap na de eerste blokkade in het procespad; controleer het logboek op aanvullende vastgelegde uitvoering |
| **Niets geregistreerd** (gestippeld) | Voor deze stap zijn geen gegevens vastgelegd |
| **Niet van toepassing** | De stap geldt niet voor dit document |

### Stappenlogboek

Het **stappenlogboek** onder het pad somt dezelfde stappen op met wat elke stap heeft geregistreerd. Een statusstip en het statuswoord staan links en rechts op elke regel.

* Elke waarde is een **waardechip**: een getal met zijn eenheid, bijvoorbeeld **Betrouwbaarheid 100 %**, **Drempel 60 %**, **Mislukte regels 0**, **8 ontbrekende velden** of **0 koppelingshiaten**. Percentages worden getoond als `97 %`, nooit als `0.97`.
* **Details** opent de volledige lijst van waarden die een stap heeft vastgelegd, inclusief de alternatieven die zijn overwogen.
* De stap die het document blokkeerde, noemt de reden, bijvoorbeeld **Veldvalidatie mislukt**.
* Een waarde die geen enkele stap heeft vastgelegd, verschijnt als **Niet geregistreerd**, nooit als verzonnen waarde. Waarden zijn getallen en vaste termen, nooit documenttekst.
* **Ruwe diagnostiek tonen** zet de ruwe gegevens aan wanneer de support erom vraagt.

<figure><img src="../.gitbook/assets/touchless-nova-trace-stage-log-nl.png" alt="Dev NOVA: stappenlogboek met betrouwbaarheid, extractiewaarden en geblokkeerde veldvalidatie"><figcaption><p>Echte eerste uitvoering: 100 % classificatiebetrouwbaarheid, 0 leverancierskandidaten, 1 tabelregel en 7 koppelingshiaten. Een geslaagde stap bevestigt de uitvoering, niet een leveranciersmatch of de juistheid van alle factuurwaarden. De validatie meldt een ontbrekend verplicht veld.</p></figcaption></figure>

### Uitvoeringen en wijzigingen

Kies een poging met de uitvoeringskiezer; de geschiedenis toont het resultaat en de eerste blokkade. Vastgelegde verschillen vergelijken de gekozen uitvoering met haar voorganger, niet automatisch met de huidige uitvoering. Elk verschil bevat de eenheid; identieke waarden blijven ongewijzigd.

De kaart Document noemt type, leverancier, factuurnummer, order, pagina’s en vastgelegde analysemethode. Handmatig verwijst hier naar het documenttype dat bij de testimport is opgegeven. De 100 % bewijst daarom niet onafhankelijk hoe nauwkeurig automatische classificatie is.

### Leveranciers- en tabeldetails lezen

<figure><img src="../.gitbook/assets/touchless-nova-trace-supplier-nl.png" alt="Dev NOVA: gevonden kenmerken, zoeken in stamgegevens en leverancierskoppeling"><figcaption><p>De naam staat op de factuur en wordt in de stamgegevens gezocht, maar er wordt geen leverancier gekoppeld. Deze testfactuur bevat geen btw-nummer, IBAN, e-mailadres of GLN. Een ontbrekende stamgegevensmatch is iets anders dan een niet gevonden factuurwaarde. Geen wedstrijd geprobeerd betekent hier dat geen koppelpoging is uitgevoerd; het gaat niet om een wedstrijd.</p></figcaption></figure>

Controleer apart of het kenmerk op het document stond, of ernaar is gezocht en of een leverancier is gekoppeld. Een groene stap beantwoordt deze drie vragen niet vanzelf.

<figure><img src="../.gitbook/assets/touchless-nova-trace-table-nl.png" alt="Dev NOVA: tabeldetails van de eerste uitvoering met zeven koppelingshiaten"><figcaption><p>De details melden 7 koppelingshiaten bij 1 tabel en 1 regel. Controleer de kolomkoppeling voordat u een extractiefout aanneemt. De vergelijkingsregel onderaan vormt geen geldige basis voor de geselecteerde eerste uitvoering, die geen voorganger heeft.</p></figcaption></figure>

### Een echte herstart herkennen

<figure><img src="../.gitbook/assets/touchless-nova-trace-runs-nl.png" alt="Dev NOVA: vergelijking van twee echte uitvoeringen met ongewijzigde stapwaarden"><figcaption><p>Dezelfde factuur na een echte handmatige herstart, zonder gecorrigeerde factuurvelden. Een nieuwe uitvoering bewijst een nieuwe poging, geen verbetering. Identieke waarden blijven ongewijzigd; er zijn geen verschillen verzonnen.</p></figcaption></figure>

Een handmatige herstart is een menselijke ingreep. Pas na een latere succesvolle afronding telt deze factuur als AP Assisted. Zolang zij in verwerking blijft, valt zij buiten de noemer van afgeronde documenten.

Grenzen van het bewijs. Deze casus toont geen zakelijke goedkeuring, geslaagde export of ERP-bevestiging. De oude ordermatcher levert hier geen vastgelegd beslispad; dit bewijst geen vergelijking met Infor. In NOVA 11.0.3 kan het logboek na geblokkeerde veldvalidatie een geslaagde orderzoekactie tonen, terwijl het procespad deze als volgende stap weergeeft. Controleer beide weergaven. Ook toont de samenvatting het factuurnummer als niet vastgelegd, hoewel het wel in de extractie staat; vergelijk origineel en geëxtraheerde velden.

## Extractie en brongegevens onderscheiden

Vergelijk origineel en uitgelezen velden/regels vóór correcties. Vergelijk daarna geïmporteerde inkooporder en actuele Infor-gegevens, inclusief eenheden, prijseenheden en importtijd. Onderscheid origineel versus extractie, correcte extractie versus geïmporteerde order en Infor versus zijn kopie. Een geslaagde stap bewijst niet elke waarde. Laat de oorzaak open als bewijs ontbreekt.

**Voorbeeld:** origineel en extractie tonen €10, de geïmporteerde order €9. Dat is een orderafwijking, geen aangetoonde extractiefout. Controleer de afgesproken prijs. Menselijke herstart gevolgd door succes geeft AP Assisted. Zie [kengetallen en berekening](touchless-metrics.md).

Terugkerende ontbrekende velden bewijzen een herhaald blokkeringspunt, niet noodzakelijk een ontbrekende standaardwaarde. Controleer origineel, extractie, validatie en configuratie.

## Oorspronkelijke extractie en opeenvolgende blokkades bewijzen

1. Open het juiste document en de juiste uitvoering. Vergelijk ordernummer, valuta, aantallen, eenheden, prijseenheden, prijzen, regels en relevante totalen met het origineel.
2. Scheid huidige waarden van waarden vóór correcties. Gebruik historisch bewijs van dezelfde uitvoering; wisselen van uitvoering herstelt niet gegarandeerd elke oude cel.
3. Ontbreekt de oorspronkelijke waarde, noteer **niet beoordeelbaar**. Leg selectie, velden, regels en steekproefgrootte vooraf vast.
4. Vergelijk de geïmporteerde kopie, importtijd en actuele Infor-waarden om een verouderde kopie van een foutieve bron te onderscheiden.

Een uitvoering kan wachten op een order; een volgende kan na de import een prijsverschil tonen. De eerste bewijst niet dat die latere controle al is uitgevoerd. Een menselijke herstart blijft na succes AP Assisted; een definitieve ERP-afwijzing heeft voorrang als uitzondering. **Niet vastgelegd** betekent ontbrekend bewijs.

Tools en menselijke acties worden uitgelegd bij [Touchless met MCP](touchless-mcp.md).

## Gerelateerde pagina's

* [Touchless Intelligence](touchless-intelligence.md)
* [Leveranciersdiagnose en probleemclusters](touchless-supplier-diagnosis.md)
* [PO-matchingdiagnose](touchless-po-matching-diagnosis.md)

De schermafbeeldingen op deze pagina tonen de interface in het Nederlands.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->

<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->

De vijf nieuwe afbeeldingen tonen de gelokaliseerde interface van Dev NOVA 11.0.3 en dezelfde factuur die voor de documentatie is aangemaakt. Een afzonderlijk beeld van origineel en velden illustreert uitsluitend die vergelijking.
