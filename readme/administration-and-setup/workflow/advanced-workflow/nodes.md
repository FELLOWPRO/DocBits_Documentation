# Nodes

An Advanced Workflow is a graph of **nodes** connected by edges. You add nodes from the **+ Add** menu (or right-click the canvas) and connect them to define the execution flow.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Add node menu with the available node types"><figcaption><p>The <strong>+ Add</strong> node menu — the available node types.</p></figcaption></figure>

## Node types

- **Start** — the entry point of the workflow. Added automatically; every flow begins here.
- **When** — a trigger card, the same as in the Standard builder.
- **And** — a condition card. It evaluates to true or false and can branch the flow.
- **Then** — an action card that performs work (set fields, create tasks, call APIs, …).
- **Wait ALL** — waits until *all* incoming branches complete before continuing.
- **Wait ANY** — continues as soon as *any* incoming branch completes.
- **OR** — branches the flow down alternative paths.
- **Note** — a free-text annotation on the canvas; it does not affect execution.

The **When / And / Then** nodes use the exact same cards described in the [Cards](../cards-overview.md) section.

## Connecting nodes

Nodes are connected by **colored edges**. Drag from a handle on the **right** side of a node to the input handle on the **left** side of another node to create a connection. Each colour indicates a different execution outcome:

- **Success** (blue) — the default path taken when a node completes successfully. Available on all node types.
- **Failed Condition** (orange) — taken when a condition evaluates to false. Available on **And** (condition) nodes.
- **Error** (red) — taken when a node encounters an error during execution. Available on **And** and **Then** (action) nodes.

## Execution path highlighting

Click any node to see its execution path. All nodes leading into it and all nodes following from it are highlighted — everything else is dimmed. For **Wait ALL** nodes, every incoming branch is shown so you can see exactly what the gate waits for before continuing.

## Next steps

- Pass data between nodes with [Variables](variables.md).
- Check and run your flow with [Validation & Testing](validation-and-testing.md).
