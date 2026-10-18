---
description: "Uruguay CFE has generic, 24 and 25 entries. E-Factura and E-Nota Credito are also listed."
---

# Uruguay

Use this guide to identify the configured family and version scope before testing a source file.

[All countries and support scope](../README.md)

## Variants and version limits

Uruguay CFE has generic, 24 and 25 entries. E-Factura and E-Nota Credito are also listed.

**Syntax:** XML

Credit-note entries lack dedicated extraction bundles in the inspected status. Confirm the CFE version and the effective invoice or credit-note mapping.

The tables record a development-catalogue check on 17 October 2026 and the corresponding processing code. They describe available rules and configuration components, not a certification of every file, legal requirement or production rollout. Your organization can override the defaults.

## Inspected rule and component matrix

| Exact format label | Rule document key | Available components |
| --- | --- | --- |
| `URUGUAY E-FACTURA` | `CREDIT_NOTE` | C / — / — / — |
| `URUGUAY E-NOTA CREDITO` | `CREDIT_NOTE` | C / — / — / — |
| `URUGUAY CFE` | `INVOICE` | C / T / P / E |
| `URUGUAY CFE 24` | `INVOICE` | C / T / P / E |
| `URUGUAY CFE 25` | `INVOICE` | C / T / P / E |
| `URUGUAY E-FACTURA` | `INVOICE` | C / T / P / E |

C = classification, T = Transformation, P = Preview, E = Extraction Paths. The document key is the rule/configuration lookup key; it does not guarantee the final stored invoice_type. A transformation can classify a credit note through an INVOICE mapping.

A dash means the status check did not report a dedicated component for this exact format/document key. It does not rule out a shared or fallback mapping. Verify the effective resolver and a representative file before relying on that path.

## Find the mapping in DocBits

<figure><img src="../../../../../../../.gitbook/assets/edocs-support-uruguay-en.png" alt="Uruguay: URUGUAY CFE 25"><figcaption><p>Real development UI: the representative format and its available configuration components. Other versions are listed in the matrix.</p></figcaption></figure>

## Country explainer

Localized narration and WebVTT captions explain format selection, configuration and acceptance checks.

This read-only walkthrough shows the country’s existing DocBits configuration. Check the effective source and active version, then validate representative invoices, credit notes and exports in your own organisation.

{% file src="../../../../../../../.gitbook/assets/edocs-support-uruguay-en-v2.mp4" %}
Uruguay — Country explainer
{% endfile %}

{% file src="../../../../../../../.gitbook/assets/edocs-support-uruguay-en-v2.vtt" %}
WebVTT
{% endfile %}

## Acceptance checks

A component check confirms configuration presence. It is not an end-to-end processing test for every version. Test the exact payload and the invoice or credit-note path required by your integration.

## Check a format in your organization

1. Keep the original XML or the PDF with its embedded XML. Read the namespace, schema or customization identifier and the declared version/profile.

2. Open Settings → Document Types → E-Doc for the applicable business document. Search for the exact electronic-document format shown in the guide.

3. Check the effective Default or Custom source and its active configuration version. Inspect Transformation, Preview and Extraction Paths. Saving a draft does not activate it.

4. Test representative source files for each syntax, version and business document you need. Verify key fields, amounts, tax, invoice/credit-note classification and the ERP export.

5. Confirm validation policy and transport separately. Preserve custom mappings and check approvals and export history before restarting existing documents.

## Related format reference

- [🇺🇾 URUGUAY CFE](../uruguay-cfe.md)
- [🇺🇾 URUGUAY CFE 24](../uruguay-cfe-24.md)
- [🇺🇾 URUGUAY CFE 25](../uruguay-cfe-25.md)
- [🇺🇾 URUGUAY E-FACTURA](../uruguay-e-factura.md)
- [🇺🇾 URUGUAY E-NOTA CREDITO](../uruguay-e-nota-credito.md)
