---
description: "Find the configured eDocs family, syntax, version and profile before testing document processing."
---

# eDocs formats, versions and country guides

Start with the source document and the matching country guide. A country name alone does not identify a file format. A version label, XML syntax and a business profile describe different things.

{% hint style="info" %}
The tables record a development-catalogue check on 17 October 2026 and the corresponding processing code. They describe available rules and configuration components, not a certification of every file, legal requirement or production rollout. Your organization can override the defaults.
{% endhint %}

## Read the support matrix correctly

- Family: the electronic-document format, such as XRechnung, Factur-X, KSeF or CFDI.
- Syntax: the actual payload, such as UBL XML, CII XML or a PDF with embedded XML. A PDF scan, JSON export or QR image is not an equivalent XML payload.
- Version: the declared publication or schema release. A generic family label does not establish support for every release.
- Profile: a business or data subset, such as BASIC, EN16931, EXTENDED or self-billing. A profile is not a publication version.
- Rule and components: classification, Transformation, Preview and Extraction Paths are separate. A configured profile does not necessarily have its own classification rule.
- Validation and transmission: rendering or extracting a file does not by itself verify all legal rules, signatures, tax clearance or network delivery.

## Country guides

| Country / region | Families and version scope | Catalogue result |
| --- | --- | --- |
| [Austria](countries/austria.md) | ebInterface 4.3, 5.0, 6.0 and 6.1 have separate entries. | Entries found |
| [Denmark](countries/denmark.md) | OIOUBL 2.1 is the named Danish entry. | Entries found |
| [Finland](countries/finland.md) | Finvoice 1.3, 2.0, 2.01 and 3.0 have separate entries. TEAPPSXML is another family. | Entries found |
| [France](countries/france.md) | Factur-X has generic and release-specific entries, including 1.0.05, 1.08 and 1.09. VRBL FR CIUS 1.0 is separate. | Entries found |
| [Germany](countries/germany.md) | XRechnung has thirteen version labels from 1.0 to 3.0.2, each in CII and UBL. ZUGFeRD includes legacy profiles and 2.5 CII and UBL entries. | Entries found |
| [Italy](countries/italy.md) | FatturaPA is the configured Italian family. | Entries found |
| [Netherlands](countries/netherlands.md) | SI-UBL 2.0 has a dedicated entry. | Entries found |
| [Norway](countries/norway.md) | EHF Invoice 3.0 is listed alongside EHF Order, Order Response and Despatch Advice. | Entries found |
| [Poland](countries/poland.md) | KSeF has generic, FA2 and FA3 entries. | Entries found |
| [Slovenia](countries/slovenia.md) | e-SLOG 1.6 and 2.0 have separate entries. | Entries found |
| [Spain](countries/spain.md) | Facturae has generic, 3.2, 3.2.1 and 3.2.2 entries. | Entries found |
| [Sweden](countries/sweden.md) | Svefaktura 1.0 is the named Swedish entry. | Entries found |
| [Australia](countries/australia.md) | PINT A-NZ has invoice and credit-note rule entries shared with New Zealand. | Entries found |
| [New Zealand](countries/new-zealand.md) | PINT A-NZ has invoice and credit-note rule entries shared with Australia. | Entries found |
| [India](countries/india.md) | India GST E-Invoice and GST CreditNote have separate entries. | Entries found |
| [Indonesia](countries/indonesia.md) | Indonesia E-Faktur is the configured family. | Entries found |
| [China](countries/china.md) | The catalogue includes Fapiao, E-Fapiao, General VAT Invoice and Special VAT Invoice. | Entries found |
| [Japan](countries/japan.md) | JP PINT and JP PINT Self-Billing are separate entries. | Entries found |
| [South Korea](countries/korea.md) | Korea E-Tax Invoice and Korea NTS are configured families. | Entries found |
| [Malaysia](countries/malaysia.md) | MyInvois has invoice and credit-note rule entries. | Entries found |
| [Philippines](countries/philippines.md) | Philippines EIS is the configured family. | Entries found |
| [Singapore](countries/singapore.md) | InvoiceNow has invoice and credit-note entries; InvoiceNow SG is another configured label. | Entries found |
| [Taiwan](countries/taiwan.md) | Taiwan eGUI is the configured family. | Entries found |
| [Thailand](countries/thailand.md) | Thailand E-Tax Invoice is the configured family. | Entries found |
| [Vietnam](countries/vietnam.md) | Vietnam E-Invoice is the configured family. | Entries found |
| [Argentina](countries/argentina.md) | Argentina AFIP and Factura Electronica are configured labels. | Entries found |
| [Brazil](countries/brazil.md) | Brazil has NF-e, NFC-e, CT-e, NFS-e and SPED NFS-e entries. NFS-e includes versions 1.00 and 2.00 to 2.04; SPED includes 1.00.02 and 1.01. | Entries found |
| [Chile](countries/chile.md) | Chile DTE has invoice, credit-note and despatch-guide entries. | Entries found |
| [Colombia](countries/colombia.md) | Colombia Factura Electronica and Documento Soporte have separate entries. | Entries found |
| [Costa Rica](countries/costa-rica.md) | The older documentation names Costa Rica, but no matching classification or configuration entry was found in the inspected development catalogue. | Not confirmed |
| [Ecuador](countries/ecuador.md) | Ecuador SRI has generic, 1.0.0, 1.1.0, 2.0.0 and 2.1.0 entries. Withholding is a separate document type. | Entries found |
| [Mexico](countries/mexico.md) | Mexico CFDI 3.3 and 4.0 have separate entries. | Entries found |
| [Paraguay](countries/paraguay.md) | Paraguay DTE, SIFEN and SIFEN 150 are configured labels. | Entries found |
| [Peru](countries/peru.md) | Peru CPE has generic, UBL 2.0 and UBL 2.1 entries. Factura Electronica is another label. | Entries found |
| [Uruguay](countries/uruguay.md) | Uruguay CFE has generic, 24 and 25 entries. E-Factura and E-Nota Credito are also listed. | Entries found |
| [Kazakhstan](countries/kazakhstan.md) | Kazakhstan ESF is the configured family. | Entries found |
| [Saudi Arabia](countries/saudi-arabia.md) | ZATCA Fatoorah, Reporting, Simplified and Tax Invoice have separate entries. | Entries found |
| [Turkey](countries/turkey.md) | Turkey E-Fatura and E-Arsiv are separate configured families. | Entries found |
| [United Arab Emirates](countries/united-arab-emirates.md) | UAE VAT Invoice is the configured label. | Entries found |
| [International](countries/international.md) | International entries include Peppol BIS 3.0, UBL 2.1, pure CII, EDI, INVOIC02, cXML, OCI, BOD and SPS Commerce RSX 7.7.4. | Entries found |

