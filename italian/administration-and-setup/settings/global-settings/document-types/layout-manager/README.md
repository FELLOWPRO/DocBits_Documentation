# Layout Manager

<figure><img src="../../../../../.gitbook/assets/docbits_layout_manager_overview.png" alt="Docbits Layout Manager Overview"><figcaption></figcaption></figure>

#### Overview

The Layout Manager allows administrators to visually configure and modify the layout of document types by setting properties for various data fields and groups within a document. This interface helps ensure that the extraction models and manual data entry points align precisely with the document's structure as scanned or uploaded into Docbits.

#### Key Components

1. **Groups and Fields**:
   * **Groups**: Organizational units within a document type that categorize related fields (e.g., Invoice Details, Payment Details). These can be expanded or collapsed and arranged to mirror the logical grouping in the actual document.
   * **Fields**: Individual data points within each group (e.g., Invoice Number, Payment Terms). Each field can be customized for how data is captured, displayed, and processed.
2. **Properties Panel**:
   * This panel displays the properties of the selected field or group, allowing for detailed configuration, such as:
     * **Label**: The visible label for the field in the user interface.
     * **Field Name**: The technical identifier used within the system.
     * **Element Width in Percentage**: Determines the width of the field in relation to the document layout.
     * **Tab Index**: Controls the tabbing order for navigation.
     * **Run Script on Change**: Whether to execute a script when the field value changes.
     * **Display Label On Left**: Whether the label is displayed to the left of the field or above it.
     * **Is Textarea**: Specifies if the field should be a textarea, accommodating larger amounts of text.
     * **Select Model Type**: Option to select which model type will handle the extraction of this field.
     * **Field Length**: Maximum length of data to be accepted in this field.
     * **Banned Keywords**: Keywords that are not allowed within the field.
3. **Template Preview**:
   * Shows a real-time preview of how the document will appear based on the current layout configuration. This helps in ensuring that the layout matches the actual document structure and is vital for testing and refining the document processing setup.

{% @jira/embed url="https://fellowpro.atlassian.net/browse/DOCB-2490" %}


