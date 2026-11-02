# Validation for each document type

Administrators decide for each document type whether DocBits validates incoming e-invoices and whether a failed check blocks the document. Every change is confirmed and written to the [change log](validation-change-log.md).

> Only **organisation administrators** can change these settings. Other users see the table read-only, or do not see it.

## The table

Go to **Settings → E-Documents → E-Invoice Validation**. The tab **Rules and policy** starts with the table **Validation for each document type**.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-settings.png" alt="The table Validation for each document type with the switches Enabled and Blocking"><figcaption><p>One row for each document type with the switches Enabled and Blocking. Example organisation.</p></figcaption></figure>

| Switch       | What it does                                                                                                                                                                                                      |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Enabled**  | DocBits validates every incoming e-invoice of this document type and saves a [validation report](validation-report.md).                                                                                           |
| **Blocking** | A finding that is an error stops the document. It gets the status **Error**. When blocking is off, DocBits saves the report and the document continues. You can turn **Blocking** on only when **Enabled** is on. |

If a document type has sub-type overrides, the table shows a note about them.

## Change a setting

1. Select the switch you want to change.
2. DocBits shows **Confirm validation change** with the document type and the change, for example _QUOTE: Enabled → On_.

<figure><img src="../../../../../.gitbook/assets/einvoice-validation-confirm.png" alt="The dialog Confirm validation change"><figcaption><p>Every change needs a confirmation</p></figcaption></figure>

3. Read the note: **Already saved reports do not change.** The change applies only to new checks, including when you restart the processing of a document.
4. Select **Confirm change**, or **Cancel** to keep the old setting.

If you do not have the permission, DocBits shows a message that an organisation administrator is required, and nothing changes.

## Related pages

* [E-Invoice Validation](./)
* [Change log](validation-change-log.md)
* [Validation setup and accepted versions](validation-setup.md)
* [Validation report](validation-report.md)
* [Enable or disable e-invoice validation](../#enable-or-disable-e-invoice-validation)
