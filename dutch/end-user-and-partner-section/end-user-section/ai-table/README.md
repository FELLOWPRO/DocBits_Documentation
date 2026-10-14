# AI Tabel

De AI Geëxtraheerde tabel is de regelitemtabel die DocBits met AI uitleest wanneer een leverancier geen getrainde tabelregels heeft. Ze verschijnt op het validatiescherm onder de koptekstvelden. Deze pagina beschrijft wanneer u deze tabel krijgt, hoe u de extractie opnieuw uitvoert en hoe u stuurt wat er wordt geëxtraheerd.

## Wanneer u de AI-tabel krijgt

* Een beheerder heeft **AI-tabel extractie** ingeschakeld (Instellingen → Documentverwerking → Classificatie en extractie). Als deze uitstaat, toont het tabelgebied *AI Table will display here. Enable in …*.
* De leverancier heeft **geen opgeslagen regels**. Zodra iemand de tabel van de leverancier traint en op *Regels opslaan* klikt, vervangen de opgeslagen regels de AI-tabel voor die leverancier; de rijen verschijnen dan in het tabblad *Geëxtraheerde tabel* in plaats van in het tabblad *AI Geëxtraheerde tabel*.
* Uitzondering: kolommen met de markering **AI gebruiken** in de tabelkolominstellingen worden door de AI gevuld, ook voor leveranciers met opgeslagen regels, zie [AI gebruiken per kolom](#ai-gebruiken-per-kolom).

Welke AI-tier de tabel leest (Fast, Full, Nexus) wordt per organisatie ingesteld en kan per leverancier worden overschreven onder *Meer instellingen* op het validatiescherm, zie [Leverancierspecifiek AI-model](../validation-screen/supplier-specific-ai-model-for-field-and-table-extraction.md).

## De AI-tabel opnieuw extraheren

Gebruik dit wanneer rijen ontbreken of een kolom verschoven is en u de AI het opnieuw wilt laten proberen, bijvoorbeeld na het toevoegen van een [tag](ai-table-tags.md):

1. Voeg [tags](ai-table-tags.md) toe of wijzig ze in het veld onder de tabel en klik op **Toepassen**. De AI bouwt de tabel voor dit document opnieuw op met uw tags en kolomwijzigingen; er wordt nog niets voor de leverancier opgeslagen. Als het document PO-gematchte regels heeft, waarschuwt DocBits dat de matches door het opnieuw opbouwen worden verwijderd.
2. Tevreden met het resultaat? Klik op **Opslaan** (*Regels opslaan*), zodat het volgende document van deze leverancier op dezelfde manier wordt geëxtraheerd.
3. Om opnieuw te beginnen, klikt u op **Verwijderen** (*Regels verwijderen*): DocBits bevestigt *Rules has been deleted successfully* en voert de AI-extractie opnieuw uit zonder opgeslagen tags of opmaak.

*Regels verwijderen* verwijdert de tags en opmaakregels die voor deze leverancier zijn opgeslagen, niet de tabelkolomconfiguratie. Om het hele document (koptekst en tabel) opnieuw te extraheren nadat een beheerder instellingen of kolommen heeft gewijzigd, gebruikt u in plaats daarvan *Opnieuw starten* in het documentmenu op het dashboard.

## AI gebruiken per kolom

Elke tabelkolom heeft een vlag **AI gebruiken** (Instellingen → Globale instellingen → Documenttypen → [Tabelkolommen](../../../administration-and-setup/settings/global-settings/document-types/table-columns/README.md)). Met de vlag ingeschakeld vult de AI die kolom, ook wanneer de leverancier opgeslagen regels heeft; de andere kolommen blijven uit de regels komen. Typisch gebruik: een vrije-tekstomschrijvingskolom die getrainde regels slecht vastleggen, of een waarde die op de pagina van plaats verandert.

Houd er rekening mee dat de AI die kolom dan uit de hele rij afleidt. Als de AI er consequent de verkeerde waarde in zet (bijvoorbeeld het regeltotaal in *Kosten*), mislukt de regeltotaalcontrole op elke rij. Schakel in dat geval *AI gebruiken* voor die kolom uit, of voeg een tag toe die de AI vertelt wat de kolom is.

## Gestructureerde extractie

Met **Gebruik gestructureerde extractie (AI)** ingeschakeld in de organisatie-instellingen geeft de AI de tabel terug in een vaste structuur die direct op de geconfigureerde tabelkolommen wordt afgebeeld, in plaats van de kolomkoppen van de leverancier over te nemen. Kolomnamen komen dan altijd overeen met uw configuratie; een kolom die de leverancier afdrukt maar die u niet hebt geconfigureerd, wordt niet geëxtraheerd. Vraag uw beheerder om dit in te schakelen wanneer de kolomkoppen van leveranciers sterk variëren en u veel tijd kwijt bent aan het opnieuw koppelen.

## Werken met de geëxtraheerde tabel

Hier zijn de belangrijkste mogelijkheden en gebruiksinstructies:

* **Kolommen Verwijderen**: Als bepaalde kolommen in de geëxtraheerde tabel niet nodig zijn, kunnen gebruikers deze eenvoudig verwijderen door op het pictogram "Verwijder kolom" (weergegeven door drie verticale stippen) naast de kolomkop te klikken. Dit helpt om de tabel op te schonen en zich te concentreren op relevante informatie.

<figure><img src="../../../.gitbook/assets/ai-table1.png" alt=""><figcaption></figcaption></figure>

* **Valutaformaat Wijzigen**: Het valutaformaat kan worden gewijzigd door het gewenste formaat te selecteren uit het dropdownmenu naast het veld "Valuta". Dit zorgt ervoor dat de valutawaarden in het gewenste formaat worden weergegeven, waardoor het gemakkelijker wordt om de financiële gegevens te interpreteren en te analyseren.

<figure><img src="../../../.gitbook/assets/ai-table2.png" alt=""><figcaption></figcaption></figure>

* **Niet-Gemapte Kolommen Tonen/Verbergen**: Standaard zijn alleen de gemapte kolommen (kolommen met geëxtraheerde gegevens) zichtbaar in de tabel. Gebruikers kunnen echter kiezen om de niet-gemapte kolommen te tonen of te verbergen door op de knop "Verberg niet-gemapte kolommen" of "Toon niet-gemapte kolommen" onderaan de tabel te klikken. Deze functie is nuttig wanneer gebruikers alle beschikbare kolommen willen bekijken, zelfs als ze momenteel geen gegevens bevatten.

<figure><img src="../../../.gitbook/assets/ai-table3.png" alt=""><figcaption></figcaption></figure>

* **Tabelkoppen Wijzigen**: De tabelkoppen (kolomnamen) kunnen worden gewijzigd door op de kop te klikken en de gewenste naam in te voeren. Deze functie stelt gebruikers in staat om de kolomnamen aan te passen zodat ze beter aansluiten bij hun terminologie of voorkeuren, waardoor de gegevens leesbaarder en begrijpelijker worden.

<figure><img src="../../../.gitbook/assets/ai-table4.png" alt=""><figcaption></figcaption></figure>

* **Opslaan wat u hebt gewijzigd**: **Opslaan** naast de tags (tooltip *Regels opslaan*) slaat de huidige kolomkoppeling, verborgen kolommen en tags voor deze leverancier op. Het volgende document van de leverancier wordt daarmee geëxtraheerd.

Deze functies geven u controle over de geëxtraheerde gegevens. Wanneer dezelfde leverancier elke keer dezelfde correcties nodig heeft, train de tabel dan eenmalig, zie [Training Line Fields / Tabeltraining](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md); de AI-tabel wordt dan voor die leverancier niet meer gebruikt.
