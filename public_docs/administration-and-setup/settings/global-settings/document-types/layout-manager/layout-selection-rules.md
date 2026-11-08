# Layout Selection Rules

## Overzicht

Een **layout** bepaalt welke velden en groepen een gebruiker ziet — en in welke volgorde — op de schermen **Field Validation**, **Approval**, **Reject** en **Review** van een document. Je ontwerpt layouts in de [Layout Manager](./).

Klassiek koos DocBits de layout op basis van de **herkomst** van het document: het land of de regio uit de taalinstellingen van het document, zoals `DE` of `US`. Elke herkomst had een eigen kopie van de layout, en niets anders kon de keuze beïnvloeden.

Met **layout selection rules** worden layouts herbruikbare bouwstenen die losstaan van de herkomst, en bepalen **regels** welke layout een document krijgt:

> *Wanneer* het document aan een voorwaarde voldoet, *dan* krijgt het deze layout. Regels worden van boven naar beneden gecontroleerd; **de eerste overeenkomende regel wint**. Komt geen enkele regel overeen, dan wordt de **default layout** gebruikt.

De herkomst blijft beschikbaar — als één voorwaarde van vele. Een regel kan net zo goed kijken naar de leverancier, het bedrag, de documentstatus, de extractiemethode of een willekeurig headerveld.

### Problemen die ze oplossen

| Vereiste                                                            | Klassieke layouts op basis van herkomst    | Met selectieregels                                                                  |
| ------------------------------------------------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------- |
| Facturen van één leverancier hebben extra velden nodig (project, douanenummer) | onmogelijk zonder nieuwe herkomst           | regel _Supplier ID is 20723_ → layout "Factuur met projectvelden"                    |
| DE-, AT- en CH-documenten moeten er hetzelfde uitzien               | drie kopieën van dezelfde layout om te onderhouden | één layout, één regel per herkomst (of een ANY-groep) die ernaar verwijst            |
| E-facturen hebben een eenvoudiger scherm nodig dan gescande pdf's   | niet mogelijk                                | regel _Extraction Method is ELECTRONIC\_DOCUMENT_ → layout "E-factuur"                 |
| Facturen met een hoge waarde hebben meer velden nodig op het goedkeuringsscherm | niet mogelijk                                | Approval-regel _Total Amount greater than 10000_ → layout "Goedkeuring hoge waarde"        |
| De tweede goedkeurder moet een ander scherm zien dan de eerste      | apart layouttype "tweede goedkeuring"      | Approval-regel _Document Status is Pending second approval_ → layout "Second approval" |

## Op regels gebaseerde layouts inschakelen

Op regels gebaseerde layouts worden **per documenttype** ingeschakeld door een **organisatiebeheerder**.

1. Ga naar **Settings → Document Processing → Document Types**.
2. Klik op het **settings**-pictogram (tandwiel) op de kaart van het documenttype.
3. Open **Manage Layouts** en zet de schakelaar aan.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-manage-layouts-toggle-en-20261102.png" alt="De sectie Manage Layouts in de aanvullende instellingen van een documenttype, met de ondertitel Enable Layout Management en de schakelaar Manage Layouts aan"><figcaption><p>De schakelaar Manage Layouts in de aanvullende instellingen van een documenttype</p></figcaption></figure>
<!-- English source image: lsr-manage-layouts-toggle-en-20261102.png -->

De link **Layouts** op de kaart van het documenttype opent nu **Layouts & Selection Rules**.

### Wat er gebeurt als je het inschakelt

DocBits zet je bestaande layouts op basis van herkomst eenmalig om in regels — voor dit documenttype en voor elk scherm:

* De layout van de herkomst **DEFAULT** wordt de **default layout** (de terugvaloptie).
* Elke layout van een specifieke herkomst wordt een regel **"Layout for XX"** met de voorwaarde _Document Origin is XX_, die naar die layout verwijst. Deze regels krijgen prioriteiten in stappen van 10 (bijvoorbeeld 2000, 2010, 2020 …), zodat je je eigen regels ervoor, ertussen of erna kunt plaatsen.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-default-layout-row-en-20261102.png" alt="De onderkant van de lijst met selectieregels: de laatste herkomstregels Layout for UY en Layout for VN, gevolgd door de FALLBACK-rij Default layout met de markering is_default, die wordt gebruikt wanneer geen enkele regel erboven overeenkomt."><figcaption><p>De herkomstregels die bij de activering worden aangemaakt, gevolgd door de default layout (FALLBACK)</p></figcaption></figure>
<!-- English source image: lsr-default-layout-row-en-20261102.png -->