## Factur-X / ZUGFeRD: do not invent a publication version

A harmonized CII Guideline ID can identify a family and profile while sharing the same 1p0 marker across several releases. Factur-X XMP Version 1.0 is a schema marker, not a publication such as 1.08 or 1.09. ZUGFeRD XMP can declare its version. When authoritative metadata is absent, keep the generic family result and confirm the original file with the sender.

MINIMUM and BASIC WL can omit line-item information needed downstream. BASIC, EN16931/COMFORT and EXTENDED offer different data coverage. A more extensive profile can carry fields that your extraction mapping does not use. Check required fields with actual examples.

## Check a format in your organization

1. Keep the original XML or the PDF with its embedded XML. Read the namespace, schema or customization identifier and the declared version/profile.

2. Open Settings → Document Types → E-Doc for the applicable business document. Search for the exact electronic-document format shown in the guide.

3. Check the effective Default or Custom source and its active configuration version. Inspect Transformation, Preview and Extraction Paths. Saving a draft does not activate it.

4. Test representative source files for each syntax, version and business document you need. Verify key fields, amounts, tax, invoice/credit-note classification and the ERP export.

5. Confirm validation policy and transport separately. Preserve custom mappings and check approvals and export history before restarting existing documents.

[Acceptance checks](../credit-note-recognized-as-invoice.md)

[Configure DocBits with Claude or Codex](../../../../../../advanced-functions-and-tools/docbits-mcp/configuration-with-claude-or-codex.md): connection, copyable prompts, previews, versioned changes, checks and rollback.
