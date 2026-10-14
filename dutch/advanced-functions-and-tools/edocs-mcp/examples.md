# Voorbeelden

End-to-end voorbeelden die laten zien hoe u de eDocs MCP-tools samen gebruikt.

## Voorbeeld 1: Een aangepaste voorvertoning voor XRechnung maken

Dit voorbeeld doorloopt de volledige levenscyclus van een aangepaste PREVIEW-regel:
1. Controleren welke regels al bestaan
2. De XSLT bekijken zonder te activeren
3. De aangepaste regel aanmaken
4. Bijwerken naar een nieuwe versie
5. Terugkeren naar de standaard

### Stap 1: Bestaande aanpassingen controleren

Roep `list_edoc_custom_attributes` aan:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "doc_type_key": "INVOICE"
}
```

Het antwoord toont twee lijsten. Als `custom` leeg is voor het attribuut `PREVIEW`, gebruikt uw organisatie momenteel de ingebouwde standaard-voorvertoningsstylesheet.

### Stap 2: Uw XSLT testen vóór het aanmaken

Roep `preview_edoc_custom_xslt` aan met een bestaande attribuut-ID (gebruik een standaardattribuut uit het antwoord van `list`) en een voorbeeld-XML-bestand gecodeerd als base64:

```json
{
  "attribute_id": "<attribute_id_from_list>",
  "file_content_base64": "<base64_encoded_xrechnung_xml>",
  "file_name": "test_invoice.xml"
}
```

Bekijk de gerenderde uitvoer om te controleren of uw XSLT het verwachte resultaat oplevert voordat u deze vastlegt.

### Stap 3: De aangepaste regel aanmaken

Roep `create_edoc_custom_attribute` aan:

```json
{
  "electronic_document_type": "XRECHNUNG 2.1 CII",
  "attribute_name": "PREVIEW",
  "attribute_value": "<?xml version=\"1.0\"?><xsl:stylesheet xmlns:xsl=\"http://www.w3.org/1999/XSL/Transform\" version=\"2.0\">...</xsl:stylesheet>",
  "doc_type_key": "INVOICE"
}
```

Bewaar de `attribute_id` uit het antwoord. Vanaf dit moment gebruikt elke XRechnung 2.1 CII-factuur die uw organisatie verwerkt uw aangepaste voorvertoning.

### Stap 4: De regel bijwerken met een nieuwe versie

Wilt u de XSLT later verfijnen, roep dan `update_edoc_custom_attribute` aan:

```json
{
  "attribute_id": "<your_attribute_id>",
  "new_value": "<?xml version=\"1.0\"?><xsl:stylesheet ...><!-- improved version --></xsl:stylesheet>",
  "activate": true
}
```

Met `activate: true` schakelt u onmiddellijk over naar de nieuwe versie. De vorige versie blijft bewaard in de geschiedenis. Stel `activate: false` in om als concept op te slaan en later apart te activeren.

### Stap 5: Terugkeren naar de ingebouwde standaard

Wilt u terug naar de standaardvoorvertoning, roep dan `delete_edoc_custom_attribute` aan:

```json
{
  "attribute_id": "<your_attribute_id>"
}
```

De aangepaste regel wordt verwijderd en het systeem valt automatisch terug op de gedeelde standaardstylesheet. Andere klanten worden niet beïnvloed.

---

## Voorbeeld 2: Extractiepaden voor EDI aanpassen

Uw organisatie ontvangt EDI-facturen met een niet-standaard veldindeling. Dit voorbeeld laat zien hoe u de extractiepaden voor uw organisatie overschrijft.

### Stap 1: De huidige regels controleren

```
list_edoc_custom_attributes
  electronic_document_type: "EDI"
  doc_type_key: "INVOICE"
```

Ziet u een `EXTRACTION_PATHS`-item in `default` maar niet in `custom`, dan erft uw organisatie de gedeelde XPath-regels.

### Stap 2: Uw aangepaste extractiepaden aanmaken

Roep `create_edoc_custom_attribute` aan met uw aangepaste XPath-JSON:

```json
{
  "electronic_document_type": "EDI",
  "attribute_name": "EXTRACTION_PATHS",
  "attribute_value": "{\"invoice_id\": \"//Invoice/ID/text()\", \"invoice_date\": \"//Invoice/IssueDate/text()\", \"total_amount\": \"//Invoice/LegalMonetaryTotal/TaxInclusiveAmount/text()\"}",
  "doc_type_key": "INVOICE"
}
```

### Stap 3: Verifiëren met een proefrun

Roep `test_electronic_document` aan met een voorbeeld-EDI-bestand om te bevestigen dat de aangepaste extractiepaden de juiste waarden oppikken:

```json
{
  "file_content_base64": "<base64_encoded_edi_xml>",
  "file_name": "sample_edi_invoice.xml"
}
```

Het antwoord bevat `extracted_fields` en een `preview.image_base64`-PNG — controleer beide op juistheid voordat u live gaat.

---

## Voorbeeld 3: Een volledige eDoc-verificatie uitvoeren

Controleer vóór het uitrollen van een wijziging of alle ondersteunde eDoc-fixtures nog slagen:

```
validate_all_edocs
  fixture_filter: "xrechnung*"
  limit: 0
```

De tool haalt elke XRechnung-fixture door de pipeline en rapporteert per fixture geslaagd/mislukt/waarschuwing. Een schone run bevestigt dat uw aanpassingen andere documenttypen niet hebben beschadigd.

Om snel slechts één type te testen:

```
verify_electronic_documents
  fixture_filter: "zugferd*"
  limit: 3
```

Dit uploadt maximaal 3 ZUGFeRD-fixtures, wacht op de verwerking en verifieert classificatie, extractie en het genereren van de voorvertoning end-to-end.
