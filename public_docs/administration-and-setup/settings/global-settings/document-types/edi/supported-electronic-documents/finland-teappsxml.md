---
description: Suporte para documentos TEAPPSXML finlandeses no DocBits
---

# 🇫🇮 Finland TEAPPSXML

| Propriedade | Valor |
|----------|-------|
| **País / Região** | Finlândia |
| **Tipos de documento** | Fatura, Nota de crédito |
| **Formato** | XML |
| **Padrão** | TEAPPSXML 3.0 (Tieto / Finnish Banking) |
| **Locale** | `fi_FI` |

TEAPPSXML (Tietotekniikan ja viestinnän toimiala) é um padrão de fatura eletrónica finlandês utilizado principalmente no setor bancário e financeiro. O elemento raiz é `<TEAPPSXML>` com o namespace `urn:TEAPPSXML:3.0`. O DocBits deteta documentos TEAPPSXML pela presença de `xmlns="urn:TEAPPSXML:` no elemento raiz.

O formato TEAPPSXML utiliza nomes de elementos em maiúsculas e uma estrutura plana com secções separadas `<SENDER>`, `<RECEIVER>`, `<INVOICE>` e `<PAYMENTINFO>`. O formato do ID de empresa finlandês (Y-tunnus) é `1234567-8`, e os números de IVA utilizam o prefixo `FI` (ex. `FI12345678`).

## Status de suporte

| Componente | Status |
|-----------|--------|
| Pré-visualização | ✅ Suportado |
| Extração de campos | ✅ Suportado |
| Transformação | ✅ Suportado |

## Pré-visualização padrão

<figure><img src="finland-teappsxml-preview.png" alt="Finland TEAPPSXML invoice preview in DocBits"><figcaption><p>Pré-visualização padrão do DocBits para uma fatura Finland TEAPPSXML</p></figcaption></figure>

## Mapeamento de campos

### Campos de cabeçalho

| Campo DocBits | Elemento XML fonte | Notas |
|---|---|---|
| `invoice_id` | `INVOICE/INVOICENUMBER` | Número da fatura |
| `invoice_date` | `INVOICE/INVOICEDATE` | Data de emissão (AAAA-MM-DD) |
| `due_date` | `INVOICE/DUEDATE` | Data de vencimento (AAAA-MM-DD) |
| `invoice_type` | `INVOICE/INVOICE_TYPE` | Tipo de mensagem (INVOICE) |
| `currency` | `INVOICE/CURRENCY` | Código de moeda (tipicamente `EUR`) |
| `purchase_order` | `INVOICE/REFERENCENUMBER` | Número de referência de pagamento |
| `payment_reference` | `INVOICE/REFERENCENUMBER` | Referência de pagamento finlandesa (viitenumero) |
| `net_amount` | `INVOICE/TOTALVATEXCLUDED` | Valor líquido excl. IVA |
| `tax_amount` | `INVOICE/TOTALVAT` | Valor total do IVA |
| `total_amount` | `INVOICE/TOTALAMOUNT` | Valor total incl. IVA |
| `payment_terms` | `INVOICE/PAYMENT_TERMS` | Método de pagamento (ex. `BANKTRANSFER`) |
| `supplier_name` | `SENDER/NAME` | Nome da empresa remetente |
| `supplier_id` | `SENDER/ID` | ID de empresa finlandês (Y-tunnus, ex. `1234567-8`) |
| `supplier_tax_id` | `SENDER/VATNUMBER` | Número de IVA (ex. `FI12345678`) |
| `supplier_address` | `SENDER/ADDRESS/STREET` | Morada do remetente |
| `supplier_city` | `SENDER/ADDRESS/CITY` | Cidade do remetente |
| `supplier_postal_code` | `SENDER/ADDRESS/POSTCODE` | Código postal do remetente |
| `supplier_country` | `SENDER/ADDRESS/COUNTRY` | Código de país ISO (`FI`) |
| `supplier_bic` | `SENDER/BANK/BIC` | Código BIC do banco remetente |
| `buyer_name` | `INVOICE/BUYER/NAME` | Nome da empresa compradora |
| `buyer_id` | `INVOICE/BUYER/ID` | ID de empresa finlandês do comprador |
| `buyer_address` | `INVOICE/BUYER/ADDRESS_LINE_1` | Morada do comprador |
| `buyer_city` | `INVOICE/BUYER/CITY` | Cidade do comprador |
| `buyer_postal_code` | `INVOICE/BUYER/POSTAL_CODE` | Código postal do comprador |
| `buyer_country` | `INVOICE/BUYER/COUNTRY` | Código de país ISO (`FI`) |
| `iban` | `PAYMENTINFO/BENEFICIARYACCOUNT/IBAN` | IBAN do beneficiário |
| `bic` | `PAYMENTINFO/BENEFICIARYACCOUNT/BIC` | Código BIC do beneficiário |

### Tabela de itens (`INVOICE_TABLE`)

Caminho de linha: `INVOICE/LINES/LINE`

| Coluna | Elemento XML fonte | Notas |
|---|---|---|
| `POSITION` | `LINENUMBER` | Número de sequência da linha |
| `DESCRIPTION` | `ARTICLENAME` | Nome / descrição do artigo |
| `QUANTITY` | `QUANTITY` | Quantidade faturada |
| `UNIT` | `UNIT` | Unidade de medida (ex. `KPL` = peça) |
| `UNIT_PRICE` | `UNITPRICE` | Preço unitário excl. IVA |
| `VAT_RATE` | `VATRATE` | Taxa de IVA em % (padrão 25,5%) |
| `VAT` | Calculado | Valor do IVA por linha |
| `NET_AMOUNT` | `LINEAMOUNT` | Total da linha excl. IVA |

## Regra de classificação

O DocBits deteta documentos TEAPPSXML correspondendo ao atributo `xmlns` no elemento raiz `<TEAPPSXML>`:

| Tipo de documento eletrónico | Padrão |
|--------------------------|---------|
| TEAPPSXML | `xmlns` contém `urn:TEAPPSXML:` |

## Relacionados

- [Padrões de fatura eletrónica atualmente suportados](../../currently-supported-e-invoice-standards/)
- [Finland Finvoice](./finland-finvoice.md)
- [Documentos eletrónicos suportados](./)
