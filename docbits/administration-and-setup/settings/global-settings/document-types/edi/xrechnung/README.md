# XRechnung Overview

## Introduction

XRechnung is a German electronic invoicing standard designed for public administration. It is based on the European standard EN 16931 and exists in two technical formats: **UBL** (Universal Business Language) and **CII** (Cross Industry Invoice).

DocBits provides full support for XRechnung, allowing for the extraction of structured data and seamless export to Infor ERP systems.

## Supported XRechnung Versions (CII)

DocBits supports the following XRechnung CII versions:

* [XRechnung 1.2](xrechnung-1-2.md)
* [XRechnung 2.1](xrechnung-2-1.md)
* [XRechnung 3.0](xrechnung-3-0.md)
* [XRechnung 3.0.1](xrechnung-3-0-1.md)
* [XRechnung 3.0.2](xrechnung-3-0-2.md)

## Data Flow

The data flow from an XRechnung document to your ERP system follows these steps:

1. **Extraction**: DocBits parses the XML data based on the XRechnung version and format (CII or UBL).
2. **DocBits Field Mapping**: Extracted data is mapped to standard DocBits fields.
3. **ERP Alignment**: DocBits fields are mapped to Infor BOD (Business Object Document) fields, typically using the `SyncSupplierInvoice` BOD.
4. **Export**: The mapped data is exported to the Infor system.

## Mapping Standards

The mapping is based on the following standards:

* **UN/CEFACT CII**: The base for XRechnung CII XML structure.
* **OAGIS/OASIS**: The standard for Infor BODs.
* **EN 16931**: The European standard for e-invoicing.
