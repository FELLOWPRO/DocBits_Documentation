# Analyse-dashboard

## Overzicht

Het **Analyse-dashboard** biedt volledig inzicht in de prestaties van uw documentverwerking. Het volgt hoe lang documenten in elke fase van hun traject doorbrengen — van import tot export — en helpt u knelpunten te identificeren, prestaties te vergelijken tussen organisaties, documenttypen en leveranciers, en uw resultaten te benchmarken tegen het **DocBits Global Average** (wereldwijd gemiddelde).

Elk document doorloopt verschillende fasen:

**Nieuw** (geïmporteerd) → **Actief** (verwerking) → **Klaar voor validatie** (in afwachting van gebruikersbeoordeling) → **In afwachting van goedkeuring** → **Export** (voltooid en geëxporteerd)

In elke fase verstrijkt tijd — het Analyse-dashboard vertelt u precies **hoeveel** en **waar** u uw verbeteringen moet richten.

### Twee soorten knelpunten

Het dashboard helpt u onderscheid te maken tussen:

* **Systeemknelpunten** — Hoe lang DocBits bezig is met automatische verwerking (OCR en tekstextractie, documentclassificatie, veldextractie, automatische validatie). Te optimaliseren via configuratie en systeembronnen.
* **Gebruikersknelpunten** — Tijd doorgebracht met wachten op handmatige validatie en goedkeuring (wachttijd in de wachtrij, handmatige gegevenscorrectie, beoordeling en validatie, goedkeuringsworkflows). Te optimaliseren via workflow en personeelsinzet.

## Hoe activeren

Het Analyse-dashboard wordt aangestuurd door een module-instelling. Zodra deze is ingeschakeld, verschijnt er een **Analyse-dashboard**-item in de linker zijbalk.

1. Navigeer naar **Instellingen → Documentverwerking → Module → Dashboard en analyse**.
2. Schakel de optie **Analyse-dashboard** in.

<mark style="color:red;">**Opmerking**</mark>: Het Analyse-dashboard vereist een **Analytics Dashboard-abonnement**.

<mark style="color:red;">**Opmerking**</mark>: Toegang tot het Analyse-dashboard is beperkt tot gebruikers met **beheerdersrechten**.

## Flow-typen

Kies de juiste invalshoek voor uw analyse. Elk flow-type geeft u een ander perspectief op dezelfde gegevens.

| Flow-type | Doel | Kernvraag |
| --- | --- | --- |
| **Status** | Volg de levenscyclus van documenten van import tot export | *"Wat is de totale tijd van mijn documenten van import tot export?"* |
| **Verwerking** | Technische analyse van moduleprestaties | *"Welke verwerkingsstappen vormen knelpunten?"* |
| **Gebruikersinteractie** | Menselijke contactpunten en wachttijden | *"Hoe lang wachten documenten op gebruikers?"* |

Gebruik de **Flow-type**-schakelaar boven aan het dashboard om tussen perspectieven te wisselen.

<figure><img src="../.gitbook/assets/analytics_dashboard_flow_types.png" alt="Flow Type Switch"><figcaption></figcaption></figure>

### Status-flow

Volgt het documenttraject van **Nieuw** tot **Geëxporteerd** — nuttig voor end-to-end levenscyclusanalyse.

<figure><img src="../.gitbook/assets/analytics_dashboard_status_flow.png" alt="Status Flow"><figcaption></figcaption></figure>

### Verwerkings-flow

Analyseert prestaties over alle **technische verwerkingsmodules** (OCR, classificatie, extractie, validatie) — nuttig voor het identificeren van knelpunten aan de systeemkant.

<figure><img src="../.gitbook/assets/analytics_dashboard_processing_flow.png" alt="Processing Flow"><figcaption></figcaption></figure>

### Gebruikersinteractie-flow

Richt zich op **menselijke contactpunten** — wachttijd in de wachtrij, handmatige validatie, beoordeling en goedkeuring — nuttig voor het identificeren van knelpunten in workflow en personeelsinzet.

