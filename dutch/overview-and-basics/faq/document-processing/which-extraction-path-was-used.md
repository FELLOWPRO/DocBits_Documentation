# Welk extractiepad is gebruikt?

"Waarom ziet deze tabel er zo uit?" beantwoordt u door uit te zoeken *wat* DocBits voor dit document heeft gedaan: opgeslagen regels, de AI-tabel, welke AI-tier, en waar het misging. Deze pagina is de checklist die support en partners doorlopen voordat ze een configuratie wijzigen.

## 1. Bekijk de tabbladen op het validatiescherm

Open het document en kijk naar de tabbladen boven de regelitemtabel:

| Wat u ziet | Pad |
|---|---|
| Rijen in het tabblad **Geëxtraheerde tabel** | Regelgebaseerd pad. De leverancier heeft een getrainde tabel; de rijen komen uit de opgeslagen coördinaatregels en de AI was er niet bij betrokken (behalve voor kolommen met *AI gebruiken*). |
| Rijen in het tabblad **AI Geëxtraheerde tabel**, veld *Tags* eronder | AI-pad. Geen opgeslagen regels kwamen overeen; de AI-tabelextractie heeft de rijen geproduceerd, met de AI-tier van de organisatie of de tier die voor deze leverancier is ingesteld onder *Meer instellingen* → *Leverancierspecifiek AI-model*. |
| Tooltip *AI table not found* op het AI-tabblad | Het AI-pad is uitgevoerd en heeft voor dit document niets teruggegeven. |
| Helemaal geen tabeltabbladen | Beide tabelinstellingen zijn voor de organisatie uitgeschakeld; niets heeft de tabel geëxtraheerd. |
| *No line items yet* | Het pad is uitgevoerd, maar heeft geen rijen gevonden (geen leesbare tekst, geen tabel op de pagina, of de regels kwamen niet overeen met deze lay-out). |

Koptekstvelden hebben hun eigen bronlabel naast de waarde: *Extracted using AI*, *Learned from validated AI extraction*, *Extracted using saved rules (FELLOW_KV2)*, *Extracted from electronic document*, *Calculated from vendor master data*. Deze labels beschrijven het koptekstveld, niet de tabel.

## 2. Controleer de configuratie van de leverancier

* **Instellingen → Documentverwerking → Classificatie en extractie → AI-model**: de tabel onder de keuzelijst toont elke leverancier met een opgeslagen model of training. Een leverancier in deze lijst met *trainingsgegevens* heeft opgeslagen regels; *trainingsgegevens resetten* verwijdert ze.
* **Instellingen → Documentverwerking → OCR-instellingen**: *Gebruik E-Text indien beschikbaar* en *Gebruik AI-gegevens voor tabellen* bepalen welke tekst de extractie te zien krijgt. Een leverancier kan E-Text overschrijven onder *Meer instellingen* op het validatiescherm.
* **Instellingen → Globale instellingen → Documenttypen → Tabelkolommen**: de vlaggen Verborgen, Verplicht en *AI gebruiken*. Een verborgen kolom wordt nooit gevuld; een kolom met *AI gebruiken* wordt door de AI gevuld, ook voor leveranciers met regels.

## 3. Reproduceren zonder de UI (API / MCP)

Met API- of MCP-toegang kunt u dezelfde vragen programmatisch stellen:

| Vraag | Tool |
|---|---|
| Is deze tabel door de AI geproduceerd? | `get_extracted_tables(doc_id)`: elke tabel bevat `is_ai_table: true/false`. |
| Wat geven de regels, wat geeft de AI? | `get_table_extraction_report(doc_id, mode="nonai")` en nogmaals met `mode="ai"`; het rapport toont voor elk pad de geconfigureerde structuur, de geëxtraheerde rijen en het paginavoorbeeld. Vergelijk de twee. |
| Welke kolommen zijn geconfigureerd, met welke vlaggen? | `get_table_config(doc_type)` |
| Maakt de AI-tier verschil? | `compare_table_extraction_models(doc_id)`, voert twee tiers uit op hetzelfde document (vereist een document met een leveranciersnummer). |
| De extractie op dit document opnieuw uitvoeren | `extract_table_ai(doc_id)` (AI) of `restart_document(doc_id)` (hele pipeline). |
| Wat heeft de pipeline voor dit document gelogd? | `get_document_logs(doc_id)` |

