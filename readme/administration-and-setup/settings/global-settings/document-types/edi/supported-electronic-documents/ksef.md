---
description: Ondersteuning voor KSEF elektronische documenten in DocBits
---

# 🇵🇱 KSEF

<!-- edocs-country-scope -->

{% hint style="info" %}
Raadpleeg de landengids voor versiebeperkingen, de daadwerkelijk gebruikte configuratie en de uitlegvideo voor het land. [Polen](countries/poland.md). FA2 en FA3 gebruiken verschillende structuren. Controleer het bronschema en test de juiste toewijzing; het parseren dient geen factuur in bij KSeF.
{% endhint %}

| Eigenschap           | Waarde                                       |
| -------------------- | -------------------------------------------- |
| **Land / Regio**     | Polen                                        |
| **Documenttypen**    | Factuur, Creditnota, Correctiefactuur        |
| **Formaat**          | XML                                          |
| **Standaard**        | KSeF (Krajowy System e-Faktur)               |

KSeF is het Poolse nationale e-factuursysteem dat wordt beheerd door het Ministerie van Financiën. Het wordt verplicht voor alle Poolse btw-plichtige bedrijven. DocBits ondersteunt de schemaversies KSeF FA2 en FA3 voor de verwerking van facturen.

## Ondersteuningsstatus

| Component     | Status         |
| ------------- | -------------- |
| Voorbeeld     | ✅ Ondersteund |
| Veldextractie | ✅ Ondersteund |
| Transformatie | ✅ Ondersteund |

## Standaardvoorbeeld

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Voorbeeld van een KSeF-factuur in DocBits"><figcaption><p>Standaard DocBits-voorbeeld voor een Poolse KSeF-factuur</p></figcaption></figure>

## Gerelateerd

* [Ondersteunde elektronische documenten](./)
* [KSeF FA2](ksef-fa2.md)
* [KSeF FA3](ksef-fa3.md)
