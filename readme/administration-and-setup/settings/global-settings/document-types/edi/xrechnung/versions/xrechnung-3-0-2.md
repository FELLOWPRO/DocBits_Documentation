# XRechnung 3.0.2 CII – Feldzuordnung

## Überblick

Dieses Dokument beschreibt den vollständigen Ablauf der Feldzuordnung für XRechnung 3.0.2 im CII-Format (Cross-Industry Invoice).

## 1. CII-XML-Struktur

XRechnung CII verwendet das Cross-Industry-Invoice-Format von UN/CEFACT mit folgenden Namensräumen:

| Präfix | Namensraum | Zweck |
| :--- | :--- | :--- |
| `rsm` | `urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100` | Wurzelelement |
| `ram` | `urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100` | Geschäftsobjekte |
| `qdt` | `urn:un:unece:uncefact:data:standard:QualifiedDataType:100` | Qualifizierte Datentypen |
| `udt` | `urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100` | Unqualifizierte Datentypen |

**Klassifizierungs-URN**: `urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0.2`

## 2. CII-XML → Feldextraktion in DocBits

### Kopffelder

| CII-XML-Pfad | DocBits-Feld | Datentyp |
| :--- | :--- | :--- |
| `ExchangedDocument/ID` | `invoice_id` | Zeichenfolge |
| `ExchangedDocument/TypeCode` | `invoice_type` | Zeichenfolge |
| `ExchangedDocument/IssueDateTime/DateTimeString` | `invoice_date` | Datum (YYYYMMDD) |
| `ApplicableHeaderTradeAgreement/BuyerReference` | `buyer_reference` | Zeichenfolge |
| `BuyerOrderReferencedDocument/IssuerAssignedID` | `purchase_order` | Zeichenfolge |
| `ActualDeliverySupplyChainEvent/.../DateTimeString` | `ship_date` | Datum |
| `SpecifiedTradePaymentTerms/DueDateDateTime/DateTimeString` | `due_date` | Datum |
| `ApplicableHeaderTradeSettlement/InvoiceCurrencyCode` | `currency` | Zeichenfolge |

### Dokumenttyp-Klassifizierung

Das TRANSFORMATION-XSLT ersetzt den numerischen `TypeCode`-Wert durch eine sprechende Bezeichnung, bevor er in `invoice_type` übernommen wird:

| UNCL-1001-Code | Bedeutung | DocBits `invoice_type` |
| :--- | :--- | :--- |
| `381` / `261` | Gutschrift / Selbst ausgestellte Gutschrift | **Credit Note** |
| Jeder andere Code (`380`, `383`, `384`, `386`, `389`, `325`, …) | Rechnung / Lastschrift / Proforma / etc. | **Invoice** |

### Lieferantenfelder

| CII-XML-Pfad | DocBits-Feld |
| :--- | :--- |
| `SellerTradeParty/ID` | `supplier_id` |
| `SellerTradeParty/Name` | `supplier_name` |
| `SellerTradeParty/PostalTradeAddress/LineOne` | `supplier_address` |
| `SellerTradeParty/PostalTradeAddress/CityName` | `supplier_city` |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `supplier_postal_code` |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `supplier_country` |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `supplier_vat` |
| `PayeePartyCreditorFinancialAccount/IBANID` | `iban` |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `bic` |

### Kundenfelder

| CII-XML-Pfad | DocBits-Feld |
| :--- | :--- |
| `BuyerTradeParty/ID` | `customer_id` |
| `BuyerTradeParty/Name` | `customer_name` |
| `BuyerTradeParty/PostalTradeAddress/LineOne` | `customer_address` |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `customer_vat` |

### Betragsfelder

| CII-XML-Pfad | DocBits-Feld |
| :--- | :--- |
| `SpecifiedTradeSettlementHeaderMonetarySummation/TaxBasisTotalAmount` | `net_amount` |
| `SpecifiedTradeSettlementHeaderMonetarySummation/TaxTotalAmount` | `tax_amount` |
| `SpecifiedTradeSettlementHeaderMonetarySummation/GrandTotalAmount` | `total_amount` |
| `ApplicableTradeTax/RateApplicablePercent` | `tax_rate` |
| `ApplicableTradeTax/BasisAmount` | `taxable_amount` |

### Positionsfelder

| CII-XML-Pfad | DocBits-Tabellenspalte |
| :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_NUMBER` |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` |
| `SpecifiedTradeProduct/SellerAssignedID` | `SELLER_ITEM_ID` |
| `SpecifiedTradeProduct/BuyerAssignedID` | `BUYER_ITEM_ID` |
| `SpecifiedLineTradeDelivery/BilledQuantity` | `QUANTITY` |
| `BilledQuantity/@unitCode` | `UNIT` |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` |
| `SpecifiedTradeSettlementLineMonetarySummation/LineTotalAmount` | `TOTAL_AMOUNT` |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT_RATE` |
| `ApplicableTradeTax/CategoryCode` | `VAT_CATEGORY` |

## 3. DocBits → Infor-BOD-Export (SyncSupplierInvoice)

### Zuordnung der Kopffelder

| DocBits-Feld | BOD-XML-Pfad |
| :--- | :--- |
| `INVOICE_NUMBER` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/DocumentID/ID` |
| `INVOICE_DATE` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/DocumentDateTime` |
| `VENDOR_ID` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/SupplierParty/PartyIDs/ID` |
| `VENDOR_NAME` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/SupplierParty/Name` |
| `TOTAL_AMOUNT` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/TotalAmount` |
| `NET_AMOUNT` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/ExtendedBaseAmount` |
| `TAX_AMOUNT` | (Berechnet als ExtendedAmount - ExtendedBaseAmount) |
| `CURRENCY` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/CurrencyExchangeRate/SourceCurrencyCode` |
| `PAYMENT_TERMS` | `DataArea/SupplierInvoice/SupplierInvoiceHeader/PaymentTerm/Term/Description` |
| `PURCHASE_ORDER` | `UserArea/Property/NameValue[@name='PONumber']` |

### Zuordnung der Positionsfelder

| DocBits-Spalte | BOD-XML-Pfad |
| :--- | :--- |
| `POSITION` | `SupplierInvoiceDetail/LineNumber` |
| `ITEM_NUMBER` | `SupplierInvoiceDetail/Item/ItemID/ID` |
| `DESCRIPTION` | `SupplierInvoiceDetail/Item/Description` |
| `QUANTITY` | `SupplierInvoiceDetail/InvoicedQuantity` |
| `UNIT` | `SupplierInvoiceDetail/InvoicedQuantity/@unitCode` |
| `UNIT_PRICE` | `SupplierInvoiceDetail/UnitPrice/Amount` |
| `TOTAL_AMOUNT` | `SupplierInvoiceDetail/ExtendedAmount` |
