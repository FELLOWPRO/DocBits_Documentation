# eSLOG 1.6 and 2.0

**eSLOG 1.6** and **eSLOG 2.0** appear as separate electronic invoice formats in DocBits. Choose the version used by your incoming Slovenian invoice. The screenshots below show the English interface in a documentation test organization. Existing row names, versions and timestamps are masked; the images do not prove that an invoice of either version has been processed successfully.

## Find the configurations

1. Go to **Settings → Document Types → Invoice → E-Doc**.
2. Expand **E-SLOG 1.6** or **E-SLOG 2.0**. Each format has its own three entries.

<figure><img src="../../../../../.gitbook/assets/dbdc-106-eslog-16-native-en-20261101.png" alt="English E-Doc list for E-SLOG 1.6 with three configuration rows; existing names, versions and timestamps are masked"><figcaption>E-SLOG 1.6: from top to bottom, Transformation, Preview and Extraction Paths. This test view contains two Default rows and one existing Custom row. Names, versions and timestamps are masked.</figcaption></figure>

<figure><img src="../../../../../.gitbook/assets/dbdc-106-eslog-20-native-en-20261101.png" alt="English E-Doc list for E-SLOG 2.0 with three configuration rows; existing names, versions and timestamps are masked"><figcaption>E-SLOG 2.0: separate entries for the same three steps, all shown as Default here. Names, versions and timestamps are masked.</figcaption></figure>

| Entry | What it controls | Next guide |
| --- | --- | --- |
| **TRANSFORMATION (XSLT)** | Converts the format's source data into structured XML. | [Transformation](edi/edi-transformation-file-guide.md) |
| **PREVIEW (XSLT)** | Defines the readable document view. | [Preview](edi/edi-preview-file-guide.md) |
| **EXTRACTION PATHS (JSON)** | Maps XML values to DocBits fields and table columns. | [Extraction Paths](edi/edi-extraction-paths-file-guide.md) |

Click a row to see its versions and configuration. **Default** identifies the supplied entry. **Last Modified At** shows when that entry was last changed. Where available in your view, the **New** button starts an additional configuration entry. The three-dot menu on a default row offers **Customize**, which creates an organization-specific copy, and **Delete**; review the selected row carefully before using Delete.

Inside a configuration, the pencil beside an active version creates a draft. Check a draft with the **Preview** test panel and a representative uploaded document ID before activating it with the checkmark. A draft's trash icon removes that draft. The actual field names and XML paths depend on your eSLOG file; use the corresponding guide above for the editor details.
