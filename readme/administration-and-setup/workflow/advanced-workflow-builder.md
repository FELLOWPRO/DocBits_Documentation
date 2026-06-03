# Advanced Workflow

The **Advanced Workflow** builder is a node-graph editor for workflows that need branching, parallel paths and flow control — beyond the linear When/And/Then of the Standard builder. You arrange nodes on a canvas and connect them to define the execution flow.

## How to access

Open the Advanced Workflow designer from the workflow area (the advanced builder canvas). You start from a **Start** node and build out the flow by adding nodes.

<figure><img src="../../.gitbook/assets/workflow_advanced_canvas.png" alt="Advanced Workflow node-graph canvas with toolbar"><figcaption><p>The Advanced Workflow canvas — a node graph with zoom, run, grid and save controls. Give the workflow a name in the toolbar.</p></figcaption></figure>

## Adding nodes

Click **+ Add** to open the node menu. In addition to the familiar **When**, **And** and **Then** cards, the advanced builder adds flow-control nodes:

<figure><img src="../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Advanced Workflow Add menu with node types"><figcaption><p>The <strong>+ Add</strong> node menu: When / And / Then plus Wait ALL, Wait ANY, OR and Note.</p></figcaption></figure>

- **When / And / Then** — the same condition and action cards as the Standard builder.
- **Wait ALL** — wait until *all* incoming branches complete before continuing.
- **Wait ANY** — continue as soon as *any* incoming branch completes.
- **OR** — branch the flow down alternative paths.
- **Note** — a free-text annotation on the canvas (does not affect execution).

Run the flow with the play control, validate it, and save with the save button in the toolbar.

## Next steps

- See what each card does in the **Cards** section.
- For simple linear automations, the **Standard Workflow** builder is faster to set up.
