---
description: Prise en charge du document électronique ZATCA TAX INVOICE dans DocBits
---

# 🇸🇦 ZATCA TAX INVOICE

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Arabie saoudite](countries/saudi-arabia.md). Ces libellés décrivent des processus et variantes de facture différents. L’analyse du fichier ne prouve ni la signature, ni la validation fiscale, ni la déclaration via ZATCA.
{% endhint %}

| Propriété              | Valeur                     |
| ---------------------- | -------------------------- |
| **Pays / Région**      | Saudi Arabia               |
| **Types de documents** | Standard Tax Invoice       |
| **Format**             | UBL 2.1 XML                |
| **Norme**              | ZATCA Standard Tax Invoice |

ZATCA Tax Invoice est le format de facture fiscale B2B standard du système saoudien de facturation électronique. Il exige l'identification complète de l'acheteur et du vendeur (y compris les numéros d'immatriculation à la TVA), des lignes de détail avec calcul de la TVA, et doit être validé (cleared) par la plateforme ZATCA avant d'être transmis à l'acheteur.

## Statut de prise en charge

| Composant             | Statut      |
| --------------------- | ----------- |
| Aperçu                | ✅ Supported |
| Extraction des champs | ✅ Supported |
| Transformation        | ✅ Supported |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/zatca-tax-invoice-preview.png" alt="Aperçu de la facture ZATCA Tax Invoice dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture ZATCA Tax Invoice d'Arabie saoudite</p></figcaption></figure>

## Pages liées

* [Documents électroniques pris en charge](./)
