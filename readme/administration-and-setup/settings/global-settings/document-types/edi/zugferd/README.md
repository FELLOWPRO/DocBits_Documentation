# ZUGFeRD-overzicht

## Inleiding

ZUGFeRD (Zentraler User Guide des Forums elektronische Rechnung Deutschland) is een Duitse e-invoicingstandaard die is gebaseerd op de UN/CEFACT Cross Industry Invoice (CII) en ISO 19005-3 (PDF/A-3). Ze combineert gestructureerde factuurgegevens met een PDF-bestand.

DocBits extraheert velden uit ZUGFeRD-documenten en stemt ze af met Infor ERP-systemen (M3, LN) met behulp van OAGIS BOD-standaarden.

## Ondersteunde ZUGFeRD-versies

DocBits ondersteunt meerdere versies van de ZUGFeRD-standaard:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Volledige toewijzing van header-velden

### Factuuridentificatie

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Invoice number |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Factuurtypecode |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Datum van uitgifte van de factuur |
| `ExchangedDocument/IncludedNote` | `INVOICE_NOTE` | `Note` | STRING | Invoice notes |

### Documenttype en subtype (TRA-gestuurd)

> Dezelfde logica geldt voor **Factur-X** — Factur-X 1.x gebruikt dezelfde CII-vocabulaire als ZUGFeRD 2.x, dus het dynamische blok hieronder wordt voor beide uitgegeven.

Naast de ruwe `INVOICE_TYPE_CODE` geeft de standaard TRANSFORMATION-XSLT een canonieke `<INVOICE>`-boom uit met twee afgeleide velden:

| DocBits-veld | Bron | Logica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `ExchangedDocument/TypeCode` (of `HeaderExchangedDocument/TypeCode` voor ZUGFeRD 1.0) | UNCL 1001 `381` van `261` → **Creditnota**; elke andere code → **Factuur** |
| `INVOICE_SUB_TYPE` | Aanwezigheid van `BuyerOrderReferencedDocument/IssuerAssignedID` (onder `ApplicableHeaderTradeAgreement` voor 2.x / `ApplicableSupplyChainTradeAgreement` voor 1.0) | Niet-leeg → **Purchase Invoice**; leeg/ontbrekend → **Cost Invoice** |

`INVOICE_SUB_TYPE` onderscheidt PO-gekoppelde facturen van directe kostenfacturen voor AP-routing.

### Documentreferenties

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Inkoopordernummer |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Contract reference |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Referentie van de leveringsbon |

### Datums

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Invoice date |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualShipDateTime` | DATE | Leverings-/verzenddatum |
| `SpecifiedTradePaymentTerms/DueDateDateTime` | `DUE_DATE` | `PaymentDueDateTime` | DATE | Vervaldatum van betaling |
| `BillingSpecifiedPeriod/StartDateTime` | `BILLING_PERIOD_START` | `BillingPeriodStart` | DATE | Begin van de factureringsperiode |
| `BillingSpecifiedPeriod/EndDateTime` | `BILLING_PERIOD_END` | `BillingPeriodEnd` | DATE | Einde factureringsperiode |

### Gegevens van de leverancier (verkoper)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Supplier ID |
| `SellerTradeParty/GlobalID` | `VENDOR_GLN` | `SupplierPartyGLN` | STRING | Globaal locatienummer |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Supplier name |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Address line 1 |
| `SellerTradeParty/PostalTradeAddress/Line2` | `VENDOR_ADDRESS_2` | `SupplierAddress2` | STRING | Address line 2 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postal code |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | City |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Country code |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `VAT_NO_EXTRACTED` | `SupplierTaxID` | STRING | VAT registration number |
| `SellerTradeParty/DefinedTradeContact/EmailURIID` | `VENDOR_EMAIL` | `SupplierEmail` | STRING | Email |
| `SellerTradeParty/DefinedTradeContact/TelephoneUniversalCommunication` | `VENDOR_PHONE` | `SupplierPhone` | STRING | Phone |

### Kopersgegevens

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Customer ID |
| `BuyerTradeParty/GlobalID` | `COMPANY_GLN` | `CustomerPartyGLN` | STRING | Globaal locatienummer |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Company name |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Address line 1 |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Postal code |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | City |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Country code |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `COMPANY_VAT_ID` | `CustomerTaxID` | STRING | VAT ID |

### Betalingsgegevens

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | BIC/SWIFT code |
| `SpecifiedTradePaymentTerms/Description` | `PAYMENT_TERMS` | `PaymentTerms` | STRING | Beschrijving van de betalingsvoorwaarden |
| `SpecifiedTradeSettlementPaymentMeans/TypeCode` | `PAYMENT_METHOD` | `PaymentMethod` | STRING | Betaalmethodecode |

### Valuta en bedragen (kopniveau)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Invoice currency |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Totaal nettobedrag |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Totaal belastingbedrag |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Grand total |
| `DuePayableAmount` | `AMOUNT_DUE` | `DuePayableAmount` | AMOUNT | Amount due |
| `TotalPrepaidAmount` | `PREPAID_AMOUNT` | `TotalPrepaidAmount` | AMOUNT | Prepaid amount |
| `AllowanceTotalAmount` | `NEGATIVE_AMOUNT` | `AllowanceTotalAmount` | AMOUNT | Total allowances |
| `ChargeTotalAmount` | `CHARGES` | `ChargeTotalAmount` | AMOUNT | Total charges |

### Belastingverdeling (tier-geclassificeerd)

De standaard TRANSFORMATION-XSLT verdeelt `ApplicableTradeTax`-blokken over drie tarief-gebaseerde tiers in plaats van positionele indexen. Elk blok wordt toegewezen aan een tier op basis van zijn `RateApplicablePercent`:

| Tier | DocBits-velden | Selectieregel |
| :--- | :--- | :--- |
| Tier 1 (Standaard) | `TAX_RATE`, `NET_AMOUNT`, `TAX_AMOUNT` | tarief ≥ 19 |
| Tier 2 (Verlaagd) | `TAX_RATE_2`, `NET_AMOUNT_2`, `TAX_AMOUNT_2` | 0 < tarief < 19 |
| Tier 3 (Nul) | `TAX_RATE_3`, `NET_AMOUNT_3`, `TAX_AMOUNT_3` | tarief = 0 |

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (tier 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Standaard btw-percentage |
| `ApplicableTradeTax/BasisAmount` (tier 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Nettobedrag tegen standaardtarief |
| `ApplicableTradeTax/CalculatedAmount` (tier 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Belastingbedrag tegen standaardtarief |
| `ApplicableTradeTax/RateApplicablePercent` (tier 2) | `TAX_RATE_2` | `TaxPercent2` | NUMBER | Verlaagd btw-percentage |
| `ApplicableTradeTax/BasisAmount` (tier 2) | `NET_AMOUNT_2` | `TaxableAmount2` | AMOUNT | Nettobedrag tegen verlaagd tarief |
| `ApplicableTradeTax/CalculatedAmount` (tier 2) | `TAX_AMOUNT_2` | `TaxAmount2` | AMOUNT | Belastingbedrag tegen verlaagd tarief |
| `ApplicableTradeTax/RateApplicablePercent` (tier 3) | `TAX_RATE_3` | `TaxPercent3` | NUMBER | Nul btw-percentage |
| `ApplicableTradeTax/BasisAmount` (tier 3) | `NET_AMOUNT_3` | `TaxableAmount3` | AMOUNT | Nettobedrag tegen nultarief |
| `ApplicableTradeTax/CalculatedAmount` (tier 3) | `TAX_AMOUNT_3` | `TaxAmount3` | AMOUNT | Belastingbedrag tegen nultarief |

## Volledige Regelitemmapping (tabel)

### Regelidentificatie

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Line number |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Artikelnummer van de koper |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Artikelnummer van de verkoper |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_CODE` | `ItemCode` | STRING | Global ID (GTIN/EAN) |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Item description |

