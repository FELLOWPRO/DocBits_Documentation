# Touchless Intelligence: PO-matchingdiagnose

## Overzicht

Veel facturen stoppen bij de inkooporder. De factuur zegt het ene, de inkooporder (PO) zegt het andere, en DocBits kan niet zelf beslissen of ze bij elkaar horen. Elk zo'n document heeft een persoon nodig, dus het is **niet touchless**.

Touchless Intelligence laat u zien **waarom** een PO-match mislukte en **hoe** DocBits probeerde te matchen. Deze pagina legt de twee betrokken pipelinefasen uit, de redenen die u zult zien en de **beslisstroom van de PO-matching**, een diagram dat de matchingstappen na elkaar toont.

### Waar u PO-matching in Touchless Intelligence ziet

| Waar | Wat u ziet |
| --- | --- |
| **Waar touchless het eerst verloren gaat** (overzichtstabblad) | Een staaf zoals *PO line match: PO item mismatch*. Die vertelt u hoeveel documenten daar stopten |
| **Leverancierskansen** | Een leverancier met de hoofdoorzaak **PO-matching** |
| **Leveranciersdiagnose**, sectie **Hoe deze organisatie matcht** (How this organisation matches) en het **probleemcluster** | De beslisstroom met de regelset van uw organisatie |
| **Documentspoor** | De fase **PO-regelmatch** met de status **geblokkeerd** en de reden |
| **Instellingen → Documenttypen → Meer instellingen → Inkooporder** | De matchingregels zelf. Zie [Regels voor het Matchen van Inkooporders](settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) |

## De twee PO-fasen

| Fase | Vraag | Stopt met |
| --- | --- | --- |
| **9 · PO-opzoeking** | Is er een inkooporder voor deze factuur? | *Purchase order not found* (inkooporder niet gevonden) |
| **10 · PO-regelmatch** | Komt elke factuurregel overeen met een PO-regel? | *PO item mismatch*, *PO line identifier mismatch*, *Unit price outside PO tolerance*, *Quantity outside PO tolerance* |

Een document dat bij fase 9 of 10 stopt, verschijnt in de leverancierswachtrij met de eerste blokkade **PO-matching**.

## Redenen waarom een PO-match mislukt

| Reden die u ziet | Wat het betekent | Typische oorzaak | Wat te wijzigen |
| --- | --- | --- | --- |
| **Purchase order not found** | DocBits vond geen inkooporder bij het PO-nummer op de factuur | Het PO-nummer wordt verkeerd gelezen of ontbreekt; de PO is nog niet geïmporteerd; de PO hoort bij een andere leverancier | Controleer de extractie van het PO-nummer voor deze leverancier, de import van PO-stamgegevens en de koppeling met de leverancier |
| **PO item mismatch** | De factuurregels kwamen niet overeen met de PO-regels | De leverancier gebruikt eigen artikelnummers; de omschrijving verschilt; regels zijn samengevoegd of gesplitst | Controleer de mapping van artikelnummers en de **regelprioriteiten** in de matchingregels; voeg een regel toe voor de manier waarop de leverancier regels identificeert |
| **PO line identifier mismatch** | Het regelnummer of de identificatie op de factuur komt niet overeen met de PO | De leverancier nummert regels opnieuw | Match op artikel en hoeveelheid in plaats van op regelnummer |
| **Unit price outside PO tolerance** | De prijs wijkt meer af dan de toegestane tolerantie | Een echte prijswijziging, een afrondingsverschil of een andere prijseenheid | Controleer de **tolerantie voor stukprijs** in de regelset; corrigeer de PO of vraag het de leverancier |
| **Quantity outside PO tolerance** | De hoeveelheid wijkt meer af dan de toegestane tolerantie | Deellevering, overlevering | Controleer **Match Hoeveelheid Op** en de **hoeveelheidstolerantie** |
| **PO matching service error** | De matchingservice kon niet antwoorden | Een tijdelijk technisch probleem | Start de documenten opnieuw; neem contact op met support als het zich herhaalt |
| **Automatic PO export disabled** | De instelling **Auto export if PO matched 100%** staat uit, dus gematchte documenten worden niet automatisch geëxporteerd | De instelling staat uit | Schakel de instelling in als u automatische export wilt. Zie [Auto Export if PO Matched 100%](settings/document-processing/module/auto-export-if-po-matched-100.md) |

