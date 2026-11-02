# Visão geral do mapeamento de campos ZUGFeRD

## Introdução

O ZUGFeRD é uma norma alemã de faturação eletrónica baseada no UN/CEFACT Cross Industry Invoice (CII) e na norma ISO 19005-3 (PDF/A-3). Permite trocar dados de fatura estruturados incorporados num ficheiro PDF.

O DocBits extrai campos de documentos ZUGFeRD e mapeia-os para sistemas ERP Infor (M3 e LN) através das normas OAGIS BOD.

## Versões ZUGFeRD suportadas

O DocBits suporta várias versões da norma ZUGFeRD:

* [ZUGFeRD 1.0](versions/zugferd-1-0.md)
* [ZUGFeRD 2.0](versions/zugferd-2-0.md)
* [ZUGFeRD 2.1 (Factur-X 1.0)](versions/zugferd-2-1.md)
* [ZUGFeRD 2.2](versions/zugferd-2-2.md)
* [ZUGFeRD 2.3](versions/zugferd-2-3.md)
* [ZUGFeRD 2.3.2](versions/zugferd-2-3-2.md)

## Mapeamento completo dos campos de cabeçalho

### Identificação da fatura

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/ID` | `INVOICE_NUMBER` | `DocumentID` | STRING | Número da fatura |
| `ExchangedDocument/TypeCode` | `INVOICE_TYPE_CODE` | `DocumentType` | STRING | Código do tipo de fatura |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data de emissão da fatura |
| `ExchangedDocument/IncludedNote` | `INVOICE_NOTE` | `Note` | STRING | Notas da fatura |

### Tipo e subtipo do documento (orientado pelo TRA)

> A mesma lógica se aplica ao **Factur-X** — Factur-X 1.x usa o mesmo vocabulário CII que o ZUGFeRD 2.x, então o bloco dinâmico abaixo é emitido para ambos.

Além do `INVOICE_TYPE_CODE` bruto, o XSLT de TRANSFORMATION padrão emite uma árvore `<INVOICE>` canônica com dois campos derivados:

| Campo DocBits | Origem | Lógica |
| :--- | :--- | :--- |
| `INVOICE_TYPE` | `ExchangedDocument/TypeCode` (ou `HeaderExchangedDocument/TypeCode` para ZUGFeRD 1.0) | UNCL 1001 `381` ou `261` → **Credit Note**; qualquer outro código → **Invoice** |
| `INVOICE_SUB_TYPE` | Presença de `BuyerOrderReferencedDocument/IssuerAssignedID` (sob `ApplicableHeaderTradeAgreement` para 2.x / `ApplicableSupplyChainTradeAgreement` para 1.0) | Não vazio → **Purchase Invoice**; vazio/ausente → **Cost Invoice** |

`INVOICE_SUB_TYPE` diferencia faturas vinculadas a PO das faturas de custo direto para roteamento de AP.

### Referências do documento

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Número do pedido de compra |
| `ContractReferencedDocument/ID` | `CONTRACT_NUMBER` | `ContractID` | STRING | Referência do contrato |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Referência da nota de entrega |

### Datas

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `ExchangedDocument/IssueDateTime` | `INVOICE_DATE` | `DocumentDateTime` | DATE | Data da fatura |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualShipDateTime` | DATE | Data de entrega/expedição |
| `SpecifiedTradePaymentTerms/DueDateDateTime` | `DUE_DATE` | `PaymentDueDateTime` | DATE | Data de vencimento do pagamento |
| `BillingSpecifiedPeriod/StartDateTime` | `BILLING_PERIOD_START` | `BillingPeriodStart` | DATE | Início do período de faturação |
| `BillingSpecifiedPeriod/EndDateTime` | `BILLING_PERIOD_END` | `BillingPeriodEnd` | DATE | Fim do período de faturação |

