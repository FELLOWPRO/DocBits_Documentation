# Test Manager

The **Test Manager** lets you save reusable **test scenarios** for your workflows and run them together — so you can confirm that a workflow still behaves correctly after you change it. It works for both Standard and Advanced workflows.

Open it from **Workflow Dashboard → Test Manager List**.

<figure><img src="../../.gitbook/assets/workflow_test_manager.png" alt="Test Manager List with test scenarios, status and Run All Tests"><figcaption><p>The Test Manager List — each saved scenario shows a pass/fail result.</p></figcaption></figure>

## What a test scenario is

A test scenario captures a workflow, a sample input and the **expected outcome**. When you run it, the Test Manager replays the workflow against that input and compares the result to what you expected — turning the row **green** (pass) or **red** (fail).

## Working with scenarios

- **Add Test Scenario** — create a new scenario from a workflow and a sample document.
- **Run All Tests** — run every scenario at once and see, at a glance, which workflows still pass.
- **View Details** — open a scenario to inspect its result.

<figure><img src="../../.gitbook/assets/workflow_test_manager_detail.png" alt="Workflow test scenario details with status, run time and data"><figcaption><p>Scenario details — name, status, run time, and the actual vs. extracted data the run produced.</p></figcaption></figure>

The details view shows the scenario name and **status**, the **workflow name**, the **run time**, and the **actual** and **extracted data** the run produced — so you can see exactly why a scenario passed or failed.

## Test Manager vs. testing in the builder

These are two different things:

- **Test Manager** (this page) — *saved, repeatable* scenarios with expected outcomes, run together with **Run All Tests**. Use it for regression testing after changes.
- **Testing in the builder** — the inline **Validate** and **Test** controls inside the Advanced Workflow builder, for quick checks while you are building. See [Validation & Testing](advanced-workflow/validation-and-testing.md).
