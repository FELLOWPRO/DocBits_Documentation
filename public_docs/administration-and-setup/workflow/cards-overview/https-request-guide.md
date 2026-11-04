# Send HTTPS Request

***

Add this card to the **Then** group of the Workflow Builder — the actions that run once the When/And conditions match:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder canvas with When, And and Then card groups"><figcaption><p>The <strong>Send HTTPS Request</strong> card is added to the <strong>Then</strong> group via <strong>Add Card</strong>.</p></figcaption></figure>

***

## 📌 Version Information

**Current Version:** v2 (Latest & Recommended) **Status:** ✅ Active

**Version History:**

* v1 → Simple HTTP request (no longer recommended)
* **v2 → CURRENT** (added multi-language support)

**What Changed:** v2 added internationalization (i18n) support. Core webhook/request functionality remains unchanged.

📖 [Version History & Changes](../release.md) | [Complete Card Database](export-cards-guide.md)

***

## Purpose

The HTTPS request card uses a configured HTTPS URL and its own headers. `call_api` uses a relative DocBits API path and the current DocBits user context; its result is derived from response text. Choose by endpoint and response contract, not by a simple-versus-complex API distinction.

## When to Use This Card

Use this card when you need to:

* Send webhook notifications to external services
* Trigger actions in other systems
* Query a simple web service
* Send status updates to other applications
* Perform simple integrations without complex API requirements

***

## How It Works

1. **Trigger Check**: System checks if the "When" and "And" conditions are met
2. **Build Request**: System prepares the HTTPS request with your parameters
3. **Send Securely**: Data is sent using secure HTTPS connection
4. **Receive Response**: External service responds
5. **Continue**: Workflow proceeds with the response data

***

## Parameters

### URL

The website address to send the request to

**Example:** `https://webhook.company.com/process`

### Headers

Special instructions for the recipient

**Example:**

```
Content-Type: application/json
Authorization: Bearer token123
```

### Method

* **GET**: Request information
* **POST**: Send data
* **PUT**: Update data

### Parameters (Query String)

Data added to the URL

**Example:** `?action=approve&user_id=123`

### Request Data

The actual information being sent (in JSON format)

**Example:**

```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

***

## Step-by-Step Example

### Scenario: Send Invoice to Accounting System

**Card Configuration:**

* **URL:** `https://accounting.company.com/invoices/create`
* **Method:** POST
* **Headers:** `Authorization: Bearer YOUR-TOKEN`
* **Request Data:**

```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Expected Response:**

```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

***

## Common Use Cases

### 1. Webhook Notifications

Send real-time notifications to other systems whenever something happens in DocFlow

**Example:**

* Document approved → Send notification to fulfillment system
* Supplier changed → Notify purchasing team via Slack/Teams webhook

### 2. External System Integration

Connect DocFlow with other business systems for automatic data exchange

**Example:**

* After document is processed → Sync to ERP system
* New supplier added → Create supplier record in master data system

### 3. Approval Workflows

Send document to external approval system and receive decision

**Example:**

* High-value invoice → Send to Finance for approval
* Return document to external system with decision

***

## Configuration Guide

### Step 1: Get Endpoint Information

Ask the receiving system for:

* [ ] HTTPS URL
* [ ] Required headers
* [ ] Authentication method
* [ ] Expected request format
* [ ] Expected response format

### Step 2: Configure the Card

1. Enter the HTTPS URL
2. Set HTTP method (usually POST)
3. Add authentication if required
4. Format request data as JSON
5. Add any custom headers

### Step 3: Test

Send a test request and verify response

***

## Response Handling

Your HTTPS request will get a response. Common responses:

### Success (200, 201)

```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Bad Request (400)

```json
{
  "error": "Missing required field: invoice_number"
}
```

### Unauthorized (401)

```json
{
  "error": "Invalid authentication token"
}
```

### Server Error (500)

The receiving system has an internal problem

***

## Troubleshooting

### "Certificate Error"

**Cause:** HTTPS security certificate issue

**Solution:**

* Verify the URL is correct
* Check if the website's certificate is valid
* Ensure you're using HTTPS (not HTTP)

### "Connection Refused"

**Cause:** Cannot connect to the server

**Solution:**

* Verify the URL/IP address is correct
* Check if the service is running
* Check firewall rules
* Verify internet connectivity

### "No Response / Timeout"

**Cause:** Server not responding within time limit

**Solution:**

* Check if the service is available
* Verify the endpoint URL
* Check if there are rate limits
* Contact system administrator

### "Invalid JSON"

**Cause:** The request data is malformed

**Solution:**

* Check for missing commas in JSON
* Verify all quotes are correct
* Validate JSON format (use online JSON validator)
* Check for special characters

***

## Examples

### Example 1: Send to Webhook Service

```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Example 2: Update External System

```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Example 3: Query External Service

```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

***

## Difference from "Call API" Card

The HTTPS request card uses a configured HTTPS URL and its own headers. `call_api` uses a relative DocBits API path and the current DocBits user context; its result is derived from response text. Choose by endpoint and response contract, not by a simple-versus-complex API distinction.

***

## Security Considerations

✅ **Always use HTTPS** (secure connection)

⚠️ **Never:**

* Put passwords in the URL
* Expose API keys in logs
* Include personal data in parameters
* Use HTTP for sensitive data

***

## Best Practices

✅ **Do:**

* Test with small amounts of data first
* Include error handling
* Log important requests
* Document the integration
* Monitor for failures

❌ **Don't:**

* Call the same endpoint repeatedly if not needed
* Ignore response errors
* Include sensitive data in plain text
* Exceed service rate limits

***

## Related Cards

* **CALL\_API** - More advanced API integration
* **CONDITION\_HTTPS\_REQUEST\_STATUS** - Check if request succeeded
* **ACTION\_SEND\_EMAIL** - Send via email instead
* **ACTION\_RUN\_DOCOPERATOR\_SCRIPT** - Automated scripts

<!-- workflow-card-complete-example-20261021 action_https_request -->

### HTTPS action example

**Configuration:** Select method `POST`, replace `DEMO_WEBHOOK_URL` with your authorized test endpoint, add header `Content-Type: application/json` and body `{"document_number":"DEMO-001"}`. Configure authentication only as required by that endpoint; never copy a real secret into documentation.

**Expected result and counterexample:** The action sends the configured request when its workflow route executes. Inspect the HTTP response and receiving test service. A timeout is not proof that the service did nothing, and this Then action is separate from the And card that checks an HTTP status. This illustrative request has not been sent.

This is an illustrative test configuration and expected outcome; it was not executed. Use data and recipients configured in your test organization.
