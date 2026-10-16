# Mapeamento ZUGFeRD 2.3.2

## Visão geral

O ZUGFeRD 2.3.2 é uma versão de manutenção do padrão 2.3 e garante a compatibilidade com as atualizações mais recentes do CII.

## Mapeamento de campos de cabeçalho

### Identificação da fatura

| Caminho ZUGFeRD CII               | Campo DocBits    | Campo Infor BOD    | Tipo   | Descrição                 |
| --------------------------------- | ---------------- | ------------------ | ------ | ------------------------- |
| `ExchangedDocument/ID`            | `INVOICE_NUMBER` | `DocumentID`       | STRING | Número da fatura          |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE`   | `DocumentDateTime` | DATE   | Data de emissão da fatura |

### Tipo e subtipo do documento (orientado pelo TRA)

O XSLT de TRANSFORMATION padrão emite dois campos derivados:

| Campo DocBits      | Origem                                                                                                     | Lógica                                                                          |
| ------------------ | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `INVOICE_TYPE`     | `CrossIndustryInvoice/ExchangedDocument/TypeCode`                                                          | UNCL 1001 `381` ou `261` → **Credit Note**; qualquer outro código → **Invoice** |
| `INVOICE_SUB_TYPE` | `SupplyChainTradeTransaction/ApplicableHeaderTradeAgreement/BuyerOrderReferencedDocument/IssuerAssignedID` | Não vazio → **Purchase Invoice**; vazio/ausente → **Cost Invoice**              |

### Detalhamento de impostos (classificado por faixa)

Os blocos `ApplicableTradeTax` são distribuídos em três faixas baseadas em alíquota (não posicionais `[1]`/`[2]`/`[3]`): os campos de alíquota padrão (`TAX_RATE` / `NET_AMOUNT` / `TAX_AMOUNT`) capturam alíquota ≥ 19; os campos de alíquota reduzida (`*_2`) capturam 0 < alíquota < 19; os campos de alíquota zero (`*_3`) capturam alíquota = 0. Consulte [Detalhamento de impostos ZUGFeRD](./#detalhamento-de-impostos-classificado-por-faixa) para a lista completa de campos.

| Caminho ZUGFeRD CII                                  | Campo DocBits | Campo Infor BOD | Tipo   | Descrição                        |
| ---------------------------------------------------- | ------------- | --------------- | ------ | -------------------------------- |
| `ApplicableTradeTax/RateApplicablePercent` (faixa 1) | `TAX_RATE`    | `TaxPercent`    | NUMBER | IVA da faixa padrão (≥ 19)       |
| `ApplicableTradeTax/BasisAmount` (faixa 1)           | `NET_AMOUNT`  | `TaxableAmount` | AMOUNT | Valor líquido da faixa padrão    |
| `ApplicableTradeTax/CalculatedAmount` (faixa 1)      | `TAX_AMOUNT`  | `TaxAmount`     | AMOUNT | Valor do imposto da faixa padrão |

## Mapeamento de itens de linha

| Caminho ZUGFeRD CII                      | Campo DocBits  | Campo Infor BOD    | Tipo   | Descrição              |
| ---------------------------------------- | -------------- | ------------------ | ------ | ---------------------- |
| `AssociatedDocumentLineDocument/LineID`  | `POSITION`     | `LineNumber`       | STRING | Número da linha        |
| `SpecifiedTradeProduct/Name`             | `DESCRIPTION`  | `ItemDescription`  | STRING | Descrição do item      |
| `BilledQuantity`                         | `QUANTITY`     | `InvoicedQuantity` | NUMBER | Quantidade faturada    |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE`   | `UnitPrice`        | AMOUNT | Preço unitário líquido |
| `LineTotalAmount`                        | `TOTAL_AMOUNT` | `ExtendedAmount`   | AMOUNT | Total da linha         |
