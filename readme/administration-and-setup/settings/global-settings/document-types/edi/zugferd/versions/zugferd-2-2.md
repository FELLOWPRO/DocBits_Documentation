# ZUGFeRD 2.2 Feldzuordnung

## Überblick

ZUGFeRD 2.2 setzt die Ausrichtung auf EN 16931 fort und übernimmt weitere Aktualisierungen aus dem CII-Standard.

## Header Feldzuordnung

### Rechnungsidentifikation

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Rechnungsnummer |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Ausstellungsdatum der Rechnung |

### Dokumenttyp & Untertyp (TRA-gesteuert)

Das Standard-TRANSFORMATION-XSLT erzeugt zwei abgeleitete Felder:

| DocBits-Feld | Quelle | Logik |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` oder `261` → **Credit Note**; jeder andere Code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Nicht leer → **Purchase Invoice**; leer/fehlend → **Cost Invoice** |

### Tax Breakdown (stufenklassifiziert)

`ApplicableTradeTax`-Blöcke werden auf drei steuersatzbasierte Stufen verteilt (nicht über positionale Indexe): Felder zum Regelsatz (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) erfassen rate ≥ 19; Felder zum ermäßigten Satz (`*_2`) erfassen 0 < rate < 19; Felder zum Nullsatz (`*_3`) erfassen rate = 0. Siehe [ZUGFeRD Tax Breakdown](../README.md#tax-breakdown-tier-classified) für die vollständige Feldliste.

### Währung & Beträge

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Rechnungswährung |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Gesamt-Nettobetrag |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Gesamt-Steuerbetrag |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Bruttobetrag |

## Positionsmapping

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Positionsnummer |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelbeschreibung |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Berechnete Menge |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto-Einzelpreis |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Gesamtbetrag der Position |