{% hint style="info" %}
Niet elke reden voor PO-matching kan in DocBits worden opgelost. Als de leverancier een verkeerd PO-nummer stuurt, zegt de kaart **Alleen actie van leverancier**: de leverancier moet het document corrigeren en opnieuw sturen.
{% endhint %}

## De beslisstroom van de PO-matching

De beslisstroom toont hoe DocBits een factuurregel aan een PO-regel probeert te koppelen. Hij heeft **vijf fasen**, en de eerste match wint:

1. **Single match validation** (validatie van enkelvoudige match): pas de regels toe in volgorde van prioriteit. Dit is het normale geval, één factuurregel en één PO-regel
2. **Multi match validation** (validatie van meervoudige match): na een enkelvoudige match, wanneer aan één kant meerdere regels betrokken zijn
3. **Total match validation** (validatie van totaalmatch): alleen wanneer er helemaal niets matchte. Het totaal van de PO-regel wordt vergeleken met de som van de tabelregels
4. **Single mismatch validation** (validatie van enkelvoudige afwijking): de stukprijs wordt genegeerd, zodat een regel op artikel en hoeveelheid kan worden gematcht, ook als de prijs verschilt
5. **Fallback logic** (terugvallogica): er blijven één PO-regel en één tabelregel over, die dan worden gekoppeld

Binnen de fasen probeert DocBits in deze volgorde:

* **Exacte match voor alle regels**: elke vergeleken waarde is identiek
* **Match op basis van tolerantie**: numerieke waarden mogen binnen de tolerantie afwijken
* **Verpakkingscriteria**: de laatste ronde, gebaseerd op de verpakkingsgerelateerde criteria van de regelset

Elke stap vraagt **Match found?** (match gevonden?). Het antwoord **Yes** (groen) leidt naar **Match found** en het document gaat verder. Het antwoord **No match** (rood) gaat door naar de volgende stap, en na de laatste stap is het resultaat **No match found**: het document stopt en heeft een persoon nodig.

<figure><img src="../.gitbook/assets/touchless-po-matching-flow.png" alt="De beslisstroom van de PO-matching: kop met regelset, vijf genummerde matchingfasen met hun rondes en de eindpunten Match found en No match found"><figcaption><p>De beslisstroom van de PO-matching, geopend via <strong>Hoe deze organisatie matcht</strong> op de pagina Leveranciersdiagnose. De kop toont de regelset (versie 7, eigendom van deze organisatie) en de tolerantie. Daaronder lopen de vijf fasen met hun rondes van boven naar beneden. Groen leidt naar <strong>Match found</strong>, rood gaat door naar de volgende stap en eindigt in <strong>No match found</strong>. Voorbeeldorganisatie met demogegevens.</p></figcaption></figure>

### Wat de kop van het diagram u vertelt

| Veld | Betekenis |
| --- | --- |
| **Documenttype** (Document type) | Het documenttype waartoe de regelset behoort, bijvoorbeeld INVOICE |
| **Versie van de regelset** (Rule set version) | De versie van de matchingregels, bijvoorbeeld v3 |
| **Eigenaar van de regelset** (Rule set owner) | **Deze organisatie** (uw eigen regels) of **Meegeleverde standaardregelset** (de standaardregels van DocBits) |
| **Gepubliceerd** (Published) | Wanneer de versie is gepubliceerd |
| **Match Hoeveelheid Op** (Match quantity on) | Welke hoeveelheid wordt vergeleken (bestelde hoeveelheid, openstaande hoeveelheid) |
| **Tolerantiebedrag** (Tolerance amount) | Of de toleranties uit de attributen van het documenttype komen of uit de regelset |
| **Tolerantie stukprijs** / **Hoeveelheidstolerantie** (Unit price tolerance / Quantity tolerance) | Hoeveel een prijs of een hoeveelheid mag afwijken |
| **Standaardtolerantie** (Default tolerance) | De tolerantie voor alle andere numerieke waarden |

In het voorbeeld hierboven tonen de toleranties **not configured** en **not in force: attribute decides**. Dat betekent: de regelset zelf heeft geen eigen tolerantie, en de regel **Tolerantiebedrag** zegt dat de toleranties uit de **attributen van het documenttype** komen. Een tolerantie beslist alleen als ze van kracht is. Lees deze regel eerst wanneer een prijs- of hoeveelheidsverschil documenten blokkeert: ze vertelt u **waar** u de tolerantie moet wijzigen.

De status van de regelset wordt als opmerking getoond: **Actieve versie** (deze regels beslissen), **Goedgekeurd, niet actief**, **Concept, nog niet van kracht** of **Versiestatus onbekend**. Alleen de actieve versie beslist.

