---
description: INVOIC02 electronic document support in DocBits
---

# INVOIC02

<!-- edocs-country-scope -->

{% hint style="info" %}
Check the country guide for version limits, effective configuration and the country explainer. [International](countries/international.md). Invoice, order, response and despatch mappings are distinct. File processing does not itself provide a Peppol access point or trading-partner connectivity.
{% endhint %}

| Property             | Value                   |
| -------------------- | ----------------------- |
| **Country / Region** | International           |
| **Document Types**   | Invoice                 |
| **Format**           | EDIFACT                 |
| **Standard**         | UN/EDIFACT INVOIC D.02B |

INVOIC02 is a UN/EDIFACT invoice message based on the D.02B directory version. EDIFACT (Electronic Data Interchange for Administration, Commerce and Transport) is a widely used EDI standard in logistics, retail, and manufacturing. DocBits parses the EDIFACT segment structure and extracts header, line item, and summary fields.

## Support Status

| Component        | Status      |
| ---------------- | ----------- |
| Preview          | ✅ Supported |
| Field Extraction | ✅ Supported |
| Transformation   | ✅ Supported |

## Default Preview

<figure><img src="../../../../../../.gitbook/assets/invoic02-preview.png" alt="INVOIC02 invoice preview in DocBits"><figcaption><p>Default DocBits preview for an INVOIC02 invoice</p></figcaption></figure>

## Related

* [Supported Electronic Documents](./)
