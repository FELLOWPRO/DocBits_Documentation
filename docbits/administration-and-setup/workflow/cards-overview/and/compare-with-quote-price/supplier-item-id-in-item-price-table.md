# Supplier Item ID in Item Price Table

<figure><img src="../../../../../.gitbook/assets/workflow_card_condition_quote_supplier_item_number_exists_v2.png" alt="Supplier Item ID in Item Price Table, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

## Purpose:

This workflow card checks whether the supplier item IDs on the lines of a document can be found in the supplier item price table. It can be used to find out whether DocBits holds price data for the items on a quote, for the document's supplier, before other quote comparisons run, or to route documents with unknown items to a manual check. Based on the result, the workflow continues with the true or the false condition.

## Components of the Card:

1. **Any/All**
   * **Description:** Defines whether one line or every line of the document table should meet the condition.
   * **Options:**
     * **Any:** The condition is true if at least one line meets the condition.
     * **All:** The condition is true only if every line meets the condition.
2. **Operator**
   * **Description:** Defines whether the supplier item ID should be found in the supplier item price table or not.
   * **Options:**
     * **Is:** A line meets the condition if its supplier item ID is in the supplier item price table.
     * **Is Not:** A line meets the condition if its supplier item ID is not in the supplier item price table.

## Functionality:

* **Condition Evaluation:** The card reads the supplier item ID (column `SUPPLIER_ITEM_NUMBER`) of every line in the document table and checks whether the supplier item price table contains an entry for it. The results of all lines are then combined with **Any** or **All**.
* **Validity Dates:** If an entry in the supplier item price table has a start or end date and the document date lies outside that period, the card notes this in the workflow log. This note does not change the result of the card.
* **Action Execution:**
  * **True Condition:**\
    With **Is**, the supplier item IDs (any or all, as selected) are in the supplier item price table. With **Is Not**, they are not. The workflow continues with the true condition, for example to continue with the price comparison.
  * **False Condition:**\
    If the condition is not met, the workflow continues with the false condition, for example to send the document for a manual review.
* **Missing Data:** If the document has no table, has more than one table, no lines could be read from the table, or the document has no supplier item price data at all, the card does not evaluate the condition and reports the missing data in the workflow log. If no **Any/All** option is set, the card notes this in the log and uses **All**.
* **Errors:** The card ends with an error if a line of the table has no `SUPPLIER_ITEM_NUMBER` column. If no operator is set, the card reports a setup error.

## Setup and Configuration:

* The card can be added from the **Compare with Quote Price** category. After that, **Any** or **All** and the operator (**Is** or **Is Not**) can be selected. Finally, the continue condition (true or false) is set, which determines the next step in the workflow.
* The card works on documents with exactly one table, whose lines carry the supplier item ID.

## Conclusion:

The "Supplier Item ID in Item Price Table" workflow card shows whether the items on a document are known in the supplier item price table. It can serve as a first check in a quote workflow, so that the later price, item number and unit of measure comparisons only run for documents whose items have price data.
