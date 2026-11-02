# Mapeamento de campos ZUGFeRD 2.3

## Visão geral

O ZUGFeRD 2.3 é a versão principal mais recente e incorpora melhorias para uma melhor interoperabilidade e conformidade com os requisitos modernos de faturamento eletrônico.

## Mapeamento de campos de cabeçalho

### Identificação da fatura

| Caminho ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Número da fatura |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data de emissão da fatura |

### Tipo e subtipo do documento (orientado pelo TRA)

O XSLT de TRANSFORMATION padrão emite dois campos derivados:

| Campo DocBits | Origem | Lógica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `CrossIndustryInvoice/ExchangedDocument/TypeCode` | UNCL 1001 `381` ou `261` → **Credit Note**; qualquer outro código → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Não vazio → **Purchase Invoice**; vazio/ausente → **Cost Invoice** |

### Informações de pagamento

| Caminho ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | Código BIC/SWIFT |

### Detalhamento de impostos (classificado por faixa)

Os blocos `ApplicableTradeTax` são distribuídos em três faixas baseadas em alíquota (não índices posicionais): os campos de alíquota padrão (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capturam alíquota ≥ 19; os campos de alíquota reduzida (`*_2`) capturam 0 < alíquota < 19; os campos de alíquota zero (`*_3`) capturam alíquota = 0. Consulte [Detalhamento de impostos ZUGFeRD](../README.md#detalhamento-de-impostos-classificado-por-faixa) para a lista completa de campos.

## Mapeamento de itens de linha

| Caminho ZUGFeRD CII | Campo DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Número da linha |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Descrição do item |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Quantidade faturada |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Preço unitário líquido |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Total da linha |
