# Table extraction for costing element

Costing elements are charges or other amounts represented as invoice table lines. If this feature is enabled and the document has extracted lines, DocBits can classify those lines against the costing elements configured for the organization. A reviewer can correct a line's classification in the document table.

## Enable the setting

1. Open **Settings → Document Types** and select **Classification and Extraction** below the **Document Types** entry.
2. Stay on **General** and expand **Extraction**.
3. Find **Table extraction for costing element** below the fields requested for table extraction. An administrator can turn on this switch for the organization.

<figure><img src="../../../../.gitbook/assets/costing-table-extraction-setting-en.png" alt="The Extraction section of the Classification and Extraction settings with the switches Table Extraction, AI Table extraction, Use Table Extraction Vision, Use Structured Extraction, Table extraction for costing element, Auto extract tax code, Save extraction rules, Extract hidden fields and the AI model selector"><figcaption><p>The <strong>Table extraction for costing element</strong> switch sits between <strong>Use Structured Extraction (AI)</strong> and <strong>Auto extract tax code</strong>. It is off in the organization used for this guide.</p></figcaption></figure>

{% hint style="info" %}
The switch alone does not create costing elements or invoice rows. Configure the elements and import any required data first. The linked [costing-element setup guide](../../../../infor-integration-and-configuration/importing-customer-master-data/m3/table-extraction-for-costing-element.md) explains the M3 example. Check [Classification and Extraction](README.md) for the other extraction controls.
{% endhint %}

## Review or correct a line

Open a document whose invoice table contains extracted lines and inspect the costing-element icon beside the relevant line. Select the icon to open the available classifications. Choose the correct configured costing element, or choose **Uncategorize** if the line is an ordinary item. Then review the resulting line and totals before saving the document.

If the icon or a classification is missing, first confirm that the document has extracted lines, the feature is enabled, and a costing element is configured for the organization. The document used for this documentation check had no extracted invoice lines, so the classification menu could not be pictured or exercised. The steps above reflect the current document control; no classification was saved during this check.
