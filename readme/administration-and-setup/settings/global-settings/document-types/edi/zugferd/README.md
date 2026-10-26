# ZUGFeRD-Überblick

## Einführung

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) ist ein deutscher E-Invoicing-Standard, der auf der UN/CEFACT Cross Industry Invoice (CII) und der ISO-Norm 19005-3 (PDF/A-3) basiert. Er kombiniert strukturierte Rechnungsdaten mit einer PDF-Datei.

DocBits extrahiert Felder aus ZUGFeRD-Dokumenten und gleicht sie mit Infor ERP-Systemen (M3, LN) unter Verwendung von OAGIS BOD-Standards ab.

## Unterstützte ZUGFeRD-Versionen

DocBits unterstützt mehrere Versionen des ZUGFeRD-Standards:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Vollständige Kopffeldzuordnung

### Rechnungsidentifikation

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Rechnungsnummer |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Rechnungstypcode |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Rechnungsausstellungsdatum |
| `ExchangedDocument/IncludedNote` | `INVOICE_NOTE` | `Note` | STRING | Rechnungsanmerkungen |

### Dokumenttyp & Untertyp (TRA-gesteuert)

> Dieselbe Logik gilt für **Factur-X** — Factur-X 1.x verwendet das gleiche CII-Vokabular wie ZUGFeRD 2.x, sodass der unten beschriebene dynamische Block für beide ausgegeben wird.

Zusätzlich zum rohen `INVOICE_TYPE_CODE` erzeugt das Standard-TRANSFORMATION-XSLT einen kanonischen `<INVOICE>`-Baum mit zwei abgeleiteten Feldern:

| DocBits-Feld | Quelle | Logik |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `ExchangedDocument/TypeCode` (oder `HeaderExchangedDocument/TypeCode` bei ZUGFeRD 1.0) | UNCL 1001 `381` oder `261` → **Credit Note**; jeder andere Code → **Invoice** |
| `INVOICE_SUB_TYPE` | Vorhandensein von `BuyerOrderReferencedDocument/IssuerAssignedID` (unter `ApplicableHeaderTradeAgreement` bei 2.x / `ApplicableSupplyChainTradeAgreement` bei 1.0) | Nicht leer → **Purchase Invoice**; leer/fehlend → **Cost Invoice** |

`INVOICE_SUB_TYPE` unterscheidet bestellbezogene Rechnungen von direkten Kostenrechnungen für das AP-Routing.

### Dokumentreferenzen

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Bestellnummer |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Vertragsreferenz |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Lieferscheinreferenz |

