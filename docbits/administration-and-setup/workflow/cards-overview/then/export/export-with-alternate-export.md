# Export with alternate Export

<figure><img src="../../../../../.gitbook/assets/image (362).png" alt="Workflow Then card that exports the document using an alternate export" width="563"><figcaption></figcaption></figure>

## When to use this card

Use this Then action for the alternate export configured on the current document type. Configure and validate that route before adding the action.

## Configuration comes from the document type

The card has no export-configuration selector. It reads whether alternate export is enabled, the alternate export configuration and the status after export from the document-type settings. Internally these are `DOC_ALTERNATE_EXPORT_SETTING`, `DOC_ALTERNATE_EXPORT_EXPORT_CONFIG` and `DOC_ALTERNATE_EXPORT_STATUS`.

An explicitly disabled alternate export produces a failed condition. Missing activation data, configuration or result status is reported rather than silently substituting the default route. The export request checks pending tasks.

## Verify the result

Inspect the card log, export history, document status and authorized test destination. A request, timeout or status change alone does not establish that data reached the destination. Check export history before retrying an operation that could create duplicates.

<!-- workflow-card-complete-example-20261021 action_alternate_export -->

### Alternate export example

**Configuration:** Prepare synthetic document type `DEMO_INVOICE` with alternate export enabled, an authorized test export configuration and the desired result status in its document-type settings. Add this Then action after the required checks. This card reads those settings; it does not offer an export-configuration selector.

**Expected result and counterexample:** The action requests export through that alternate configuration and checks pending tasks. Verify the export result and test destination separately. Disabling alternate export causes a failed condition; an absent activation setting or configuration is not a successful export. Do not run this example against an accounting destination.

This is an illustrative test configuration and expected outcome; it was not executed. Use data and recipients configured in your test organization.
