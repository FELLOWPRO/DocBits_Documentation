# Aperçu de XRechnung

## Introduction

XRechnung est une norme allemande de facturation électronique conçue pour l'administration publique. Elle est basée sur la norme européenne EN 16931 et existe en deux formats techniques : **UBL** (Universal Business Language) et **CII** (Cross Industry Invoice).

DocBits offre un support complet pour XRechnung, permettant l'extraction de données structurées et l'exportation transparente vers les systèmes ERP Infor.

## Versions XRechnung supportées (CII)

DocBits supports the following XRechnung CII versions:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Flux de données

The data flow from an XRechnung document to your ERP system follows these steps:

1. **Extraction**: DocBits parses the XML data based on the XRechnung version and format (CII or UBL).
2. **DocBits Field Mapping**: Extracted data is mapped to standard DocBits fields.
3. **ERP Alignment**: DocBits fields are mapped to Infor BOD (Business Object Document) fields, typically using the `SyncSupplierInvoice` BOD.
4. **Export**: The mapped data is exported to the Infor system.

## Standards de mappage

The mapping is based on the following standards:
* **UN/CEFACT CII**: The base for XRechnung CII XML structure.
* **OAGIS/OASIS**: The standard for Infor BODs.
* **EN 16931**: The European standard for e-invoicing.
