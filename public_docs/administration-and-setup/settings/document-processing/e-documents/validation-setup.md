# Validation setup and accepted versions

This page explains the setup wizard, the accepted XRechnung versions and the accepted profiles of the [E-Invoice Validation](validation-rules.md) page. Only organisation administrators can change these settings.

## Validation Setup

<figure><img src="../../../../.gitbook/assets/einvoice-setup-versions.png" alt="Validation setup and accepted versions"><figcaption><p>Validation setup and accepted XRechnung versions</p></figcaption></figure>

The **Validation Setup** card shows your current validation profile (for example *B2G — Public Sector Receiver*). Click **Edit answers** to re-run the setup wizard and change which standard you validate against.

## Accepted XRechnung versions

The **Accepted XRechnung versions** gate lists every XRechnung version. Tick the versions you accept — documents whose CustomizationID falls outside this list are rejected with `VAL-VERSION-NOT-ALLOWED` before any other check. An empty list means "accept everything". Each version is tagged **current**, **deprecated** or **EOL** together with its release date.

## Accepted profiles and severity model

<figure><img src="../../../../.gitbook/assets/einvoice-profiles-severity.png" alt="Accepted profiles and severity legend"><figcaption><p>Accepted profiles and what each severity means</p></figcaption></figure>

Choose which **profiles** you accept (BASIC WL, BASIC, EN 16931 / COMFORT, EXTENDED, XRECHNUNG (CIUS)) using **Accept all** / **Clear**, then **Save**.

Each validation rule has a **severity** that decides what happens when it fires:

| Severity | Effect |
|----------|--------|
| **FATAL** | Stops processing immediately. No subsequent layer is checked; the document goes to Error. |
| **ERROR** | The document is rejected. Other findings on the same document are still surfaced; the supplier notification (if enabled) fires. |
| **WARNING** | Surfaces in the validation report, but the document proceeds through the pipeline normally. |
| **INFO** | Audit-log only. No user-facing effect and no rejection. |

### What the wizard changes

The card **Validation Setup** further down the page opens a wizard with **Edit answers**. The wizard replaces the whole set of rule overrides of your organisation. DocBits warns you before you save. Check the **Review and apply** step carefully.

Next: [Rule severities](validation-rule-severities.md) and [Validation for each document type](validation-per-document-type.md).
