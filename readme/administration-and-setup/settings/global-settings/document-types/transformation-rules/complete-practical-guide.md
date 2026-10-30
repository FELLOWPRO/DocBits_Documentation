# Transformatieregels: volledig praktisch overzicht

> Bekende beperking van het voorbeeld (gecontroleerd op 29 oktober 2026, versie 11.15.2): bij het toevoegen van het voorvoegsel `INV-` verandert het voorbeeld `INV-4711` ten onrechte in `INV-INV-4711`. De afzonderlijk gecontroleerde servertest behoudt `INV-4711`. Controleer herhaalde uitvoering daarom ook met een servertest; een correct voorbeeldresultaat bewijst op zichzelf niet de volledige uitvoering bij het opslaan.

Stand van de controle: 28 oktober 2026. De voorbeelden zijn gecontroleerd met synthetische trainingswaarden op Dev NOVA. Een voorbeeld is geen bewijs van een opgeslagen documentwijziging, een bestellingsafstemming of een ERP-export.


## Zichtbare labels in de editor

Sommige labels in de huidige interface zijn onnauwkeurig vertaald. De tabel vermeldt de werkelijk weergegeven tekst om de juiste stap te vinden; de uitleg gebruikt de technische betekenis. De schermafbeeldingen tonen de ongewijzigde interface.

| Bewerking | Zichtbaar label |
| --- | --- |
| case | Hoofdletters/kleine letters |
| trim | Trim |
| pad | Pad |
| truncate | Inkorten |
| affix | Voor-/achtervoegsel |
| sanitize | Opschonen |
| substring | Neem een plakje |
| regex_extract | Extract |
| regex_replace | Zoeken en vervangen |
| value_map | Waarden koppelen |
| date_format | Datum opnieuw formatteren |
| number_format | Formaatnummer |
| fix_value | Vaste waarde |
| clear | Wissen |
| clear_rows | Wis alle rijen |
| add_row | Rij toevoegen |


## Vier geldigheidsbereiken

| Bereik | Invoer en doel | Typische taak |
| --- | --- | --- |
| Kopveld | Eén veld per document; bron kan een ander kopveld zijn | Factuurnummer opschonen, bestelnummer overnemen |
| Tabelkolom | De gekozen kolom per rij van de gekozen tabel | Artikelnummers of eenheidscodes uniformeren |
| Tabelrijen | Hele tabel | Rijen verwijderen of gedefinieerde posities toevoegen |
| Routing | Documentattribuut `sub_org_id` | Bestaande suborganisatie toewijzen |

De bereiken lopen **Kopveld → Routing → Tabelrijen → Tabelkolom**. Binnen een bereik bepalen prioriteit en regelsleutel de volgorde. De stappen van een regel lopen van boven naar beneden. Een latere regel kan daarom reeds gewijzigde waarden lezen. De volgorde van de bereiken wordt niet door de prioriteit van een enkele regel omgekeerd.

## Alle stappen van de editor

De gecontroleerde editor biedt 14 waardestappen voor kop/kolom, twee stappen voor hele tabellen en een vaste toewijzing in de routing. `fix_value` en de vaste routingtoewijzing gebruiken serverzijdig beide `set_value`. Daarnaast kent de interface `default`; deze stap wordt in het gecontroleerde normale stapmenu niet aangeboden.

