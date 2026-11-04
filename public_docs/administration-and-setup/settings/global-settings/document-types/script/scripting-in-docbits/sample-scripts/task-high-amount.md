# Task for High Invoice Amount

## What does this script do?

Creates an approval task when the invoice total exceeds a threshold (e.g., 100,000). The task is assigned to the "Finance Approval" group and triggers an email notification to ensure timely review.

## Trigger

`AFTER_FORMATTING` on document type **INVOICE**

## Full Script

```python
# Read total amount from the document
total = get_field_value(document_data, "total_amount", "0")

try:
    if float(total) > 100000:
        # Find the Finance Approval group by name
        finance_group = get_group_by_name(org_id, "Finance Approval")

        # Create an approval task
        create_document_task(
            user,
            document_data,
            title="Amount > 100,000 - Approval required",
            description=f"Total amount: {total}",
            priority="HIGH",
            assigned_to_user_id=None,
            assigned_to_group_id=str(finance_group.id) if finance_group else None,
            send_email=True
        )
except ValueError:
    pass
```

## Step-by-Step Explanation

1. **Read total amount** from the document
2. **Check threshold** — only proceed if amount exceeds 100,000
3. **Find group** by name using `get_group_by_name()` to get the group ID dynamically
4. **Create task** assigned to the finance group with high priority and email notification

## Functions Used

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Read field value
- [get\_group\_by\_name()](../business-logic-functions.md#get\_group\_by\_id--get\_group\_by\_name) — Find group by name
- [create\_document\_task()](../business-logic-functions.md#create\_document\_task) — Create approval task
