# Templates

A template describes **what** is checked: which page opens, what is clicked or filled in, and what must be
visible or true at the end. It contains no data of your organisation. Values that differ per organisation or per
run, such as a document ID, are declared as **parameters** and filled in by an [input](inputs.md).

Open **Settings → Testing**, tab **Templates**.

<figure><img src="../../../../.gitbook/assets/testing-04-templates-list.png" alt="Templates tab: groups, columns and row actions"><figcaption><p>Templates tab: groups, columns and row actions.</p></figcaption></figure>

## Read the list

Templates are grouped by category (for example **Smoke checks**, **Validation**, **Documents**, **Export**).
Select a group name to fold it; a red chip on the group counts templates whose last run failed.
**Search templates** filters by name.

| Column | Meaning |
|---|---|
| **Name** | The template name and, below it, its ID. |
| **Executor** | **Runner**: runs in your browser tab from this page. **Playwright**: a check run by your test automation; it can be documented here but not started from this page. |
| **Parameters** | The values an input must supply. *none* means the template runs as it is. |
| **Version** | Saved versions never change. A change is saved as a new version. |
| **Kind** | **built-in** (lock icon): part of the default set, the same for every organisation, read-only. **custom**: your organisation's own template. **writes**: the template changes data (for example uploads a document) and needs a confirmation before it starts. |

Row actions:

| Action | What it does |
|---|---|
| Download icon (**Export as JSON**) | Downloads the template definition as a JSON file, for example to keep it or to import it into another organisation. |
| **Edit a copy** (built-in) / **Edit** (custom) | Opens the template editor with a copy you can change and save as your own template. |
| **Create input** | Opens the [Inputs](inputs.md) tab with a new input for this template. Tests are started there, not here. |
| Bin icon (**Delete template**) | Only on your own templates. See *Delete your own template* below. |

<figure><img src="../../../../.gitbook/assets/testing-05-own-templates.png" alt="A default row and an own template row with their actions"><figcaption><p>A default row and an own template row with their actions.</p></figcaption></figure>

## Create your own template

You need your own template when no default checks what you need, or when you want a changed copy of a default.

**Start from a default:** select **Edit a copy** on its row. **Start empty:** select **New template**.

In the template editor:

1. Enter a **Template name** and, optionally, what the template is for.
2. Select **+ Add step** and choose a block, for example **Open page**, **Click**, **Fill in**, **Select**,
   **Wait for**, **Check text**, **Check field** or **Check status**. **Ready-made blocks** add a common sequence in one go, for example
   **Upload a document** or **Upload document and wait until processed**. See [Steps and Ready-made Blocks](steps-and-blocks.md)
   for the step groups, the **Advanced** settings and cleanup steps.
3. For every value that differs per organisation or per run, use the parameter button next to the value. The value
   becomes a parameter under **Inputs · change for each run**, with a type (**Text**, **Number**, **Yes/No**,
   **Server test file**), a default value and **Required** if it must be filled in.
4. Select **Save**. To try the draft once without saving, select **Run once**.

To choose the element of a step by pointing at it in the application, use **Pick in app**
([Pick an Element in the App](pick-in-app.md)).

Steps that change data (for example uploading a document) are marked **writes data**. A template with such steps
asks for a confirmation every time it starts.

<figure><img src="../../../../.gitbook/assets/testing-07-composer.png" alt="Template editor with two steps and one parameter"><figcaption><p>Template editor with two steps and one parameter.</p></figcaption></figure>

If someone saved the same version of this template in the meantime (for example in another tab), DocBits keeps your
draft and offers **Save as the next free version** or **Reload the latest version**.

## Create an extraction regression

Use this when you know what a set of documents must extract. You upload test files, enter the values they
must produce, and the assistant builds a template that reads those values from a document again. Run it after
a release or a configuration change to see whether the extraction still returns the same values.

Select **New extraction regression** next to **New template** on the Templates tab.

<figure><img src="../../../../.gitbook/assets/testing-35-regression-entry.png" alt="Templates tab: Import JSON, New template and New extraction regression"><figcaption><p>Templates tab: Import JSON, New template and New extraction regression.</p></figcaption></figure>

The dialog has three steps.

1. **Files and fields**: select the test files of your organisation, up to 50. **Upload test files** adds
   further files. Then choose the **Document type** and tick the **Fields to check**, up to 20 per template;
   you can also type the technical name of a field.
2. **Expected values**: one row per file and one column per field. Enter the value each file must extract,
   exactly as the validation screen shows it, or select **Take over values** and choose a document of your
   organisation that has already been validated: its current values fill the row. An empty cell only checks
   that the field is not empty. Numbers and dates are compared independent of how they are written
   (*1.234,50* = *1234.50*, *31.01.2026* = *2026-01-31*) as long as only one reading is possible.
3. **Name and save**: enter a **name** and select **Save**. If the files and fields do not fit into one
   template, the assistant splits them over several templates, for example *Quarterly check (1/4)*, and
   saves all of them in one step.

<figure><img src="../../../../.gitbook/assets/testing-36-regression-wizard.png" alt="The wizard New extraction regression, step Files and fields: test files, document type INVOICE, the field list and the two selected fields"><figcaption><p>The wizard <strong>New extraction regression</strong>, step <strong>Files and fields</strong>: test files, document type and the fields to check.</p></figcaption></figure>

The templates run like any other template. Each file is uploaded, DocBits waits until the document is
processed and then compares every selected field. A file that fails a check is reported as a deviation and
does not stop the other files. The result of such a run is described under
[Logs and History](logs.md).

{% hint style="warning" %}
While a template runs, its test files are uploaded as new documents in the environment you start it in, and
each document goes through the whole workflow there: extraction, validation rules, workflows and, depending
on the configuration, exports to connected systems, notifications and quota. Afterwards the documents are
deleted again. The document of a file with a deviation stays, so that you can open it from the
**Deviations** table. Run regressions in a test environment or on a test organisation.
{% endhint %}

## Import a template from JSON

1. Select **Import JSON**.
2. Select **Upload JSON file**, or paste the definition into **Paste the test definition (JSON)**.
3. Select **Validate**. DocBits checks the definition in the browser and on the server and lists any problems.
4. Select **Save as template** to add it to your templates, or **Run once** to try it without saving.

<figure><img src="../../../../.gitbook/assets/testing-06-import-dialog.png" alt="Import a test dialog with a validated definition"><figcaption><p>Import a test dialog with a validated definition.</p></figcaption></figure>

The format is described in [For Developers](for-developers.md).

## Delete your own template

1. On the row of your own template, select the bin icon (**Delete template**).
2. Read the confirmation **Delete template?** and select **Delete**.

The template and **all its versions** are removed. Saved inputs and past logs stay, so the history remains readable.
Inputs that pointed to the template stay in the list; edit or delete them. You can later save a template with the
same ID again. Built-in and default templates cannot be deleted.

<figure><img src="../../../../.gitbook/assets/testing-08-delete-dialog.png" alt="Delete template confirmation"><figcaption><p>Delete template confirmation.</p></figcaption></figure>
