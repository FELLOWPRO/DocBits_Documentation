# Przegląd mapowania pól ZUGFeRD

## Wprowadzenie {#einfuhrung}

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) to niemiecki standard fakturowania elektronicznego oparty na UN/CEFACT Cross Industry Invoice (CII) oraz normie ISO 19005-3 (PDF/A-3). Umożliwia wymianę uporządkowanych danych faktur w pliku PDF.

DocBits wyodrębnia pola z dokumentów ZUGFeRD i porównuje je z systemami ERP Infor (M3, LN), korzystając ze standardów OAGIS BOD.

## Obsługiwane wersje ZUGFeRD {#unterstutzte-zugferd-versionen}

DocBits obsługuje wiele wersji standardu ZUGFeRD:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Pełne mapowanie pól nagłówka {#vollstandige-header-feldzuordnung}

### Identyfikacja faktury

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Kod typu faktury |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data wystawienia faktury |
| `ExchangedDocument/IncludedNote` | `INVOICE_NOTE` | `Note` | STRING | Invoice notes |

### Typ i podtyp dokumentu (sterowane przez TRA)

> Ta sama logika obowiązuje dla **Factur-X** — Factur-X 1.x używa tej samej składni CII co ZUGFeRD 2.x, więc poniższy dynamiczny blok jest emitowany dla obu.

Oprócz surowego `INVOICE_TYPE_CODE` domyślny TRANSFORMATION XSLT emituje kanoniczne drzewo `<INVOICE>` z dwoma polami pochodnymi:

| Pole DocBits | Źródło | Logika |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `ExchangedDocument/TypeCode` (lub `HeaderExchangedDocument/TypeCode` dla ZUGFeRD 1.0) | UNCL 1001 `381` lub `261` → **Credit Note**; dowolny inny kod → **Invoice** |
| `INVOICE_SUB_TYPE` | obecność `BuyerOrderReferencedDocument/IssuerAssignedID` (pod `ApplicableHeaderTradeAgreement` dla 2.x / `ApplicableSupplyChainTradeAgreement` dla 1.0) | Niepuste → **Purchase Invoice**; puste/brakujące → **Cost Invoice** |

`INVOICE_SUB_TYPE` rozróżnia faktury powiązane z PO od bezpośrednich faktur kosztowych na potrzeby routingu AP.

### Odwołania do dokumentów

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numer zamówienia |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Contract reference |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Odniesienie do dowodu dostawy |

### Daty

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice date |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualShipDateTime` | DATE | Data dostawy/wysyłki |
| `SpecifiedTradePaymentTerms/DueDateDateTime` | `DUE_DATE` | `PaymentDueDateTime` | DATE | Termin płatności |
| `BillingSpecifiedPeriod/StartDateTime` | `BILLING_PERIOD_START` | `BillingPeriodStart` | DATE | Rozpoczęcie okresu rozliczeniowego |
| `BillingSpecifiedPeriod/EndDateTime` | `BILLING_PERIOD_END` | `BillingPeriodEnd` | DATE | Koniec okresu rozliczeniowego |

### Informacje o dostawcy (sprzedawcy)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Supplier ID |
| `SellerTradeParty/GlobalID` | `VENDOR_GLN` | `SupplierPartyGLN` | STRING | Globalny numer lokalizacyjny |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Supplier name |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Address line 1 |
| `SellerTradeParty/PostalTradeAddress/Line2` | `VENDOR_ADDRESS_2` | `SupplierAddress2` | STRING | Address line 2 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postal code |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | City |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Country code |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `VAT_NO_EXTRACTED` | `SupplierTaxID` | STRING | VAT registration number |
| `SellerTradeParty/DefinedTradeContact/EmailURIID` | `VENDOR_EMAIL` | `SupplierEmail` | STRING | Email |
| `SellerTradeParty/DefinedTradeContact/TelephoneUniversalCommunication` | `VENDOR_PHONE` | `SupplierPhone` | STRING | Phone |

### Informacje o nabywcy

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Customer ID |
| `BuyerTradeParty/GlobalID` | `COMPANY_GLN` | `CustomerPartyGLN` | STRING | Globalny numer lokalizacyjny |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Company name |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Address line 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postal code |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | City |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Country code |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `COMPANY_VAT_ID` | `CustomerTaxID` | STRING | VAT ID |

### Informacje o płatności

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | BIC/SWIFT code |
| `SpecifiedTradePaymentTerms/Description` | `PAYMENT_TERMS` | `PaymentTerms` | STRING | Opis warunków płatności |
| `SpecifiedTradeSettlementPaymentMeans/TypeCode` | `PAYMENT_METHOD` | `PaymentMethod` | STRING | Kod metody płatności |

### Waluta i kwoty (nagłówek)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Invoice currency |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Łączna kwota netto |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Całkowita kwota podatku |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Grand total |
| `DuePayableAmount` | `AMOUNT_DUE` | `DuePayableAmount` | AMOUNT | Amount due |
| `TotalPrepaidAmount` | `PREPAID_AMOUNT` | `TotalPrepaidAmount` | AMOUNT | Prepaid amount |
| `AllowanceTotalAmount` | `NEGATIVE_AMOUNT` | `AllowanceTotalAmount` | AMOUNT | Total allowances |
| `ChargeTotalAmount` | `CHARGES` | `ChargeTotalAmount` | AMOUNT | Total charges |

### Podział podatków (klasyfikowany według poziomów)

Domyślny TRANSFORMATION XSLT rozdziela bloki `ApplicableTradeTax` na trzy poziomy oparte na stawce, zamiast korzystać z indeksów pozycyjnych. Każdy blok jest dopasowywany do poziomu na podstawie jego `RateApplicablePercent`:

| Poziom | Pola DocBits | Reguła wyboru |
| :--- | :--- | :--- |
| Poziom 1 (Standardowy) | `TAX_RATE`, `NET_AMOUNT`, `TAX_AMOUNT` | stawka ≥ 19 |
| Poziom 2 (Obniżony) | `TAX_RATE_2`, `NET_AMOUNT_2`, `TAX_AMOUNT_2` | 0 < stawka < 19 |
| Poziom 3 (Zero) | `TAX_RATE_3`, `NET_AMOUNT_3`, `TAX_AMOUNT_3` | stawka = 0 |

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (poziom 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Standardowa stawka VAT |
| `ApplicableTradeTax/BasisAmount` (poziom 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Kwota netto stawki standardowej |
| `ApplicableTradeTax/CalculatedAmount` (poziom 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Kwota podatku stawki standardowej |
| `ApplicableTradeTax/RateApplicablePercent` (poziom 2) | `TAX_RATE_2` | `TaxPercent2` | NUMBER | Obniżona stawka VAT |
| `ApplicableTradeTax/BasisAmount` (poziom 2) | `NET_AMOUNT_2` | `TaxableAmount2` | AMOUNT | Kwota netto stawki obniżonej |
| `ApplicableTradeTax/CalculatedAmount` (poziom 2) | `TAX_AMOUNT_2` | `TaxAmount2` | AMOUNT | Kwota podatku stawki obniżonej |
| `ApplicableTradeTax/RateApplicablePercent` (poziom 3) | `TAX_RATE_3` | `TaxPercent3` | NUMBER | Zerowa stawka VAT |
| `ApplicableTradeTax/BasisAmount` (poziom 3) | `NET_AMOUNT_3` | `TaxableAmount3` | AMOUNT | Kwota netto stawki zerowej |
| `ApplicableTradeTax/CalculatedAmount` (poziom 3) | `TAX_AMOUNT_3` | `TaxAmount3` | AMOUNT | Kwota podatku stawki zerowej |

## Pełne mapowanie pozycji liniowych (tabela)

### Identyfikacja pozycji

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Numer przedmiotu kupującego |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Numer przedmiotu sprzedającego |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_CODE` | `ItemCode` | STRING | Global ID (GTIN/EAN) |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |

### Odwołania pozycji

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Numer PO na poziomie linii |
| `BuyerOrderReferencedDocument/LineID` | `PO_LINE_NUMBER` | `CustomerOrderLineNumber` | STRING | PO line number |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Delivery note |
| `DespatchAdviceReferencedDocument/LineID` | `DELIVERY_LINE` | `ShipmentLineNumber` | STRING | Delivery line |

### Ilości i jednostki

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Kod jednostki miary |
| `PackageQuantity` | `PACKAGE_QUANTITY` | `PackageQuantity` | NUMBER | Liczba opakowań |

### Cennik

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Cena jednostkowa netto |
| `GrossPriceProductTradePrice/ChargeAmount` | `GROSS_PRICE` | `GrossUnitPrice` | AMOUNT | Cena jednostkowa brutto |
| `NetPriceProductTradePrice/BasisQuantity` | `UNIT_PRICE_PER_QUANTITY` | `PricePerQuantity` | NUMBER | Ilość bazowa ceny |

### Kwoty pozycji

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
| `TotalAllowanceChargeAmount` | `NET_AMOUNT` | `NetAmount` | AMOUNT | Linia kwota netto |

### Podatek pozycji

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT` | `TaxPercent` | NUMBER | VAT rate |
| `ApplicableTradeTax/TypeCode` | `TAX_CODE` | `TaxCode` | STRING | Kod rodzaju podatku |
| `ApplicableTradeTax/CategoryCode` | `TAX_CATEGORY` | `TaxCategoryCode` | STRING | Tax category |

### Rabaty i opłaty (pozycja)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AppliedTradeAllowanceCharge/ActualAmount` | `DISCOUNT` | `AllowanceAmount` | AMOUNT | Discount amount |
| `AppliedTradeAllowanceCharge/CalculationPercent` | `DISCOUNT_PERCENT` | `AllowancePercent` | NUMBER | Discount percentage |
| `AppliedTradeAllowanceCharge/ActualAmount` | `SURCHARGE` | `ChargeAmount` | AMOUNT | Surcharge amount |
| `AppliedTradeAllowanceCharge/Reason` | `ALLOWANCE_REASON` | `AllowanceReason` | STRING | Powód zasiłku |

### Dodatkowe pola pozycji

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SpecifiedTradeProduct/OriginTradeCountry/ID` | `COUNTRY_OF_ORIGIN` | `CountryOfOrigin` | STRING | Kraj pochodzenia |
| `SpecifiedTradeProduct/ApplicableProductCharacteristic/Value` | `PRODUCT_CHARACTERISTIC` | `ProductCharacteristic` | STRING | Product characteristic |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualDeliveryDate` | DATE | Data dostawy linii |

## Faktycznie używane reguły i aktywacja

Jeśli elektroniczna nota kredytowa jest wyświetlana jako Invoice, skorzystaj z [przewodnika rozwiązywania problemów z klasyfikacją](../credit-note-recognized-as-invoice.md). Opisuje on faktycznie używane źródło niestandardowe lub domyślne, kody typów, Extraction Paths i bezpieczną aktywację.

## Przewodniki krajowe

Przewodniki krajowe zawierają dokładne oznaczenia formatów, składnię, ograniczenia wersji i sprawdzony stan konfiguracji. [Formaty eDocs, wersje i przewodniki krajowe](../supported-electronic-documents/README.md).
