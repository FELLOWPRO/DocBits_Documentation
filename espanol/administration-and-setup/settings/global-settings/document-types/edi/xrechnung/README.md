# Resumen de XRechnung

## Introducción

XRechnung es un estándar alemán de facturación electrónica diseñado para la administración pública. Se basa en el estándar europeo EN 16931 y existe en dos formatos técnicos: **UBL** (Universal Business Language) y **CII** (Cross Industry Invoice).

DocBits ofrece soporte completo para XRechnung, lo que permite la extracción de datos estructurados y la exportación fluida a los sistemas ERP de Infor.

## Versiones de XRechnung compatibles (CII)

DocBits admite las siguientes versiones XRechnung CII:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Flujo de datos

El flujo de datos desde un documento XRechnung a su sistema ERP sigue estos pasos:

1. **Extracción**: DocBits analiza los datos de XML según la versión y el formato de XRechnung (CII o UBL).
2. **Asignación de campos de DocBits**: los datos extraídos se asignan a los campos estándar DocBits.
3. **Alineación con el ERP**: los campos DocBits se asignan a los campos Infor BOD (documento de objeto de negocio), normalmente utilizando `SyncSupplierInvoice` BOD.
4. **Export**: Los datos mapeados se exportan al sistema Infor.

## Estándares de mapeo

El mapeo se basa en los siguientes estándares:
* **UN/CEFACT CII**: La base para la estructura XRechnung CII XML.
* **OAGIS/OASIS**: El estándar para los BOD de Infor.
* **EN 16931**: El estándar europeo para facturación electrónica.

## Guías por país

Consulte las guías por país para conocer las etiquetas de formato exactas, la sintaxis, los límites de versión y el estado de configuración inspeccionado. [Formatos, versiones y guías por país de eDocs](../supported-electronic-documents/README.md).
