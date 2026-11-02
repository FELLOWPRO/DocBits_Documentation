# Przegląd XRechnung

## Wprowadzenie

XRechnung to niemiecki standard fakturowania elektronicznego opracowany dla administracji publicznej. Opiera się on na europejskiej normie EN 16931 i występuje w dwóch formatach technicznych: **UBL** (Universal Business Language) i **CII** (Cross Industry Invoice).

DocBits zapewnia pełne wsparcie dla XRechnung, umożliwiając ekstrakcję ustrukturyzowanych danych i płynny eksport do systemów ERP Infor.

## Obsługiwane wersje XRechnung (CII)

DocBits obsługuje następujące wersje XRechnung CII:

* [XRechnung 1.2](versions/xrechnung-1-2.md)
* [XRechnung 2.1](versions/xrechnung-2-1.md)
* [XRechnung 3.0](versions/xrechnung-3-0.md)
* [XRechnung 3.0.1](versions/xrechnung-3-0-1.md)
* [XRechnung 3.0.2](versions/xrechnung-3-0-2.md)

## Przepływ danych

Przepływ danych z dokumentu XRechnung do systemu ERP przebiega według następujących kroków:

1. **Wyodrębnianie**: DocBits analizuje dane XML w oparciu o wersję i format XRechnung (CII lub UBL).
2. **DocBits Mapowanie pól**: Wyodrębnione dane są mapowane na standardowe pola DocBits.
3. **Mapowanie do ERP**: Pola DocBits są mapowane na pola Infor BOD (Dokument obiektu biznesowego), zazwyczaj przy użyciu `SyncSupplierInvoice` BOD.
4. **Export**: Zmapowane dane są eksportowane do systemu Infor.

## Standardy mapowania

Mapowanie odbywa się w oparciu o następujące standardy:
* **UN/CEFACT CII**: Podstawa konstrukcji XRechnung CII XML.
* **OAGIS/OASIS**: Standard dla Infor BZT.
* **EN 16931**: Europejski standard e-fakturowania.

## Przewodniki krajowe

Przewodniki krajowe zawierają dokładne oznaczenia formatów, składnię, ograniczenia wersji i sprawdzony stan konfiguracji. [Formaty eDocs, wersje i przewodniki krajowe](../supported-electronic-documents/README.md).
