---
description: Ondersteuning voor KSEF FA3 elektronische documenten in DocBits
---

# 🇵🇱 KSEF FA3

<!-- edocs-country-scope -->

{% hint style="info" %}
Raadpleeg de landengids voor versiebeperkingen, de daadwerkelijk gebruikte configuratie en de uitlegvideo voor het land. [Polen](countries/poland.md). FA2 en FA3 gebruiken verschillende structuren. Controleer het bronschema en test de juiste toewijzing; het parseren dient geen factuur in bij KSeF.
{% endhint %}

| Eigenschap           | Waarde                        |
| -------------------- | ----------------------------- |
| **Land / Regio**     | Polen                         |
| **Documenttypen**    | Factuur, Correctiefactuur     |
| **Formaat**          | XML                           |
| **Standaard**        | KSeF FA(3)                    |

KSeF FA3 is de nieuwste schemaversie van het Poolse nationale e-factuursysteem. Het voegt ondersteuning toe voor extra documenttypen, een betere afhandeling van correctiefacturen en bijgewerkte validatieregels die zijn afgestemd op de nieuwste Poolse btw-regelgeving.

## Ondersteuningsstatus

| Component     | Status         |
| ------------- | -------------- |
| Voorbeeld     | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Voorbeeld van een KSeF FA(3)-factuur in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een Poolse KSeF FA(3)-factuur</p></figcaption></figure>

## Gerelateerd

* [Ondersteunde elektronische documenten](./)
