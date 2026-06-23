# Snel zoeken

**Snel zoeken** bovenaan het dashboard is de snelste manier om documenten te
vinden. Typ wat je zoekt — een naam, een status, een bedrag, een datum — en de
lijst filtert direct.

Deze gids is opgebouwd zoals het zoeken zelf:

1. **Standaardvelden** — de kolommen die elk document heeft (documentnaam,
   status, datums). Altijd beschikbaar.
2. **Fulltext-velden** — geëxtraheerde inhoud (leverancier, ordernummer,
   factuurnummer, bedragen, regels). Beschikbaar wanneer fulltext-zoeken aanstaat.
3. **Operatoren, sneltoetsen en recepten** — de volledige referentie.

> Je hoeft niets te onthouden: klik in de zoekbalk en kies een veld en waarde uit
> de lijst. De voorbeelden hieronder tonen ook de getypte vorm om direct te
> kopiëren.

---

## Hoe de zoekbalk werkt — chips, werkbalk en ruwe weergave

Zodra je een voorwaarde voltooit (een veld, een operator en een waarde) zet Snel
zoeken die om in een **chip** — een gekleurd pilletje in de balk — en begint een
nieuwe. Een chip toont het **veld**, de **operator** en de **waarde**, met een
**×** om hem te verwijderen. Chips zijn gekleurd naar waar de gegevens staan:

| Chipkleur | Veldtype |
|-----------|----------|
| **Blauw** | Standaardkolom (documentnaam, status, datums) |
| **Oranje** | Fulltext-/geëxtraheerd veld (leverancier, bedrag, factuurnummer) |
| **Paars** | Vector- (semantisch) zoeken |
| **Groen** | OCR-tekst zoeken |

Klik op een chip om hem te bewerken; klik op **×** om hem te verwijderen. Meerdere
gecombineerde chips worden standaard als **AND** gelezen.

**Werkbalk** (rechts van de balk): **ⓘ Hulp** opent de ingebouwde referentie van
velden en syntaxis; **Filters** is een snel paneel voor Status / Gebruiker /
Herstart; de **indexring** toont hoeveel van de fulltext-index is opgebouwd
(alleen wanneer fulltext-zoeken aanstaat).

**Standaard- versus ruwe weergave:** de balk toont je query als chips (standaard).
Schakel over naar **ruwe weergave** om hem als platte tekst te zien en te bewerken
— handig om een lange query te kopiëren of te typen. Je query wordt onthouden
wanneer je opnieuw laadt.

### Documenten op factuursubtype vinden

```
invoice_sub_type="Cost Invoice"
```

Het factuursubtype is een vaste lijst (bijv. **Cost Invoice**, **Purchase
Invoice**), dus `=` is een exacte match en de balk biedt een waardekiezer. Gebruik
`invoice_sub_type!="Cost Invoice"` voor alles behalve dat subtype.

## Resultaten groeperen

In plaats van een platte lijst kun je de resultaten **groeperen** op elk veld —
leverancier, status, documenttype of een datumvak:

```
group by supplier_name
```

De lijst toont inklapbare **groepskoppen**, elk met een **aantal**. Klik op een
kop om hem uit of in te klappen; klik in een groep om in te **zoomen** (die waarde
als filter toepassen). Groeperen combineert met elk filter.

<figure><img src="../../../.gitbook/assets/quick_search_16_grouping.png" alt="Resultaten gegroepeerd op leverancier"><figcaption><p><code>group by supplier_name</code> — resultaten klappen samen tot één uitklapbare kop per leverancier.</p></figcaption></figure>

---

## Deel 1 — Standaardvelden

Standaardvelden zijn de eigen kolommen van het document. Ze zijn **altijd
beschikbaar**, of fulltext-zoeken nu aanstaat of niet.

### Documenten op naam vinden

De documentnaam is de meest voorkomende zoekopdracht. Drie manieren — allemaal
**hoofdletterongevoelig**:

#### `=` → begint met

```
filename=invoice
```

Vindt documenten waarvan de naam **begint met** "invoice". Omdat hoofdletters
worden genegeerd, komen al deze overeen met `filename=invoice`:

