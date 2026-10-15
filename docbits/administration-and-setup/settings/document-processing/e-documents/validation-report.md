# Validation report

When DocBits rejects an e-invoice, you can read exactly why. The **validation report** lists every finding in plain language, tells you what to fix, and shows the next step. You open it from the document, not from the settings. The screen where you find it is described in [The error screen for a rejected e-invoice](validation-error-screen.md).

This page is for people who process invoices. Administrators set up the rules on the [E-Invoice Validation](validation-rules.md) page and choose per document type whether a failed check blocks the invoice, see [Validation for each document type](validation-per-document-type.md).

## When a document gets an error

If validation is **on** and **blocking** for the document type, an invoice with a blocking finding gets the status **Error**. Open the document from the dashboard. The error view shows the XML on the left and the reason on the right.

<figure><img src="../../../../.gitbook/assets/einvoice-error-view.png" alt="The error view of a rejected e-invoice with the XML on the left and the reason on the right"><figcaption><p>The error view: the XML of the invoice and the first blocking finding with a next step. Example invoice with fictional names.</p></figcaption></figure>

The card on the right names the layer that rejected the invoice (for example **L3 · Business Rules**), the rule code (for example `BR-CO-26`), a short explanation and a **Next step**. Select **View validation details** to open the full report.

## Read the report

<figure><img src="../../../../.gitbook/assets/einvoice-report-top.png" alt="The top of the validation report with file data, the verdict and the result per level"><figcaption><p>The top of the report: file data, the verdict and the result for each level</p></figcaption></figure>

The report starts with the facts about the file:

| Field | What it shows |
| --- | --- |
| **Reference** | The file name of the invoice. |
| **Time of check** | When DocBits ran the check. A saved report does not change later. |
| **Document type / profile** | The format of the invoice, for example CII and EN 16931. |
| **Rule sets** | The version of the rule sets that DocBits used. |
| **Seller** | The seller, read from the XML. |
| **Number / date** | The invoice number and the invoice date, read from the XML. |

Below the file data you see the **verdict**, for example **Not conformant**, with the number of errors, warnings and information messages. If your organisation changed the severity of a rule, a second line **Organisation severity** shows the counts after your organisation's settings.

### Result per level

The table **Result per level** shows how many errors, warnings and information messages each check found. The checks build on each other:

| Level | What it checks |
| --- | --- |
| **1 Syntax** | The XML is well-formed. |
| **2 Schema** | The structure follows the official XML schema. |
| **3 Business rules** | Required fields are present and correct (rules `BR-…`). |
| **4 Cross-check rules** | Fields agree with each other, for example sums. |
| **5 CIUS rules (XRechnung)** | The additional German XRechnung rules. |
| **Other rules** | Further rules, for example the PEPPOL rules. |
| **Value checks of DocBits** | Checks that DocBits adds, for example IBAN and VAT ID. |

> For invoices in the EN 16931 or EXTENDED profile, the XRechnung-specific rules are shown as **warnings**, not as errors.

## The findings

<figure><img src="../../../../.gitbook/assets/einvoice-report-findings.png" alt="The list of findings with code, level, plain-language text, how to fix and Show in XML"><figcaption><p>Each finding has a code, a level, a text you can read and a hint how to fix it</p></figcaption></figure>

Each finding is one row:

* **Pos** and **Code**: the position in the report and the rule code, for example `BR-CO-26`.
* **Level**: **Error**, **Warning** or **Information**.
* **Your organisation**: the level after your organisation's settings. A dash means your organisation did not change the level.
* **Field and text**: the problem in plain language, the field it concerns (for example *BT-29 Seller identifier*), the technical message of the validator, and **How to fix**.
* **Line** and **Show in XML**: select **Show in XML** to close the report and jump to the line in the XML viewer.

DocBits has plain-language texts for the most common rules. For a rule without such a text, the report shows the technical message of the validator.

## Next

* [Next step and reject a document](validation-next-step-and-reject.md): what to do after you read the report.

## Related pages

* [E-Invoice Validation](validation-rules.md): accepted versions, profiles and the severity of each rule.
* [Validation for each document type](validation-per-document-type.md): turn validation on and set blocking.
* [Notification Routing](notification-routing.md): who handles which finding.
