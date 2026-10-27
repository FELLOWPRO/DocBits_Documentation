# Connect AI Workforce to Teams and Discord

You need an active **AI Workforce** subscription, permission to manage connections and access to the intended Teams tenant or Discord server. If DocBits shows a subscription requirement, arrange activation with your administrator first.

## Microsoft Teams

1. Open **AI Workforce → Settings → Integrations**.
2. Choose **+ → Connect Teams**. DocBits generates a connection code and displays its remaining lifetime.
3. Follow the instruction shown with that code in the intended Teams environment. Keep the code private and complete the association before it expires.
4. Wait for the connected confirmation. Check the new connection's name and **Shared** or **Custom** bot mode in the list.
5. If inactive, use **Activate** when the connection should receive work. Stored and active are different states.
6. Send a harmless test request from the intended Teams context. Find its mission in DocBits, verify source and organization, and complete any required human approval in the Inbox.

For a company-managed bot, choose **Add custom bot** instead. Enter its connection name, tenant ID, app ID and app secret. Keep secrets in the credential form, outside prompts and screenshots.

## Discord

1. Under **Integrations**, choose **+ → Connect Discord**.
2. If offered, use **Add bot to Discord** with an authorized server administrator.
3. Enter a recognizable **Name** and the correct **Guild ID**. This identifies the server, not a channel.
4. Choose **Create**, inspect the resulting connection and activate it if necessary.
5. Send a harmless request through the configured server context. Verify the resulting mission, source and organization in DocBits.

## Troubleshoot

For an expired Teams code, generate a fresh one and follow its new instruction. For a connection receiving no work, check activation, tenant/server identity, bot access and errors. A connected indicator does not establish a completed agent mission.

See [AI Workforce](ai_workforce.md) for missions, agent permissions and approvals. Chat connections are separate from email import and Microsoft sign-in configuration.
