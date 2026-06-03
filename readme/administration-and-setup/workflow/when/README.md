# When

<figure><img src="../../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

#### Understanding the "When" in Workflow Configurations

**Purpose of "When"**

* The "When" section in a workflow configuration defines the trigger conditions that initiate a particular workflow action. These conditions are based on specified criteria related to document attributes or user activities within the ERP system.

**How It Works**

* In your interface, "When" appears to be a starting point where users can select different trigger cards. Each card specifies conditions under which subsequent actions (defined in "And" section) will be executed.

**Document Type Condition Cards**

* The cards with the document icon displayed in the screenshot are variations of "Document Type" conditions, which are used to trigger workflows based on the type of document being processed. Here’s a breakdown of each type of condition card shown:
  * **Document type (Operator) one of (Type)**: This card triggers an action when the type of a document matches one of the specified types in a list. The operator might include options like "is" or "is not," allowing for inclusive or exclusive conditions.
  * **Document type (Operator) (Type)**: This simpler variant triggers based on a single document type condition. It would typically check if the document type "is" or "is not" a specific type, without the option to select from multiple types.
  *

**Celery Beat**

* The card with the clock icon in the screenshot is a "Celery Beat" condition, which is used to trigger workflows based on date and time.

#### Setting Up a "When" Trigger Card

1. **Selection of Condition Type**: Users begin by selecting a condition type that is relevant to the workflow they want to automate. In this case, document types are the focus.
2. **Defining the Operator**: Users must decide the logical operator—such as "is" or "is not"—which sets the basis for comparing actual document types against the defined conditions.
3. **Specifying Document Types**: Depending on the card, users may select one or multiple document types that will trigger the workflow when documents of those types are processed.
4. **Finalizing the Trigger**: Once the condition is set up, it becomes the basis for triggering specific actions defined in the workflow. If a document meets the set condition, the defined actions will automatically be initiated.

#### Practical Application

In practice, these trigger cards are crucial for automating processes like approvals, notifications, or any procedure that depends on the type of document being handled. For example, if a document type "is" an "Invoice," and it matches the conditions set in the "When" card, the workflow might automatically route the document for payment processing.

This setup ensures that workflows are not only efficient but also tailored to the specific operational needs of the organization, reducing manual oversight and speeding up document handling processes.

In summary, the "When" part of your workflow configuration is about setting the stage for automated actions based on specific, predefined conditions. It’s a powerful tool for ensuring that your ERP system reacts dynamically to the needs of the business, enhancing both productivity and accuracy in document management.
