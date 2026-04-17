---
description: Suporte para documentos Finvoice finlandeses (1.3, 2.0, 2.01, 3.0) no DocBits
---

# 🇫🇮 Finland Finvoice

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Finlândia |
| **Tipos de documento** | Fatura (Lasku), Nota de crédito (Hyvityslasku) |
| **Formato** | XML |
| **Padrão** | Finvoice 1.3 / 2.0 / 2.01 / 3.0 (Finance Finland / Finanssiala) |
| **Locale** | `fi_FI` |

Finvoice é o padrão de faturação eletrónica do setor bancário finlandês, desenvolvido e mantido pela Finance Finland (Finanssiala ry). É utilizado para faturação B2B e B2G e é transmitido através da infraestrutura bancária finlandesa. O elemento raiz é `<Finvoice>` com um URL de namespace versionado. O DocBits deteta a versão através do atributo `xmlns`:

| Versão | URL do namespace |
|---------|--------------|
| Finvoice 1.3 | `http://www.finvoice.fi/schema/finvoice13` |
| Finvoice 2.0 | `http://www.finvoice.fi/schema/finvoice20` |
| Finvoice 2.01 | `http://www.finvoice.fi/schema/finvoice201` |
| Finvoice 3.0 | `http://www.finvoice.fi/schema/finvoice30` |

O formato do ID de empresa finlandês (Y-tunnus) é `1234567-8` (7 dígitos + dígito de controlo), utilizado como identificador de parte. O número de IVA tem o prefixo `FI` seguido de 8 dígitos (ex. `FI12345678`). As datas são codificadas no formato `CCYYMMDD`.

## Status de suporte

| Componente | Status |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="finland-finvoice-preview.png" alt="Finland Finvoice 3.0 invoice preview in DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura Finland Finvoice 3.0 (Lasku)</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML fonte | Notas |
|---|---|---|
| `invoice_id` | `InvoiceDetails/InvoiceNumber` | Número da fatura |
| `invoice_date` | `InvoiceDetails/InvoiceDate` | Data no formato `CCYYMMDD`, convertida para ISO 8601 |
| `due_date` | `InvoiceDetails/PaymentTermsDetails/InvoiceDueDate` | Data de vencimento (`CCYYMMDD`) |
| `invoice_type` | `InvoiceDetails/InvoiceTypeCode` | INV01=Fatura, CRE01=Nota de crédito |
| `currency` | `InvoiceDetails/InvoiceTotalVatExcludedAmount/@AmountCurrencyIdentifier` | Código de moeda (tipicamente `EUR`) |
| `net_amount` | `InvoiceDetails/InvoiceTotalVatExcludedAmount` | Valor líquido excl. IVA |
| `tax_amount` | `InvoiceDetails/InvoiceTotalVatAmount` | Valor total do IVA |
| `total_amount` | `InvoiceDetails/InvoiceTotalVatIncludedAmount` | Valor total incl. IVA |
| `tax_rate` | `InvoiceDetails/VatSpecificationDetails/VatRatePercent` | Taxa de IVA em % (padrão 25,5%) |
| `supplier_name` | `SellerPartyDetails/SellerOrganisationName` | Nome da empresa vendedora |
| `supplier_id` | `SellerPartyDetails/SellerPartyIdentifier` | ID de empresa finlandês (Y-tunnus, ex. `1234567-8`) |
| `supplier_vat` | `SellerPartyDetails/SellerOrganisationTaxCode` | Número de IVA (ex. `FI12345678`) |
| `supplier_address` | `SellerPartyDetails/SellerPostalAddressDetails/SellerStreetName` | Morada do vendedor |
| `supplier_city` | `SellerPartyDetails/SellerPostalAddressDetails/SellerTownName` | Cidade do vendedor |
| `supplier_postal_code` | `SellerPartyDetails/SellerPostalAddressDetails/SellerPostCodeIdentifier` | Código postal do vendedor |
| `supplier_country` | `SellerPartyDetails/SellerPostalAddressDetails/CountryCode` | Código de país ISO (`FI`) |
| `buyer_name` | `BuyerPartyDetails/BuyerOrganisationName` | Nome da empresa compradora |
| `buyer_id` | `BuyerPartyDetails/BuyerPartyIdentifier` | ID de empresa finlandês (Y-tunnus) |
| `buyer_address` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerStreetName` | Morada do comprador |
| `buyer_city` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerTownName` | Cidade do comprador |
| `buyer_postal_code` | `BuyerPartyDetails/BuyerPostalAddressDetails/BuyerPostCodeIdentifier` | Código postal do comprador |
| `buyer_country` | `BuyerPartyDetails/BuyerPostalAddressDetails/CountryCode` | Código de país ISO (`FI`) |
| `iban` | `EpiDetails/EpiBfiPartyDetails/EpiBfiIdentifier` | IBAN do beneficiário (detalhes de pagamento EPI) |
| `bic` | `EpiDetails/EpiPaymentInstructionId` | Código BIC/SWIFT |
| `payment_terms` | `InvoiceDetails/PaymentTermsDetails/PaymentTermsFreeText` | Condições de pagamento em texto livre |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `InvoiceRow`

| Coluna | Elemento XML fonte | Notas |
|---|---|---|
| `POSITION` | `InvoiceRow/ArticleIdentifier` | Código de artigo / produto |
| `DESCRIPTION` | `InvoiceRow/ArticleName` | Nome / descrição do artigo |
| `QUANTITY` | `InvoiceRow/DeliveredQuantity` | Quantidade entregue |
| `UNIT` | `InvoiceRow/DeliveredQuantity/@QuantityUnitCode` | Código de unidade (ex. `KPL` = peça) |
| `UNIT_PRICE` | `InvoiceRow/UnitPriceAmount` | Preço unitário excl. IVA |
| `VAT_RATE` | `InvoiceRow/RowVatRatePercent` | Taxa de IVA em % por linha |
| `VAT` | `InvoiceRow/RowVatAmount` | Valor do IVA por linha |
| `NET_AMOUNT` | `InvoiceRow/RowAmount` | Total da linha excl. IVA |

## Regras de classificação

O DocBits deteta documentos Finvoice correspondendo ao atributo `xmlns` no elemento raiz `<Finvoice>`:

| Tipo de documento eletrónico | Padrão |
|--------------------------|---------|
| FINVOICE 1.3 | `xmlns` contém `http://www.finvoice.fi/schema/finvoice13` |
| FINVOICE 2.0 | `xmlns` contém `http://www.finvoice.fi/schema/finvoice20` (não 2.01) |
| FINVOICE 2.01 | `xmlns` contém `http://www.finvoice.fi/schema/finvoice201` |
| FINVOICE 3.0 | `xmlns` contém `http://www.finvoice.fi/schema/finvoice30` |

A classificação usa o princípio **primeira correspondência vence** com padrões mais específicos (2.01) avaliados antes do genérico 2.0.

## Relacionados

- [Padrões de fatura eletrónica atualmente suportados](../../currently-supported-e-invoice-standards/)
- [Finland TEAPPSXML](./finland-teappsxml.md)
- [Documentos eletrónicos suportados](./)