<figure><img src="../.gitbook/assets/analytics_dashboard_user_interaction_flow.png" alt="User Interaction Flow"><figcaption></figcaption></figure>

## Filteropties

Het dashboard ondersteunt krachtige multidimensionale filtering. Alle grafieken, kaarten en tabellen worden in realtime bijgewerkt op basis van de actieve filters.

### Zoeken

Vind direct elk document op **naam** of **unieke ID**.

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_search.png" alt="Search Filter"><figcaption></figcaption></figure>

### Flow-stappen

Selecteer specifieke stappen om uw analyse te richten. Het in-/uitschakelen van stappen herberekent ook de timingstatistieken voor de andere componenten van het dashboard.

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_flow_steps.png" alt="Flow Steps Filter"><figcaption></figcaption></figure>

### Suborganisatie, documenttype, leverancier, groep

Vergelijk prestaties tussen:

* **Suborganisaties** — verschillende bedrijfsonderdelen of tenants
* **Documenttypen** — facturen, inkooporders, pakbonnen, enzovoort
* **Leveranciers** — om te identificeren welke leveranciers de langste verwerkingstijden veroorzaken
* **Groepen** — om prestaties te vergelijken tussen toegewezen gebruikersgroepen (beschikbaar voor de flow-typen **Status** en **Gebruikersinteractie**)

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_dimensions.png" alt="Sub-Organization, Document Type, Supplier, Group Filters"><figcaption></figcaption></figure>

<mark style="color:red;">**Opmerking**</mark>: Het filter **Groep** is alleen van toepassing op documenten die **rechtstreeks aan een groep zijn toegewezen**. Documenten die zijn toegewezen aan een individuele gebruiker — zelfs als die gebruiker lid is van een groep — worden **niet** opgenomen in de resultaten van het groepsfilter.

### Tijdsbereik

Analyseer elke periode van **7 dagen** tot een **volledig jaar**, of stel een **aangepast bereik** in met behulp van de datumkiezer.

<figure><img src="../.gitbook/assets/analytics_dashboard_filter_time_range.png" alt="Time Range Filter"><figcaption></figcaption></figure>

## Flow-stappen-kaarten

Elke kaart vertegenwoordigt een flow-stap op basis van het geselecteerde **Flow-type**. De kaarten passen zich aan uw selectie aan — met levenscyclusfasen voor *Status*, verwerkingsmodules voor *Verwerking* of gebruikerscontactpunten voor *Gebruikersinteractie*.

Elke kaart toont:

* **Min, Gem., Max** tijden voor de stap
* Een vergelijking tussen uw **Gem. tijd** en het **DocBits Global Average** (wanneer de vergelijkingsschakelaar aanstaat)
* Een selectiecirkel om de stap **op te nemen of uit te sluiten** van de geaggregeerde timingberekeningen die worden gebruikt door de Grafiek Gemiddelde Tijd, de Tijdtrendgrafiek en de Datatabel

Met een schakelaar **Alles selecteren** in de header kunt u alle stappen tegelijk in- of uitschakelen.

<figure><img src="../.gitbook/assets/analytics_dashboard_flow_steps_card.png" alt="Flow Steps Card showing Min, Avg, Max"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_step_toggle.png" alt="Toggle Steps On/Off"><figcaption></figcaption></figure>

### Vergelijk met het wereldwijde gemiddelde

De schakelaar **Vergelijk met het wereldwijde gemiddelde** bepaalt of het DocBits Global Average wordt weergegeven op de kaarten en in de grafiek. Indien ingeschakeld, wordt de gemiddelde tijd op elke kaart kleurgecodeerd:

* **Groen** — uw Gem. tijd is gelijk aan of lager dan het Global Average
* **Oranje** — uw Gem. tijd is tot **+25%** boven het Global Average
* **Rood** — uw Gem. tijd is **+25%** of meer boven het Global Average

