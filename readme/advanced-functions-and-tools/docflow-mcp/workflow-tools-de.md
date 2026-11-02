# Workflow-Tools

DocFlow MCP stellt Tools zur Verwaltung und zum Testen erweiterter Workflows bereit, ausserdem Tools zum Lesen von Workflow-Logs und zur Verwaltung von Workflow-Variablen. Die Card-SDK-Tools haben eine eigene Seite -- siehe [Card SDK Tools](card-sdk-tools.md).

## list\_workflows

Alle Workflows der aktuellen Organisation auflisten.

**Parameter:** Keine

## get\_workflow

Details eines bestimmten Workflows einschliesslich seiner Knoten- und Kantenstruktur abrufen.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des Workflows |

## create\_advanced\_workflow

Einen neuen erweiterten Workflow mit Knoten und Kanten erstellen.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `name` | string | Ja | Workflow-Name (3-126 Zeichen) |
| `description` | string | Nein | Optionale Beschreibung |
| `nodes` | array | Ja | Array von Workflow-Knoten |
| `edges` | array | Ja | Array von Kanten, die Knoten verbinden |

### Knoten-Struktur

Jeder Knoten benoetigt:

| Feld | Typ | Beschreibung |
|-------|------|-------------|
| `node_id` | string | Eindeutige Kennung des Knotens |
| `node_type` | string | Siehe Knotentypen unten |
| `position` | object | `{x: number, y: number}` Position auf der Arbeitsflaeche |
| `label` | string | Anzeigebezeichnung |
| `card` | object | Karten-Konfiguration (erforderlich fuer `when`, `and`, `then` -- siehe unten) |

**Knotentypen:**

| Typ | Karte erforderlich | Zweck |
|------|------------------|---------|
| `start` | Keine Karte | Triggerknoten -- Einstiegspunkt des Workflows |
| `when` | Bedingungskarte | Trigger-Bedingung (ebenfalls gueltiger Einstiegspunkt) |
| `and` | Bedingungskarte | Zusaetzliche Bedingungspruefung nach einem `when` |
| `or` | Keine Karte | Verzweigungsknoten -- faehrt fort, wenn einer der eingehenden Zweige erfolgreich ist |
| `then` | Aktionskarte | Auszufuehrende Aktion |
| `delay` | Keine Karte | Warteknoten -- pausiert die Ausfuehrung fuer eine konfigurierte Dauer |
| `all` | Keine Karte | Sammelknoten -- wartet auf alle eingehenden Zweige |
| `any` | Keine Karte | Sammelknoten -- faehrt mit dem ersten eingehenden Zweig fort |
| `note` | Keine Karte | Notizzettel / Anmerkung; wird nicht ausgefuehrt |

### Kanten-Struktur

Jede Kante benoetigt:

| Feld | Typ | Beschreibung |
|-------|------|-------------|
| `edge_id` | string | Eindeutige Kennung der Kante |
| `source_node_id` | string | ID des Quellknotens |
| `target_node_id` | string | ID des Zielknotens |
| `source_handle` | string | `success`, `error` oder `failed_condition` (optional) |
| `target_handle` | string | `input` (optional) |

**Source-Handles:**

- `success` -- wird genommen, wenn der Quellknoten erfolgreich ist (bei jedem ausfuehrbaren Knoten verfuegbar).
- `failed_condition` -- wird genommen, wenn eine `when`- oder `and`-Bedingungskarte false ergibt.
- `error` -- wird genommen, wenn ein `and`- oder `then`-Knoten einen Fehler ausloest.

### Karten-Konfiguration

Karten definieren, was ein Knoten tut. Verwenden Sie `list_cards` oder `sdk_list_cards_picker`, um verfuegbare Karten abzurufen.

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
Sie muessen pro Karte nur `id`, `card_type`, `version` und `variables` angeben. Der Server reichert die Karten automatisch mit Anzeige-Metadaten (svg, text, category) aus der Datenbank an.
{% endhint %}

**Beispielanfrage:**

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

Einen bestehenden erweiterten Workflow aktualisieren. Sie koennen jede beliebige Kombination aus Name, Beschreibung, Knoten und Kanten aktualisieren.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des zu aktualisierenden Workflows |
| `name` | string | Nein | Neuer Name |
| `description` | string | Nein | Neue Beschreibung |
| `nodes` | array | Nein | Neue Knoten (ersetzt alle bestehenden Knoten) |
| `edges` | array | Nein | Neue Kanten (ersetzt alle bestehenden Kanten) |

## delete\_workflow

Einen Workflow per ID loeschen (Soft-Delete).

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des zu loeschenden Workflows |

## test\_advanced\_workflow

Eine Ausfuehrung eines erweiterten Workflows testen. Optional kann eine Dokument-ID uebergeben werden, um mit einem echten Dokument zu testen.

**Parameter:**

| Parameter | Typ | Erforderlich | Beschreibung |
|-----------|------|----------|-------------|
| `workflow_id` | string | Ja | UUID des erweiterten Workflows |
| `doc_id` | string | Nein | UUID eines Dokuments zum Testen |

## list\_test\_scenarios

Alle Workflow-Testszenarien der Organisation auflisten.

**Parameter:** Keine

## list\_cards

Alle verfuegbaren Workflow-Karten mit ihren Bedingungen und ihrer Konfiguration auflisten.

**Parameter:** Keine

{% hint style="info" %}
Karten haben Rollen-Flags: `when_condition` (Trigger), `and_condition` (zusaetzliche Bedingung) und `then_condition` (Aktion). Anhand dieser Flags koennen Sie bestimmen, in welchen Knotentypen eine Karte verwendet werden kann.
{% endhint %}
