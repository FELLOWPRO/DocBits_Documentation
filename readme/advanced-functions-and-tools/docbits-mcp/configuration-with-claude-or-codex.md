# DocBits configureren met Claude of Codex

Beschrijf het gewenste resultaat, laat de assistent de configuratie lezen, beoordeel het voorstel en voer daarna de afgesproken wijziging uit. DocBits MCP biedt hiervoor hulpmiddelen in Claude en Codex met de rechten van het verbonden DocBits-account. Configuratiewijzigingen vereisen de bijbehorende beheerdersrechten.

Deze handleiding beschrijft een werkwijze. Ze bevestigt geen uitgevoerde klantoplossing of geslaagde exporttest.

## 1. Met de juiste organisatie verbinden

Kies regio en omgeving in de [handleiding voor endpoints en aanmelden](setup-and-configuration.md). De opdrachten gebruiken de **EU-sandbox**; vervang de URL als uw testorganisatie een ander endpoint gebruikt. Voer ze uit op de computer waarop de assistent draait, meld u aan en geef in de browser toestemming voor DocBits-toegang.

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.sandbox.api.docbits.com/v3/mcp
claude mcp login docbits
```
{% endtab %}
{% tab title="Codex CLI" %}
```bash
codex mcp add docbits --url https://eu.sandbox.api.docbits.com/v3/mcp
codex mcp login docbits
```
{% endtab %}
{% endtabs %}

Gebruik in de Codex-app de MCP-instellingen of de configuratie die op dezelfde computer met de CLI wordt gedeeld. Gebruik in Claude Desktop een aangepaste externe connector als uw abonnement dit ondersteunt, met hetzelfde HTTP-endpoint. Begin een nieuw gesprek als de hulpmiddelen ontbreken. Actuele instructies: [Codex MCP](https://developers.openai.com/codex/mcp) en [Claude MCP](https://code.claude.com/docs/en/mcp).

```text
Alleen lezen. Controleer de verbonden DocBits-omgeving en organisatie met
get_api_info en get_current_user. Toon de beschikbare configuratiehulpmiddelen.
Toon organisatie-ID en API-host, zonder tokens of delen van sleutels.
Wijzig geen instellingen en verwerk geen documenten.
```

Is de organisatie nog niet bepaald, lees dan de relevante configuratie en controleer de `org_id` in het antwoord. Stop als dit niet de bedoelde organisatie is. Namen kunnen een client-/servervoorvoegsel hebben. Gebruik de hulpmiddelen en parameterschema’s die uw verbinding daadwerkelijk aanbiedt.

## 2. Een eenvoudige instelling wijzigen

```text
Zoek met find_setting de instelling voor QR-code-extractie van deze
testorganisatie. Toon de exacte setting_key en huidige waarde. Vraag bij
meerdere resultaten welke ik bedoel. Als apply_setting deze instelling
ondersteunt, maak dan een voorbeeld van inschakelen. Toon current_value
en proposed_value en wacht op mijn bevestiging voor confirm_setting_change.
```

`apply_setting` maakt alleen een voorbeeld. Na bevestiging van dat concrete voorstel slaat `confirm_setting_change(preview_id)` de wijziging op. Lees de waarde opnieuw en bewaar de `undo_id`: met `undo_setting_change` kunt u de wijziging binnen de teruggegeven termijn terugdraaien. Voorbeelden verlopen doorgaans na 5 minuten en terugdraaien na 15 minuten. Is de waarde gewijzigd of het voorbeeld verlopen, maak en beoordeel dan een nieuw voorbeeld.

Voor ondersteunde gestructureerde wijzigingen geldt `preview_settings_action` → `confirm_settings_action` → `undo_settings_action`. Lees eerst welke actietypen beschikbaar zijn. Ontbreekt een ondersteunde schrijfactie, vraag dan om het `app_path` en wijzig de instelling in DocBits. Verzin geen voorkeursleutel en vervang dit niet door een algemene `set_preference`-aanroep.

## 3. Een als Invoice opgeslagen creditnota onderzoeken

Een Custom-transformatie kan steeds `<INVOICE_TYPE>Invoice</INVOICE_TYPE>` uitvoeren, ook als het oorspronkelijke XML een creditnotacode bevat. Dit is het configuratiescenario uit de [diagnosehandleiding met video van de echte DocBits-interface](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md).

```text
Alleen lezen. Bepaal voor het aangeleverde oorspronkelijke XML en document-ID
de eDoc-familie, syntaxis, versie/profiel en oorspronkelijke typecode. Toon
Custom- en Default-attributen. Lees effectieve en standaard-TRANSFORMATION
en EXTRACTION_PATHS met get_edoc_attribute_source. Noteer attribute_id,
active_version en active_value_id en lees de versiegeschiedenis.
Volg TypeCode -> getransformeerd XML -> invoice_type -> opgeslagen veld,
exportvoorbeeld en latere scripts. Toon bewijs en onzekerheden.
Activeer, verwijder, herstart, keur goed of exporteer niets.
```

Gebruik het **exacte gedetecteerde formaatlabel**; raad geen ZUGFeRD- of Factur-X-versie. De technische `doc_type_key` kan `INVOICE` blijven; de onderzochte bedrijfswaarde is `invoice_type`.

| Lezen | MCP-hulpmiddel |
| --- | --- |
| Custom- en Default-attributen | `list_edoc_custom_attributes` |
| Effectieve of standaardbron en actieve ID’s | `get_edoc_attribute_source`, met `source: "effective"` of `"default"` |
| Versiegeschiedenis en concepten | `list_edoc_attribute_versions`, zo nodig met `include_values: true` |
| Opgeslagen velden, logboeken, exportvoorbeeld | `get_extracted_fields`, `get_document_logs`, `get_export_preview` |

De nu actieve versie bewijst niet welke versie een oud document verwerkte. Behoud die onzekerheid als de logboeken dit niet aantonen. Een PDF-voorbeeld bewijst het opgeslagen type of de geëxporteerde bedragen niet.

<figure><img src="../../.gitbook/assets/edocs-transformation-nl.png" alt="Alleen-lezen ontwikkelvoorbeeld: de broncode- en versie-editor van DocBits. Lees uw eigen effectieve bron en actieve waarde via MCP; de afbeelding toont geen opgeslagen wijziging."><figcaption><p>Alleen-lezen ontwikkelvoorbeeld: de broncode- en versie-editor van DocBits. Lees uw eigen effectieve bron en actieve waarde via MCP; de afbeelding toont geen opgeslagen wijziging.</p></figcaption></figure>

## 4. De kleinste correctie vooraf bekijken

```text
Stel de kleinste wijziging in onze bestaande Custom-transformatie voor,
zodat 381 Credit Note oplevert. Behoud andere mappings en al ondersteunde
creditnotacodes. Classificeer 383 en 384 niet als Credit Note. Toon de diff.
Bekijk de kandidaat op onze testdocumenten zonder op te slaan. Toon het
getransformeerde INVOICE_TYPE en relevante bedragen en vermeld ontbrekende tests.
```

Roep voor een **bestaand attribuut van de eigen organisatie** `preview_edoc_custom_xslt` aan met de volledige kandidaatbron:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Vervang alle tijdelijke aanduidingen door waarden uit uw antwoorden. XSLT/JSON moet de volledige bron bevatten met correcte JSON-escaping. Het hulpmiddel gebruikt een bestaand document van dezelfde organisatie. Het geeft **XML** terug voor `TRANSFORMATION`, velden/tabellen voor `EXTRACTION_PATHS` en **PDF** voor `PREVIEW`, zonder de kandidaat op te slaan. Vergelijk de standaardtransformatie door de standaardbron als andere kandidaat met hetzelfde Custom-attribuut en document te bekijken.

`compare_edoc_extraction` vergelijkt **EXTRACTION_PATHS** en vereist een aangepast Extraction Paths-attribuut. Het vergelijkt geen twee transformaties. Maak geen onnodige aanpassing alleen om dit hulpmiddel te gebruiken.

Bestaat er geen Custom-attribuut, stop dan voordat u er een in productie maakt: `create_edoc_custom_attribute` maakt een **direct actieve** eerste versie en heeft geen optie voor uitsluitend een concept. Bereid een nieuwe aanpassing voor in een testorganisatie of gebruik de ondersteunde aanmaak-/voorbeeldstappen van de DocBits-editor. Probeer gedeelde standaardregels niet wereldwijd te wijzigen.

## 5. Een concept opslaan en bewust activeren

Lees na beoordeling van diff en uitvoer de actieve bron opnieuw. Vergelijk opnieuw als deze ondertussen is gewijzigd. Gebruik voor een bestaand Custom-attribuut `update_edoc_custom_attribute`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Geef bij deze conceptstap altijd `activate: false` mee; de standaardwaarde is `true`. Noteer het teruggegeven versiewaarde-ID en controleer met `list_edoc_attribute_versions` dat de oude versie actief blijft. Een opgeslagen concept beïnvloedt de normale verwerking niet.

Laat na de tests de beheerder de specifieke organisatie, het attribuut, de diff en versie bevestigen. Activeer met `activate_edoc_attribute_version`:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

`draft_id` is het **waarde-ID van de versie**, niet het versienummer of attribuut-ID. Lees de effectieve bron en geschiedenis opnieuw om te controleren dat precies die waarde actief is. eDocs gebruikt deze hulpmiddelen rechtstreeks, zonder het algemene instellingenproces met `preview_id`. Lees ID’s uit de doelomgeving; sandbox-ID’s zijn niet bruikbaar in productie.

## 6. Classificatie, bedragen en export controleren

`test_electronic_document` test de **momenteel actieve** configuratie zonder een document op te slaan. Het heeft geen kandidaat- of conceptselector. Stuur via externe HTTP MCP het oorspronkelijke XML als `file_content_base64` met `file_name`; de server kan geen lokaal `file_path` op uw computer lezen. Activeer de kandidaat eerst uitdrukkelijk in de testorganisatie om de volledige verwerking te testen. Alleen het XSLT-voorbeeld test latere scripts en export niet.

| Oorspronkelijke code | Verwachte controle |
| --- | --- |
| 380 | Invoice blijft Invoice |
| 381 | Creditnota wordt Credit Note |
| 261 | Creditnotagedrag behouden waar formaat/mapping dit ondersteunt |
| 383 | Debetnota wordt geen Credit Note alleen omdat ze een factuur aanpast |
| 384 | Gecorrigeerde factuur wordt geen Credit Note alleen omdat ze corrigeert |

Controleer ook aangepaste velden, regels, totalen en de instelling voor negatieve bedragen. Verwerk een **nieuw testdocument** in een geïsoleerde testorganisatie met gecontroleerde automatische exports. Vergelijk opgeslagen `invoice_type`, dashboard en `get_export_preview`. Een echte export naar het doelsysteem vereist een afzonderlijk afgesproken test. Dry-run en exportvoorbeeld bewijzen geen geslaagde ERP-levering.

`validate_all_edocs` test de beschikbare servertestbestanden zonder documenten op te slaan; `verify_electronic_documents` **uploadt en verwerkt** testbestanden. Ze vervangen uw representatieve documenten en vervolgcontroles niet. Gebruik aangeleverde voorbeelden als bestanden of hulpmiddelen ontbreken.

## 7. Terugdraaien en oude documenten afzonderlijk behandelen

Roep voor terugdraaien `activate_edoc_attribute_version` aan met de eerder vastgelegde `active_value_id` als `draft_id` en controleer de effectieve bron. Verwijder niet de hele aanpassing om één veld te corrigeren: andere mappings gaan verloren en de standaard wordt gebruikt.

Herstart historische documenten niet massaal. Een herstart kan geëxtraheerde gegevens en exportlogboeken wissen en goedkeuringen of exports herhalen. Controleer per document exportstatus, goedkeuringen en handmatige wijzigingen voordat u beslist.

Begin andere configuratievragen met `find_setting` of `run_config_checks` en vraag om de ondersteunde actie of het UI-pad. Bewaar het voor/na-voorstel, testresultaten, actieve waarde-ID’s en terugdraaireferentie in de wijzigingsregistratie.