De DocBits MCP-tools worden beschreven in de documentatie van de DocBits MCP.

## 4. Lees de logs

**Instellingen → Loginstellingen** (Activity Logging) toont de gebeurtenissen van alle services. Voor een tabelvraag:

* Filter op de bestandsnaam of het ID van het document in *Search logs*.
* Gebruik het filter *Service*: de extractie zelf draait in de extractieservice en de Celery-workers, niet in de service `api`. Als u alleen `api`-regels ziet, verbreed dan het filter.
* Een normale run logt, in deze volgorde: document ontvangen → OCR / E-Text → classificatie → veldextractie → tabelextractie (regels opzoeken, daarna AI wanneer geen regels overeenkomen) → validatie → statuswijziging. De stap die ontbreekt of een fout meldt, is de stap waar u naar moet kijken.

## 5. Beslissen: configuratie, gegevens of bug

| Symptoom | Meest waarschijnlijk | Volgende stap |
|---|---|---|
| Tabel klopt voor leverancier A, niet voor leverancier B, zelfde documenttype | Per leverancier: B heeft geen regels, of oude regels die niet meer overeenkomen met de lay-out van B | Train de tabel van B eenmalig (of verwijder de regels van B zodat de AI het overneemt). |
| Tabel klopt voor geen enkele leverancier sinds een bepaalde datum | Organisatie-instelling gewijzigd (AI-tier, gestructureerde extractie, vision, tabelkolommen) | Vergelijk de instellingen met de wijzigingsdatum; start één document opnieuw om het te bevestigen. |
| Zelfde document: regelpad leeg, AI-pad correct | De regels komen niet overeen met deze lay-outvariant | Train opnieuw met dit document, of verwijder de regels. |
| Zelfde document: beide paden leeg | Geen leesbare tekst (scan zonder OCR-tekst, pdf met alleen afbeeldingen) | OCR-weergave op het validatiescherm; schakel E-Text in als de pdf een tekstlaag heeft; probeer een andere OCR-versie. |
| Eén kolom verkeerd op elke rij, de rest klopt | Kolomkoppeling of vlag *AI gebruiken* | Tabelkolominstellingen; koppel opnieuw in de tabeltraining. |
| Rijen ontbreken bij pagina-einden of na een subtotaal | Lay-out die de AI of de regels niet hebben gevolgd | Train de tabel met een document van meerdere pagina's; voeg een tag toe zoals *"table continues on page 2"*. |
| Extractiestap ontbreekt in de logs, document blijft hangen in *running* | Infrastructuur (achterstand bij de workers), geen configuratie | Controleer de openstaande taken (`get_pending_tasks_detail` via MCP) en neem contact op met support met het document-ID. |

## Wat u naar support stuurt

* Document-ID en organisatie
* Welk tabblad de rijen bevat (Geëxtraheerde tabel / AI Geëxtraheerde tabel / geen) en de gebruikte AI-tier
* Of de leverancier opgeslagen regels heeft en wanneer die voor het laatst zijn opgeslagen
* Eén voorbeelddocument waar het werkt en één waar het niet werkt, als u beide hebt

## Gerelateerde pagina's

* [Tabel Extractie Probleemoplossing](table-extraction-troubleshoot.md): extractiekwaliteit, OCR, E-Text, tabelmeldingen
* [Training Line Fields / Tabeltraining](../../../administration-and-setup/setup/document-training/training-line-fields-table-training/README.md)
* [AI Tabel](../../../end-user-and-partner-section/end-user-section/ai-table/README.md)
* [Loginstellingen](../../../administration-and-setup/settings/log-settings/README.md)
