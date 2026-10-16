# Change Proposals and Reports

A recommendation can come with a **change proposal**, a single setting change that should help. Administrators work with it in four steps:

1. **Preview**: shows the change (current → proposed value) and what DocBits expects. Nothing is saved. **Apply** is only possible after you looked at a preview.
2. **Apply**: saves exactly the previewed change. It is logged.
3. **Measure**: DocBits compares the touchless rate of the same document type **before and after**, over equally long periods. At least **20 documents** are needed in each period, otherwise it says _not measurable_.
4. **Undo**: takes the change back.

{% hint style="warning" %}
A before/after difference is an **observation**, not proof of cause. Other things can change at the same time (a new supplier, a seasonal peak).
{% endhint %}

**Example.** You apply _Switch on automatic PO match and export_ for invoices. Two weeks later the **Change history** says: pure rate before 52 % (210 documents), after 61 % (198 documents). That is +9 pp, enough documents to be measurable.

Administrators also see two sections between the key figures and the charts:

* **Improvement requests**: suggestions that users sent from the validation assistant, in two tabs **Open** and **History**.
* **Learned rule proposals**: rules DocBits learned from your team's corrections, for example "for supplier X, replace the value in field Y". Before you create one, check the documents where it would replace a value your team had accepted. The section **After activation** shows the manual corrections of the target field before and after a rule went live.

<figure><img src="../../../.gitbook/assets/touchless-consulting-report.png" alt="The Consulting report with the top three proposals, a ranking table and the problems by domain"><figcaption><p>The Consulting report: top proposals, a ranking of all blockers with documents and estimated impact per month, and the problems by domain. Example organisation with demo data; supplier names are fictional.</p></figcaption></figure>

Administrators find the **Consulting report** at the bottom of the tab. Click **Create report** to load it. It combines, for your organisation:

* the **changes with the biggest effect**, ranked, each with the domain, the problem, the recommended action, the number of documents and the **estimated** effect per month,
* **the domain of every problem** (extraction, master data, PO matching, auto accounting, settings, process),
* **table configuration checks**, for example _structured table output not used_ or _table column type mismatch_ per document type and column.

The effect values are **estimates**. If the report answers _forbidden_, your role does not allow it.

## Related pages

* [Touchless Intelligence](./)
* [Supplier Diagnosis and Issue Clusters](touchless-supplier-diagnosis.md)
* [PO Matching Diagnosis](touchless-po-matching-diagnosis.md)
