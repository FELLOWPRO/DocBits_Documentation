# Classificatie en extractie

## Overzicht

In de Instellingen voor **Classificatie en extractie** kun je:

* **Documenten splitsen** inschakelen op basis van QR-codes
* **Bedrag opmaak** configureren
* **Tabel extractie** instellen
* Verwerking van niet-ondersteunde **ZUGFeRD**-bestanden in- of uitschakelen
* Speciale classificatieregels definiëren
* Aangepast getrainde **AI-modellen** monitoren die in het classificatieproces worden gebruikt

Deze pagina biedt een gedetailleerde uitleg van alle beschikbare instellingen.

## Toegang tot Instellingen voor Classificatie en extractie

Ga naar de Instellingen voor **Classificatie en extractie** via:\
**Instellingen → Documentverwerking → Classificatie en extractie**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_classification_and_extraction.png)

## Documenten splitsen

In de sectie **Documenten splitsen** kun je configureren of een geüpload document moet worden opgesplitst in meerdere documenten wanneer er een **streepjescode** op een van de pagina's verschijnt.

Om deze functie te activeren:

1. Ga naar de sectie **Documenten splitsen**.
2.  Open het keuzemenu.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_14.png)
3.  Selecteer **Gesplitst op barcode/QR-code**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_15.png)

Je hebt vervolgens de optie om:

* Een of meer streepjescode-typen te selecteren die moeten worden gedetecteerd.
*   Een regex-patroon op te geven waaraan de streepjescode moet voldoen om het splitsen van documenten te activeren.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_16.png)

## Bedrag opmaak

In de sectie **Bedrag opmaak** heb je twee opties:

* **Afronding toestaan tijdens het vergelijken van bedragen:**\
  Indien ingeschakeld, is een tolerantie van ±0,5 toegestaan tijdens bedragvergelijking.\
  Indien uitgeschakeld, geldt een standaardtolerantie van ±0,05.
* **Vereist exacte overeenkomst voor bedragvergelijking:**\
  Indien ingeschakeld, moeten bedragen exact overeenkomen met nul tolerantie.\
  Indien uitgeschakeld, is een tolerantie van ±0,05 toegestaan.

<mark style="color:red;">**Opmerking**</mark>: Slechts één van deze instellingen kan tegelijk actief zijn.

## Tabel extractie

{% hint style="info" %}
**Voorwaarden voor een werkende tabelextractie**

* Het documenttype heeft **tabelkolommen** (Instellingen → Globale instellingen → Documenttypen → [Tabelkolommen](../../global-settings/document-types/table-columns/README.md)). Zonder kolommen is er niets om naar te extraheren.
* **Tabel extractie** of **AI-tabel extractie** is hieronder ingeschakeld, voor de hele organisatie.
* Het document heeft leesbare tekst: OCR is uitgevoerd, of E-Text wordt gebruikt voor digitaal aangemaakte pdf's ([OCR-instellingen](../ocr-settings.md)).
* Training en AI-modellen gelden **per leverancier**. Een getrainde tabel geldt alleen voor documenten van de leverancier waarop ze is getraind.
{% endhint %}

Je kunt tabellen uit documenten extraheren door **Tabel extractie** of **AI-tabel extractie** in te schakelen. Een getrainde tabel (of deze nu AI-gebaseerd of handmatig is) wordt altijd gekoppeld aan een specifieke leverancier.

**Tabel extractie:** Activeert regelgebaseerde tabelextractie. Tabellen worden per leverancier getraind op het validatiescherm (*Ga naar tabelextractieweergave*).\
Meer informatie over training vind je [hier](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).

**AI-tabel extractie:** Gebruikt AI om de tabel van elke leverancier zonder training te extraheren. Als de resultaten voor één leverancier niet nauwkeurig genoeg zijn, train dan de tabel van die leverancier; de opgeslagen regels krijgen voor die leverancier dan voorrang op de AI.

**Gebruik Tabel extractie Vision (AI):** De AI leest de paginaafbeelding in plaats van de tekstlaag. Helpt bij gescande documenten en tabellen zonder duidelijke tekststructuur; langzamer.

**Gebruik gestructureerde extractie (AI):** De AI geeft de tabel terug in een vaste structuur die direct op de geconfigureerde tabelkolommen wordt afgebeeld. Aanbevolen wanneer de kolomkoppen op de documenten sterk variëren.

