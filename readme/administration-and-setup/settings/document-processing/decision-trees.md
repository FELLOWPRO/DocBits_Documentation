# Decision Trees

{% embed url="https://youtu.be/omFWSkSjlL0" %}
How to Create a Decision Tree in DocBits (Conditions, Policies, Testing & Export)
{% endembed %}

## Overview

Decision Trees are a powerful feature that allows for the automated routing and decision-making process based on predefined rules. This feature is especially useful in complex environments where various conditions need to be evaluated to determine the correct course of action, such as assigning prices, determining quantities, or routing documents.

#### Key Components

* **Decision Tree List**: This is the main interface where all existing decision trees are listed. Each decision tree can be associated with a specific document type such as an `INVOICE` or `QUOTE`.
* **Decision Tree Designer**: This interface allows for the creation and editing of decision trees, where you can define rules, operators, and actions to be taken when certain conditions are met.

## Decision Tree Interface

#### Decision Tree List

The Decision Tree list displays all the configured decision trees. Open it from **Settings → Document Processing → Decision Trees**.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Decision Trees list"><figcaption><p>The Decision Trees list</p></figcaption></figure>

Each entry shows:

| Column               | Description                                                      |
| -------------------- | ---------------------------------------------------------------- |
| **Name**             | The name of the decision tree. Click it to open the Designer.    |
| **Document Type**    | The document type the tree applies to (e.g. `INVOICE`, `QUOTE`). |
| **Last Modified By** | The user who last edited the tree.                               |
| **Last Modified At** | Timestamp of the last change.                                    |
| **Actions**          | Three-dot menu to edit, copy, export or delete the tree.         |

#### Creating a Decision Tree

1. Click **+ Add Decision Tree** in the top-right corner.
2. Enter a **Name** and select the **Document Type**.
3. Use the Decision Tree Designer (below) to define conditions, policies and results.

#### Importing a Decision Tree

Click **Import Decision Tree** to upload a previously exported decision tree file (JSON format). This is useful for copying a tree between organisations or environments.

## Decision Tree Designer

The Decision Tree Designer allows you to configure rules that govern how decisions are made.

### **Components of the Decision Tree Designer**

* **Rules**: Each rule consists of conditions and actions.
* **Select Source**: This dropdown allows you to specify the source field to evaluate.
* **Select Operator**: Defines the logic operator (e.g., `<=`, `>=`, `=`, `!=`) to be applied to the source field.
* **Result**: Defines the outcome or action that should be taken when the conditions are met.
* **Add New Row**: Allows you to add additional rules to the decision tree.

### Example of a Decision Tree Configuration

This decision tree evaluates the **Total Amount** field and assigns it to different groups based on predefined conditions. Each rule compares the total amount against a specific value, and based on which condition is true, the corresponding **Group** is returned.

<figure><img src="../../../.gitbook/assets/image (335).png" alt="Decision Tree Example Total Amount"><figcaption></figcaption></figure>

This decision tree evaluates two key conditions to determine which group should be assigned: **Total Amount** and **Warehouse Status**. The tree uses thresholds based on the total amount to define which group is returned, with the additional distinction of whether the warehouse is designated as "Warehouse Main," "Warehouse Sub," or "Not Warehouse Main."

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Decision Tree Example Warehouse Status"><figcaption></figcaption></figure>

Each rule is evaluated sequentially.

## Decision Tree Policy

The Decision Tree Policy defines how multiple rules within a decision tree are processed. You can choose from several policies:

* [Unique Policy](decision-trees/unique-policy.md)
* [First Policy](decision-trees/first-policy.md)
* [Priority Policy](decision-trees/priority-policy.md)
* [Collect (sum) Policy](decision-trees/collect-sum-policy.md)
* [Collect (min/max/count) Policy](decision-trees/collect-min-max-count-policy.md)
* [Rule Order Policy](decision-trees/rule-order-policy.md)
* [Any Policy](decision-trees/any-policy.md)
* [First & Adjacent Policy](decision-trees/first-and-adjacent-policy.md)

## **Testing the Decision Tree**

**Overview:** The decision tree designer includes a test feature to validate the logic of the configured rules. This feature allows users to test the decision tree by providing specific input values for the selected fields.

**Steps to Use the Test Feature:**

1.  **Locate the Test Button:**

    * In the decision tree designer, find the **Test** button.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Decision Tree Test Button" width="563"><figcaption></figcaption></figure>
2.  **Open the Test Popup:**

    * Click the **Test** button.
    * A popup window will appear, providing input fields corresponding to the criteria used in the decision tree.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Decision Tree Test Popup" width="421"><figcaption></figcaption></figure>
3. **Provide Input Values:**
   *   Enter values into the input fields to simulate a real-world scenario.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Decision Tree Test Input" width="428"><figcaption></figcaption></figure>
4.  **Evaluate the Results:**

    * After entering the inputs, the tree processes them based on the chosen policy.
    * The system highlights the rule(s) that match the provided inputs.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Decision Tree Test Result" width="563"><figcaption></figcaption></figure>
5. **Review Feedback for No Match:**
   * If no rule is highlighted, the system will display feedback explaining why no rule matched.
   * Use this feedback to adjust inputs or review the tree's configuration for potential issues.

## Export and Save

* **Save**: Saves the current configuration of the decision tree.
* **Export**: Allows you to export the decision tree configuration, which can then be imported into another environment or used for backup purposes.

## Use Cases

* **Approval workflows** — route invoices to different approvers based on amount thresholds (for example, amounts over 10,000 require manager approval).
* **Validation rules** — automatically validate field values and flag documents that do not meet the configured criteria.
* **Sequential assignment** — assign documents to users in a specific order based on conditions.
