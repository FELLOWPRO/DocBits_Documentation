# Task Assignment & Creation Cards - Complete Guide

Deze kaarten horen in de **Then**-groep van de Workflow Builder — de acties die worden uitgevoerd zodra aan de When/And-voorwaarden is voldaan:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Kaarten worden via <strong>Add Card</strong> aan de <strong>Then</strong>-groep toegevoegd.</p></figcaption></figure>

**Covers:** 12 task-related cards

---

## Overview

Task cards create work assignments for team members. When an invoice needs approval, you can automatically create a task and assign it to the right person.

---

# Basic Task Creation

## Card: tasks_create / Create Task and Assign to User

### Purpose
Creates a task and assigns it to a specific person

### When to Use
- Invoice needs specific person's review
- Approval required from named individual
- Handoff to specific team member

### Parameters

**Title**
The task name/subject
```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Description**
Details about the task
```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priority**
- 🔴 **High**: Urgent, do immediately
- 🟡 **Medium**: Normal priority
- 🟢 **Low**: Can be done later

**Assigned User**
Who gets the task
```
Example: John Smith (Finance Manager)
```

**Email Notification**
Send email alert to assigned person?
```
✅ Yes: Person gets email
❌ No: Task only in system
```

### Example
```
Condition: "Invoice amount > €10,000"
    ↓
Create Task:
- Title: "High-Value Invoice Review Required"
- Description: "Invoice #INV-2025-789 for €15,000 needs approval"
- Priority: High
- Assigned to: Sarah Johnson (Finance Approver)
- Send Email: Yes
    ↓
Sarah receives task and email notification
```

---

## Card: ACTION_TASK_FOR_GROUP / Create Task for Group

### Purpose
Creates a task and assigns it to a group (all members can see it)

### When to Use
- Multiple people can do the task
- Task for team, not individual
- First person available should handle

### Difference from Individual Task
```
Individual Task:
- Only John sees it
- John must do it
- Others can't see it

Group Task:
- Everyone in group sees it
- Any group member can claim it
- Distributed workload
```

### Example Workflow
```
Document arrives
    ↓
Condition: "Is supplier new?"
    ↓
Create Task for Procurement Team:
- Title: "Verify New Supplier Details"
- Description: "Please validate supplier information"
- Priority: Medium
- Group: Procurement Team (10 members)
- Notify: Yes
    ↓
All 10 procurement team members see task
First person available takes it
```

---

## Card: ACTION_DECISION_TREE_CREATE_TASKS

### Purpose
Creates tasks based on decision table logic

### How It Works
```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

### When to Use
- Different suppliers need different approval
- Complex routing based on multiple factors
- Different team based on document type

### Example
```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

---

## Card: ACTION_DECISION_TREE_TASKS_SEQUENTIAL

### Purpose
Creates tasks sequentially based on decision table
Tasks are assigned one at a time with priority order

### When to Use
- Multiple approvals needed in sequence
- Workflow approval chain
- Each person reviews then passes to next

### How It Works
```
Step 1: Create Task for Procurement Manager
        (Priority 1)
    ↓
Step 2: Procurement Manager approves
    ↓
Step 3: Create Task for Finance Manager
        (Priority 2)
    ↓
Step 4: Finance Manager approves
    ↓
Step 5: Export
```

### Priority System
```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

### Example Configuration
```
Decision Table Returns:
  Level 1: Sarah Johnson (Finance)
  Level 2: Mike Smith (Manager)
  Level 3: Director (for approval)

Task Flow:
1. Sarah reviews → Comments
2. Passes to Mike → He reviews
3. Passes to Director → Final approval
4. All complete → Export
```

---

## Card: ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL

### Purpose
Assigns document to one user AND creates sequential task

### When to Use
- Assign document AND create task at same time
- Document needs to be reviewed by specific person
- Track both assignment and task creation

### How It Works
```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

### Example
```
High-value invoice arrives
    ↓
ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL:
- Assign Document to: Finance Manager
- Create Task: "Review & Approve High Value Invoice"
- Priority: High
    ↓
Document AND task both go to Finance Manager
```

---

## Card: ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL

### Purpose
Assigns document to group AND creates task

### When to Use
- Document needs group attention
- Want to track task creation
- Create initial task then document assignment

### Example
```
New supplier evaluation
    ↓
ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL:
- Document assigned to: Supplier Management Group
- Create Task: "Evaluate New Supplier Credentials"
- Assign Task to: Same group
- Priority: Medium
    ↓
Group members see document and task
```

---

# Advanced Task Creation

## Card: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP

### Purpose
Creates task for specific facility group

### When to Use
- Task for warehouse/facility team
- Facility-specific operations
- Physical location matters

### Example
```
Document: Shipment notification
    ↓
Create Task for Facility Group:
- Group: Berlin Warehouse Team
- Task: "Prepare items for shipment"
- Items: From document
    ↓
Berlin warehouse team gets task
```

---

## Card: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL

### Purpose
Sequential task assignment across facilities

### When to Use
- Multi-facility operations
- Tasks pass from facility to facility
- Sequential facility processing

### How It Works
```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

### Example
```
Manufacturing Document
    ↓
