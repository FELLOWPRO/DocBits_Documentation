---
description: Prise en charge du document électronique FATTURAPA dans DocBits
---

# 🇮🇹 FATTURAPA

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [Italie](countries/italy.md). Le libellé de famille ne certifie pas chaque version de FatturaPA ni la transmission via SDI. Vérifiez le schéma source et les exigences du destinataire.
{% endhint %}

| Propriété              | Valeur                                   |
| ---------------------- | ---------------------------------------- |
| **Pays / Région**      | Italie                                   |
| **Types de documents** | Facture, Avoir, Facture simplifiée       |
| **Format**             | XML (FatturaPA 1.2.x)                    |
| **Norme**              | FatturaPA (SDI)                          |

FatturaPA est la norme italienne de facturation électronique imposée par l'Agenzia delle Entrate. Depuis janvier 2019, toutes les factures entre entreprises italiennes doivent être transmises via le Sistema di Interscambio (SDI). DocBits traite les documents XML FatturaPA et en extrait tous les champs d'en-tête et de lignes.

## Statut de prise en charge

| Composant             | Statut           |
| --------------------- | ---------------- |
| Aperçu                | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation        | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/fatturapa-preview.png" alt="Aperçu d'une facture FatturaPA dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'une facture italienne FatturaPA</p></figcaption></figure>

## Voir aussi

* [Documents électroniques pris en charge](./)
