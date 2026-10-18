---
description: Unterstützung für das elektronische Dokument TURKEY E-FATURA in DocBits
---

# 🇹🇷 TURKEY E-FATURA

<!-- edocs-country-scope -->

{% hint style="info" %}
Die Länderanleitung enthält Versionsgrenzen, die tatsächlich verwendete Konfiguration und das Erklärvideo zum Land. [Türkei](countries/turkey.md). Prüfen Sie das Profil und die Dokumentstruktur der Quelldatei. Die Familienbezeichnung identifiziert nicht jede UBL-TR-Veröffentlichung und belegt keine Zustellung über die Steuerplattform.
{% endhint %}

| Eigenschaft | Wert |
| ----------- | ---- |
| **Land / Region** | Türkei |
| **Dokumenttypen** | Rechnung, Gutschrift |
| **Format** | UBL-TR 1.2 XML |
| **Standard** | e-Fatura (GİB - Revenue Administration) |

Turkey e-Fatura ist der primäre elektronische Rechnungsstandard, den die GİB (Revenue Administration) für B2B-Transaktionen zwischen registrierten Steuerpflichtigen vorschreibt. Rechnungen werden über registrierte Integratoren und die GİB-Plattform ausgetauscht. Das Format verwendet UBL-TR, die lokalisierte türkische Variante von UBL, mit türkischen Spezialfeldern für die Steueridentifikation über TCKN/VKN.

## Unterstützungsstatus

| Komponente | Status |
| ---------- | ------ |
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Standard-Vorschau

<figure><img src="../../../../../../.gitbook/assets/turkey-e-fatura-preview.png" alt="Turkey E-Fatura Rechnungsvorschau in DocBits"><figcaption><p>Standard-Vorschau in DocBits für eine Turkey-E-Fatura-Rechnung</p></figcaption></figure>

## Verwandte Themen

* [Unterstützte elektronische Dokumente](./)
* [TURKEY E-ARSIV](turkey-e-arsiv.md)
