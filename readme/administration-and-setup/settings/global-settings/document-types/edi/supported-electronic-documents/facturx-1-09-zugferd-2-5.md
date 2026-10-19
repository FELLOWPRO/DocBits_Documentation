---
description: FACTURX 1.09 - ZUGFERD 2.5 elektronische Dokumentenunterstützung in DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Die Länderanleitung enthält Versionsgrenzen, die tatsächlich verwendete Konfiguration und das Erklärvideo zum Land. [Frankreich](countries/france.md). Die XML-Kennung 1p0 und Factur-X XMP Version 1.0 identifizieren keine Veröffentlichungsversion. Behalten Sie die generische Bezeichnung bei, wenn die Veröffentlichung unbekannt ist.
{% endhint %}

| Eigenschaft | Wert |
|-------------|------|
| **Land / Region** | Frankreich / Deutschland |
| **Dokumenttypen** | Rechnung, Gutschrift |
| **Format** | CII (PDF/A-3 eingebettet) |
| **Standard** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Basiert auf** | EN 16931 |

Factur-X 1.09 ist die französische Veröffentlichung, die ZUGFeRD 2.5 entspricht (gemeinsame Veröffentlichung von FeRD/FNFE-MPE, Juni 2026). Das zugehörige CII-XML verwendet die UN/CEFACT-D22B-Basis, die abwärtskompatibel zu D16B ist, sodass der vollständige Extraktions- und Transformationsvertrag von Factur-X 1.08 / ZUGFeRD 2.4 weiterhin gilt. Das Profil EXTENDED ergänzt neue Felder für Zahlungsmittel und BIC, einen Drittzahlungsempfänger (Factor) und den Grund für die Steuerbefreiung bei Nachlässen/Zuschlägen.

Alle fünf Profile werden unterstützt: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) und EXTENDED.

## Unterstützungsstatus

| Komponente | Status |
|------------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Verwandte Themen

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [ZUGFeRD Configuration](../zugferd/configuration.md)
- [ZUGFeRD Field Mapping](../zugferd/README.md)
- [Supported Electronic Documents](./)
