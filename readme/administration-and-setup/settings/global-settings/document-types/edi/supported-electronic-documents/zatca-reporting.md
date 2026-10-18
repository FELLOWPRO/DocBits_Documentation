---
description: Prise en charge du document électronique ZATCA REPORTING dans DocBits
---

# 🇸🇦 ZATCA REPORTING

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Arabie saoudite](countries/saudi-arabia.md). Ces libellés décrivent des processus et variantes de facture différents. L’analyse du fichier ne prouve ni la signature, ni la validation fiscale, ni la déclaration via ZATCA.
{% endhint %}

| Propriété              | Valeur                                |
| ---------------------- | ------------------------------------- |
| **Pays / Région**      | Saudi Arabia                          |
| **Types de documents** | Reported Invoice                      |
| **Format**             | UBL 2.1 XML                           |
| **Norme**              | ZATCA Reporting (Phase 2 Integration) |

ZATCA Reporting désigne le mode d'intégration de la phase 2, dans lequel les factures fiscales standard sont déclarées à la plateforme ZATCA dans les 24 heures suivant leur émission. La facture déclarée comprend un cachet cryptographique, un code QR et un UUID attribué par le portail Fatoorah de la ZATCA.

## Statut de prise en charge

| Composant             | Statut      |
| --------------------- | ----------- |
| Aperçu                | ✅ Supported |
| Extraction des champs | ✅ Supported |
| Transformation        | ✅ Supported |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/zatca-reporting-preview.png" alt="Aperçu de la facture ZATCA Reporting dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture ZATCA Reporting d'Arabie saoudite</p></figcaption></figure>

## Pages liées

* [Documents électroniques pris en charge](./)
