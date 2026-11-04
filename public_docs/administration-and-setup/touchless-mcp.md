# Touchless uitleggen en verbeteren met MCP

Deze werkwijzen gebruiken daadwerkelijk aangeboden DocBits MCP-tools. Scheid lezen/uitleg van schrijven. Controleer organisatie, rol, type, periode en peildatum; verzin geen ontbrekend bewijs.

<figure><img src="../.gitbook/assets/touchless-owned-po-price-nl.png" alt="Echte Nederlandse Dev-weergave van een fictieve order: 10 × 9 = 90. Dit is een bronvergelijking voor MCP-diagnose, geen screenshot van een MCP-client of bewijs van geslaagde extractie/verwerking."><figcaption><p>Echte Nederlandse Dev-weergave van een fictieve order: 10 × 9 = 90. Dit is een bronvergelijking voor MCP-diagnose, geen screenshot van een MCP-client of bewijs van geslaagde extractie/verwerking.</p></figcaption></figure>

## Touchless uitleggen met MCP

> Leg Pure Touchless, alleen goedkeuring en het gecombineerde AP-percentage uit voor facturen van de afgelopen 30 dagen. Toon teller, noemer, lopende documenten, uitsluitingen, filters en peildatum. Scheid extractiekwaliteit van automatisering.

Gebruik `touchless_get_summary` met `period: "30d"` en `doc_type: "INVOICE"`. Gebruik voor segmenten uitsluitend dimensies en waarden uit `touchless_list_segments`. Vergelijk dezelfde organisatie, hetzelfde type, tijdvak en segment; lees `data_as_of`.

**Echt Dev-tegenvoorbeeld:** drie nieuwe facturen waren nog `IN_PROGRESS`: `population.total: 3`, `population.in_progress: 3`, `population.eligible: 0`, `official_touchless_rate.ap_pct: null`. Er was nog geen percentage berekenbaar. Dit betekent geen extractiekwaliteit van 0 % of Touchless van 100 %. `eligible` in de samenvatting is hier de afgeronde KPI-populatie; een individuele trace kan tegelijk `eligible: true` en `bucket_final: false` tonen.

De voorbeelden gebruiken daadwerkelijk aangeboden en op Dev gecontroleerde MCP-tools. Organisatie en rechten blijven gelden. Dit bewijst geen beschikbaarheid in een andere interface of aanvullende lijst met toegestane tools.

## Afwijkingen onderzoeken met MCP

> Controleer order, import en actieve regels. Scheid extractie, oude kopie, onjuiste bron en ontbrekende configuratie. Wijzig nog niets.

1. Vergelijk origineel, `get_extracted_fields` en `get_extracted_tables` voordat u correcte extractie claimt.
2. Gebruik `get_po_sync_status`, bijvoorbeeld `po_number: "TL20261104X1-PO02"`, `language: "en"`. Dit overzicht ondersteunt `de` en `en`; leg de uitkomst in het Nederlands uit. Een verwerkte import bewijst geen inhoudelijke juistheid of actuele Infor-status.
3. Gebruik `touchless_get_document_trace` en `touchless_explain_po_match` met hetzelfde `doc_id`. Controleer echte engine, actieve versie, kolommen en toleranties. Gebruik een teruggegeven `issue_signature` voor `touchless_get_po_match_evidence`.
4. Het testtype gaf `state: "none_published"`, `parse_error: "no published rule set"` en lege velden. Noch prijs-/aantalblokkade, noch geslaagde matching was bewezen. Een algemeen schema vervangt die controles niet.
5. Herstel de bevestigde oorzaak en controleer nieuwe facturen. Menselijke correctie/herstart blijft na succes geregistreerd; een definitieve ERP-fout heeft voorrang. Lopende documenten vallen buiten de noemer.

Een volledig geval vereist origineel, extractie vóór correctie, bronwaarden met datum, werkelijk gebruikte regels, AP-actie en eindresultaat. Ontbrekend bewijs blijft open.

## Bewijs lezen met MCP

> Onderzoek deze factuur zonder wijzigingen. Vergelijk origineel, huidige velden en tabellen. Verklaar de vastgelegde uitvoeringen en benoem ontbrekende historische gegevens.

| Tool met hetzelfde `doc_id` | Bewijs en beperking |
| --- | --- |
| `get_extracted_fields` | Huidige waarden en betrouwbaarheid; geen historische momentopname |
| `get_extracted_tables` | Aanwezige tabellen en regels; geen bewijs van overeenstemming met het origineel |
| `touchless_get_document_trace` | Vastgelegde resultaten, ingrepen, stappen en uitvoeringen |
| `touchless_explain_pipeline` | Verklaart het bewezen traject; vult ontbrekend bewijs niet aan |

**Werkelijke negatieve controle:** `header_extraction: passed`, maar `extracted_field_count: 0`, acht verplichte velden leeg en geen tabel. Validatie blokkeerde met `REQUIRED_FIELD_MISSING`. Controleer extractie/configuratie; een groene stap bewijst geen correcte extractie of blokkade door een orderprijs.

### Is een MCP-actie een menselijke ingreep?

Lezen verandert de factuur niet. Andere tools kunnen schrijven, valideren of herstarten. Een API-sleutel kan een systeemaccount vertegenwoordigen; “via MCP” bewijst geen menselijke ingreep of Pure Touchless. Verberg menselijk herstelwerk niet via systeemaccounts.

