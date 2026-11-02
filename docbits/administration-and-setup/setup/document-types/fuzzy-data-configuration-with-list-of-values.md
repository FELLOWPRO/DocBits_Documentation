---
hidden: true
---

# Fuzzy Data Configuration with List of Values

### **Overview**

Each document type has its own List of Values (LoV) configurations, which must be set up separately. Unlike **Fuzzy Data with Master Data**, **List of Values** does not come with default lookup groups.

### To configure List of Values, navigate to:

Settings → Global Settings → Document Types → Invoice → Fields → Master Data Settings → LOV Master Data

### **Creating a New List of Values Configuration**

There are two ways to create a List of Values configuration:

**1. Duplicate an Existing Lookup**

* This copies all information and fields from an existing group.
* You only need to provide a **new name**.

**2. Create a Lookup from Scratch**

* Click **"Create List of Values"**.
* Fill in the required details:
  * **Configuration Name** → Name of the List of Values.
  * **Lookup Table** → The table from which values will be retrieved.
  * **Conflict Handler** → Choose one:
    * Best Score
    * Return None
    * Return First
  * **Context Type** → Determines if the LoV applies to the **Header** or **Line** level.
  * **Match All** → _(More details needed)_

### **Managing Fields Within a List of Values Group**

Each LoV group contains fields that can be **added, removed or edited.**

**Adding a New Field**

To add a new field within a group:

* Click **"Create"** inside the relevant group.
* Provide the following details:
  * **Lookup Field** → The column name from the lookup table.
  * **Validation Field** → The corresponding DocBits field.
  * **Parent Field** → _(More details needed)_
  * **Search Operator** → Choose one:
    * Smart
    * Contains
    * Exact
    * Starts with
    * Ends with
  * **Checkboxes:**
    * **Auto Trigger** → When enabled, if another field in a different lookup configuration shares the same column, this field will update **automatically** whenever the other field is updated.
    * **Searchable** → Enables the field as a **List of Values** field, allowing searches in the lookup table.

#### **Final Step: Adding Fields to the Layout**

After configuring List of Values fields, **make sure to add them to the layout using the Layout Builder**. If fields are not added to the layout, they will not be available for use.
