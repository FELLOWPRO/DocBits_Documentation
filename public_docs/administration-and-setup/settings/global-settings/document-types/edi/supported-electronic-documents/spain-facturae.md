---
description: Suporte para a fatura eletrónica espanhola Facturae (3.2, 3.2.1, 3.2.2) no DocBits
---

# 🇪🇸 Spain Facturae

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Espanha |
| **Tipos de documento** | Fatura (Factura), Nota de crédito |
| **Formato** | XML |
| **Padrão** | Facturae 3.2 / 3.2.1 / 3.2.2 (Agencia Tributaria / AEAT) |
| **Locale** | `es_ES` |

Facturae é o padrão obrigatório de fatura eletrónica espanhola, regulado pela Agencia Estatal de Administración Tributaria (AEAT) e pelo Ministério das Finanças. É obrigatório para faturas direcionadas a entidades do setor público espanhol e amplamente utilizado em transações B2B. O elemento raiz é `<fe:Facturae>` com um URL de namespace versionado. O DocBits deteta a versão através do atributo `xsi:schemaLocation`, que faz referência a um dos URLs de esquema oficiais:

| Versão | URL do esquema |
|---------|-----------|
| Facturae 3.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2.xml` |
| Facturae 3.2.1 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_1.xml` |
| Facturae 3.2.2 | `http://www.facturae.gob.es/formato/Versiones/Facturaev3_2_2.xml` |

## Status de suporte

| Componente | Status |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="spain-facturae-preview.png" alt="Spain Facturae invoice preview in DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura Facturae 3.2.2 espanhola</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML fonte | Notas |
|---|---|---|
| `invoice_id` | `Invoices/Invoice/InvoiceHeader/InvoiceNumber` | Número da fatura |
| `invoice_date` | `Invoices/Invoice/InvoiceIssueData/IssueDate` | Data de emissão (AAAA-MM-DD) |
| `due_date` | `PaymentDetails/Installment/InstallmentDueDate` | Data de vencimento do pagamento |
| `invoice_type` | `Invoices/Invoice/InvoiceHeader/InvoiceDocumentType` | FC=Fatura, NC=Nota de crédito |
| `currency` | `Invoices/Invoice/InvoiceIssueData/InvoiceCurrencyCode` | Sempre `EUR` |
| `purchase_order` | `Invoices/Invoice/InvoiceHeader/ReceiverContractReference` | Referência do pedido / contrato do comprador |
| `net_amount` | `Invoices/Invoice/InvoiceTotals/TotalGrossAmountBeforeTaxes` | Valor líquido excl. IVA |
| `tax_amount` | `Invoices/Invoice/InvoiceTotals/TotalTaxOutputs` | Valor total do IVA |
| `total_amount` | `Invoices/Invoice/InvoiceTotals/InvoiceTotal` | Valor total incl. IVA |
| `tax_rate` | `TaxesOutputs/Tax/TaxRate` | Taxa de IVA em % (padrão 21%) |
| `payment_terms` | `PaymentDetails/Installment/PaymentMeans` | Código do meio de pagamento |
| `supplier_name` | `Parties/SellerParty/LegalEntity/CorporateName` | Nome da empresa vendedora |
| `supplier_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF (ex. `ES12345678A`) |
| `supplier_tax_id` | `Parties/SellerParty/TaxIdentification/TaxIdentificationNumber` | NIF ou CIF espanhol |
| `supplier_address` | `Parties/SellerParty/LegalEntity/AddressInSpain/Address` | Morada do vendedor |
| `supplier_city` | `Parties/SellerParty/LegalEntity/AddressInSpain/Town` | Cidade do vendedor |
| `supplier_postal_code` | `Parties/SellerParty/LegalEntity/AddressInSpain/PostCode` | Código postal do vendedor |
| `supplier_country` | `Parties/SellerParty/LegalEntity/AddressInSpain/CountryCode` | Código de país ISO (`ESP`) |
| `buyer_name` | `Parties/BuyerParty/LegalEntity/CorporateName` | Nome da empresa compradora |
| `buyer_id` | `Parties/BuyerParty/TaxIdentification/TaxIdentificationNumber` | NIF/CIF do comprador |
| `buyer_address` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Address` | Morada do comprador |
| `buyer_city` | `Parties/BuyerParty/LegalEntity/AddressInSpain/Town` | Cidade do comprador |
| `buyer_postal_code` | `Parties/BuyerParty/LegalEntity/AddressInSpain/PostCode` | Código postal do comprador |
| `buyer_country` | `Parties/BuyerParty/LegalEntity/AddressInSpain/CountryCode` | Código de país ISO (`ESP`) |
| `iban` | `PaymentDetails/Installment/AccountToBeCredited/IBAN` | IBAN do beneficiário |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `Invoices/Invoice/Items/InvoiceLine`

| Coluna | Elemento XML fonte | Notas |
|---|---|---|
| `POSITION` | `ItemDescription` | Sequência / descrição da linha usada como identificador |
| `DESCRIPTION` | `ItemDescription` | Descrição do artigo |
| `QUANTITY` | `Quantity` | Quantidade faturada |
| `UNIT` | `UnitOfMeasure` | Unidade de medida (ex. `units`) |
| `UNIT_PRICE` | `UnitPriceWithoutTax` | Preço unitário excl. IVA |
| `VAT_RATE` | `TaxesOutputs/Tax/TaxRate` | Taxa de IVA em % (tipicamente 21%) |
| `VAT` | `TaxesOutputs/Tax/TaxAmount/TotalAmount` | Valor do IVA por linha |
| `NET_AMOUNT` | `TotalCost` | Total da linha excl. IVA |

## Regras de classificação

O DocBits deteta documentos Facturae correspondendo ao atributo `xsi:schemaLocation` no elemento raiz `<fe:Facturae>`:

| Tipo de documento eletrónico | Padrão |
|--------------------------|---------|
| FACTURAE 3.2 | `xsi:schemaLocation` contém `Facturaev3_2.xml` (não 3_2_1 ou 3_2_2) |
| FACTURAE 3.2.1 | `xsi:schemaLocation` contém `Facturaev3_2_1.xml` |
| FACTURAE 3.2.2 | `xsi:schemaLocation` contém `Facturaev3_2_2.xml` |

O elemento raiz é `<fe:Facturae>` com namespace `http://www.facturae.es/Facturae/2014/v3.2.2/Facturae` (específico da versão). A classificação usa o princípio **primeira correspondência vence**, com padrões mais específicos (3.2.2, 3.2.1) avaliados antes do genérico 3.2.

## Relacionados

- [Padrões de fatura eletrónica atualmente suportados](../../currently-supported-e-invoice-standards/)
- [Documentos eletrónicos suportados](./)
