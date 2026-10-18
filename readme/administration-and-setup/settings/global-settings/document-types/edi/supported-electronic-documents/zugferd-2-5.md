---
description: Prise en charge du document électronique ZUGFERD 2.5 dans DocBits
---

# 🇩🇪 ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Allemagne](countries/germany.md). La syntaxe, la version de publication et le profil sont des choix distincts. Ne déduisez pas une publication Factur-X du marqueur commun 1p0.
{% endhint %}

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | Germany |
| **Types de documents** | Invoice, Credit Note |
| **Format** | CII (PDF/A-3 embedded) or UBL XML |
| **Norme** | ZUGFeRD 2.5 |
| **Basé sur** | EN 16931 |

ZUGFeRD 2.5 (la publication commune FeRD/FNFE-MPE de juin 2026) équivaut à Factur-X 1.09. Son XML CII utilise la base UN/CEFACT D22B, rétrocompatible avec D16B ; le contrat complet d'extraction et de transformation de ZUGFeRD 2.4 continue donc de s'appliquer. Le profil EXTENDED ajoute de nouveaux champs pour les moyens de paiement et le BIC, un bénéficiaire tiers (affactureur) et le motif d'exonération fiscale des remises/frais.

Les cinq profils sont pris en charge : MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) et EXTENDED. DocBits classe séparément les variantes CII et UBL.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Supported |
| Extraction des champs | ✅ Supported |
| Transformation | ✅ Supported |

## Voir aussi

- [Factur-X 1.09 / ZUGFeRD 2.5](facturx-1-09-zugferd-2-5.md)
- [Configuration ZUGFeRD](../zugferd/configuration.md)
- [Correspondance des champs ZUGFeRD](../zugferd/README.md)
- [Documents électroniques pris en charge](./)
