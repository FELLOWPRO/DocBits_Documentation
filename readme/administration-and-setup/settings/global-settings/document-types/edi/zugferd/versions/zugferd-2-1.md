# ZUGFeRD 2.1 (Factur-X 1.0) Feldzuordnung

## Überblick

ZUGFeRD 2.1 ist identisch mit dem französischen Standard Factur-X 1.0. Er ist vollständig EN 16931-konform und wird häufig für grenzüberschreitende Transaktionen zwischen Deutschland und Frankreich verwendet.

## Header Feldzuordnung

### Rechnungsidentifikation

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Rechnungsnummer |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Rechnungstyp-Code |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Ausstellungsdatum der Rechnung |

### Dokumenttyp & Untertyp (TRA-gesteuert)

Neben dem rohen `INVOICE_TYPE_CODE` erzeugt das Standard-TRANSFORMATION-XSLT zwei abgeleitete Felder:

| DocBits-Feld | Quelle | Logik |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` oder `261` → **Credit Note**; jeder andere Code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Nicht leer → **Purchase Invoice**; leer/fehlend → **Cost Invoice** |

### Tax Breakdown (stufenklassifiziert)

`ApplicableTradeTax`-Blöcke werden auf drei steuersatzbasierte Stufen verteilt (nicht über positionale Indexe): Felder zum Regelsatz (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) erfassen rate ≥ 19; Felder zum ermäßigten Satz (`*_2`) erfassen 0 < rate < 19; Felder zum Nullsatz (`*_3`) erfassen rate = 0. Siehe [ZUGFeRD Tax Breakdown](../README.md#tax-breakdown-tier-classified) für die vollständige Feldliste.

### Käufer-Informationen

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Kunden-ID |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Firmenname |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Adresszeile 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postleitzahl |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | Stadt |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Ländercode |

## Positionsmapping

| ZUGFeRD CII Pfad | DocBits Feld | Infor BOD Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Positionsnummer |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Artikelnummer des Verkäufers |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelbeschreibung |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Berechnete Menge |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Maßeinheit |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto-Einzelpreis |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Gesamtbetrag der Position |
