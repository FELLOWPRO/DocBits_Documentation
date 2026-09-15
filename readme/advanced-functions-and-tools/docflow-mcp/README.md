# DocFlow MCP

DocFlow stellt einen **Model Context Protocol (MCP)**-Server bereit, mit dem KI-Assistenten Workflows und Partner-Karten programmatisch verwalten koennen. Jeder MCP-kompatible Client -- Claude Code, Claude Desktop, OpenAI Codex oder benutzerdefinierte Integrationen -- kann sich verbinden und diese Tools nutzen.

## Was koennen Sie tun?

Mit DocFlow MCP koennen Sie:

- **Erweiterte Workflows auflisten, erstellen, aktualisieren und loeschen**
- **Workflows testen** mit echten oder simulierten Dokumenten
- **Benutzerdefinierte Karten erstellen** mit dem Partner Card SDK
- **Partner-Karten-Einreichungen validieren, testen, genehmigen und verwalten**
- **Karten importieren** direkt aus GitHub-Repositories

## Tools-Uebersicht

DocFlow MCP bietet **18 Tools** in vier Kategorien:

### Workflow-Verwaltung

| Tool | Beschreibung |
|------|-------------|
| `list_workflows` | Alle Workflows der aktuellen Organisation auflisten |
| `get_workflow` | Details eines bestimmten Workflows anhand der ID abrufen |
| `delete_workflow` | Einen Workflow anhand der ID loeschen |

### Workflow-Tests

| Tool | Beschreibung |
|------|-------------|
| `test_advanced_workflow` | Einen erweiterten Workflow mit optionalem Dokument testen |
| `list_test_scenarios` | Alle Workflow-Testszenarien auflisten |
| `list_cards` | Verfuegbare Workflow-Karten/Aktionen auflisten |

### Card SDK Verwaltung

| Tool | Beschreibung |
|------|-------------|
| `sdk_list_submissions` | Alle Partner-Karten-Einreichungen auflisten |
| `sdk_get_submission_status` | Validierungsstatus einer Einreichung abrufen |
| `sdk_approve_card` | Eine validierte Partner-Karte genehmigen (Admin) |
| `sdk_reject_card` | Eine Partner-Karten-Einreichung ablehnen (Admin) |
| `sdk_delete_submission` | Eine Einreichung deaktivieren oder loeschen (Admin) |
| `sdk_list_cards_picker` | Alle aktivierten Karten mit Rollen-Flags auflisten |

### Card SDK Entwicklung

| Tool | Beschreibung |
|------|-------------|
| `sdk_create_card` | Eine neue Partner-Karte aus Quellcode erstellen |
| `sdk_validate_card` | 5-stufige Validierung ohne Speichern ausfuehren |
| `sdk_test_card` | Eine Karte in einer Sandbox-Umgebung ausfuehren |
| `sdk_import_github` | Eine Partner-App von GitHub importieren |

## Erste Schritte

1. [Richten Sie Ihren MCP-Client ein](setup-and-configuration.md)
2. Erfahren Sie mehr ueber [Workflow-Tools](workflow-tools.md)
3. Entdecken Sie die [Card SDK Tools](card-sdk-tools.md)
4. Folgen Sie den End-to-End-[Beispielen](examples.md)

{% hint style="info" %}
DocFlow MCP verwendet **Streamable HTTP**-Transport. Der Server-Endpunkt ist `/api/mcp/` auf Ihrem DocBits-API-Host.
{% endhint %}
