# Task Management Pattern

**Pattern Type:** Workflow Management
**Complexity:** Low-Medium
**Estimated Setup:** 30-45 minutes
**Common Use Cases:** Approval workflows, review tasks, exception handling, escalation

---

You build this pattern in the **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Click **Add Card** to open the card library and pick the cards this pattern uses — `tasks_create`, `ACTION_ASSIGN_TO_USER`, `ACTION_SEND_EMAIL_TO_GROUPS` and `CONDITION_TASK_STATUS` (the **Assignee** category holds the task and assignment cards):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card library in the Workflow Builder, grouped by category"><figcaption><p>The <strong>Add Card</strong> library — the task, assignment and notification cards live under the <strong>Assignee</strong> and <strong>Status</strong> categories.</p></figcaption></figure>

---

## Pattern Overview

This pattern demonstrates how to create, assign, track, and manage tasks within DocBits workflows. Tasks are actionable work items assigned to users or groups that require completion before the document workflow can continue.

**What This Pattern Does:**
1. Creates tasks based on workflow conditions
2. Assigns tasks to appropriate users or groups
3. Sets task properties (priority, deadline, description)
4. Sends notifications when tasks are created
5. Tracks task status and completion
6. Routes documents based on task outcomes

---

## When to Use This Pattern

Use this pattern when you need to:
- ✅ Create approval workflows
- ✅ Assign review tasks to users
- ✅ Handle exceptions requiring human intervention
- ✅ Escalate issues to managers
- ✅ Create multi-level approval chains
- ✅ Track who needs to do what
- ✅ Set deadlines for actions

**Don't use this pattern when:**
- ❌ No human action required (use auto-processing instead)
- ❌ Just need to notify (use email instead)
- ❌ Simple document routing (use assignment instead)

---

## Complete Workflow Example

### Scenario: Invoice Approval with Amount-Based Routing

**Business Requirement:**
- Invoices < €1,000: Auto-approve (no task needed)
- Invoices €1,000-€10,000: Approval task to Manager
- Invoices > €10,000: Dual approval (Manager + Director)
- All approvers receive email notification
- Tasks have 3-day deadline

**Workflow Cards Used:**
1. CONDITION_DOC_FIELD_AMOUNT - Check invoice amount
2. tasks_create - Create approval task
3. ACTION_ASSIGN_TO_USER - Assign task to approver
4. ACTION_SEND_EMAIL_TO_GROUPS - Send notification
5. CONDITION_TASK_STATUS - Check if task completed
6. ACTION_APPROVE_DOCUMENT - Approve after task completion

---

## Step-by-Step Implementation

### Step 1: Check Amount Threshold

**Card:** CONDITION_DOC_FIELD_AMOUNT or similar field condition

