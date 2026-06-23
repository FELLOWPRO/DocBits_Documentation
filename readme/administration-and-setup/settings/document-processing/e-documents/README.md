# E-Documents

DocBits validates incoming electronic invoices (e-invoices) against the official standards — **XRechnung**, **ZUGFeRD** and **Factur-X** — and routes any problems it finds to the right handler. The **E-Documents** settings group (under **Document Processing**) has two pages:

* **[Validation Rules](validation-rules.md)** — choose which e-invoice versions and profiles you accept, and set the severity of each validation rule for your organization.
* **[Notification Routing](notification-routing.md)** — map validation findings to the AI Workforce agent that should handle them.

Together they let you decide **what counts as a problem** on an incoming e-invoice and **who deals with it**.

## Enable or disable e-invoice validation

The two E-Documents pages only take effect once **e-invoice validation is switched on for the document type**. The switch lives on the document type itself, not in the E-Documents menu.

Go to **Settings → Document Types → Invoice → Advanced Settings** and open the **E-Invoice Validation** section.

<figure><img src="../../../../.gitbook/assets/edoc_enable_validation_toggle.png" alt="The E-Invoice Validation toggles on the Invoice document type"><figcaption><p>Turn e-invoice validation on or off per document type, with optional supplier notification</p></figcaption></figure>

* **Validate incoming e-invoices** — the master switch. When **on**, every uploaded invoice is checked against the KoSIT XRechnung Schematron rules plus the L0 PDF/A-3 and L4 IBAN/VAT semantic checks, using the severities you set on the [Validation Rules](validation-rules.md) page. Invalid invoices are blocked. When **off**, invoices skip e-invoice validation entirely and the Validation Rules and Notification Routing pages have no effect.
* **Notify supplier on rejection** — appears once validation is enabled. When **on**, a rejected invoice triggers an email to the supplier listing the missing or incorrect fields so they can reissue it. Who receives and handles each finding is configured on the [Notification Routing](notification-routing.md) page.

> E-invoice validation is configured **per document type**. Today it applies to the **Invoice** document type; enable it on each document type that should be validated.

You can also jump straight here with **Global Quick Search**: press <kbd>Cmd</kbd> + <kbd>K</kbd> (<kbd>Ctrl</kbd> + <kbd>K</kbd> on Windows and Linux) anywhere in DocBits and type *e-invoice*.

<figure><img src="../../../../.gitbook/assets/edoc_quicksearch_einvoice.png" alt="Global Quick Search jumping to E-Invoice Validation"><figcaption><p>Type "e-invoice" in Quick Search to jump straight to the toggle.</p></figcaption></figure>
