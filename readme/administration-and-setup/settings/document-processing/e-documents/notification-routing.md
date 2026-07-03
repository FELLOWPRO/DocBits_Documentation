# Notification Routing

<figure><img src="../../../../.gitbook/assets/edoc_notification_routing.png" alt="Notification routes"><figcaption><p>Mapping validation findings to agents</p></figcaption></figure>

The **Notification Routing** page (**E-Documents → Actions**) maps validation findings to **AI Workforce agents**. Each blocking finding triggers exactly one agent — the one whose code-prefix matches the longest. Anything with no match falls back to the default supplier-notification agent.

## Notification Routes

Choose who handles each kind of invoice problem. Anything not listed goes to the default agent:

| Route                          | Findings it covers                                      |
| ------------------------------ | ------------------------------------------------------- |
| **Colombian business rules**   | Colombia-specific business-rule findings.               |
| **German business rules**      | Germany-specific business-rule findings.                |
| **IBAN / bank-account checks** | Payment-data findings (IBAN checksum, length, country). |
| **VAT-ID checks**              | VAT/tax-ID format findings.                             |
| **Everything else**            | The default fallback for anything not matched above.    |

For each route, pick the handling agent from the dropdown. **Advanced (custom code rules)** lets you route by an exact finding code when you need finer control.

## Available Agents

<figure><img src="../../../../.gitbook/assets/due_date_calc_formats.png" alt="Available agents registry"><figcaption><p>Read-only registry of AI Workforce agents</p></figcaption></figure>

The **Available Agents** section is a read-only registry of the AI Workforce agents shipped with your deployment, for example:

| Agent                             | Purpose                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------- |
| **Default supplier notification** | Generic supplier-notification email; the catch-all when no more specific agent matches. |
| **Banking Bot**                   | Specialised template for payment-data findings (IBAN/BIC corrections).                  |
| **Tax Bot**                       | VAT/tax-ID specific supplier notification.                                              |
| **Compliance Bot**                | Handles compliance findings.                                                            |

Each agent shows its Celery task and the finding-code prefixes it handles by default.
