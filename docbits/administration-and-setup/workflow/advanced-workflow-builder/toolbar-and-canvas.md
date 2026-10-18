---
description: "Every Advanced Workflow toolbar control, canvas interaction, note function and keyboard shortcut."
---

# Toolbar & Canvas

## Video: Builder and canvas

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v2/en.vtt) · 1:38

<details>
<summary>Transcript</summary>

**An invoice with two routes**

Here is a real Advanced Workflow in DocBits. An invoice amount check leads to two actions. The connections define which action runs. This example uses an unsaved draft and demonstration fields.

**Configure the amount check**

Open Add, choose And, and select a Document Field condition. Set the amount field, choose Greater Than, and enter one thousand. Use the exact field key from your document configuration.

**Configure the actions**

Add two Then cards. Each card sets the demonstration field approval route. One writes Approval; the other writes Standard. These values label the route. Configure your business actions for a production workflow.

**Connect the result outputs**

Connect Start to the condition input. Connect blue Success to Approval, and orange Failed Condition to Standard. The red Error output handles evaluation errors separately. Card position alone does not create a route.

**Prepare the test cases**

Open Test in the toolbar. Choose a test document, or enter complete document data as JSON. Check amounts above, below, and exactly at one thousand. Also check missing values. Inspect the node results after execution.

**Validate, save and activate**

Validate the connections and card settings. Save explicitly to write the workflow to the server, then check activation separately. Automatic browser drafts do not replace Save. Execution and log access require the appropriate module and subscription.

</details>

[Watch all five chapters](videos.md)

Use the bottom toolbar to configure the workflow and the canvas to arrange nodes. Panning, zooming and card positions change the view or layout. Connections determine execution.

## Every toolbar control

Controls follow their left-to-right order.

| Control | Purpose and result |
| --- | --- |
| **+ Add** | When, And, Then, existing Start, Wait ALL, Wait ANY, OR and Note. See [Nodes](nodes.md). |
| **Undo / Redo** | Undo or repeat supported canvas edits. Does not roll back executed actions or independently saved organization variables. |
| **Zoom out / Zoom in** | Change the view scale. |
| **Workflow Name** | Name the workflow before saving. |
| **Edit description** | Explain the business purpose and exceptional routes. |
| **Automatic-save indicator** | Shows the last local draft save after changes; not a server-save confirmation. |
| **Variables — { }** | Open the organization-wide [variables](variables.md). |
| **Help — ?** | Shortcuts, path highlighting and connection legend. |
| **Validate — check-circle** | Report graph errors and warnings. |
| **Test — play-circle** | Choose test input for the current canvas. See [testing](validation-and-testing.md). |
| **Snap to grid** | Toggle alignment when moving nodes. |
| **Mini-map** | Show or hide an overview for large graphs. |
| **Export Image** | Download a diagram image. This is not an importable workflow configuration or execution recording. |
| **Save — disk** | Write the workflow to the server. Wait for confirmation. |
| **Activate / Deactivate — toggle** | Change the enabled state of a saved workflow. Unavailable before the first save; review any unsaved-change prompt. |
| **Hide toolbar — down arrow** | Hide it. Use the remaining up arrow to restore it. |

The current toolbar does not expose a separate Logs or Save as Template button. Open [Workflow Logs](../workflow-logs.md) from the document. Workflow List configuration import/export is separate from Export Image.

## Navigate and select

- Drag the blank background to pan; use wheel, pinch or zoom buttons to change scale.
- Drag a node to move it. Connections remain attached.
- Click a node to highlight incoming and outgoing paths; unrelated nodes dim.
- **Shift + drag** selects an area. **Cmd/Ctrl + click** adds/removes a node from the selection.
- Right-click the background for Add. The node context menu offers editing actions for the selection.

Connectivity highlighting is different from [execution evidence](../workflow-logs.md).

## Edit nodes and notes

Copy, paste or duplicate a selection to reuse a configured section, then check its fields and connections. Review the selection before deleting: removing a node also removes its connections and can disconnect a downstream path. Undo/redo corrects canvas edits.

Use **Note** to explain a decision, owner or configuration context. Edit its text and use the available color and size controls to keep it readable. Notes are annotations, not execution steps or logs.

## Keyboard shortcuts

Use **Cmd** on macOS and **Ctrl** on Windows/Linux. Finish typing in an input before using canvas-editing shortcuts. **?** opens the application's current reference.

<figure><img src="../../../.gitbook/assets/advanced_workflows_help_en.png" alt="Help dialog showing the keyboard shortcut reference"><figcaption><p>Built-in help provides the current editing shortcuts. Scroll to the connection legend or select Card setup for field-name guidance.</p></figcaption></figure>

| Shortcut | Action |
| --- | --- |
| **Cmd/Ctrl + S** | Save to server. |
| **Cmd/Ctrl + Shift + V** | Validate. |
| **Cmd/Ctrl + Shift + T** | Open testing. |
| **Cmd/Ctrl + Z** | Undo. |
| **Cmd/Ctrl + Shift + Z** | Redo. |
| **Cmd/Ctrl + C / V / D** | Copy / paste / duplicate selected nodes. |
| **Cmd/Ctrl + A** | Select all nodes. |
| **Shift + drag** | Area selection. |
| **Cmd/Ctrl + left-click** | Add/remove one node from selection. |
| **Right-click** | Open context menu. |
| **Delete** | Delete selection. |
| **?** | Open help. |

Before leaving, [validate, test and save](validation-and-testing.md). A local draft and an exported image do not replace a saved workflow.
