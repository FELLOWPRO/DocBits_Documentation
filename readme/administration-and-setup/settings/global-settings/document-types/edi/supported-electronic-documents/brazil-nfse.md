---
description: BRAZIL NFS-E electronic document support in DocBits
---

# 🇧🇷 BRAZIL NFS-E

| Property | Value |
|----------|-------|
| **Country / Region** | Brazil |
| **Document Types** | Service Invoice (Nota Fiscal de Serviços Eletrônica) |
| **Format** | XML |
| **Standard** | NFS-e 2.04 (ABRASF national standard for municipal service invoices) |
| **Locale** | `pt_BR` |

NFS-e (Nota Fiscal de Serviços Eletrônica) is the Brazilian electronic invoice for services, issued at the municipal level. DocBits supports the ABRASF (Associação Brasileira das Secretarias de Finanças das Capitais) standard schema. NFS-e documents use a different XML structure than NF-e: the main tax is ISS (Imposto Sobre Serviços) rather than ICMS, and supplier/buyer are called `PrestadorServico` / `TomadorServico`. The `Discriminacao` element contains the free-text service description.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="brazil-nfse-preview.png" alt="Brazil NFS-e preview in DocBits"><figcaption><p>Default DocBits preview for a BRAZIL NFS-E document</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XPath | Notes |
|---|---|---|
| `invoice_id` | `//*[local-name()='Numero']` | NFS-e number |
| `invoice_date` | `//*[local-name()='DataEmissao']` | ISO 8601 emission date |
| `currency` | Fixed: `BRL` | Always Brazilian Real |
| `total_amount` | `//*[local-name()='ValorServicos']` | Gross service value |
| `net_amount` | `//*[local-name()='ValorLiquidoNfse']` | Net value after deductions |
| `tax_amount` | `//*[local-name()='ValorIss']` | ISS (municipal service tax) |
| `supplier_name` | `//*[local-name()='PrestadorServico']//*[local-name()='RazaoSocial']` | Service provider name |
| `supplier_id` | `//*[local-name()='PrestadorServico']//*[local-name()='Cnpj']` | Provider CNPJ |
| `buyer_name` | `//*[local-name()='TomadorServico']//*[local-name()='RazaoSocial']` | Service taker name |
| `buyer_id` | `//*[local-name()='TomadorServico']//*[local-name()='Cnpj']` | Taker CNPJ |

> NFS-e describes a single service in the `Discriminacao` element rather than line items. No `INVOICE_TABLE` is extracted.

## Classification Rule

DocBits detects BRAZIL NFS-E documents via the namespace:

```
http://www.abrasf.org.br/nfse.xsd
```

## Related

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL CT-E](brazil-cte.md)
- [Supported Electronic Documents](./)
