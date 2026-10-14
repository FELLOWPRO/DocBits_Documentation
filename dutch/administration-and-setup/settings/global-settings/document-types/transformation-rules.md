# Transformatie Regels

## Overzicht

Transformatie regels maken geëxtraheerde data **automatisch** schoon of herschrijven deze — een veld in de header, een kolom in een tabel, hele tabelrijen, of een attribuut van het document — elke keer dat een document wordt verwerkt en elke keer dat het wordt opgeslagen. Ze vervangen de kleine scripts die veel organisaties vroeger schreven voor "altijd dit veld trimmen", "standaard deze kolom op 1 zetten", "de eenheidscodes van deze leverancier mappen" of "de regelitems van deze leverancier samenvoegen tot één totaallijn".

Een regel wordt per **documenttype** gedefinieerd en draait bij elk document van dat type. Regels draaien **voor** validatie, scripts en inkooporder-matching, zodat alles stroomafwaarts al de getransformeerde waarden ziet.

## Hoe te openen

1. Navigeer naar **Instellingen → Globale Instellingen → Documenttypen**.
2. Open het documenttype en kies **Transformatie Regels**. De lijst toont elke regel van het type met de scope, doel, prioriteit en of deze actief is.
3. Klik op **Nieuwe regel** om de regelbouwer te openen, of open een bestaande regel om deze te wijzigen.

## Anatomie van een regel

| Deel                 | Wat het is                                                                                                                                                                                                                                         |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Naam / sleutel**   | De weergavenaam die getoond wordt in lijsten, berichten en de matchgeschiedenis, en een technische sleutel die stabiel blijft bij het hernoemen van de regel.                                                                                      |
| **Scope**            | Waar de regel schrijft: een **header veld**, een **tabelkolom**, een **tabel** (hele rijen) of een **documentattribuut**. Zie hieronder.                                                                                                           |
| **Doel**             | Het veld, de kolom (met de tabel) of tabel waar de regel naar schrijft.                                                                                                                                                                            |
| **Bron**             | Optioneel. Waar de regel zijn invoer vandaan haalt in plaats van het doel zelf: `header.<veld>` voor een header veld, `doc.<attribuut>` voor een documentattribuut, `row.<kolom>` voor een andere kolom van dezelfde rij (alleen kolom scope).     |
| **Wanneer**          | **Altijd**, of **alleen wanneer** een voorwaarde waar is (zie Voorwaarden).                                                                                                                                                                        |
| **Acties**           | De lijst van transformaties, toegepast in volgorde; de output van de ene actie is de input van de volgende.                                                                                                                                        |
| **Prioriteit**       | Regels met dezelfde scope draaien in oplopende prioriteit (daarna op sleutel). Gebruik dit wanneer een regel het resultaat van een andere moet zien.                                                                                               |
| **Eén keer draaien** | De regel wordt op een document **hooguit één keer** toegepast. Nodig voor acties die de waarde bij elke save opnieuw zouden veranderen (substring, regex\_replace, regex\_extract) en voor tabelregels die de regels niet opnieuw moeten opbouwen. |
| **Log uitvoering**   | Schrijft één logregel per toepassing — handig tijdens het afstellen van een nieuwe regel.                                                                                                                                                          |

### Scopes

| Scope                 | Schrijft naar                                                     | Typische regel                                                                              |
| --------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| **Header veld**       | één geëxtraheerd header veld (factuurnummer, valuta, …)           | trimmen en hoofdletters van het factuurnummer; "EUR€" mappen naar "EUR"                     |
| **Tabelkolom**        | één kolom in elke rij van een tabel                               | standaard `UNIT_PRICE_PER` op 1 zetten; prefix "Art.-Nr." verwijderen uit het artikelnummer |
| **Tabel**             | de rijen van een tabel                                            | regels wissen en één totaallijn toevoegen voor een leverancier die op totaal wordt gematcht |
| **Documentattribuut** | een attribuut van het document zelf (momenteel de suborganisatie) | documenten van een leverancier routeren naar een suborganisatie                             |

Regels draaien scope voor scope in deze volgorde: header → document → tabel → kolom. Een kolomregel ziet dus al rijen die een tabelregel heeft toegevoegd.

### Voorwaarden ("alleen wanneer")

Een voorwaarde vergelijkt een waarde van het document met een constante. De waarde komt uit een header veld (`header.<veld>`), een documentattribuut (`doc.<attribuut>`) of, voor kolomregels, een kolom van de huidige rij (`row.<kolom>`).

| Operator                                         | Betekenis              |
| ------------------------------------------------ | ---------------------- |
| is / is niet                                     | exacte vergelijking    |
| is een van / is geen van                         | waarde in een lijst    |
| bevat, begint met, eindigt met                   | tekstvergelijking      |
| is leeg / is niet leeg                           | geen waarde nodig      |
| groter dan, kleiner dan, ten minste, ten hoogste | numerieke vergelijking |
| komt overeen                                     | reguliere expressie    |

Voorwaarden kunnen gegroepeerd worden met **alle van** (en) en **een van** (of) en genegeerd met **niet**. Voorbeeld: _alleen wanneer `header.supplier_id`_ _`20723` is_ — de regel draait alleen voor één leverancier.

### Acties

Acties voor header velden en tabelkolommen (ze vormen een pijplijn; de waarde gaat bovenin erin en komt onderin eruit):