<figure><img src="../.gitbook/assets/analytics_dashboard_global_average_comparison.png" alt="Compare with DocBits Global Average"><figcaption></figcaption></figure>

## Grafiek Gemiddelde Tijd

De Grafiek Gemiddelde Tijd visualiseert hoe de verwerkingstijd is verdeeld over de geselecteerde flow-stappen. Gebruik de selector **Groeperen op** om te vergelijken op verschillende dimensies:

* **Flow-stappen** — zie welke stappen de meeste tijd kosten
* **Suborganisatie** — identificeer variaties tussen bedrijfsonderdelen
* **Documenttype** — vergelijk verwerkingstijden tussen documenttypen
* **Leverancier** — ontdek welke leveranciers de langste verwerkingstijden hebben
* **Groep** — vergelijk tussen toegewezen gebruikersgroepen (alleen flow-typen Status en Gebruikersinteractie)

Wanneer **Vergelijk met het wereldwijde gemiddelde** is ingeschakeld, toont de grafiek ook het DocBits Global Average voor benchmarking.

<figure><img src="../.gitbook/assets/analytics_dashboard_average_time_chart.png" alt="Average Time Chart"><figcaption></figcaption></figure>

## Topdocumenten

De kaart **Topdocumenten** somt individuele documenten op die overeenkomen met de actieve filterset, gerangschikt op totale tijdsduur.

* Schakelaar **Sorteervolgorde** — wissel tussen **aflopend** (eerst de langzaamste) en **oplopend** (eerst de snelste).
* Vervolgkeuzelijst **Paginagrootte** en paginering — blader door de resultatenset.
* **Verberg / toon** een document via het oogpictogram ernaast — verborgen documenten worden uitgesloten van alle timingberekeningen op het dashboard.
* **Verberg / toon alle** documenten in het filter via het oogpictogram in de header.
* **Klik op een document** (bestandsnaam of voortgangsbalk) om de document-ID naar het klembord te kopiëren.

<figure><img src="../.gitbook/assets/analytics_dashboard_top_documents.png" alt="Top Documents"><figcaption></figcaption></figure>

## Tijdtrendgrafiek

Volg prestatietrends in de tijd en spot afwijkingen. De Tijdtrendgrafiek toont de **Gem. tijd** van de momenteel geselecteerde flow-stappen en kan worden gegroepeerd op:

* **Flow-stappen** — één lijn per geselecteerde stap
* **Suborganisatie**
* **Documenttype**
* **Leverancier**
* **Groep** (beschikbaar voor de flow-typen **Status** en **Gebruikersinteractie**)

Hierdoor is het eenvoudig om een plotselinge piek voor een specifieke leverancier te detecteren, of een geleidelijke toename voor een specifiek documenttype, voordat het een kritiek probleem wordt.

<figure><img src="../.gitbook/assets/analytics_dashboard_time_trend.png" alt="Time Trend Chart"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_time_trend_grouped.png" alt="Time Trend Chart Grouped"><figcaption></figcaption></figure>

## Datatabel

De Datatabel biedt volledige toegang tot alle onderliggende rijgegevens voor de actieve filterset.

* **Sleep kolommen naar het paneel Verborgen kolommen** (links van de tabel) om ze uit de weergave te verwijderen. Verborgen kolommen worden gebruikt voor aggregatie — **Min / Max / Gem.** timings worden dynamisch herberekend op basis van de zichtbare kolommen. Sleep een chip terug naar de tabel (of klik op het **+**-pictogram) om de kolom te herstellen.
* **Sorteer** door op kolomkoppen te klikken en **herschik** kolommen via drag-and-drop.
* **CSV downloaden** via de knop in de kaartheader — alleen de momenteel zichtbare kolommen worden geëxporteerd.

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table.png" alt="Data Table"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table_hide_columns.png" alt="Hide Columns to Recalculate Aggregations"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/analytics_dashboard_data_table_export.png" alt="Export Data Table as CSV"><figcaption></figcaption></figure>
