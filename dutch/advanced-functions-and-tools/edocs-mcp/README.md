# eDocs MCP

De DocBits API biedt een **Model Context Protocol (MCP)**-server met tools voor het inspecteren en aanpassen van de verwerking van elektronische documenten (eDoc). Elke MCP-compatibele client — Claude Code, Claude Desktop of aangepaste integraties — kan verbinding maken en deze tools gebruiken.

## Wat kunt u doen?

Met de eDocs MCP-tools kunt u:

- **Inspecteren** hoe elk type elektronisch document wordt geclassificeerd en welke extractieregels van toepassing zijn
- **Testen** van documenten via de volledige verwerkingspipeline zonder op te slaan in de database
- **Aangepaste regels maken** voor uw organisatie — XSLT-voorvertoningen, extractiepaden, transformaties
- **Bijwerken** van een aangepaste regel met een nieuwe versie (met of zonder deze direct te activeren)
- **Verwijderen** van een aangepaste regel om terug te keren naar de ingebouwde standaard
- **Verifiëren** dat alle ondersteunde eDoc-fixtures correct worden verwerkt

## Rechtenmodel

DocBits levert een bibliotheek met ingebouwde standaardregels die door alle klanten wordt gedeeld. Deze standaardregels gebruiken de gereserveerde organisatie-ID `00000000-0000-0000-0000-000000000000`.

**De standaardregels zijn onveranderlijk via MCP.** Elke schrijftool controleert uw organisatie-ID voordat een verzoek wordt gedaan. Als die naar de standaardorganisatie verwijst, wordt de bewerking onmiddellijk geweigerd — er wordt nooit een API-aanroep gedaan.

Klanten kunnen alleen regels **binnen hun eigen organisatie** aanmaken, wijzigen of verwijderen. Als er een aangepaste regel voor uw organisatie bestaat, heeft die voorrang op de standaard. Het verwijderen van een aangepaste regel herstelt automatisch het standaardgedrag.

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## Overzicht van tools

### Inspectie (alleen-lezen)

| Tool | Beschrijving |
|------|-------------|
| `test_electronic_document` | De volledige eDoc-pipeline als proefrun uitvoeren — classificatie, extractie, voorvertoning — zonder op te slaan |
| `list_electronic_document_types` | Alle ondersteunde eDoc-typen weergeven met de configuratiestatus |
| `get_extraction_rules` | De XPath-regels tonen waarmee velden voor een bepaald documenttype worden geëxtraheerd |
| `get_extracted_fields` | De headervelden ophalen die uit een verwerkt document zijn geëxtraheerd |
| `get_extracted_tables` | De factuurregels ophalen die uit een verwerkt document zijn geëxtraheerd |
| `get_preview_pdf` | De met XSLT gerenderde voorvertoning-pdf van een document ophalen |
| `get_preview_image` | Een gerenderd paginabeeld van een verwerkt document ophalen |
| `extract_edoc_table` | Een XML/EDI-bestand dat u aanlevert extraheren en de velden teruggeven als platte tabel, samen met de regel die elk veld heeft opgeleverd |
| `compare_edoc_extraction` | De standaardextractie en uw aangepaste extractie (en optioneel een kandidaatregel) op één document vergelijken |

### Aanpassing (per organisatie, standaardorganisatie geblokkeerd)

| Tool | Beschrijving |
|------|-------------|
| `list_edoc_custom_attributes` | De aangepaste overschrijvingen van uw organisatie en de ingebouwde standaarden voor een documenttype weergeven |
| `create_edoc_custom_attribute` | Een nieuwe aangepaste regel aanmaken (EXTRACTION_PATHS, TRANSFORMATION of PREVIEW) |
| `update_edoc_custom_attribute` | Een nieuwe versie van een aangepaste regel toevoegen, optioneel direct geactiveerd |
| `delete_edoc_custom_attribute` | Een aangepaste regel verwijderen — het systeem valt automatisch terug op de standaard |
| `preview_edoc_custom_xslt` | Een XSLT-transformatie als proefrun op een XML-document uitvoeren vóór activering |
| `get_edoc_attribute_source` | De bewerkbare bron van een attribuut (PREVIEW, EXTRACTION_PATHS, TRANSFORMATION) ophalen om het te wijzigen |
| `list_edoc_attribute_versions` | Versiegeschiedenis van een aangepast attribuut: concepten en de actieve versie |
| `activate_edoc_attribute_version` | Een specifieke versie of een concept activeren (zo draait u terug) |
| `delete_edoc_attribute_draft` | Een concept verwijderen dat nooit is geactiveerd |

### Verificatie

| Tool | Beschrijving |
|------|-------------|
| `verify_electronic_documents` | Fixtures uploaden en classificatie, extractie en voorvertoning end-to-end verifiëren |
| `validate_all_edocs` | Alle eDoc-fixtures als proefrun door de pipeline halen en problemen rapporteren |

## Attribuuttypen

Elke aanpasbare regel heeft een specifiek type en formaat:

| Attribuutnaam | Formaat | Doel |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | XPath-expressies die XML-knooppunten aan DocBits-velden koppelen |
| `TRANSFORMATION` | XSLT | Stylesheet die vóór de extractie op de XML wordt toegepast |
| `PREVIEW` | XSLT | Stylesheet die de voor mensen leesbare pdf-voorvertoning rendert |
| `STRUCTURE_DESCRIPTOR` | JSON | Structuurtoewijzing, alleen voor EDI-documenten |

De tool `create_edoc_custom_attribute` leidt het juiste formaat automatisch af uit de attribuutnaam.

## Snelstart

### Weergeven wat uw organisatie heeft aangepast

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

Geeft twee lijsten terug: `custom` (de overschrijvingen van uw organisatie) en `default` (gedeelde regels die u overerft).

### Een aangepaste voorvertoning voor XRechnung maken

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

Geeft de nieuwe `attribute_id` terug — bewaar die voor updates en verwijdering.

### Een bestaande aangepaste regel bijwerken

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

Maakt een nieuwe versie aan en activeert die. De vorige versie blijft bewaard in de geschiedenis.

### Terugkeren naar de standaard

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

Verwijdert de aangepaste overschrijving. Het systeem valt onmiddellijk terug op de ingebouwde standaardregel.

## Veiligheidsregels

| Actie | Toegestaan |
|--------|---------|
| Standaardregels lezen | ✅ Ja |
| Aangepaste regel voor uw organisatie aanmaken | ✅ Ja |
| Aangepaste regel voor uw organisatie bijwerken | ✅ Ja |
| Aangepaste regel voor uw organisatie verwijderen | ✅ Ja |
| Standaardregels wijzigen of verwijderen | ❌ **Nooit** — geblokkeerd op de MCP-laag |

Een poging om naar `00000000-0000-0000-0000-000000000000` te schrijven geeft als resultaat:

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```