Er wordt niets verwijderd of gewijzigd aan de layouts zelf. Direct na de activering krijgt elk document daarom precies de layout die het ervoor ook kreeg. Pas wanneer je regels toevoegt of wijzigt, verandert het gedrag.

**Uitschakelen** brengt het documenttype onmiddellijk terug naar selectie op basis van herkomst. De regels blijven bewaard maar worden niet gebruikt, en ze werken weer zodra je de schakelaar opnieuw aanzet.

## Het scherm Layouts & Selection Rules

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-layouts-overview-en-20261102.png" alt="Het tabblad Layouts van Layouts and Selection Rules voor het documenttype INVOICE: de schermtabbladen Field Validation, Approval, Reject en Review, het filter All, My layouts en System, de knop New layout en layoutkaarten met Edit, Clone en Delete."><figcaption><p>Het tabblad Layouts: elke layout van het documenttype als kaart</p></figcaption></figure>
<!-- English source image: lsr-layouts-overview-en-20261102.png -->

* **Layouts / Selection rules** (in de paginakop) schakelen tussen de lijst met layouts en de lijst met regels. De getallen tonen hoeveel er zijn.
* **Field Validation / Approval / Reject / Review** schakelen het **scherm** om. Elk scherm heeft zijn eigen layouts, eigen regels en eigen default layout — een Approval-regel wijzigt het validatiescherm nooit.
* Op het tabblad **Layouts** kun je layouts aanmaken, bewerken, klonen en verwijderen. Elke kaart toont of een regel de layout gebruikt ("Not targeted by rules" wanneer geen enkele regel dat doet). Filter met **All / My layouts / System**; systeemlayouts worden met DocBits meegeleverd en kunnen worden bekeken en gekloond, maar niet gewijzigd.

