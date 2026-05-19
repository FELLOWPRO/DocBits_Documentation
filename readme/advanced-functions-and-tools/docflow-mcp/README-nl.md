# DocFlow MCP

DocFlow biedt een **Model Context Protocol (MCP)**-server waarmee AI-assistenten workflows en partnerkaarten programmatisch kunnen beheren. Elke MCP-compatibele client — Claude Code, Claude Desktop, OpenAI Codex of aangepaste integraties — kan verbinding maken en deze tools gebruiken.

## Wat kunt u doen?

Met DocFlow MCP kunt u:

- Geavanceerde workflows **opvragen, aanmaken, bijwerken en verwijderen**
- Workflows **testen** met echte of fictieve documenten
- **Eigen kaarten bouwen** met de Partner Card SDK
- Inzendingen van partnerkaarten **valideren, testen, goedkeuren en beheren**
- Kaarten rechtstreeks **importeren** vanuit GitHub-repositories

## Tools-overzicht

DocFlow MCP groepeert zijn tools in de volgende categorieën. De meeste workflow- en Card SDK-tools weerspiegelen bestaande REST-endpoints — raadpleeg daar de API-referentie. De categorieën hieronder behandelen het MCP-specifieke oppervlak en de workflow-concepten die u nodig hebt om het te gebruiken.

### Workflowbeheer

| Tool | Beschrijving |
|------|-------------|
| `list_workflows` | Alle workflows van de huidige organisatie opvragen |
| `get_workflow` | Details van een specifieke workflow opvragen op ID |
| `create_advanced_workflow` | Een nieuwe geavanceerde workflow met knopen en kanten aanmaken |
| `update_advanced_workflow` | Een bestaande geavanceerde workflow bijwerken |
| `delete_workflow` | Een workflow verwijderen op ID |

### Workflowtesten

| Tool | Beschrijving |
|------|-------------|
| `test_advanced_workflow` | Een uitvoering van een geavanceerde workflow testen, optioneel met document |
| `list_test_scenarios` | Alle workflow-testscenario's opvragen |
| `list_cards` | Beschikbare workflow-kaarten / -acties opvragen |

### Card SDK-beheer

| Tool | Beschrijving |
|------|-------------|
| `sdk_list_submissions` | Alle inzendingen van partnerkaarten opvragen |
| `sdk_get_submission_status` | Validatiestatus van een inzending opvragen |
| `sdk_approve_card` | Een gevalideerde partnerkaart goedkeuren (admin) |
| `sdk_reject_card` | Een inzending van een partnerkaart afwijzen (admin) |
| `sdk_delete_submission` | Een inzending uitschakelen of verwijderen (admin) |
| `sdk_list_cards_picker` | Alle ingeschakelde kaarten met rolvlaggen opvragen |

### Card SDK-ontwikkeling

| Tool | Beschrijving |
|------|-------------|
| `sdk_create_card` | Een nieuwe partnerkaart aanmaken vanuit broncode |
| `sdk_validate_card` | De validatie-pipeline uitvoeren zonder op te slaan |
| `sdk_test_card` | Een kaart uitvoeren in een sandbox-omgeving |
| `sdk_import_github` | Een partner-app importeren vanuit GitHub |

## Aan de slag

1. [Stel uw MCP-client in](setup-and-configuration.md)
2. Leer over [Workflow Tools](workflow-tools.md)
3. Verken de [Card SDK Tools](card-sdk-tools.md)
4. Volg de end-to-end-[voorbeelden](examples.md)

{% hint style="info" %}
DocFlow MCP gebruikt het transport **Streamable HTTP**. Het server-endpoint is `/v3/mcp/` op de DocFlow-host (bijv. `https://docflow.docbits.com/v3/mcp/`). Zie [Installatie en configuratie](setup-and-configuration.md) voor de volledige URL-lijst.
{% endhint %}
