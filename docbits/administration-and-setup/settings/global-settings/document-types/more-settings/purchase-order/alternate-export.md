# Alternate Export

## Overview

You can configure an alternate export option to appear in the export dropdown within the purchase order section when a document is in a specific status.\
This page explains how to set up this option.

## Activation Steps

1. Go to **Settings** -> **Global Settings** -> **Document Types**
2.  Select the desired document type and open its settings with the gear icon.

    <figure><img src="../../../../../../.gitbook/assets/site-complete-invoice-export-settings-en.png" alt="Current English invoice Export Settings with Alternate Export, eligibility Status and Export Configuration. Test is an existing example configuration; no settings changed or export performed."><figcaption><p>Current English invoice Export Settings with Alternate Export, eligibility Status and Export Configuration. Test is an existing example configuration; no settings changed or export performed.</p></figcaption></figure>
3.  Expand **Export Settings** and locate **Alternate Export**.



## How to set up

Once the setting is enabled, you can choose a document status and assign a predefined export configuration.

More information on setting up export configurations can be found [here](../../../../document-processing/export/).

You can choose between the following statuses:

* Classified
* Pending confirmation
* Pending approval
* Pending second approval
* Validated, pending export
* Approved pending export
* Rejected
* Exported
* On hold
* Workflow
* Error
* In Review

After setup, an additional export option will appear in the purchase order matching export options. This option uses the specified export configuration when the document matches the defined status.
