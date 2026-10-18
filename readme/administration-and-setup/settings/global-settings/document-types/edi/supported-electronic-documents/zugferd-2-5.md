---
description: Unterstützung für das elektronische Dokument ZUGFERD 2.5 in DocBits
---

# 🇩🇪 ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Die Länderanleitung enthält Versionsgrenzen, die tatsächlich verwendete Konfiguration und das Erklärvideo zum Land. [Deutschland](countries/germany.md). Syntax, Veröffentlichungsversion und Profil sind unterschiedliche Auswahlmerkmale. Leiten Sie aus der gemeinsamen Kennung 1p0 keine Factur-X-Veröffentlichung ab.
{% endhint %}

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Germany |
| **Dokumenttypen** | Invoice, Credit Note |
| **Format** | CII (PDF/A-3 eingebettet) oder UBL XML |
| **Standard** | ZUGFeRD 2.5 |
| **Basiert auf** | EN 16931 |

ZUGFeRD 2.5 (die gemeinsame Veröffentlichung von FeRD und FNFE-MPE vom Juni 2026) entspricht Factur-X 1.09. Das zugehörige CII-XML basiert auf UN/CEFACT D22B, das abwärtskompatibel zu D16B ist, sodass der vollständige Extraktions- und Transformationsvertrag von ZUGFeRD 2.4 weiterhin gilt. Das Profil EXTENDED ergänzt neue Felder für Zahlungsmittel und BIC, einen Drittzahlungsempfänger (Factor) sowie den Grund für die Steuerbefreiung bei Zu- und Abschlägen.

Alle fünf Profile werden unterstützt: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) und EXTENDED. DocBits klassifiziert die CII- und UBL-Varianten getrennt.

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Supported |
| Feldextraktion | ✅ Supported |
| Transformation | ✅ Supported |

## Verwandte Seiten

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [ZUGFeRD-Konfiguration](../zugferd/configuration.md)
- [ZUGFeRD-Feldzuordnung](../zugferd/README.md)
- [Unterstützte elektronische Dokumente](./)
