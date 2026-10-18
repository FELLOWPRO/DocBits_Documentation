---
description: Ondersteuning voor MEXICO CFDI 4.0 elektronische documenten in DocBits
---

# 🇲🇽 MEXICO CFDI 4.0

<!-- edocs-country-scope -->

{% hint style="info" %}
Raadpleeg de landengids voor versiebeperkingen, de daadwerkelijk gebruikte configuratie en de uitlegvideo voor het land. [Mexico](countries/mexico.md). Controleer de naamruimte, versie en TipoDeComprobante. Een creditnota wordt niet alleen door een negatief bedrag geïdentificeerd; het parseren certificeert geen SAT-goedkeuring.
{% endhint %}

| Eigenschap           | Waarde                                             |
| -------------------- | -------------------------------------------------- |
| **Land / Regio**     | Mexico                                             |
| **Documenttypen**    | Factuur, Creditnota, Betalingsbewijs               |
| **Formaat**          | XML                                                |
| **Standaard**        | CFDI 4.0 (Comprobante Fiscal Digital por Internet) |

CFDI 4.0 is de huidige versie van de Mexicaanse standaard voor digitale belastingbewijzen en is verplicht sinds januari 2023. Deze versie vereist de naam van de ontvanger en het belastingregime (régimen fiscal), voegt het exportveld toe en bevat het bijgewerkte digitale zegel en de bijgewerkte SAT-certificaatketen.

## Ondersteuningsstatus

| Component     | Status         |
| ------------- | -------------- |
| Voorbeeld     | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-4-0-preview.png" alt="Voorbeeld van een Mexico CFDI 4.0-factuur in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een Mexico CFDI 4.0-factuur</p></figcaption></figure>

## Gerelateerd

* [Ondersteunde elektronische documenten](./)