Controleer `human_touched`, `human_touch_source`, `human_restart_count`, `business_approval_touched`, eindstatus en uitvoeringen. Alleen goedkeuring verschilt van een opgeslagen correctie, handmatige validatie of menselijke herstart.

## Leveranciers prioriteren en verbeteringen controleren met MCP

> Rangschik leveranciers naar verloren Touchless-documenten. Scheid extractiefouten, afwijkende brongegevens en procesinstellingen. Geef per bevestigde oorzaak een actie en controle, zonder iets te wijzigen.

1. Gebruik `touchless_rank_supplier_opportunities` met `period: "30d"`, `doc_type: "INVOICE"`, `order_by_field: "lost_docs"`, `order_by_direction: "desc"`. `search` zoekt naam/nummer; `limit` en `offset` regelen paginering.
2. Gebruik de teruggegeven `supplier_key` in `touchless_diagnose_supplier`; `window: 30` toont de huidige situatie, 90 helpt herhaling te onderzoeken.
3. Geef een werkelijk ontvangen `issue_signature` aan `touchless_get_issue_cluster`. Controleer documenten en ontbrekend bewijs voordat u een oorzaak bevestigt.
4. Lees ondersteunde maatregelen met `touchless_get_recommendations`. Verwachte winst is een schatting; overlappende clusters mogen niet worden opgeteld.
5. Controleer nieuwe vergelijkbare facturen en de meting na de wijziging. Een al handmatig verwerkte factuur wordt niet achteraf Pure.

Correcte extractie met oude orders vraagt bron-/importherstel. Een verschil tussen origineel en extractie vraagt controle van de extractieconfiguratie. Alleen goedkeuring blijft na succes AP Touchless. Een lege ranglijst bewijst geen probleemloze verwerking: de drie lopende testfacturen hadden nog geen afgeronde leveranciersresultaten. Controleer filters, peildatum, leveranciersherkenning en afgerond volume.

## Voorbeeld, toepassing en effectmeting met MCP

> Verklaar de bevestigde oorzaak en toon ondersteunde voorstellen. Bekijk het gekozen voorstel en de risico’s vooraf. Pas uitsluitend die wijziging toe en controleer opgeslagen waarde, historie en meetbaar effect.

| Stap | Tool en werkelijk ontvangen ID’s | Resultaat |
| --- | --- | --- |
| Lijst | `touchless_list_change_proposals`, eventueel `issue_signature`, `window: "30d"`, `lang: "nl"` | Bestaande voorstellen; schrijft geen instelling |
| Voorbeeld | `touchless_preview_change` met ontvangen `proposal_id` en `issue_signature` | Concrete reikwijdte en, indien toegestaan, gebonden `preview_token` |
| Gekozen wijziging toepassen | `touchless_apply_change` met dezelfde ID’s, token, `overrides` en `window` | **Schrijft** de ondersteunde instelling; succes geeft `change_id` |
| Effect lezen | `touchless_verify_change` met dat `change_id` en hetzelfde `window` | Voor/na; minimaal 20 afgeronde geschikte documenten per tijdvak nodig |

Verzin geen ID’s of tokens. Een voorbeeld van de ene waarde rechtvaardigt geen toepassing van een andere. Verlopen, verboden of onvolledige voorbeelden bewijzen geen toepassing. De tabel beschrijft de werkwijze; voor de demonstratie is geen toegepast voorstel of gemeten winst aangetoond.

Controleer na bevestigd configuratieherstel de instelling en nieuwe facturen. Van 52 naar 61 % is 9 waargenomen procentpunten, geen bewijs van één oorzaak. Een foutieve Infor-order vraagt inhoudelijke correctie en gecontroleerde import: `touchless_apply_change` schrijft niet willekeurig naar Infor. Verruim geen toleranties om onjuiste gegevens te verbergen.

Een rapport bevat schattingen, geen bewijs van toepassing of terugdraaien. Toepassing vereist een succesantwoord en historie. Terugdraaien is alleen mogelijk als het voorstel dat ondersteunt; controleer de herstelde waarde. Historie vernieuwen past niets toe; terugdraaien wist eerdere menselijke ingrepen niet.

## Gerelateerde pagina’s

* [Touchless Intelligence](touchless-intelligence.md)
* [Metrieken en berekening](touchless-metrics.md)
* [Het dashboard gebruiken](touchless-dashboard.md)
* [Voorbeelden: prijs en aantal](touchless-examples.md)
* [Touchless Intelligence: Leveranciersdiagnose en probleemclusters](touchless-supplier-diagnosis.md)
* [Touchless Intelligence: PO-matchingdiagnose](touchless-po-matching-diagnosis.md)
* [Touchless Intelligence: Documentspoor](touchless-document-trace.md)
* [Touchless Intelligence: Wijzigingsvoorstellen en rapporten](touchless-change-proposals.md)

<!-- Source notes (not shown): screenshots come from the dev test organisation with synthetic demo data (seed script) and fictional supplier names; the PO matching decision flow has no screenshot yet. facts read from the doc2app code (TouchlessIntelligence pages and components) and the dev UI on 14 Oct 2026; NOVA gates the tab with its own organisation flag, VESTA with the Analytics module. Consulting report export format not verified, so no export is described.

<!-- Alignment 2026-11-04: correct extraction is distinct from process Touchless; KPI numerator and denominator verified. -->
<!-- Completion 2026-11-04: localized MCP examples, AP actions, original-value evidence and owned synthetic PO cards. -->
