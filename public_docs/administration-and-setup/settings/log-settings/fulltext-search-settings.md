# Instellingen voor zoeken in volledige tekst

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Instellingen voor zoeken in volledige tekst in de sandbox, met een dialoogvenster dat uitlegt dat de module vereist is en knoppen voor Go to Modules en Enable Now"><figcaption><p>Wanneer zoeken in volledige tekst is uitgeschakeld, legt dit dialoogvenster de volgende stappen uit.</p></figcaption></figure>

De instellingen voor zoeken in volledige tekst bepalen wat DocBits indexeert en hoe die inhoud doorzoekbaar wordt in documenten, ERP-stamgegevens en sjablonen. De instellingenpagina toont een dialoogvenster met vereisten totdat de **Fulltext Search module** is ingeschakeld — zie [Zoeken in volledige tekst](../document-processing/module/fulltext-search.md) voor de zoektaal voor eindgebruikers.

## Vereisten

De module Fulltext Search moet zijn geactiveerd in **Settings → Module → Dashboards & Analytics → Full text search**. Als de module niet is ingeschakeld, biedt het dialoogvenster drie acties:

* **Help (?)** — Opent de documentatie over zoeken in volledige tekst in een nieuw tabblad voordat u een instelling wijzigt.
* **Go to Modules** — Opent de module-instellingen onder Dashboards & Analytics om de configuratie te controleren.
* **Enable Now** — Opent het abonnementsvenster. Controleer en bevestig dat venster voordat de module wordt ingeschakeld; alleen op deze knop klikken schakelt de module nog niet in.

De instellingenpagina zelf wordt beschikbaar zodra de module actief is.

## Pagina-indeling

De instellingenpagina is ingedeeld in drie tabbladen: **Documents**, **ERP** en **Templates**. Elk tabblad heeft betrekking op een ander inhoudstype dat Fulltext Search kan indexeren.

### Tabblad Documents

Het tabblad Documents omvat alles rond het indexeren van verwerkte documenten:

* **Indexing statistics** — totalen voor geïndexeerde en wachtende documenten, op verzoek vernieuwd.
* **Vector preferences** — drie schakelaars op organisatieniveau die bepalen of vectorindexering naast de tekstindex voor documenten loopt. Vectorindexering voedt de zoekmodus `vector:` en de functie "Find Similar".
* **Reindex actions** — start een volledige of incrementele herindexering. Tijdens een herindexering ziet u live voortgang (documenten per minuut, verwachte resterende tijd), de huidige streamstatus en de laatste fout (indien aanwezig).
* **Sync diagnostics** — diagnostiek op aanvraag voor gevallen waarin de index niet synchroon lijkt met de onderliggende documentopslag.

<mark>Herindexering is niet-destructief — bestaand zoeken blijft werken terwijl de nieuwe index wordt opgebouwd.</mark>

### Tabblad ERP

Het tabblad ERP regelt de indexering van ERP-stamgegevens — leveranciers, klanten, artikelen en vergelijkbare entiteiten. Elke entiteit heeft een eigen schakelaar:

* **Indexing** — indexeert de entiteit tekstueel, zodat deze vanuit het dashboard doorzoekbaar is.
* **Vector** — indexeert de entiteit vectorieel, zodat deze door semantische queries kan worden gevonden.

Gebruik de actie **Toggle all** bovenaan de lijst om dezelfde aan/uit-status in één keer op alle entiteiten toe te passen. De indexering start op de achtergrond; een indicator op elke rij toont wanneer deze bezig is.

### Tabblad Templates

Het tabblad Templates toont de sjabloonversies die bekend zijn bij de Fulltext-index. Gebruik deze weergave om na een nieuwe uitrol te bevestigen dat de sjabloonversies waarvan u afhankelijk bent aanwezig zijn in de index.

## Wat wordt geïndexeerd

Eenmaal ingeschakeld en geconfigureerd biedt Fulltext Search gebruikers:

* Zoeken in alle documentinhoud (niet alleen in metadatavelden).
* Documenten vinden op tekst in geüploade bestanden.
* Geavanceerde zoekoperatoren gebruiken voor precieze queries.
* Rechtstreeks vanuit het dashboard toegang tot de zoekresultaten.
* Semantisch zoeken (voorvoegsel `vector:`) wanneer vectorindexering voor dat inhoudstype is ingeschakeld.

Zie de modulepagina [Zoeken in volledige tekst](../document-processing/module/fulltext-search.md) voor de volledige referentie van de zoektaal, inclusief bereikqueries, slimme filters en de AI-zoekmodus.
