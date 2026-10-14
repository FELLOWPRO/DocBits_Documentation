---
description: Prise en charge du document électronique FACTURX dans DocBits
---

# 🇫🇷 FACTURX

| Propriété              | Valeur                   |
| ---------------------- | ------------------------ |
| **Pays / Région**      | France / Allemagne       |
| **Types de documents** | Facture, Avoir           |
| **Format**             | CII (intégré en PDF/A-3) |
| **Norme**              | Factur-X                 |
| **Basée sur**          | EN 16931                 |

Factur-X est la mise en œuvre française de la norme de facture hybride franco-allemande. Elle intègre des données XML CII structurées dans un document PDF/A-3, ce qui permet une facturation à la fois lisible par l'humain et exploitable par la machine. DocBits détecte automatiquement la version et le profil de Factur-X à partir du XML intégré.

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
