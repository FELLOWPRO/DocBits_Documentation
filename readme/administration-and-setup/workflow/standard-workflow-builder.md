# Standard Workflow

The **Standard Workflow** builder is the linear, card-based editor for automating document processing. A workflow is made of three groups of cards — **When** (the trigger), **And** (additional conditions) and **Then** (the actions to run). When a document matches the When/And conditions, the Then actions run automatically.

## How to access

Open **Workflow Dashboard → Workflow List**, then click **Add Workflow** to create a new Standard workflow, or click an existing workflow to edit it.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Workflow List with type, execution order and trigger"><figcaption><p>The Workflow List — each row is a workflow you can open, toggle on/off or edit.</p></figcaption></figure>

## The When / And / Then model

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="Standard Workflow canvas with When, And and Then cards"><figcaption><p>The Standard Workflow canvas. This example triggers on invoices in a sub-organization and assigns them to a user.</p></figcaption></figure>

- **When** — the trigger that starts the workflow (e.g. *Document type is Invoice*).
- **And** — extra conditions that must also be true (e.g. *Document is part of sub-organization*). Leave empty to run on every match of the When card.
- **Then** — the actions to perform (e.g. *Assign the document to the user*, create a task, call an API, send an email).

## Adding cards

Click **Add Card** in any group to open the card library. Cards are organised by category so you can find the building block you need:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Add Card library grouped by category"><figcaption><p>The <strong>Add Card</strong> library — condition cards, comparison cards, action cards and more, grouped by category.</p></figcaption></figure>

Save with **Save Workflow**, or save the layout as a reusable template with **Save Template**.

## Next steps

- See what each card does in the **Cards** section.
- Combine cards into proven solutions with the **Workflow Pattern Guides**.
- For branching flows with parallel paths (Wait ALL / Wait ANY / OR), use the **Advanced Workflow** builder.
