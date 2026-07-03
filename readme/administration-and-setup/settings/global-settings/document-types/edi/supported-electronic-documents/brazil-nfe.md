---
description: BRAZIL NF-E electronic document support in DocBits
---

# 🇧🇷 BRAZIL NF-E

| Property             | Value                                                           |
| -------------------- | --------------------------------------------------------------- |
| **Country / Region** | Brazil                                                          |
| **Document Types**   | Invoice (Nota Fiscal Eletrônica)                                |
| **Format**           | XML                                                             |
| **Standard**         | NF-e 4.0 (Nota Fiscal Eletrônica — goods & interstate commerce) |
| **Locale**           | `pt_BR`                                                         |

NF-e (Nota Fiscal Eletrônica, `<mod>55</mod>`) is the Brazilian electronic invoice for goods and interstate commerce, regulated by SEFAZ. Each NF-e contains a unique 44-digit access key (`chNFe`), detailed product line items, and multi-tier tax data (ICMS, IPI, PIS, COFINS). DocBits classifies NF-e by detecting the `http://www.portalfiscal.inf.br/nfe` namespace.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/brazil-nfe-preview.png" alt="Brazil NF-e preview in DocBits"><figcaption><p>Default DocBits preview for a BRAZIL NF-E document</p></figcaption></figure>

## Field Mapping

### Header Fields

| DocBits Field   | Source XPath                                               | Notes                               |
| --------------- | ---------------------------------------------------------- | ----------------------------------- |
| `invoice_id`    | `//*[local-name()='ide']/*[local-name()='nNF']`            | Nota Fiscal number                  |
| `invoice_date`  | `//*[local-name()='ide']/*[local-name()='dhEmi']`          | ISO 8601 with BRT offset            |
| `currency`      | Fixed: `BRL`                                               | Always Brazilian Real               |
| `total_amount`  | `//*[local-name()='ICMSTot']/*[local-name()='vNF']`        | Total NF-e value                    |
| `net_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vProd']`      | Total products value                |
| `tax_amount`    | `//*[local-name()='ICMSTot']/*[local-name()='vICMS']`      | ICMS tax total                      |
| `supplier_name` | `//*[local-name()='emit']/*[local-name()='xNome']`         | Emitter company name                |
| `supplier_id`   | `//*[local-name()='emit']/*[local-name()='CNPJ']` or `CPF` | CNPJ (14 digits) or CPF (11 digits) |
| `buyer_name`    | `//*[local-name()='dest']/*[local-name()='xNome']`         | Recipient company name              |
| `buyer_id`      | `//*[local-name()='dest']/*[local-name()='CNPJ']` or `CPF` | CNPJ or CPF                         |

### Line Item Table (`INVOICE_TABLE`)

Row path: `//*[local-name()='det']`

| Column          | Relative XPath                                                                  | Notes                      |
| --------------- | ------------------------------------------------------------------------------- | -------------------------- |
| `POSITION`      | `@nItem`                                                                        | Item sequence number       |
| `ITEM_CODE`     | `*[local-name()='prod']/*[local-name()='cProd']`                                | Product code               |
| `DESCRIPTION`   | `*[local-name()='prod']/*[local-name()='xProd']`                                | Product description        |
| `NCM_CODE`      | `*[local-name()='prod']/*[local-name()='NCM']`                                  | NCM customs classification |
| `CFOP_CODE`     | `*[local-name()='prod']/*[local-name()='CFOP']`                                 | Operation fiscal code      |
| `UNIT`          | `*[local-name()='prod']/*[local-name()='uCom']`                                 | Unit of measure            |
| `QUANTITY`      | `*[local-name()='prod']/*[local-name()='qCom']`                                 | Commercial quantity        |
| `UNIT_PRICE`    | `*[local-name()='prod']/*[local-name()='vUnCom']`                               | Unit price                 |
| `TOTAL_AMOUNT`  | `*[local-name()='prod']/*[local-name()='vProd']`                                | Line total                 |
| `ICMS_AMOUNT`   | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='vICMS']`     | ICMS tax per line          |
| `PIS_AMOUNT`    | `*[local-name()='imposto']/*[local-name()='PIS']//*[local-name()='vPIS']`       | PIS tax per line           |
| `COFINS_AMOUNT` | `*[local-name()='imposto']/*[local-name()='COFINS']//*[local-name()='vCOFINS']` | COFINS tax per line        |
| `VAT_RATE`      | `*[local-name()='imposto']/*[local-name()='ICMS']//*[local-name()='pICMS']`     | ICMS rate (%)              |

## Classification Rule

DocBits detects BRAZIL NF-E documents by checking for the string:

```
http://www.portalfiscal.inf.br/nfe
```

in the XML namespace (`mod=55` for NF-e, `mod=65` for NFC-e are distinguished separately).

## Related

* [BRAZIL NFC-E](brazil-nfce.md)
* [BRAZIL CT-E](brazil-cte.md)
* [BRAZIL NFS-E](brazil-nfse.md)
* [Supported Electronic Documents](./)
