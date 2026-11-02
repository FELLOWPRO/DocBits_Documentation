# Export not matched PO lines

## Understand export scope with three purchase order lines

<figure><picture><source srcset="../../../../../../.gitbook/assets/intro-process-03-po-export-en-dark-20261029.png" media="(prefers-color-scheme: dark)"><img src="../../../../../../.gitbook/assets/intro-process-03-po-export-en-light-20261029.png" alt="Understand export scope with three purchase order lines"></picture><figcaption><p>Understand export scope with three purchase order lines</p></figcaption></figure>

In this example, the purchase order has three lines and only one is matched to an order confirmation line. With “Export Not Matched PO Lines” off, only the matched purchase order line is exported. With the option on, the two unmatched purchase order lines are included as well. This does not create additional matches.


## **Where to Find It**

Go to **Settings → General Settings → Document Types → More Settings → Purchase Order Section → Export Not Matched PO Lines**.\
Toggle the button to enable this setting.

<figure><img src="../../../../../../.gitbook/assets/image (39).png" alt="Export not matched PO lines setting shown as a switch in the off position with an arrow pointing to it"><figcaption></figcaption></figure>

## **How It Works**

* **When disabled**, the system only exports purchase order lines that are matched with an order confirmation line. Unmatched purchase order lines will not be included in the export.
* **When enabled**, the system exports all purchase order lines, even if they are not matched to an order confirmation line.

For example, if a purchase order has **three lines**, but the supplier sends an **order confirmation with only one line**, you match that line to a purchase order line. The remaining two unmatched purchase order lines will be:

* **Excluded from the export** if the setting is disabled.
* **Included in the export** if the setting is enabled.
