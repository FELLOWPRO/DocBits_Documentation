# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../../.gitbook/assets/image (381).png" alt="Workflow Action card labelled AI Calculation for Cost Increase Surcharges" width="563"><figcaption></figcaption></figure>

## When to use this card

Use this action to request the configured MTZ/ETZ material- and energy-surcharge calculation for the current document. Prepare the document data and calculation-service configuration required by your organization first.

## Actual configuration

The displayed card has no Cost Increase Factor, Base Cost Field or Surcharge Field inputs. It delegates calculation to the configured service. Do not look for these nonexistent card controls or assume a fixed percentage formula from the card name.

## Result and verification

A successful service response marks the card successful. A timeout or unsuccessful response produces a card error. Inspect the card log and the document's resulting surcharge data; success of the call alone does not document a particular amount.

In card-testing mode, the call is skipped and success is simulated. This is useful for testing the workflow structure, but it does not prove that the service ran or any surcharge was calculated.

<!-- workflow-card-practical-example-20261021 -->

## Practical example

**When to use:** Request the configured material/energy-surcharge calculation for a prepared invoice.

**Configuration:** Use synthetic invoice `DEMO-001` with the data required by your configured MTZ/ETZ service. Add this action after the document-validation conditions.

**Expected result and counterexample:** A successful service response marks the card successful; a timeout or unsuccessful response produces a card error. Inspect the document fields and calculation result separately. Card-testing mode simulates success and does not call the service, so it cannot prove a real surcharge result.

This is an illustrative configuration and expected outcome. Use fields, users and groups configured in your test organization; it is not a claim that this example was executed.
