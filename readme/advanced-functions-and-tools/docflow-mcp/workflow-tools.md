# Workflow Tools

DocFlow MCP biedt tools voor het beheren en testen van geavanceerde workflows, plus tools voor het lezen van workflowlogs en het beheren van workflowvariabelen.

{% hint style="info" %}
**Toolnamen via de DocBits MCP-gateway.** Wanneer u verbinding maakt via de gecombineerde DocBits MCP (`api.docbits.com/v3/mcp`), krijgt elke DocFlow-tool het voorvoegsel `docflow_`: `list_workflows` heet dan `docflow_list_workflows`, `run_workflow_with_assertions` heet `docflow_run_workflow_with_assertions`. De parameters zijn identiek. De namen hieronder zijn de kale DocFlow-namen.

Workflows worden **aangemaakt en bewerkt in de DocFlow-designer** in de webapp. De MCP leest, test, voert uit en verwijdert ze; de MCP maakt of wijzigt geen workflowgrafen.
{% endhint %} De Card SDK-tools staan op een eigen pagina, zie [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Alle workflows van de huidige organisatie weergeven.

**Parameters:** Geen

## get\_workflow

Details van een specifieke workflow ophalen, inclusief de node- en edge-structuur.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID van de workflow |

## delete\_workflow

Een workflow verwijderen op basis van ID (zachte verwijdering).

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID van de te verwijderen workflow |

## test\_advanced\_workflow

Een geavanceerde workflow-uitvoering testen. Optioneel kunt u een document-ID opgeven om met een echt document te testen.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID van de geavanceerde workflow |
| `doc_id` | string | Nee | UUID van een document om mee te testen |

## list\_test\_scenarios

Alle testscenario's voor workflows van de organisatie weergeven.

**Parameters:** Geen

## list\_cards

Alle beschikbare workflowkaarten weergeven met hun condities en configuratie.

**Parameters:** Geen

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
|-----------|------|----------|-------------|
| `name` | string | Ja | Naam van de variabele |
| `value` | string | Nee | Nieuwe waarde |
| `var_type` | string | Nee | Type van de variabele bij het aanmaken (bijvoorbeeld `string`, `number`, `document`) |

## search\_workflow\_logs

Workflow-uitvoeringslogs doorzoeken om te achterhalen waarom runs zijn mislukt, geslaagd of op een niet-overeenkomende conditie zijn gestuit.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
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
|-----------|------|----------|-------------|
| `log_id` | string | Ja | ID van de logvermelding uit `search_workflow_logs` |

## run\_workflow\_with\_assertions

Workflowvariabelen vooraf vullen, een geavanceerde workflow met de echte executor uitvoeren en het resultaat controleren tegen de database. Variabelen zijn echte schrijfacties, geen mocks; gebruik dit om een workflow vanuit een assistent te integratietesten.

**Parameters:**

| Parameter | Type | Vereist | Beschrijving |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID van de uit te voeren workflow |
| `doc_id` | string | Nee | Document waartegen de workflow wordt uitgevoerd |
| `seed_variables` | array | Nee | Variabelen die vóór de run worden aangemaakt of bijgewerkt; variabelen van het type document kunnen via `value` naar een `doc_id` verwijzen |
