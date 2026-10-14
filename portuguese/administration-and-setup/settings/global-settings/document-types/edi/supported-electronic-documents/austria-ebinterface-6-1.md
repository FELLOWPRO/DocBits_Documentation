---
description: Suporte para documento eletrônico AUSTRIA EBINTERFACE 6.1 no DocBits
---

# 🇦🇹 AUSTRIA EBINTERFACE 6.1

| Propriedade | Valor |
|----------|-------|
| **País/Região** | Áustria |
| **Tipos de documento** | Fatura, Nota de crédito |
| **Formato** | XML |
| **Padrão** | ebInterface 6.1 |
| **Locale** | `de_AT` |

O ebInterface 6.1 é a versão mais recente do padrão austríaco de faturação eletrônica. Inclui regras de validação atualizadas, suporte aprimorado para notas de crédito e compatibilidade expandida com a rede Peppol para faturação transfronteiriça. O namespace é `http://www.ebinterface.at/schema/6p1/`.

## Estado do suporte

| Componente | Estado |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="austria-ebinterface-preview.png" alt="Pré-visualização da fatura Austria ebInterface 6.1 no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura AUSTRIA EBINTERFACE 6.1</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML de origem | Notas |
|---|---|---|
| `invoice_id` | `eb:InvoiceNumber` | Número da fatura |
| `invoice_date` | `eb:InvoiceDate` | Data ISO 8601 |
| `due_date` | `eb:PaymentConditions/eb:DueDate` | Data de vencimento |
| `delivery_date` | `eb:Delivery/eb:Date` | Data de entrega |
| `currency` | `@eb:InvoiceCurrency` | Atributo raiz, sempre `EUR` para AT |
| `total_amount` | `eb:TotalGrossAmount` | Total bruto incl. IVA |
| `net_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:TaxedAmount` | Base tributável líquida |
| `tax_amount` | `eb:Tax/eb:VAT/eb:VATItem/eb:Amount` | Valor do IVA |
| `purchase_order` | `eb:OrderReference/eb:OrderID` | Referência da ordem de compra |
| `payment_terms` | `eb:PaymentConditions/eb:Comment` | Condições de pagamento em texto livre |
| `supplier_name` | `eb:Biller/eb:Address/eb:Name` | Nome da empresa do emitente |
| `supplier_tax_id` | `eb:Biller/eb:VATIdentificationNumber` | UID austríaco (ex. ATU12345678) |
| `supplier_street` | `eb:Biller/eb:Address/eb:Street` | Rua do emitente |
| `supplier_city` | `eb:Biller/eb:Address/eb:Town` | Cidade do emitente |
| `supplier_postal_code` | `eb:Biller/eb:Address/eb:ZIP` | Código postal do emitente |
| `supplier_country` | `eb:Biller/eb:Address/eb:Country/@eb:CountryCode` | Código do país ISO |
| `supplier_email` | `eb:Biller/eb:Address/eb:Email` | E-mail do emitente |
| `supplier_iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN do emitente |
| `customer_name` | `eb:InvoiceRecipient/eb:Address/eb:Name` | Nome da empresa do destinatário |
| `customer_tax_id` | `eb:InvoiceRecipient/eb:VATIdentificationNumber` | UID do destinatário |
| `customer_street` | `eb:InvoiceRecipient/eb:Address/eb:Street` | Rua do destinatário |
| `customer_city` | `eb:InvoiceRecipient/eb:Address/eb:Town` | Cidade do destinatário |
| `customer_postal_code` | `eb:InvoiceRecipient/eb:Address/eb:ZIP` | Código postal do destinatário |
| `customer_country` | `eb:InvoiceRecipient/eb:Address/eb:Country/@eb:CountryCode` | Código do país ISO |
| `iban` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:IBAN` | IBAN de pagamento |
| `bic` | `eb:PaymentMethod/eb:UniversalBankTransaction/eb:BeneficiaryAccount/eb:BIC` | BIC/SWIFT de pagamento |

### Tabela de itens (`INVOICE_TABLE`)

Caminho das linhas: `eb:Details/eb:ItemList/eb:ListLineItem`

| Coluna | Elemento XML de origem | Notas |
|---|---|---|
| `POSITION` | Índice sequencial | Número da linha a partir de 1 |
| `DESCRIPTION` | `eb:Description` | Descrição do produto/serviço |
| `QUANTITY` | `eb:Quantity` | Quantidade numérica |
| `UNIT` | `eb:Quantity/@eb:Unit` | Código da unidade (ex. `STK` = peça) |
| `UNIT_PRICE` | `eb:UnitPrice` | Preço unitário sem IVA |
| `VAT_RATE` | `eb:VAT/eb:VATItem/eb:VATRate` | Taxa de IVA em % |
| `VAT` | `eb:VAT/eb:VATItem/eb:TaxedAmount` | Valor do IVA por linha |
| `NET_AMOUNT` | `eb:LineItemAmount` | Total da linha sem IVA |

## Regra de classificação

O DocBits detecta documentos AUSTRIA EBINTERFACE 6.1 através da string de namespace:

```
http://www.ebinterface.at/schema/6p1/
```

## Relacionados

- [Documentos eletrônicos suportados](./)
- [Austria ebInterface](austria-ebinterface.md)
- [Austria ebInterface 6.0](austria-ebinterface-6-0.md)