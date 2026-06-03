# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to evaluate whether a specified country, located in a designated field, is part of a particular trade or political area (European Union, Schengen Area, or NAFTA). Based on this evaluation, the workflow can continue with a true or false condition, enabling further actions within the system. It is particularly useful for automating region-specific business rules, ensuring compliance, or triggering specific workflows based on geographical affiliations.

## **Components of the Card:**

1. **Field Name**
   * **Description:** Specifies the document field where the country name or code is stored.
   * **Detail:** This should match the exact field identifier of the country data within the document.&#x20;
2. **Operator**
   * **Description:** Specifies whether the country in the selected field should match or not match the selected region or agreement.
   * **Options:**
     * **Is:** The country must be part of the selected agreement (EU, Schengen, or NAFTA) for the condition to be true.
     * **Is Not:** The country must not be part of the selected agreement for the condition to be true.
3. **Country Comparison**
   * **Description:** Defines whether the country in the field is checked against a specific political or trade agreement.
   * **Options:**
     * **European Union:** The card checks if the country is a member of the European Union.
     * **Schengen Area:** The card checks if the country is part of the Schengen Area.
     * **NAFTA:** The card checks if the country is a member of the NAFTA agreement.
4. **Boolean**
   * **Description:** Defines the result of the comparison. If the country meets the condition, the workflow continues with the specified Boolean value.
   * **Options:**
     * **True:** The workflow continues if the condition matches.
     * **False:** The workflow continues if the condition does not match.

## **Functionality:**

* **Condition Evaluation:**
  * The system evaluates whether the country specified in the field is part of the chosen region or agreement (EU, Schengen Area, or NAFTA) based on the operator selected. This evaluation checks the country name or code against a predefined list of countries that belong to each respective group.
* **Action Execution:**
  * **True Condition:** If the country in the field matches the selected region (as per the operator), the workflow continues with the specified true condition. This can trigger further actions, such as routing documents, applying special processing rules, or enabling region-specific features.
  * **False Condition:** If the country does not match the selected region (as per the operator), the workflow continues with the specified false condition, allowing for the execution of alternative actions or terminating the workflow based on the system setup.

## **Setup and Configuration:**&#x20;

* Users configure the card by selecting the document field containing the country and specifying the region (European Union, Schengen Area, or NAFTA). The operator is then chosen from a dropdown list to define whether the country must be part of or not part of the selected region. Finally, users set the continue condition (true or false), which dictates the next step in the workflow.

## **Conclusion:**

The "Country in Field Comparison" workflow card is an essential tool for automating processes that depend on geographical rules, such as compliance with trade agreements or political affiliations. By comparing country data with specific regions like the European Union, Schengen Area, or NAFTA, this card ensures that the system applies the right processing logic, improving efficiency and ensuring accurate workflow execution based on geographical conditions.
