# Doel en gebruik

Een tabelkolom is één veld van de regelitemtabel. Alles wat DocBits met een tabel doet (extractie, validatie, PO-matching, export) werkt op de kolommen die hier zijn geconfigureerd.

## Waar een kolom voorkomt

| Plaats | Wat de kolom daar doet |
|---|---|
| **Validatiescherm** | Eén kolom in de regelitemtabel. De *Titel* is de kolomkop, het *Kolomtype* bepaalt de editor (bedrag, datum, tekst, ja/nee). Verborgen kolommen worden niet getoond. |
| **Tabeltraining** | Wanneer u de tabel van een leverancier traint, koppelt u elke herkende tabelkolom aan een van deze geconfigureerde kolommen. Alleen geconfigureerde kolommen kunnen worden gekoppeld. |
| **AI-tabelextractie** | De AI vult de geconfigureerde kolommen. Een kolom met *AI gebruiken* wordt door de AI gevuld, ook voor leveranciers met getrainde regels. |
| **Validatieregels** | Controles op regelniveau, zoals *hoeveelheid × eenheidsprijs = regeltotaal*, draaien op de standaardkolommen `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT`. |
| **PO-matching** | Heeft de standaardkolommen artikelnummer, eenheidsprijs, hoeveelheid en totaalbedrag nodig. Zonder deze kolommen toont het document *Line Item Table is missing Mandatory column for PO*. |
| **Export** | Elke niet-verborgen kolom maakt deel uit van de regelitemgegevens die naar het ERP worden verzonden. De exportmapping verwijst naar de *Kolomnaam*. |
| **Scripts** | Scripts lezen en schrijven kolommen via de *Kolomnaam*, bijvoorbeeld `row["TOTAL_AMOUNT"]`. |

## Bereik

* Tabelkolommen worden **per tabel** geconfigureerd, en een tabel hoort bij een **documenttype**. Factuurkolommen hebben geen invloed op leveringsbonnen.
* De configuratie geldt **per organisatie**. Suborganisaties erven deze.
* Welke kolommen voor een bepaalde leverancier *gevuld* worden, wordt bepaald door de training van die leverancier of door de AI; de kolomconfiguratie zegt alleen welke kolommen bestaan.

## Typische redenen om de configuratie te wijzigen

* Een klantspecifieke waarde moet per regel worden vastgelegd (kostenplaats, projectnummer, intern artikelnummer) → voeg een kolom toe.
* Een standaardkolom wordt nooit gebruikt en maakt het validatiescherm onoverzichtelijk → verberg de kolom.
* Een kolom moet vóór de export altijd gevuld zijn → markeer de kolom als *Verplicht*.
* Een waarde komt uit de ERP-lookup en mag niet door gebruikers worden bewerkt → markeer de kolom als *Alleen-lezen*.
* De AI herkent een kolom beter dan de getrainde regels (bijvoorbeeld vrije-tekstomschrijvingen) → markeer de kolom met *AI gebruiken*.

## Gerelateerde pagina's

* [Een nieuwe kolom toevoegen](adding-a-new-column.md)
* [Kolommen bewerken en verwijderen](editing-and-deleting-columns.md)
* [Tabel Extractie Probleemoplossing](../../../../../overview-and-basics/faq/document-processing/table-extraction-troubleshoot.md)
