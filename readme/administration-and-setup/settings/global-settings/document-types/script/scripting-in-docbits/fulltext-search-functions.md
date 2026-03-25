# Fulltext & Vector Zoekfuncties

{% hint style="info" %}
**Beschikbaar vanaf versie 11.48.0**

Deze functies vereisen dat de **OPENSEARCH\_ENABLED** licentie/voorkeur is geactiveerd voor uw organisatie. Zonder activering geven alle functies een `RuntimeError("Fulltext search license is missing")`.
{% endhint %}

Functies voor het doorzoeken van documentarchieven, het vinden van vergelijkbare documenten en het opvragen van ERP-stamgegevens. Deze zoeken in **alle documenten** van de organisatie — in tegenstelling tot `get_document_content()` dat alleen de tekst van het huidige document leest.

**Bron:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Doorzoekt de volledige OCR-tekst van **alle documenten** in de organisatie. Vindt tekst in de velden `pages.pageText`, `tfidfCustomPageText` en `ai_text` via de fulltextsearch-microservice.

```python
fulltext_search(org_id, query, **kwargs)
```

**Parameters:**

| Naam | Type | Standaard | Beschrijving |
| ---- | ---- | --------- | ------------ |
| `org_id` | `str` | verplicht | Organisatie-UUID (gebruik de contextvariabele `org_id`) |
| `query` | `str` | verplicht | Zoekterm (gezocht in OCR-tekst van alle documenten) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (exacte frase), `"fuzzy"` (fouttolerant, tot 2 tekens verschil), `"prefix"` (begint met) |
| `doc_type` | `str` | `None` | Filter op documenttype (kommagescheiden, bijv. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Filter op documentstatus (kommagescheiden, bijv. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Filter op leveranciersnaam |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Max resultaten (begrensd op 50) |

**Retourneert:** `list[dict]` — Elk dict bevat:

| Veld | Beschrijving |
| ---- | ------------ |
| `doc_id` | Document-UUID |
| `name` | Bestandsnaam (bijv. `"INV-2026-001.pdf"`) |
| `doc_type` | Documenttype (`"INVOICE"`, `"ORDER_CONFIRMATION"`, enz.) |
| `vendor_name` | Leveranciersnaam |
| `status` | Documentstatus |
| `total_amount` | Totaalbedrag |
| `ocr_content` | Overeenkomend tekstfragment uit het document |
| `highlights` | Dict met gemarkeerde overeenkomsten per veld |

**Voorbeeld — Zoeken naar exacte frase:**

```python
results = fulltext_search(org_id, "REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Voorbeeld — Fuzzy zoeken (OCR-fouttolerant):**

```python
# Vindt "REVERSE CHARGE" ook bij OCR-fouten zoals "REVERS CHARG"
results = fulltext_search(org_id, "REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Voorbeeld — Prefix zoeken:**

```python
# Vindt alle documenten met woorden die beginnen met "Rechn"
results = fulltext_search(org_id, "Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Lege zoekopdracht:** Het doorgeven van een lege string retourneert direct `[]` zonder een HTTP-aanroep te doen.
{% endhint %}

{% hint style="info" %}
**Foutafhandeling:** Als de fulltextsearch-service onbereikbaar is, retourneert de functie `[]` en logt een waarschuwing. Er wordt **geen** uitzondering gegenereerd.
{% endhint %}

---

## vector\_search()

Vindt semantisch vergelijkbare documenten met behulp van vectorembeddings (k-NN-zoekopdracht met 384-dimensionale vectoren). Handig voor het vinden van documenten met vergelijkbare inhoud ongeacht de exacte bewoording.

```python
vector_search(org_id, doc_id, **kwargs)
```

**Parameters:**

| Naam | Type | Standaard | Beschrijving |
| ---- | ---- | --------- | ------------ |
| `org_id` | `str` | verplicht | Organisatie-UUID |
| `doc_id` | `str` | verplicht | Brondocument-UUID (het document waarvoor vergelijkbare overeenkomsten gevonden moeten worden) |
| `k` | `int` | `5` | Aantal vergelijkbare documenten om te retourneren (begrensd op 50) |

**Retourneert:** `list[dict]` — Elk dict bevat:

| Veld | Beschrijving |
| ---- | ------------ |
| `doc_id` | UUID van vergelijkbaar document |
| `name` | Bestandsnaam |
| `doc_type` | Documenttype |
| `similarity_score` | Ruwe gelijkenisscore (0-1) |
| `similarity_percent` | Gelijkenis als percentage (0-100) |

**Voorbeeld — Vergelijkbare documenten vinden:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(org_id, doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% similar")
```

{% hint style="info" %}
**Hoe het werkt:** Elk document wordt bij indexering omgezet naar een 384-dimensionale vector. De vectorzoekopdracht vindt de dichtstbijzijnde buren in deze vectorruimte, die overeenkomen met semantisch vergelijkbare documenten.
{% endhint %}

---

## fulltext\_search\_erp()

Doorzoekt ERP-stamgegevens (leveranciers, inkooporders, klanten, materialen) die in OpenSearch zijn geindexeerd.

```python
fulltext_search_erp(org_id, query, **kwargs)
```

**Parameters:**

| Naam | Type | Standaard | Beschrijving |
| ---- | ---- | --------- | ------------ |
| `org_id` | `str` | verplicht | Organisatie-UUID |
| `query` | `str` | verplicht | Zoekterm |
| `entity_types` | `str` | `None` | Filter op entiteittype (kommagescheiden: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Filter op leveranciersnummer |
| `vendor_name` | `str` | `None` | Filter op leveranciersnaam |
| `company_code` | `str` | `None` | Filter op bedrijfscode |
| `size` | `int` | `10` | Max resultaten (begrensd op 50) |

**Retourneert:** `list[dict]` — Entiteittype-specifieke velden (leveranciersrecords hebben `vendor_number`, `vendor_name`, enz.)

**Voorbeeld — Leverancier valideren in ERP:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(org_id, vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Voorbeeld — Inkooporders zoeken:**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(org_id, po_number,
                                   entity_types="purchase_order")
    if results:
        # PO gevonden in ERP
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

Retourneert autocomplete-suggesties voor zoektermen. Groepeert resultaten per categorie (leveranciers, bestandsnamen, factuurnummers).

```python
fulltext_suggestions(org_id, query, **kwargs)
```

**Parameters:**

| Naam | Type | Standaard | Beschrijving |
| ---- | ---- | --------- | ------------ |
| `org_id` | `str` | verplicht | Organisatie-UUID |
| `query` | `str` | verplicht | Prefix / zoekterm |
| `limit` | `int` | `10` | Max suggesties per categorie (begrensd op 20) |

**Retourneert:** `dict` met gegroepeerde suggesties:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Voorbeeld — Leverancierssuggesties ophalen:**

```python
suggestions = fulltext_suggestions(org_id, "ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Lege zoekopdracht:** Het doorgeven van een lege string retourneert direct `{}`.
{% endhint %}

---

## Snelreferentie

| Functie | Doel | Retourneert |
| ------- | ---- | ----------- |
| `fulltext_search()` | OCR-tekst doorzoeken in alle documenten | `list[dict]` |
| `vector_search()` | Semantisch vergelijkbare documenten vinden | `list[dict]` |
| `fulltext_search_erp()` | ERP-stamgegevens doorzoeken | `list[dict]` |
| `fulltext_suggestions()` | Autocomplete-suggesties | `dict` |

---

## Veelvoorkomende Patronen

### Licentiecontrole

Alle vier functies controleren automatisch de `OPENSEARCH_ENABLED`-voorkeur. Indien niet geactiveerd:

```python
# Dit genereert RuntimeError("Fulltext search license is missing")
results = fulltext_search(org_id, "test")
```

Om dit elegant af te handelen in scripts:

```python
try:
    results = fulltext_search(org_id, "test")
except RuntimeError:
    # OpenSearch niet geactiveerd voor deze organisatie — zoeken overslaan
    results = []
```

### Combinatie met Veldfuncties

```python
# Zoeken -> valideren -> veld instellen
results = fulltext_search(org_id, invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```