Als transformatieregels een document vóór de matching hebben gewijzigd, zegt het diagram dat, bijvoorbeeld *2 applied: (names)* of *"(rule)" rebuilt (table): the PO match was lost here*. Dat is een veelvoorkomende verborgen oorzaak: een regel die een tabel opnieuw opmaakt, kan een match breken die eerder werkte.

## Voorbeelden

De cijfers in de voorbeelden zijn illustratief.

### Voorbeeld 1: Prijs binnen de tolerantie

Een factuurregel heeft een stukprijs van **10,40**. De PO-regel zegt **10,00**. De tolerantie voor de stukprijs is **5 %**.

* **Exacte match** mislukt (10,40 is niet 10,00).
* **Match op basis van tolerantie** slaagt: het verschil is **4 %**, en dat valt binnen 5 %.
* De regel is gematcht. **Match found.**

Bij een tolerantie van **3 %** mislukt ook de match op basis van tolerantie. Na alle fasen stopt het document met **Unit price outside PO tolerance**. Het diagram toont precies dit pad, en de oplossing is ofwel de tolerantie (als 4 % acceptabel is voor uw bedrijf) ofwel een correctie bij de leverancier.

### Voorbeeld 2: De artikelnummers van de leverancier verschillen van de uwe

Een leverancier factureert artikel **"A-4711-X"**, uw PO zegt **"4711"**. Geen enkele regel vergelijkt de twee, dus er wordt geen match gevonden, en Touchless Intelligence groepeert alle facturen van deze leverancier in één cluster: **PO-regelmatch, PO item mismatch**, 27 documenten.

* In het cluster leest u *27 getroffen, 27 herstelbaar*, verwachte stijging bijvoorbeeld **+8,7 pp**.
* De oplossing ligt aan uw kant: voeg een regel toe of wijzig de volgorde van regels zodat op het artikelnummer van de leverancier of op de omschrijving wordt gematcht, of onderhoud de artikelnummers van de leverancier in de stamgegevens.
* Nadat u de regel hebt gewijzigd, past u de wijziging toe met een [wijzigingsvoorstel](touchless-change-proposals.md) en leest u twee weken later de **Wijzigingsgeschiedenis**: puur percentage voor en na.

### Voorbeeld 3: De inkooporder is er nog niet

Facturen komen binnen voordat de PO is geïmporteerd. Ze stoppen bij **PO-opzoeking** met **Purchase order not found**. Het cluster toont een korte piek. De oplossing is de volgorde van uw processen of het schema van de PO-import, niet de matchingregels. Kijk bij **Waar touchless het eerst verloren gaat**: een staaf *PO lookup: Purchase order not found* die na elke importpauze groeit, wijst op deze oorzaak.

### Voorbeeld 4: Eén regel heeft de tabel opnieuw opgebouwd

Nadat een transformatieregel voor de tabel van een leverancier live ging, daalde het matchingpercentage van deze leverancier sterk. Het diagram van een getroffen document zegt *"(rule)" rebuilt (table): the PO match was lost here*. De oplossing is de transformatieregel aan te passen of ongedaan te maken, niet de matchingregels.

## Een routine voor problemen met PO-matching

1. Open **Waar touchless het eerst verloren gaat**. Staat een PO-matchingfase in de top drie?
2. Open **Leverancierskansen** en sorteer op **Verwachte stijging**. Neem de leverancier met de hoofdoorzaak **PO-matching** en de status **RECOVERABLE**.
3. Open de **Leveranciersdiagnose** en lees het cluster: reden, getroffen documenten, **Wat te wijzigen**, **Ontbrekend bewijs**.
4. Open **Hoe deze organisatie matcht** en controleer de regelset: versie, eigenaar en toleranties.
5. Open één **voorbeelddocument** en het bijbehorende [Documentspoor](touchless-document-trace.md): welke fase, welke reden?
6. Wijzig **één** ding (volgorde van regels, tolerantie, artikelmapping) met een voorbeeldweergave, zodat de **Wijzigingsgeschiedenis** het kan meten.

## Gerelateerde pagina's

* [Touchless Intelligence](touchless-intelligence.md)
* [Leveranciersdiagnose en probleemclusters](touchless-supplier-diagnosis.md)
* [Documentspoor](touchless-document-trace.md)
* [Wijzigingsvoorstellen en rapporten](touchless-change-proposals.md)
* [Regels voor het Matchen van Inkooporders](settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md)
* PO Matching Cards: Complete Guide
