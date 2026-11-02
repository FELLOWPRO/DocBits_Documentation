---
description: "P1: API-aanroepen en gebruik van antwoorden verifiëren"
---

# P1: API-aanroepen en gebruik van antwoorden verifiëren

**Call API** v2 voegt het ingestelde pad toe aan de DocBits-API-basis en gebruikt de huidige organisatiecontext. **Send HTTPS Request** v2 gebruikt een externe URL en eigen headers. Een volledige externe URL vervangt geen Call API-pad. Beide kaarten simuleren verzending in Advanced Test.

De onderzochte HTTPS-actie logt status en antwoordtekst, maar biedt geen vrij benoembare JSON-antwoordopslag aan volgende kaarten. Call API zet de antwoordtekst om naar een boolean. HTTP 200, geldige JSON en geslaagde zakelijke vervolgverwerking vragen dus afzonderlijk bewijs. Verzin geen toegangssyntaxis zoals `api.response.cost_center`.

Spreek voor extern `{"cost_center":"4711"}` een expliciet ondersteunde terugschrijfactie of callback naar een documentveld af. Controleer het opgeslagen veld en lees dit in de bedoelde vervolguitvoering. Directe antwoordoverdracht vereist een kaart of uitbreiding met gedocumenteerd uitvoercontract. JSON in de configuratie bewijst ook niet automatisch de daadwerkelijk verstuurde JSON-bytes.

Gebruik een eigen testdoel en inspecteer methode, headers, echte body, status en schema. Neem 4xx, 5xx, timeout, ongeldige JSON en dubbele activering mee. Herhaal schrijfaanroepen pas na controle van de eerste ontvangst. De voorbeeld-URL is een gereserveerde aanduiding en is niet als bereikbare dienst getest.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `call_api` · v2

Identiteit: `6ca5e621-af72-4f55-aa2e-b3caa288722a`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `params` | `params:str` | `"{}"` |
| `api_endpoint` | `api_endpoint:str` | `"YOUR_RELATIVE_API_PATH"` |
| `data` | `data:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

### `action_https_request` · v2

Identiteit: `18d06ca4-3aca-4e49-b75c-566ade2fcb10`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `data` | `data` | `"{}"` |
| `params` | `params` | `"{}"` |
| `url` | `url:str` | `"https://training.example.invalid/status"` |
| `headers` | `headers:str` | `"{}"` |
| `method` | `put / post / delete / get` | `"get"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| API-01 | Advanced Test | gesimuleerd; geen afleveringsbewijs |
| API-02 | HTTPS: 4xx / 5xx | error |
| API-03 | timeout | controleer ontvangst vóór herhaling |
| API-04 | {"cost_center":"4711"} | geen automatisch api.response.cost_center |
| API-05 | POST × 2 | controleer duplicaten bij het doel |

## Bewijs en grenzen

Parameters en gedrag zijn vergeleken met de Dev-catalogus en onderzochte broncode. Zakelijke testgevallen vormen een acceptatieprocedure. Voor dit hoofdstuk zijn geen persoonlijke goedkeuringen, echte wijzigingen of afleveringen uitgevoerd.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)
