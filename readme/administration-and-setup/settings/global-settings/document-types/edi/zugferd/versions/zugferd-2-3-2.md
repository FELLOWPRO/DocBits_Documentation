# ZUGFeRD 2.3.2 Veldomapping

## Overzicht

ZUGFeRD 2.3.2 was de eerste versie van de standaard. Hoewel deze verouderd is, gebruiken veel documenten nog steeds dit formaat. DocBits biedt volledige ondersteuning voor het extraheren van gegevens uit ZUGFeRD 2.3.2 XML-bestanden.

## Header Veldomapping

### Factuuridentificatie

| ZUGFeRD CII Pad | DocBits Veld | Infor BOD Veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Factuurnummer |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Factuurtypecode |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Factuurdatum |

### Documenttype en subtype (TRA-gestuurd)

De standaard TRANSFORMATION-XSLT geeft twee afgeleide velden uit:

| DocBits-veld | Bron | Logica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` of `261` → **Credit Note**; elke andere code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Niet-leeg → **Purchase Invoice**; leeg/ontbrekend → **Cost Invoice** |

### Belastingverdeling (tier-geclassificeerd)

`ApplicableTradeTax`-blokken worden verdeeld over drie tarief-gebaseerde tiers (niet positioneel `[1]`/`[2]`/`[3]`): standaardtariefvelden (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) vangen tarief ≥ 19; verlaagd-tariefvelden (`*_2`) vangen 0 < tarief < 19; nultariefvelden (`*_3`) vangen tarief = 0. Zie [ZUGFeRD belastingverdeling](../README.md#tax-breakdown-tier-classified) voor de volledige veldlijst.

| ZUGFeRD CII Path | DocBits Field | Infor BOD Field | Type | Description |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (tier 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Standaard btw (≥ 19) |
| `ApplicableTradeTax/BasisAmount` (tier 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Nettobedrag tegen standaardtarief |
| `ApplicableTradeTax/CalculatedAmount` (tier 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Belastingbedrag tegen standaardtarief |

### Documentreferenties

| ZUGFeRD CII Pad | DocBits Veld | Infor BOD Veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Inkoopordernummer |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Contractreferentie |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Leveringsbonreferentie |

### Leveranciersinformatie (Verkoper)

| ZUGFeRD CII Pad | DocBits Veld | Infor BOD Veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Leveranciers-ID |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Naam leverancier |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Adresregel 1 |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Postcode |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Stad |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Landcode |

## Regelitemmapping

| ZUGFeRD CII Pad | DocBits Veld | Infor BOD Veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Regelnummer |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Artikelnummer koper |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelomschrijving |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Gefactureerde hoeveelheid |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto eenheidsprijs |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Regeltotaal |
