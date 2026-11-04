# In Order Confirmation Purchase Order

### Compare with Purchase Order:&#x20;

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Logic Card: Quantity or Unit Price or Discount Match

This logic card is designed to automatically verify that the quantity, unit price, or discount detailed in an order confirmation matches the corresponding figures in the purchase order. This verification ensures consistency and accuracy between what was ordered and what the supplier confirms to deliver.

#### Trigger Condition

The logic is activated when any of the following conditions are met in an order confirmation relative to the original purchase order:

* **Quantity**: The quantity of items ordered matches the quantity confirmed by the supplier.
* **Unit Price**: The price per item agreed upon matches the supplier's confirmation.
* **Discount**: Any discounts applied are consistent between the purchase order and the order confirmation.

#### Outcomes

* **Equals**: If the order confirmation's quantity, unit price, or discount exactly matches the purchase order, the system considers the confirmation as valid and proceeds with the next steps in the procurement process.
* **Not Equal**: If there's a discrepancy in the quantity, unit price, or discount, the system flags the order confirmation for manual review. This ensures any mismatches are resolved before moving forward.

#### Benefits

* **Accuracy and Consistency**: Maintains accuracy in the procurement process, ensuring that payments and deliveries are made based on correct figures.
* **Efficiency**: Automates the verification process, reducing the need for manual checks and speeding up order processing.
* **Cost Control**: Helps prevent overpayments or incorrect deliveries by catching discrepancies early in the process.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Define Comparison Parameters**: Set up the specific fields (quantity, unit price, discount) that the logic card will check for a match.
2. **Automate Verification**: Configure the system to automatically compare these details upon receipt of an order confirmation.
3. **Customize Alerts**: Decide on the workflow for handling discrepancies, including customization of alerts for manual review.

This logic card is vital for ensuring that the details of an order confirmation align with the original purchase order, safeguarding the integrity of the procurement cycle. \`\`