### Informações do fornecedor (vendedor)

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `SellerTradeParty/ID` | `VENDOR_ID` | `SupplierPartyID` | STRING | Identificador do fornecedor |
| `SellerTradeParty/GlobalID` | `VENDOR_GLN` | `SupplierPartyGLN` | STRING | Número Global de Localização |
| `SellerTradeParty/Name` | `VENDOR_NAME` | `SupplierPartyName` | STRING | Nome do fornecedor |
| `SellerTradeParty/PostalTradeAddress/Line1` | `VENDOR_ADDRESS` | `SupplierAddress1` | STRING | Linha 1 da morada |
| `SellerTradeParty/PostalTradeAddress/Line2` | `VENDOR_ADDRESS_2` | `SupplierAddress2` | STRING | Linha 2 da morada |
| `SellerTradeParty/PostalTradeAddress/PostcodeCode` | `VENDOR_POSTAL_CODE` | `SupplierPostalCode` | STRING | Código postal |
| `SellerTradeParty/PostalTradeAddress/CityName` | `VENDOR_CITY` | `SupplierCity` | STRING | Cidade |
| `SellerTradeParty/PostalTradeAddress/CountryID` | `VENDOR_COUNTRY` | `SupplierCountryCode` | STRING | Código do país |
| `SellerTradeParty/SpecifiedTaxRegistration/ID` | `VAT_NO_EXTRACTED` | `SupplierTaxID` | STRING | Número de identificação fiscal para IVA |
| `SellerTradeParty/DefinedTradeContact/EmailURIID` | `VENDOR_EMAIL` | `SupplierEmail` | STRING | Email |
| `SellerTradeParty/DefinedTradeContact/TelephoneUniversalCommunication` | `VENDOR_PHONE` | `SupplierPhone` | STRING | Phone |

