# Run DocOperator Prompt (Automation Script)

Deze kaarten horen in de **Then**-groep van de Workflow Builder — de acties die worden uitgevoerd zodra aan de When/And-voorwaarden is voldaan:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Kaarten worden via <strong>Add Card</strong> aan de <strong>Then</strong>-groep toegevoegd.</p></figcaption></figure>

## Purpose
This card runs an automated browser action or script using DocOperator. Think of it as a robot that can interact with websites or systems exactly like a human would - clicking buttons, filling forms, extracting data, etc.

**Real-world example:** Your company uses a web-based purchasing system. This card can automatically log in, search for a product, check availability, and get the current price - all without anyone doing it manually.

---

## When to Use This Card

Use this card when you need to:
- Automate tasks on websites that don't have APIs
- Extract data from web pages
- Fill forms automatically
- Log into systems and retrieve information
- Automate repetitive manual tasks
- Interact with legacy systems that aren't integrated

**Common scenarios:**
- Log into supplier websites and get real-time inventory
- Automatically fill out forms on external systems
- Extract data from web pages that don't offer APIs
- Check delivery status on courier websites
- Get pricing from systems without API access

---

## How It Works

1. **Card Triggered**: Workflow reaches this card and conditions are met
2. **Script Starts**: DocOperator bot starts running your automation script
3. **Bot Actions**: The bot performs actions like clicking, typing, scrolling, extracting
4. **Data Extraction**: Bot collects information from web pages
5. **Return Data**: Data comes back to DocFlow for use in next cards
6. **Timeout Handling**: If script takes too long, it stops and returns what it has

---

## Parameters Explained

### DocOperator Prompt/Script
The automation script that tells DocOperator exactly what to do

**Example (Plain English):**
```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Variables
Data you want to pass INTO the script

**Example:**
```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

These variables can be used in the script like:
```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maximum Steps
How many actions the bot is allowed to perform

**Typical values:**
- Simple task (like getting one price): 10-20 steps
- Medium complexity (fill form + extract): 20-50 steps
- Complex workflow (login + search + validate): 50-100 steps

**Why it matters:** Prevents infinite loops and very long running scripts

### Maximum Retries
If the bot fails an action, how many times should it try again?

**Examples:**
- 1: Try once, if it fails move on
- 3: Try 3 times before giving up
- 5: Very persistent - try 5 times

---

## Step-by-Step Example

### Scenario: Get Supplier Pricing from Website

**Script Definition:**
```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Variables Passed In:**
```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Script Using Variables:**
```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Expected Result:**
```
price: 45.50
quantity_available: 500
```

---

## Types of Actions DocOperator Can Perform

### Navigation
- Go to URL
- Click links
- Press buttons
- Scroll page

### Form Filling
- Type text into fields
- Select dropdown options
- Check/uncheck boxes
- Click buttons

### Data Extraction
- Read text from page
- Extract numbers
- Get table data
- Copy information

### Waiting
- Wait for page to load
- Wait for elements to appear
- Wait for dynamic content

### Conditional Logic
- If something exists, do this
- If text matches, then...
- Count results and act accordingly

---

## Common Use Cases

### 1. Get Real-Time Pricing
**Scenario:** Supplier doesn't have API but website shows prices

**Script:**
```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Check Inventory Availability
**Scenario:** Need to know if supplier has stock

**Script:**
```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Automatic Form Submission
**Scenario:** Need to fill out a form on an external site

**Script:**
```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Data Entry Verification
**Scenario:** Verify data matches on two different systems

**Script:**
```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

---

## Configuration Steps

### Step 1: Create the Script
1. Define what you want to accomplish
2. Break it into small steps
3. Write each step clearly
4. Test manually first (open the website, do it yourself)
5. Document exactly what you click, where you type, what you extract

### Step 2: Identify Variables
1. What data will change between documents?
2. What should be passed into the script?
3. Define variable names
4. Specify where variables are used in the script

### Step 3: Set Parameters
- **Maximum Steps**: Based on script complexity
- **Maximum Retries**: How persistent should bot be?
- **Timeout**: How long should it wait for pages?

### Step 4: Test
1. Test with sample data
2. Verify bot can access the website
3. Verify extraction is correct
4. Check if variables work properly

---

## Script Writing Tips

### Clear Language
✅ **Do:**
```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Don't:**
```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Specific Selectors
✅ **Do:**
```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Don't:**
```
Click somewhere
Type in a field
```

### Error Handling
✅ **Do:**
```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Don't:**
```
Click "Next" (assumes it's always there)
```

---

## Troubleshooting

### "Script Timed Out"
**Cause:** Script took too long to complete

**Solutions:**
- [ ] Reduce the number of actions
- [ ] Increase "Maximum Steps" value
- [ ] Optimize the script for faster execution
- [ ] Simplify what you're trying to extract

### "Element Not Found"
**Cause:** DocOperator couldn't find the button/field you specified

**Solutions:**
- [ ] Verify button/field name is exactly correct
- [ ] Check if website layout changed
- [ ] Add wait time before clicking
- [ ] Check if button only appears under certain conditions

### "Login Failed"
**Cause:** Authentication failed

**Solutions:**
- [ ] Verify username/password are correct
- [ ] Check if password has special characters
- [ ] Verify account isn't locked
- [ ] Check if login process changed

### "Data Not Extracted Correctly"
**Cause:** The script ran but extracted wrong information

**Solutions:**
- [ ] Verify the correct field was selected
- [ ] Check if data is in expected location
- [ ] Test extraction logic manually
- [ ] Add debugging steps to verify what's on page

### "Script Runs Slowly"
**Cause:** Too many steps or slow website

**Solutions:**
- [ ] Remove unnecessary steps
- [ ] Optimize wait times
- [ ] Check internet connection
- [ ] Consider if API alternative exists

---

## Best Practices

✅ **Do:**
- Test scripts thoroughly before deploying
- Keep scripts simple and focused
- Add comments explaining each step
- Use meaningful variable names
- Monitor script performance
- Have fallback for when scripts fail

❌ **Don't:**
- Create extremely long scripts (>100 steps)
- Put sensitive passwords in logs
- Rely on exact coordinates (websites change)
- Create loops without exit conditions
- Ignore error messages

---

## Performance Tips

- **Remove unused steps** - Every step takes time
- **Combine similar actions** - Group related clicks
- **Optimize waits** - Use only necessary delays
- **Cache data** - Don't extract same data twice
- **Parallel processing** - Run multiple scripts if possible

---

## Security Considerations

⚠️ **Important:**
- Don't store passwords in DocFlow
- Use secure methods to pass credentials
- Don't log sensitive data
- Monitor what's being extracted
- Ensure bot activity is logged and auditable

---

## Variables Example

### Available Variables You Can Use:
```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Script Using Variables:
```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

---

## Comparison: When to Use DocOperator vs API

| Situation | Use DocOperator | Use API |
|-----------|-----------------|---------|
| Website has API | ❌ No | ✅ Yes |
| Website is interactive | ✅ Yes | ❌ No |
| Requires login | ✅ Yes | Depends |
| Very fast needed | ❌ No | ✅ Yes |
| Complex workflow | ✅ Yes | ❌ Maybe not |
| Data changes daily | ✅ Yes | ✅ Yes |

---

## Related Cards

- **CALL_API** - Use when API is available instead
- **ACTION_HTTPS_REQUEST** - Simpler requests
- **ACTION_SET_FIELD_TO_TEXT** - Use extracted data
- **CONDITION_HTTPS_REQUEST_STATUS** - Check request status

