---
description: Prise en charge du document électronique FACTURX dans DocBits
---

# 🇫🇷 FACTURX

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [France](countries/france.md). Le marqueur XML 1p0 et Factur-X XMP Version 1.0 n’identifient pas une version de publication. Conservez le libellé générique lorsque la publication est inconnue.
{% endhint %}

| Propriété              | Valeur                   |
| ---------------------- | ------------------------ |
| **Pays / Région**      | France / Allemagne       |
| **Types de documents** | Facture, Avoir           |
| **Format**             | CII (intégré en PDF/A-3) |
| **Norme**              | Factur-X                 |
| **Basée sur**          | EN 16931                 |

Un Guideline ID CII harmonisé peut identifier une famille et un profil tout en partageant le même marqueur 1p0 entre plusieurs versions. Factur-X XMP Version 1.0 est un marqueur de schéma, et non une publication telle que 1.08 ou 1.09. Les métadonnées XMP de ZUGFeRD peuvent déclarer sa version. En l’absence de métadonnées faisant autorité, conservez le résultat de famille générique et confirmez le fichier d’origine avec l’émetteur.

## Statut de prise en charge

| Composant             | Statut           |
| --------------------- | ---------------- |
| Aperçu                | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation        | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/facturx-preview.png" alt="Aperçu d'une facture Factur-X dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'une facture française Factur-X</p></figcaption></figure>

## Voir aussi

* [Configuration de ZUGFeRD](../zugferd/)
* [Mappage des champs ZUGFeRD](../zugferd/versions/)
* [Documents électroniques pris en charge](./)