### Informações do comprador

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerTradeParty/ID` | `COMPANY_ID` | `CustomerPartyID` | STRING | Identificador do cliente |
| `BuyerTradeParty/GlobalID` | `COMPANY_GLN` | `CustomerPartyGLN` | STRING | Número Global de Localização |
| `BuyerTradeParty/Name` | `COMPANY_NAME` | `CustomerPartyName` | STRING | Nome da empresa |
| `BuyerTradeParty/PostalTradeAddress/Line1` | `COMPANY_ADDRESS` | `CustomerAddress1` | STRING | Linha 1 da morada |
| `BuyerTradeParty/PostalTradeAddress/PostcodeCode` | `COMPANY_POSTAL_CODE` | `CustomerPostalCode` | STRING | Código postal |
| `BuyerTradeParty/PostalTradeAddress/CityName` | `COMPANY_CITY` | `CustomerCity` | STRING | Cidade |
| `BuyerTradeParty/PostalTradeAddress/CountryID` | `COMPANY_COUNTRY` | `CustomerCountryCode` | STRING | Código do país |
| `BuyerTradeParty/SpecifiedTaxRegistration/ID` | `COMPANY_VAT_ID` | `CustomerTaxID` | STRING | Identificador de IVA |

### Informações de pagamento

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `PayeePartyCreditorFinancialAccount/IBANID` | `IBAN_EXTRACTED` | `PayeeIBAN` | STRING | IBAN |
| `PayeeSpecifiedCreditorFinancialInstitution/BICID` | `BIC` | `PayeeBIC` | STRING | Código BIC/SWIFT |
| `SpecifiedTradePaymentTerms/Description` | `PAYMENT_TERMS` | `PaymentTerms` | STRING | Descrição das condições de pagamento |
| `SpecifiedTradeSettlementPaymentMeans/TypeCode` | `PAYMENT_METHOD` | `PaymentMethod` | STRING | Código do método de pagamento |

### Moeda e valores (cabeçalho)

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `InvoiceCurrencyCode` | `CURRENCY` | `CurrencyCode` | STRING | Moeda da fatura |
| `TaxBasisTotalAmount` | `TOTAL_NET_AMOUNT` | `TaxBasisTotalAmount` | AMOUNT | Valor líquido total |
| `TaxTotalAmount` | `TOTAL_TAX_AMOUNT` | `TaxTotalAmount` | AMOUNT | Valor total dos impostos |
| `GrandTotalAmount` | `TOTAL_AMOUNT` | `GrandTotalAmount` | AMOUNT | Total geral |
| `DuePayableAmount` | `AMOUNT_DUE` | `DuePayableAmount` | AMOUNT | Valor em dívida |
| `TotalPrepaidAmount` | `PREPAID_AMOUNT` | `TotalPrepaidAmount` | AMOUNT | Valor pago antecipadamente |
| `AllowanceTotalAmount` | `NEGATIVE_AMOUNT` | `AllowanceTotalAmount` | AMOUNT | Total de descontos |
| `ChargeTotalAmount` | `CHARGES` | `ChargeTotalAmount` | AMOUNT | Total de encargos |

### Detalhamento de impostos (classificado por faixa)

O XSLT de TRANSFORMATION padrão distribui os blocos `ApplicableTradeTax` em três faixas baseadas em alíquota, em vez de usar índices posicionais. Cada bloco é associado a uma faixa pelo seu `RateApplicablePercent`:

| Faixa | Campos DocBits | Regra de Seleção |
| :--- | :--- | :--- |
| Faixa 1 (Padrão) | `TAX_RATE`, `NET_AMOUNT`, `TAX_AMOUNT` | alíquota ≥ 19 |
| Faixa 2 (Reduzida) | `TAX_RATE_2`, `NET_AMOUNT_2`, `TAX_AMOUNT_2` | 0 < alíquota < 19 |
| Faixa 3 (Zero) | `TAX_RATE_3`, `NET_AMOUNT_3`, `TAX_AMOUNT_3` | alíquota = 0 |

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` (faixa 1) | `TAX_RATE` | `TaxPercent` | NUMBER | Percentual de IVA da faixa padrão |
| `ApplicableTradeTax/BasisAmount` (faixa 1) | `NET_AMOUNT` | `TaxableAmount` | AMOUNT | Valor líquido da faixa padrão |
| `ApplicableTradeTax/CalculatedAmount` (faixa 1) | `TAX_AMOUNT` | `TaxAmount` | AMOUNT | Valor do imposto da faixa padrão |
| `ApplicableTradeTax/RateApplicablePercent` (faixa 2) | `TAX_RATE_2` | `TaxPercent2` | NUMBER | Percentual de IVA da faixa reduzida |
| `ApplicableTradeTax/BasisAmount` (faixa 2) | `NET_AMOUNT_2` | `TaxableAmount2` | AMOUNT | Valor líquido da faixa reduzida |
| `ApplicableTradeTax/CalculatedAmount` (faixa 2) | `TAX_AMOUNT_2` | `TaxAmount2` | AMOUNT | Valor do imposto da faixa reduzida |
| `ApplicableTradeTax/RateApplicablePercent` (faixa 3) | `TAX_RATE_3` | `TaxPercent3` | NUMBER | Percentual de IVA da faixa zero |
| `ApplicableTradeTax/BasisAmount` (faixa 3) | `NET_AMOUNT_3` | `TaxableAmount3` | AMOUNT | Valor líquido com alíquota zero |
| `ApplicableTradeTax/CalculatedAmount` (faixa 3) | `TAX_AMOUNT_3` | `TaxAmount3` | AMOUNT | Valor do imposto da faixa zero |

## Mapeamento completo de itens de linha (tabela)

### Identificação da linha

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `AssociatedDocumentLineDocument/LineID` | `POSITION` | `LineNumber` | STRING | Número da linha |
| `SpecifiedTradeProduct/BuyerAssignedID` | `ITEM_NUMBER` | `BuyerItemID` | STRING | Número do artigo do comprador |
| `SpecifiedTradeProduct/SellerAssignedID` | `SUPPLIER_ITEM_NUMBER` | `SellerItemID` | STRING | Número do artigo do vendedor |
| `SpecifiedTradeProduct/GlobalID` | `ITEM_CODE` | `ItemCode` | STRING | Identificador global (GTIN/EAN) |
| `SpecifiedTradeProduct/Name` | `DESCRIPTION` | `ItemDescription` | STRING | Descrição do artigo |

