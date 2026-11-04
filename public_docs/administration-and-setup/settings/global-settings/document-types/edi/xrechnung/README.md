# XRechnung Überblick

## Einführung

XRechnung ist ein deutscher Standard für die elektronische Rechnungsstellung, der für die öffentliche Verwaltung entwickelt wurde. Er basiert auf der europäischen Norm EN 16931 und existiert in zwei technischen Formaten: **UBL** (Universal Business Language) und **CII** (Cross Industry Invoice).

DocBits bietet volle Unterstützung für XRechnung und ermöglicht die Extraktion strukturierter Daten sowie den nahtlosen Export in Infor ERP-Systeme.

## Unterstützte XRechnung-Versionen (CII)

DocBits unterstützt die folgenden XRechnung-CII-Versionen:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Datenfluss

Die Daten eines XRechnung-Dokuments gelangen über folgende Schritte in Ihr ERP-System:

1. **Extraktion**: DocBits liest die XML-Daten entsprechend der XRechnung-Version und dem Format (CII oder UBL).
2. **DocBits-Feldzuordnung**: Die extrahierten Daten werden den Standardfeldern von DocBits zugeordnet.
3. **ERP-Zuordnung**: Die DocBits-Felder werden den Feldern eines Infor-BODs (Business Object Document) zugeordnet. Üblicherweise wird dafür `SyncSupplierInvoice` verwendet.
4. **Export**: Die zugeordneten Daten werden in das Infor-System exportiert.

## Mapping-Standards

Die Zuordnung basiert auf folgenden Standards:
* **UN/CEFACT CII**: Grundlage der XML-Struktur von XRechnung CII.
* **OAGIS/OASIS**: Standard für Infor-BODs.
* **EN 16931**: Europäische Norm für elektronische Rechnungen.

## Länderanleitungen

Die Länderanleitungen enthalten genaue Formatbezeichnungen, Syntax, Versionsgrenzen und den geprüften Konfigurationsstand. [eDocs-Formate, Versionen und Länderanleitungen](../supported-electronic-documents/README.md).
