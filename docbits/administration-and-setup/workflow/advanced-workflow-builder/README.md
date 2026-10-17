---
description: "Build, connect, test, save and activate document workflows with alternative routes and merge nodes."
---

# Advanced Workflows

An **Advanced Workflow** routes a document through a graph of triggers, conditions and actions. Use it when the next action depends on a result, several checks feed a common action, or an error needs its own handling path. **Connections determine execution order**; placing a card farther to the right does not make it run later.

Use a [Standard Workflow](../standard-workflow-builder/README.md) for a linear **When → And → Then** automation. Both builders use the same [card catalog](../cards-overview/README.md). The advanced builder adds explicit connections and control nodes.

## Watch: builder and canvas

Start with the narrated introduction to creating and editing an Advanced Workflow. Choose English or German. The videos use labelled teaching diagrams; the screenshots below show the application interface.

{% tabs %}
{% tab title="English" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v1/en.mp4" %}

[Captions (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v1/en.vtt) · [Read the transcript](videos.md#builder-and-canvas)
{% endtab %}

{% tab title="Deutsch" %}
{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v1/de.mp4" %}

[Untertitel (WebVTT)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/advanced_workflows_canvas/v1/de.vtt) · [Transkript lesen](videos.md#builder-and-canvas)
{% endtab %}
{% endtabs %}

Continue with the [five-part video guide](videos.md) for nodes and routes, variables and testing, finding log entries and diagnosing an execution. Every chapter includes English and German narration, caption files and a transcript.

## Open or create an Advanced Workflow

1. Open **Workflow Dashboard → Workflow List**.
2. Select **New Workflow → Advanced Workflow**. Some versions label the button **Add Workflow**.
3. Enter a name in the toolbar. Add a description that explains the business purpose.
4. Use the automatic **Start** node for a manual entry point, or add a **When** card for an event trigger.
5. Add and configure conditions and actions. Connect their appropriate result handles.
6. [Validate and test](validation-and-testing.md), save explicitly and check the enabled state.

The Workflow Builder module and Advanced Workflow option must be enabled for the organization, and the required subscription must be available. If the creation option is missing or an operation is refused, ask your administrator to check both module access and licensing. Opening a designer URL alone does not establish execution or log access.

<figure><img src="../../../.gitbook/assets/advanced_workflows_canvas_en.png" alt="Advanced Workflow canvas with its automatic Start node and bottom toolbar"><figcaption><p>Start provides the manual entry. The toolbar adds nodes, configures the workflow, validates, tests, saves and activates it.</p></figcaption></figure>

## Building blocks

| Building block | Purpose | Details |
| --- | --- | --- |
| **Start / When** | Start a manual test or respond to an event. Entry nodes have no input. | [Nodes](nodes.md) |
| **And** | Route success, false condition and error separately. | [Condition cards](../cards-overview/condition-cards-complete-guide.md) |
| **Then** | Perform an action, such as assigning a task or setting a field. Actions can connect to further actions. | [Action cards](../cards-overview/then/README.md) |
| **Wait ALL / Wait ANY / OR** | Merge incoming routes according to their results. | [Merge rules](nodes.md#merge-branches) |
| **Note** | Explain the design without executing an operation. | [Toolbar and canvas](toolbar-and-canvas.md) |
| **Variables** | Share typed values that compatible cards can read or update. | [Variables and scope](variables.md) |

<figure><img src="../../../.gitbook/assets/advanced_workflows_add_menu_en.png" alt="Add menu with When, And, Then, Start, Wait ALL, Wait ANY, OR and Note"><figcaption><p>The available node types. Start is already present and cannot be added a second time from this menu.</p></figcaption></figure>

## Example: route a high-value invoice for approval

1. Choose the appropriate invoice event in a **When** card.
2. Add an **And** card that compares the invoice amount with the threshold. Configure its field, comparison and value.
3. Connect the trigger to the condition's input.
4. Connect **blue success** to a **Then** card that creates or assigns an approval task.
5. Connect **orange failed condition** to the intended normal-processing action.
6. Connect **red error** to a separate handling action if evaluation fails.
7. Test an amount above the threshold, below it, at the exact boundary and with missing or invalid data.

Connections create the behavior. Two unconnected actions do not create alternatives. A false condition is also different from an execution error.

{% hint style="info" %}
An Advanced Workflow can continue through an explicitly connected **Failed Condition** route. The Standard Workflow rule that stops remaining linear cards after a false condition does not apply to the entire advanced graph.
{% endhint %}

## Save, activation and automatic drafts

**Save** writes the workflow to the server. The activation switch changes the enabled state of a saved workflow and is unavailable before the first save. Check the resulting state in **Workflow List**, including after the first save. Saving and checking activation are separate steps.

The automatic-save indicator refers to a **local browser draft**, normally stored every 30 seconds after changes. It does not replace a server save. A draft belongs to that browser and can expire after 24 hours. A restore prompt can appear after a reload; a newer server version can make an old draft stale. Save explicitly before relying on the workflow from another session.

Organization variables persist independently. Discarding a canvas draft does not undo a variable change.

## Complete guide

- [Video guide](videos.md): five narrated chapters in English and German, with captions and transcripts.
- [Toolbar and canvas](toolbar-and-canvas.md): every control, selection, editing, notes and shortcuts.
- [Nodes and connections](nodes.md): entry points, versions, result handles, merges and connection rules.
- [Variables](variables.md): all four types, organization scope and immediate persistence.
- [Validation and testing](validation-and-testing.md): structural checks, document and custom input, results and regression scenarios.
- [Workflow Logs](../workflow-logs.md): inspect document executions and their messages.