### Datumsangaben

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Rechnungsdatum |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualShipDateTime` | DATE | Liefer-/Versanddatum |
| `SpecifiedTradePaymentTerms/DueDateDateTime` | `DUE_DATE` | `PaymentDueDateTime` | DATE | Fälligkeitsdatum |
| `BillingSpecifiedPeriod/StartDateTime` | `BILLING_PERIOD_START` | `BillingPeriodStart` | DATE | Beginn des Abrechnungszeitraums |
| `BillingSpecifiedPeriod/EndDateTime` | `BILLING_PERIOD_END` | `BillingPeriodEnd` | DATE | Ende des Abrechnungszeitraums |

### Lieferantenangaben (Verkäufer)

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Lieferanten-ID |
| `SellerTradeParty/GlobalID` | `VENDOR_GLN` | `SupplierPartyGLN` | STRING | Globale Lokationsnummer (GLN) |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Lieferantenname |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Adresszeile 1 |
| `SellerTradeParty/PostalTradeAddress/Line2` | `VENDOR_ADDRESS_2` | `SupplierAddress2` | STRING | Adresszeile 2 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postleitzahl |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Ort |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Ländercode |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `VAT_NO_EXTRACTED` | `SupplierTaxID` | STRING | Umsatzsteuer-Identifikationsnummer |
| `SellerTradeParty/DefinedTradeContact/EmailURIID` | `VENDOR_EMAIL` | `SupplierEmail` | STRING | E-Mail |
| `SellerTradeParty/DefinedTradeContact/TelephoneUniversalCommunication` | `VENDOR_PHONE` | `SupplierPhone` | STRING | Telefon |

### Käuferangaben

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Kunden-ID |
| `BuyerTradeParty/GlobalID` | `COMPANY_GLN` | `CustomerPartyGLN` | STRING | Globale Lokationsnummer (GLN) |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Firmenname |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Adresszeile 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postleitzahl |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | Ort |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Ländercode |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `COMPANY_VAT_ID` | `CustomerTaxID` | STRING | Umsatzsteuer-ID |

### Zahlungsinformationen

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | BIC-/SWIFT-Code |
| `SpecifiedTradePaymentTerms/Description` | `PAYMENT_TERMS` | `PaymentTerms` | STRING | Beschreibung der Zahlungsbedingungen |
| `SpecifiedTradeSettlementPaymentMeans/TypeCode` | `PAYMENT_METHOD` | `PaymentMethod` | STRING | Zahlungsartcode |

### Währung und Beträge auf Kopfebene

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Rechnungswährung |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Gesamtnettobetrag |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Gesamtsteuerbetrag |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Gesamtbetrag |
| `DuePayableAmount` | `AMOUNT_DUE` | `DuePayableAmount` | AMOUNT | Fälliger Betrag |
| `TotalPrepaidAmount` | `PREPAID_AMOUNT` | `TotalPrepaidAmount` | AMOUNT | Vorausgezahlter Betrag |
| `AllowanceTotalAmount` | `NEGATIVE_AMOUNT` | `AllowanceTotalAmount` | AMOUNT | Gesamte Abschläge |
| `ChargeTotalAmount` | `CHARGES` | `ChargeTotalAmount` | AMOUNT | Gesamte Zuschläge |

### Steueraufschlüsselung nach Steuersatzstufen <a href="#tax-breakdown-stufenklassifiziert" id="tax-breakdown-stufenklassifiziert"></a>

Das Standard-TRANSFORMATION-XSLT verteilt `ApplicableTradeTax`-Blöcke auf drei steuersatzbasierte Stufen anstatt positionale Indexe zu verwenden. Jeder Block wird anhand seines `RateApplicablePercent` einer Stufe zugeordnet:

| Stufe | DocBits-Felder | Auswahlregel |
| :--- | :--- | :--- |
| Stufe 1 (Regelsatz) | `TAX_RATE`, `NET_AMOUNT`, `TAX_AMOUNT` | rate ≥ 19 |
| Stufe 2 (ermäßigt) | `TAX_RATE_2`, `NET_AMOUNT_2`, `TAX_AMOUNT_2` | 0 < rate < 19 |
| Stufe 3 (Null) | `TAX_RATE_3`, `NET_AMOUNT_3`, `TAX_AMOUNT_3` | rate = 0 |

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (Stufe 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Mehrwertsteuersatz zum Regelsatz |
| `ApplicableTradeTax/BasisAmount` (Stufe 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Nettobetrag zum Regelsatz |
| `ApplicableTradeTax/CalculatedAmount` (Stufe 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Steuerbetrag zum Regelsatz |
| `ApplicableTradeTax/RateApplicablePercent` (Stufe 2) | `TAX_RATE_2` | `TaxPercent2` | NUMBER | Ermäßigter Mehrwertsteuersatz |
| `ApplicableTradeTax/BasisAmount` (Stufe 2) | `NET_AMOUNT_2` | `TaxableAmount2` | AMOUNT | Nettobetrag zum ermäßigten Satz |
| `ApplicableTradeTax/CalculatedAmount` (Stufe 2) | `TAX_AMOUNT_2` | `TaxAmount2` | AMOUNT | Steuerbetrag zum ermäßigten Satz |
| `ApplicableTradeTax/RateApplicablePercent` (Stufe 3) | `TAX_RATE_3` | `TaxPercent3` | NUMBER | Mehrwertsteuersatz zum Nullsatz |
| `ApplicableTradeTax/BasisAmount` (Stufe 3) | `NET_AMOUNT_3` | `TaxableAmount3` | AMOUNT | Nettobetrag zum Nullsatz |
| `ApplicableTradeTax/CalculatedAmount` (Stufe 3) | `TAX_AMOUNT_3` | `TaxAmount3` | AMOUNT | Steuerbetrag zum Nullsatz |

## Vollständige Positionszuordnung (Tabelle)

### Positionsidentifikation

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Positionsnummer |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Artikelnummer des Käufers |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Artikelnummer des Verkäufers |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_CODE` | `ItemCode` | STRING | Globale ID (GTIN/EAN) |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelbeschreibung |

### Positionsreferenzen

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Bestellnummer auf Positionsebene |
| `BuyerOrderReferencedDocument/LineID` | `PO_LINE_NUMBER` | `CustomerOrderLineNumber` | STRING | Bestellpositionsnummer |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Lieferschein |
| `DespatchAdviceReferencedDocument/LineID` | `DELIVERY_LINE` | `ShipmentLineNumber` | STRING | Lieferposition |

### Mengen und Einheiten

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Berechnete Menge |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Maßeinheitencode |
| `PackageQuantity` | `PACKAGE_QUANTITY` | `PackageQuantity` | NUMBER | Anzahl der Packstücke |

### Preisangaben

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Nettostückpreis |
| `GrossPriceProductTradePrice/ChargeAmount` | `GROSS_PRICE` | `GrossUnitPrice` | AMOUNT | Bruttostückpreis |
| `NetPriceProductTradePrice/BasisQuantity` | `UNIT_PRICE_PER_QUANTITY` | `PricePerQuantity` | NUMBER | Preisbezugsmenge |

### Positionsbeträge

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Positionsgesamtbetrag |
| `TotalAllowanceChargeAmount` | `NET_AMOUNT` | `NetAmount` | AMOUNT | Positionsnettobetrag |

### Steuer auf Positionsebene

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT` | `TaxPercent` | NUMBER | Mehrwertsteuersatz |
| `ApplicableTradeTax/TypeCode` | `TAX_CODE` | `TaxCode` | STRING | Steuerartcode |
| `ApplicableTradeTax/CategoryCode` | `TAX_CATEGORY` | `TaxCategoryCode` | STRING | Steuerkategorie |

### Abschläge und Zuschläge auf Positionsebene

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `AppliedTradeAllowanceCharge/ActualAmount` | `DISCOUNT` | `AllowanceAmount` | AMOUNT | Rabattbetrag |
| `AppliedTradeAllowanceCharge/CalculationPercent` | `DISCOUNT_PERCENT` | `AllowancePercent` | NUMBER | Rabattsatz |
| `AppliedTradeAllowanceCharge/ActualAmount` | `SURCHARGE` | `ChargeAmount` | AMOUNT | Zuschlagsbetrag |
| `AppliedTradeAllowanceCharge/Reason` | `ALLOWANCE_REASON` | `AllowanceReason` | STRING | Abschlagsgrund |

### Weitere Positionsfelder

| ZUGFeRD-CII-Pfad | DocBits-Feld | Infor-BOD-Feld | Typ | Beschreibung |
| :--- | :--- | :--- | :--- | :--- |
| `SpecifiedTradeProduct/OriginTradeCountry/ID` | `COUNTRY_OF_ORIGIN` | `CountryOfOrigin` | STRING | Ursprungsland |
| `SpecifiedTradeProduct/ApplicableProductCharacteristic/Value` | `PRODUCT_CHARACTERISTIC` | `ProductCharacteristic` | STRING | Produktmerkmal |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualDeliveryDate` | DATE | Lieferdatum der Position |

## Verwendete Regeln und Aktivierung

Wenn eine elektronische Gutschrift als Invoice erscheint, folgen Sie der [Anleitung zur Fehlerbehebung bei der Klassifizierung](../credit-note-recognized-as-invoice.md). Sie erläutert die verwendete angepasste oder standardmäßige Quelle, die Typcodes, Extraction Paths und die sichere Aktivierung.

## Länderanleitungen

Die Länderanleitungen enthalten genaue Formatbezeichnungen, Syntax, Versionsgrenzen und den geprüften Konfigurationsstand. [eDocs-Formate, Versionen und Länderanleitungen](../supported-electronic-documents/README.md).