**Tabelextractie voor kostenelement:** Wanneer ingeschakeld, kan DocBits kostenelementen uit tabellen op regelniveau extraheren en deze dienovereenkomstig classificeren.\
Een gedetailleerde uitleg is beschikbaar [hier](table-extraction-for-costing-element.md).

**Automatisch belastingcode ophalen:** Wanneer ingeschakeld, vult het systeem automatisch het veld **Belastingcode** op het Validatiescherm, mits er een belastingcodeveld is geconfigureerd.\
Meer informatie over deze instelling vind je [hier](auto-extract-tax-code.md).

**Extractieregels opslaan (alleen admin):** Alleen beheerders kunnen in de tabeltraining op *Regels opslaan* klikken. Schakel dit in wanneer gebruikers steeds regels opslaan die de extractie van een leverancier verstoren.

**AI-model:** Selecteert de AI-tier die voor tabelextractie wordt gebruikt: **Fast** (standaard), **Full** (hoogste nauwkeurigheid, langzamer) of **Nexus** (optionele derde tier). De tabel onder de keuzelijst toont:

* Welke **leveranciers** welk AI-model gebruiken
* Of ze E-Text gebruiken
* Opties om een item te verwijderen of de trainingsgegevens te resetten

Deze instelling wordt in detail uitgelegd [hier](ai-model.md).

### Waarom ziet de tabel er per leverancier anders uit?

Alles wat DocBits over een tabel leert, wordt **per leverancier** opgeslagen:

* **Opgeslagen regels** (tabeltraining): positie van de tabel en koppeling van de kolommen op de lay-out van die leverancier.
* **AI-tabeltags en opmaakregels**: aanwijzingen die de gebruiker voor de AI-tabel van die leverancier heeft opgeslagen.
* **Leverancierspecifiek AI-model**: de tier die voor die leverancier is gekozen onder *Meer instellingen* op het validatiescherm.

Leverancier A met opgeslagen regels toont dus een deterministische tabel in het tabblad *Geëxtraheerde tabel* van het validatiescherm, terwijl leverancier B zonder regels de *AI Geëxtraheerde tabel* krijgt. Om leverancier B zich als A te laten gedragen, train je de tabel van B eenmalig. Om een leverancier te resetten, verwijder je de regels op het validatiescherm of reset je de trainingsgegevens in de AI-modeltabel.

### Voorkeurssleutels

Elke schakelaar in deze sectie wordt opgeslagen als een organisatievoorkeur. Gebruik de sleutel wanneer je de waarde instelt via de API (`/preferences/set_preference`), een script of de DocBits MCP (`get_preference` / `set_preference`).

| Instelling (UI-label) | Voorkeurssleutel | Waarden |
|---|---|---|
| Tabel extractie | `TABLE_EXTRACTION_SETTING` | `true` / `false` |
| AI-tabel extractie | `USE_AI_TABLE_EXTRACTION` | `true` / `false` |
| Gebruik Tabel extractie Vision (AI) | `TABLE_EXTRACTION_USE_VISION` | `true` / `false` |
| Gebruik gestructureerde extractie (AI) | `USE_STRUCTURED_EXTRACTION` | `true` / `false` |
| Tabelextractie voor kostenelement | `CHARGES_TABLE_EXTRACTION` | `true` / `false` |
| Automatisch belastingcode ophalen | `AUTO_EXTRACT_TAX_CODE` | `true` / `false` |
| Extractieregels opslaan (alleen admin) | `ONLY_ADMIN_CAN_SAVE_RULES` | `true` / `false` |
| AI-model | `AI_MODEL` | `gpt-5.4-mini` (Fast), `gpt-5.5` (Full), `qwen3.8-max` (Nexus) |
| Tabelextractieversie (bevestigingsdialoog) | `TBL_EXT_VERSION` | versiestring |
| OCR-instellingen → Gebruik AI-gegevens voor tabellen indien beschikbaar | `USE_AI_DATA_FOR_TABLE` | `true` / `false` |
| OCR-instellingen → Gebruik E-Text indien beschikbaar | `USE_ETEXT_IF_AVAILABLE` | `true` / `false` |

Opmerkingen:

* Booleaanse voorkeuren worden opgeslagen als de strings `true` / `false`; een sleutel die nooit is ingesteld, telt als `false`. Als je `1` of `0` verstuurt, slaat DocBits `true` / `false` op.
* Een niet-ingestelde `AI_MODEL` betekent **Fast**.
* Het wijzigen van een sleutel geldt voor documenten die daarna worden verwerkt. Start een document opnieuw om het met de nieuwe instelling opnieuw te extraheren.
* Keuzes per leverancier (E-Text, AI-model, opgeslagen regels) zijn geen organisatievoorkeuren; ze worden op het validatiescherm ingesteld onder *Meer instellingen* bij een document van die leverancier.

## Elektronisch document

**Proces Niet-ondersteund ZUGFeRD PDF:** Indien ingeschakeld, worden niet-ondersteunde **ZUGFeRD**-versies verwerkt als standaard-pdf's en wordt de ingesloten XML genegeerd.

De lijst met ondersteunde **ZUGFeRD**-versies vind je [hier](../../global-settings/document-types/edi/zugferd/README.md).

## Classificatieregels

In de sectie **Classificatieregels** kun je specifieke **regex**-patronen en criteria definiëren om het systeem te helpen documenten automatisch te classificeren tijdens de verwerking.

Om deze sectie te openen, klik op het tabblad **Classificatieregels** bovenaan de pagina.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_1.png)

### Nieuwe classificatieregel toevoegen

Om een nieuwe regel te maken:

1.  Klik rechtsboven op **Toevoegen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_2.png)
2. Vul de volgende velden in:
   * **Patroon**: Het regex-patroon waar het systeem naar moet zoeken om classificatie te activeren.
   * **Type**: Waar naar het patroon moet worden gezocht (bijv. **Streepjescode**).
   * **Suborganisatie** _(optioneel)_: Geef aan op welke suborganisatie de regel van toepassing is.
   * **Documenttype**: Definieer het documenttype dat moet worden toegewezen wanneer het patroon overeenkomt.
   *   **Subdocumenttype** _(optioneel)_: Geef een subtype op voor een gedetailleerdere classificatie.

       ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_3.png)
3.  Klik op **Opslaan** om je classificatieregel op te slaan.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### Een classificatieregel bewerken

Om een bestaande regel te bewerken:

1.  Klik op de drie puntjes in de kolom **Acties**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Selecteer **Bewerking**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_6.png)
3. Breng de gewenste wijzigingen aan.
4.  Klik op **Opslaan** om de updates toe te passen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_4.png)

### Een classificatieregel verwijderen

Om een regel te verwijderen:

1.  Klik op de drie puntjes in de kolom **Acties**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_5.png)
2.  Selecteer **Verwijderen**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_7.png)

## AI-modellen

De sectie **AI-modellen** toont alle op maat getrainde modellen die specifiek voor jouw behoeften zijn verfijnd.

### Toegang tot de sectie AI-modellen

Om deze sectie te openen, klik op het tabblad **AI-modellen** bovenaan de pagina.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_8.png)

### Modelcategorieën

Modellen zijn georganiseerd in categorieën. Onder elke categorienaam wordt het aantal modellen weergegeven dat deze bevat.\
Klik op een categorie om de details te bekijken.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_9.png)

Bovenaan de pagina van de geselecteerde categorie zie je kerninformatie over elk model:

* **Type**: Het type model.
* **Alleen eerste pagina**: Geeft aan of het model alleen de eerste pagina van een document verwerkt.
* **Versie**: Het versienummer van het model.

### Modeltabel

Alle modellen binnen een categorie worden weergegeven in een tabel met de volgende informatie:

* **Naam**: De naam van het model.
* **Volgend model**: Het model dat de output van het huidige model verder zal verwerken.
* **Documenttype**: Het primaire documenttype dat door het model tijdens classificatie wordt toegewezen.
* **Document-subtypen**: De subtypen waarin het document verder wordt geclassificeerd.
* **Prioriteit**: Het prioriteitsniveau dat de positie van het model in de classificatiewachtrij bepaalt.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_11.png)

### Een model bewerken

Om een model te bewerken:

1.  Klik op het penpictogram in de kolom **Acties** naast het model dat je wilt bewerken.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_10.png)
2. Werk de beschikbare velden bij:
   * **Volgend model**: Selecteer het model dat de output van het huidige model moet verwerken.
   * **Documenttype**: Kies het documenttype waarmee het model de input moet classificeren.
3.  Klik op **Opslaan** om je wijzigingen toe te passen.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/classification_and_extraction_12.png)
