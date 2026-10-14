# Regelbeheer

<figure><img src="../../../../.gitbook/assets/rule_management.png" alt="Regelbeheer"><figcaption><p>Pagina Regelbeheer</p></figcaption></figure>

Met Regelbeheer maakt en beheert u op TOML gebaseerde regels voor conflictoplossing die worden gebruikt tijdens PO-matching en documentexport. Elke regelset definieert hoe DocBits omgaat met discrepanties tussen factuurgegevens en inkoopordergegevens.

## Regellijst

De hoofdtabel toont alle regelconfiguraties:

| Kolom | Beschrijving |
|--------|-------------|
| **Name** | De naam van de regelset. Items met het label **default** zijn door het systeem geleverde sjablonen. |
| **Description** | Een samenvatting van wat de regelset afhandelt. |
| **Last Modified By** | De gebruiker die deze regelset het laatst heeft bewerkt. |
| **Last Modified At** | Tijdstempel van de laatste wijziging. |
| **Actions** | Menu met drie puntjes om te bewerken, te kopiëren of te verwijderen. |

Klik op **+ New** om een nieuwe regelset aan te maken, of klik op een bestaande naam om de regeleditor te openen.

---

## Naslag regelstructuur

Dit onderdeel geeft een diepgaande uitleg van de regels voor conflictoplossing die in het DocBits-factureringssysteem worden gebruikt. Deze regels zijn ontworpen om automatisch om te gaan met discrepanties tussen factuurgegevens en inkoopordergegevens (PO), zodat een nauwkeurige financiële afstemming is gewaarborgd. Het systeem past deze regels toe om factuurregels, kosten en belastingen te verwerken en genereert indien nodig passende aanpassingen of notities.

## Structuur van de regels

### 1. Metadata

• version: Identificeert de versie van het mappingbestand.

• revision: Revisienummer voor het bijhouden van wijzigingen.

• author: Geeft de maker van het mappingbestand aan.

• description: Een korte beschrijving van het doel van het bestand.

• created_at & updated_at: Tijdstempels van het aanmaken en de laatste wijziging van het bestand.

### 2. Exportconfiguratie

Het onderdeel exportconfiguratie definieert de mapping tussen de gegevensvelden in het systeem en de overeenkomstige velden in de exportbestanden.

• Header: Definieert de headervelden voor de geëxporteerde factuurgegevens.

• Tax Lines: Specificeert de velden voor belastingregels in de export.

• Order Header Charges: Koppelt velden voor extra kosten op het niveau van de orderheader.

• Receipt Lines: Koppelt velden voor individuele regels in een ontvangst.

• Order Line Charges: Definieert de velden voor kosten die bij specifieke orderregels horen.

• Cost Lines: Specificeert velden voor kostenallocatieregels.

• Debit Note & Credit Note: Definieert velden voor het genereren van debet- en creditnota's bij discrepanties.

### 3. Regels voor conflictoplossing

Deze regels handelen discrepanties af tussen factuurgegevens en de bijbehorende PO-gegevens. Elke regel bestaat uit meerdere componenten:

• Name: De beschrijvende naam van de regel, die aangeeft welk type discrepantie ermee wordt afgehandeld.

• Section: Geeft aan op welk deel van de factuur (bijv. receipt_lines, line_charges) de regel van toepassing is.

• Active: Booleaanse waarde (true of false) die aangeeft of de regel momenteel actief is.

• Match Criteria: Voorwaarden die de regel activeren op basis van vergelijkingen tussen de werkelijke factuurgegevens en de verwachte PO-gegevens.

• Actions: Definieert wat het systeem moet doen wanneer de regel wordt geactiveerd, zoals het aanpassen van waarden, het toepassen van kosten of het genereren van credit-/debetnota's.

## Veelvoorkomende elementen in de regels

### Vergelijkingsoperatoren

Deze operatoren bepalen hoe de werkelijke factuurwaarden worden vergeleken met de verwachte PO-waarden:

• equal (gelijk aan)

• greater than (groter dan)

• greater than or equal to (groter dan of gelijk aan)

• less than (kleiner dan)

• less than or equal to (kleiner dan of gelijk aan)

• within tolerance (binnen tolerantie)

• outside tolerance (buiten tolerantie)


### Goedkeuringsstatus

Geeft aan of een discrepantie al dan niet is goedgekeurd:

• approved (goedgekeurd)

• rejected (afgewezen)

• any (elke)


### Actietypen

Definieert specifieke acties die worden uitgevoerd wanneer een discrepantie wordt gedetecteerd:

