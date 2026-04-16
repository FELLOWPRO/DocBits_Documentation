---
description: BRAZIL CT-E electronic document support in DocBits
---

# 🇧🇷 BRAZIL CT-E

| Property | Value |
|----------|-------|
| **Country / Region** | Brazil |
| **Document Types** | Transport Invoice (Conhecimento de Transporte Eletrônico) |
| **Format** | XML |
| **Standard** | CT-e 3.0 (electronic freight/transport bill of lading) |
| **Locale** | `pt_BR` |

CT-e (Conhecimento de Transporte Eletrônico, `<mod>57</mod>`) is the Brazilian electronic transport document issued by logistics and freight companies. It documents the transport service, cargo value, origin and destination municipalities (`cMunIni` / `cMunFim`), and the freight price (`vTPrest`). Unlike NF-e, CT-e uses `cteProc` as root element and references linked NF-e documents.

## Support Status

| Component | Status |
|-----------|--------|
| Preview | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation | ✅ Supported |

## Default Preview

<figure><img src="brazil-cte-preview.png" alt="Brazil CT-e preview in DocBits"><figcaption><p>Default DocBits preview for a BRAZIL CT-E document</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field | Source XPath | Notes |
|---|---|---|
| `invoice_id` | `//*[local-name()='ide']/*[local-name()='nCT']` | CT-e number |
| `invoice_date` | `//*[local-name()='ide']/*[local-name()='dhEmi']` | ISO 8601 with BRT offset |
| `currency` | Fixed: `BRL` | Always Brazilian Real |
| `total_amount` | `//*[local-name()='vPrest']/*[local-name()='vTPrest']` | Total freight service value |
| `net_amount` | `//*[local-name()='vPrest']/*[local-name()='vRec']` | Amount to be received |
| `tax_amount` | `//*[local-name()='ICMS']//*[local-name()='vICMS']` | ICMS on transport service |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']` | Carrier (transportadora) name |
| `supplier_id` | `//*[local-name()='emit']/*[local-name()='CNPJ']` | Carrier CNPJ |
| `buyer_name` | `//*[local-name()='dest']/*[local-name()='xNome']` | Consignee (destinatário) name |
| `buyer_id` | `//*[local-name()='dest']/*[local-name()='CNPJ']` | Consignee CNPJ |

> CT-e does not include a line item table — the transport service is a single document-level charge.

## Classification Rule

DocBits detects BRAZIL CT-E documents via:

```
http://www.portalfiscal.inf.br/cte
```

in the XML namespace (root element `<cteProc>`).

## Related

- [BRAZIL NF-E](brazil-nfe.md)
- [BRAZIL NFC-E](brazil-nfce.md)
- [BRAZIL NFS-E](brazil-nfse.md)
- [Supported Electronic Documents](./)