### Referências da linha

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `BuyerOrderReferencedDocument/ID` | `PURCHASE_ORDER` | `CustomerOrderID` | STRING | Número do pedido de compra da linha |
| `BuyerOrderReferencedDocument/LineID` | `PO_LINE_NUMBER` | `CustomerOrderLineNumber` | STRING | Número da linha do pedido de compra |
| `DespatchAdviceReferencedDocument/ID` | `DELIVERY_NOTE` | `ShipmentID` | STRING | Nota de entrega |
| `DespatchAdviceReferencedDocument/LineID` | `DELIVERY_LINE` | `ShipmentLineNumber` | STRING | Linha de entrega |

### Quantidades e unidades

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `BilledQuantity` | `QUANTITY` | `InvoicedQuantity` | NUMBER | Quantidade faturada |
| `BilledQuantity/@unitCode` | `UNIT` | `UnitCode` | STRING | Código da unidade de medida |
| `PackageQuantity` | `PACKAGE_QUANTITY` | `PackageQuantity` | NUMBER | Número de embalagens |

### Preços

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `NetPriceProductTradePrice/ChargeAmount` | `UNIT_PRICE` | `UnitPrice` | AMOUNT | Preço unitário líquido |
| `GrossPriceProductTradePrice/ChargeAmount` | `GROSS_PRICE` | `GrossUnitPrice` | AMOUNT | Preço unitário bruto |
| `NetPriceProductTradePrice/BasisQuantity` | `UNIT_PRICE_PER_QUANTITY` | `PricePerQuantity` | NUMBER | Quantidade base do preço |

### Valores da linha

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `LineTotalAmount` | `TOTAL_AMOUNT` | `ExtendedAmount` | AMOUNT | Total da linha |
| `TotalAllowanceChargeAmount` | `NET_AMOUNT` | `NetAmount` | AMOUNT | Valor líquido da linha |

### Impostos da linha

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `ApplicableTradeTax/RateApplicablePercent` | `VAT` | `TaxPercent` | NUMBER | Taxa de IVA |
| `ApplicableTradeTax/TypeCode` | `TAX_CODE` | `TaxCode` | STRING | Código do tipo de imposto |
| `ApplicableTradeTax/CategoryCode` | `TAX_CATEGORY` | `TaxCategoryCode` | STRING | Categoria de imposto |

### Descontos e encargos (itens de linha)

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `AppliedTradeAllowanceCharge/ActualAmount` | `DISCOUNT` | `AllowanceAmount` | AMOUNT | Valor do desconto |
| `AppliedTradeAllowanceCharge/CalculationPercent` | `DISCOUNT_PERCENT` | `AllowancePercent` | NUMBER | Percentagem de desconto |
| `AppliedTradeAllowanceCharge/ActualAmount` | `SURCHARGE` | `ChargeAmount` | AMOUNT | Valor do encargo adicional |
| `AppliedTradeAllowanceCharge/Reason` | `ALLOWANCE_REASON` | `AllowanceReason` | STRING | Motivo do desconto |

### Campos adicionais dos itens de linha

| Caminho CII ZUGFeRD | Campo do DocBits | Campo Infor BOD | Tipo | Descrição |
| :--- | :--- | :--- | :--- | :--- |
| `SpecifiedTradeProduct/OriginTradeCountry/ID` | `COUNTRY_OF_ORIGIN` | `CountryOfOrigin` | STRING | País de origem |
| `SpecifiedTradeProduct/ApplicableProductCharacteristic/Value` | `PRODUCT_CHARACTERISTIC` | `ProductCharacteristic` | STRING | Característica do produto |
| `ActualDeliverySupplyChainEvent/OccurrenceDateTime` | `DELIVERY_DATE` | `ActualDeliveryDate` | DATE | Data de entrega da linha |

## Regras efetivas e ativação

Se uma nota de crédito eletrónica aparecer como Invoice, siga o [guia de resolução de problemas de classificação](../credit-note-recognized-as-invoice.md). Este explica como verificar a origem personalizada ou predefinida efetivamente utilizada, os códigos de tipo, os Extraction Paths e a ativação segura.

## Guias por país

Consulte os guias por país para obter as designações exatas dos formatos, a sintaxe, os limites das versões e o estado da configuração examinada. [Formatos, versões e guias por país para eDocs](../supported-electronic-documents/README.md).
