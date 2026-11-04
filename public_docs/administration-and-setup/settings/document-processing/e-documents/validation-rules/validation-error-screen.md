# The error screen for a rejected e-invoice

When you upload an e-invoice that is wrong, DocBits does not lose it. The document gets the status **Error**, and the error screen tells you what is wrong, where, and what to do next. This page shows two examples: an XML file that is not well-formed, and an invoice that breaks a business rule.

> An invoice gets the status **Error** only when validation is **on** and **blocking** for its document type. See [Validation for each document type](validation-per-document-type.md).

## Example 1: the XML file is damaged

A supplier sends an XML file in which a closing tag does not match its opening tag. The file cannot be read, so DocBits stops at the first check, **L1 · Well-formedness**.

<figure><img src="../../../../../.gitbook/assets/einvoice-error-xml-malformed.png" alt="The error screen for an XML file that is not well-formed: the XML on the left with the faulty line marked, the explanation on the right"><figcaption><p>The error screen for a damaged XML file. The faulty line is marked in the XML. Example file with fictional data.</p></figcaption></figure>

The screen has two sides:

* **Left: the XML file.** DocBits shows the file with line numbers. The line with the problem is marked in red. Use the buttons above the file to copy the XML or open it in a new tab.
* **Right: the explanation.** The card **Rejected by** names the check that stopped the file (here **L1 · Well-formedness**) and the rule code (here `XML-PARSE`). Below you see a title in plain language (_XML is not well-formed_), a short explanation and the block **Next step**.

Select **View validation details** to open the full [validation report](validation-report.md).

<figure><img src="../../../../../.gitbook/assets/einvoice-report-xml-malformed.png" alt="The validation report of the damaged XML file with the finding XML-PARSE"><figcaption><p>The report of the damaged file: one error at level 1 Syntax, with the technical message and the position</p></figcaption></figure>

The report names the exact position (here line 5, column 4081) and gives the technical message of the XML parser. Select **Show in XML** to jump to that line. The hint **How to fix** tells you to ask the sender for a corrected file.

## Example 2: the invoice breaks a business rule

The XML is fine, but a required field is missing. For example, the seller cannot be identified because no seller identifier, registration identifier or VAT identifier is present (rule `BR-CO-26`).

<figure><img src="../../../../../.gitbook/assets/einvoice-error-view.png" alt="The error screen for an invoice that breaks a business rule"><figcaption><p>The error screen for a business-rule error: the layer <strong>L3 · Business Rules</strong>, the rule code and a next step</p></figcaption></figure>

Here the card names the layer **L3 · Business Rules** and the code `BR-CO-26`. The report lists all findings of the invoice, see [Validation report](validation-report.md).

## The buttons below the card

| Button                 | What it does                                                                                                             |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| **Restart Processing** | Runs the processing of the document again, for example after you changed a setting. The check uses the current settings. |
| **View DocFlow**       | Shows the workflow of the document.                                                                                      |
| **Copy Details**       | Copies the error details, for example for a message to your administrator.                                               |
| **Create ticket**      | Opens a support ticket with the error details.                                                                           |

Select **Show technical details** on the card for the raw technical information.

## What to do next

* **Errors:** ask the sender for a corrected invoice, or [reject the document](validation-next-step-and-reject.md). A corrected invoice is a new document.
* **Only warnings:** the document is not blocked. You can continue.

## Related pages

* [Validation report](validation-report.md): all findings, level by level.
* [Next step and reject a document](validation-next-step-and-reject.md)
* [Validation for each document type](validation-per-document-type.md): turn validation on and set blocking.
