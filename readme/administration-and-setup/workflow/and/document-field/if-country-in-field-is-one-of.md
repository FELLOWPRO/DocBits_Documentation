# If Country in Field is One of

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

This workflow card is designed to evaluate whether a specified country, located in a designated field, is part of a predefined list of countries. Based on this evaluation, the workflow can continue with a true or false condition. It helps automate processes where actions depend on whether the country is listed among a set of allowed or restricted countries.

## **Components of the Card:**

1. **Field Name**
   * **Description:** Specifies the document field where the country name or code is stored.
   * **Detail:** This should match the exact field identifier of the country data within the document.&#x20;
2. **Operator**
   * **Description:** Defines whether the country in the field must be part of a predefined list of countries.
   * **Options:**
     * **Is:** The country must be included in the list of specified countries for the condition to be true.
     * **Is Not:** The country must not be included in the list of specified countries for the condition to be true.
3. **Countries**
   * **Description:** Specifies the list of countries against which the selected country will be compared.
   * **Detail:** This is a comma-separated list of countries. The comparison checks if the country in the field is included in this list.
4. **Continue Condition**
   * **Description:** Defines the result of the comparison. If the country meets the condition, the workflow continues with the specified Boolean value.
   * **Options:**
     * **True:** The workflow continues if the condition matches.
     * **False:** The workflow continues if the condition does not match.

## **Functionality:**

* **Condition Evaluation:** The system evaluates whether the country specified in the field is part of the list of predefined countries. This evaluation checks the country name or code against the provided list.
* **Action Execution:**
  * **True Condition:**\
    If the country in the field is part of the specified list of countries, the workflow continues with the true condition. This can trigger further actions, such as routing documents to the appropriate department, applying specific processing rules, or enabling region-specific features.
  * **False Condition:**\
    If the country does not match the list, the workflow continues with the false condition. This allows for executing alternative actions or halting the workflow based on the system setup.

## **Setup and Configuration:**

* Users configure the card by selecting the document field containing the country and specifying the list of countries to check against. The operator is then chosen from a dropdown list to define whether the country must be part of or not part of the specified list of countries. Finally, users set the continue condition (true or false), which dictates the next step in the workflow.

## **Conclusion:**

The "Country in Field Comparison with List" workflow card is a valuable tool for automating actions based on whether a country is part of a predefined group. By comparing the country data with a list of allowed or restricted countries, this card enhances workflow efficiency and ensures that system processes follow the correct geographic rules.
