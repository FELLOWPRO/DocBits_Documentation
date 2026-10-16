# XRechnung Überblick

## Einführung

XRechnung ist ein deutscher Standard für die elektronische Rechnungsstellung, der für die öffentliche Verwaltung entwickelt wurde. Er basiert auf der europäischen Norm EN 16931 und existiert in zwei technischen Formaten: **UBL** (Universal Business Language) und **CII** (Cross Industry Invoice).

DocBits bietet volle Unterstützung für XRechnung und ermöglicht die Extraktion strukturierter Daten sowie den nahtlosen Export in Infor ERP-Systeme.

## Unterstützte XRechnung-Versionen (CII)

DocBits supports the following XRechnung CII versions:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Datenfluss

The data flow from an XRechnung document to your ERP system follows these steps:

1. **Extraction**: DocBits parses the XML data based on the XRechnung version and format (CII or UBL).
2. **DocBits Field Mapping**: Extracted data is mapped to standard DocBits fields.
3. **ERP Alignment**: DocBits fields are mapped to Infor BOD (Business Object Document) fields, typically using the `SyncSupplierInvoice` BOD.
4. **Export**: The mapped data is exported to the Infor system.

## Mapping-Standards

The mapping is based on the following standards:
* **UN/CEFACT CII**: The base for XRechnung CII XML structure.
* **OAGIS/OASIS**: The standard for Infor BODs.
* **EN 16931**: The European standard for e-invoicing.
