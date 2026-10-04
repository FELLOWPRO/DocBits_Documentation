---
description: ZUGFERD 2.5 elektronische documentondersteuning in DocBits
---

# 🇩🇪 ZUGFERD 2.5

| Eigenschap | Waarde |
|------------|--------|
| **Land / Regio** | Duitsland |
| **Documenttypen** | Factuur, Creditnota |
| **Formaat** | CII (ingesloten in PDF/A-3) of UBL XML |
| **Standaard** | ZUGFeRD 2.5 |
| **Gebaseerd op** | EN 16931 |

ZUGFeRD 2.5 (de gezamenlijke FeRD/FNFE-MPE-publicatie van juni 2026) is equivalent aan Factur-X 1.09. De CII-XML gebruikt de UN/CEFACT-basis D22B, die achterwaarts compatibel is met D16B, waardoor het volledige extractie- en transformatiecontract van ZUGFeRD 2.4 van toepassing blijft. Het EXTENDED-profiel voegt nieuwe velden toe voor betaalmiddelen en BIC, een derde ontvanger (factor) en de reden voor btw-vrijstelling van kortingen/toeslagen.

Alle vijf profielen worden ondersteund: MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) en EXTENDED. DocBits classificeert de CII- en UBL-varianten apart.

## Ondersteuningsstatus

| Component | Status |
|-----------|--------|
| Voorbeeld | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Gerelateerd

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [ZUGFeRD-configuratie](../zugferd/configuration.md)
- [ZUGFeRD veldomapping](../zugferd/README.md)
- [Ondersteunde elektronische documenten](./)
