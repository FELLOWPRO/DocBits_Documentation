# Send Email to Groups

Queste schede vanno nel gruppo **Then** del Generatore di workflow — le azioni eseguite una volta soddisfatte le condizioni When/And:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede vengono aggiunte al gruppo <strong>Then</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

## Purpose
This card automatically sends email notifications to groups of users. Instead of assigning work to individual people, you send the message to a group, and all members of that group receive it.

**Real-world example:** When a high-value invoice arrives, automatically send an email notification to everyone in the "Finance Team" group so they're aware it needs review.

---

## When to Use This Card

Use this card when you need to:
- Notify multiple people at once
- Send alerts to team groups
- Broadcast updates to departments
- Notify groups about document status changes
- Send reminders to group members

**Common scenarios:**
- Notify procurement team about new suppliers
- Alert finance team about high-value invoices
- Notify warehouse team about shipments
- Broadcast document status changes

---

## How It Works

1. **Condition Check**: Workflow checks "Where" and "And" conditions
2. **Prepare Email**: System prepares the email using template
3. **Get Group Members**: System finds all members of specified group
4. **Send**: Email is sent to each group member
5. **Log**: Email sending is recorded

---

## Parameters Explained

### Email Template
The email message to be sent

**Options:**
- Choose from existing templates
- Each template has predefined subject, body, and formatting
- Templates can include placeholders like {document_number}, {supplier_name}

**Example Template:**
```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Group
The group of users to send the email to

**Example groups:**
- Finance Team
- Procurement Team
- Warehouse Team
- Approval Committee
- Management Group

---

## Configuration Steps

### Step 1: Choose Email Template
1. Click "Select Email Template"
2. Choose template from list
3. Verify subject and content

### Step 2: Select Group
1. Click "Select Group"
2. Choose the group you want to notify
3. Verify group members (usually shows count)

### Step 3: Set Conditions
1. Add condition: "When [condition] is true"
2. Example: "When invoice amount is greater than €5000"

### Step 4: Test
1. Test with sample document
2. Verify email sends to group
3. Check template rendering

---

## Email Template Examples

### Template 1: High-Value Invoice Alert
```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Template 2: Supplier Status Change
```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Template 3: Document Ready for Export
```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

---

## Common Use Cases

### Use Case 1: Quality Control Alerts
**Trigger:** When discrepancy is found between invoice and PO

**Email Group:** Quality Team

**Content:**
```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Use Case 2: Approval Notifications
**Trigger:** When document reaches certain status

**Email Group:** Approval Committee

**Content:**
```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Use Case 3: Exception Notifications
**Trigger:** When conditions not met

**Email Group:** Managers

**Content:**
```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Use Case 4: Status Updates
**Trigger:** When document status changes

**Email Group:** Team responsible for next step

**Content:**
```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

---

## Troubleshooting

### "Email not received"

**Possible Causes:**
- [ ] Users in group don't have email addresses
- [ ] Email blocked by spam filter
- [ ] Email address is incorrect in group
- [ ] Group has no members

**Solutions:**
1. Verify all group members have email addresses
2. Check spam/junk folder
3. Verify group membership is correct
4. Add users to group if missing
5. Check with IT that email service is working

### "Template not rendering correctly"

**Cause:** Placeholder variables not found

**Solution:**
- [ ] Verify field names match exactly
- [ ] Check if field has a value in the document
- [ ] Use correct placeholder format: {field_name}
- [ ] Test with sample document that has all fields

### "Some people getting email, others not"

**Cause:** Incomplete group membership or invalid emails

**Solutions:**
- [ ] Verify all members have valid email
- [ ] Check if some users have opted out
- [ ] Verify group membership is current
- [ ] Contact IT to validate email addresses

### "Want to add/remove people from group"

**Solution:**
- Contact your administrator
- Groups are managed in system settings
- Can't be changed from this card
- Request group membership changes in IT

---

## Email Template Customization

### Available Placeholders
```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Creating Custom Placeholders
If you need additional data in emails:
1. Contact your administrator
2. Request new placeholder
3. Add necessary field to document
4. Update email template

---

## Best Practices

✅ **Do:**
- Keep email content brief and clear
- Include action items (what should recipients do?)
- Include link or instructions to access document
- Test template with sample data
- Send to right group (don't over-notify)
- Use templates for consistency

❌ **Don't:**
- Send too many emails (notification fatigue)
- Include sensitive data in emails
- Send to groups that don't need info
- Use unclear subject lines
- Forget to include how to take action
- Send emails to individuals (use group instead)

---

## Performance Notes

- Each email takes ~1 second to send
- Large groups may take time (100 people = ~100 seconds)
- Don't create loops that send thousands of emails
- Monitor email service capacity
- Consider batching if many documents

---

## Related Cards

- **ACTION_SEND_EMAIL** - Send to individual person
- **ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP** - Assign task instead of just notifying
- **ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL** - Create task and notify
- **STAUS_CHANGE** - Change status and notify

---

## Typical Workflow Example

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

---

## FAQ

**Q: Can I send to multiple groups?**
A: Create separate cards for each group

**Q: What if someone's email bounces?**
A: Email is logged as failed, IT can troubleshoot

**Q: Can I change the email template?**
A: Contact your administrator to modify templates

**Q: Can I send based on conditions?**
A: Yes! Use "Where" and "And" conditions to control when emails send

**Q: How do I know if email was received?**
A: Check email logs in DocBits for sending status

