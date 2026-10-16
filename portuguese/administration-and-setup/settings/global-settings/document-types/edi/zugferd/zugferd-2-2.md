# Mapeamento ZUGFeRD 2.2

## Visão geral

O ZUGFeRD 2.2 continua o alinhamento com a EN 16931 e incorpora outras atualizações do padrão CII.

## Mapeamento dos campos de cabeçalho

### Identificação da fatura

| Caminho CII do ZUGFeRD            | Campo do DocBits | Campo do Infor BOD | Tipo   | Descrição                 |
| --------------------------------- | ---------------- | ------------------ | ------ | ------------------------- |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | Número da fatura          |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | Data de emissão da fatura |

### Tipo e subtipo do documento (orientados pelo TRA)

O XSLT de TRANSFORMATION padrão gera dois campos derivados:

| Campo do DocBits   | Origem                                                                                                     | Lógica                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` ou `261` → **Credit Note**; qualquer outro código → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Não vazio → **Purchase Invoice**; vazio/ausente → **Cost Invoice**              |

### Detalhamento de impostos (classificado por faixa)

Os blocos `ApplicableTradeTax` são distribuídos em três faixas baseadas na alíquota (não em índices posicionais): os campos da alíquota padrão (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capturam alíquota ≥ 19; os campos da alíquota reduzida (`*_2`) capturam 0 < alíquota < 19; os campos da alíquota zero (`*_3`) capturam alíquota = 0. Consulte [Detalhamento de impostos do ZUGFeRD](./#detalhamento-de-impostos-classificado-por-faixa) para ver a lista completa de campos.

### Moeda e valores

| Caminho CII do ZUGFeRD | Campo do DocBits   | Campo do Infor BOD    | Tipo   | Descrição               |
| ---------------------- | ------------------ | --------------------- | ------ | ----------------------- |
| `InvoiceCurrencyCode`  | `CURRENCY`         | `CurrencyCode`        | STRING | Moeda da fatura         |
| `TaxBasisTotalAmount`  | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Valor líquido total     |
| `TaxTotalAmount`       | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount`      | AMOUNT | Valor total de impostos |
| `GrandTotalAmount`     | `TOTAL_AMOUNT`     | `GrandTotalAmount`    | AMOUNT | Total geral             |

## Mapeamento dos itens de linha

| Caminho CII do ZUGFeRD                   | Campo do DocBits | Campo do Infor BOD | Tipo   | Descrição              |
| ---------------------------------------- | ---------------- | ------------------ | ------ | ---------------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`       | `LineNumber`       | STRING | Número da linha        |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`    | `ItemDescription`  | STRING | Descrição do item      |
| `BilledQuantity`                         | `QUANTITY`       | `InvoicedQuantity` | NUMBER | Quantidade faturada    |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`     | `UnitPrice`        | AMOUNT | Preço unitário líquido |
| `LineTotalAmount`                        | `TOTAL_AMOUNT`   | `ExtendedAmount`   | AMOUNT | Total da linha         |
