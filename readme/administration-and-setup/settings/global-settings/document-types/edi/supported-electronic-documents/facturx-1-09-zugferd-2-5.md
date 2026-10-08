---
description: Prise en charge de FACTURX 1.09 - ZUGFERD 2.5 (document électronique) dans DocBits
---

# 🇫🇷 FACTURX 1.09 - ZUGFERD 2.5

| Propriété | Valeur |
|----------|-------|
| **Pays / Région** | France / Allemagne |
| **Types de documents** | Facture, Note de crédit |
| **Format** | CII (PDF/A-3 intégré) |
| **Standard** | Factur-X 1.09 / ZUGFeRD 2.5 |
| **Basé sur** | EN 16931 |

Factur-X 1.09 est la publication française équivalente à ZUGFeRD 2.5 (publication commune FeRD/FNFE-MPE, juin 2026). Son XML CII utilise la base UN/CEFACT D22B, rétrocompatible avec D16B : le contrat complet d'extraction et de transformation de Factur-X 1.08 / ZUGFeRD 2.4 continue donc de s'appliquer. Le profil EXTENDED ajoute de nouveaux champs pour les moyens de paiement et le BIC, un bénéficiaire tiers (affréteur) et le motif d'exonération de taxe des remises/suppléments.

Les cinq profils sont pris en charge : MINIMUM, BASIC WL, BASIC, EN 16931 (COMFORT) et EXTENDED.

## Statut de support

| Composant | Statut |
|-----------|--------|
| Aperçu | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation | ✅ Pris en charge |

## Pages connexes

- [ZUGFeRD 2.5](zugferd-2-5.md)
- [Configuration de ZUGFeRD](../zugferd/configuration.md)
- [Mappage des champs ZUGFeRD](../zugferd/README.md)
- [Documents électroniques pris en charge](./)