**Configuration for Path 1 (< €1,000):**
```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Configuration for Path 2 (€1,000-€10,000):**
```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Configuration for Path 3 (> €10,000):**
```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Guide Reference:** [Condition Cards Guide](../and/condition-cards-complete-guide.md)

---

### Step 2A: Auto-Approve Small Invoices (< €1,000)

**No task needed for small amounts**

**Cards:**
- ACTION_SET_FIELD_TO_TEXT
  - Set "Approval_Type" = "AUTO"
  - Set "Approval_Reason" = "Amount below threshold"
- ACTION_APPROVE_DOCUMENT

**Result:** Document automatically approved, no task created

---

### Step 2B: Create Manager Approval Task (€1,000-€10,000)

**Card:** tasks_create (v4 recommended)

**Configuration:**
```json
{
  "task_type": "Approval",
  "task_title": "Approve Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "Please approve invoice from {{Supplier_Name}}\n\nAmount: €{{Total_Amount}}\nInvoice Number: {{Invoice_Number}}\nInvoice Date: {{Invoice_Date}}\n\nReview and approve within 3 business days.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "{{DOCUMENT_FIELD:Approving_Manager}}",
  "task_category": "Invoice Approval",
  "required_action": "Approve or Reject"
}
```

**Field Mapping:**
- `{{DOCUMENT_NUMBER}}` - Automatic document ID
- `{{Total_Amount}}` - Field: Total_Amount
- `{{Supplier_Name}}` - Field: Supplier_Name
- `{{Invoice_Number}}` - Field: Invoice_Number
- `{{Invoice_Date}}` - Field: Invoice_Date
- `{{Approving_Manager}}` - Field or fixed user

**Guide Reference:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

---

### Step 2C: Create Dual Approval Tasks (> €10,000)

**Two sequential tasks for high-value invoices**

**Task 1: Manager Approval**
```json
{
  "task_type": "First Approval",
  "task_title": "URGENT: Approve High-Value Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "HIGH VALUE INVOICE REQUIRES APPROVAL\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nThis invoice exceeds €10,000 and requires dual approval.\nYour approval is required before Director review.",
  "priority": "High",
  "deadline_days": 2,
  "assign_to": "Finance_Manager",
  "task_category": "High-Value Approval",
  "next_task": "Director_Approval"
}
```

**Task 2: Director Approval (Created after Task 1 completion)**
```json
{
  "task_type": "Second Approval",
  "task_title": "Final Approval: Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "FINAL APPROVAL REQUIRED\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nFirst approval: Completed by {{Task1_Approver}} on {{Task1_Date}}\n\nYour final approval required.",
  "priority": "High",
  "deadline_days": 1,
  "assign_to": "Finance_Director",
  "task_category": "Final Approval",
  "prerequisite_task": "Manager_Approval"
}
```

---

### Step 3: Assign Task to User/Group

**Card:** ACTION_ASSIGN_TO_USER or ACTION_ASSIGN_TO_GROUP

**Option 1: Assign to Specific User**
```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Option 2: Assign to Group**
```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Option 3: Sequential Assignment**
```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Guide Reference:** [Assignment User Guide](../then/assignee/assignment-user-guide.md)

---

### Step 4: Send Email Notification

**Card:** ACTION_SEND_EMAIL_TO_GROUPS

**Configuration:**
```json
{
  "recipients": [
    "{{TASK_ASSIGNEE_EMAIL}}",
    "finance-notifications@company.com"
  ],
  "subject": "New Task Assigned: Approve Invoice {{DOCUMENT_NUMBER}}",
  "body": "Dear {{TASK_ASSIGNEE_NAME}},\n\nA new approval task has been assigned to you:\n\nTask: Approve Invoice {{DOCUMENT_NUMBER}}\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\nDeadline: {{TASK_DEADLINE}}\nPriority: {{TASK_PRIORITY}}\n\nPlease log in to DocBits to review and approve:\n{{DOCUMENT_LINK}}\n\nBest regards,\nDocBits Automation"
}
```

**Email Variables:**
- `{{TASK_ASSIGNEE_EMAIL}}` - Task assignee's email
- `{{TASK_ASSIGNEE_NAME}}` - Task assignee's name
- `{{DOCUMENT_NUMBER}}` - Document ID
- `{{TASK_DEADLINE}}` - Task due date
- `{{TASK_PRIORITY}}` - Task priority level
- `{{DOCUMENT_LINK}}` - Direct link to document

**Guide Reference:** [Send Email Groups Guide](../then/action/send-email-groups-guide.md)

---

### Step 5: Track Task Status

**Card:** CONDITION_TASK_STATUS or similar task status checker

**Configuration:**
```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Status Options:**
- CREATED - Task just created
- ASSIGNED - Task assigned to user
- IN_PROGRESS - User started working on task
- COMPLETED - Task finished
- APPROVED - Task approved
- REJECTED - Task rejected
- CANCELLED - Task cancelled
- OVERDUE - Task past deadline

**Logic:**
```
IF TASK_STATUS = COMPLETED AND TASK_RESULT = APPROVED:
  → Continue to next step (or next approval level)
  → Update document status
  → Log approval

