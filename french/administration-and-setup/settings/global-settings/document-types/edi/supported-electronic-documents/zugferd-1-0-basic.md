---
description: Prise en charge du document électronique ZUGFERD 1.0 BASIC dans DocBits
---

# 🇩🇪 ZUGFERD 1.0 BASIC

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Allemagne](countries/germany.md). La syntaxe, la version de publication et le profil sont des choix distincts. Ne déduisez pas une publication Factur-X du marqueur commun 1p0.
{% endhint %}

| Propriété              | Valeur                     |
| ---------------------- | -------------------------- |
| **Pays / Région**      | Germany                    |
| **Types de documents** | Invoice, Credit Note       |
| **Format**             | CII (PDF/A-3 embedded)     |
| **Norme**              | ZUGFeRD 1.0, Basic profile |
| **Basé sur**           | ZUGFeRD 1.0 specification  |

Le profil Basic de ZUGFeRD 1.0 comprend les champs de facture essentiels, tels que le numéro et la date de facture, le vendeur et l'acheteur, les lignes de détail et les totaux de TVA. Il fournit suffisamment de données structurées pour une comptabilisation automatisée dans la plupart des systèmes ERP.

## Statut de prise en charge

| Composant             | Statut      |
| --------------------- | ----------- |
| Aperçu                | ✅ Supported |
| Extraction des champs | ✅ Supported |
| Transformation        | ✅ Supported |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="Aperçu de la facture ZUGFeRD 1.0 Basic dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture ZUGFeRD 1.0 Basic allemande</p></figcaption></figure>

## Pages liées

* [Configuration ZUGFeRD](../zugferd/)
* [Correspondance des champs ZUGFeRD](../zugferd/versions/)
* [Documents électroniques pris en charge](./)