```
Invoice.pdf   iNVoice.pdf   iNvoiCE.pdf   INVOICE.pdf
Invoice.xml   iNVoice.xml   iNvoiCE.edi   …
```

Komt **niet** overeen met `XYZ_Invoice.pdf` (daar staat "invoice" in het midden — gebruik `:`).

<figure><img src="../../../.gitbook/assets/nl_quick_search_02_filename_starts.png" alt="filename=invoice komt alleen overeen met namen die met invoice beginnen"><figcaption><p><code>filename=invoice</code> — alleen namen die <strong>beginnen met</strong> "invoice", in elke schrijfwijze (<code>INVOICE.pdf</code>, <code>iNvoiCE.pdf</code>, <code>iNVoice.pdf</code>, <code>Invoice.pdf</code> komen overeen — 7 resultaten).</p></figcaption></figure>

#### `:` → bevat (overal)

```
filename:invoice
```

Met `:` komt het woord **overal** in de naam overeen — `2026_Invoice.pdf`,
`XYZ_Invoice ABC.pdf`, `123_Invoice ABC bla bla.pdf`.

<figure><img src="../../../.gitbook/assets/nl_quick_search_03_filename_contains.png" alt="filename:invoice komt overeen met het woord overal in de naam"><figcaption><p><code>filename:invoice</code> — komt overeen met "invoice" op elke positie in de naam (ook <code>XYZ_Invoice ABC.pdf</code>).</p></figcaption></figure>

#### `="…"` → begint *of* eindigt met

```
filename="invoice"
```

Aanhalingstekens laten `=` namen matchen die met de waarde **beginnen of
eindigen**.

> **De drie in één regel:** `=` → begint met · `:` → bevat · `="…"` → begint of
> eindigt met. Alle negeren hoofdletters.

### Op status vinden

```
status=ready_for_validation
```

Status is een vaste lijst, dus `=` is een **exacte** match en de balk biedt een
waardekiezer.

### Op datum vinden

```
created_on>2026-05-25
```

Gebruik `>`, `<`, `>=`, `<=` voor datumbereiken. Ook **relatieve** datums:
`today()`, `today()-7` (laatste 7 dagen), `today()+30`.

---

## Deel 2 — Fulltext-velden

Fulltext-velden doorzoeken de **geëxtraheerde inhoud** — leverancier, ordernummer,
factuurnummer, bedragen, regels. Ze verschijnen in het **oranje** en vereisen dat
**fulltext-zoeken aanstaat**. De matchregels zijn identiek aan standaard
tekstvelden (`=` begint-met, `:` bevat, `="…"` begint-of-eindigt).

### Documenten van een leverancier vinden

```
supplier_name=Test
```

Begint-met op de geëxtraheerde leveranciersnaam; `supplier_name:fuji` matcht
overal; `supplier_name:"Ruiz Foods"` zet een waarde met spaties tussen
aanhalingstekens.

### Op bedrag vinden

```
total_amount>5000
```

Gebruik `>`, `<`, `>=`, `<=` of `between 1000 and 5000` voor een venster.

### Vinden wat ontbreekt

```
supplier_name=""
```

`=""` betekent "dit veld is **niet ingevuld**"; `supplier_name!=""` betekent
"heeft een leverancier". Dezelfde controle werkt op elk veld, bijv.
`ap_assignment_code=""`.

---

## Slimme filters — één klik

Bovenaan het zoek-dropdownmenu vind je de **Slimme filters**: kant-en-klare
zoekopdrachten met één klik. Elk is een sneltoets voor een query die je ook kunt
typen:

| Slim filter | Vindt | Komt overeen met |
|-------------|-------|------------------|
| ⚠️ **Achterstallig** | Vervaldatum verstreken | `invoice_due_date<today()` |
| 🕐 **Bijna vervallen** | Binnen 7 dagen | `invoice_due_date<=today()+7` |
| 👤 **Aan mij toegewezen** | Wacht op jouw actie | `assigned_to=<jij>` |
| 📅 **Inbox van vandaag** | Vandaag geïmporteerd | `imported_on>=today()` |
| 📋 **Wacht op validatie** | Klaar om te valideren | `status=ready_for_validation` |
| 🧾 **Elektronische documenten** | E-facturen (XML, ZUGFeRD, EDI) | `is_edoc=true` |
| ✅ **Volledige PO-match** | Volledig afgestemd op een order | `po_match_status=full_matched` |
| ➗ **Gedeeltelijke PO-match** | Gedeeltelijk afgestemd | `po_match_status=partial_matched` |
| 📉 **Onder-PO-match** | Aantal of prijs onder de order | `po_match_status=under_matched` |

De drie **PO-match**-filters en de fulltext-velden vereisen dat fulltext-zoeken
aanstaat.

---

## Deel 3 — Operatoren, verbindingen, sneltoetsen

### De ingebouwde hulp

Het **hulppictogram** in de zoekbalk opent een volledige referentie van alle
velden, operatoren en sneltoetsen van je werkruimte.

<figure><img src="../../../.gitbook/assets/nl_quick_search_08_help_modal.png" alt="De ingebouwde dashboard-zoekhulp met alle operatoren"><figcaption><p>De ingebouwde hulp <strong>Dashboard zoeken — Velden en syntaxis</strong> toont elke operator en hoe waarden matchen (bijv. "Exact / begint met").</p></figcaption></figure>

### Wat `=` betekent per veldtype

Elke tekstmatch negeert hoofdletters.

| Veldtype | Voorbeeld | `=` betekent |
|----------|-----------|--------------|
| Tekst (naam, leverancier, order) | `filename=invoice` | **begint met** |
| Tekst, overal | `filename:invoice` | **bevat** |
| Tekst, begin *of* eind | `filename="invoice"` | **begint of eindigt met** |
| Status / type / PO-match (vaste lijsten) | `status=finished` | **exact** |
| Identifiers (factuurnr., leverancier-id) | `invoice_number=INV-100` | **exact** |
| Getal | `total_amount>5000` | bereik (`> < >= <= between`) |
| Datum | `created_on>2026-01-01` | bereik + `today()±N` |

### Operatoren

| Operator | Betekenis |
|----------|-----------|
| `=` | begint-met (tekst) / exact (lijst, getal, datum) |
| `:` | bevat (tekst, overal) |
| `="…"` | begint-met of eindigt-met (tekst) |
| `!=` | het tegenovergestelde van `=` |
| `>` `<` `>=` `<=` | groter / kleiner dan |
| `between … and …` | inclusief bereik |
| `field=""` / `field!=""` | is leeg / is ingevuld |
| `today()`, `today()-7`, `today()+30` | relatieve datums |

### Verbindingen

Combineer voorwaarden met **AND** (beide), **OR** (een), **NOT** en haakjes
`( … )` om te groeperen:

```
status=ready_for_validation AND supplier_name=Test
(status=error OR status=failed) AND created_on>today()-1
```

### Sneltoetsen

Kortere schrijfwijzen voor dezelfde queries:

| Sneltoets | Komt overeen met |
|-----------|------------------|
| `total_amount gt 5000` | `total_amount>5000` (alias gt/gte/lt/lte) |
| `due_date > today` | `due_date>today()` |
| `imported_on this_week` | deze ISO-week (ook `last_week`, `this_month`, …) |
| `ap_assignment_code is empty` | `ap_assignment_code=""` |
| `status:open` | `status=ready_for_validation` (open/closed/failed/done) |
| `total_amount not between 100, 200` | `total_amount<100 OR total_amount>200` |
| `status in (finished, error)` | `status=finished OR status=error` |
| `not status=finished` | `status!=finished` |
| `filename contains rechnung` | `filename:rechnung` |
| `total_amount > 5k` | `total_amount>5000` (`k`=duizend, `M`=miljoen) |
| `overdue` | `invoice_due_date<today() AND status!=finished` |
| `#INV-1234` | `invoice_id:INV-1234` |
| `@User` | `assigned_to:User` |
| `$5000+` | `total_amount>=5000` |

### Galerij query + resultaat voor sneltoetsen