IF TASK_STATUS = COMPLETED AND TASK_RESULT = REJECTED:
  → Stop workflow
  → Send rejection notification
  → Create review task for corrections

IF TASK_STATUS = OVERDUE:
  → Escalate to manager
  → Send reminder email
  → Create escalation task
```

---

### Step 6: Complete Workflow Based on Task Result

**After Task Completion:**

**Scenario A: Task Approved**
```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Scenario B: Task Rejected**
```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Scenario C: Task Overdue**
```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

---

## Complete Workflow Diagram

```
INVOICE ARRIVES
│
├─ CHECK AMOUNT
│  │
│  ├─ Amount < €1,000 ✅
│  │  │
│  │  ├─ Set Approval_Type = "AUTO"
│  │  └─ Auto-Approve Document
│  │     → END (Approved)
│  │
│  ├─ Amount €1,000-€10,000 ⚠️
│  │  │
│  │  ├─ CREATE TASK: Manager Approval
│  │  │  - Title: "Approve Invoice"
│  │  │  - Priority: Medium
│  │  │  - Deadline: 3 days
│  │  │  │
│  │  │  ├─ ASSIGN TO: Finance Manager
│  │  │  │
│  │  │  ├─ SEND EMAIL: Notification
│  │  │  │
│  │  │  ├─ WAIT FOR TASK COMPLETION
│  │  │  │  │
│  │  │  │  ├─ TASK APPROVED ✅
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "APPROVED"
│  │  │  │  │  └─ Approve Document
│  │  │  │  │     → END (Approved)
│  │  │  │  │
│  │  │  │  ├─ TASK REJECTED ❌
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "REJECTED"
│  │  │  │  │  ├─ Reject Document
│  │  │  │  │  └─ Create Correction Task
│  │  │  │  │     → END (Rejected)
│  │  │  │  │
│  │  │  │  └─ TASK OVERDUE ⏰
│  │  │  │     │
│  │  │  │     ├─ Send Reminder Email
│  │  │  │     ├─ Escalate to Director
│  │  │  │     └─ Create Escalation Task
│  │  │  │        → WAIT (Escalated)
│  │  │  │
│  │  │  └─ [Task tracking active]
│  │  │
│  │  └─ [Manager approval path]
│  │
│  └─ Amount > €10,000 🚨
│     │
│     ├─ CREATE TASK 1: Manager First Approval
│     │  - Title: "URGENT: First Approval"
│     │  - Priority: High
│     │  - Deadline: 2 days
│     │  │
│     │  ├─ ASSIGN TO: Finance Manager
│     │  ├─ SEND EMAIL: High Priority Notification
│     │  │
│     │  ├─ WAIT FOR TASK 1 COMPLETION
│     │  │  │
│     │  │  ├─ TASK 1 APPROVED ✅
│     │  │  │  │
│     │  │  │  ├─ CREATE TASK 2: Director Final Approval
│     │  │  │  │  - Title: "Final Approval Required"
│     │  │  │  │  - Priority: High
│     │  │  │  │  - Deadline: 1 day
│     │  │  │  │  │
│     │  │  │  │  ├─ ASSIGN TO: Finance Director
│     │  │  │  │  ├─ SEND EMAIL: Final Approval Notification
│     │  │  │  │  │
│     │  │  │  │  ├─ WAIT FOR TASK 2 COMPLETION
│     │  │  │  │  │  │
│     │  │  │  │  │  ├─ TASK 2 APPROVED ✅
│     │  │  │  │  │  │  │
│     │  │  │  │  │  │  ├─ Set Dual_Approval = "COMPLETE"
│     │  │  │  │  │  │  └─ Approve Document
│     │  │  │  │  │  │     → END (Dual Approved)
│     │  │  │  │  │  │
│     │  │  │  │  │  └─ TASK 2 REJECTED ❌
│     │  │  │  │  │     │
│     │  │  │  │  │     ├─ Reject Document
│     │  │  │  │  │     └─ Notify All Parties
│     │  │  │  │  │        → END (Final Rejected)
│     │  │  │  │  │
│     │  │  │  │  └─ [Task 2 tracking]
│     │  │  │  │
│     │  │  │  └─ [Task 2 created]
│     │  │  │
│     │  │  └─ TASK 1 REJECTED ❌
│     │  │     │
│     │  │     ├─ Reject Document (No Task 2 created)
│     │  │     └─ Notify Supplier
│     │  │        → END (First Rejected)
│     │  │
│     │  └─ [Task 1 tracking]
│     │
│     └─ [Dual approval path]
│
└─ [Amount check complete]
```

