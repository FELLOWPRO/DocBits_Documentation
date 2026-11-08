---
description: Use Claude and DocBits MCP to design an invoice workflow, choose its cards and test the decisions before activation.
---

# Design workflows with Claude

Describe the process you want to automate and work through it with Claude. You can choose what starts the workflow, decide which invoices need review and plan what should happen when data is missing. Then build the flow in DocBits and check the result.

## Design Your Workflow · Berlin

Start with a rule you already use in your business. Here, invoices above 1,000 go for review, while totals of 1,000 or less follow the standard route. Claude helps explain the decisions and test a custom condition. You can then inspect the connected flow in the DocBits Workflow Builder.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflow-design-office-preview-admin/v4/en.mp4" %}

[Watch with English captions](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflow-design-office-preview-admin/v4/en.html)

> Help me design an invoice workflow. Route invoices with a total above 1,000 for review, process totals up to 1,000 normally, and send invalid values to a correction route. Explain which cards to use and how to test the conditions. Then help me check the routing in DocBits before I activate it.

The eight tests in the video cover the custom condition. The workflow shown in DocBits is a draft built with standard cards. Review and install the custom card separately, and test the full process in your environment before activation.

## Workflow planning: explainer

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflows-feature/v1/en.mp4" %}

[Open the video player](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflows-feature/v1/en.html)

## Try this question

> Help me plan an invoice workflow. Check the total and route invoices above 1,000 for review. Explain which cards I need before we build it.

Then ask:

> Explain this test result. Which condition matched? What did the action do, and what should I test next?

Ask Claude to explain a test result when a route behaves differently from what you expected. The recorded walkthrough uses a card lookup and a test result as an example.

## Continue in the documentation

- [Workflows & Cards with DocFlow MCP](../docflow-mcp/README.md)
- [Workflow tools](../docflow-mcp/workflow-tools.md)
- [Card SDK tools for developers](../docflow-mcp/card-sdk-tools.md)
- [See all video examples](README.md)