Deze voorbeelden tonen elk sneltoetspatroon met de query die je typt en het resultaat in het dashboard. De eerste groep gebruikt standaardvelden en werkt ook wanneer fulltext zoeken niet is ingeschakeld. De tweede groep gebruikt fulltext-only velden zoals bedrag of vervaldatum.

#### Werkt zonder fulltext

##### Operatoraliassen

- Query: `created_on gt 2026-05-25`
- Gelijk aan: `created_on>2026-05-25`
Resultaat: Filtert op Created na 25 mei 2026.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_01_operator_aliases.png" alt="Quick Search-resultaat voor created_on gt 2026-05-25"><figcaption><p><code>created_on gt 2026-05-25</code> - Filtert op Created na 25 mei 2026.</p></figcaption></figure>

##### Datumwoorden zonder haakjes

- Query: `created_on < today`
- Gelijk aan: `created_on<today()`
Resultaat: Breidt het woord today uit naar today().

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_02_bare_date.png" alt="Quick Search-resultaat voor created_on &lt; today"><figcaption><p><code>created_on &lt; today</code> - Breidt het woord today uit naar today().</p></figcaption></figure>

##### Relatieve periode

- Query: `created_on this_month`
- Gelijk aan: `created_on>=first day of this month AND created_on<=last day of this month`
Resultaat: Breidt this_month uit naar een datumbereik.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_03_period.png" alt="Quick Search-resultaat voor created_on this_month"><figcaption><p><code>created_on this_month</code> - Breidt this_month uit naar een datumbereik.</p></figcaption></figure>

##### Leeg/ingesteld-woorden

- Query: `assigned_to is empty`
- Gelijk aan: `assigned_to=""`
Resultaat: Vindt documenten zonder toegewezen gebruiker.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_04_presence.png" alt="Quick Search-resultaat voor assigned_to is empty"><figcaption><p><code>assigned_to is empty</code> - Vindt documenten zonder toegewezen gebruiker.</p></figcaption></figure>

##### Leesbare status

- Query: `status:open`
- Gelijk aan: `status=ready_for_validation`
Resultaat: Koppelt open aan de validatiestatus.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_05_status_open.png" alt="Quick Search-resultaat voor status:open"><figcaption><p><code>status:open</code> - Koppelt open aan de validatiestatus.</p></figcaption></figure>

##### Niet tussen

- Query: `created_on not between 2026-06-01, 2026-06-15`
- Gelijk aan: `(created_on<2026-06-01 OR created_on>2026-06-15)`
Resultaat: Vindt waarden buiten een datumvenster.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_06_not_between.png" alt="Quick Search-resultaat voor created_on not between 2026-06-01, 2026-06-15"><figcaption><p><code>created_on not between 2026-06-01, 2026-06-15</code> - Vindt waarden buiten een datumvenster.</p></figcaption></figure>

##### In-lijst

- Query: `status in (ready_for_validation, exported)`
- Gelijk aan: `status=ready_for_validation OR status=exported`
Resultaat: Matcht elke opgegeven status.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_07_in_list.png" alt="Quick Search-resultaat voor status in (ready_for_validation, exported)"><figcaption><p><code>status in (ready_for_validation, exported)</code> - Matcht elke opgegeven status.</p></figcaption></figure>

##### Negatieprefix

- Query: `not status=finished`
- Gelijk aan: `status!=finished`
Resultaat: Keert het finished-statuspredicaat om.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_08_negation.png" alt="Quick Search-resultaat voor not status=finished"><figcaption><p><code>not status=finished</code> - Keert het finished-statuspredicaat om.</p></figcaption></figure>

##### Tekst bevat

- Query: `filename contains E2E`
- Gelijk aan: `filename:E2E`
Resultaat: Gebruikt contains als substringzoekopdracht in bestandsnaam.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_09_contains.png" alt="Quick Search-resultaat voor filename contains E2E"><figcaption><p><code>filename contains E2E</code> - Gebruikt contains als substringzoekopdracht in bestandsnaam.</p></figcaption></figure>

##### Factuurprefix

