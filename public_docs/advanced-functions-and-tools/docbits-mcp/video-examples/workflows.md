---
description: Plan an invoice workflow with Claude, choose the cards and understand what the tests check.
---

# Workflow planning with Claude

Describe the invoice process you want to automate, including what should happen when a value is missing or a step fails. Claude can help you choose the cards and work through the routing before you build it in DocBits.

## Design Your Workflow · Berlin

In the Berlin preview, Claude helps design an invoice workflow with a review route and an error route. The developer checks a custom condition with eight unit tests, then reviews the routing in the DocBits Workflow Builder.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflow-design-office-preview-admin/v4/en.mp4" %}

[Watch with English captions](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflow-design-office-preview-admin/v4/en.html)

> Help me design an invoice workflow. Route invoices with a total above 1,000 for review, process totals up to 1,000 normally, and send invalid values to a correction route. Explain which cards to use and how to test the conditions. Then help me check the routing in DocBits before I activate it.

The DocBits view is a draft built with standard cards. The eight unit tests cover the custom condition's decision logic. Review and install that condition separately if you want to use it in your workflow.

## Workflow planning: explainer

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflows-feature/v1/en.mp4" %}

[Open the video player](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflows-feature/v1/en.html)

## Try this question

> Help me plan an invoice workflow. Check the total and route invoices above 1,000 for review. Explain which cards I need before we build it.

Then ask:

> Explain this test result. Which condition matched? What did the action do, and what should I test next?

The walkthrough uses a card lookup and a recorded test result. Build the workflow in your environment and test its routes before you activate it.

## Continue in the documentation

- [Workflows & Cards with DocFlow MCP](../docflow-mcp/README.md)
- [Workflow tools](../docflow-mcp/workflow-tools.md)
- [Card SDK tools for developers](../docflow-mcp/card-sdk-tools.md)
- [See all video examples](README.md)
