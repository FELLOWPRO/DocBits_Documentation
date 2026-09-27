---
description: FACTURX electronic document support in DocBits
---

# 🇫🇷 FACTURX

| Property             | Value                  |
| -------------------- | ---------------------- |
| **Country / Region** | France / Germany       |
| **Document Types**   | Invoice, Credit Note   |
| **Format**           | CII (PDF/A-3 embedded) |
| **Standard**         | Factur-X               |
| **Based On**         | EN 16931               |

Factur-X is the French implementation of the Franco-German hybrid invoice standard. It embeds structured CII XML data within a PDF/A-3 document, allowing both human-readable and machine-processable invoicing. DocBits auto-detects the Factur-X version and profile from the embedded XML.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/facturx-preview.png" alt="Factur-X invoice preview in DocBits"><figcaption><p>Default DocBits preview for a France Factur-X invoice</p></figcaption></figure>

## Related

* [ZUGFeRD Configuration](../zugferd/)
* [ZUGFeRD Field Mapping](../zugferd/versions/)
* [Supported Electronic Documents](./)
