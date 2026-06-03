# API Integration Pattern

**Pattern Type:** Integration
**Complexity:** Medium
**Estimated Setup:** 45-60 minutes
**Common Use Cases:** External data fetching, pricing validation, master data lookup

---

You build this pattern in the **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Click **Add Card** to open the card library and pick the cards this pattern uses — `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` and `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card library in the Workflow Builder, grouped by category"><figcaption><p>The <strong>Add Card</strong> library — pick the API, condition and field cards used by this pattern from these categories.</p></figcaption></figure>

---

## Pattern Overview

This pattern demonstrates how to integrate DocBits with external APIs to fetch, validate, and store data from external systems. It's one of the most common workflow patterns for connecting DocBits to pricing systems, validation services, ERP systems, and other external data sources.

**What This Pattern Does:**
1. Calls an external API to fetch data
2. Validates the API response
3. Stores response data in document fields
4. Makes decisions based on fetched data
5. Routes documents accordingly

---

## When to Use This Pattern

Use this pattern when you need to:
- ✅ Fetch real-time pricing from external systems
- ✅ Validate supplier information against master database
- ✅ Look up product details from catalog systems
- ✅ Get exchange rates from currency services
- ✅ Verify addresses with geocoding services
- ✅ Check inventory levels from warehouse systems
- ✅ Validate tax rates from tax services

**Don't use this pattern when:**
- ❌ Data is already in DocBits master data (use master data lookup instead)
- ❌ External system doesn't have an API (use DocOperator Script pattern instead)
- ❌ Data doesn't change frequently (consider manual import)

---

## Complete Workflow Example

### Scenario: Validate Invoice Price Against Current Pricing API

**Business Requirement:**
- Supplier sends invoice
- Invoice shows unit price of €52.00
- We need to verify this matches current supplier pricing
- If price varies more than 5%, escalate for review

**Workflow Cards Used:**
1. CALL_API - Fetch current price from supplier API
2. CONDITION_HTTPS_REQUEST_STATUS - Check if API call succeeded
3. ACTION_SET_FIELD_TO_TEXT - Store API price in document field
4. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Compare invoice price vs API price
5. ACTION_ASSIGN_TO_USER - Route based on comparison result
6. tasks_create - Create review task if needed

---

## Step-by-Step Implementation

### Step 1: Call External API

**Card:** CALL_API or ACTION_CALL_EXTERNAL_API

**Configuration:**
```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**Expected Response:**
```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**Guide Reference:** [Call API Guide](../then/action/call-api-guide.md)

---

### Step 2: Validate API Response

**Card:** CONDITION_HTTPS_REQUEST_STATUS

**Configuration:**
```
Operator: IS EQUAL TO
Status Code: 200
```

**Logic:**
```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**Guide Reference:** [Condition Cards Guide - HTTP Status](../and/condition-cards-complete-guide.md#condition-https-request-status)

---

### Step 3: Store API Response in Document Fields

**Card:** ACTION_SET_FIELD_TO_TEXT (or equivalent field setter)

**Configuration:**

**Field 1: Current_API_Price**
```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**Field 2: API_Price_Valid_Until**
```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**Field 3: API_Discount_Available**
```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**Result:** Data from API is now stored in document fields for later use

**Guide Reference:** [Field Manipulation Guide - API Data Storage](../then/document-field/field-manipulation-guide.md#storing-api-data)

---

### Step 4: Compare Invoice Price with API Price

**Card:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Configuration:**
```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**Calculation:**
```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**Guide Reference:** [Condition Cards Guide - Field Comparison](../and/condition-cards-complete-guide.md#field-comparison)

---

### Step 5: Route Based on Validation Result

**Scenario A: Price Within Tolerance (Pass)**

**Cards:**
- ACTION_SET_FIELD_TO_TEXT
  - Set field "Price_Validation_Status" = "PASS"
  - Set field "Price_Variance_Percent" = "4%"
- ACTION_APPROVE_DOCUMENT
  - Auto-approve document

**Scenario B: Price Outside Tolerance (Fail)**

**Cards:**
- ACTION_SET_FIELD_TO_TEXT
  - Set field "Price_Validation_Status" = "FAIL"
  - Set field "Price_Variance_Percent" = "12%" (example)
- tasks_create
  - Task Title: "Review Price Variance - {{DOCUMENT_NUMBER}}"
  - Task Description: "Invoice price (€{{Invoice_Unit_Price}}) exceeds API price (€{{Current_API_Price}}) by {{Price_Variance_Percent}}"
  - Priority: High
- ACTION_ASSIGN_TO_USER
  - Assign to: Procurement Manager
- ACTION_SEND_EMAIL_TO_GROUPS
  - Send notification to Procurement Team

**Guide References:**
- [Assignment Guide](../then/assignee/assignment-user-guide.md)
- [Task Assignment Guide](../then/task/task-assignment-guide.md)
- [Send Email Guide](../then/action/send-email-groups-guide.md)

---

## Complete Workflow Diagram

```
DOCUMENT ARRIVES (Invoice with Product ABC123, Price €52)
│
├─ STEP 1: Call Pricing API
│  Card: CALL_API
│  Request: Get current price for ABC123
│  │
│  ├─ SUCCESS (200) ✅
│  │  Response: {"unit_price": 50.00}
│  │  │
│  │  ├─ STEP 2: Check API Status
│  │  │  Card: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Result: 200 = Success
│  │  │  │
│  │  │  ├─ STEP 3: Store API Data
│  │  │  │  Card: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Action: Store €50 in "Current_API_Price" field
│  │  │  │  │
│  │  │  │  ├─ STEP 4: Compare Prices
│  │  │  │  │  Card: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Calculate: Variance = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF Variance ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Set Status Field: "PASS"
│  │  │  │  │  │  └─ Auto-Approve Document
│  │  │  │  │  │     → END (Document Approved)
│  │  │  │  │  │
│  │  │  │  │  └─ IF Variance > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Set Status Field: "FAIL"
│  │  │  │  │     ├─ Create Review Task
│  │  │  │  │     ├─ Assign to Procurement Manager
│  │  │  │  │     └─ Send Email Notification
│  │  │  │  │        → END (Pending Review)
│  │  │  │  │
│  │  │  │  └─ [Field storage complete]
│  │  │  │
│  │  │  └─ [Status check complete]
│  │  │
│  │  └─ [API data retrieved]
│  │
│  └─ ERROR (Non-200) ❌
│     │
│     ├─ Set Error Status
│     ├─ Create "API Error" Task
│     ├─ Assign to IT Support
│     └─ Send Email to Admin
│        → END (API Error - Manual Review)
```

---

## Configuration Templates

### Template 1: Simple GET Request (Lookup)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

**Use:** Simple data lookup by ID

---

### Template 2: POST Request with Body (Validation)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**Use:** Send document data for validation

---

### Template 3: Complex Request with Nested Data

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**Use:** Complex document processing with table data

---

## Error Handling

### Common Errors and Solutions

#### Error 1: Connection Timeout

**Symptoms:**
- API doesn't respond
- Workflow stuck waiting

**Solution:**
```
1. Check API endpoint URL (typo?)
2. Verify network connectivity
3. Check API service status
4. Implement timeout handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Create "API Timeout" task
     → Assign to IT Support
     → Send email notification
     → Use fallback value (if available)
```

#### Error 2: 401 Unauthorized

**Symptoms:**
- API returns 401 status
- Authentication failed

**Solution:**
```
1. Verify API key is correct
2. Check if API key expired
3. Ensure Authorization header formatted correctly
4. Implement auth error handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Create "API Auth Failed" task
     → Assign to Admin
     → Log error details
     → Stop workflow execution
```

#### Error 3: Invalid Response Format

**Symptoms:**
- Response received but can't parse
- Missing expected fields

**Solution:**
```
1. Verify API documentation
2. Check response structure matches expectations
3. Implement response validation:

   IF API_RESPONSE:data.unit_price IS NULL:
     → Set default value
     → Create "Invalid Response" task
     → Log response for debugging
```

**Guide Reference:** [Call API Troubleshooting](../then/action/call-api-guide.md#troubleshooting)

---

## Advanced Variations

### Variation 1: Multi-API Chaining

**Scenario:** Need data from multiple APIs

```
Step 1: Call Supplier API → Get Supplier Details
Step 2: Call Product API → Get Product Info (using Supplier ID from Step 1)
Step 3: Call Pricing API → Get Price (using Product ID from Step 2)
Step 4: Validate & Store all data
```

---

### Variation 2: Conditional API Calls

**Scenario:** Only call API under certain conditions

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

---

### Variation 3: API Response Caching

**Scenario:** Reduce API calls by caching responses

```
1. Check if "API_Last_Called" date is today
2. IF Yes:
     → Use cached value from "Cached_API_Price" field
3. IF No:
     → Call API
     → Store response in "Cached_API_Price"
     → Set "API_Last_Called" to today
```

---

## Performance Considerations

### Best Practices

✅ **Do:**
- Cache API responses when possible
- Use timeout settings (30-60 seconds)
- Implement retry logic for temporary failures
- Log API calls for debugging
- Monitor API usage/costs
- Test with sample documents first

❌ **Don't:**
- Call APIs synchronously for every document (consider batch processing)
- Ignore response errors
- Hardcode credentials in workflow
- Make unnecessary API calls
- Forget to handle timeouts

---

## Testing Checklist

Before deploying this pattern:

- [ ] Test API call with valid data
- [ ] Test API call with invalid data
- [ ] Test timeout scenario (what happens if API is slow?)
- [ ] Test authentication failure
- [ ] Test invalid response format
- [ ] Test field storage (data stored correctly?)
- [ ] Test comparison logic (correct calculation?)
- [ ] Test routing (documents go to right place?)
- [ ] Test error handling (errors handled gracefully?)
- [ ] Test with high volume (performance acceptable?)

---

## Real-World Examples

### Example 1: Currency Exchange Rate Lookup

**API:** https://api.exchangerate-api.com/v4/latest/USD

**Workflow:**
1. Extract invoice currency: "GBP"
2. Call exchange rate API
3. Get GBP→EUR exchange rate
4. Calculate EUR equivalent
5. Store in "Amount_EUR" field
6. Continue processing with EUR amount

---

### Example 2: Supplier Credit Check

**API:** Internal credit check service

**Workflow:**
1. Extract supplier code
2. Call credit check API
3. Get credit status: "APPROVED" or "BLOCKED"
4. IF BLOCKED:
   - Stop processing
   - Create urgent task
   - Notify finance team
5. IF APPROVED:
   - Continue normal workflow

---

### Example 3: Product Master Data Enrichment

**API:** Product catalog service

**Workflow:**
1. Extract product code from invoice
2. Call product API
3. Get: Product name, category, GL account
4. Store in document fields
5. Use for auto-accounting

---

## Related Patterns

### This Pattern Works Well With:

- **[Data Transformation Pattern](data-transformation-pattern.md)** - Transform API response data
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Route based on API data
- **[Task Management Pattern](task-management-pattern.md)** - Create tasks for API errors
- **[PO Matching Pattern](po-matching-pattern.md)** - Combine API pricing with PO validation

---

## Related Guides

### Prerequisites
- [Call API Guide](../then/action/call-api-guide.md) - API card documentation
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Condition logic
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Field operations

### Related Cards
- **CALL_API** - [Call API Guide](../then/action/call-api-guide.md)
- **ACTION_HTTPS_REQUEST** - [HTTPS Request Guide](../then/action/https-request-guide.md)
- **CONDITION_HTTPS_REQUEST_STATUS** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-https-request-status)
- **ACTION_SET_FIELD_TO_TEXT** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#set-field)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#field-comparison)

### Next Steps
- Implement error handling: [Error Handling Pattern](error-handling-pattern.md)
- Add task creation: [Task Management Pattern](task-management-pattern.md)
- Transform data: [Data Transformation Pattern](data-transformation-pattern.md)

---

## Support & Resources

**Need Help?**
- Review [Call API Troubleshooting](../then/action/call-api-guide.md#troubleshooting)
- Check [API Response Codes](../then/action/call-api-guide.md#response-scenarios)
- Test API with Postman first
- Contact API provider support

**Feedback:**
- Report pattern issues to: docs@docbits.com
- Suggest improvements
- Share your use cases

---

**Pattern Version:** 1.0
**Last Updated:** October 23, 2025
**Difficulty:** Medium
**Estimated Time:** 45-60 minutes
**Success Rate:** High (when API is stable)
