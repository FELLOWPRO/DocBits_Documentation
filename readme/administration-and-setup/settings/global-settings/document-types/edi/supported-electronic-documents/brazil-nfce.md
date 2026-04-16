---
description: BRAZIL NFC-E electronic document support in DocBits
---

# 🇧🇷 BRAZIL NFC-E

| Property | Value |
|----------|-------|
| **Country / Region** | Brazil |
| **Document Types** | Consumer Invoice (Nota Fiscal de Consumidor Eletrônica) |
| **Format** | XML |
| **Standard** | NFC-e 4.0 (retail / point-of-sale consumer invoice) |
| **Locale** | `pt_BR` |

NFC-e (Nota Fiscal de Consumidor Eletrônica, `<mod>65</mod>`) is the Brazilian electronic invoice for retail sales to end consumers. It shares the NF-e XML schema (`nfeProc` namespace) but uses model code 65. NFC-e documents typically carry a CPF (individual tax ID) for the buyer instead of a CNPJ, and do not include PIS/COFINS per line for simple retail transactions.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="brazil-nfce-preview.png" alt="Brazil NFC-e preview in DocBits"><figcaption><p>Default DocBits preview for a BRAZIL NFC-E document</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XPath | Notes |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nNF']` | Nota Fiscal number |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 with BRT offset |
| `currency` | Fixed: `BRL` | Always Brazilian Real |
| `total_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vNF']` | Total NFC-e value |
| `net_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vProd']` | Products subtotal |
| `tax_amount` | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']` | ICMS tax total |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Retailer name |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` or `CPF` | CNPJ or CPF |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Consumer name |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CPF']` or `CNPJ` | CPF (individual) or CNPJ |

### Line Item Table (`INVOICE_TABLE`)

Row path: `//*[local-name()='det']`

| Column | Relative XPath | Notes |
|---|---|---|
| `POSITION` | `@nItem` | Item sequence number |
| `ITEM_CODE` | `*[local-name()='prod']/*[local-name()='cProd']` | Product code |
| `DESCRIPTION` | `*[local-name()='prod']/*[local-name()='xProd']` | Product description |
| `NCM_CODE` | `*[local-name()='prod']/*[local-name()='NCM']` | NCM customs classification |
| `CFOP_CODE` | `*[local-name()='prod']/*[local-name()='CFOP']` | Operation fiscal code |
| `UNIT` | `*[local-name()='prod']/*[local-name()='uCom']` | Unit of measure |
| `QUANTITY` | `*[local-name()='prod']/*[local-name()='qCom']` | Commercial quantity |
| `UNIT_PRICE` | `*[local-name()='prod']/*[local-name()='vUnCom']` | Unit price |
| `TOTAL_AMOUNT` | `*[local-name()='prod']/*[local-name()='vProd']` | Line total |
| `ICMS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS tax per line |
| `VAT_RATE` | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']` | ICMS rate (%) |

## Classification Rule

DocBits detects BRAZIL NFC-E documents via the pattern `<mod>65</mod>` within the `http://www.portalfiscal.inf.br/nfe` namespace XML.

## Related

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL CT-E](brazil-cte.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Supported Electronic Documents](./)
