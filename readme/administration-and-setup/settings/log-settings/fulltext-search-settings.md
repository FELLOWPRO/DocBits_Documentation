# Volledige-Tekstzoek-Instellingen

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Volledige-Tekstzoek-Instellingen"><figcaption><p>Volledige-Tekstzoek-Instellingen — Dialoog "Module vereist"</p></figcaption></figure>

De Volledige-Tekstzoek-Instellingen bepalen wat DocBits indexeert en hoe die inhoud doorzoekbaar wordt over documenten, ERP-stamgegevens en sjablonen. De instellingenpagina opent alleen wanneer de **module Volledige-Tekstzoek** is ingeschakeld — zie [Volledige-Tekstzoek](../document-processing/module/fulltext-search.md) voor de gebruikersgerichte zoekquerytaal.

## Vereisten

De module Volledige-Tekstzoek moet worden geactiveerd in **Instellingen → Documentverwerking → Module → Dashboards → Volledige tekstzoek**. Als de module niet is ingeschakeld, vraagt een dialoogvenster u om:

* **Naar Modules** — Open de Module-instellingenpagina om de configuratie te bekijken.
* **Nu activeren** — Activeer de module Volledige-Tekstzoek direct (start een DocSearch-abonnement).

De instellingenpagina zelf wordt beschikbaar zodra de module actief is.

## Indeling van de pagina

De instellingenpagina is georganiseerd in drie tabbladen, elk met een ander type inhoud dat Volledige-Tekstzoek kan indexeren.

### Tabblad "Documenten"

Het tabblad Documenten behandelt alles rondom het indexeren van verwerkte documenten:

* **Indexeringsstatistieken** — totalen voor geïndexeerde en wachtende documenten, op verzoek bijgewerkt.
* **Vectorvoorkeuren** — drie organisatie-brede schakelaars die regelen of vectorindexering naast de tekstindex loopt voor documenten. Vectorindexering voedt de `vector:`-zoekmodus en de functie "Zoek vergelijkbare".
* **Herindex-acties** — start een volledige of incrementele herindex. Tijdens een herindex ziet u live voortgang (documenten per minuut, ETA), de huidige streamstatus en de laatste fout (indien aanwezig).
* **Synchronisatiediagnostiek** — diagnostiek op aanvraag voor gevallen waarin de index niet meer synchroon lijkt met de onderliggende documentopslag.

<mark>Herindexering is niet destructief — de bestaande zoek blijft werken terwijl de nieuwe index wordt opgebouwd.</mark>

### Tabblad "ERP"

Het tabblad ERP regelt indexering voor ERP-stamgegevens — leveranciers, klanten, artikelen en vergelijkbare entiteiten. Elke entiteit heeft zijn eigen schakelaar:

* **Indexering** — indexeer de entiteit tekstueel, zodat hij doorzoekbaar is vanuit het dashboard.
* **Vector** — indexeer de entiteit vectorieel, zodat hij door semantische queries kan worden gematcht.

Gebruik de actie **Alles schakelen** bovenaan de lijst om dezelfde aan/uit-status op alle entiteiten tegelijk toe te passen. Indexering start op de achtergrond; een indicator op elke rij toont wanneer hij bezig is.

### Tabblad "Sjablonen"

Het tabblad Sjablonen toont de sjabloonversies die de Volledige-Tekstindex kent. Gebruik deze weergave om na een redeploy te bevestigen dat de sjabloonversies waarvan u afhankelijk bent aanwezig zijn in de index.

## Wat wordt geïndexeerd

Eenmaal ingeschakeld en geconfigureerd laat Volledige-Tekstzoek gebruikers:

* Zoeken over alle documentinhoud (niet alleen de metadatavelden).
* Documenten vinden op tekst in geüploade bestanden.
* Geavanceerde zoekoperatoren gebruiken voor precieze queries.
* Resultaten rechtstreeks vanuit het dashboard benaderen.
* Semantisch zoeken gebruiken (prefix `vector:`) wanneer vectorindexering aan staat voor dat type inhoud.

Zie de modulepagina [Volledige-Tekstzoek](../document-processing/module/fulltext-search.md) voor de volledige naslag van de queryt­aal, inclusief bereikqueries, slimme filters en de AI-zoekmodus.
