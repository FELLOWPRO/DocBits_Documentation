# Workflow Tools

DocFlow MCP biedt tools voor het beheren en testen van geavanceerde workflows, plus tools voor het lezen van workflow-logs en het beheren van workflow-variabelen. De Card SDK-tools hebben een eigen pagina — zie [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Alle workflows van de huidige organisatie opvragen.

**Parameters:** Geen

## get\_workflow

Details van een specifieke workflow opvragen, inclusief zijn knoop- en kantstructuur.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID van de workflow |

## create\_advanced\_workflow

Een nieuwe geavanceerde workflow aanmaken met knopen en kanten.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `name` | string | Ja | Workflow-naam (3-126 tekens) |
| `description` | string | Nee | Optionele beschrijving |
| `nodes` | array | Ja | Array van workflow-knopen |
| `edges` | array | Ja | Array van kanten die knopen verbinden |

### Knoopstructuur

Elke knoop vereist:

| Veld | Type | Beschrijving |
|-------|------|-------------|
| `node_id` | string | Unieke identificator van de knoop |
| `node_type` | string | Zie knooptypen hieronder |
| `position` | object | `{x: number, y: number}` positie op het canvas |
| `label` | string | Weergavelabel |
| `card` | object | Kaartconfiguratie (vereist voor `when`, `and`, `then` — zie hieronder) |

**Knooptypen:**

| Type | Kaart vereist | Doel |
|------|------------------|---------|
| `start` | Geen kaart | Triggerknoop — startpunt van de workflow |
| `when` | Conditiekaart | Trigger-conditie (ook geldig startpunt) |
| `and` | Conditiekaart | Aanvullende conditiepoort na een `when` |
| `or` | Geen kaart | Vertakkingsknoop — gaat door als een van de inkomende takken slaagt |
| `then` | Actiekaart | Uit te voeren actie |
| `delay` | Geen kaart | Wachtknoop — pauzeert de uitvoering voor een geconfigureerde duur |
| `all` | Geen kaart | Samenvoegknoop — wacht op alle inkomende takken |
| `any` | Geen kaart | Samenvoegknoop — gaat verder met de eerste inkomende tak |
| `note` | Geen kaart | Plakbriefje / annotatie; wordt niet uitgevoerd |

### Kantstructuur

Elke kant vereist:

| Veld | Type | Beschrijving |
|-------|------|-------------|
| `edge_id` | string | Unieke identificator van de kant |
| `source_node_id` | string | ID van de bronknoop |
| `target_node_id` | string | ID van de doelknoop |
| `source_handle` | string | `success`, `error` of `failed_condition` (optioneel) |
| `target_handle` | string | `input` (optioneel) |

**Source-handles:**

- `success` — genomen wanneer de bronknoop slaagt (beschikbaar op elke uitvoerbare knoop).
- `failed_condition` — genomen wanneer een `when`- of `and`-conditiekaart als false wordt geëvalueerd.
- `error` — genomen wanneer een `and`- of `then`-knoop een fout opwerpt.

### Kaartconfiguratie

Kaarten definiëren wat een knoop doet. Gebruik `list_cards` of `sdk_list_cards_picker` om beschikbare kaarten op te vragen.

```json
{
  "id": "card-uuid-here",
  "card_type": "document_type_is",
  "version": 1,
  "variables": [
    {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
  ]
}
```

{% hint style="info" %}
U hoeft alleen `id`, `card_type`, `version` en `variables` op te geven voor elke kaart. De server verrijkt kaarten automatisch met weergavemetadata (svg, text, category) uit de database.
{% endhint %}

**Voorbeeldverzoek:**

```json
{
  "name": "Simple Invoice Router",
  "description": "Routes invoices to approval",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 100, "y": 100},
      "label": "Document is Invoice",
      "card": {
        "id": "card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 100, "y": 300},
      "label": "Send Notification",
      "card": {
        "id": "card-uuid-2",
        "card_type": "send_email",
        "version": 1,
        "variables": []
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

## update\_advanced\_workflow

Een bestaande geavanceerde workflow bijwerken. U kunt elke combinatie van naam, beschrijving, knopen en kanten bijwerken.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID van de bij te werken workflow |
| `name` | string | Nee | Nieuwe naam |
| `description` | string | Nee | Nieuwe beschrijving |
| `nodes` | array | Nee | Nieuwe knopen (vervangt alle bestaande knopen) |
| `edges` | array | Nee | Nieuwe kanten (vervangt alle bestaande kanten) |

## delete\_workflow

Een workflow verwijderen op ID (soft delete).

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID van de te verwijderen workflow |

## test\_advanced\_workflow

Een uitvoering van een geavanceerde workflow testen. Geef optioneel een document-ID op om met een echt document te testen.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID van de geavanceerde workflow |
| `doc_id` | string | Nee | UUID van een document om mee te testen |

## list\_test\_scenarios

Alle workflow-testscenario's voor de organisatie opvragen.

**Parameters:** Geen

## list\_cards

Alle beschikbare workflow-kaarten met hun voorwaarden en configuratie opvragen.

**Parameters:** Geen

{% hint style="info" %}
Kaarten hebben rolvlaggen: `when_condition` (trigger), `and_condition` (aanvullende conditie) en `then_condition` (actie). Gebruik deze om te bepalen in welke knooptypen een kaart kan worden gebruikt.
{% endhint %}
