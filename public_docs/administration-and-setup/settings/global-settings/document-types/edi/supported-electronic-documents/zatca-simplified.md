---
description: Prise en charge du document électronique ZATCA SIMPLIFIED dans DocBits
---

# 🇸🇦 ZATCA SIMPLIFIED

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Arabie saoudite](countries/saudi-arabia.md). Ces libellés décrivent des processus et variantes de facture différents. L’analyse du fichier ne prouve ni la signature, ni la validation fiscale, ni la déclaration via ZATCA.
{% endhint %}

| Propriété              | Valeur                       |
| ---------------------- | ---------------------------- |
| **Pays / Région**      | Saudi Arabia                 |
| **Types de documents** | Simplified Tax Invoice       |
| **Format**             | UBL 2.1 XML                  |
| **Norme**              | ZATCA Simplified Tax Invoice |

La facture fiscale simplifiée ZATCA est utilisée pour les transactions B2C en Arabie saoudite dont le montant total (TVA comprise) ne dépasse pas 1 000 SAR. Contrairement aux factures fiscales standard, les factures simplifiées n'exigent pas l'identification de l'acheteur, mais doivent comporter un code QR contenant les informations du vendeur encodées en TLV, le montant de la TVA et l'horodatage.

## Statut de prise en charge

| Composant             | Statut      |
| --------------------- | ----------- |
| Aperçu                | ✅ Supported |
| Extraction des champs | ✅ Supported |
| Transformation        | ✅ Supported |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/zatca-simplified-preview.png" alt="Aperçu de la facture ZATCA Simplified dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture ZATCA Simplified d'Arabie saoudite</p></figcaption></figure>

## Pages liées

* [Documents électroniques pris en charge](./)
