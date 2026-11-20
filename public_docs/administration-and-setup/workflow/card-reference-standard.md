---
description: "Configure cards reliably using their name, version, inputs, data scope, results and side effects."
---

# Understand and configure workflow cards

Choose a card by its operation and data scope. **Field is** checks presence or empty state; **Docfield is** compares a value. Document assignment, a task and a notification have different effects. A category name does not replace the reference for a specific card version.

## What a complete reference explains

| Component | Required question |
| --- | --- |
| Identity | What is the visible name, technical type, version and When/And/Then role? |
| Prerequisites | Which license, permissions and document data are required? |
| Inputs | What type, value, default and allowed choices does each parameter accept? |
| Scope | Does it read a field, row, every item or an organization-wide variable? |
| Results | What means success, false or error? What can the next card consume? |
| Side effects | Are documents, tasks or external systems changed? What does testing simulate? |
| Examples | Which complete configuration and input produces which result? |
| Limits and versions | What happens with missing data, exact boundaries and older versions? |

## Filled example: Docfield is

**Technical type:** `condition_docfield_operator_value` · **Version:** 2 · **Role:** And. Requires a document with a defined layout and the field to check.

| Input | Example configuration |
| --- | --- |
| Field Name | `total_amount`, the technical key rather than its translated label |
| Operator | `gt` / Greater Than |
| Field Value | `1000`, without a currency symbol |

The card reads the current document's field and compares it with the configured value. It does not change status, create a task or export. In Advanced, true continues through Success, normally false through Failed Condition, and an evaluation error through Error. In Standard, a condition that is not met stops the linear sequence.

Actual checked cases: **1785** → Success; **999** and **1000** → Failed Condition; **1000.01** → Success; missing or invalid numeric data → Error. JSON uses decimal points. These results describe this numeric configuration, not every type and operator.

Distinguish this card from explicit tolerance cards. Do not infer equality or inclusive-operator behavior solely from `gt`; test the required combination with its own boundaries.

## Suitable next steps

Connect success to review, false to standard processing, and error to data correction. The [complete case study](advanced-workflow-case-study.md) includes configuration, subsequent cards and real test results. The [execution model](workflow-execution-model.md) explains saving and activation; [troubleshooting](workflow-troubleshooting.md) helps investigate different outcomes.

## WF-05: Exercise and acceptance

Document Run Workflow and a PO comparison card using the same structure. Include parameters, inspected code defaults, paths, effects and version limits. Specifically check inactive targets, absent data and the percentage reference.

[Learning path](workflow-learning-path.md)
