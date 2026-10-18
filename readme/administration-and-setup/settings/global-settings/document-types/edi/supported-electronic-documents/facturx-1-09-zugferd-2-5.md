---
description: Prise en charge du document électronique FACTURX 1.09 - ZUGFERD 2.5 dans DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [France](countries/france.md). Le marqueur XML 1p0 et Factur-X XMP Version 1.0 n’identifient pas une version de publication. Conservez le libellé générique lorsque la publication est inconnue.
{% endhint %}

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | France / Allemagne |
| **Types de documents** | Facture, Avoir |
| **Format** | CII (intégré en PDF/A-3) |
| **Norme** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Basée sur** | EN 16931 |

Factur-X 1.09 est la publication française équivalente à ZUGFeRD 2.5 (publication commune FeRD/FNFE-MPE, juin 2026). Son XML CII utilise la base UN/CEFACT D22B, rétrocompatible avec D16B ; le contrat complet d'extraction et de transformation de Factur-X 1.08 / ZUGFeRD 2.4 continue donc de s'appliquer. Le profil EXTENDED ajoute de nouveaux champs pour les moyens de paiement et le BIC, un bénéficiaire tiers du paiement (affactureur) et le motif d'exonération fiscale des remises/charges.

Les cinq profils sont pris en charge : MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) et EXTENDED.

## Statut de prise en charge

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Voir aussi

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [Configuration de ZUGFeRD](../zugferd/configuration.md)
- [Mappage des champs ZUGFeRD](../zugferd/README.md)
- [Documents électroniques pris en charge](./)
