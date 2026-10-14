# Handling Charges with Infor M3

## Overview

This document provides detailed information on how DocBits integrates with Infor M3 to handle charges associated with invoices and purchase orders (PO). It includes scenarios for external charges and the expected solutions.

## Charge Handling Scenarios

| Scenario ID | Description                                                                          | Business Case                                                                                                                          | Expected Solution                                                                                                                                                                                                                         |
| ----------- | ------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1           | External Charges Not on PO but on Invoice (Accepted)                                 | External charges appear on the invoice but are not listed on the PO. These charges are accepted.                                       | Charges will be posted against Accounting Rule PP20-228 based on the cost element sent by DocBits.                                                                                                                                        |
| 2           | External Charges Not on PO but on Invoice (Not Accepted)                             | External charges appear on the invoice but are not listed on the PO. These charges are not accepted or approved.                       | The total invoice value is recorded with a header charge for non-approved charges. Additionally, a debit note is created for these charges.                                                                                               |
| 3           | External Charges on Invoice Greater or Lesser than PO (Within Tolerance)             | External charges on the invoice are greater or lesser than those on the PO but within the accepted tolerance.                          | Extra charges are posted against Accounting Rule PP20-228 based on the cost element sent by DocBits.                                                                                                                                      |
| 4           | External Charges on Invoice Greater than PO (Outside Tolerance, Not Approved)        | External charges on the invoice are greater than those on the PO and outside the accepted tolerance, and they are not approved.        | The invoice is recorded with the total invoice amount. An additional non-approved charge is added as a header charge, and a debit note is created for this additional charge.                                                             |
| 5           | External Charges on Invoice Greater than PO (Outside Tolerance, Approved in DocBits) | External charges on the invoice are greater than those on the PO and outside the accepted tolerance, and they are approved in DocBits. | Extra charges are posted against PP20-228. Two options considered:\<br>- If APS900 tolerance > DocBits, extra charges automatically posted.\<br>- If APS900 tolerance = DocBits, extra charges posted with new charge elements not on PO. |
| 6           | External Charges on Invoice Lesser than PO (Outside Tolerance, Not Approved)         | External charges on the invoice are lesser than those on the PO and outside the accepted tolerance, and they are not approved.         | The invoice is posted as unapproved in APS110. The AP team adjusts the charges through the Invoice Control option in APS110, which calls APS360.                                                                                          |
| 7           | External Charges on PO and No Charge on Invoice                                      | External charges are listed on the PO, but there are no charges on the invoice.                                                        | The invoice is posted as unapproved in APS110. The AP team adjusts the charges through the Invoice Control option in APS110, which calls APS360.                                                                                          |

## Example for Scenario 5

| Field          | PO Value | Supplier Invoice Value |
| -------------- | -------- | ---------------------- |
| Line 1         | $6000    | $6000                  |
| Freight (E001) | $1000    | $3000                  |
| **Total**      | $7000    | $9000                  |

**Tolerance of Freight:** $100 approved automatically in M3 (APS900) and DocBits. Total invoice value of $9000 approved (with charges) manually.

**APS451 (Invoice Line):**

* Line Type 1 (Invoice Line): $9000
* Line Type 5 (Line Charge): $1000 (Element: E001 for Freight on PO $1000)
* Line Type 5 (Line Charge): $2000 (Element: E101 for Freight on PO $0)

### Important Fields and Values for Handling Charges in DocBits

| Field                       | Description                                              |
| --------------------------- | -------------------------------------------------------- |
| Sequence Number             | Unique identifier for each charge scenario               |
| Costing Element ID          | Identifier for the costing element                       |
| Costing Element Description | Description of the costing element                       |
| Charge Type                 | Typically, "External"                                    |
| Charge Invoicing            | Relevance needs to be determined                         |
| Distribution Method         | Method used for distributing the charges                 |
| Gross Weight                | Applicable if gross weight is available on the invoice   |
| Volume                      | Applicable cases need to be defined                      |
| Net Amount                  | Applicable cases need to be defined                      |
| 3rd Party Charge            | Presence on the invoice and processing requirements      |
| Invoice Charge Quantity     | Clarification needed                                     |
| Markup                      | Assumed to be the difference between charge and discount |
| Charge Category             | Relevance needs to be defined                            |
| Costing Operator            | Relevance needs to be defined                            |

\\