- Query: `#INV-1234`
- Gelijk aan: `invoice_id:INV-1234`
Resultaat: Koppelt #... aan zoeken op factuur-ID.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_12_invoice_prefix.png" alt="Quick Search-resultaat voor #INV-1234"><figcaption><p><code>#INV-1234</code> - Koppelt #... aan zoeken op factuur-ID.</p></figcaption></figure>

##### Toegewezen-prefix

- Query: `@Daniel`
- Gelijk aan: `assigned_to:"Daniel"`
Resultaat: Koppelt @... aan zoeken op naam van toegewezen gebruiker.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_13_assignee_prefix.png" alt="Quick Search-resultaat voor @Daniel"><figcaption><p><code>@Daniel</code> - Koppelt @... aan zoeken op naam van toegewezen gebruiker.</p></figcaption></figure>

#### Vereist fulltext zoeken

Gebruik je dezelfde sneltoets met een fulltext-only veld, dan vereist de query nog steeds fulltext. Bijvoorbeeld: `ap_assignment_code is empty` gebruikt dezelfde leeg/ingesteld-sneltoets als `assigned_to is empty`, maar het AP-veld is fulltext-only.

##### Bedragsuffix

- Query: `total_amount > 5k`
- Gelijk aan: `total_amount>5000`
Resultaat: Breidt k uit naar duizendtallen op een bedragveld.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_10_currency_suffix.png" alt="Quick Search-resultaat voor total_amount &gt; 5k"><figcaption><p><code>total_amount &gt; 5k</code> - Breidt k uit naar duizendtallen op een bedragveld.</p></figcaption></figure>

##### Achterstallig-sneltoets

- Query: `overdue`
- Gelijk aan: `invoice_due_date<today() AND status!=finished`
Resultaat: Vindt niet-afgeronde facturen na de vervaldatum.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_11_overdue.png" alt="Quick Search-resultaat voor overdue"><figcaption><p><code>overdue</code> - Vindt niet-afgeronde facturen na de vervaldatum.</p></figcaption></figure>

##### Bedragprefix

- Query: `$5000+`
- Gelijk aan: `total_amount>=5000`
Resultaat: Koppelt $...+ aan een bedragdrempel.

<figure><img src="../../../.gitbook/assets/quick_search_shortcut_14_amount_prefix.png" alt="Quick Search-resultaat voor $5000+"><figcaption><p><code>$5000+</code> - Koppelt $...+ aan een bedragdrempel.</p></figcaption></figure>

---

## Deel 4 — Geavanceerde zoekmodi

Naast het zoeken op velden doorzoeken drie prefixen de documentinhoud zelf.

### Vector- (semantisch) zoeken — `vector:`

Matcht op **betekenis**, niet op exacte tekst. Vereist de Vector-module.

```
vector: invoices about office supplies
vector: shipping delays with Hamburg port
```

### OCR-tekst zoeken — `ocr:`

Doorzoekt de **paginatekst** die OCR heeft geëxtraheerd, niet alleen de kolommen.

```
ocr: Versandkosten
ocr: "purchase order PO-12345"
ocr: Hamburg AND doc_type=INVOICE
```

### Zoeken in natuurlijke taal (AI) — `ai:`

Beschrijf in gewone taal wat je zoekt; de AI leest je zin en haalt filters
(leverancier, datums, bedragen) eruit in een gestructureerde query.

```
ai: invoices from Ruiz over 1000 last quarter
ai: overdue invoices waiting on approval
```

---

### Recepten

| Je wilt… | Typ dit |
|----------|---------|
| Klaar om te valideren, volledig afgestemd | `status=ready_for_validation AND po_match_status=full_matched` |
| Deze leverancier, deze week | `supplier_name=Test AND created_on>today()-7` |
| Achterstallige facturen met hoog bedrag | `total_amount>5000 AND invoice_due_date<today()` |
| Twee leveranciers tegelijk | `supplier_name=fuji OR supplier_name=acme` |
| Foutdocumenten van vandaag | `(status=error OR status=failed) AND created_on>today()-1` |
| Op ordernummer-prefix | `purchase_order=PO-2026` |

> Oranje (fulltext-)velden en de slimme PO-filters vereisen dat **fulltext-zoeken**
> aanstaat.
