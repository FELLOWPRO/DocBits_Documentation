# DocFlow MCP

DocFlow biedt een **Model Context Protocol (MCP)**-server waarmee AI-assistenten workflows en partnerkaarten programmatisch kunnen beheren. Elke MCP-compatibele client — Claude Code, Claude Desktop, OpenAI Codex of aangepaste integraties — kan verbinding maken en deze tools gebruiken.

## Wat kunt u doen?

Met DocFlow MCP kunt u:

- **Geavanceerde workflows** weergeven, aanmaken, bijwerken en verwijderen
- **Workflows testen** met echte of gesimuleerde documenten
- **Aangepaste kaarten bouwen** met de Partner Card SDK
- **Partnerkaartinzendingen** valideren, testen, goedkeuren en beheren
- **Kaarten importeren** rechtstreeks vanuit GitHub-repositories

## Overzicht van tools

DocFlow MCP biedt **18 tools** verdeeld over vier categorieën:

### Workflowbeheer

| Tool | Beschrijving |
|------|-------------|
| `list_workflows` | Alle workflows van de huidige organisatie weergeven |
| `get_workflow` | Details van een specifieke workflow ophalen op basis van ID |
| `delete_workflow` | Een workflow verwijderen op basis van ID |

### Workflow testen

| Tool | Beschrijving |
|------|-------------|
| `test_advanced_workflow` | Een geavanceerde workflow-uitvoering testen met optioneel document |
| `list_test_scenarios` | Alle testscenario's voor workflows weergeven |
| `list_cards` | Beschikbare workflowkaarten/acties weergeven |

### Card SDK-beheer

| Tool | Beschrijving |
|------|-------------|
| `sdk_list_submissions` | Alle partnerkaartinzendingen weergeven |
| `sdk_get_submission_status` | Validatiestatus van een inzending ophalen |
| `sdk_approve_card` | Een gevalideerde partnerkaart goedkeuren (admin) |
| `sdk_reject_card` | Een partnerkaartinzending afwijzen (admin) |
| `sdk_delete_submission` | Een inzending deactiveren of verwijderen (admin) |
| `sdk_list_cards_picker` | Alle ingeschakelde kaarten met rolvlaggen weergeven |

### Card SDK-ontwikkeling

| Tool | Beschrijving |
|------|-------------|
| `sdk_create_card` | Een nieuwe partnerkaart aanmaken vanuit broncode |
| `sdk_validate_card` | 5-fasen validatie uitvoeren zonder op te slaan |
| `sdk_test_card` | Een kaart uitvoeren in een sandboxomgeving |
| `sdk_import_github` | Een partnerapp importeren vanuit GitHub |

## Aan de slag

1. [Stel uw MCP-client in](setup-and-configuration.md)
2. Leer over [Workflow Tools](workflow-tools.md)
3. Ontdek de [Card SDK Tools](card-sdk-tools.md)
4. Volg de volledige [Voorbeelden](examples.md)

{% hint style="info" %}
DocFlow MCP gebruikt **Streamable HTTP**-transport. Het servereindpunt is `/api/mcp/` op uw DocBits API-host.
{% endhint %}