| Actie           | Effect                                                                                                          |
| --------------- | --------------------------------------------------------------------------------------------------------------- |
| `trim`          | verwijder witruimte (of opgegeven tekens) links, rechts of aan beide zijden                                     |
| `case`          | hoofdletters, kleine letters, titel of kapitaliseren                                                            |
| `pad`           | opvullen tot een lengte met een teken, links of rechts                                                          |
| `truncate`      | afkappen tot een maximale lengte                                                                                |
| `affix`         | voeg een prefix of suffix toe, of verwijder er één                                                              |
| `sanitize`      | behoud alleen een tekenklasse (alfanumeriek, alfa, numeriek, alfanumeriek + spatie) of verwijder een set tekens |
| `substring`     | neem een deel van de waarde op basis van start en lengte of einde                                               |
| `regex_replace` | vervang wat een reguliere expressie matcht                                                                      |
| `regex_extract` | behoud wat een reguliere expressie vastlegt                                                                     |
| `value_map`     | map waarden naar andere waarden (optioneel hoofdletterongevoelig, met een standaardwaarde)                      |
| `date_format`   | herformatteer een datum (de invoer moet de ISO datum zijn die DocBits opslaat in `value`)                       |
| `number_format` | herformatteer een nummer                                                                                        |
| `default`       | stel een waarde in alleen wanneer het veld leeg is                                                              |
| `set_value`     | stel een vaste waarde in, ongeacht wat het veld bevatte                                                         |
| `clear`         | maak het veld leeg                                                                                              |

Acties voor **tabel** scope (ze werken op rijen, niet op waarden, en kunnen niet gemengd worden met bovenstaande acties):

| Actie        | Effect                                                                                                                                                                |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clear_rows` | verwijder elke rij van de tabel                                                                                                                                       |
| `add_row`    | voeg één rij toe aan het einde of begin; elke kolom krijgt een vaste waarde of een waarde gelezen uit de header (`header.<veld>`) of het document (`doc.<attribuut>`) |

{% hint style="info" %}
`substring`, `regex_replace` en `regex_extract` veranderen een waarde opnieuw wanneer ze draaien op een al getransformeerde waarde. Combineer ze met **Eén keer draaien**, of schrijf de reguliere expressie zo dat een tweede keer niets meer te veranderen valt.
{% endhint %}

## Wanneer regels draaien

* Tijdens verwerking, na extractie en voor validatie, scripts en inkooporder-matching.
* Bij **elke keer opslaan** van het document waarin de geëxtraheerde data veranderde. Regels zonder **Eén keer draaien** worden bij elke save opnieuw toegepast; omdat elke actie behalve de drie hierboven idempotent is, blijft een waarde die al in de doelvorm is hetzelfde.

## Transformatie regels en inkooporder-matching

Tabelregels en kolomregels veranderen wat de PO matcher ziet:

* Een tabelregel die regels **herbouwt** (bijvoorbeeld alle rijen wissen en één totaallijn toevoegen) behoudt een bestaande inkoopordermatch zolang deze **dezelfde regels opnieuw** produceert — waarden worden vergeleken op betekenis, dus `1.0` en `1.00` zijn dezelfde regel. De regels behouden hun identiteit en de match overleeft elke save.
* Als een regel regels **vervangt of verwijdert die gematcht waren**, kan de match niet worden behouden. Het document registreert dan welke regel dit deed, het Purchase Order Matching scherm toont dit als reden ("_De PO match kon niet worden opgeslagen: de transformatie regel "…" heeft de tabel herbouwd_") en beheerders krijgen een link naar de regel. De **matchgeschiedenis** van het document toont een _Transformatie regels_ stap vóór de eerste matching fase met de regels die draaiden.
* Het aantal regels na de regels is wat de [activatievoorwaarden](https://github.com/Fellow-Consulting-AG/docbits/tree/nl/readme/administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) van de matching regels tellen. Een regel die een factuur samenvouwt tot **één** regel heeft alleen zin samen met een match-op-totaal regel die actief is voor één-regel documenten (`[[count(table_lines)]] >= 1`).

## Voorbeelden

**Maak het factuurnummer schoon** — header veld `invoice_id`, altijd: `trim` → `case` upper.

**Standaard de prijsbasis** — tabelkolom `UNIT_PRICE_PER` van de regel-item tabel, altijd: `default` `1`.

**Map een leverancier zijn eenheidscodes** — tabelkolom `UNIT` van de regel-item tabel, alleen wanneer `header.supplier_id` `10040` is: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Één totaallijn voor een leverancier die op totaal wordt gematcht** — tabel scope op de regel-item tabel, alleen wanneer `header.supplier_id` `20723` is: `clear_rows`, daarna `add_row` met `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Combineer met een match-op-totaal regel waarvan de activatievoorwaarde één documentregel accepteert.

**Routeer een leverancier naar een suborganisatie** — documentattribuut `sub_org_id`, alleen wanneer `header.supplier_id` één van `[…]` is: `set_value` `<sub-organisatie id>`.

## Problemen oplossen

| Symbool                                             | Wat te controleren                                                                                                                                                                                      |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| De regel veranderde niets                           | Is deze actief? Komt het documenttype overeen? Is de voorwaarde waar voor dit document (vergelijk de exacte waarde, inclusief spaties)? Is een **Eén keer draaien** regel al toegepast op het document? |
| De waarde verandert bij elke save opnieuw           | De pijplijn bevat `substring`, `regex_replace` of `regex_extract`. Zet **Eén keer draaien** aan of maak de expressie idempotent.                                                                        |
| De inkoopordermatch gaat verloren na opslaan        | Een tabelregel verving de gematchte regels. De reden op het document noemt de regel; zorg dat de regel dezelfde regels reproduceert, of zet deze op **Eén keer draaien**.                               |
| Een matching regel draait nooit na de transformatie | De regel veranderde het aantal regels; pas de activatievoorwaarde van de matching regel aan.                                                                                                            |
