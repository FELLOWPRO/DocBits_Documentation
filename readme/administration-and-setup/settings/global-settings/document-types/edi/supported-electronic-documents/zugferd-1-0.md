---
description: Prise en charge du document électronique ZUGFERD 1.0 dans DocBits
---

# 🇩🇪 ZUGFERD 1.0

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Allemagne](countries/germany.md). La syntaxe, la version de publication et le profil sont des choix distincts. Ne déduisez pas une publication Factur-X du marqueur commun 1p0.
{% endhint %}

| Propriété | Valeur |
| -------------------- | ------------------------- |
| **Pays / Région** | Germany |
| **Types de documents** | Invoice, Credit Note |
| **Format** | CII (PDF/A-3 embedded) |
| **Norme** | ZUGFeRD 1.0 |
| **Basé sur** | ZUGFeRD 1.0 specification |

ZUGFeRD 1.0 était la norme allemande originelle de facture hybride, publiée en 2014. Elle intègre un fichier XML CII (ZUGFeRD-invoice.xml) dans un document PDF/A-3. Cette version est antérieure à la norme européenne EN 16931 et utilise son propre système de profils.

## Statut de prise en charge

| Composant | Statut |
| ---------------- | ----------- |
| Aperçu | ✅ Supported |
| Extraction des champs | ✅ Supported |
| Transformation | ✅ Supported |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/zugferd-preview.png" alt="Aperçu d'une facture ZUGFeRD 1.0 dans DocBits"><figcaption><p>Aperçu DocBits par défaut pour une facture ZUGFeRD 1.0 allemande</p></figcaption></figure>

## Voir aussi

* [Configuration ZUGFeRD](../zugferd/)
* [Correspondance des champs ZUGFeRD](../zugferd/README.md)
* [Documents électroniques pris en charge](./)
