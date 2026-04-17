---
description: Suporte a documentos eletrônicos DIAN da Colômbia no DocBits (Factura Electrónica, Documento Soporte)
---

# 🇨🇴 Colômbia DIAN

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Colombia |
| **Tipos de documento** | Fatura (Factura Electrónica), Nota de Crédito (Nota de Crédito), Documento Soporte |
| **Formato** | XML (UBL 2.1) |
| **Padrão** | DIAN 2.1 (Dirección de Impuestos y Aduanas Nacionales) |
| **Localidade** | `es_CO` |

O padrão colombiano de faturamento eletrônico é regulamentado pela **DIAN** (Dirección de Impuestos y Aduanas Nacionales). É baseado em UBL 2.1 com extensões específicas da DIAN (`sts:DianExtensions`). O DocBits detecta documentos Colombia DIAN por meio do namespace DIAN e roteia pelo `CustomizationID`:

| CustomizationID | Tipo de documento |
|-----------------|--------------|
| 10 | Factura Electrónica de Venta (FACTURA ELECTRONICA) |
| 20 | Nota de Crédito (Nota de Crédito) |
| 91 | Nota de Crédito por devolución |
| 92 | Nota de Débito |
| DS | Documento Soporte (DOCUMENTO SOPORTE) |

O identificador DIAN (**NIT** — Número de Identificación Tributaria) usa `schemeID="31"` no elemento UBL `CompanyID`.

## Status de suporte

| Componente | Status |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="colombia-dian-preview.png" alt="Pré-visualização da Colombia DIAN Factura Electrónica no DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma COLOMBIA FACTURA ELECTRONICA (CustomizationID 10)</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML de origem | Observações |
|---|---|---|
| `invoice_id` | `cbc:ID` | Número da fatura com prefixo (ex.: `SETP990000001`) |
| `invoice_date` | `cbc:IssueDate` | Data de emissão (ISO 8601) |
| `due_date` | `cbc:DueDate` | Data de vencimento do pagamento |
| `currency` | `cbc:DocumentCurrencyCode` | Sempre `COP` (Peso colombiano) |
| `total_amount` | `cac:LegalMonetaryTotal/cbc:PayableAmount` | Total a pagar incl. IVA |
| `net_amount` | `cac:LegalMonetaryTotal/cbc:TaxExclusiveAmount` | Valor líquido excl. IVA |
| `tax_amount` | `cac:TaxTotal/cbc:TaxAmount` | Total do IVA (alíquota padrão 19%) |
| `supplier_name` | `cac:AccountingSupplierParty//cbc:RegistrationName` | Nome legal do fornecedor |
| `supplier_id` | `cac:AccountingSupplierParty//cbc:CompanyID` | NIT do fornecedor (schemeID=31) |
| `buyer_name` | `cac:AccountingCustomerParty//cbc:RegistrationName` | Nome legal do comprador |
| `buyer_id` | `cac:AccountingCustomerParty//cbc:CompanyID` | NIT do comprador (schemeID=31) |

### Tabela de itens de linha (`INVOICE_TABLE`)

Caminho de linha: `cac:InvoiceLine` (ou `cac:CreditNoteLine`)

| Coluna | Elemento XML de origem | Observações |
|---|---|---|
| `POSITION` | `cbc:ID` | Número de linha |
| `DESCRIPTION` | `cac:Item/cbc:Description` | Descrição do produto ou serviço |
| `QUANTITY` | `cbc:InvoicedQuantity` | Quantidade com atributo de código de unidade |
| `UNIT_PRICE` | `cac:Price/cbc:PriceAmount` | Preço unitário excl. IVA |
| `NET_AMOUNT` | `cbc:LineExtensionAmount` | Total de linha excl. IVA |

## Regras de classificação

O DocBits detecta documentos Colombia DIAN pela string de namespace DIAN:

| Tipo de documento eletrônico | Padrão |
|--------------------------|---------|
| COLOMBIA FACTURA ELECTRONICA | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `DianExtensions` |
| COLOMBIA DOCUMENTO SOPORTE | `http://www.dian.gov.co/contratos/facturaelectronica/v1/Structures` + `CustomizationID=DS` |

O elemento raiz é `<Invoice>` (UBL 2.1) para faturas, `<CreditNote>` para notas de crédito. Todos os documentos incluem um bloco `<sts:DianExtensions>` com dados de autorização DIAN (`InvoiceAuthorization`, UUID `CUFE`/`CUDE`, código QR).

## Relacionado

- [Padrões de fatura eletrônica atualmente suportados](../../currently-supported-e-invoice-standards/)
- [Documentos eletrônicos suportados](./)
