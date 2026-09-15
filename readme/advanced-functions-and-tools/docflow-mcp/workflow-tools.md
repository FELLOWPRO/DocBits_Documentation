# Workflow-Tools

DocFlow MCP stellt Tools zur Verwaltung und zum Testen erweiterter Workflows bereit, dazu Tools zum Lesen von Workflow-Protokollen und zur Verwaltung von Workflow-Variablen.

{% hint style="info" %}
**Tool-Namen über das DocBits-MCP-Gateway.** Wenn Sie sich über das vereinheitlichte DocBits MCP (`api.docbits.com/v3/mcp`) verbinden, trägt jedes DocFlow-Tool das Präfix `docflow_`: `list_workflows` heißt dort `docflow_list_workflows`, `run_workflow_with_assertions` heißt `docflow_run_workflow_with_assertions`. Die Parameter sind identisch. Die Namen unten sind die reinen DocFlow-Namen.

Workflows werden **im DocFlow-Designer** in der Web-App **erstellt und bearbeitet**. Das MCP liest, testet, führt aus und löscht sie; es erstellt oder verändert keine Workflow-Graphen.
{% endhint %} Die Card SDK Tools haben eine eigene Seite, siehe [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Alle Workflows der aktuellen Organisation auflisten.

**Parameter:** Keine

**Beispielantwort:**

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

Details eines bestimmten Workflows einschliesslich seiner Knoten- und Kantenstruktur abrufen.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des Workflows |

**Beispielantwort:**

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

Einen Workflow anhand der ID loeschen (Soft-Delete).

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des zu loeschenden Workflows |

**Beispielantwort:**

```json
{
  "success": true,
  "workflow_id": "a1b2c3d4-..."
}
```

## test\_advanced\_workflow

Einen erweiterten Workflow testen. Optional kann eine Dokument-ID angegeben werden, um mit einem echten Dokument zu testen.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des erweiterten Workflows |
| `doc_id` | string | Nein | UUID eines Dokuments zum Testen |

**Beispielantwort:**

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

Alle Workflow-Testszenarien der Organisation auflisten.

**Parameter:** Keine

**Beispielantwort:**

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

Alle verfuegbaren Workflow-Karten mit ihren Bedingungen und Konfigurationen auflisten.

**Parameter:** Keine

**Beispielantwort:**

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
Karten haben Rollen-Flags: `when_condition` (Ausloeser), `and_condition` (zusaetzliche Bedingung) und `then_condition` (Aktion). Verwenden Sie diese, um zu bestimmen, in welchen Knotentypen eine Karte verwendet werden kann.
{% endhint %}

## list\_workflow\_variables

Alle Workflow-Variablen der Organisation mit Name, Typ und aktuellem Wert auflisten.

**Parameter:** Keine

## set\_workflow\_variable

Eine Workflow-Variable erstellen oder ihren Wert aktualisieren. Variablen vom Typ Dokument haben keinen eigenen Wert; sie werden vom Workflow zur Laufzeit gesetzt.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `name` | string | Ja | Name der Variable |
| `value` | string | Nein | Neuer Wert |
| `var_type` | string | Nein | Typ der Variable beim Erstellen (zum Beispiel `string`, `number`, `document`) |

## search\_workflow\_logs

Workflow-Ausführungsprotokolle durchsuchen, um herauszufinden, warum Läufe fehlgeschlagen sind, erfolgreich waren oder an einer Bedingung gescheitert sind.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Nein | Auf einen Workflow einschränken |
| `doc_id` | string | Nein | Auf Läufe für ein Dokument einschränken |
| `status` | string | Nein | Laufstatus, nach dem gefiltert wird |
| `keyword` | string | Nein | Freitextfilter auf das Protokoll |
| `include_workflow_data` | boolean | Nein | Den Snapshot der Workflow-Definition pro Lauf einschließen |
| `limit` / `offset` | integer | Nein | Seitenweise Ausgabe |

## get\_workflow\_log\_detail

Alle Details eines Laufs: die rohen Ausführungsprotokolle der Karten und die Workflow-Definition, wie sie zur Laufzeit war.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `log_id` | string | Ja | ID des Protokolleintrags aus `search_workflow_logs` |

## run\_workflow\_with\_assertions

Workflow-Variablen vorbelegen, einen erweiterten Workflow mit dem echten Executor ausführen und das Ergebnis gegen die Datenbank prüfen. Variablen sind echte Schreibvorgänge, keine Mocks; verwenden Sie das Tool, um einen Workflow aus einem Assistenten heraus zu integrationstesten.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des auszuführenden Workflows |
| `doc_id` | string | Nein | Dokument, gegen das der Workflow ausgeführt wird |
| `seed_variables` | array | Nein | Variablen, die vor dem Lauf erstellt oder aktualisiert werden; Variablen vom Typ Dokument können über `value` auf eine `doc_id` zeigen |