| Stap | Varianten en parameters | Voorbeeld | Grens en tegenproef |
| --- | --- | --- | --- |
| Hoofd-/kleine letters wijzigen (`case`) | upper, lower, title, capitalize | `inv-4711` → `INV-4711` | Title: `acme gmbh` → `Acme Gmbh`; capitalize: `aCME GMBH` → `Acme gmbh`. Eigen namen/afkortingen kunnen zich vaktechnisch ongewenst wijzigen. Bij `capitalize` laat de gecontroleerde browservoorbeeld de rest ongewijzigd, terwijl de server deze klein schrijft; serverwaarde afzonderlijk controleren. |
| Trimmen (`trim`) | beide / links / rechts; teken leeg = witruimte | `  4711  ` → `4711` | `47 11` blijft behouden. Links teken `0`: `004711` → `4711`, maar `000` → leeg. Tekens zijn een verzameling, geen volledige prefixtekst. |
| Aanvullen (`pad`) | minimumlengte, één vul teken, links/rechts | Lengte 10, links `0`: `4711` → `0000004711` | Reeds 11 tekens blijven 11 tekens. Rechts `_`, lengte 6: `ABC` → `ABC___`. |
| Inkorten (`truncate`) | maximale lengte | Lengte 10: `ABCDEFGHIJKL` → `ABCDEFGHIJ` | `ABC` blijft `ABC`. Afsnijden verliest informatie en kan nummers samen laten vallen. |
| Affix (`affix`) | prefix/suffix toevoegen/verwijderen | `INV-` + `4711` → `INV-4711` | Bestaand exact affix wordt niet dubbel toegevoegd. Verwijderen werkt alleen aan de passende zijde en let op hoofdletters. |
| Tekens opschonen (`sanitize`) | alfanumerisch / letters / cijfers / alfanumerisch + spatie behouden; alternatief tekenklasse verwijderen | `DE 123.456.789` → `DE123456789` | Tekens kunnen betekenisdragend zijn. Bij verwijderen is de invoer een regex-tekenklasse; koppelteken correct beschermen, bijv. `.\-/`. |
| Deelstuk (`substring`) | start + lengte **of** start + einde; negatieve indices mogelijk | Start 3, einde 7: `DE-4711-X` → `4711` | Start telt vanaf 0, einde is exclusief. Start −4: laatste vier tekens. Gescheiden oorspronkelijke bron vereist. |
| Extraheren (`regex_extract`) | reguliere expressie, vangstgroep | `PO[- ]?(\d+)`, groep 1: `Order PO-45001234` → `45001234` | Eerste treffer; groep 0 = volledige treffer. Zonder treffer: leeg. Gescheiden bron vereist. |
| Zoeken en vervangen (`regex_replace`) | patroon, vervanging, aantal | `\s+` → spatie: `ACME    GmbH` → `ACME GmbH` | Aantal 0 = alle, 1 = eerste treffer. Gescheiden bron vereist. Browser-/server-regex bij complexe patronen afzonderlijk controleren. |
| Waarden toewijzen (`value_map`) | volledige van→naar-paren; hoofdletters negeren; vervanging zonder treffer | `stk` → `PCE` met `STK→PCE` en genegeerde hoofdletters | Lege vervanging betekent **invoer behouden**. `BOX` blijft `BOX`; een vaste vervanging `C62` zou `BOX` overschrijven. Trimmen geschiedt niet automatisch. |
| Datum formatteren (`date_format`) | uitvoerpatroon, bijv. `%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y` | `2026-10-28` → `28.10.2026` in tekstdoel | Bij DATE-kopvelden kan de opgeslagen waarde ISO blijven en alleen de weergave wisselen. Onleesbare tekst blijft ongewijzigd; de servertest noemt de reden. |
| Getal formatteren (`number_format`) | de_DE / en_US / en_GB / fr_FR; min./max. decimalen | `1234.5` → `1234,50` respectievelijk `1234.50` in het gecontroleerde serverresultaat | Geen duizendtalscheidingsteken in het gecontroleerde serverresultaat. Geen valuta- of hoeveelheidsconversie. Afronding en herverwerking afzonderlijk controleren. |
| Vaste waarde (`fix_value` in de editor, `set_value` in de API) | één vaste waarde | `USD` → `EUR` | Overschrijft ook bestaande waarden. Niet verwarren met een standaardwaarde. |
| Leegmaken (`clear`) | geen parameters | `Altwert` → `""` | Maakt de waarde leeg; verwijdert noch velddefinitie noch document. |
| Alle rijen verwijderen (`clear_rows`) | alleen tabelrijen | 2 posities → 0 | Kan rijverwijzingen en bestaande PO-afstemming ongeldig maken. |
| Rij toevoegen (`add_row`) | begin/einde; per kolom vaste waarde of kopbron | Hoeveelheid `1`, nettobedrag uit `header.total_net_amount` | Zonder voorafgaand verwijderen alleen met geschikte eenmalige uitvoering. Geen automatische aggregatie van bestaande posities. |
| Vaste suborganisatie (`set_value`, routing) | bestaand doel uit de suborganisatiekiezer | Leverancier A → suborganisatie Noord | Geen willekeurig status-/gebruiker-/autorisatieattribuut. Alternatief toewijzing via `value_map` en bron. |

### Standaardwaarde via de interface

