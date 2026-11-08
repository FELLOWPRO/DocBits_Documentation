---
description: Connect DocBits to Claude to ask about your synced ERP data, compare orders with deliveries and invoices, and create charts and reports.
---

# Your ERP data in Claude

Connect DocBits to Claude and ask about the data synced from your ERP system. You can compare an order with its delivery notes and invoices, find out why quantities differ, and ask Claude to show the results in a chart.

## Connect DocBits to Claude

1. Add DocBits MCP as a custom connector in Claude. [Quick Connect](../quick-connect.md) lists the endpoint for your region and environment. On a company Claude account, your administrator may need to add the connector first.
2. Connect with your DocBits login and approve access.
3. Start a new chat with the DocBits connector enabled. Ask Claude which data it can read, then try a question about an order you know.

Claude uses your DocBits account's permissions. The ERP records you can ask about are the ones available in DocBits.

## ERP Insights · London

Start with a purchase order and ask Claude to check it against the delivery notes and invoices. You can follow up on any difference in the same conversation and ask which documents it used.

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-erp-insights-office-preview-admin/v4/en.mp4" %}

[Watch with English captions](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-erp-insights-office-preview-admin/v4/en.html)

> Compare purchase order [number] with its delivery notes and invoices. Show the quantities for each line in a chart and explain any differences. Keep different units separate and list the documents you compared.

## Look for recurring supplier problems

You can ask about a pattern across orders, too:

> Which suppliers repeatedly delivered less than we ordered? Compare the orders with the delivery records and invoices. Show the differences by supplier and list the records I should check.

If your records include agreed delivery dates and actual receipt dates, try:

> Which suppliers delivered after the agreed date? Show the late deliveries in a chart. List any records where dates are missing so I know what you could not verify.

## Infor insights and morning briefings: explainer

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-infor-insights-feature/v1/en.mp4" %}

[Open the video player](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/mcp-infor-insights-feature/v1/en.html)

## Try this question

> Which Infor export problems should I look at first? Group the responses stored in DocBits by reason and show them in a chart. Tell me what to do next and include when the data was recorded.

Check when the data was last recorded or synced before you act on the result.

## Make the briefing a routine

Once you have a report you like, you can use the same questions for a daily briefing:

> Prepare a weekday briefing at 08:00 in [timezone]. Include quantity differences, late deliveries you can verify and the invoices I should review first. Add charts and list the documents behind each issue.

Use [Claude's scheduled tasks](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork) in a supported Cowork or Claude account to set this up. Review the proposed schedule, timezone and DocBits access before saving it. 08:00 is the planned start time; the finished report may arrive later.

## Continue in the documentation

- [Analytics and reporting prompts](../examples.md#analytics-and-reporting)
- [Connect DocBits MCP](../setup-and-configuration.md)
- [See all video examples](README.md)
