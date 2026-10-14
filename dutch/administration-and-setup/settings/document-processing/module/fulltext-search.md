# Volledige tekstzoekopdracht

Met de volledige tekstzoekopdracht kunnen gebruikers de werkelijke inhoud van documenten en elk geëxtraheerd veld doorzoeken — niet alleen bestandsnamen en ID's.

<figure><img src="../../../../.gitbook/assets/fulltext-search-required-dialog.png" alt="Dialoogvenster „Fulltext Module Required“ wanneer de module is uitgeschakeld"><figcaption><p>Het dialoogvenster «Fulltext Module Required» verschijnt op pagina's die afhankelijk zijn van de module.</p></figcaption></figure>

## Zonder de module

Wanneer de volledige tekstzoekopdracht niet is ingeschakeld, kan de zoekbalk van het dashboard slechts een kleine reeks gestructureerde velden doorzoeken. Vrije tekst valt terug op het matchen tegen:

* `filename`
* `ID` van het document
* `invoice_id`
* `purchase_order`

Alles buiten deze velden wordt genegeerd. Er is geen zoeken op inhoud en geen ondersteuning voor bereiken, operatoren of slimme filters.

## Met de module ingeschakeld

Door de volledige tekstzoekopdracht te activeren wordt zoeken in elk geëxtraheerd veld van een document mogelijk en wordt de zoekbalk van het dashboard vervangen door een rijkere zoektaal. Query's kunnen veldfilters, bereikvergelijkingen, logische operatoren, relatieve datums en slimme filters combineren.

<figure><img src="../../../../.gitbook/assets/fulltext-search-dashboard-query.png" alt="Zoekbalk van het dashboard met een bereikquery en de gefilterde documentenlijst"><figcaption><p>De zoekbalk van het dashboard accepteert de uitgebreide zoektaal. Typ een query en druk op <kbd>Enter</kbd> om de documentenlijst te filteren.</p></figcaption></figure>

### Veldgebonden query's

Zoek in een specifiek geëxtraheerd veld door de veldnaam met een dubbele punt te laten voorafgaan. Veldnamen volgen de API-conventie (kleine letters, snake\_case) en gelden voor elk veld dat door uw documenttypen wordt vastgelegd — leverancier, factuurmetagegevens, regels, aangepaste velden.

```
supplier_name: Acme
invoice_id: INV-1234
status: ready_for_validation
```

### Bereikquery's

Vergelijkingsoperatoren werken op numerieke en datumvelden. Zowel open vergelijkingen als begrensde bereiken worden ondersteund.

```
total_amount > 5000
total_amount <= 10000
invoice_due_date between 2026-01-01 and 2026-04-30
```

### Logische operatoren

Combineer clausules met `AND`, `OR` en `NOT`, met haakjes om de evaluatievolgorde vast te leggen. `IN`-lijsten controleren een veld tegen een verzameling mogelijke waarden.

```
supplier_name: Acme AND total_amount > 1000
(status: ready_for_validation OR status: validated) AND invoice_date: this_month
NOT status: archived
status IN (ready_for_validation, exported)
```

### Relatieve datums

Tijdsexpressies worden geëvalueerd op het moment van de query. Ze kunnen overal worden gebruikt waar een datum wordt verwacht.

```
imported_on: today()
invoice_date: last_week
imported_on: this_quarter
```

### Slimme filters

Snelkoppelingen van één token voor veelvoorkomende query's. Ze werken op zichzelf of als onderdeel van een grotere expressie.

```
overdue
@User
#INV-1234
$5k+
```

* `overdue` — documenten waarvan de vervaldatum is verstreken.
* `@User` — filter op toegewezen persoon; vervang `User` door de gebruikersnaam.
* `#INV-1234` — snelzoeken op document-identifier.
* `$5k+` — bedragen hoger dan 5.000 in de valuta van het document.

## Aanvullende functies

Twee gespecialiseerde zoekmodi bouwen voort op de module voor volledige tekstzoekopdrachten. Beide vereisen dat de module is ingeschakeld en kunnen niet zelfstandig worden gebruikt.

### Vectorzoeken

Vectorzoeken vindt documenten die semantisch lijken op de query, niet alleen lexicaal overeenkomen. Het dashboard behandelt elke query die met `vector:` begint als vectorzoekopdracht, laat deze door de document-embeddings lopen en rangschikt de resultaten op gelijkenis.

```
vector: frozen food invoices
```

Vectorindexering wordt op de pagina **Instellingen volledige tekstzoekopdracht** los van de tekstindex beheerd. Door deze uit te schakelen worden voor nieuwe documenten geen embeddings meer aangemaakt, terwijl de tekstindex behouden blijft.

### AI-zoekopdracht

De AI-zoekopdracht accepteert query's in natuurlijke taal en gebruikt een LLM om er gestructureerde filters uit te halen, die vervolgens tegen de volledige-tekstindex worden uitgevoerd. Plaats `ai:` voor de query.

```
ai: invoices from Ruiz over 1000 last quarter
```

AI-zoekopdracht en vectorzoeken zijn niet uitwisselbaar: vectorzoeken vindt vergelijkbare inhoud, AI-zoekopdracht vertaalt taal naar filters. De AI-zoekopdracht heeft geen eigen schakelaar — zij maakt gebruik van de bestaande volledige-tekst- en vectorindexen.

<figure><img src="../../../../.gitbook/assets/fulltext-search-settings-page.png" alt="Pagina „Instellingen volledige tekstzoekopdracht“ met de sub-indexen Documents, Vector Index en Fulltext (Text)"><figcaption><p>Instellingen volledige tekstzoekopdracht. De vectorindex heeft een eigen schakelaar; de tekstindex draait zolang de module actief is.</p></figcaption></figure>

## Vereisten

* De OpenSearch-infrastructuur draait op de achtergrond om de index te voeden.
* Bij de eerste activering worden alle bestaande documenten opnieuw geïndexeerd. De duur schaalt met het aantal documenten in de organisatie.
* Alleen organisatiebeheerders kunnen modules in- of uitschakelen.

## De module inschakelen

1. Ga naar **Instellingen → Documentverwerking → Module**.
2. Schakel onder de groep **Dashboards** de optie **Full text search** in.
3. Bevestig het abonnementsvenster indien dit verschijnt.
4. Wacht totdat de eerste herindexering is voltooid voordat u op volledige-tekstquery's vertrouwt.

<figure><img src="../../../../.gitbook/assets/fulltext-search-module-toggle.png" alt="Modulepagina met de schakelaar „Full text search“ onder de groep Dashboards"><figcaption><p>De schakelaar <strong>Full text search</strong> staat onder <strong>Module → Dashboards &#x26; Analytics</strong>.</p></figcaption></figure>

{% hint style="info" %}
De prijsstelling van de module voor volledige tekstzoekopdrachten loopt via uw DocBits-verkoopcontact. De abonnementsbevestiging verschijnt bij de eerste activering van de module.
{% endhint %}

## Zie ook

* [Instellingen volledige tekstzoekopdracht](../../log-settings/fulltext-search-settings.md) — indexbeheer en schakelaar voor de vectorindex.
* [Fulltext- en Vector Search-functies](../../global-settings/document-types/script/scripting-in-docbits/fulltext-search-functions.md) — scripting-API voor `fulltext_search()` en `vector_search()`.
* [Overzicht modules](README.md) — volledige lijst met optionele DocBits-modules.