---

## Configuration Templates

### Template 1: Simple Approval Task

```json
{
  "card": "tasks_create",
  "task_title": "Approve {{DOCUMENT_TYPE}} {{DOCUMENT_NUMBER}}",
  "task_description": "Please review and approve this document.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "approver@company.com",
  "category": "Approval"
}
```

---

### Template 2: Review Task with Details

```json
{
  "card": "tasks_create",
  "task_title": "Review Exception: {{EXCEPTION_TYPE}}",
  "task_description": "Document: {{DOCUMENT_NUMBER}}\nException: {{EXCEPTION_REASON}}\n\nDetails:\n- Supplier: {{Supplier_Name}}\n- Amount: €{{Total_Amount}}\n- Date: {{Document_Date}}\n\nAction Required: Review and resolve exception",
  "priority": "High",
  "deadline_days": 1,
  "assign_to_group": "Exceptions Team",
  "category": "Exception Handling"
}
```

---

### Template 3: Escalation Task

```json
{
  "card": "tasks_create",
  "task_title": "ESCALATION: {{ORIGINAL_TASK_TITLE}}",
  "task_description": "ESCALATED TASK\n\nOriginal Task: {{ORIGINAL_TASK_ID}}\nOriginal Assignee: {{ORIGINAL_ASSIGNEE}}\nDeadline Passed: {{ORIGINAL_DEADLINE}}\nDays Overdue: {{DAYS_OVERDUE}}\n\nPlease review and take immediate action.",
  "priority": "Urgent",
  "deadline_days": 1,
  "assign_to": "manager@company.com",
  "category": "Escalation",
  "parent_task": "{{ORIGINAL_TASK_ID}}"
}
```

---

## Advanced Patterns

### Pattern 1: Sequential Multi-Level Approval

**Use:** Invoices must go through multiple approvers in sequence

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Implementation:**
```
1. Create Task 1 for Clerk
2. Wait for Task 1 completion
3. IF Task 1 = APPROVED:
     Create Task 2 for Manager
4. Wait for Task 2 completion
5. IF Task 2 = APPROVED:
     Create Task 3 for Director
6. Wait for Task 3 completion
7. IF Task 3 = APPROVED:
     Approve Document
```

---

### Pattern 2: Parallel Multi-Approver

**Use:** Multiple people must approve simultaneously

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Implementation:**
```
1. Create 3 tasks simultaneously
2. Track all 3 task statuses
3. WAIT until ALL tasks completed
4. IF ALL = APPROVED:
     Approve Document
   ELSE:
     Reject Document
```

---

### Pattern 3: Conditional Task Creation

**Use:** Create different tasks based on conditions

```
IF Supplier = "New":
  → Create "New Supplier Review" task
ELSE IF Amount > €50,000:
  → Create "High Value Approval" task
ELSE IF Document has errors:
  → Create "Error Correction" task
ELSE:
  → Create "Standard Approval" task
```

---

### Pattern 4: Deadline-Based Escalation

**Use:** Auto-escalate if task not completed on time

```
Day 0: Create task for User A (3-day deadline)
Day 3: IF not completed:
         → Send reminder to User A
Day 4: IF still not completed:
         → Create escalation task for Manager B
         → Notify both User A and Manager B
Day 5: IF still not completed:
         → Create urgent task for Director C
         → High priority notification
```

---

## Error Handling

### Scenario 1: Assignee Not Found