{% hint style="info" %}
Eerste en tweede goedkeuring delen de **Approval**-layouts en -regels. Om de tweede goedkeuringsfase een eigen scherm te geven, voeg je een Approval-regel toe met de voorwaarde _Document Status is Pending second approval_ — zie het [voorbeeld](layout-selection-rules.md#different-screens-for-first-and-second-approval).
{% endhint %}

## Hoe een layout wordt gekozen

Telkens wanneer een document wordt geopend, en opnieuw nadat het is opgeslagen, bepaalt DocBits de layout voor het huidige scherm:

1. De **actieve regels** van het scherm worden gecontroleerd in volgorde van **prioriteit** (laagste nummer eerst). **De eerste regel waarvan de voorwaarde waar is, wint**, en de bijbehorende layout wordt gebruikt.
2. Komt geen enkele regel overeen, dan wordt de **default layout** gebruikt.
3. Is er ook geen default, dan valt DocBits terug op de klassieke keuze op basis van herkomst.

Regels waarvan de layout is verwijderd of leeg is, worden overgeslagen.

### Een uitgewerkt voorbeeld

Regels van het scherm **Field Validation**:

| Prioriteit | Regel                  | Voorwaarde                                   | Layout                         |
| -------- | --------------------- | ------------------------------------------- | ------------------------------ |
| 5        | Behaelterbau invoices | _Supplier ID is HP0000278_                  | Invoice with project fields    |
| 10       | E-invoices            | _Extraction Method is ELECTRONIC\_DOCUMENT_ | E-invoice                      |
| 2020     | Layout for DE         | _Document Origin is DE_                     | Field Validation Layout (DE)   |
| —        | Default layout        | —                                           | Field Validation Layout (Base) |

Welke layout elk document krijgt:

| Document | Leverancier  | Extractie  | Herkomst | Layout                         | Omdat                                               |
| -------- | --------- | ----------- | ------ | ------------------------------ | ----------------------------------------------------- |
| 1        | HP0000278 | e-invoice   | DE     | Invoice with project fields    | prioriteit 5 komt als eerste overeen; latere regels worden niet gecontroleerd |
| 2        | 10040     | e-invoice   | DE     | E-invoice                      | prioriteit 5 komt niet overeen, 10 wel                |
| 3        | 10040     | scanned PDF | DE     | Field Validation Layout (DE)   | alleen de herkomstregel komt overeen                  |
| 4        | 10040     | scanned PDF | US     | Field Validation Layout (Base) | geen enkele regel komt overeen → default              |

**De volgorde is belangrijk**: plaats specifieke regels (één leverancier) boven algemene regels (één land).

### Wanneer een gebruiker een veld wijzigt waar de regels naar kijken

De layout wordt altijd gekozen op basis van de **huidige** waarden van het document. Corrigeert een gebruiker bijvoorbeeld de leverancier op het validatiescherm, dan kiest DocBits na het opslaan opnieuw een layout en kan het scherm naar een andere layout overschakelen. Er gaan geen gegevens verloren: een veld dat geen deel uitmaakt van de nieuwe layout behoudt zijn waarde; het wordt alleen niet getoond totdat weer een layout geldt die het bevat.

## Selectieregels beheren

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rules-list-en-20261102.png" alt="Het tabblad Selection rules van het scherm Field Validation: een tabel met de kolommen Priority, Rule en voorwaarden, Target layout, Source en Active, de eerste rij gemarkeerd met FIRST, sleepgrepen links en een menu met drie puntjes op elke rij."><figcaption><p>Het tabblad Selection rules van het scherm Field Validation</p></figcaption></figure>
<!-- English source image: lsr-rules-list-en-20261102.png -->

Elke rij toont de **prioriteit** (de eerste rij is gemarkeerd met **FIRST**), de **regelnaam en -sleutel** met de bijbehorende **voorwaarden**, de **target layout**, de **source**-badge en een **Active**-schakelaar.

| Taak | Hoe |
| ------------------- | ---------------------------------------------------------------------------------- |
| Een regel aanmaken | **New rule**                                                                       |
| Een regel bewerken | Klik op de rij                                                                      |
| De volgorde wijzigen | Sleep de greep links van een rij omhoog of omlaag. De nieuwe volgorde wordt direct opgeslagen. |
| Een regel uitschakelen | Schakelaar **Active**. Inactieve regels worden genegeerd.                          |
| Dupliceren of verwijderen | Menu **⋮** van de rij                                                              |
| Een regel zoeken | **Search rules…**                                                                  |

De **source**-badge geeft aan waar een regel vandaan komt: **System**-regels worden met DocBits meegeleverd. Een systeemregel bewerken maakt een kopie voor je organisatie, getoond als **Customized**; het origineel blijft intact en kan worden hersteld. Regels die je zelf aanmaakt zijn **Custom**.

### De default layout

De laatste rij, gemarkeerd met **FALLBACK** en **is\_default**, is de default layout: die wordt gebruikt wanneer geen enkele regel erboven overeenkomt en heeft geen voorwaarde. Ze wordt aangemaakt wanneer je de functie inschakelt (vanuit de layout van de herkomst DEFAULT).

{% hint style="info" %}
Om een andere terugvallayout te gebruiken, maak je een regel **zonder enige voorwaarde** en geef je die het hoogste prioriteitsnummer, zodat ze als laatste wordt gecontroleerd. Ze komt overeen met elk document waarmee geen eerdere regel overeenkwam, nog voordat de default wordt bereikt.
{% endhint %}

## Een regel aanmaken

Klik op **New rule** op het tabblad Selection rules van het scherm dat je wilt wijzigen.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rule-editor-en-20261104.png" alt="De editor voor een layoutselectieregel voor een factuur: bovenaan de samenvattende zin, dan Step 1 Scope and priority met Rule name, Rule key, Document Type, Layout Type, Priority en een selectievakje Log execution, Step 2 Applies when met de voorwaarde Document Origin is AR en de knoppen Add Condition en Add nested group, Step 3 Target layout met de geselecteerde Field Validation Layout (AR), en rechts het live voorvertoningspaneel met Sample document, matched_by, Resolved layout, Priority hit en watched_fields."><figcaption><p>De recordeditor: reikwijdte en prioriteit, de voorwaarden, de target layout en de live voorvertoning van wat de regel zou doen.</p></figcaption></figure>
<!-- English source image: lsr-rule-editor-en-20261104.png -->

De zin bovenaan vat de regel samen terwijl je hem opbouwt — "When doc.doc_origin = AR, an INVOICE document gets the origin-ar layout for Field validation. Checked at priority 0 — the first matching rule wins."

### Step 1 — Scope & priority

| Instelling                          | Wat het doet                                                                                                      |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| **Rule Name**                       | Wordt getoond in de regellijst. Beschrijf de zakelijke aanleiding: "Behaelterbau invoices", "E-invoices", "High value approval". |
| **Rule key**                        | Gegenereerd uit de naam; blijft gelijk wanneer je de regel hernoemt.                                              |
| **Document Type** / **Layout type** | Het documenttype en het scherm waarvoor de regel geldt. Overgenomen van waar je op **New rule** klikte.           |
| **Priority**                        | Lagere nummers worden eerst gecontroleerd. Laat tussenruimte (5, 10, 20 …) zodat je later regels kunt invoegen.   |
| **Log execution**                   | Legt elke beoordeling van de regel vast, zodat je later kunt nagaan waarom een document wel of niet overeenkwam. Laat het uit totdat je die trace nodig hebt. |

### Step 2 — Applies when

De voorwaarde waaraan een document moet voldoen. Je kunt gebruiken:

* **documentattributen**: Document Origin, Extraction Method, Document Status, Sub Document Type,
* **headervelden**: Supplier ID, Total Amount, Currency, Purchase Order en elk ander veld van het documenttype,
* een **aangepast JSON-pad** (Advanced).

Tabelkolommen zijn niet beschikbaar: de layout wordt één keer voor het hele document gekozen.

Laat de stap leeg om met elk document op deze prioriteit overeen te komen. Hoe voorwaarden werken — ALL / ANY, geneste groepen, alle operatoren, lege waarden, hoofdletters en kleine letters — wordt uitgelegd op [Regelvoorwaarden (Applies when)](../rule-conditions-applies-when.md).

### Step 3 — Target layout

Klik op de layout die het document moet krijgen. De lijst toont je eigen layouts en de systeemlayouts van het geselecteerde scherm. Een layout kan niet worden verwijderd zolang een regel er nog naar verwijst.

### Live voorvertoning · /resolve

Het paneel rechts toont wat de regel doet voor een voorbeelddocument met de waarden van je voorwaarden:

| Regel               | Betekenis                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------- |
| **Sample document** | De waarden die voor de voorvertoning worden gebruikt, overgenomen uit je voorwaarden                   |
| **matched\_by**     | `rule` als een regel overeenkwam, anders de default                                                    |
| **Resolved layout** | De layout die het voorbeelddocument zou krijgen                                                       |
| **Priority hit**    | De prioriteit van de regel die overeenkwam                                                             |
| **watched\_fields** | De velden waarvan de layoutkeuze afhangt. Wijzigt een gebruiker er één, dan wordt de layout opnieuw gekozen. |

Klik op **Create Rule** (of **Save rule** bij het bewerken) om op te slaan. **Cancel** brengt je terug naar de regellijst.

## Voorbeelden

### Extra velden voor één leverancier

Scherm **Field Validation** · prioriteit **5** · _Supplier ID is HP0000278_ · target _Invoice with project fields_ (een kloon van je standaardlayout met de extra velden voor project en kostenplaats).

### Eén layout voor meerdere landen

Scherm **Field Validation** · prioriteit **100** · **ANY of**: _Document Origin is Deutsch_, _Document Origin is Austria_, _Document Origin is Switzerland_ · target _DACH invoice_. Deactiveer de gemigreerde regels "Layout for AT" en "Layout for CH" als ze naar oudere kopieën verwijzen.

### Een eenvoudiger scherm voor e-facturen

Scherm **Field Validation** · prioriteit **10** · _Extraction Method is ELECTRONIC\_DOCUMENT_ · target _E-invoice_ (zonder OCR-gerelateerde velden).

### Een strenger goedkeuringsscherm voor hoge bedragen

Scherm **Approval** · prioriteit **10** · _Total Amount greater than 10000_ · target _High value approval_ (met kostenplaats, budgethouder en contractnummer).

### Verschillende schermen voor eerste en tweede goedkeuring

Scherm **Approval** · prioriteit **5** · _Document Status is Pending second approval_ · target _Second Approval Layout_. Documenten in de eerste goedkeuringsstap komen niet overeen en krijgen de default layout van Approval.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/lsr-rule-editor-approval-en-20261104.png" alt="Een Approval-selectieregel in de editor: Rule name Layout for DE, prioriteit 2000, de voorwaarden Document Status is Pending second approval en Document Origin is Deutsch, de target layout Second Approval Layout (DE), en de live voorvertoning met het voorbeelddocument, matched_by rule, de opgeloste layout en priority hit 2000."><figcaption><p>Een Approval-regel voor de tweede goedkeuringsstap — de live voorvertoning rechts laat al zien dat deze regel wint bij prioriteit 2000.</p></figcaption></figure>
<!-- English source image: lsr-rule-editor-approval-en-20261104.png -->

### Een speciaal afwijzingsscherm voor sommige leveranciers

Scherm **Reject** · prioriteit **10** · _Supplier ID is one of_ `10040, 10041` · target _Reject with reason codes_.

## Aanbevolen werkwijzen

* **Specifiek vóór algemeen.** Leveranciersregels boven landregels, landregels boven de default.
* **Laat prioriteitsruimte** (5, 10, 20 …) zodat nieuwe regels passen zonder hernummering.
* **Baseer voorwaarden op betrouwbare velden.** Leverancier en herkomst worden vroeg ingesteld en veranderen zelden. Voorwaarden op velden die gebruikers vaak bewerken, laten het scherm van layout wisselen terwijl ze werken.
* **Kloon in plaats van vanaf nul te beginnen.** Kloon je standaardlayout en pas die aan, zodat alle layouts dezelfde basisstructuur behouden.
* **Controleer de live voorvertoning** en open na het wijzigen van regels een echt document van elk soort.
* **Houd een zinvolle default aan** voor elk scherm, zodat geen enkel document zonder layout eindigt.

## Probleemoplossing

| Symptoom                                          | Wat te controleren                                                                                                                        |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| Een document krijgt de verkeerde layout          | Een eerdere regel komt als eerste overeen. Bekijk de regels erboven, of de **Priority hit** in de voorvertoning.                      |
| De default wordt gebruikt hoewel een regel zou moeten overeenkomen | Is de regel **Active**? Komt de voorwaarde overeen met de exacte waarde (hoofdletters, spaties)? Staat de regel op het juiste **scherm**-tabblad? |
| De layout verandert terwijl een gebruiker werkt  | Een veld in **watched\_fields** is gewijzigd. Baseer de regel op een stabieler veld.                                                  |
| Een layout kan niet worden verwijderd            | Een regel verwijst er nog naar. Wijs die regel eerst opnieuw toe of verwijder hem.                                                    |
| Er wordt helemaal geen layout getoond            | Geen enkele regel kwam overeen, er is geen default en er bestaat geen layout op basis van herkomst voor dit scherm. Voeg een regel zonder voorwaarde toe als vangnet. |
| Er veranderde niets na de activering             | Verwacht: de activering reproduceert de vorige keuze op basis van herkomst. Voeg je eigen regels toe.                                 |
| De tweede goedkeuring toont de layout van de eerste goedkeuring | Voeg een Approval-regel toe op _Document Status is Pending second approval_ boven de andere Approval-regels.                        |

## Gerelateerd

* [Regelvoorwaarden (Applies when)](../rule-conditions-applies-when.md)
* [Aangepaste validatieregels](../custom-validation-rules.md)
* [Transformatieregels](../transformation-rules/)
* [Navigeren in de Layout Manager](navigating-the-layout-manager.md)
