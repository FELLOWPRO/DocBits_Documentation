# Assign User to Supplier

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_user_to_supplier_v2.png" alt="Assign User to Supplier, Version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

## Purpose:

This workflow card sets the assigned user of a registered supplier. The assigned user is the internal contact responsible for the supplier. The card does not work on a document: it is meant for workflows that are started by a change of a supplier's status, for example with the When card **Supplier status changed**. The supplier whose status changed is the supplier the user is assigned to.

## Components of the Card:

1. **User**
   * **Description:** The user who becomes the assigned user of the supplier.
   * **Detail:** One user of the organization can be selected. If the supplier already has an assigned user, that user is replaced.

## Functionality:

* **Action Execution:** The card takes the supplier from the workflow run and saves the selected user as the supplier's assigned user. The result is recorded in the workflow log.
* **Use with Emails:** Once a user is assigned, emails can be addressed to this user with the option **User assigned to supplier**, for example in the card **Send Email**.
* **Missing Data:** If no user is selected on the card, the card does not run and reports the missing data in the workflow log.
* **Errors:** If the supplier service rejects the request or does not answer in time, the card ends with an error.

## Setup and Configuration:

* The card can be used in a workflow that is started by a change of a supplier's status.
* The card can be added from the **Assignee** category. After that, the user who should be responsible for the supplier is selected in the **User** field.

## Conclusion:

The "Assign User to Supplier" workflow card gives every supplier a responsible contact automatically when its status changes, for example after registration. Later steps, such as emails to the assigned user, can build on this assignment.