Create Sequential Tasks:
- Task 1: Factory A (Manufacturing) - Priority 1
- Task 2: Quality Team (Testing) - Priority 2
- Task 3: Warehouse (Packing) - Priority 3
- Task 4: Shipping (Dispatch) - Priority 4
    ↓
Each team completes → Passes to next
```

---

## Card: ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP

### Purpose
Creates task for procurement department

### When to Use
- Task for procurement team
- Supplier management tasks
- Purchase-related work

### Example
```
Supplier status change notification
    ↓
Create Task for Procurement Group:
- Task: "Update supplier records"
- Supplier: ABC Corp
- Action: Change status to 'On Hold'
- Priority: High
    ↓
Procurement team is notified
```

---

## Card: ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL

### Purpose
Sequential task routing within procurement

### When to Use
- Multi-step procurement processes
- Approval chain in procurement
- Escalation path

### Example
```
Purchase Requisition received
    ↓
Step 1: Buyer verifies (Priority 1)
    ↓
Step 2: Approver approves (Priority 2)
    ↓
Step 3: Director signs off (Priority 3)
    ↓
All sign-offs complete → Release to supplier
```

---

## Card: ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK

### Purpose
Get user from document field, assign task
If user not found, use fallback user

### When to Use
- User stored in document field
- Document specifies who should review
- Have backup person if specified user unavailable

### How It Works
```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

### Example
```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

### Parameters
```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

---

# Common Task Parameters

All task cards use these parameters:

### Title
```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

### Description
```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

### Priority Levels
```
🔴 HIGH
   - Action needed within hours
   - Blocks other processes
   - Example: Supply missing, urgent approval

🟡 MEDIUM
   - Standard processing
   - Normal timeline
   - Example: Regular invoice review

🟢 LOW
   - Can wait days/weeks
   - Non-urgent
   - Example: Archive old documents
```

### Due Date (if available)
```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

---

# Task Workflow Scenarios

## Scenario 1: Simple Approval
```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

## Scenario 2: Multi-Level Approval
```
Invoice Arrives (€50,000 - High Value)
    ↓
Create Sequential Tasks:
1. Finance Team (Initial review)
2. Finance Manager (Approval)
3. Director (Final sign-off)
    ↓
Each level completes → Next begins
```

## Scenario 3: Parallel Tasks
```
Invoice Arrives (From New Supplier)
    ↓
Create Task 1: Quality Team (verify supplier)
Create Task 2: Finance Team (check prices)
Create Task 3: Procurement (check contract)
    ↓
All teams work simultaneously
All must complete before proceeding
```

## Scenario 4: Conditional Routing
```
Invoice Arrives
    ↓
Decision Table:
  If amount > €10k → Assign to Director
  If amount €1k-€10k → Assign to Manager
  If amount < €1k → Assign to Team Lead
    ↓
Task created for correct person
```

---

# Task Assignment Best Practices

✅ **Do:**
- Include specific details in task title
- Set appropriate priority levels
- Set realistic deadlines
- Notify assignees
- Include link to document
- Use clear, actionable descriptions

❌ **Don't:**
- Create vague task titles ("Review this")
- Set everything as High priority
- Forget to notify assigned person
- Create multiple tasks for same work
- Assign to unavailable people

---

# Troubleshooting Tasks

## "Task not assigned to anyone"
**Cause:** User doesn't exist or group is empty

**Solution:**
- Verify user name spelling
- Check user is active in system
- Verify group has members
- Use fallback if needed

## "Person says they didn't get notification"
**Cause:** Email notification disabled or email wrong

**Solution:**
- Check "Send Email" checkbox is enabled
- Verify recipient email address
- Check spam folder
- Resend notification manually

## "Wrong person got task"
**Cause:** Routing logic incorrect

**Solution:**
- Check decision table conditions
- Verify fallback settings
- Test with sample document
- Check for typos in user names

## "Too many tasks created"
**Cause:** Card firing multiple times

**Solution:**
- Check conditions are specific enough
- Verify card only runs once per document
- Review "And" conditions
- Add additional filtering

---

# Task Card Comparison Table

| Card | Creates Task | Assigns To | When |
|------|-------------|-----------|------|
| tasks_create | Yes | Individual | Always |
| ACTION_TASK_FOR_GROUP | Yes | Group | Always |
| ACTION_DECISION_TREE_CREATE_TASKS | Yes | Decision Table Result | Conditional |
| ACTION_DECISION_TREE_TASKS_SEQUENTIAL | Yes | Multiple (Sequential) | Conditional |
| ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL | Yes | User + Document | Conditional |
| ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL | Yes | Group + Document | Conditional |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP | Yes | Facility Group | Conditional |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL | Yes | Multiple Facilities | Conditional |
| ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP | Yes | Procurement Team | Conditional |
| ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL | Yes | Multiple (Sequential) | Conditional |
| ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK | Yes | Field/Fallback | Conditional |

---

# Related Cards

- **ACTION_ASSIGN_DOCUMENT_TO_USER** - Assign document without creating task
- **ACTION_SEND_EMAIL** - Notify people directly
- **STAUS_CHANGE** - Change status instead of creating task
- **RUN_WORKFLOW** - Trigger different workflow instead

