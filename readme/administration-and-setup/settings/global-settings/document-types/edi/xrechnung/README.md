# XRechnung Overzicht

## Inleiding

XRechnung is een Duitse e-facturatiestandaard ontworpen voor het openbaar bestuur. Het is gebaseerd op de Europese standaard EN 16931 en bestaat in twee technische formaten: **UBL** (Universal Business Language) en **CII** (Cross Industry Invoice).

DocBits biedt volledige ondersteuning voor XRechnung, waardoor gestructureerde gegevens kunnen worden geëxtraheerd en naadloos kunnen worden geëxporteerd naar Infor ERP-systemen.

## Ondersteunde XRechnung-versies (CII)

DocBits ondersteunt de volgende XRechnung CII versies:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Gegevensstroom

De gegevensstroom van een XRechnung-document naar uw ERP-systeem volgt deze stappen:

1. **Extractie**: DocBits parseert de XML-gegevens op basis van de XRechnung-versie en -indeling (CII of UBL).
2. **DocBits Veldtoewijzing**: geëxtraheerde gegevens worden toegewezen aan standaard DocBits-velden.
3. **Afstemming op het ERP**: DocBits-velden worden toegewezen aan Infor BOD (Business Object Document)-velden, meestal met behulp van de `SyncSupplierInvoice` BOD.
4. **Exporteren**: de toegewezen gegevens worden geëxporteerd naar het Infor-systeem.

## Mapping-standaarden

De mapping is gebaseerd op de volgende standaarden:
* **UN/CEFACT CII**: De basis voor de XRechnung CII XML structuur.
* **OAGIS/OASIS**: De standaard voor Infor BOD's.
* **EN 16931**: De Europese standaard voor e-facturatie.

## Landengidsen

Raadpleeg de landengidsen voor exacte formaatlabels, syntaxis, versiebeperkingen en de onderzochte configuratiestatus. [eDocs-formaten, versies en landengidsen](../supported-electronic-documents/README.md).
