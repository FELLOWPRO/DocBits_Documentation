---
description: Ondersteuning voor ZATCA REPORTING elektronisch document in DocBits
---

# 🇸🇦 ZATCA REPORTING

<!-- edocs-country-scope -->

{% hint style="info" %}
Raadpleeg de landengids voor versiebeperkingen, de daadwerkelijk gebruikte configuratie en de uitlegvideo voor het land. [Saoedi-Arabië](countries/saudi-arabia.md). Deze labels beschrijven verschillende processen en factuurvarianten. Het parseren bewijst geen ondertekening, fiscale goedkeuring of rapportage via ZATCA.
{% endhint %}

| Eigenschap           | Waarde                                |
| -------------------- | ------------------------------------- |
| **Land / Regio**     | Saoedi-Arabië                         |
| **Documenttypen**    | Gerapporteerde factuur                |
| **Formaat**          | UBL 2.1 XML                           |
| **Standaard**        | ZATCA Reporting (Phase 2 Integration) |

ZATCA Reporting verwijst naar de integratiemodus van fase 2, waarbij standaard belastingfacturen binnen 24 uur na uitgifte aan het ZATCA-platform worden gerapporteerd. De gerapporteerde factuur bevat een cryptografische stempel, een QR-code en een UUID die door het Fatoorah-portaal van ZATCA wordt toegewezen.

## Ondersteuningsstatus

| Component        | Status       |
| ---------------- | ------------ |
| Voorvertoning    | ✅ Ondersteund |
| Veldextractie    | ✅ Ondersteund |
| Transformatie    | ✅ Ondersteund |

## Standaardvoorvertoning

<figure><img src="../../../../../../.gitbook/assets/zatca-reporting-preview.png" alt="Voorvertoning van ZATCA Reporting-factuur in DocBits"><figcaption><p>Standaard DocBits-voorvertoning voor een Saoedi-Arabische ZATCA Reporting-factuur</p></figcaption></figure>

## Gerelateerd

* [Ondersteunde elektronische documenten](./)