**Problem:** User doesn't exist or is inactive

**Solution:**
```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

---

### Scenario 2: Task Creation Failed

**Problem:** System error creating task

**Solution:**
```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

---

### Scenario 3: No Response to Task

**Problem:** User doesn't complete task by deadline

**Solution:**
```
1. Monitor task deadline
2. Day before deadline:
     → Send reminder email
3. On deadline day:
     → Send urgent reminder
4. After deadline:
     → Create escalation task
     → Notify manager
     → Log overdue event
```

---

## Testing Checklist

- [ ] Task created successfully
- [ ] Task assigned to correct user/group
- [ ] Email notification sent
- [ ] Task appears in user's task list
- [ ] Task properties correct (title, description, priority, deadline)
- [ ] User can complete task
- [ ] Workflow continues after task completion
- [ ] Approval workflow works correctly
- [ ] Rejection workflow works correctly
- [ ] Escalation triggers at right time
- [ ] Overdue handling works
- [ ] All email notifications sent
- [ ] Field updates work correctly

---

## Real-World Examples

### Example 1: Three-Way PO Matching Exception

**Scenario:** Invoice doesn't match PO, needs review

```
1. PO Matching fails (price variance > 5%)
2. Create Task: "Review PO Mismatch"
   - Assign to: Procurement Officer
   - Priority: High
   - Description: Include variance details
3. Send email with comparison table
4. Wait for task completion
5. IF Approved: Continue processing
   IF Rejected: Return to supplier
```

---

### Example 2: Supplier Invoice Approval

**Scenario:** New supplier invoice needs special approval

```
1. Check if supplier is new (< 6 months old)
2. IF New:
     Create Task: "New Supplier Invoice Review"
     - Assign to: Procurement Manager
     - Include supplier details
     - Require supplier verification
3. After approval:
     Add to approved supplier list
     Continue normal workflow
```

---

### Example 3: Month-End Processing

**Scenario:** Month-end invoices need urgent processing

```
1. Check if document date in last 3 days of month
2. IF Yes:
     Create Task: "URGENT: Month-End Invoice"
     - Priority: Urgent
     - Deadline: 1 day
     - Assign to: Finance Team (all members)
     - Flag for expedited processing
3. Send urgent email notification
4. Track completion
```

---

## Performance Tips

✅ **Best Practices:**
- Set realistic deadlines
- Use clear task titles and descriptions
- Include all necessary information in task
- Send timely notifications
- Monitor task completion rates
- Escalate overdue tasks automatically
- Log all task activities
- Review task patterns monthly

❌ **Avoid:**
- Creating tasks for everything
- Vague task descriptions
- Unrealistic deadlines
- Too many notification emails
- No escalation path
- Ignoring overdue tasks
- Not tracking task metrics

---

## Related Patterns

### Patterns That Work Well Together:

- **[API Integration Pattern](api-integration-pattern.md)** - Create tasks for API errors
- **[PO Matching Pattern](po-matching-pattern.md)** - Create tasks for PO mismatches
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Route to appropriate task type
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Transform data before creating task

---

## Related Guides

### Prerequisites
- [Task Assignment Guide](../then/task/task-assignment-guide.md) - Task card documentation
- [Assignment User Guide](../then/assignee/assignment-user-guide.md) - User assignment
- [Send Email Groups Guide](../then/action/send-email-groups-guide.md) - Email notifications

### Related Cards
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** - [Assignment Guide](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** - [Email Guide](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** - [Condition Cards Guide](../and/condition-cards-complete-guide.md)

### Next Steps
- Add email notifications: [Send Email Guide](../then/action/send-email-groups-guide.md)
- Implement complex routing: [Decision Logic Pattern](decision-logic-pattern.md)
- Handle errors: [Error Handling Pattern](error-handling-pattern.md)

---

**Pattern Version:** 1.0
**Last Updated:** October 23, 2025
**Difficulty:** Low-Medium
**Estimated Time:** 30-45 minutes
**Success Rate:** Very High
