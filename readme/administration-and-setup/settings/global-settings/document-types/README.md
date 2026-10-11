# Document Types

{% embed url="https://youtu.be/pFz_6tvNlU4" %}
DocBits Document Types Explained: Create, Configure & Assign Processing Settings
{% endembed %}

<figure><img src="../../../../.gitbook/assets/docbits_document_types_overview_screenshot.png" alt="Docbits Document Types Overview Screenshot"><figcaption><p>Document Types Screenshot </p></figcaption></figure>

#### Overview

The Document Types section lists all document types recognized and processed by Docbits. Administrators can manage various aspects such as layout, field definitions, extraction rules, and more for each type of document. This customization is key to ensuring accurate data handling and compliance with organizational standards.

#### Key Features and Options

1. **Document Type List**:
   * Each row represents a document type such as Invoice, Credit Note, Delivery Note, etc.
   * Document types can be standard or custom, as indicated by labels like "Standard."
2. **Edit layout**: This option allows administrators to modify the document layout settings, which include defining how the document appears and where data fields are located.
3. **Document Sub Types**: If any document types have subcategories, this option lets admins configure settings specific to each subtype.
4. **Table columns**: Customize which data columns should appear when the document type is viewed in lists or reports.
5. **Fields**: Manage the data fields associated with the document type, including adding new fields or modifying existing ones.
6. **Model Training**: Configure and train the model used for recognizing and extracting data from the documents. This may involve setting parameters for machine learning models that improve over time with more data.
7. **Regex**: Set up regular expressions that are used to extract data from documents based on patterns. This is particularly useful for structured data extraction.
8. **Scripts**: Write or modify scripts that run custom processing rules or workflows for documents of this type.
9. **E-DOC**: Configure settings related to the exchange of documents in standardized electronic formats. You can configure XRechnung, EDI, FakturaPA or EDI

#### Regole di convalida personalizzate

Apri un tipo di documento, attiva la funzione **Regole di convalida personalizzate**, poi scegli **Gestisci le regole di convalida** per amministrare le regole di convalida proprie di questo tipo (la funzione deve essere attiva sul tipo di documento). Per riprendere una regola esistente senza ricrearla, segui la guida [Duplicare una regola di convalida personalizzata](duplicate-a-custom-validation-rule.md). Spiega il nome della regola, la chiave delle regole e i pulsanti di conferma.

{% hint style="info" %}
See [Setup Document Type](../../../setup/document-types/)
{% endhint %}