### Regelreferenties

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | PO nummer op lijnniveau |
| `BuyerOrderReferencedDocument/LineID` | `PO_LINE_NUMBER` | `CustomerOrderLineNumber` | STRING | PO line number |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Delivery note |
| `DespatchAdviceReferencedDocument/LineID` | `DELIVERY_LINE` | `ShipmentLineNumber` | STRING | Delivery line |

### Hoeveelheden en eenheden

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Billed quantity |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Maateenheidcode |
| `PackageQuantity` | `PACKAGE_QUANTITY` | `PackageQuantity` | NUMBER | Aantal pakketten |

### Prijzen

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto eenheidsprijs |
| `GrossPriceProductTradePrice/ChargeAmount` | `GROSS_PRICE` | `GrossUnitPrice` | AMOUNT | Bruto eenheidsprijs |
| `NetPriceProductTradePrice/BasisQuantity` | `UNIT_PRICE_PER_QUANTITY` | `PricePerQuantity` | NUMBER | Prijs basishoeveelheid |

### Regelbedragen

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Line total |
| `TotalAllowanceChargeAmount` | `NET_AMOUNT` | `NetAmount` | AMOUNT | Lijn nettobedrag |

### Regelbelasting

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT` | `TaxPercent` | NUMBER | VAT rate |
| `ApplicableTradeTax/TypeCode` | `TAX_CODE` | `TaxCode` | STRING | Belastingsoortcode |
| `ApplicableTradeTax/CategoryCode` | `TAX_CATEGORY` | `TaxCategoryCode` | STRING | Tax category |

### Kortingen en toeslagen (regelniveau)

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `AppliedTradeAllowanceCharge/ActualAmount` | `DISCOUNT` | `AllowanceAmount` | AMOUNT | Discount amount |
| `AppliedTradeAllowanceCharge/CalculationPercent` | `DISCOUNT_PERCENT` | `AllowancePercent` | NUMBER | Discount percentage |
| `AppliedTradeAllowanceCharge/ActualAmount` | `SURCHARGE` | `ChargeAmount` | AMOUNT | Surcharge amount |
| `AppliedTradeAllowanceCharge/Reason` | `ALLOWANCE_REASON` | `AllowanceReason` | STRING | Reden voor korting |

### Aanvullende regelvelden

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `SpecifiedTradeProduct/OriginTradeCountry/ID` | `COUNTRY_OF_ORIGIN` | `CountryOfOrigin` | STRING | Land van herkomst |
| `SpecifiedTradeProduct/ApplicableProductCharacteristic/Value` | `PRODUCT_CHARACTERISTIC` | `ProductCharacteristic` | STRING | Product characteristic |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualDeliveryDate` | DATE | Leveringsdatum van de lijn |

## Effectieve regels en activering

Als een elektronische creditnota als Invoice verschijnt, volg dan de [handleiding voor het oplossen van classificatieproblemen](../credit-note-recognized-as-invoice.md). Deze behandelt de effectieve aangepaste of standaardbron, typecodes, Extraction Paths en veilige activering.

## Landengidsen

Raadpleeg de landengidsen voor exacte formaatlabels, syntaxis, versiebeperkingen en de onderzochte configuratiestatus. [eDocs-formaten, versies en landengidsen](../supported-electronic-documents/README.md).
