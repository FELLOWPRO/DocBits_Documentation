# Fields

<figure><img src="../../../../../.gitbook/assets/s150-docbits_fields_overview-fr.png" alt="Vue des champs du type de document Facture."><figcaption><p>Vue des champs du type de document Facture.</p></figcaption></figure>

## Overview

The Fields setting provides a user interface where administrators can manage the properties and behavior of individual data fields associated with a document type. Each field can be adjusted to optimize the accuracy and efficiency of data capture and validation.

{% hint style="info" %}
[Fields with Charges](new-fields-with-charges.md)
{% endhint %}

## Key Features and Options

1. **Fields Configuration**:
   * **Field Names**: Lists the names of the fields, typically corresponding to the data elements within the document, like "Invoice Number" or "Purchase Order Date".
   * **Obligatoire**: Administrators can mark fields as required, making sure that data must be entered or captured for these fields to complete the document processing.
   * **Lecture seule**: Fields can be set to read-only to prevent modification after data capture or during certain stages of document processing.
   * **Caché**: Fields can be hidden from view in the user interface, useful for sensitive information or for simplifying user workflows.
2. **Paramètres avancés**:
   * **Force Validation**: Ensures that data entered into a field passes certain validation rules before being accepted.
   * **OCR (Optical Character Recognition)**: This toggle can be switched on to enable OCR processing for a specific field, useful for automated data extraction from scanned or digital documents.
   * **Match Score**: Administrators can define a match score, a threshold used to determine the confidence level of data recognition or matching, impacting how data validation and quality checks are performed.
3. **Action Buttons**:
   * **Create New Field**: Allows adding new fields to the document type.
   * **Edit Icons**: Each field has an edit icon that allows administrators to further configure field-specific settings, such as data type, default values, or connected business logic.
   * **Enregistrer les paramètres**: Commits the changes made to the field configuration
