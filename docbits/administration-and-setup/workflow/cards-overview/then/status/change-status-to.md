# Change Status to

<figure><img src="../../../../../.gitbook/assets/image (359).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Change Status"** workflow card is used to change the status of a document to one of the predefined states—**Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval**—and optionally trigger associated workflows based on the status change. This card automates the process of status updates and workflow triggers, ensuring efficient document management and error handling.

## **Components of the Card:**

1. **Status**
   * **Description**: Specifies the new status to be applied to the document.
   * **Options**:
     * **Error**: Marks the document as having encountered an error.
     * **Rejected**: Indicates the document has been rejected and will not proceed further.
     * **Ready for Validation**: Sets the document to be reviewed and validated by the next user or system process.
     * **Pending Approval**: Places the document in a pending state for approval.
     * **Pending Second Approval**: Puts the document on hold for a second level of approval if applicable.
2. **Trigger Workflows**
   * **Description**: Determines whether any subsequent workflows should be triggered after the status change.
   * **Options**:
     * **True**: Initiates any relevant workflows based on the status change.
     * **False**: Prevents workflow execution after the status change.

## **Functionality:**

* **Condition Evaluation**: The system evaluates the conditions set in the **"When"** and **"And."** If these conditions are true, the card proceeds to change the document's status to the selected value.
* **Status Update**: Once the conditions are satisfied, the document's status is updated to one of the predefined options (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval), depending on the user’s selection.
* **Trigger Workflow Action**: If **Trigger Workflows** is set to **True**, the system automatically initiates any associated workflows following the status update. If set to **False**, no additional workflows are triggered, and the process ends with the status change.

## **Setup and Configuration:**

To configure this card, users need to:

1. Specify the desired **Status** that the document will be set to upon condition evaluation (Error, Rejected, Ready for Validation, Pending Approval, or Pending Second Approval).
2. Choose whether to **Trigger Workflows** after the status change by selecting **True** or **False**.
3. The card only executes its action if both conditions in the **"When"** and **"And"** are evaluated as true.

## **Conclusion:**

The **"Change Status"** workflow card offers a streamlined approach to managing document statuses and triggering related workflows. It ensures documents are automatically routed to the correct status and that the necessary actions are taken, depending on the status change. By setting clear conditions for execution, it reduces manual effort and enhances workflow efficiency.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Move a checked document to the approval step.

**Where:** Standard workflow designer → Then → Status → Change Status to.

**Configuration:** Select version 3 of `staus_change`, choose Pending Approval (`validated_pending_approval`) and set workflow triggering to `false` (`trigger_docflow=false`). Use an isolated synthetic invoice whose preceding checks are satisfied.

**Expected result and counterexample:** An allowed, successful update places the document in the selected status. If a preceding condition is false, this action is not reached and makes no status change. A refused or failed API update is not success: inspect the actual status and logs. This card does not itself perform an export.

### Card versions

The explicit workflow-triggering switch is available in v3. Versions 1 and 2 do not expose it; their legacy update call uses the default workflow-triggering behavior. Do not assume a v3 `false` setting applies after switching to an older card version.

This is a source-reviewed configuration and expected result. No workflow or status update was executed.
