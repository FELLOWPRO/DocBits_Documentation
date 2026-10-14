# ZUGFeRD 2.3 Veldmapping

## Overzicht

ZUGFeRD 2.3 is de nieuwste hoofdversie, met verbeteringen voor betere interoperabiliteit en naleving van moderne e-facturatievereisten.

## Header-veldmapping

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
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Niet-leeg → **Purchase Invoice**; leeg/ontbrekend → **Cost Invoice** |

### Betalingsinformatie

| ZUGFeRD CII-pad | DocBits-veld | Infor BOD-veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | BIC/SWIFT-code |

### Belastingverdeling (tier-geclassificeerd)

`ApplicableTradeTax`-blokken worden verdeeld over drie op tarief gebaseerde tiers (geen positionele indexen): standaardtariefvelden (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) vangen tarief ≥ 19; verlaagd-tariefvelden (`*_2`) vangen 0 < tarief < 19; nultariefvelden (`*_3`) vangen tarief = 0. Zie [ZUGFeRD belastingverdeling](../README.md#belastingverdeling-tier-geclassificeerd) voor de volledige veldlijst.

## Regelitemmapping

| ZUGFeRD CII-pad | DocBits-veld | Infor BOD-veld | Type | Beschrijving |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Regelnummer |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Artikelomschrijving |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Gefactureerde hoeveelheid |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Netto eenheidsprijs |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Regeltotaal |
