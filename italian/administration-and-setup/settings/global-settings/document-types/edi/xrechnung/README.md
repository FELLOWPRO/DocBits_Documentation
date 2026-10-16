# Panoramica di XRechnung

## Introduzione

XRechnung è uno standard tedesco per la fatturazione elettronica progettato per la pubblica amministrazione. Si basa sullo standard europeo EN 16931 ed esiste in due formati tecnici: **UBL** (Universal Business Language) e **CII** (Cross Industry Invoice).

DocBits fornisce il pieno supporto per XRechnung, consentendo l'estrazione di dati strutturati e l'esportazione senza soluzione di continuità verso i sistemi ERP Infor.

## Versioni XRechnung supportate (CII)

DocBits supports the following XRechnung CII versions:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Flusso di dati

The data flow from an XRechnung document to your ERP system follows these steps:

1. **Extraction**: DocBits parses the XML data based on the XRechnung version and format (CII or UBL).
2. **DocBits Field Mapping**: Extracted data is mapped to standard DocBits fields.
3. **ERP Alignment**: DocBits fields are mapped to Infor BOD (Business Object Document) fields, typically using the `SyncSupplierInvoice` BOD.
4. **Export**: The mapped data is exported to the Infor system.

## Standard di mappatura

The mapping is based on the following standards:
* **UN/CEFACT CII**: The base for XRechnung CII XML structure.
* **OAGIS/OASIS**: The standard for Infor BODs.
* **EN 16931**: The European standard for e-invoicing.
