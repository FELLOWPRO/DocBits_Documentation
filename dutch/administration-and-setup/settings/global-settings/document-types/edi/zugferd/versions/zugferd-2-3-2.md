# ZUGFeRD 2.3.2 Veldmapping

## Overzicht

ZUGFeRD 2.3.2 is een onderhoudsrelease van de 2.3-standaard die compatibiliteit met de nieuwste CII-updates waarborgt.

## Mapping van headervelden

### Factuuridentificatie

| ZUGFeRD CII-pad | DocBits-veld | Infor BOD-veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Factuurnummer |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Factuurdatum |

### Documenttype en subtype (TRA-gestuurd)

De standaard TRANSFORMATION-XSLT geeft twee afgeleide velden uit:

| DocBits-veld | Bron | Logica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` of `261` → **Credit Note**; elke andere code → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Niet leeg → **Purchase Invoice**; leeg/ontbrekend → **Cost Invoice** |

### Belastingverdeling (op tier geclassificeerd)

`ApplicableTradeTax`-blokken worden verdeeld over drie op tarief gebaseerde tiers (niet positioneel `[1]`/`[2]`/`[3]`): velden voor het standaardtarief (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) bevatten tarief ≥ 19; velden voor het verlaagde tarief (`*_2`) bevatten 0 < tarief < 19; velden voor het nultarief (`*_3`) bevatten tarief = 0. Zie [ZUGFeRD-belastingverdeling](../README.md#belastingverdeling-tier-geclassificeerd) voor de volledige veldlijst.

| ZUGFeRD CII-pad | DocBits-veld | Infor BOD-veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (tier 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Btw tegen standaardtarief (≥ 19) |
| `ApplicableTradeTax/BasisAmount` (tier 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Nettobedrag tegen standaardtarief |
| `ApplicableTradeTax/CalculatedAmount` (tier 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Belastingbedrag tegen standaardtarief |

## Mapping van regelitems

| ZUGFeRD CII-pad | DocBits-veld | Infor BOD-veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Regelnummer |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelomschrijving |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Gefactureerde hoeveelheid |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto eenheidsprijs |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Regeltotaal |
