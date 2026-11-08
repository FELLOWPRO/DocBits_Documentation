---
description: Use Claude to find workflow building blocks, plan conditions, and explain recorded test results.
---

# Workflow planning with Claude

Describe the process you want to automate. Ask Claude to help find the building blocks and make the logic easier to review.

## Design Your Workflow · Berlin

English office video preview. Start with the complete invoice process in Claude: the trigger, amount decision, review route, standard processing and error handling. Inspect eight custom-card unit tests, then review the routing draft in the actual DocBits Workflow Builder.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflow-design-office-preview-admin/v4/en.mp4" %}

[Watch with English captions](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflow-design-office-preview-admin/v4/en.html)

> Design an invoice workflow with review above 1,000, standard processing at or below 1,000, and a correction route for invalid inputs. Explain the available cards, test the decision logic, and help me review the routing in DocBits before activation.

The native designer view uses available standard cards. The custom condition is demonstrated separately through unit tests; those tests do not install or approve the card for a workflow. The illustrated workflow remains a draft.

## Workflow planning: explainer

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflows-feature/v1/en.mp4" %}

[Open the video player](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-workflows-feature/v1/en.html)

## Try this question

> Help me plan an invoice workflow: check the total, route amounts over 1,000 for review, and explain the available cards before we build it.

Then ask:

> Explain this test result. Which condition matched, which action ran, and what should I test next?

The film combines an available-card lookup with a labelled recorded test example. The workflow plan still needs to be built and tested in your environment.

## Continue in the documentation

- [Workflows & Cards with DocFlow MCP](../docflow-mcp/README.md)
- [Workflow tools](../docflow-mcp/workflow-tools.md)
- [Card SDK tools for developers](../docflow-mcp/card-sdk-tools.md)
- [See all video examples](README.md)
