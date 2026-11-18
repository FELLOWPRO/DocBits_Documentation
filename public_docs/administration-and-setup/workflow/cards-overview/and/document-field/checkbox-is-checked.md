# Checkbox is checked

<figure><img src="../../../../../.gitbook/assets/workflow_card_condition_checkbox_is_v2.png" alt="Workflow card Document Field: Checkbox Field Name is checked: Boolean, version 2" width="634"><figcaption><p>Version 2</p></figcaption></figure>

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-checkbox/v1/en.mp4" %}

**Video:** Card: Checkbox is checked · 0:37 · [Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-checkbox/v1/en.vtt)

<details>

<summary>Transcript</summary>

**Checkbox is checked** · [0:00](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-checkbox/v1/en.mp4#t=0.25)

The card Checkbox checks a checkbox field of the document. Choose the field, for example Special handling, and whether it should be checked or not checked.

**Empty means not checked** · [0:16](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-checkbox/v1/en.mp4#t=16.583)

An empty checkbox counts as not checked. If the document has no such checkbox, the card takes its error exit.

**Example: a tick for special handling** · [0:25](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/card-checkbox/v1/en.mp4#t=25.983)

For example, the validator ticks Special handling, and the workflow sends the document to the logistics team. Documents without the tick take the normal path.

</details>

## Purpose:

This workflow card checks whether a checkbox field on the document is checked or unchecked. It can be used to let a workflow continue only after a flag has been set on the document, for example a review flag.

## Components of the Card:

1. **Field Name**
   * **Description:** The technical name of the checkbox field on the document.
   * **Detail:** The field should be a checkbox (Boolean) field of the document type.
2. **Boolean**
   * **Description:** The state the checkbox should have.
   * **Options:**
     * **True:** The checkbox should be checked.
     * **False:** The checkbox should be unchecked.

## Functionality:

* **Condition Evaluation:** When the workflow reaches the card, it reads the current value of the field on the document and compares it with **Boolean**. The card does not watch the field over time and does not change it.
  * An empty checkbox value counts as unchecked.
  * If no **Boolean** value is selected, the card checks for an unchecked checkbox.
  * If the field is not a checkbox field, the card notes this in the workflow log and still compares its value.
* **Action Execution:**
  * **True Condition:**\
    If the checkbox state matches **Boolean**, the workflow continues with the next cards.
  * **False Condition:**\
    If it does not match, the workflow stops with an unmet condition.
* **Missing Data:** If the field does not exist on the document, the card does not evaluate the condition. It reports that the field was not found on the document, which is a different result from an unchecked checkbox.

## Setup and Configuration:

* The card can be added as an And condition from the **Document Field** category. Then the technical name of the checkbox field is entered in **Field Name** and **True** or **False** is selected.
* **Test Card** in the card menu of the Workflow Builder can be used to check the configuration on a document with the checkbox checked, one with it unchecked, and one without the field.

## Conclusion:

The "Checkbox is checked" workflow card turns a checkbox on the document into a workflow condition. This lets a workflow wait for a manual step, such as a completed review, before the following actions run.
