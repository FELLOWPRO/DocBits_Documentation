# Workflow-Tools

DocFlow MCP stellt Tools zur Verwaltung und zum Testen erweiterter Workflows bereit, dazu Tools zum Lesen von Workflow-Protokollen und zur Verwaltung von Workflow-Variablen.

{% hint style="info" %}
**Tool-Namen über das DocBits-MCP-Gateway.** Wenn Sie sich über das vereinheitlichte DocBits MCP (`api.docbits.com/v3/mcp`) verbinden, trägt jedes DocFlow-Tool das Präfix `docflow_`: `list_workflows` heißt dort `docflow_list_workflows`, `run_workflow_with_assertions` heißt `docflow_run_workflow_with_assertions`. Die Parameter sind identisch. Die Namen unten sind die reinen DocFlow-Namen.

Workflows werden **im DocFlow-Designer** in der Web-App **erstellt und bearbeitet**. Das MCP liest, testet, führt aus und löscht sie; es erstellt oder verändert keine Workflow-Graphen.
{% endhint %} Die Card SDK Tools haben eine eigene Seite, siehe [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Listet alle Workflows der aktuellen Organisation auf.

**Parameter:** Keine

## get\_workflow

Ruft Details eines bestimmten Workflows ab, einschließlich seiner Knoten- und Kantenstruktur.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des Workflows |

## delete\_workflow

Löscht einen Workflow anhand der ID (Soft-Delete).

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des zu löschenden Workflows |

## test\_advanced\_workflow

Testet die Ausführung eines erweiterten Workflows. Optional kann eine Dokument-ID angegeben werden, um mit einem echten Dokument zu testen.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des erweiterten Workflows |
| `doc_id` | string | Nein | UUID eines Dokuments zum Testen |

## list\_test\_scenarios

Listet alle Workflow-Testszenarien der Organisation auf.

**Parameter:** Keine

## list\_cards

Listet alle verfügbaren Workflow-Karten mit ihren Bedingungen und Konfigurationen auf.

**Parameter:** Keine

{% hint style="info" %}
Karten haben Rollen-Flags: `when_condition` (Auslöser), `and_condition` (zusätzliche Bedingung) und `then_condition` (Aktion). Verwenden Sie diese, um zu bestimmen, in welchen Knotentypen eine Karte verwendet werden kann.
{% endhint %}

## list\_workflow\_variables

Listet alle Workflow-Variablen der Organisation mit Name, Typ und aktuellem Wert auf.

**Parameter:** Keine

## set\_workflow\_variable

Erstellt eine Workflow-Variable oder aktualisiert ihren Wert. Variablen vom Typ Dokument haben keinen eigenen Wert; sie werden vom Workflow zur Laufzeit gesetzt.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `name` | string | Ja | Name der Variable |
| `value` | string | Nein | Neuer Wert |
| `var_type` | string | Nein | Typ der Variable beim Erstellen (zum Beispiel `string`, `number`, `document`) |

## search\_workflow\_logs

Durchsucht Workflow-Ausführungsprotokolle, um herauszufinden, warum Läufe fehlgeschlagen sind, erfolgreich waren oder an einer Bedingung gescheitert sind.

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

Belegt Workflow-Variablen vor, führt einen erweiterten Workflow mit dem echten Executor aus und prüft das Ergebnis gegen die Datenbank. Variablen sind echte Schreibvorgänge, keine Mocks; verwenden Sie das Tool, um einen Workflow aus einem Assistenten heraus per Integrationstest zu prüfen.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des auszuführenden Workflows |
| `doc_id` | string | Nein | Dokument, gegen das der Workflow ausgeführt wird |
| `seed_variables` | array | Nein | Variablen, die vor dem Lauf erstellt oder aktualisiert werden; Variablen vom Typ Dokument können über `value` auf eine `doc_id` zeigen |
