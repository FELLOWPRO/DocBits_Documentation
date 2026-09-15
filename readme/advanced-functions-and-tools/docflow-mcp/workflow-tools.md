# Workflow Tools

DocFlow MCP biedt tools voor het beheren en testen van geavanceerde workflows, plus tools voor het lezen van workflowlogs en het beheren van workflowvariabelen.

{% hint style="info" %}
**Toolnamen via de DocBits MCP-gateway.** Wanneer u verbinding maakt via de gecombineerde DocBits MCP (`api.docbits.com/v3/mcp`), krijgt elke DocFlow-tool het voorvoegsel `docflow_`: `list_workflows` heet dan `docflow_list_workflows`, `run_workflow_with_assertions` heet `docflow_run_workflow_with_assertions`. De parameters zijn identiek. De namen hieronder zijn de kale DocFlow-namen.

Workflows worden **aangemaakt en bewerkt in de DocFlow-designer** in de webapp. De MCP leest, test, voert uit en verwijdert ze; de MCP maakt of wijzigt geen workflowgrafen.
{% endhint %} De Card SDK-tools staan op een eigen pagina, zie [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Alle workflows van de huidige organisatie weergeven.

**Parameters:** Geen

**Voorbeeldrespons:**

```json
[
  {
    "id": "a1b2c3d4-...",
    "name": "Invoice Approval",
    "version": 3,
    "enabled": true,
    "doc_types": ["INVOICE"],
    "workflow_type": "advanced",
    "created_on": "2025-01-15 10:30:00",
    "last_modified_on": "2025-03-20 14:22:00"
  }
]
```

## get\_workflow

Details van een specifieke workflow ophalen, inclusief de node- en edge-structuur.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `workflow_id` | string | Ja | UUID van de workflow |

**Voorbeeldrespons:**

```json
{
  "id": "a1b2c3d4-...",
  "name": "Invoice Approval",
  "version": 3,
  "enabled": true,
  "doc_types": ["INVOICE"],
  "workflow_type": "advanced",
  "description": "Routes invoices based on amount",
  "advanced_config": {
    "nodes": [
      {"node_id": "when-1", "node_type": "when", "label": "Amount > 1000"},
      {"node_id": "then-1", "node_type": "then", "label": "Send for Approval"}
    ],
    "edges": [
      {"source_node_id": "when-1", "target_node_id": "then-1"}
    ]
  }
}
```

## delete\_workflow

Een workflow verwijderen op basis van ID (zachte verwijdering).

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `workflow_id` | string | Ja | UUID van de te verwijderen workflow |

**Voorbeeldrespons:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-..."
}
```

## test\_advanced\_workflow

Een geavanceerde workflow-uitvoering testen. Optioneel kunt u een document-ID opgeven om met een echt document te testen.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `workflow_id` | string | Ja | UUID van de geavanceerde workflow |
| `doc_id` | string | Nee | UUID van een document om mee te testen |

**Voorbeeldrespons:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-...",
  "execution_time": 0.234,
  "workflow_result": "completed",
  "node_results": {
    "when-1": {"status": "success", "output": true},
    "then-1": {"status": "success"}
  },
  "logs": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "status": "success",
      "error": null,
      "duration_ms": 12
    }
  ]
}
```

## list\_test\_scenarios

Alle testscenario's voor workflows van de organisatie weergeven.

**Parameters:** Geen

**Voorbeeldrespons:**

```json
[
  {
    "id": "scenario-uuid",
    "name": "Invoice over 1000 EUR",
    "workflow_id": "a1b2c3d4-...",
    "enabled": true,
    "status": "passed",
    "last_run": "2025-03-20 14:00:00"
  }
]
```

## list\_cards

Alle beschikbare workflowkaarten weergeven met hun condities en configuratie.

**Parameters:** Geen

**Voorbeeldrespons:**

```json
[
  {
    "id": "card-uuid",
    "text": "Document Type Is",
    "card_type": "document_type_is",
    "card_version": 1,
    "category": "Document",
    "when_condition": true,
    "and_condition": false,
    "then_condition": false
  },
  {
    "id": "card-uuid-2",
    "text": "Send Email Notification",
    "card_type": "send_email",
    "card_version": 1,
    "category": "Communication",
    "when_condition": false,
    "and_condition": false,
    "then_condition": true
  }
]
```

{% hint style="info" %}
Kaarten hebben rolvlaggen: `when_condition` (trigger), `and_condition` (aanvullende voorwaarde) en `then_condition` (actie). Gebruik deze om te bepalen in welke nodetypes een kaart kan worden gebruikt.
{% endhint %}

## list\_workflow\_variables

Alle workflowvariabelen van de organisatie weergeven met naam, type en huidige waarde.

**Parameters:** Geen

## set\_workflow\_variable

Een workflowvariabele aanmaken of de waarde ervan bijwerken. Variabelen van het type document hebben geen eigen waarde; ze worden tijdens de uitvoering door de workflow ingesteld.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `name` | string | Ja | Naam van de variabele |
| `value` | string | Nee | Nieuwe waarde |
| `var_type` | string | Nee | Type van de variabele bij het aanmaken (bijvoorbeeld `string`, `number`, `document`) |

## search\_workflow\_logs

Workflow-uitvoeringslogs doorzoeken om te achterhalen waarom runs zijn mislukt, geslaagd of op een niet-overeenkomende conditie zijn gestuit.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `workflow_id` | string | Nee | Beperken tot één workflow |
| `doc_id` | string | Nee | Beperken tot runs voor één document |
| `status` | string | Nee | Runstatus om op te filteren |
| `keyword` | string | Nee | Vrije-tekstfilter op de log |
| `include_workflow_data` | boolean | Nee | De momentopname van de workflowdefinitie per run meesturen |
| `limit` / `offset` | integer | Nee | Paginering |

## get\_workflow\_log\_detail

Volledige details van één run: de ruwe kaartuitvoeringslogs en de workflowdefinitie zoals die op het moment van de run was.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `log_id` | string | Ja | ID van de logvermelding uit `search_workflow_logs` |

## run\_workflow\_with\_assertions

Workflowvariabelen vooraf vullen, een geavanceerde workflow met de echte executor uitvoeren en het resultaat controleren tegen de database. Variabelen zijn echte schrijfacties, geen mocks; gebruik dit om een workflow vanuit een assistent te integratietesten.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|---------|-------------|
| `workflow_id` | string | Ja | UUID van de uit te voeren workflow |
| `doc_id` | string | Nee | Document waartegen de workflow wordt uitgevoerd |
| `seed_variables` | array | Nee | Variabelen die vóór de run worden aangemaakt of bijgewerkt; variabelen van het type document kunnen via `value` naar een `doc_id` verwijzen |
