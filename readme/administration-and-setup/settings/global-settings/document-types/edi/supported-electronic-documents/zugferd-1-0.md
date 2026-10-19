---
description: Unterstützung für das elektronische Dokument ZUGFERD 1.0 in DocBits
---

# 🇩🇪 ZUGFERD 1.0

<!-- edocs-country-scope -->

{% hint style="info" %}
Die Länderanleitung enthält Versionsgrenzen, die tatsächlich verwendete Konfiguration und das Erklärvideo zum Land. [Deutschland](countries/germany.md). Syntax, Veröffentlichungsversion und Profil sind unterschiedliche Auswahlmerkmale. Leiten Sie aus der gemeinsamen Kennung 1p0 keine Factur-X-Veröffentlichung ab.
{% endhint %}

| Eigenschaft | Wert |
|---|---|
| **Land / Region** | Germany |
| **Dokumenttypen** | Invoice, Credit Note |
| **Format** | CII (PDF/A-3 eingebettet) |
| **Standard** | ZUGFeRD 1.0 |
| **Basiert auf** | ZUGFeRD 1.0 Spezifikation |

ZUGFeRD 1.0 war der ursprüngliche deutsche Hybrid-Rechnungsstandard und wurde 2014 veröffentlicht. Er bettet eine CII-XML-Datei (ZUGFeRD-invoice.xml) in ein PDF/A-3-Dokument ein. Diese Version entstand vor der europäischen Norm EN 16931 und verwendet ein eigenes Profilsystem.

## Unterstützungsstatus

| Komponente | Status |
| ---------- | ------ |
| Vorschau | ✅ Supported |
| Feldextraktion | ✅ Supported |
| Transformation | ✅ Supported |

## Standard-Vorschau

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="ZUGFeRD 1.0 Rechnungsvorschau in DocBits"><figcaption><p>Standardvorschau in DocBits für eine ZUGFeRD 1.0-Rechnung aus Deutschland</p></figcaption></figure>

## Verwandte Seiten

* [ZUGFeRD-Konfiguration](../zugferd/)
* [ZUGFeRD-Feldzuordnung](../zugferd/versions/)
* [Unterstützte elektronische Dokumente](./)