`default` vult zijn waarde alleen aan bij ontbrekende/lege invoer. Met standaard `1` geven `null` en `""` de waarde `1`; `0` blijft `0`, `100` blijft `100`. Dit is serverzijdig gecontroleerd. De normale editor heeft daarvoor in de gecontroleerde stand geen eigen stap. Het vaktechnisch overeenkomstige eenvoudige geval is vaak met **Doel is leeg → Vaste waarde** af te beelden. Dit is een regelvoorwaarde met toewijzing, geen verborgen menuoptie.

## Negen uitgebreide praktijkreeksen

- [01 · Basisbeginselen, geldigheidsbereiken en veilige tests](01-foundations.md)
- [02 · Tekst opschonen: schrijfwijze, trimmen en tekens](02-text-cleaning.md)
- [03 · Nummers vormen: aanvullen, inkorten, prefix en suffix](03-numbers-and-affixes.md)
- [04 · Deelstukken en patronen: knippen, extraheren, vervangen](04-substrings-and-patterns.md)
- [05 · Waardetoewijzingen en regels per tabelrij](05-value-mapping.md)
- [06 · Datum en getallen correct formatteren](06-dates-and-numbers.md)
- [07 · Velden overnemen, vaste waarden, leegmaken en standaardwaarden](07-field-copy-and-defaults.md)
- [08 · Tabelrijen opnieuw opbouwen](08-table-rows.md)
- [09 · Routing, volgorde, stamgegevens en herhalingen](09-routing-and-execution.md)

| Reeks | Inhoud | Concreet controlepunt |
| --- | --- | --- |
| 01 Basisbeginselen | Doel, bron, vier bereiken, pipeline, voorwaarden, voorbeeld, opslag | Passend geval, tegenvoorbeeld, opgeslagen regel opnieuw openen |
| 02 Tekstopschoning | Alle vier schrijfwijzen, trimmen, alle opschoonmodi | Interne spaties, pure nulreeks, betekenisdragende tekens |
| 03 Nummers | Aanvullen, inkorten, alle vier affix-varianten | Te lang nummer, reeds aanwezige prefix, dubbele prefixes |
| 04 Patronen | Deelstuk, negatieve indices, extractie/groepen, vervangen/aantal | Gescheiden bron, geen treffer, meerdere treffers |
| 05 Toewijzing | Paren, hoofdletters, vervanging, toepassing per rij | `STK→PCE`, onbekend `BOX`, herhaalde toepassing op `PCE` |
| 06 Formaten | Datum, DATE vs. tekst, onleesbare datum, getalformaten | Werkelijke serverwaarde in plaats van veronderstelde browserweergave |
| 07 Veldovername | Andere bron, leeg doel, vaste waarde, leegmaken, API-standaardwaarde | Bestaand correct bestelnummer beschermen; nul blijft nul |
| 08 Tabellen | Verwijderen, toevoegen, statische en dynamische kolomwaarden | Volgorde, herhaling, rijenaantal en PO-verwijzingen |
| 09 Samenspel | Routing, fasen, lookup, eenmalige uitvoering, logboeken | Opgeschoonde kopbron, overgeslagen voorwaarde, tweede keer opslaan |

## Voorwaarden en bronnen

Met "Altijd" geldt de regel zonder vaktechnische beperking voor het documenttype. "Alleen als…" beperkt deze door voorwaarden. Kopwaarden staan in de context `header.*`, documentkenmerken in `doc.*`; `row.*` staat alleen in de rijcontext van een kolomregel ter beschikking. Geneste en/of-groepen staan gecombineerde criteria toe. Voor de afzonderlijke operatoren geldt de afzonderlijke documentatie van de regelvoorwaarden.

**Voorbeeld veldovername:** Doel `purchase_order`, bron `header.invoice_id`, voorwaarde `header.purchase_order` is leeg, stappen Trimmen → Hoofdletters. `  po-4711  ` geeft `PO-4711`. Een reeds correct gevuld bestelnummer moet ongewijzigd blijven. Niet de verkeerde bron leegmaken: kopiëren met verwerking verplaatst de bron niet.

**Voorbeeld artikelnummer:** Tabel `INVOICE_TABLE`, kolom `ITEM_NUMBER`, prefix `Art.-Nr. ` verwijderen → alfanumerisch behouden → hoofdletters. `Art.-Nr. ab-12/3` geeft `AB123`. Alleen geschikt als het doelsysteem precies deze vorm verwacht.

