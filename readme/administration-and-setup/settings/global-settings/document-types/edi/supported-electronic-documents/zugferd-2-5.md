---
description: ZUGFeRD 2.5 elektronische Dokumentenunterstützung in DocBits
---

# 🇩🇪 ZUGFeRD 2.5

| Eigenschaft | Wert |
|----------|-------|
| **Land / Region** | Deutschland |
| **Dokumenttypen** | Rechnung, Gutschrift |
| **Format** | CII (in PDF/A-3 eingebettet) oder UBL XML |
| **Standard** | ZUGFeRD 2.5 |
| **Basierend auf** | EN 16931 |

ZUGFeRD 2.5 (die gemeinsame Veröffentlichung von FeRD/FNFE-MPE vom Juni 2026) ist gleichwertig mit Factur-X 1.09. Sein CII-XML nutzt die UN/CEFACT-Basis D22B, die abwärtskompatibel zu D16B ist, daher gilt der vollständige Extraktions- und Transformationsvertrag von ZUGFeRD 2.4 weiter. Das Profil EXTENDED ergänzt neue Felder für Zahlungsmittel und BIC, einen Drittempfänger (Faktor) sowie den Steuerbefreiungsgrund für Nachlässe/Zuschläge.

Alle fünf Profile werden unterstützt: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) und EXTENDED. DocBits klassifiziert die CII- und UBL-Varianten getrennt.

## Unterstützungsstatus

| Komponente | Status |
|-----------|--------|
| Vorschau | ✅ Unterstützt |
| Feldextraktion | ✅ Unterstützt |
| Transformation | ✅ Unterstützt |

## Verwandte Seiten

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [ZUGFeRD Konfiguration](../zugferd/configuration.md)
- [ZUGFeRD Feldzuordnung](../zugferd/README.md)
- [Unterstützte elektronische Dokumente](./)
