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

| Column | Description |
|--------|-------------|
| **Name** | The name of the decision tree. Click it to open the Designer. |
| **Document Type** | The document type the tree applies to (e.g. `INVOICE`, `QUOTE`). |
| **Last Modified By** | The user who last edited the tree. |
| **Last Modified At** | Timestamp of the last change. |
| **Actions** | Three-dot menu to edit, copy, export or delete the tree. |

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

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Decision Tree Example Total Amount"><figcaption></figcaption></figure>

This decision tree evaluates two key conditions to determine which group should be assigned: **Total Amount** and **Warehouse Status**. The tree uses thresholds based on the total amount to define which group is returned, with the additional distinction of whether the warehouse is designated as "Warehouse Main," "Warehouse Sub," or "Not Warehouse Main."

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Decision Tree Example Warehouse Status"><figcaption></figcaption></figure>

Each rule is evaluated sequentially.

## Decision Tree Policy

The Decision Tree Policy defines how multiple rules within a decision tree are processed. You can choose from several policies:

### **1. Unique Policy**

Ensures that only a single rule is matched. If multiple rules are matched, the decision tree will return false.

**Example:**

| Rule | Condition            | Return Group |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

If the total amount is **1500**, the rules evaluated will be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (matches)
* **Rule 3**: Total Amount <= 5000 (matches)
* **Rule 4**: Total Amount <= 4000 (matches)
* **Rule 5**: Total Amount <= 3000 (matches)

Since multiple rules are matched (**Rule 2**, **Rule 3**, **Rule 4**, **Rule 5**), the decision tree will return **false** because the **Unique** policy ensures only one rule can match.

### **2. First Policy**

The first matching rule is applied, and no further rules are evaluated.

**Example:**

| Rule | Condition            | Return Group |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

If the total amount is **1500**, the rules evaluated will be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (matches) → The decision tree stops evaluating further rules and applies **GROUP_2**.

### **3. Priority Policy**

Choosing this option allows you to set priorities for each rule. The lower the selected number, the higher the priority (i.e., priority 1 has the highest priority). Rules are evaluated based on their priority order. The highest priority matching rule will be applied.

**Example:**

<table><thead><tr><th width="137">Rule</th><th width="110">Priority</th><th width="268">Condition</th><th>Return Group</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

If the total amount is **1500**, the rules evaluated will be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (matches)
* **Rule 3**: Total Amount <= 3000 (matches)
* **Rule 4**: Total Amount <= 4000 (matches)
* **Rule 5**: Total Amount <= 5000 (matches)

Since the priority is applied in the order **5, 4, 3, 2, 1**, the highest priority matching rule will be **Rule 5** (**GROUP_5**). The decision tree will return **GROUP_5** because **Rule 5** has the highest priority (priority 1).

### **4. Collect (sum) Policy**

This policy collects all matching rules and sums the results. It only works for **Return Type Value**.

**Example:**

| Rule | Condition            | Return Value |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

For the input value of **Total Amount = 3500**, the evaluation of rules would be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (does not match)
* **Rule 3**: Total Amount <= 3000 (matches, Return Value = 3)
* **Rule 4**: Total Amount <= 4000 (matches, Return Value = 4)
* **Rule 5**: Total Amount <= 5000 (matches, Return Value = 5)

Since the **Collect (sum)** policy is applied, we sum the **Return Values** of the matching rules, which are **3, 4, 5**.

**Summing these values** gives:

* 5 + 4 + 3 = **12**

Thus, the result returned by the decision tree would be **12**, which is the sum of all matching return values.

### **5. Collect (min/max/count) Policy**

This policy collects all matching rules and either selects the **minimum**, **maximum**, or **counts** the occurrences. It only works for **Return Type Value**.

**Example:**

| Rule | Condition            | Return Value |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. If the **Collect (min)** option is selected, the result will return the **minimum** of the **Return Values** for the matching rules.
   * For the input value of **Total Amount = 3500**, the evaluation of rules would be:
     * **Rule 1**: Total Amount <= 1000 (does not match)
     * **Rule 2**: Total Amount <= 2000 (does not match)
     * **Rule 3**: Total Amount <= 3000 (matches, Return Value = 3)
     * **Rule 4**: Total Amount <= 4000 (matches, Return Value = 4)
     * **Rule 5**: Total Amount <= 5000 (matches, Return Value = 5)
   * The **matching rules** are Rule 3, Rule 4, and Rule 5, with **Return Values** of **3, 4, and 5**.
   * Since the **Collect (min)** policy is applied, the result will be the **minimum value**, which is **3**.
   * **Result**: **3**
2. If the **Collect (max)** option is selected, the result will return the **maximum** of the **Return Values** for the matching rules.
   * For the same evaluation as above, the result will be:
   * **Result**: **5**
3. If the **Collect (count)** option is selected, the result will count the **number of matching rules**.
   * For the same evaluation as above, the result will be:
   * **Result**: **3** (since 3 rules matched).

### **6. Rule Order Policy**

This policy applies rules in the order they appear in the decision tree and returns the result of the rule that matches first.

**Example:**

| Rule | Condition            | Return Group |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Given that the input value is **Total Amount = 3500**, the evaluation of the rules would be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (does not match)
* **Rule 3**: Total Amount <= 3000 (matches)
* **Rule 4**: Total Amount <= 4000 (matches)
* **Rule 5**: Total Amount <= 5000 (matches)

Under **Rule Order**, the tree will process the rules in the order they are listed. So, the matching rules will be:

* **Rule 3**: GROUP_3
* **Rule 4**: GROUP_4
* **Rule 5**: GROUP_5

**Result**: **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Any Policy**

Multiple rules can be true, but the result of those rules must be the same.

**Example:**

| Rule | Condition            | Return Group |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

If the total amount is **2500**, the rules evaluated will be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (does not match)
* **Rule 3**: Total Amount <= 3000 (matches)
* **Rule 4**: Total Amount <= 4000 (matches)
* **Rule 5**: Total Amount <= 5000 (matches)

For **Any** to apply, all matching rules must return the same **Return Group**. Since the groups do not match across the different rules, the result would be **false**.

### **8. First & Adjacent Policy**

Chooses the result of the rule that is adjacent to the first rule that is true.

**Example:**

| Rule | Condition            | Return Group |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

If the total amount is **1500**, the rules evaluated will be:

* **Rule 1**: Total Amount <= 1000 (does not match)
* **Rule 2**: Total Amount <= 2000 (matches)

Since **Rule 2** is the first rule that matches, **First & Adjacent** would apply the result of **Rule 3**: **GROUP_3**.

## **Testing the Decision Tree**

**Overview:**
The decision tree designer includes a test feature to validate the logic of the configured rules. This feature allows users to test the decision tree by providing specific input values for the selected fields.

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
