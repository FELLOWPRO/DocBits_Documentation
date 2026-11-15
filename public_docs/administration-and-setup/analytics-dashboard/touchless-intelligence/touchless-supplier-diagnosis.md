# Touchless Intelligence: Leveranciersdiagnose en probleemclusters

<!-- touchless-admin-video-v2-20261104:start -->
**Videohoofdstuk (controleversie):** [Terugkerende problemen onderzoeken](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/nl.html#chapter=06).
<!-- touchless-admin-video-v2-20261104:end -->


Klik op een leverancier in de wachtrij om de diagnosepagina te openen.

<figure><img src="../../../.gitbook/assets/touchless-supplier-detail-nl.png" alt="De pagina Leveranciersdiagnose met uitkomsttegels, trend en twee probleemclusters"><figcaption><p>De pagina Leveranciersdiagnose: uitkomsttegels, trend met periodekiezer en twee probleemclusters, gesorteerd op verwachte stijging. Voorbeeldorganisatie met demogegevens; de namen van leveranciers zijn fictief.</p></figcaption></figure>

De pagina toont:

* **Vier tegels met eindresultaten**: Pure Touchless, AP Touchless, AP Assisted en procesuitzondering; elke tegel opent de documenten.
* **De trend** met een eigen periodekiezer: 30 dagen, 90 dagen, 6 maanden, 1 jaar of een zelfgekozen bereik (tot twee jaar). Dit wijzigt alleen de grafiek.
* **Probleemclusters** (zie hieronder).
* **Wijzigingsgeschiedenis** (Change history): de wijzigingen die u voor deze leverancier hebt toegepast en wat ze hebben gedaan.
* **Recente voorbeelden** (Recent examples): voorbeelddocumenten, in twee tabbladen: **Needed attention** en **Went touchless**.
* **Diagnose supplier with AI**: analyseert alle clusters van de leverancier (beheerders).

Een korte opmerking verklaart een lege pagina, bijvoorbeeld: *5 documenten van deze leverancier worden nog verwerkt en hebben nog geen analyseresultaat.* of *Alle 40 voltooide documenten van deze leverancier liepen touchless door: er valt niets te diagnosticeren.*

### Probleemclusters

Een **cluster** groepeert de documenten van één leverancier die om dezelfde **eerste reden** stopten. In plaats van 40 afzonderlijke problemen ziet u "3 problemen".

<figure><img src="../../../.gitbook/assets/touchless-issue-cluster-nl.png" alt="Een geopende clusterkaart met de eerste blokkade, wat te wijzigen en het wijzigingsvoorstel"><figcaption><p>Een geopende clusterkaart: de eerste blokkade, <strong>What to change</strong> en een <strong>Change proposal</strong> met risico, bereik en open vragen. Hier omvat het cluster 58 documenten en is het +18,7 pp waard. Voorbeeldorganisatie met demogegevens; de namen van leveranciers zijn fictief.</p></figcaption></figure>

**Voorbeeldcluster (illustratief).**

* **Headline**: *Required field missing* in fase *Field Validation*
* **Affected**: 28 documenten. **Recoverable**: 28 documenten. **Expected lift**: +2,8 pp
* **Suspected cause**: de leverancier drukt het PO-nummer onder de tabel af, waar de extractie niet kijkt
* **What to check next**: vergelijk het gedrukte en uitgelezen ordernummer en daarna de extractieconfiguratie voordat u een wijziging voorstelt
* **Owner**: Consultant. **Confidence**: Medium. **Source**: Hypothesis

Wat een clusterkaart toont:

| Onderdeel | Betekenis |
| --- | --- |
| **First blocker** en **stage** | De reden en de pipelinefase waar de documenten stoppen. Er zijn meer dan 30 redenen, bijvoorbeeld *Supplier not identified*, *Purchase order not found*, *Unit price outside PO tolerance*, *Rejected by the ERP*, *E-invoice validation failed* |
| **Affected / Recoverable / Expected lift** | Hoeveel documenten, hoeveel er kunnen worden teruggewonnen, hoeveel procentpunten dat oplevert |
| **Suspected cause / Confirmed cause** | Wat DocBits denkt (of wat een persoon heeft bevestigd) dat de reden is |
| **Evidence** en **Missing evidence** | Waarop de bevinding is gebaseerd, en wat DocBits **niet** kon vaststellen. Lees **Missing evidence** voordat u de rest vertrouwt |
| **What to change** | Concrete stappen met **Open**-links naar de instellingen. Een label geeft het type aan: *Configuration change*, *Master data change*, *Supplier template change*, *Process change*, *Supplier action needed*, *Not fixable* |
| **Owner** | DocBits, Customer, Consultant, Supplier or Unassigned |
| **Sample documents** | Echte documenten uit het cluster om te bekijken |

**Fixable in DocBits** en **Supplier action only** worden in twee groepen getoond. Bij *Supplier action only* verandert niets in DocBits het resultaat: de leverancier moet het document corrigeren en opnieuw sturen.

### Waar komt een aanbeveling vandaan

Elke oorzaak toont zijn **source**, zodat u een afgeleide bevinding van een gok kunt onderscheiden:

| Bron | Betekenis |
| --- | --- |
| **Deterministic** / **Rule-based** | Een regel heeft het afgeleid uit het vastgelegde pipelinebewijs. Er was geen taalmodel bij betrokken |
| **Hypothesis** | Een taalmodel heeft het voorgesteld op basis van het clusterbewijs. Beschouw het als een aanwijzing en controleer het voordat u handelt |
| **Confirmed** | Een persoon heeft het bewijs beoordeeld en de oorzaak bevestigd |

AI-teksten worden geschreven in de taal van uw organisatie. Als een cluster in een andere taal is geanalyseerd, gebruikt u **Analyse in this language**.

## PO-matchingclusters

Als de eerste blokkade van een cluster een reden voor PO-matching is (bijvoorbeeld *PO item mismatch* of *Purchase order not found*), toont de clusterkaart hoe DocBits probeert de factuur aan de inkooporder te koppelen. Zie [PO-matchingdiagnose](touchless-po-matching-diagnosis.md).

## Wie corrigeert de gegevens?

| Bewijs | Waar onderzoeken of oplossen? |
| --- | --- |
| Origineel en extractie verschillen | Extractie of leveranciersconfiguratie |
| Extractie correct, Infor-prijs/hoeveelheid/eenheid aantoonbaar onjuist | Bron; AP stemt af met inkoop of stamdatabeheer |
| Infor correct, importkopie oud of onvolledig | Import of ERP-integratie |
| Waarden verschillen, afspraak nog onbekend | Inhoudelijke afstemming; oorzaak niet bevestigd |

De AP-tegel bij de leverancier telt alleen goedkeuring; het AP-koppercentage omvat ook Pure. Leg de directe actie en blijvende oplossing apart vast. Een kleine ingreep kan de factuur afronden terwijl de terugkerende oorzaak blijft bestaan. Eén cluster bewijst de historische inhoud van Infor niet. Zie het [uitgewerkte Infor-voorbeeld](touchless-po-matching-diagnosis.md#worked-example-correct-extraction-different-infor-data).

Tools en menselijke acties worden uitgelegd bij [Touchless met MCP](touchless-mcp.md).

## Gerelateerde pagina's

* [Touchless Intelligence](../../touchless-intelligence.md)
* [PO-matchingdiagnose](touchless-po-matching-diagnosis.md)
* [Documentspoor](touchless-document-trace.md)
* [Wijzigingsvoorstellen en rapporten](touchless-change-proposals.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->
