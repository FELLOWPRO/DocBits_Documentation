---
description: "Download a synthetic invoice, workflow JSON, test inputs, expectations and real test responses."
---

# Workflow training kit

Use this kit with the [Advanced case study](advanced-workflow-case-study.md). It includes a synthetic invoice, an importable workflow, seven complete document inputs, independent expectations and actual saved test responses. Technical keys and route names remain identical in every language.

{% file src="../../.gitbook/assets/workflow-training-kit-v2.zip" %}
Workflow training kit with examples and results
{% endfile %}

## Contents and formats

| File | Use |
| --- | --- |
| `training-invoice.pdf` | Synthetic invoice: EUR 1500 net, EUR 285 tax, EUR 1785 total. Not payable. |
| `advanced-workflow.json` | Import through **Import Workflow**; no global variable, restricted to Invoice and the exact training number. Import disabled. |
| `*-input.json` | Complete document data for **Advanced Test → Custom Data**. |
| `expectations.json` | Expected paths, status messages and overall results. A business acceptance specification, not a Test Manager upload. |
| `*-result.json` | Real Dev test responses with node results and messages; private organization references are replaced. |
| `prepare_inputs.py` | Replaces the synthetic organization reference in both required locations. |
| `verify_results.py` | Checks saved responses against independent expectations. Requires Python 3, no access key. |

## Use the kit

1. Extract the ZIP and read the included instructions.
2. Import the workflow into your test organization and verify it is disabled.
3. Find your own test organization's ID and run locally:

```bash
python3 prepare_inputs.py --org-id YOUR_TEST_ORGANIZATION_UUID --out prepared
python3 verify_results.py
```

4. Use files from `prepared/` in the Advanced test dialog. Do not replace a synthetic document ID with a live customer invoice.
5. Check all seven cases against the [result table](advanced-workflow-case-study.md). Amount variations are deliberate test inputs; they do not change the attached invoice.

Data includes `id`, `org_id`, `doc_type`, `status` and `extracted_data` with `layout.groups`, `fields` and `tables`. The organization references at the top level and inside `extracted_data` must match the signed-in account. Values without corresponding layout definitions may not be read as existing document fields.

## Scope of the exercise

The expectation file checks more than a document status: selected paths, route text, status messages and completion nodes. It is different from the status comparison in a saved Test Manager scenario.

A successful Advanced test confirms processing of the supplied test data. Simulated actions are not actual assignment, email or delivery. Activation requires a suitable event entry and a separately verified real run. See [When does my workflow run?](workflow-execution-model.md).

## WF-03: Exercise and acceptance

Extract v2, adapt the organization with prepare_inputs.py and run verify_results.py. Use decision-table-setup.json as setup guidance and acceptance-record-template.json as a record template; neither is a workflow import. Confirm the disabled state before importing.

[Learning path](workflow-learning-path.md)
