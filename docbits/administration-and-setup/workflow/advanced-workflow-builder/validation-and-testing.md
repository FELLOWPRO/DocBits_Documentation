# Validation & Testing

While you build an Advanced Workflow, two controls in the toolbar let you check it without leaving the builder. These are for *quick checks during building* — for saved, repeatable tests, use the [Test Manager](../test-manager.md).

## Validate

Click the **Validate** control (the check-circle icon, or press <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>V</kbd>). Validation checks the graph for problems — unconnected nodes, missing configuration and invalid connections — and points them out so you can fix them before the workflow runs on real documents.

## Test

Click the **Test** control (the play icon, or press <kbd>Cmd/Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>T</kbd>) to run the current flow against a sample and watch how it behaves, without affecting live documents. This is the fastest way to sanity-check a change you just made on the canvas.

## When to use which

- **Validate / Test in the builder** (this page) — instant feedback while you are designing the flow.
- **[Test Manager](../test-manager.md)** — save the scenario so you can re-run it later (and together with all your other scenarios) to catch regressions after future changes.

## Next steps

- Review the node types and connections in [Nodes](nodes.md).
- See all toolbar and canvas controls in [Toolbar & Canvas](toolbar-and-canvas.md).