**Voorbeeld totaalrij:** Voor een duidelijk afgebakende leverancier eerst `clear_rows`, dan `add_row`; `POSITION=001`, `QUANTITY=1`, `NET_AMOUNT` uit het nettobedrag van de kop. Of een bestellingsafstemming op het totaalbedrag vaktechnisch correct is, wordt door de aanvullende PO-configuratie en een afzonderlijke afstemmingstest bepaald.

## Herhaling en eenmalige uitvoering

Regels kunnen in meerdere verwerkingsdoorlopen en bij het opslaan opnieuw lopen. Controleer altijd **de hele pipeline**, niet alleen de stabiliteit van een enkele stap.

* `substring`, `regex_extract` en `regex_replace` mogen in de gecontroleerde serverovereenkomst niet hun eigen doelwaarde lezen. Een gescheiden bron is vereist; `run_once` heft deze voorschrift niet op.
* Aanvullen van een reeds aanwezig exact affix is stabiel. Verwijderen van een meermaals aanwezige prefix kan daarentegen bij elke doorloop verder verwijderen.
* `A→B` en `B→C` in dezelfde waardetoewijzing kunnen bij twee doorlopen uit `A` uiteindelijk `C` maken. Test uitvoer opnieuw als invoer.
* `clear_rows → add_row` bouwt een tabel beperkt opnieuw op. `add_row` zonder voorafgaand verwijderen vereist een geschikte eenmalige uitvoering, anders groeit de tabel bij elke keer opslaan.
* "Alleen eenmaal per document" markeert een werkelijk toegepaste regel. Niet vervulde voorwaarden verbruiken de toepassing niet. Zonder betrouwbaar leesbaar document-/toepassingsbewijs wordt de uitvoering van een eenmalige regel uitgesteld.

## Na de lookup en voor de bestellingsafstemming

"Ook na de stamgegevenszoekactie uitvoeren" voegt een fase toe na de lookup-vulling en voor de PO-afstemming. Alleen overeenkomstig gemarkeerde regels lopen in deze aanvullende fase. De overige doorlopen blijven bestaan. Gecombineerd met eenmalige uitvoering wacht de regel bij de eerste extractiedoorloop op de latere fase; valt de lookup-fase uit, dan komt een latere reguliere doorloop in aanmerking. De fasenweergave van de huidige editor toont deze verschillen.

## Een belastbaar acceptatietest

1. Vaktechnisch doel, doelsysteemformaat en geldigheidsbereik vastleggen.
2. Een passende ruwe waarde, een tegenvoorbeeld, een lege waarde en een reeds verwerkt resultaat voorbereiden.
3. Voorwaarden en alle tussenwaarden in de voorbeeldweergave controleren.
4. Serverzijdige test tegen hetzelfde voorbeeld uitvoeren; complexe patronen en getal-/datumformaten bijzonder vergelijken.
5. Regel opslaan en opnieuw openen. Een actieve regel alleen in het voorziene testbereik inzetten.
6. Bij een geïsoleerd document opslaan, nieuw laden en waarde en weergave controleren; bij tabellen ook rijenaantal en kolomwaarden.
7. Nogmaals opslaan. Het resultaat mag niet ongewenst verder wijzigen of verveelvuldigen.
8. Indien vaktechnisch vereist, PO-afstemming en werkelijke ontvangst in het doelsysteem aanvullend controleren. Een transformatielogboek alleen bewijst deze resultaten niet.

## Wat een transformatie niet automatisch verwerkt

Geen nieuwe OCR-herkenning, geen wiskundige eenheids- of valutaconversie, geen willekeurige tabelaggregatie en geen volledige ERP-boeking. Routing is beperkt tot het aangeboden documentattribuut. Beschikbaarheid en exacte weergave hangen af van de ingezette versie, het documenttype en de organisatieconfiguratie.

## Doorlopend oefenbewijs

{% file src="../../../../../.gitbook/assets/transformation-training-invoice-nl-20261028.pdf" %}
Trainingsfactuur downloaden
{% endfile %}

Het fictieve bewijs bevat twee posities, verschillende schrijfwijzen van de eenheid en een bestelverwijzing in de vrije tekst. Voor reproduceerbare regeltests worden de uitgangswaarden doelgericht voorbereid; dit is geen bewijs van een automatisch foutloze OCR-extractie.
