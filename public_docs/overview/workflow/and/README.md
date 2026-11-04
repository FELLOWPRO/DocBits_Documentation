# And

## Understanding "And" Cards

### **Purpose of 'And' Cards:**

* **And** cards serve as condition cards that specify criteria that must be met for the workflow to continue. They effectively act as logical "AND" operators, meaning all conditions specified in these cards must be satisfied for the subsequent action to be triggered.

#### Categories of 'And' Cards

From the screenshots, it's clear that these cards cover a wide range of conditions, which include:

*   **Compare with Purchase Order**:

    * Conditions related to validation and comparison against purchase orders, such as comparing delivery dates, unit prices, or quantity differences. These are crucial for ensuring that transactions align with agreed terms.



<figure><img src="../../../../.gitbook/assets/And1.png" alt=""><figcaption></figcaption></figure>

*   **Document Field**:

    * These involve conditions based on specific fields within documents, such as checkboxes being marked, comparison of field values, or ensuring a document field meets a specified tolerance. This is particularly important for data integrity and automated checks within forms or document management systems.



<figure><img src="../../../../.gitbook/assets/And2.png" alt=""><figcaption></figcaption></figure>

* **Document**:
  * Conditions based on document characteristics, such as type or association with a particular sub-organization. These conditions can direct workflows based on document categorization or departmental involvement.

<figure><img src="../../../../.gitbook/assets/And3.png" alt=""><figcaption></figcaption></figure>

* **Logic**:
  * Logical conditions that might involve evaluations like "Continue with a chance of X%" or executing HTTPS requests, which are vital for integrations and probabilistic decision-making within workflows.

<figure><img src="../../../../.gitbook/assets/And4.png" alt=""><figcaption></figcaption></figure>

*   **Status**:

    * Focusing on the status of documents or tasks, these conditions ensure that only items in certain states trigger specific workflows, crucial for status-driven process management.



<figure><img src="../../../../.gitbook/assets/And5.png" alt=""><figcaption></figcaption></figure>

* **Table**:
  * These involve conditions based on table data, such as matching regex patterns or comparing values within a table. Such conditions are essential for validating and manipulating large data sets.

<figure><img src="../../../../.gitbook/assets/And6.png" alt=""><figcaption></figcaption></figure>

*   **Assignee**:

    * Conditions based on task or document assignees. This ensures that actions are only taken when certain users are involved, enhancing accountability and task specificity.



<figure><img src="../../../../.gitbook/assets/And7.png" alt=""><figcaption></figcaption></figure>

#### Practical Application

These "And" cards are configured within the workflow to perform checks and validations that ensure the process adheres strictly to business rules and data integrity standards. For example:

* **A workflow might use an 'And' card to verify that an invoice's total amount matches the purchase order before triggering payment.**
* **Another workflow could use an 'And' card to ensure a document is reviewed by specific team members before it progresses to the next stage.**

#### Conclusion

"And" cards are a fundamental component of workflow systems that require precise control over process execution based on multiple conditions. They ensure that each step of a workflow only proceeds when all necessary criteria are thoroughly met, thus automating complex decision trees within business processes.

Understanding and configuring these cards correctly is crucial for leveraging the full capabilities of your workflow management system to enhance efficiency, accuracy, and compliance within organizational processes.

