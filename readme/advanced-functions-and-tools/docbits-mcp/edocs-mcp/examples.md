# Voorbeelden

Kopieerbare prompts en de volledige werkwijze voor diagnose, concepten, activering en terugdraaien staan in [DocBits configureren met Claude of Codex](../configuration-with-claude-or-codex.md). De voorbeelden gebruiken de huidige parameters. Vervang tijdelijke aanduidingen door waarden van uw organisatie en gebruik volledige broncode met correcte JSON-escaping.

## 1. Een bestaande Custom-regel wijzigen

Lees de effectieve `TRANSFORMATION` met `get_edoc_attribute_source` en gebruik het exacte formaatlabel uit de classificatie:

```json
{
  "electronic_document_type": "<detected_type_from_response>",
  "attribute_name": "TRANSFORMATION",
  "doc_type_key": "INVOICE",
  "source": "effective"
}
```

Noteer `attribute_id`, `active_value_id`, `active_version` en `value`. Lees `source: "default"` apart ter vergelijking en de geschiedenis met `list_edoc_attribute_versions`. De volgende stappen vereisen een bestaand Custom-attribuut van uw organisatie.

Bekijk de volledige kandidaat zonder opslaan met `preview_edoc_custom_xslt`. Gebruik een bestaand document van dezelfde organisatie:

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

Het resultaat is getransformeerd XML voor `TRANSFORMATION`, PDF voor `PREVIEW` of velden/tabellen voor `EXTRACTION_PATHS`. Het voorbeeld selecteert geen opgeslagen concept en test geen latere scripts of exports.

Lees na beoordeling van diff en voorbeeld de actieve bron opnieuw en sla een concept op met `update_edoc_custom_attribute`. Geef uitdrukkelijk `activate: false` mee; de standaardwaarde is `true`.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

Roep na tests in de testorganisatie en bevestiging van de specifieke wijziging `activate_edoc_attribute_version` aan. `draft_id` is het versiewaarde-ID. Lees daarna de effectieve bron opnieuw. Terugdraaien gebruikt de eerder vastgelegde `active_value_id` in dezelfde aanroep.

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

## 2. Als er nog geen Custom-attribuut is

`create_edoc_custom_attribute` maakt een direct actieve eerste versie, geen concept. Test de nieuwe aanpassing in een testorganisatie of gebruik de ondersteunde DocBits-editorstappen. Maak of verwijder geen productieaanpassing alleen voor een voorbeeld. Behoud vereiste mappings; wijzig gedeelde standaardregels niet wereldwijd.

## 3. De actieve configuratie testen

Roep `test_electronic_document` aan met het oorspronkelijke XML als base64:

```json
{
  "file_content_base64": "<base64_of_original_xml>",
  "file_name": "credit-note-test.xml"
}
```

Dit test de actieve regels zonder een document op te slaan, geen inactief concept. Externe HTTP MCP kan geen lokaal `file_path` op uw computer lezen. `compare_edoc_extraction` vergelijkt alleen Extraction Paths en vereist een aangepast Extraction Paths-attribuut; het vergelijkt geen transformaties.

`validate_all_edocs` test de beschikbare servertestbestanden zonder documenten op te slaan. `verify_electronic_documents` uploadt en verwerkt ze en maakt dus documenten. Geen van beide bewijst ERP-levering. Gebruik representatieve voorbeelden, controleer opgeslagen velden/bedragen en export afzonderlijk en herstart historische documenten niet massaal.
