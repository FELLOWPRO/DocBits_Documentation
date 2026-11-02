---
description: Suporte a documentos eletrônicos Denmark OIOUBL 2.1 no DocBits
---

# 🇩🇰 DENMARK OIOUBL

<!-- edocs-country-scope -->

{% hint style="info" %}
Consulte o guia do país para conhecer os limites das versões, a configuração efetiva e o vídeo explicativo. [Dinamarca](countries/denmark.md). OIOUBL e Peppol BIS são perfis distintos. A sintaxe UBL, por si só, não identifica o perfil nacional.
{% endhint %}

| Propriedade | Valor |
| --- | --- |
| **País / Região** | Dinamarca |
| **Tipos de documento** | Fatura (Faktura), nota de crédito |
| **Formato** | XML (UBL 2.1) |
| **Padrão** | OIOUBL 2.1 (Offentlig Information Online UBL) |
| **Idioma** | `da_DK` |

O OIOUBL (Offentlig Information Online UBL) é o padrão dinamarquês de fatura eletrônica, baseado no UBL 2.1. É obrigatório para faturas destinadas a entidades do setor público dinamarquês e amplamente utilizado em transações B2B. O DocBits detecta documentos OIOUBL 2.1 pela presença de `<cbc:CustomizationID>OIOUBL-2.1</cbc:CustomizationID>`. O identificador de perfil `urn:www.nesubl.eu:profiles:profile5:ver2.0` indica o perfil de fatura NES (Northern European Subset).

## Status de suporte

| Componente | Status |
| --- | --- |
| Visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Visualização padrão

<figure><img src="../../../../../../.gitbook/assets/denmark-oioubl-preview.png" alt="Visualização de fatura Denmark OIOUBL 2.1 no DocBits"><figcaption><p>Visualização padrão do DocBits para uma fatura Denmark OIOUBL 2.1 (Faktura)</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML de origem | Observações |
| --- | --- | --- |
| `invoice_id` | `cbc:ID` | Número da fatura |
| `invoice_date` | `cbc:IssueDate` | Data de emissão ISO 8601 |
| `due_date` | `cbc:DueDate` | Data de vencimento do pagamento |
| `invoice_type` | `cbc:InvoiceTypeCode` | Código UNCL 1001 (380=Fatura, 381=Nota de crédito) |
| `currency` | `cbc:DocumentCurrencyCode` | Sempre `DKK` (coroa dinamarquesa) |
| `purchase_order` | `cac:OrderReference/cbc:ID` | Número de referência do pedido do comprador |
| `buyer_reference` | `cbc:BuyerReference` | Referência interna do comprador / número de localização EAN |
| `note` | `cbc:Note` | Instruções de pagamento ou observações em texto livre |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Valor líquido sem IVA |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Valor total do IVA (alíquota padrão de 25%) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Valor total com IVA |
| `tax_rate` | `cac:TaxTotal/cac:TaxSubtotal/cac:TaxCategory/cbc:Percent` | Alíquota de IVA em % |
| `supplier_name` | `cac:AccountingSupplierParty/cac:Party/cac:PartyName/cbc:Name` | Nome da empresa fornecedora |
| `supplier_id` | `cac:AccountingSupplierParty/cac:Party/cac:PartyIdentification/cbc:ID` | Número CVR (por exemplo, `DK12345678`) |
| `supplier_vat` | `cac:AccountingSupplierParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Número de IVA/CVR |
| `supplier_address` | `cac:AccountingSupplierParty/.../cbc:StreetName` | Endereço (rua) do fornecedor |
| `supplier_city` | `cac:AccountingSupplierParty/.../cbc:CityName` | Cidade do fornecedor |
| `supplier_postal_code` | `cac:AccountingSupplierParty/.../cbc:PostalZone` | Código postal do fornecedor |
| `supplier_country` | `cac:AccountingSupplierParty/.../cbc:IdentificationCode` | Código de país ISO (`DK`) |
| `customer_name` | `cac:AccountingCustomerParty/cac:Party/cac:PartyName/cbc:Name` | Nome da empresa cliente |
| `customer_id` | `cac:AccountingCustomerParty/cac:Party/cac:PartyIdentification/cbc:ID` | Número CVR |
| `customer_vat` | `cac:AccountingCustomerParty/cac:Party/cac:PartyTaxScheme/cbc:CompanyID` | Número de IVA/CVR |
| `customer_address` | `cac:AccountingCustomerParty/.../cbc:StreetName` | Endereço (rua) do cliente |
| `customer_city` | `cac:AccountingCustomerParty/.../cbc:CityName` | Cidade do cliente |
| `customer_postal_code` | `cac:AccountingCustomerParty/.../cbc:PostalZone` | Código postal do cliente |
| `customer_country` | `cac:AccountingCustomerParty/.../cbc:IdentificationCode` | Código de país ISO (`DK`) |
| `iban` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cbc:ID` | Conta bancária / IBAN |
| `bic` | `cac:PaymentMeans/cac:PayeeFinancialAccount/cac:FinancialInstitutionBranch/cbc:ID` | Código BIC/SWIFT |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `cac:InvoiceLine`

| Coluna | Elemento XML de origem | Observações |
| --- | --- | --- |
| `POSITION` | `cbc:ID` | Número de sequência da linha |
| `DESCRIPTION` | `cac:Item/cbc:Name` | Nome / descrição do item |
| `QUANTITY` | `cbc:InvoicedQuantity` | Quantidade faturada |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Preço unitário sem IVA |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Total da linha sem IVA |

## Regra de classificação

O DocBits detecta documentos OIOUBL 2.1 por meio da correspondência com o elemento `CustomizationID`:

| Tipo de documento eletrônico | Padrão |
| --- | --- |
| OIOUBL 2.1 | `<cbc:CustomizationID>OIOUBL-2\.1\s*</cbc:CustomizationID>` |

O elemento raiz é `<Invoice>` (ou `<CreditNote>`) no namespace UBL 2.1 `urn:oasis:names:specification:ubl:schema:xsd:Invoice-2`.

## Relacionado

* [Padrões de Fatura Eletrônica Atualmente Suportados](../currently-supported-e-invoice-standards/README.md)
* [Documentos Eletrônicos Suportados](./)
