---
description: Prise en charge du document électronique INVOIC02 dans DocBits
---

# INVOIC02

<!-- edocs-country-scope -->

{% hint style="info" %}
Consultez le guide du pays pour connaître les limites de version, la configuration effectivement utilisée et la vidéo explicative du pays. [International](countries/international.md). Les correspondances de facture, de commande, de réponse et d’expédition sont distinctes. Le traitement des fichiers ne fournit pas, à lui seul, de point d’accès Peppol ni de connexion aux partenaires commerciaux.
{% endhint %}

| Propriété              | Valeur                  |
| ---------------------- | ----------------------- |
| **Pays / Région**      | International           |
| **Types de documents** | Facture                 |
| **Format**             | EDIFACT                 |
| **Norme**              | UN/EDIFACT INVOIC D.02B |

INVOIC02 est un message de facture UN/EDIFACT basé sur la version D.02B du répertoire. EDIFACT (Electronic Data Interchange for Administration, Commerce and Transport) est une norme EDI très répandue dans la logistique, le commerce de détail et l'industrie. DocBits analyse la structure des segments EDIFACT et en extrait les champs d'en-tête, de lignes et de totaux.

## Statut de prise en charge

| Composant             | Statut           |
| --------------------- | ---------------- |
| Aperçu                | ✅ Pris en charge |
| Extraction des champs | ✅ Pris en charge |
| Transformation        | ✅ Pris en charge |

## Aperçu par défaut

<figure><img src="../../../../../../.gitbook/assets/invoic02-preview.png" alt="Aperçu d'une facture INVOIC02 dans DocBits"><figcaption><p>Aperçu DocBits par défaut d'une facture INVOIC02</p></figcaption></figure>

## Voir aussi

* [Documents électroniques pris en charge](./)
