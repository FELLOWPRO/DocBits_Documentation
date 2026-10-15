# Validation for each document type

Administrators decide for each document type whether DocBits validates incoming e-invoices and whether a failed check blocks the document. Every change is confirmed and written to a change log.

> Only **organisation administrators** can change these settings. Other users see the table read-only, or do not see it.

## The table

Go to **Settings → E-Documents → E-Invoice Validation**. The tab **Rules and policy** starts with the table **Validation for each document type**.

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings.png" alt="The table Validation for each document type with the switches Enabled and Blocking"><figcaption><p>One row for each document type with the switches Enabled and Blocking. Example organisation.</p></figcaption></figure>

| Switch | What it does |
| --- | --- |
| **Enabled** | DocBits validates every incoming e-invoice of this document type and saves a [validation report](validation-report.md). |
| **Blocking** | A finding that is an error stops the document. It gets the status **Error**. When blocking is off, DocBits saves the report and the document continues. You can turn **Blocking** on only when **Enabled** is on. |

If a document type has sub-type overrides, the table shows a note about them.

## Change a setting

1. Select the switch you want to change.
2. DocBits shows **Confirm validation change** with the document type and the change, for example *QUOTE: Enabled → On*.

<figure><img src="../../../../.gitbook/assets/einvoice-validation-confirm.png" alt="The dialog Confirm validation change"><figcaption><p>Every change needs a confirmation</p></figcaption></figure>

3. Read the note: **Already saved reports do not change.** The change applies only to new checks, including when you restart the processing of a document.
4. Select **Confirm change**, or **Cancel** to keep the old setting.

If you do not have the permission, DocBits shows a message that an organisation administrator is required, and nothing changes.

## Change log

The tab **Change log** lists every change.

<figure><img src="../../../../.gitbook/assets/einvoice-validation-change-log.png" alt="The Change log tab with the columns When, Who, Rule, From to To and Action"><figcaption><p>The change log of an organisation without changes yet</p></figcaption></figure>

| Column | What it shows |
| --- | --- |
| **When** | The time of the change. |
| **Who** | The user who made the change. |
| **Rule** | The setting or rule that changed. |
| **From → To** | The old and the new value. |
| **Action** | The kind of change. Rows from the setup wizard can be opened to see the single changes. |

The list shows 50 entries on each page.

## Setup wizard

The card **Validation Setup** further down the page opens a wizard with **Edit answers**. The wizard replaces the whole set of rule overrides of your organisation. DocBits warns you before you save. Check the **Review and apply** step carefully.

## Related pages

* [E-Invoice Validation](validation-rules.md)
* [Validation report](validation-report.md)
* [Enable or disable e-invoice validation](README.md#enable-or-disable-e-invoice-validation)
