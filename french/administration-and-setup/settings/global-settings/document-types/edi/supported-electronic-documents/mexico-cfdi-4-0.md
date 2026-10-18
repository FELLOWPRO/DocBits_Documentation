---
description: Prise en charge des documents électroniques MEXICO CFDI 4.0 dans DocBits
---

# 🇲🇽 MEXICO CFDI 4.0

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Mexique](countries/mexico.md). Vérifiez l’espace de noms, la version et TipoDeComprobante. Un montant négatif ne suffit pas à identifier un avoir ; l’analyse du fichier ne certifie pas la validation par le SAT.
{% endhint %}

| Propriété | Valeur |
| --------- | ------ |
| **Pays / Région** | Mexique |
| **Types de documents** | Facture, Note de crédit, Reçu de paiement |
| **Format** | XML |
| **Norme** | CFDI 4.0 (Comprobante Fiscal Digital por Internet) |

CFDI 4.0 est la version actuelle de la norme mexicaine de reçu fiscal numérique, obligatoire depuis janvier 2023. Elle exige le nom du destinataire et son régime fiscal (régimen fiscal), ajoute le champ d'exportation et inclut le sceau numérique mis à jour ainsi que la chaîne de certificats du SAT.

## Statut de prise en charge

| Composant | Statut |
| --------- | ------ |
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/mexico-cfdi-4-0-preview.png" alt="Aperçu d'une facture Mexico CFDI 4.0 dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'une facture Mexico CFDI 4.0</p></figcaption></figure>

## Voir aussi

* [Documents électroniques pris en charge](./)
