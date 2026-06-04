# Validation & Testing

Before you rely on an Advanced Workflow, use the toolbar controls to confirm it is correct and behaves as expected.

## Validate

Click the **validate** control (the check-circle icon, or press <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Validation checks the graph for problems — unconnected nodes, missing configuration and invalid connections — so you can fix them before the workflow runs on real documents.

## Test

Click the **test** control (the play icon, or press <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) to run the workflow against a sample and see how it behaves, without affecting live documents.

## Test scenarios

For repeatable checks, save **test scenarios** in the **Test Manager** (see the [Dashboard](../workflow-dashboard.md)). Each scenario records an expected outcome and shows a pass/fail result, and **Run All Tests** re-runs them together — so you can confirm your workflows still behave correctly after a change.

<figure><img src="../../../.gitbook/assets/workflow_test_manager.png" alt="Workflow Test Manager List with test scenarios and Run All Tests"><figcaption><p>The Test Manager — saved scenarios with pass/fail results and <strong>Run All Tests</strong>.</p></figcaption></figure>

## Next steps

- Review the node types and connections in [Nodes](nodes.md).
- See all toolbar and canvas controls in [Toolbar & Canvas](toolbar-and-canvas.md).
