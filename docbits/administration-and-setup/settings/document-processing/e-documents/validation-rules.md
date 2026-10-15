# E-Invoice Validation

The **E-Invoice Validation** page (**Settings → E-Documents → E-Invoice Validation**, path `/settings/einvoice-validation`; earlier called *Validation Rules*) controls how DocBits validates incoming e-invoices. It is based on the official **KoSIT XRechnung + ZUGFeRD** rule set plus the validator's in-house finding codes, and lets you override the severity of each rule for your organization.

> This page is for **e-invoices** (XRechnung, ZUGFeRD, Factur-X). It is not the same as **Data Validation Rules**, which check extracted document fields.

## What is on this page

<figure><img src="../../../../.gitbook/assets/einvoice-validation-settings.png" alt="The E-Invoice Validation page with the table Validation for each document type"><figcaption><p>The E-Invoice Validation page. The tab <strong>Rules and policy</strong> starts with the table <strong>Validation for each document type</strong>. Example organisation.</p></figcaption></figure>

| Topic | What it does | Who |
| --- | --- | --- |
| [Validation setup and accepted versions](validation-setup.md) | The setup wizard, the accepted XRechnung versions, the accepted profiles and what each severity means. | Organisation administrators |
| [Rule severities](validation-rule-severities.md) | The rule table: change the severity of each rule for your organisation. | Organisation administrators |
| [Validation for each document type](validation-per-document-type.md) | Turn validation on (**Enabled**) and decide whether a failed check stops the document (**Blocking**). Every change needs a confirmation. | Organisation administrators |
| [Change log](validation-change-log.md) | Every change of the settings: when, who, which rule, from → to. | Organisation administrators |
| [The error screen for a rejected e-invoice](validation-error-screen.md) | What you see when you upload a wrong XML: the explanation, the faulty line and the next step. | Everyone who processes invoices |
| [Validation report](validation-report.md) | What a user sees when an invoice fails: the findings in plain language. It opens from the document, not from this page. | Everyone who processes invoices |
| [Next step and reject a document](validation-next-step-and-reject.md) | What to do after you read the report, downloads of the report, and **Reject document**. | Everyone who processes invoices |
