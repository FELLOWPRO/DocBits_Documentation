---
description: Prise en charge des documents électroniques MYINVOIS dans DocBits
---

# 🇲🇾 MYINVOIS

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Malaisie](countries/malaysia.md). Le chemin d’extraction examiné repose sur XML. La plateforme nationale accepte aussi JSON, mais cela ne démontre pas la prise en charge de l’import JSON par cette correspondance DocBits.
{% endhint %}

| Propriété | Valeur |
| --------- | ------ |
| **Pays / Région** | Malaisie |
| **Types de documents** | Facture, Note de crédit, Note de débit, Facture d'autofacturation |
| **Format** | XML UBL 2.1 / JSON |
| **Norme** | MyInvois (LHDN - Lembaga Hasil Dalam Negeri) |

MyInvois est le système de facturation électronique de la Malaisie, exploité par l'administration fiscale (LHDN). En vigueur depuis août 2024 pour les grandes entreprises, il exige que toutes les factures soient soumises au portail MyInvois pour validation et reçoivent un identifiant unique. Le système utilise UBL 2.1 et prend en charge les formats de soumission XML et JSON.

## Statut de prise en charge

| Composant | Statut |
| --------- | ------ |
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/myinvois-preview.png" alt="Aperçu d'une facture MyInvois dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'une facture MyInvois de Malaisie</p></figcaption></figure>

## Voir aussi

* [Documents électroniques pris en charge](./)
