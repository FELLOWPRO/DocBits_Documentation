# Visão geral do XRechnung

## Introdução

XRechnung é um padrão alemão de faturação eletrónica concebido para a administração pública. Baseia-se na norma europeia EN 16931 e existe em dois formatos técnicos: **UBL** (Universal Business Language) e **CII** (Cross Industry Invoice).

O DocBits oferece suporte total para XRechnung, permitindo a extração de dados estruturados e a exportação perfeita para sistemas Infor ERP.

## Versões do XRechnung suportadas (CII)

DocBits supports the following XRechnung CII versions:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Fluxo de dados

The data flow from an XRechnung document to your ERP system follows these steps:

1. **Extraction**: DocBits parses the XML data based on the XRechnung version and format (CII or UBL).
2. **DocBits Field Mapping**: Extracted data is mapped to standard DocBits fields.
3. **ERP Alignment**: DocBits fields are mapped to Infor BOD (Business Object Document) fields, typically using the `SyncSupplierInvoice` BOD.
4. **Export**: The mapped data is exported to the Infor system.

## Padrões de mapeamento

The mapping is based on the following standards:
* **UN/CEFACT CII**: The base for XRechnung CII XML structure.
* **OAGIS/OASIS**: The standard for Infor BODs.
* **EN 16931**: The European standard for e-invoicing.
