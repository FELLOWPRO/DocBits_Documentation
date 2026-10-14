# ZUGFeRD 2.2 Veldmapping

## Overzicht

ZUGFeRD 2.2 zet de afstemming op EN 16931 voort en neemt verdere updates van de CII-standaard over.

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

`ApplicableTradeTax`-blokken worden verdeeld over drie op tarief gebaseerde tiers (niet op positionele indexen): velden voor het standaardtarief (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) bevatten tarief ≥ 19; velden voor het verlaagde tarief (`*_2`) bevatten 0 < tarief < 19; velden voor het nultarief (`*_3`) bevatten tarief = 0. Zie [ZUGFeRD-belastingverdeling](../README.md#belastingverdeling-tier-geclassificeerd) voor de volledige veldlijst.

### Valuta en bedragen

| ZUGFeRD CII-pad | DocBits-veld | Infor BOD-veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Factuurvaluta |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Totaal nettobedrag |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Totaal belastingbedrag |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Eindtotaal |

## Mapping van regelitems

| ZUGFeRD CII-pad | DocBits-veld | Infor BOD-veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Regelnummer |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelomschrijving |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Gefactureerde hoeveelheid |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto eenheidsprijs |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Regeltotaal |
