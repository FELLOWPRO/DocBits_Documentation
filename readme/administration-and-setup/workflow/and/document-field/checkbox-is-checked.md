# Checkbox is checked

<figure><img src="../../../../.gitbook/assets/image (20) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Purpose:**

This workflow card is designed to automate actions based on the state (checked or unchecked) of a checkbox within your ERP system. By evaluating the checkbox's condition, it facilitates the triggering of specific processes or the enforcement of certain rules within the application.

## **Components of the Card:**

* **Field Name**
  * **Description:** Specifies the name of the checkbox field that will be evaluated.
  * **Detail:** This should match the exact field identifier used in the system. It determines which checkbox's state is being monitored.
* **Boolean**
  * **Description:** Defines the condition that triggers the workflow.
  * **Options:**
    * **True:** The workflow triggers if the checkbox is checked.
    * **False:** The workflow triggers if the checkbox is unchecked.

#### **Functionality:**

* **State Detection:** The card continuously monitors the state of the specified checkbox field.
* **Condition Evaluation:** The system checks whether the checkbox is in the state (checked or unchecked) specified by the Boolean condition.
* **Action Execution:**
  * **True Condition:**\
    If the checkbox’s state matches the specified Boolean condition (either true for checked or false for unchecked), the system initiates the associated actions. These could include enabling or disabling form fields, triggering notifications, starting workflows, or updating records.
  * **False Condition:**\
    If the checkbox’s state does not match the condition, alternative or no actions may be taken, depending on the workflow setup.

## **Setup and Configuration:**

* Users configure the card by selecting the checkbox field from a list of available fields and setting the Boolean condition.&#x20;

## Conclusion :

The "Checkbox Field Condition" workflow card is a fundamental tool for managing dynamic forms and documents within an ERP system, where user inputs can dictate subsequent data processes. By automating actions based on the state of a checkbox, this card enhances workflow efficiency and ensures that system behaviors align with user inputs. Clear documentation of this card will help users effectively implement it within their operations, allowing for better control over form behaviors and process automations.



**Note: Not every customer has the checkbox, but it can be added if desired.**
