# Any / All Charges

<figure><img src="../../../../.gitbook/assets/workflow_cards_and_po_compare_any_all_charges.png" alt="The card in the Add Card library, version 2 and version 3"><figcaption><p>The card in the Add Card library. Version 2 above, version 3 below.</p></figcaption></figure>

## **Purpose:**

This workflow card compares the additional charges on a document against the additional charges on the matched purchase order, within a defined tolerance. It answers one question: do the document and the purchase order agree about the additional costs? Every charge that purchase order matching paired up is compared, so no field name has to be named on the card.

This card is distinct from **Compare Total Charges**, which compares one named document field against a single charge identified by a Charge ID. Use this card when every paired charge on the document should be checked at once.

Purchase order matching has to run before this card. If the document has no matched purchase order the card stops the workflow and reports missing data.

## **Components of the Card:**

1. **Any / All:**
   * **Description**: How the individual charge comparisons are combined into the single result of the card.
   * **Options**:
     * **Any**: at least one charge has to satisfy the comparison.
     * **All**: every charge has to satisfy the comparison.
2. **Operator:**
   * **Description**: How each document charge amount is compared against the purchase order amount for the same charge.
   * **Options**:
     * **Within**: the two amounts have to agree, allowing for the tolerance.
     * **Outside**: the two amounts have to differ by more than the tolerance.
3. **Tolerance Amount:**
   * **Description**: The variance allowed between the document charge and the purchase order charge.
4. **Tolerance Type:**
   * **Description**: How the tolerance amount is interpreted.
   * **Options**:
     * **Percentage**: a percentage of the purchase order charge.
     * **Value**: a fixed amount.
5. **Missing Data Behaviour (version 3 only):**
   * **Description**: What to do when a charge exists on only one side, document or purchase order, so there is no counterpart to compare it against. The option sits at the end of the version 3 sentence.
   * **Options**:
     * **treat as a mismatch**: the workflow stops. This is the default.
     * **ignore it and treat as a match**: the workflow continues as if the charge agreed.

## **How the card works:**

The card runs through the following steps.

1. **It requires a matched purchase order.** With no matched purchase order the card stops immediately and reports missing data.
2. **It reads the tolerance** from the **Tolerance Amount** and **Tolerance Type** set on the card.
3. **Version 3 sorts every matched purchase order line** into one of four situations, by asking only whether each side carries any charge at all: charges on both sides, no charges on either side, charges on the document only, or charges on the purchase order only. A line that cannot be resolved against the purchase order data on the document is a data error and the card stops.
4. **A charge on one side only settles the whole card.** As soon as one matched line carries charges on one side and none on the other, **Missing Data Behaviour** decides the result and no charge is compared at all, including the charges on lines that are properly paired. The operator and the tolerance are not consulted.
5. **If no line has charges on either side**, both sides agree there are no additional costs. The **Outside** operator is not satisfied by that, because nothing differs beyond the tolerance, so the workflow stops. Any other operator treats the agreement as satisfied and the workflow continues. **Missing Data Behaviour** has no effect here.
6. **Otherwise each charge is compared**, document amount against purchase order amount, using the operator and the tolerance. A charge amount that is not a number stops the card with missing data.
7. **The comparisons are pooled and combined once.** Every charge on every matched line contributes to one set of results, which the **Any / All** setting reduces to the single result of the card. The pooling is document-wide, not per line, so **Any** means any charge anywhere on the document. If the combined result is true the workflow continues, otherwise it stops with an unmet condition.

Three consequences are worth knowing before configuring the card.

* **Within with a tolerance of 0 requires exact equality.** The two amounts have to match to the cent.
* **A charge on one side only overrides everything else.** Because step 4 runs before any comparison, **ignore it and treat as a match** also skips the amount check on every properly paired charge in the document. Keep **treat as a mismatch** if the amounts have to be verified.
* **treat as a mismatch stops the workflow as an error, not as an unmet condition.** Despite the wording, the card reports missing data, which the workflow log and the card test show in red rather than in the orange used for an unmet condition. The workflow stops either way.

## **Setup and Configuration:**

Add the card as an And condition after purchase order matching. Choose whether every charge or any charge has to satisfy the comparison, pick the **Within** or **Outside** operator, and enter the tolerance amount and type. On version 3, choose what should happen when charges appear on one side only.

To try a configuration without waiting for a document, open the card menu in the Workflow Builder, choose **Test Card**, pick a document and select **Test on Document**. The card log lists every charge that was compared with both amounts, the operator and the tolerance used, and it also records which **Missing Data Behaviour** value resolved the result when a charge was present on one side only.

## **Example Scenario:**

An order confirmation carries a freight charge of 100.00 and the matched purchase order line carries the same freight charge of 100.00. With **All**, the **Within** operator and a tolerance of 0 as a value, the amounts are equal, the card passes and the workflow continues.

With 120.00 on the order confirmation against 100.00 on the purchase order, the same configuration is not satisfied and the workflow stops with an unmet condition.

If neither the order confirmation nor the purchase order carries any charge, the **Within** operator treats that as agreement and the workflow continues, while the **Outside** operator stops it.

If the order confirmation carries a freight charge and the purchase order carries none, the operator no longer applies. With **treat as a mismatch** the workflow stops so somebody can check why the charge is on one side only.

## **Version Differences:**

Version 3 is what new cards use. Version 2 remains supported on existing workflows. Both versions compare per charge and combine the results document-wide with the **Any / All** setting, but version 2 has no case classification, which changes what happens whenever charges are not present on both sides:

* Version 2 has no **Missing Data Behaviour** option. Its sentence ends after the tolerance type.
* Version 2 does not sort the matched lines, so it does not recognise a charge that exists on one side only. It compares the amount that is there against the 0.00 held for the missing side, and the operator decides: **Within** is not satisfied and the workflow stops, **Outside** is satisfied and the workflow continues. The card log shows the comparison against 0.00.
* With no charges on either side there is nothing for version 2 to compare, so it reports missing data instead of treating the absence on both sides as agreement.

## **Conclusion:**

The "Any / All Charges" card automates the check that the additional costs invoiced or confirmed match the additional costs ordered. Because absence of charges on both sides counts as agreement on version 3, documents without additional costs pass without manual intervention, while charges that appear on only one side are held back for review unless that is deliberately allowed.
