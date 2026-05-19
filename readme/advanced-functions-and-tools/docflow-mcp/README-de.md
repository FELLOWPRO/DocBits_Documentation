# DocFlow MCP

DocFlow stellt einen **Model Context Protocol (MCP)**-Server bereit, mit dem KI-Assistenten Workflows und Partner-Karten programmatisch verwalten koennen. Jeder MCP-kompatible Client -- Claude Code, Claude Desktop, OpenAI Codex oder benutzerdefinierte Integrationen -- kann sich verbinden und diese Tools nutzen.

## Was koennen Sie tun?

Mit DocFlow MCP koennen Sie:

- Erweiterte Workflows **auflisten, erstellen, aktualisieren und loeschen**
- Workflows mit echten oder fiktiven Dokumenten **testen**
- Mit dem Partner Card SDK **eigene Karten erstellen**
- Partner-Karten-Einreichungen **validieren, testen, genehmigen und verwalten**
- Karten direkt aus GitHub-Repositories **importieren**

## Tools-Uebersicht

DocFlow MCP gliedert seine Tools in die folgenden Kategorien. Die meisten Workflow- und Card-SDK-Tools spiegeln vorhandene REST-Endpunkte wider -- die API-Referenz finden Sie dort. Die folgenden Kategorien decken die MCP-spezifische Oberflaeche und die Workflow-Konzepte ab, die Sie zur Nutzung benoetigen.

### Workflow-Verwaltung

| Tool | Beschreibung |
|------|-------------|
| `list_workflows` | Alle Workflows der aktuellen Organisation auflisten |
| `get_workflow` | Details eines bestimmten Workflows per ID abrufen |
| `create_advanced_workflow` | Einen neuen erweiterten Workflow mit Knoten und Kanten erstellen |
| `update_advanced_workflow` | Einen bestehenden erweiterten Workflow aktualisieren |
| `delete_workflow` | Einen Workflow per ID loeschen |

### Workflow-Tests

| Tool | Beschreibung |
|------|-------------|
| `test_advanced_workflow` | Eine Ausfuehrung eines erweiterten Workflows testen, optional mit Dokument |
| `list_test_scenarios` | Alle Workflow-Testszenarien auflisten |
| `list_cards` | Verfuegbare Workflow-Karten / -Aktionen auflisten |

### Card-SDK-Verwaltung

| Tool | Beschreibung |
|------|-------------|
| `sdk_list_submissions` | Alle Partner-Karten-Einreichungen auflisten |
| `sdk_get_submission_status` | Validierungsstatus einer Einreichung abrufen |
| `sdk_approve_card` | Eine validierte Partner-Karte genehmigen (Admin) |
| `sdk_reject_card` | Eine Partner-Karten-Einreichung ablehnen (Admin) |
| `sdk_delete_submission` | Eine Einreichung deaktivieren oder loeschen (Admin) |
| `sdk_list_cards_picker` | Alle aktivierten Karten mit Rollen-Flags auflisten |

### Card-SDK-Entwicklung

| Tool | Beschreibung |
|------|-------------|
| `sdk_create_card` | Eine neue Partner-Karte aus Quellcode erstellen |
| `sdk_validate_card` | Die Validierungs-Pipeline ohne Speichern ausfuehren |
| `sdk_test_card` | Eine Karte in einer Sandbox ausfuehren |
| `sdk_import_github` | Eine Partner-App aus GitHub importieren |

## Erste Schritte

1. [MCP-Client einrichten](setup-and-configuration.md)
2. [Workflow Tools](workflow-tools.md) kennenlernen
3. [Card SDK Tools](card-sdk-tools.md) erkunden
4. End-to-End-[Beispiele](examples.md) durchgehen

{% hint style="info" %}
DocFlow MCP nutzt den Transport **Streamable HTTP**. Der Server-Endpunkt ist `/v3/mcp/` auf dem DocFlow-Host (z.B. `https://docflow.docbits.com/v3/mcp/`). Die vollstaendige URL-Liste finden Sie unter [Einrichtung & Konfiguration](setup-and-configuration.md).
{% endhint %}
