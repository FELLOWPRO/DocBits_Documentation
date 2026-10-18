# e-docs

{% embed url="https://youtu.be/AxrHNEmmXtg" %}
DocBits E-Invoice Tutorial: Process XRechnung / ZUGFeRD (Factur-X), Validate Data & Automate Workflows
{% endembed %}

<figure><img src="../../../../../.gitbook/assets/docbits_edi_overview.png" alt="Docbits Edi Overview"><figcaption></figcaption></figure>

#### Overview

In Docbits, the EDI settings provide tools for defining and managing the structure and format of EDI messages that correspond to various document types, such as invoices or purchase orders. The settings enable the customization of EDI messages to comply with the standards and requirements specific to different trading partners and industries.

#### Key Features and Options

1. **EDI Configuration Elements**:
   * **Structure Descriptor**: Defines the basic structure of the EDI document, including segment ordering, mandatory fields, and qualifiers necessary for the EDI document to be valid.
   * **Transformation**: Specifies the transformations applied to convert the document data into an EDI formatted message. This typically involves specifying mappings from document fields to EDI segments and elements.
   * **Preview**: Allows administrators to view how the EDI message will look after transformation, helping to ensure accuracy before transmission.
   * **Extraction Paths**: Shows the paths used to extract values from the document, which are then used to populate the EDI message.
2. **XSLT Editor**:
   * Used for editing and validating the XSLT (eXtensible Stylesheet Language Transformations) used in the transformation process. XSLT is a powerful language designed for transforming XML documents into other XML documents or other formats like HTML, text, or even other XML structures.

<figure><img src="../../../../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 09.49.59.png" alt=""><figcaption></figcaption></figure>

## Reglas utilizadas y activación

Si una nota de crédito electrónica aparece como Invoice, siga la [guía de resolución de problemas de clasificación](credit-note-recognized-as-invoice.md). Explica el origen personalizado o predeterminado que se está utilizando, los códigos de tipo, Extraction Paths y la activación segura.

## Guías por país

Consulte las guías por país para conocer las etiquetas de formato exactas, la sintaxis, los límites de versión y el estado de configuración inspeccionado. [Formatos, versiones y guías por país de eDocs](supported-electronic-documents/README.md).
