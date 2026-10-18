---
description: Prise en charge du document électronique TURKEY E-FATURA dans DocBits
---

# 🇹🇷 TURKEY E-FATURA

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Turquie](countries/turkey.md). Vérifiez le profil source et la structure du document. Le libellé de famille n’identifie pas chaque version UBL-TR et ne démontre pas la transmission via la plateforme fiscale.
{% endhint %}

| Propriété              | Valeur                                  |
| ---------------------- | --------------------------------------- |
| **Pays / Région**      | Turquie                                 |
| **Types de documents** | Facture, Note de crédit                 |
| **Format**             | UBL-TR 1.2 XML                          |
| **Norme**              | e-Fatura (GİB - Revenue Administration) |

Turkey e-Fatura est la principale norme de facture électronique imposée par la GİB (administration fiscale) pour les transactions B2B entre contribuables enregistrés. Les factures sont échangées via des intégrateurs agréés et la plateforme de la GİB. Le format utilise UBL-TR, la version localisée d'UBL pour la Turquie, avec des champs propres à la Turquie pour l'identification fiscale TCKN/VKN.

## Statut de prise en charge

| Composant             | Statut            |
| --------------------- | ----------------- |
| Aperçu                | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation        | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/turkey-e-fatura-preview.png" alt="Aperçu d'une facture Turkey E-Fatura dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture Turkey E-Fatura</p></figcaption></figure>

## Voir aussi

* [Documents électroniques pris en charge](./)
* [TURKEY E-ARSIV](turkey-e-arsiv.md)
