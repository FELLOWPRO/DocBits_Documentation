# Assign document to matching sub organization

<figure><img src="../../../../../.gitbook/assets/image (376).png" alt="Workflow Then card that assigns the document to the matching sub-organization" width="563"><figcaption></figcaption></figure>

## **Purpose:**

The **"Assign Document to Matching Sub-Organization Based on Field"** workflow card assigns a document to a sub-organization dynamically, based on a specified field in the document. If no matching sub-organization is found, the card uses a predefined fallback sub-organization.

## **Components of the Card:**

1. **Field Name**
   * **Description:** Specifies the document field to be used for determining the matching sub-organization.
   * **Detail:** The card looks for a value in the specified field to match with an available sub-organization.
2. **Sub-Organization (Fallback)**
   * **Description:** Defines the fallback sub-organization to be used if no match is found in the specified field.
   * **Detail:** If the field value does not match any sub-organization, the document will be assigned to the fallback sub-organization selected.

## **Functionality:**

* **Condition Evaluation:**\
  The card only executes its action if both the **"When"** and **"And"** evaluate as true.
* **Dynamic Assignment:**\
  The card checks the value of the specified field and assigns the document to the sub-organization that matches this value.
* **Fallback Mechanism:**\
  If no matching sub-organization is found, the document is assigned to the fallback sub-organization.

## **Setup and Configuration:**

* **Select Field Name:**\
  Choose the field from the document that contains the value to match with a sub-organization.
* **Select Fallback Sub-Organization:**\
  Choose the sub-organization that will be used if no match is found in the document field.

## **Conclusion:**

The **"Assign Document to Matching Sub-Organization Based on Field"** workflow card offers flexibility by dynamically routing documents to the appropriate sub-organization, with an added fallback option to ensure no document is left unassigned.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Choose a business unit from an extracted routing field.

**Configuration:** Set the routing field `business_unit` to the configured suborganization name `Demo North` and choose `Demo Default` as fallback.

**Expected result and counterexample:** A matching field value selects `Demo North`. An unknown name uses `Demo Default`; test the fallback before enabling the workflow.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
