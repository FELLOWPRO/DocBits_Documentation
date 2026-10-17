---
description: "Every Advanced Workflow toolbar control, canvas interaction, note function and keyboard shortcut."
---

# Toolbar & Canvas

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
