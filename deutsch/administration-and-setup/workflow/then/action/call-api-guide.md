# Call External API

Diese Karten gehören in die **Then**-Gruppe des Workflow-Builders – die Aktionen, die ausgeführt werden, sobald die When-/And-Bedingungen zutreffen:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karten werden über <strong>Add Card</strong> zur <strong>Then</strong>-Gruppe hinzugefügt.</p></figcaption></figure>

## Purpose
This card allows you to send data to an external website or service and receive information back. Think of it like sending a question to an external service and getting an answer that you can use in your workflow.

**Real-world example:** Your company uses a pricing system on another website. This card can automatically ask that pricing system for the current price of an item and bring that price into your document.

---

## When to Use This Card

Use this card when you need to:
- Get information from an external service (like pricing, validation, or lookup data)
- Send document information to another system for processing
- Integrate with third-party services
- Automatically fetch data without manual lookups
- Connect multiple business systems together

**Common scenarios:**
- Look up supplier information from a database
- Get real-time pricing from a pricing service
- Validate data against an external system
- Fetch shipping information from a logistics provider

---

## How It Works

1. **Condition Check**: The workflow first checks if the conditions in "Where" and "And" sections are met
2. **Prepare Data**: The card collects the parameters you've configured
3. **Send Request**: It sends your data to the external API/service
4. **Receive Response**: The external service responds with data
5. **Continue**: The workflow uses this data in subsequent cards

---

## Parameters Explained

### API Endpoint URL
**What it is:** The address of the external service you want to communicate with

**Example:** `https://api.supplier-system.com/product/pricing`

**How to find it:** Ask your IT team or the service provider for their API endpoint

---

### HTTP Method
**What it is:** The type of request to send

**Options:**
- **GET**: Request information (like asking a question)
- **POST**: Send new data
- **PUT**: Update existing data
- **DELETE**: Remove data

**Most common:** GET (for fetching information)

---

### Headers
**What it is:** Additional instructions for the service you're calling

**Example:**
```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Why it's needed:** Services often require authentication or specific format instructions

---

### Parameters (Query Parameters)
**What it is:** Extra information passed in the URL

**Example:**
```
?supplier_id=12345&currency=USD
```

**Real example:** If you're asking for prices, parameters might include the supplier ID and currency

---

### Request Data (Body)
**What it is:** The information you're sending to the service

**Example:**
```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**When used:** When using POST or PUT methods

---

## Step-by-Step Example

### Scenario: Get Real-Time Supplier Pricing

**Setup:**
1. **Card Type:** Call API
2. **API Endpoint:** `https://api.suppliers.com/v1/prices`
3. **Method:** POST
4. **Headers:** `Authorization: Bearer YOUR-API-KEY`
5. **Request Data:**
   ```json
   {
     "product_id": "ABC123",
     "quantity": 100
   }
   ```

**What happens:**
1. Document arrives with Product ID: ABC123, Quantity: 100
2. Card sends request to supplier's API
3. Supplier's API responds with: `{"unit_price": 25.50, "total_price": 2550}`
4. Workflow continues with this pricing information
5. Next card can use this data to validate the invoice price

---

## Configuration Steps

### 1. Get API Information
Contact the external service provider and request:
- [ ] API endpoint URL
- [ ] Authentication method (API key, username/password, OAuth)
- [ ] Required parameters
- [ ] Expected response format
- [ ] Rate limits or quotas

### 2. Configure the Card
1. Enter the API endpoint URL
2. Select the HTTP method (usually GET or POST)
3. Add authentication headers if required
4. Add any required parameters
5. Format request data as JSON if needed

### 3. Test the Card
1. Use a test document
2. Run the workflow
3. Check if the response is received correctly
4. Verify the data format matches expectations

---

## Common Response Scenarios

### Successful Response (Status Code 200)
```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```
✅ Data is available for next cards to use

### Error Response (Status Code 404)
```json
{
  "error": "Product not found"
}
```
⚠️ The API couldn't find what you're looking for

### Timeout
The external service didn't respond within the time limit
⚠️ Check if the service is available or if the endpoint URL is correct

---

## Example Workflows

### Example 1: Automatic Price Validation
**Scenario:** Validate invoice prices against supplier's current pricing

**Flow:**
1. Document arrives with invoice line item (Product: A123, Price: €50)
2. **Call API Card** → Asks supplier API: "What's the current price for A123?"
3. Supplier responds: "€48"
4. **Condition Card** → Checks if invoice price (€50) is within 5% of current price (€48)
5. **Approval Card** → Approves if within tolerance

### Example 2: Automatic Supplier Lookup
**Scenario:** Get supplier master data from central database

**Flow:**
1. Invoice arrives with Supplier Code: SUPP-789
2. **Call API Card** → Asks system: "Give me details for supplier SUPP-789"
3. System responds with: Name, Contact, Terms, etc.
4. **Set Field Cards** → Populate document fields with this data
5. **Export Card** → Export with complete information

### Example 3: Real-Time Shipping Costs
**Scenario:** Get automatic shipping cost based on destination

**Flow:**
1. Document has delivery address
2. **Call API Card** → Ask shipping provider: "What's the cost to [address]?"
3. Provider responds with shipping cost
4. **Calculate Card** → Add shipping to total invoice amount
5. **Export Card** → Send with updated total

---

## Troubleshooting

### "Connection Timeout" Error
**Cause:** The API service is not responding

**Solutions:**
- [ ] Check if the service is available (visit the website)
- [ ] Verify the endpoint URL is correct (no typos)
- [ ] Check internet connection
- [ ] Contact the service provider
- [ ] Check if the service has rate limits (you're sending too many requests)

### "Unauthorized" or "403 Forbidden" Error
**Cause:** Authentication failed

**Solutions:**
- [ ] Verify your API key is correct
- [ ] Check if your API key has expired
- [ ] Ensure authentication header is formatted correctly
- [ ] Verify you have permissions for this endpoint

### "Bad Request" or "400 Error"
**Cause:** The request data format is incorrect

**Solutions:**
- [ ] Check JSON syntax (missing commas, quotes, etc.)
- [ ] Verify all required fields are included
- [ ] Check parameter names match what the service expects
- [ ] Consult the API documentation

### "Response not working as expected"
**Solutions:**
- [ ] Test the API using a tool like Postman
- [ ] Compare actual response format with expected format
- [ ] Check if the API's documentation changed
- [ ] Verify the data you're sending is correct

---

## Response Data Usage

Once you get data back from the API, the next cards can use it:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

---

## Security Notes

⚠️ **Important:** Never put sensitive information in the card configuration that might be visible to other users

- Don't hardcode passwords
- Use API keys securely
- Don't include personal data in logs
- Use HTTPS endpoints (not HTTP)

---

## Tips & Best Practices

✅ **Do:**
- Test with a small sample of documents first
- Keep API calls simple and focused
- Add error handling with Condition cards
- Monitor API usage/costs
- Document the API requirements for your team

❌ **Don't:**
- Call APIs for every single request if you can cache data
- Ignore response error codes
- Use test APIs in production
- Forget to add authentication headers
- Assume the API will always be available

---

## Related Cards

- **ACTION_HTTPS_REQUEST** - Similar but simpler HTTPS requests
- **CONDITION_HTTPS_REQUEST_STATUS** - Check if API call was successful
- **ACTION_SEND_EMAIL** - Send data via email instead of API
- **CALL_API** (different version) - Alternative API call method

---

## Need Help?

- Ask your IT/Integration team for API documentation
- Use Postman tool to test API endpoints first
- Check the service provider's support portal
- Review API documentation for required formats

