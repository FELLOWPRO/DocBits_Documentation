---
description: Suporte a documentos eletrônicos PINT A-NZ no DocBits
---

# 🇦🇺 PINT A-NZ

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Austrália / Nova Zelândia |
| **Tipos de documento** | Fatura, Nota de crédito |
| **Formato** | UBL 2.1 XML |
| **Padrão** | PINT A-NZ (Peppol International Model for Australia-New Zealand) |
| **Locale** | `en_AU` |

PINT A-NZ (Peppol International Model for Australia-New Zealand) é a especificação de faturação Peppol localizada para a região da Austrália/Nova Zelândia. Estende o modelo PINT global com regras de negócio específicas do A-NZ, categorias de imposto (GST) e esquemas de identificação (ABN, NZBN). Esta é a página de referência técnica com o mapeamento completo de campos.

## Estado do suporte

| Componente | Estado |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="aunz-pint-preview.png" alt="Pré-visualização da fatura PINT A-NZ no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura PINT A-NZ</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | XPath de origem (UBL 2.1) | Notas |
|---|---|---|
| `invoice_id` | `cbc:ID` | Número da fatura |
| `invoice_date` | `cbc:IssueDate` | Data ISO 8601 |
| `due_date` | `cbc:DueDate` | Data de vencimento |
| `currency` | `cbc:DocumentCurrencyCode` | Tipicamente `AUD` ou `NZD` |
| `total_amount` | `cbc:PayableAmount` (em `cac:LegalMonetaryTotal`) | Total incl. GST |
| `net_amount` | `cbc:TaxExclusiveAmount` (em `cac:LegalMonetaryTotal`) | Subtotal excl. GST |
| `tax_amount` | `cbc:TaxAmount` (em `cac:TaxTotal`) | Valor do GST |
| `purchase_order` | `cbc:BuyerReference` | Referência da ordem de compra |
| `payment_terms` | `cbc:Note` (em `cac:PaymentTerms`) | Condições de pagamento em texto livre |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nome da empresa fornecedora |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cbc:EndpointID` | ABN (schemeID 0151) |
| `supplier_tax_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | ABN ou número GST |
| `supplier_street` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Rua do fornecedor |
| `supplier_city` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:CityName` | Cidade do fornecedor |
| `supplier_postal_code` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Código postal do fornecedor |
| `supplier_country` | `cac:AccountingSupplierParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Código de país ISO (`AU` ou `NZ`) |
| `buyer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nome da empresa compradora |
| `buyer_id` | `cac:AccountingCustomerParty/cac:Party/cbc:EndpointID` | ABN/NZBN (schemeID 0151) |
| `buyer_street` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:StreetName` | Rua do comprador |
| `buyer_city` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:CityName` | Cidade do comprador |
| `buyer_postal_code` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cbc:PostalZone` | Código postal do comprador |
| `buyer_country` | `cac:AccountingCustomerParty/cac:Party/cac:PostalAddress/cac:Country/cbc:IdentificationCode` | Código de país ISO |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | ID da conta de pagamento |

### Tabela de itens (`INVOICE_TABLE`)

Caminho da linha: `cac:InvoiceLine`

| Coluna | XPath de origem (UBL 2.1) | Notas |
|---|---|---|
| `POSITION` | `cbc:ID` | Número da linha |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Descrição do produto/serviço |
| `QUANTITY` | `cbc:InvoicedQuantity` | Quantidade (código de unidade em `@unitCode`) |
| `UNIT` | `cbc:InvoicedQuantity/@unitCode` | Código de unidade (ex. `C62` = peça, `EA` = cada) |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Preço unitário excl. GST |
| `VAT_RATE` | `cac:Item/cac:ClassifiedTaxCategory/cbc:Percent` | Taxa de GST em % |
| `VAT` | *(calculado a partir do valor do imposto)* | Valor do GST por linha |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Total da linha excl. GST |

## Regra de classificação

O DocBits detecta documentos PINT A-NZ correspondendo ao elemento `CustomizationID`:

```
urn:peppol.org:pint:billing-1@aunz
```

Para documentos de auto-faturação, o padrão é:

```
urn:peppol.org:pint:selfbilling-1@aunz
```

Ambos são classificados sob o tipo de documento eletrônico `PINT A-NZ`.

## Veja também

- [AUNZ PINT](aunz-pint.md) — Visão geral e recursos específicos do A-NZ
- [AUNZ PINT Self-Billing](aunz-pint-self-billing.md) — Variante de auto-faturação
- [Documentos eletrônicos suportados](./)