• receipt line

• cost line

• header charge

• line charge

• tax line

• debit note receipt line

• debit note cost line

• debit note header charge

• debit note line charge

• credit note receipt line

• credit note cost line

• credit note header charge

• credit note line charge

• credit note tax line


### Regelvoorbeelden

#### [Geval 1, 2, 3: Hoeveelheid en eenheidsprijs binnen tolerantie](transactionconfig-pro-template/case-1-2-3-quantity-and-unit-price-within-tolerance.md)

• Doel: Behandelt scenario's waarin zowel de hoeveelheid als de eenheidsprijs op de factuur binnen de toegestane tolerantiegrenzen ten opzichte van de PO liggen.

• Actie: Het systeem accepteert de factuurwaarden en berekent het totaalbedrag.



#### [Geval 4, 5: Hoeveelheid binnen tolerantie, eenheidsprijs buiten tolerantie (goedgekeurd)](./#case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved)

• Doel: Is van toepassing wanneer de hoeveelheid binnen de tolerantie ligt, maar de eenheidsprijs buiten de tolerantie valt en is goedgekeurd.

• Actie: Het systeem past de eenheidsprijs aan zodat deze overeenkomt met de PO en past eventueel noodzakelijke regelkosten toe.



#### [Geval 6: Hoeveelheid binnen tolerantie, eenheidsprijs buiten negatieve tolerantie (afgewezen)](transactionconfig-pro-template/case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

• Doel: Behandelt gevallen waarin de eenheidsprijs lager is dan verwacht en buiten het tolerantiebereik valt, wat tot afwijzing leidt.

• Actie: Het systeem past de eenheidsprijs aan zodat deze overeenkomt met de PO, genereert een creditnota voor het verschil en past indien nodig headerkosten toe.


### Omgaan met kosten en belastingen

### Tolerantie voor kosten per eenheid

• Regels in deze categorie handelen discrepanties in kosten per eenheid af, met specifieke acties afhankelijk van of de kosten binnen of buiten de tolerantie vallen en of ze zijn goedgekeurd of afgewezen.

### Aanpassingen van belastingregels

• Deze regels beheren belastingdiscrepanties door de belastingregels aan te passen of bijbehorende credit- of debetnota's te genereren op basis van de verschillen tussen de belastinggegevens van de factuur en de PO.

### Enums en opties

• Enums: Vooraf gedefinieerde lijsten met waarden die zorgen voor consistentie binnen de regels (bijv. vergelijkingsoperatoren, goedkeuringstypen).

• Opties: Vooraf gedefinieerde keuzes voor het omgaan met hoeveelheden of eenheidsprijzen, die flexibiliteit bieden bij het definiëren van regels.

## Toelichting bij de schermafbeeldingen

### Schermafbeelding 1: Interface van Regelbeheer

<figure><img src="../../../../.gitbook/assets/rule_management_interface.png" alt="Interface van Regelbeheer"><figcaption></figcaption></figure>

Deze schermafbeelding toont de interface van Regelbeheer waar beheerders alle regels voor conflictoplossing kunnen bekijken en beheren. Belangrijke elementen zijn:

• Add Rule-knop: Hiermee voegt u nieuwe regels toe.

• Lijst met regels: Toont alle actieve regels met details zoals naam, sectie en actieve status.

• Keuzelijst Section: Filtert de regels op basis van de sectie waarop ze van toepassing zijn (bijv. Receipt Lines, Line Charges).

### Schermafbeelding 2: Gedetailleerd bewerken van een regel

<figure><img src="../../../../.gitbook/assets/rule_detailed_editing.png" alt="Gedetailleerd bewerken van een regel"><figcaption></figcaption></figure>

Deze schermafbeelding toont de detailweergave van een specifieke regel die wordt bewerkt. Belangrijke elementen zijn:

• Criteria-sectie: Definieert de voorwaarden waaronder de regel wordt geactiveerd. De criteria kunnen bijvoorbeeld bepalen dat de regel moet worden toegepast als de hoeveelheid en de eenheidsprijs afwijken van de PO maar binnen de tolerantie liggen.

• Actions-sectie: Specificeert welke acties worden uitgevoerd wanneer aan de criteria is voldaan. Dit kan het aanpassen van factuurregels, het genereren van credit- of debetnota's of het toepassen van extra kosten omvatten.

• Document Type en Costing Elements: Hiermee kan de beheerder specifieke acties koppelen aan documenttypes en kostenelementen, wat flexibiliteit biedt bij het afhandelen van verschillende scenario's.
