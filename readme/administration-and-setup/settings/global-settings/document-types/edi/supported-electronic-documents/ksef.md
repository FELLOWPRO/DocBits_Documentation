---
description: Prise en charge des documents électroniques KSEF dans DocBits
---

# 🇵🇱 KSEF

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Pologne](countries/poland.md). FA2 et FA3 utilisent des structures différentes. Confirmez le schéma source et testez la correspondance appropriée ; l’analyse d’une facture ne la soumet pas à KSeF.
{% endhint %}

| Propriété | Valeur |
| --------- | ------ |
| **Pays / Région** | Pologne |
| **Types de documents** | Facture, Note de crédit, Facture rectificative |
| **Format** | XML |
| **Norme** | KSeF (Krajowy System e-Faktur) |

KSeF est le système national polonais de facturation électronique, exploité par le ministère des Finances. Il deviendra obligatoire pour toutes les entreprises polonaises assujetties à la TVA. DocBits prend en charge les versions de schéma KSeF FA2 et FA3 pour le traitement des factures.

## Statut de prise en charge

| Composant | Statut |
| --------- | ------ |
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/ksef-preview.png" alt="Aperçu d'une facture KSeF dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'une facture KSeF de Pologne</p></figcaption></figure>

## Voir aussi

* [Documents électroniques pris en charge](./)
* [KSeF FA2](ksef-fa2.md)
* [KSeF FA3](ksef-fa3.md)
