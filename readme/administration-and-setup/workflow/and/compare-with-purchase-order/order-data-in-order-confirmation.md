# Order Data in Order Confirmation

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose**

This workflow card is designed to compare specific fields—**Unit Price**, **Discount**, or **Quantity**—between an order confirmation and a purchase order. It ensures consistency and compliance with agreed terms. Based on the comparison result, the card allows users to write specified text into a chosen field when the condition evaluates as **true** or **false**, streamlining document processing and reducing manual intervention.

## **Components of the Card**

1. **Order Data**
   * **Description:** Specifies the field to be compared between the order confirmation and the purchase order.
   * **Options:**
     * **Unit Price**: Compares the unit price in both documents.
     * **Discount**: Compares the discount percentage or value.
     * **Quantity**: Compares the ordered quantity.
2. **Operator**
   * **Description:** Defines the condition applied during the comparison.
   * **Options:**
     * **Equals (=):** Checks if the value in the selected field matches between the order confirmation and the purchase order.
     * **Not Equals (≠):** Ensures the value in the selected field differs between the two documents.
3. **Text**
   * **Description:** Specifies the text to be written into the target field upon condition evaluation.
   * **Detail:** This text can include custom notes, status updates, or predefined values.
4. **Field Name**
   * **Description:** Specifies the field where the text will be written.
   * **Detail:** The target field is selected from available editable fields within the system.
5. **Condition Result**
   * **Description:** Determines when the text should be written, based on the comparison result.
   * **Options:**
     * **True:** Writes the text if the comparison condition is met.
     * **False:** Writes the text if the comparison condition is not met.

## **Functionality**

* **Comparison Evaluation:** The system compares the selected field between the order confirmation and the purchase order using the specified operator.
* **Action Execution:** If the condition evaluates as **true** or **false**, the specified text is written into the designated field.

## **Setup and Configuration**

* To set up this card, users first select the field to be compared—**Unit Price**, **Discount**, or **Quantity**. Then, they choose an operator to define the comparison condition, such as **equals** or **not equals**. Users specify the text to be written into a target field and select when this action should occur, based on the condition result (**true** or **false**).

## **Example Scenario**

* An order confirmation lists a unit price of $50 for a product, while the purchase order specifies a price of $45. Using the **Not Equals (≠)** operator, the card identifies the discrepancy and writes the text "Price Mismatch" into a designated field when the condition evaluates as **true**.

## **Conclusion**

The "\[Unit Price/Discount/Quantity] in Order Confirmation" workflow card provides a practical solution for ensuring document consistency. By automatically flagging discrepancies and writing relevant text into specified fields, it enhances efficiency and reduces errors in order management processes.
